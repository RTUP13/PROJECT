MYGEM

For this monitoring application to work, the deployment of a program is required on the clients.

This guide will show you the steps required for this deployment.

First of all, MYGEM only works on linux distribution. Indeed, bash commands are used to probe the machine to be supervised. 
You need to know your system password.

The application will install into a virtual environment.
It use the micro framework Flask that provides tools, libraries and technologies to build a web application.

You must have version 3 of Python :

sudo apt-get install python3

We will also need the standard Python package manager Pip to install and manage additional packages that are not part of the 
Python standard library :

sudo apt-get install python3-pip

Below are the commands to deploy the application :

git clone --single-branch --branch mygem_client https://github.com/RTUP13/PROJECT.git

cd PROJECT

The first command is used to import the client branch on github which will be copied to the Project directory in which we enters
thanks to the second command.

./deploiement_client.sh

Then we execute a deployment script with the last command. During the installation it will be necessary to enter the system 
password and an identifier that will have to be mentioned on the application when adding a machine.

And that's all ! The client is installed and ready. 

Thank you for reporting any problem you may have encountered at the following address: applicationrt@gmail.com
