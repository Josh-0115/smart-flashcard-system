# 🧠 Smart Flashcard System Backend

This is a Flask-based backend application for a smart flashcard system that allows students to add flashcards without specifying the subject. The system uses rule-based inference to automatically classify each flashcard into a subject based on its content. It also provides an API to retrieve a mixed batch of flashcards from different subjects for efficient revision.

---

## 📘 Features

- 🔍 **Subject Inference**: Automatically detects the subject of each flashcard using keyword-based rules.
- 📥 **Add Flashcards**: Simple API to submit flashcards with a question and answer.
- 📤 **Retrieve Flashcards**: Get a shuffled mix of flashcards from different subjects for a specific student.
- 🗃️ **SQLite Database**: All data is stored locally in a lightweight database.

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/Josh-0115/smart-flashcard-system.git
cd smart-flashcard-system
Create a Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Dependencies

pip install -r requirements.txt
Run the Flask App

python app.py
The server will run at http://127.0.0.1:5000/

📡 API Endpoints
➕ Add a Flashcard
POST /flashcard

Request

{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}

Response

{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}

🎲 Get Flashcards by Mixed Subjects
GET /get-subject?student_id=stu001&limit=5

Sample Response

[
  {
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]

📝 Notes
Subject classification is rule-based (e.g., "photosynthesis" → "Biology").

The app supports multiple students by using the student_id.

Data is stored in flashcards.db using SQLite.

📬 Contact
For any issues or suggestions, feel free to raise an issue or contact the maintainer.

---

Let me know if you’d like this in `.md` format as a downloadable file or help with deployment.







