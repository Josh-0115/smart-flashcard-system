from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# In-memory storage for flashcards
flashcards = []

# Simple rule-based subject inference
def infer_subject(question):
    keywords = {
        "Physics": ["force", "mass", "acceleration", "Newton", "gravity"],
        "Biology": ["photosynthesis", "cell", "organism", "plant", "animal"],
        "Mathematics": ["addition", "subtraction", "multiplication", "division", "algebra"],
        "Chemistry": ["atom", "molecule", "reaction", "element", "compound"]
    }
    
    question_lower = question.lower()
    for subject, words in keywords.items():
        if any(word in question_lower for word in words):
            return subject
    return "General Knowledge"

@app.route('/flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    student_id = data.get("student_id")
    question = data.get("question")
    answer = data.get("answer")
    
    subject = infer_subject(question)
    
    flashcard = {
        "student_id": student_id,
        "question": question,
        "answer": answer,
        "subject": subject
    }
    
    flashcards.append(flashcard)
    
    return jsonify({
        "message": "Flashcard added successfully",
        "subject": subject
    })

@app.route('/get-subject', methods=['GET'])
def get_flashcards():
    student_id = request.args.get("student_id")
    limit = int(request.args.get("limit", 5))
    
    student_flashcards = [fc for fc in flashcards if fc["student_id"] == student_id]
    random.shuffle(student_flashcards)
    
    return jsonify(student_flashcards[:limit])

if __name__ == '__main__':
    app.run(debug=True)
