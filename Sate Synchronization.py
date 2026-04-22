from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
import threading

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage
answers_db = {}
final_submissions = {}   # 🔒 Locked answers
submitted_users = set()

# Lock
submission_lock = threading.Lock()

# Timer
start_time = datetime.now()
end_time = start_time + timedelta(minutes=30)

# Models
class Answer(BaseModel):
    user_id: int
    question_id: int
    answer: str

class Submit(BaseModel):
    user_id: int
    answers: dict

# ✅ Save Answer
@app.post("/save-answer")
def save_answer(data: Answer):

    if data.user_id in submitted_users:
        return {"message": "Submission locked. Cannot change answers."}

    if datetime.now() > end_time:
        return {"message": "Time Over"}

    if data.user_id not in answers_db:
        answers_db[data.user_id] = {}

    answers_db[data.user_id][data.question_id] = data.answer
    return {"message": "Answer saved"}

# ✅ Timer
@app.get("/timer")
def get_timer():
    remaining = int((end_time - datetime.now()).total_seconds())
    if remaining < 0:
        remaining = 0
    return {"remaining_time": remaining}

# ✅ Submit (ONE TIME ONLY)
@app.post("/submit")
def submit_exam(data: Submit):

    print("🚀 SUBMIT CALLED")

    with submission_lock:

        if data.user_id in submitted_users:
            print("⚠️ Duplicate blocked")
            return {"message": "Already submitted"}

        if datetime.now() > end_time:
            return {"message": "Time Over"}

        # 🔒 LOCK FINAL ANSWERS
        final_submissions[data.user_id] = data.answers.copy()
        submitted_users.add(data.user_id)

        print("✅ Final submission stored")

    return {"message": "Submitted successfully"}

# ✅ Get result (locked)
@app.get("/result/{user_id}")
def get_result(user_id: int):
    if user_id not in final_submissions:
        return {"message": "No submission found"}

    return {
        "answers": final_submissions[user_id]
    }

# ✅ Reset (for testing)
@app.get("/reset")
def reset():
    answers_db.clear()
    final_submissions.clear()
    submitted_users.clear()
    return {"message": "Reset done"}
