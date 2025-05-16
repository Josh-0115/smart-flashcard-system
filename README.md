# 🧠 Smart Flashcard System Backend

This is a Flask-based backend server for a smart flashcard system. It allows users to add flashcards with automatic subject inference and retrieve flashcards mixed by subject for a specific student.

## Features

- Add flashcards via POST `/flashcard` with automatic subject detection.
- Retrieve a mixed batch of flashcards by student via GET `/get-subject`.

## API Endpoints

### Add Flashcard

**POST** `/flashcard`

Request JSON body example:

```json
{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}

```
Response example:
```
{
  "message": "Flashcard added successfully",
  "subject": "Physics"
}
```
Get Flashcards by Mixed Subjects
GET /get-subject?student_id=stu001&limit=5

Query Parameters:

student_id (required): The student ID to retrieve flashcards for.
limit (optional, default 5): Maximum number of flashcards to return.
Response example:
```
[
  {
    "student_id": "stu001",
    "question": "What is Newton's Second Law?",
    "answer": "Force equals mass times acceleration",
    "subject": "Physics"
  },
  {
    "student_id": "stu001",
    "question": "What is photosynthesis?",
    "answer": "A process used by plants to convert light into energy",
    "subject": "Biology"
  }
]
```
Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/smart-flashcard-system.git
cd smart-flashcard-system
```
2. Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```
pip install flask
```
4. Run the application:
```
python app.py
```
The server will start at `http://127.0.0.1:5000`.

Testing the API
You can use curl or any API client like Postman.

Add flashcard example:
```
curl -X POST http://127.0.0.1:5000/flashcard -H "Content-Type: application/json" -d '{"student_id":"stu001","question":"What is photosynthesis?","answer":"A process used by plants to convert light into energy"}'
```
Retrieve flashcards example:
```
curl "http://127.0.0.1:5000/get-subject?student_id=stu001&limit=5"
```














