                                                      #Mémoire restante

#!/bin/usr/python

import os
import json
import sys

D=dict()

f=os.popen('free -m | head -n2 | tail -n1 | cut -d" " -f20')
D["TailleDispo"]=f.readline().strip()

A=json.dumps(D)
print(A)

=================================================================================================================================
                                                    #Nom d'utilisateur
#!/bin/usr/python

import os
import json
import sys

D=dict()

f=os.popen('whoami')
D["nom_utilisateur"]=f.readline().strip()

A=json.dumps(D)
print(A)         

=================================================================================================================================
                                                  #Température CPU 
 #!/bin/usr/python

import os
import json
import sys

D=dict()
f=os.popen("""sensors | sed -n '/Core /p' | cut -d" " -f1,2,10""")
temperature=""
for temp in f: 
	temperature+='{},'.format(temp)

D["temperature"]=temperature

A=json.dumps(D)
print(A)

================================================================================================================================
                                                    #Temps de connexion
#!/bin/usr/python

import os
import json
import sys

D=dict()

f=os.popen('uptime | cut -d" " -f4')
f=os.popen('uptime | cut -d" " -f5 | cut -d"," -f1')
D["TempsAllumage"]=f.readline().strip()

A=json.dumps(D)
print(A)



