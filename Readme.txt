How to build and run this application

Prerequisites
•	MongoDB
•	Python 2.X (tested on 2.9)
•	Tornado (Python library)
•	Pymongo (python library)
To install MongoDB follow this step
•	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
•	echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
•	sudo apt-get update
•	sudo apt-get install mongodb-10gen
•	sudo service mongodb restart
•	sudo mkdir -p /data/db
•	sudo chmod -R 755 /data/db
•	sudo mongod
Install Pip
Sudo apt-get install python-pi
Install Tornado
Sudo pip install tornado
Install pymongo
Sudo pip install pymongo

To Run this application create a directory “xyz”
Cd to “xyz” directory
Python TornadoServer.py

This will start tornado server on port 8888
Change the port in the tornadoServer.py file if you wish
