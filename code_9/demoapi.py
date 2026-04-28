from flask import Flask, jsonify, request

#Creer l'application Flask
app = Flask(__name__)

# Une liste d'étudiants
students = [
    {"id":1, "name":"Youcef", "age":21},
    {"id":2, "name":"Samir", "age":41},
    ]
print(students)
#Racine de l'API pour tester si le serveur fonctionne ....
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants !"

# Endpoint pour lister tout les étudiants ....
@app.route('/students', methods=['GET'])
# Methode HTTP Get qui permet de retourner la liste des étudiants 
def get_students():
    "jsonif transforme la liste students en json"
    return jsonify(students)

# Ajouter un étudiant (Post)
@app.route("/students", methods=["POST"])
def add_student():
    new_student=request.get_json()

# recupere les données envoyé par le client
    new_student["id"]=len(students)+1

# attribue un numéro de manière incrémentable
    students.append(new_student)
    return jsonify(new_student), 201 #201 pour indiquer la réussite de la creation

# Supprimer un étudiant (DELETE)
@app.route("/students", methods=["DELETE"])
def remove_student():
    r_student = request.get_json()
    if not r_student or "name" not in r_student:
        return jsonify({"error": "Expected JSON: {\"name\": \"...\"}"}), 400

    name = r_student["name"]

    # supprime tous les étudiants qui matchent ce nom
    before = len(students)
    students[:] = [s for s in students if s.get("name") != name]
    deleted = before - len(students)

    if deleted == 0:
        return jsonify({"message": "Student not found", "name": name}), 404

    return jsonify({"message": "Deleted", "name": name, "deleted": deleted}), 201

# Retourne l'étudiant dont l'id est passé en parametre ....
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
# student = next((s for s in students if s["id"]==id), None)
    student = None
    for s in students:
        if s["id"] == id:
            student = s
        
    if student:
        return jsonify(student)
    return jsonify({"erreur":"l'étudiant n'existe pas !"}), 404

# Mettre à jour un étudiant PUT

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = next((s for s in students if s["id"]==id), None)
    if not student:
        return jsonify({"message":"Etudiant non trouvé !"}), 404

    data=request.get_json()
    data.pop("id", None)
    student.update(data) # Mise à jour des données
    return jsonify(student)



# Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur 
if __name__ == '__main__':
    app.run(debug=True)