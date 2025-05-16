# Smart Flashcard System Backend

This is a Flask-based backend server for a smart flashcard system. It allows users to add flashcards with automatic subject inference, and retrieve flashcards mixed by subject for a specific student.

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
