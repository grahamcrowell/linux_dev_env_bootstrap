#!/bin/bash

# configure ssh connections to ubuntu server

# https://www.maketecheasier.com/setup-enable-ssh-ubuntu/

printf "configuring ssh"

sudo apt-get install openssh-server
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
sudo chmod a-w /etc/ssh/sshd_config.factory-defaults
sudo systemctl restart ssh
mkdir ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t rsa

echo "configuration of ssh complete"

ifconfig

