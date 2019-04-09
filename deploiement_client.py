#!/usr/bin/python
# -- coding: utf-8 --

import shelve
import os,subprocess,json

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.connect(('<broadcast>', 0))
address, port = s.getsockname()

identifiant = str()
identifiant = input("Entrez un identifiant : ")

client = str()
client = """#!/usr/bin/python
# -- coding: utf-8 --

import shelve
import os,subprocess,json

# Importation du framework
from flask import Flask,g,request,jsonify

app = Flask(__name__)

identifiants = {'id_name' : '"""+str(identifiant)+"""'}
@app.route('/equipements/<string:id_name>', methods=['GET'])
def getone(id_name):
    if not (id_name == identifiants['id_name']):
        return jsonify({'message':'Equipement introuvable: id_name', 'data': {}}),404
    information = subprocess.check_output(['python', '$chemin/sondes.py'])
    inform = information.decode("utf-8")
    inform = json.loads(inform)
    return jsonify({'identifiant': id_name, 'data' : inform})
if __name__ == '__main__':
    app.run(debug=True, host='"""+str(address)+"""' ,port=10000) #Lancement de l'application dur le port 10000 en mode debug."""

fichier = open("client.py", "a")
fichier.write(client)

sondes = """#!/bin/usr/python
# coding : utf-8
import os
import json
import sys
D=dict()
#=================================================================================================================================
                                                    #Nom d'utilisateur
f=os.popen('whoami')
D["nom_utilisateur"]=f.readline().strip()
# ================================================================================================================================
                                                    #Temps de connexion
f=os.popen('uptime | cut -d"," -f1-2 | cut -d"p" -f2')
D["TempsAllumage"]=f.readline().strip()
#================================================================================================================================
                                                    #Memoire restante
f=os.popen("cat /proc/meminfo | sed -n '/MemFree/p' | awk '{print $2,$3}'")
D["TailleDispo"]=f.readline().strip()
# =================================================================================================================================
                                                  #Temperature CPU
f=os.popen("sensors | sed -n '/Core /p' | cut -d' ' -f1,2,10-11")
temperature=""
for temp in f:
	temperature+='{},'.format(temp)
D["temperature"]=temperature
# =================================================================================================================================
						#Charge CPU
f=os.popen('cat /proc/loadavg | cut -d" " -f1')
D["ChargeCPU"]=f.readline().strip()
# =================================================================================================================================
						#Nombre process
f=os.popen('cat /proc/loadavg | cut -d" " -f4')
D["NbProcess"]=f.readline().strip()
# ================================================================================================================================
                                                    # transformation du format dictionnaire au format json
A=json.dumps(D)
print(A)"""

fichier = open("sondes.py", "a")
fichier.write(sondes)
