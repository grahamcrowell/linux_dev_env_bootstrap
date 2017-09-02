#!/bin/bash
# install java development kit

sudo apt-get update
javac -version
# add these lines to /etc/environment
# JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64"
# export JAVA_HOME
echo $JAVA_HOME


# install sbt

echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt

# install scala

sudo apt-get install scala
scala -version
