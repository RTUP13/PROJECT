#!/usr/bin/python
# coding: utf-8
import markdown
import shelve
import os,subprocess,json,requests
# Importation du framework
from flask import Flask,g,request,jsonify, render_template,redirect, url_for, session, escape
from flask_restful import Resource, Api, reqparse
#Création d'une instance de Flasks
#Serveur :


# Création d'une instance de Flask
app = Flask(__name__)
app.secret_key = os.urandom(12)

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

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Entrée(s) invalide(s)'

        else:
            session['username']=request.form['username']
            return redirect(url_for('mygem'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/MYGEM')
def mygem():
    """ La page d'acceuil MYGEM """
    try:
        redirect(url_for('mygem'))
    except UnboundLocalError:
        redirect(url_for('login'))

    if 'username' in session:
      username = session['username']
    shelf = get_db()
    keys = list(shelf.keys())
    noms = []
    for key in keys:
        noms.append(shelf[key]['identifiant'])
    return render_template( 'MYGEM.html', list_dyna=noms, username=username)


@app.route('/MYGEM/equipements/mod', methods=['GET', 'POST', 'DELETE']) #les methodes(requetes) accepter sont GET and POST
# utilisation de la méthode post pour l'enregistrement d'un nouvel équipement dans la bd
def ajout_equipements():
    if request.method == 'POST':  #Ce block n'est édité que lorsque le formulaire a été remplie
        identifiant = request.form.get('identifiant')
        nom = request.form['nom']
        type = request.form['type']
        ip_controleur = request.form['ip_controleur']

        parser = reqparse.RequestParser()

        parser.add_argument('identifiant', required=True)
        parser.add_argument('nom', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('ip_controleur', required=True)

        # Insertion d'un argument dans l'objet
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifiant']] = args
        return render_template('ajout_equipement.html', result=args)
    if request.method == 'GET':
        shelf = get_db()
        keys = list(shelf.keys())
        equipements = []

        for key in keys:
            equipements.append(shelf[key]['identifiant'])
        return render_template('supprim_equipements.html', equipements=equipements)

@app.route('/MYGEM/equipements/del/<string:identifiant>', methods=['POST', 'GET'])
def supprim_equipements(identifiant):
    shelf = get_db()
    # Si la clé n'existe pas dans la base de donnée, on retourne erreur 404
    if not (identifiant in shelf):
        return """L'équipement {} est introuvable """.format(identifiant),404
    del shelf[identifiant]
    return render_template('supprim_equipements.html',reponse=("Équipement {} à bien été supprimer").format(identifiant))

# @app.route('/MYGEM/formajout/')
# def form_ajout():
#     return render_template('form_ajout.html')

# @app.route('/MYGEM/equipements/del/')
# def form_suppr():
#     return render_template('supprim_equipements.html,')

class ListEquipements(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])
        return {'message':'Réussie', 'data': devices }, 200

@app.errorhandler(KeyError)
def handle_global_error(e):
    shelf = get_db()
    keys = list(shelf.keys())
    for key in keys:
        identifiant=shelf[key]['identifiant']
        nom=shelf[key]['nom']
        type= shelf[key]['type']
        ip= shelf[key]['ip_controleur']
    return render_template('client_absent.html', identifiant=identifiant, nom=nom, type=type, ip=ip)


@app.route('/MYGEM/equipements/<string:identifiant>', methods=['GET']) # Une route vers le résultat des sondes, les méthodes acceptées sont GET
# définition de equipement prend en paramètre l'identifiant renvoyé par le lien dans la liste déroulante
def equipement(identifiant):
    shelf = get_db()
    try :
        ip_controleur=shelf[identifiant]['ip_controleur']
        reponse = requests.get('http://{}:8080/equipements/{}'.format(ip_controleur,identifiant))
    except requests.exceptions.ConnectionError :
        keys = list(shelf.keys())
        details = dict()
        nom=shelf[identifiant]['nom']
        type= shelf[identifiant]['type']
        ip= shelf[identifiant]['ip_controleur']
        return render_template('client_absent.html', identifiant=identifiant, nom=nom, type=type, ip=ip)
    # try:
    #
    #
    # except KeyError:
    #     keys = list(shelf.keys())
    #     details = dict()
    #     nom=shelf[identifiant]['nom']
    #     type= shelf[identifiant]['type']
    #     ip= shelf[identifiant]['ip_controleur']
    #     return render_template('client_absent.html', identifiant=identifiant, nom=nom, type=type, ip=ip)

    reponse = reponse.json()
    nom = shelf[identifiant]['nom']
    nom_utilisateur = reponse['data']['nom_utilisateur']
    temperature = reponse['data']['temperature']
    memoire = reponse['data']['TailleDispo']
    temps_connexion = reponse['data']['TempsAllumage']
    return render_template('fiche_machine.html', nom_utilisateur=nom_utilisateur, temperature=temperature, memoire=memoire, temps_connexion=temps_connexion, nom=nom, identifiant=identifiant)

@app.route('/MYGEM/equipements/') # Une route vers le détails de tout les équipements enregistré,
def listequipement():
     shelf = get_db()
     keys = list(shelf.keys())
     details = dict()
     for key in keys:
         details[key] = dict()
         details[key]['identifiant'] = shelf[key]['identifiant']
         details[key]['nom']= shelf[key]['nom']
         details[key]['type']= shelf[key]['type']
         details[key]['ip'] = shelf[key]['ip_controleur']
     return render_template("detail_equipement.html", details=details), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
