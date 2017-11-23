# mount usb external hard drive

# list disks: get device (eg /dev/sdb1)
sudo fdisk -l

SOURCE=/dev/sdc
DEST=/media/usb4

# make dir to map drive to
sudo mkdir $DEST

# install helper 
sudo apt-get install cifs-utils

# mount it
sudo mount --source $SOURCE --target $DEST

printf "device mounted to: %s\n" $DEST
ls -l $DEST


# unmount it
# sudo umount /dev/sdb1

# folder size
# du -sh /media/usb/Video/
# copy file
# rsync -ah --progress /media/usb/Video/Pi\ 1998.avi /home/user/Video/
