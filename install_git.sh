#! /usr/bin/env sh

# git
sudo apt-get install -y git
# git flow
sudo apt-get install -y git-flow

# config git
git config --global user.email "graham.crowell@gmail.com"
git config --global user.name "grahamcrowell"
# TODO FIXME
if [ -f ~/.shh/id_rsa ] 
then
    echo "rsa key already exists";
else
    echo "foo"
fi
# config github account key

ssh-keygen -t rsa -b 4096 -C "graham.crowell@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
sudo apt-get install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub
google-chrome https://github.com/settings/ssh/new