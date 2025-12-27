# ML React Calculator 🔢🤖

A small beginner-friendly project demonstrating **end-to-end integration** of:

- React (Frontend)
- Node.js + Express (Backend)
- Python + Flask (ML Service)

The application takes **user input numbers**, sends them through a **Node.js API** to a **Python ML service**, performs an operation, and returns the result to the React UI.

---

## 📁 Project Structure

ml-react/
├── ml/ # Python ML service (Flask)
│ ├── app.py
│ └── venv/ # (ignored in git)
│
├── backend/ # Node.js backend (Express)
│ └── server.js
│
├── frontend/ # React frontend
│ └── src/
│ └── App.js
│
├── .gitignore
└── README.md

yaml
Copy code

---

## 🚀 Features

- User inputs numbers dynamically (no predefined values)
- Select operation: Add / Subtract / Multiply
- Backend-to-ML communication using REST APIs
- Clean separation of frontend, backend, and ML logic
- Beginner-friendly project structure

---

## 🧠 Architecture Overview

React Frontend
↓ (HTTP POST)
Node.js Backend
↓ (HTTP POST)
Python ML Service (Flask)
↓
Result returned to React UI

yaml
Copy code

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- **Python 3.8+**
- **Node.js 16+**
- **npm**
- **Git**
Check versions:
```bash
python --version
node --version
npm --version
git --version


▶️ How to Run the Project
Terminal 1
cd ml
venv\Scripts\activate
python app.py

Terminal 2
cd backend
node server.js

Terminal 3
cd frontend
npm start

