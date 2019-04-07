#!/usr/bin/python
# -- coding: utf-8 --
#import markdown
import shelve
import os,subprocess,json

# Importation du framework
from flask import Flask,g,request,jsonify
#from flask_restful import Resource, Api, reqparse
app = Flask(__name__)

# Création de l'API
#api = Api(app)

identifiants = {'id_name' : 'Moustapha'}

@app.route('/equipements/<string:id_name>', methods=['GET'])
def getone(id_name):
    if not (id_name == identifiants['id_name']):
        return jsonify({'message':'Equipement introuvable: id_name', 'data': {}}),404
    information = subprocess.check_output(['python', '/home/spirit/Desktop/Projet_appli_info/client/scripts/script_sonde.py'])
    inform = information.decode("utf-8")
    inform = json.loads(inform)
    return jsonify({'identifiant': id_name, 'data' : inform})

if __name__ == '__main__':
    app.run(debug=True, host='192.168.248.13', port=8080) #run app on port 8080 in debug mode
