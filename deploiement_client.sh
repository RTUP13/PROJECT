python deploiement_client.py

host=`sudo ifconfig | grep 192 | cut -d"t" -f2 | cut -d"n" -f1`

echo "Entrez votre mot de passe système"
read -s password

echo -e "$password\n" | sudo -S apt-get install -y python3-venv
python3 -m venv venv
source venv/bin/activate 
touch client.py sondes.py

pip install flask requests

chmod +x client.py sondes.py
export FLASK_APP=client.py
flask run -h $host -p 10000
