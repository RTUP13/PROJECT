# PROJECT
Projet d'application

Plusieurs taches à réaliser :

Gestion de projet - Mahine 

Serveur - Moustapha Mahine

Sonde | JSON  - Yann Hugo

Protocole RTNP  - Noé Moustapha Yann Hugo

Interface graphique - HTML/CSS à voir à la fin
# Base de données des équipements du réseau

## Utilisation
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

`GET /equipements/<identifiant>/details`

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

# Protocole (Veuillez bien prendre en considération de ce format lorsque vous codez)

## Remonté des informations entre le client et le serveur

**Définition**

`GET /equipements/<identifiant>`

**Réponses**

Les réponses seront de la forme suivante

```JSON
{
  "identfiant" : "Machine 2",
  "data" : 
  {
  "nom_utilisateur": "Mahine",
  "Température du CPU en dégrés" : "41°C",
  "Temps écoulé depuis le dernier arrêt en secondes" : "16:55",
  "Mémoire libre en Go" : " 4012 Go",
  }
}
```  
### Donner remplie dans la base de données.
```JSON
{
  "identfiant" : "Machine 2",
  "data" : 
  {
  "nom_utilisateur": "Mahine",
  "Température du CPU en dégrés" : "41°C",
  "Temps écoulé depuis le dernier arrêt en secondes" : "16:55",
  "Mémoire libre en Go" : " 4012 Go",
  }
}
```
