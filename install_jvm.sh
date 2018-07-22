#! /usr/bin/env bash

# java
# https://stackoverflow.com/a/49507161
sudo add-apt-repository ppa:linuxuprising/java
sudo apt-get update
sudo apt-get install -y oracle-java10-installer

# scala
sudo apt-get install -y scala

# sbt
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt