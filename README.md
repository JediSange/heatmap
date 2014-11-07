# Red 5 Heatmap

## Requirements
- python 2.x/3.x
- virtualenv
- mongodb

## Vagrant
This app makes use of [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) for local development but neither are required.  The default provision provides a 64 bit Ubuntu box that should come preinstalled with everything you need to run the included Django app.  Simply `vagrant up` and then navigate to the `/vagrant` directory

## Installation
    git clone git@github.com:JediSange/red5app.git
    virtualenv red5app
    cd red5app
    source bin/activate
    pip install -r config/pip.requirements.txt
    cd app
    python manage.py runserver
