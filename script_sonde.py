#!/bin/usr/python
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

f=os.popen("""sensors | sed -n '/Core /p' | cut -d" " -f1,2,10-11""")
temperature=""
for temp in f:
	temperature+='{},'.format(temp)

D["temperature"]=temperature


# ================================================================================================================================
                                                    # transformation du format dictionnaire au format json
A=json.dumps(D)
print(A)
