#!/usr/bin/env bash

apt-get update
apt-get -y install git
apt-get -y install sqlite

# install python tools
apt-get -y install python3-setuptools
apt-get -y install build-essential python3-dev

#install pip
easy_install3 pip

# production packages
pip3.4 install flask
pip3.4 install flask-wtf
pip3.4 install flask-sqlalchemy
pip3.4 install flask-login
pip3.4 install flask-restless

# development packages
pip3.4 install pylint
pip3.4 install pyflakes
pip3.4 install jupyter

