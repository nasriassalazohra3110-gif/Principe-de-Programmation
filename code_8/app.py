from flask import Flask, jsonify, request
import repository

app = Flask(__name__)

@app.route('/')
def home():
    return " Bon REST!"

@app.route('/students', methods=['GET'])
def get_students():
    students = repository.get_all_students()
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = repository.get_student_by_id(student_id)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200

if __name__ == '__main__':
    # Force Flask à écouter sur toutes les interfaces (IPv4 + IPv6)
    app.run(host="0.0.0.0", port=5002, debug=True)