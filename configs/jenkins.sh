#!/bin/bash

# install jenkins

# see https://wiki.jenkins.io/display/JENKINS/Starting+and+Accessing+Jenkins
# see https://wiki.jenkins.io/display/JENKINS/Jenkins+CLI
# https://pkg.jenkins.io/debian-stable/

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

printf "add\ndeb https://pkg.jenkins.io/debian-stable binary/\nto\n/etc/apt/sources.list"
sudo vi /etc/apt/sources.list
# deb https://pkg.jenkins.io/debian-stable binary/

mkdir $HOME/jenkins
cd $HOME/jenkins 
wget https://jenkins.example.com/jnlpJars/jenkins-cli.jar