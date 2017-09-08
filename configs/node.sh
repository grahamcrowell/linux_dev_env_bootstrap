#!/bin/bash

# install nodejs and npm
# http://www.hostingadvice.com/how-to/install-nodejs-ubuntu-14-04/

sudo apt-get install nodejs
sudo apt-get install npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
node -v
npm -v

# https://webtorrent.io/desktop/
npm install --save webtorrent
npm install --save webtorrent-cli -g
npm install --save imdb-api
echo "imdb-api: apikey=814d92d0"
# npm install  --save thepiratebay


