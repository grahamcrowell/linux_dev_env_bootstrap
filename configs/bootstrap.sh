
sudo apt-get update
sudo apt-get upgrade
mkdir ~/Documents/logs
apt list --installed >> ~/Documents/logs/default_installs.log

sudo apt-get install git

# zsh
# https://github.com/robbyrussell/oh-my-zsh
sudo apt-get install zsh
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

sudo apt-get install dconf-tools
dconf write /org/gnome/desktop/interface/cursor-size 48

# chrome
# https://askubuntu.com/a/510186
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable

# windows bootable
# https://itsfoss.com/install-winusb-in-ubuntu-14-04/

# virtual box
# https://itsfoss.com/install-windows-10-virtualbox-linux/
# https://askubuntu.com/a/229908
sudo apt-get autoremove virtualbox-dkms
sudo apt-get install build-essential linux-headers-`uname -r` dkms virtualbox-dkms

# vs code
# https://code.visualstudio.com/docs/setup/linux
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

sudo apt-get install
sudo apt-get install
sudo apt-get install