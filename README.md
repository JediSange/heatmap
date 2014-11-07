# Red 5 Heatmap

## Requirements
- python 2.x/3.x
- virtualenv
- mongodb

## Local Environment
This app makes use of [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) for local development but neither are required.  The default provision provides a 64 bit Ubuntu box that should come preinstalled with everything you need to run the included Django app.  Simply `vagrant up` and then navigate to the `/vagrant` directory

## Installation
Most of this should be platform agnostic pending python and virtualenv are installed.  However, it is recommended to be ran on a Linux variant, preferrably Ubuntu.  Adjust accordingly.

    git clone git@github.com:JediSange/red5app.git
    virtualenv red5app
    cd red5app
    source bin/activate
    pip install -r config/pip.requirements.txt
    cd app
    python manage.py runserver

**Note** that if you're running Vagrant, the final command will have to be `python manage.py runserver 0.0.0.0:8000`.  You should now be able to see the heatmap by going to `http://localhost:8000` in your browser

## Usage
The app accepts events as URLs.  The format and example follow, assuming Django is running locally from the `manage.py runserver` command.

    127.0.0.1:8000/api/player_id/source_player_id/weapon_id/pos_x/pos_y
    127.0.0.1:8000/api/1/2/1/10.0/11.1

## Design Choices
### Scalability
### Coupled Requirements

## Future Improvements
- Validation checks surrounding events
- Wrap "API" into its own app for expansion
- Make local environment variables (IE: hide secret key, debug settings, etc)
- Add in Nginx/Gunicorn configuration