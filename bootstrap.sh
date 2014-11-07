#!/usr/bin/env bash

apt-get update
apt-get install vim
apt-get install -y python
apt-get install -y python-virtualenv
apt-get install -y git

git config --global user.name "Austin DeVinney"
git config --global user.email austin.devinney@gmail.com
git config --global core.editor vim