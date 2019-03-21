#Serveur :

#! /usr/bin/python
# -*- coding:utf-8 -*-

import json, requests

reponse = requests.get('http://192.168.200.9:8080/equipements/Machine2')
reponse = reponse.json()

nom_utilisateur = reponse['data']['nom_utilisateur']
temperature = reponse['data']['temperature']
memoire = reponse['data']['TailleDispo']
temps_connexion = reponse['data']['TempsAllumage']

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fiche():
    return render_template('machine2.html', nom_utilisateur=nom_utilisateur, temperature=temperature, memoire=memoire, temps_connexion=temps_connexion)

if __name__ == '__main__':
    app.run(debug=True)

#A l'aide d'une template html :

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
    <link rel="stylesheet" href="{{ url_for('static', filename='css/machine2.css')}}" />
        <title>My Gem : Fiche de supervision</title>
    </head>

    <body>
    <center><p><b> My Gem </b></p></center>
    <hr>
    <center><p><i>Fiche de supervision de la machine 1</i></p><br></center>
    <p></p>
    <center>
    <table>
            <thead>
                <tr>
                    <th colspan="2">Nom de la machine : {{nom_utilisateur}} </th>
                </tr>
            </thead>
                <tbody>
                    <tr>
                            <td>Temp&eacute;rature du CPU en degr&eacute;s </td>
                            <td>{{temperature}}</td>
                </tr>
                    <td>M&eacute;moire libre en Mo </td>
                            <td>{{memoire}}</td>
                    </tr>
                    <td>Temps &eacute;coul&eacute; depuis le dernier arr&ecirc;t en secondes  </td>
                            <td>{{temps_connexion}}</td>
                </tr>
               </tbody>
    </table>
    <br>
    </center>
    <hr>
    <center><img
                src="/home/student/905/11701053/Documents/TemplateHTML/exterieur-iutv.jpg"
             alt=""
             height="500px"
             width="800px"
    /></center>
    <!-- <form method="get" action="URL">-->
    <!-- </form>-->
    </body>
</html>

