from flask import Flask, jsonify, request
    #creation de l'application
app = Flask(__name__)
perso = [{"name":"viego", "rôle":"jungle", "smite":1400},{"name":"brand","rôle":"support","smite":40},{"name":"yi","rôle":"jungle","smite":0}]

@app.route('/perso', methods=['GET'])
def presente_perso():
    return jsonify(perso)

@app.route('/perso', methods=["POST"])
def ajout_perso():
    new_perso = request.get_json()
    new_perso["id"] = len(perso)+1
    perso.append(new_perso)
    return jsonify(perso)
@app.route('/perso/<char:name>', methods=["PUT"])
def maj_perso(name):
    person = next((p for p in perso if p["name"]==name),None)
    if not perso:
        ()
if __name__ == '__main__':
    app.run(debug=True)