#! /usr/bin/env sh

# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
# ensure output like:
# Installed: (none)

# install docker-ce
sudo apt-get install -y docker-ce
# check if docker is running 
sudo systemctl status docker


# non-sudo-ize docker commands
sudo usermod -aG docker ${USER}
su - ${USER}
id -nG