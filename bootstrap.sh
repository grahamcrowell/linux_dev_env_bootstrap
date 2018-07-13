#! /usr/bin/env bash

# update apt-get
sudo apt-get update
# upgrade all installed apps
sudo apt-get upgrade
# log default install
mkdir ~/Documents/.install_logs
apt list --installed >> ~/Documents/.default_installs/`date +%Y%m%d`_installs.log


./install_nodeps.sh


# git
./install_git.sh

# zsh
# https://github.com/robbyrussell/oh-my-zsh
sudo apt-get install -y zsh
sudo sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

# linuxbrew
# http://linuxbrew.sh/
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
sudo apt-get install build-essential
# requires: env.sh

# git credentials manager
# https://github.com/Microsoft/Git-Credential-Manager-for-Mac-and-Linux/blob/master/Install.md
brew update
brew install git-credential-manager
git-credential-manager install


# chrome
# https://askubuntu.com/a/510186
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable


# vscode
# https://code.visualstudio.com/docs/setup/linux
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt-get update
sudo apt-get install -y code # or code-insiders
# fix inotify error
echo "customize max file watch handles"
echo "current max: "
cat /proc/sys/fs/inotify/max_user_watches
if [[ `cat /etc/sysctl.conf | grep "fs.inotify.max_user_watches="` -ne 0 ]]
then
    echo "max file watch handlers not yet custmized";
    echo "fs.inotify.max_user_watches=524288 >> /etc/sysctl.conf"
    sudo echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf
else
    echo "max file watch handlers already customized";
    echo "go to: https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc"
fi
fs.inotify.max_user_watches=524288

# java
# https://stackoverflow.com/a/49507161
sudo add-apt-repository ppa:linuxuprising/java
sudo apt-get update
sudo apt-get install -y oracle-java10-installer

# python3
# https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04
sudo apt-get install -y python3-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-get install -y python3-venv

./install_js.sh
# requires: env.sh

# awscli
# https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html
pip3 install awscli --upgrade --user

# go
# https://github.com/golang/go/wiki/Ubuntu
sudo add-apt-repository ppa:gophers/archive
sudo apt-get update
sudo apt-get install golang-1.10-go
# TODO add /usr/lib/go-1.10/bin to PATH

# shfmt (for vscode)
/usr/lib/go-1.10/bin/go get -u mvdan.cc/sh/cmd/shfmt

