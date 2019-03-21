#!/bin/usr/python

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

# ================================================================================================================================
                                                    #Mémoire restante


f=os.popen('free -m | head -n2 | tail -n1 | cut -d" " -f20')
D["TailleDispo"]=f.readline().strip()


# =================================================================================================================================
                                                  #Température CPU

f=os.popen("""sensors | sed -n '/Core /p' | cut -d" " -f1,2,10""")
temperature=""
for temp in f:
	temperature+='{},'.format(temp)

D["temperature"]=temperature


# ================================================================================================================================
                                                    # transformation du format dictionnaire au format json
A=json.dumps(D)
print(A)
