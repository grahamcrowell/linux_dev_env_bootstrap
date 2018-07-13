#! /usr/bin/env sh

# TODO check for docker

docker pull jenkins/jenkins:lts
sudo mkdir /var/jenkins_home
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
