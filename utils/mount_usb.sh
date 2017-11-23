# mount usb external hard drive

# list disks: get device (eg /dev/sdb1)
sudo fdisk -l

# make dir to map drive to
sudo mkdir /media/netdrive

# install helper 
sudo apt-get install cifs-utils

# mount it
sudo mount --source /dev/sdb1 --target /media/netdrive

printf "device mounted to: /media/usb\n"
ls -l /media/usb


# unmount it
sudo umount /dev/sdb1

# folder size
du -sh /media/usb/Video/
# copy file
rsync -ah --progress /media/usb/Video/Pi\ 1998.avi /home/user/Video/
