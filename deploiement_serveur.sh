cd PROJECT

mkdir templates
mkdir -p static/css
mkdir -p static/js

mv MYGEM.css fiche_machine.css static/css/

mv MYGEM.html ajout_equipements.html detail_equipement.html fiche_machine.html forme_ajout.html login.html logo.png client_absent.html supprim_equipements.html templates/

mv fonction.js static/js
mv logo.png static/images/

python deploiement_client.py

host=`sudo ifconfig | grep 192 | cut -d"t" -f2 | cut -d"n" -f1`

echo "Entrez votre mot de passe système"
read -s password

echo -e "$password\n" | sudo -S apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate

pip install flask requests flask_restful markdown

chmod +x -R ~/PROJECT
export FLASK_APP=serveur.py
flask run -h $host -p 10000
