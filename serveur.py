#!/usr/bin/python
# coding: utf-8
#import markdown
import shelve
import os,subprocess,json,requests
# Importation du framework
from flask import Flask,g,request,jsonify, render_template
from flask_restful import Resource, Api, reqparse
#Création d'une instance de Flasks
#Serveur :


# Création d'une instance de Flask
app = Flask(__name__)

# Création de l'API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("equipements.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    """" La documentation du protocole """
    # Ouverture du fichier README.md
    with open(os.path.dirname(app.root_path) + '/README.md','r') as markdown_file:
        # Lecture du contenu du readme
        content = markdown_file.read()

        # Conversion en HTML
        return markdown.markdown(content)

@app.route('/<string:page_name>/')
def render_static(page_name):
    """ La page d'acceuil MYGEM """
    return render_template( '{page}.html'.format(page=page_name))
# @app.route('/MYGEM/<string:page_name>/')
# def render_static(page_name):
#     """ Les pages des machines """
#     return render_template( '{page}.html'.format(page=page_name),)

class ListEquipements(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])
        return {'message':'Réussie', 'data': devices }, 200

# utilisation de la méthode post pour l'enregistrement d'un nouvel équipement dans la bd
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifiant', required=True)
        parser.add_argument('nom', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('ip_controleur', required=True)


        # Insertion d'un argument dans l'objet
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifiant']] = args
        return {'message':'Equipement enregistré', 'data': args }, 201

class Equipement(Resource):
    def get(self,identifiant):
        shelf = get_db()

        # Si la clé n'existe pas dans la base de donnée, on retourne erreur 404
        if not (identifiant in shelf):
            return {'message':'Equipement introuvable', 'data': {}}, 404
        return {'message':'Equipement trouvé', 'data': shelf[identifiant] }, 200

    def delete(self,identifiant):
        shelf = get_db()

        # Si la clé n'existe pas dans la base de donnée, on retourne erreur 404
        if not (identifiant in shelf):
            return {'message':'Equipement introuvable', 'data': {}}, 404
        del shelf[identifiant]
        return {'message':'Equipement supprimer'},204

#@app.route('/equipements/Machine1')
class ResultSonde(Resource):
    def get(self,identifiant):
        data = {"identifiant":identifiant}
        reponse = requests.get('http://127.0.0.1:8080/equipements/', data = data)
        reponse = reponse.json()

        nom_utilisateur = reponse['data']['nom_utilisateur']
        temperature = reponse['data']['temperature']
        memoire = reponse['data']['TailleDispo']
        temps_connexion = reponse['data']['TempsAllumage']
        return render_template('fiche_machine.html', nom_utilisateur=nom_utilisateur, temperature=temperature, memoire=memoire, temps_connexion=temps_connexion)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

api.add_resource(ListEquipements,'/MYGEM/equipements')
api.add_resource(Equipement,'/MYGEM/equipements/<string:identifiant>/details')
api.add_resource(ResultSonde,'/MYGEM/equipements/<string:identifiant>')

#A l'aide d'une template html :
