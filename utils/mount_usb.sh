# mount usb external hard drive

# list disks: get device (eg /dev/sdb1)
sudo fdisk -l

# make dir to map drive to
sudo mkdir /media/usb

sudo mount --source /dev/sdb1 --target /media/usb
