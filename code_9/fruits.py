from flask import Flask, jsonify, request

#   Creer l'app
app = Flask(__name__)

# liste des paniers 
#database_names = []
# liste de panier de fruits
database_basket = {}

#liste qui contiendra les paniers perso fait par les clients
database_custom_basket = {}

universal_panier_fruit = [
    {"name":"apple", "color":"green", "from":"Spain"},
    {"name":"banana", "color":"yellow", "from":"Costa Rica"},
    {"name":"strawberry", "color":"red", "from":"France"},
]

database_basket["universalBasket"] = universal_panier_fruit

hiver_panier_fruit = [
    {"name":"kiwi", "color":"green", "from":"China"},
    {"name":"lemon", "color":"yellow", "from":"Russia"},
    {"name":"pear", "color":"green", "from":"Mongolia"}]

database_basket["winterBasket"] = hiver_panier_fruit

ete_panier_fruit = [
    {"name":"raspberry", "color":"red", "from":"Greece"},
    {"name":"watermelon", "color":"red", "from":"Algeria"},
    {"name":"apricot", "color":"yellow", "from":"Spain"}
]

database_basket["summerBasket"]= ete_panier_fruit

printemps_panier_fruit = [
    {"name":"grapefruit", "color":"magenta red", "from":"Barbados"},
    {"name":"lime", "color":"green", "from":"Venezuela"},
    {"name":"plum", "color":"dark red", "from":"Georgia"}
]

database_basket["springBasket"] = printemps_panier_fruit

database_fruit = {}

for basket_name, fruits in database_basket.items():
    for fruit in fruits:
        name = fruit["name"]                 
        database_fruit[name] = fruit         


database_names = list(database_basket.keys())
s = "<br>Vous êtes chez le primeurs, nous proposons une variété de panier. </br>\n"
s1 = "<br>Cette variété peut être récupéré en ajoutant '/offers' au chemin actuelle.</br>\n"
s2 = "<br>Les différents noms de paniers sont : " + str(database_names) + " </br>\n"
s3 = "<br>Liste de tout les fruits que nous utilisons sont recuperable en ajoutant /fruits au chemin actuelle </br>\n"


@app.route("/")

def home():
    
    return s + s1 + s2
# instruction pour consulter les paniers
@app.route("/offers", methods=["GET"])
def show_offer():
    return jsonify([{"name":b_name} for b_name in database_names])

# Affiche panier selon nom
@app.route("/offers/<string:name>", methods=["GET"])
def show_basket(name):
    if not database_basket[name]:
        return "Error aucun panier ne porte ce nom"
    return database_basket[name]

#Affiche la totalité des fruits
@app.route("/fruits", methods=["GET"])
def show_fruits():
    return database_fruit

@app.route("/customs", methods=["GET"])
def show_customs():
    return database_custom_basket

# todo -- Fonctionnalité creer un panier de fruit personnalisé avec suppression/modification 

@app.route("/customs/addCustomBasket", methods=["POST"])
def create_basket():
    new_basket = request.get_json()
    if new_basket[name] in database_custom_basket[name]:
        return "Error un panier portant ce nom existe deja"
    database_custom_basket[new_basket[name]] = new_basket

    return jsonify(new_basket), 201

@app.route("/custom/", methods=["DELETE"])
def remove_basket():
    return


# Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur 
if __name__ == '__main__':
    app.run(debug=True)