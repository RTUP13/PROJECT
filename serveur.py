#!/usr/bin/python
# coding: utf-8
import markdown
import shelve
import os,subprocess,json
# Importation du framework
from flask import Flask,g,request,jsonify
from flask_restful import Resource, Api, reqparse
#Création d'une instance de Flasks

app = Flask(__name__)


# PORT = 8888
# server_address = ("", PORT)

@app.route('/acceuil')
def acceuil():
    with open(os.path.dirname(app.root_path) + '/Projet_appli_info/acceuil.py','r') as page_acceuil:
        return (page_acceuil.read())

if __name__ == '__main__':
    app.run(debug=True, port=8888) #run app on port 8080 in debug mode
# handler = http.server
# handler.cgi_directories = ["/"]
# print("Serveur actif sur le port :", PORT)
#
# httpd = server(server_address, handler)
# httpd.serve_forever()
