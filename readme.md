<h1 align="center">🧩 Assessment State Synchronization System</h1>
<h3 align="center">Module of Online Assessment Platform</h3>

<p align="center">
  <img src="https://img.shields.io/badge/State-Synchronized-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Submission-One%20Time-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Timer-Backend%20Controlled-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Result-Locked-red?style=for-the-badge" />
</p>

---

## 📌 MODULE OVERVIEW

This module ensures **real-time synchronization between frontend and backend** during an online exam.

### 🎯 It maintains:
- 📝 Question State  
- ⏱ Timer State  
- 🔒 Submission State  

---

## 🚀 KEY FEATURES

### 📝 QUESTION STATE SYNC
- Real-time answer saving  
- Prevents data loss  
- Backend storage using API  

---

### ⏱ TIMER STATE SYNC
- Controlled by backend  
- Accurate countdown  
- Auto submission on timeout  

---

### 🔒 SUBMISSION CONTROL
- Only one submission allowed  
- Duplicate submissions blocked  
- Answers locked permanently  

---

### 📊 RESULT SYSTEM
- Score shown instantly  
- ✅ Correct answers highlighted  
- ❌ Wrong answers highlighted  

---

### 🚫 CONSISTENCY CHECKS
- No changes after submission  
- No submission after time ends  
- Results remain unchanged  

---

## 🛠️ TECHNOLOGIES USED

- ⚙️ FastAPI (Python)  
- 🌐 HTML, CSS, JavaScript  
- 🔗 REST APIs  

---

## 🌐 API ENDPOINTS

| Endpoint | Purpose |
|----------|--------|
| `/save-answer` | Save answers |
| `/timer` | Get time |
| `/submit` | Submit exam |
| `/result/{user_id}` | Get result |

---

## ▶️ HOW TO RUN

### 🔹 Install Dependencies
```bash
pip install fastapi uvicorn
```
uvicorn assessment_api:app --reload

