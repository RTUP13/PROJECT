# MY GEM Monitoring system 
## Presentation 
MYGEM is a monitoring system created by 5 second year students preparing a DUT Réseaux et Télécoms at IUT de Villetaneuse. 
The aim of the project was to learn how monitoring systems work and implemented the knowledge we acquired from our school courses. 
Different programming languages were used. The programming languages used for the creation of the app : 
Python :
The project greatyly depends on python and the implementation of it's web oriented modules. The server was mainly coded using flask 

, HTML5, CSS3, Bash  
All responses will have the form

## Base de données des équipements du réseau

# Utilisation
### Récupération des hôtes présent dans la base de données.
Les réponses seront de la forme suivante

```JSON
{
  "Machine" : "Nom de la machine",
  "nom": "Machine Mahine",
  "type" : "pc_bureau",
  "ip_controleur" : "192.168.0.2"
}
```  
## Liste des équipements surveillés
**Définition:**

`GET /equipements`

**Réponse:**

- `200 OK`  Requête réussie

```JSON
[ {
  "identifiant" : "Machine 1",
  "nom": "Machine Mahine",
  "type" : "pc_bureau",
  "ip_controleur" : "192.168.0.2"
}
{
  "identifiant" : "Machine 2",
  "nom": "Machine Hugo ",
  "type" : "pc_bureau",
  "ip_controleur" : "192.168.0.3"
  }
]
```
## Inscription d'un nouvel équipement dans la base
**Définition:**

`POST /equipements`

**Arguments:**

- `"identifiant" : string`  Un identifiant unique pour la machine
- `"nom": string`  Le nom commun de la machine
- `"type" : string`  Le type d'équipement
- `"ip_controlleur" : string`  L'adresse IP à utiliser pour controller l'équipement.

Si l'équipement existe déjà, ses informations seront écrasées

- `201 Créer`  Requête réussie

```JSON
{
  "identifiant": "Machine 2",
  "nom": "Machine Hugo ",
  "type": "pc_bureau",
  "ip_controleur": "192.168.0.3"
}
```

## Vérifie les détails de l'équipement

`GET /equipements/<identifiant>`

**Réponse:**

- `404 Not Found`  L'équipement n'existe pas
- `200 OK`  Requête réussie

```JSON
{
  "identifiant" : "Machine 2",
  "nom": "Machine Hugo",
  "type" : "pc_bureau",
  "ip_controleur" : "192.168.0.3"
}
```
## Suppression d'un équipement de la base de données

**Définition**

`DELETE /equipements/<identifiant>`

**Réponses**

- `404 Not Found`  L'équipement n'existe pas
- `204 OK` Pas de contenu (Contenu supprimer)

## Remonté des informations entre le client et le serveur
Les réponses seront de la forme suivante

```JSON
{
  "identfiant" : "Machine 2",
  "data" : {
  "nom_utilisateur": "Mahine",
  "Mémoire libre en Go" : " 4012 Go",
  "Température du CPU en dégrés" : "41°C",
  "Temps écoulé depuis le dernier arrêt en secondes" : "16:55"}

}
```  
### Donner remplie dans la base de données.
```JSON
{
  "identifiant": "Machine 2",
  "nom_utilisateur": "Mahine",
  "température": "21°C",
  "temps_connexion": "16:55",
  "memoire" : "4012 Go",
}
```
