# https://help.ubuntu.com/lts/serverguide/samba-fileserver.html
# https://wiki.samba.org/index.php/Setting_up_Samba_as_a_Standalone_Server
# /etc/samba/smb.conf

# print mounts
udisksctl

sudo apt install samba

[global]
        workgroup = WORKGROUP
        netbios name = SA

        map to guest = Bad User

        log file = /var/log/samba/%m
        log level = 1


[guest]
        # This share allows anonymous (guest) access
        # without authentication!
        path = /srv/samba/guest/
        read only = no
        guest ok = yes

[user]
        # This share requires authentication to access
        path = /srv/samba/user/
        read only = no
        guest ok = no

