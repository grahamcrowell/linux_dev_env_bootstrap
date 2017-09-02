#!/bin/bash

# install docker ce

# https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

# https://github.com/grahamcrowell/docker-transmission-openvpn

sudo apt-get install docker-ce

# docker run --cap-add=NET_ADMIN --device=/dev/net/tun -d \
#               -v /transmission:/data \
#               -v /etc/localtime:/etc/localtime:ro \
#               -e "OPENVPN_PROVIDER=NORDVPN" \
#               -e "OPENVPN_USERNAME=graham.crowell@yahoo.com" \
#               -e "OPENVPN_PASSWORD=2and2is5" \
#               -e LOCAL_NETWORK=192.168.0.0/24 \
#               -p 9091:9091 \
#               haugene/transmission-openvpn