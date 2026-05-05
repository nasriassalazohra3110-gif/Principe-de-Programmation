from flask import Flask, jsonify, request
#creer l'app Flask
app = Flask(__name__)
#une liste d'etudiants
students = [
    {"id":1,"name":"youcef","age":21},
    {"id":2,"name":"Mathura","age":25},
]
#Racine de l'API pour tester si le serveur connection
@app.route('/')
def home():
    return "Bienvenue dans l'API de gestion des étudiants!"

# Endpoint pour lister tous les étudiants...•
@app.route('/students', methods= ['GET'] )
# Méthode HTTP Get qui permet de retourner la liste des étudiants
def get_students():
    """jsonif transforme la liste students en json"""
    return jsonify(students)

# Ajouter un étudiant (POST)
@app.route('/students', methods= ['POST'])
def add_student() :
    new_student=request.get_json()
    #Pour récupérer les données envoyé par le client
    new_student['id']=len(students)+1
    #Attribuer un numéro de manière incrémentable
    students.append(new_student)
    return jsonify(new_student), 201
# Le code 201 pour dire création réussie .••.
#func pour delete
"""def del_student():
    student=request.get_json()"""

# Afficher un étudiant sachant son identifiant ....
@app.route('/students/<int:id>', methods=['GET'])
def get_student (id):
    student = next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify ({"erreur":"l'étudiant n'existe pas !"}), 404

# Mettre un jour un étudiant PUT

@app.route('/students/<int:id>', methods= ['PUT'])
def update_student (id):
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify ({"message":"Etudiant non trouvé !"}), 404
    data=request.get_json()
    student.update(data) # Mise à jour des données
    return jsonify (student)
#Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur
if __name__ == '__main__':
    app.run(debug=True)