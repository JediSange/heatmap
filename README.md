# Heatmap

## About
This is just a small heatmap app I did for fun and to mess around more with Django.  There are a huge number of issues with it and I'm not sure how much I will maintain it.  Pull requests welcome.

## Requirements
- python 2.x/3.x
- virtualenv
- mongodb

## Made With
- [Django](https://www.djangoproject.com/)
- [Leaflet](http://leafletjs.com/)
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)
- [MapTiler](http://www.maptiler.com)
- [mongoengine](http://mongoengine.org/)

## Local Environment
This app makes use of [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) for local development but neither are required.  The default provision provides a 64 bit Ubuntu box that should come preinstalled with everything you need to run the included Django app.  Simply `vagrant up` and then navigate to the `/vagrant` directory

## Installation
Most of this should be platform agnostic pending python and virtualenv are installed.  However, it is recommended to be ran on a Linux variant, preferrably Ubuntu.  Adjust accordingly.

    git clone git@github.com:JediSange/heatmap.git heatmap
    virtualenv heatmap
    cd heatmap
    source bin/activate
    pip install -r config/pip.requirements.txt
    cd app
    python manage.py generate_data
    python manage.py runserver

**Note:** Run `python manage.py runserver 0.0.0.0:8000` if running from Vagrant.  

You should now be able to see the heatmap by going to `http://localhost:8000` in your browser

## Usage
The app accepts events as URLs.  The format and example follow, assuming Django is running locally from the `manage.py runserver` command.

    127.0.0.1:8000/api/player_id/source_player_id/weapon_id/pos_x/pos_y
    127.0.0.1:8000/api/1/2/1/10.0/11.1

## Future Improvements
- Filter by weapon type (can be done with an AJAX solution and filtering by Mongo)
- Validation checks surrounding events - is player valid? are points valid?
- Wrap "API" into its own app for expansion
- Make local environment variables (IE: hide secret key, debug settings, etc)
- Add in Nginx/Gunicorn configuration
