Upload the create_vols.py, validate_vols.py and prepare_disk.sh to the datanodes.

Run create_vols.py

```
$ python create_vols.py
A: set(['/dev/sdr', '/dev/sdp', '/dev/sdq', '/dev/sdn', '/dev/sdo', '/dev/sdl', '/dev/sdm', '/dev/sdj', '/dev/sdk', '/dev/sdh', '/dev/sdi', '/dev/sdf', '/dev/sdg', '/dev/sdd', '/dev/sde', '/dev/sdb', '/dev/sdc', '/dev/sda'])
B: set(['/dev/sds'])
A-B: ['/dev/sda', '/dev/sdb', '/dev/sdc', '/dev/sdd', '/dev/sde', '/dev/sdf', '/dev/sdg', '/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk', '/dev/sdl', '/dev/sdm', '/dev/sdn', '/dev/sdo', '/dev/sdp', '/dev/sdq', '/dev/sdr'] 
B-A: ['/dev/sds']
```

This script creates two files: append-to-fstab.txt and cmds.sh, with the directives needed to adjust the mountpoints. As for create_vols.py output, the last line should show up the boot device. Confirm with the mount command and ensure there are mountpoints for /dev/sds active:

```
$ python create_vols.py
A: set(['/dev/sdr', '/dev/sdp', '/dev/sdq', '/dev/sdn', '/dev/sdo', '/dev/sdl', '/dev/sdm','/dev/sdj', '/dev/sdk', '/dev/sdh', '/dev/sdi', '/dev/sdf', '/dev/sdg', '/dev/sdd', '/dev/sde','/dev/sdb', '/dev/sdc', '/dev/sda'])
B: set(['/dev/sds'])
A-B: ['/dev/sda', '/dev/sdb', '/dev/sdc', '/dev/sdd', '/dev/sde', '/dev/sdf', '/dev/sdg','/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk', '/dev/sdl', '/dev/sdm', '/dev/sdn', '/dev/sdo','/dev/sdp', '/dev/sdq', '/dev/sdr']
B-A: ['/dev/sds']
$ mount
/dev/sds3 on / type ext4 (rw,noatime,nodiratime) proc on /proc type proc (rw) sysfs on /sys type sysfs (rw)
devpts on /dev/pts type devpts (rw,gid=5,mode=620) tmpfs on /dev/shm type tmpfs (rw)
/dev/sds1 on /boot type ext3 (rw,noatime,nodiratime) /dev/sds2 on /var type ext4 (rw,noatime,nodiratime) none on /proc/sys/fs/binfmt_misc type binfmt_misc (rw)
```

if they match, run cmds.sh piping to sudo as such:

```
$ bash cmds.sh | sudo bash -xe –
```

Then edit /etc/fstab and append the contents of append-to-fstab.txt to it, then run mount –a to enable it.

Then, run validate_vols.py on each host. The results of A-B and B-A should be empty:

```
$ sudo python validate_vols.py

A: set(['/dev/sdr', '/dev/sds', '/dev/sdp', '/dev/sdq', '/dev/sdn', '/dev/sdo', '/dev/sdl','/dev/sdm', '/dev/sdj', '/dev/sdk', '/dev/sdh', '/dev/sdi', '/dev/sdf', '/dev/sdg', '/dev/sdd','/dev/sde', '/dev/sdb', '/dev/sdc', '/dev/sda'])

B: set(['/dev/sdr', '/dev/sds', '/dev/sdp', '/dev/sdq', '/dev/sdn', '/dev/sdo', '/dev/sdl','/dev/sdm', '/dev/sdj', '/dev/sdk', '/dev/sdh', '/dev/sdi', '/dev/sdf', '/dev/sdg', '/dev/sdd', '/dev/sde', '/dev/sdb', '/dev/sdc', '/dev/sda'])

A-B: set([])

B-A: set([])
```

Also, run mount for extra validation:

```
$ mount

/dev/sds3 on / type ext4 (rw,noatime,nodiratime) proc on /proc type proc (rw) sysfs on /sys type sysfs (rw)
devpts on /dev/pts type devpts (rw,gid=5,mode=620) tmpfs on /dev/shm type tmpfs (rw)
/dev/sds1 on /boot type ext3 (rw,noatime,nodiratime) /dev/sds2 on /var type ext4 (rw,noatime,nodiratime) none on /proc/sys/fs/binfmt_misc type binfmt_misc (rw) /dev/sda1 on /cdh/0 type ext4 (rw,noatime,nodiratime)
/dev/sdb1 on /cdh/1 type ext4 (rw,noatime,nodiratime)
/dev/sdc1 on /cdh/2 type ext4 (rw,noatime,nodiratime)
/dev/sdd1 on /cdh/3 type ext4 (rw,noatime,nodiratime) /dev/sde1 on /cdh/4 type xt4 (rw,noatime,nodiratime)
/dev/sdf1 on /cdh/5 type ext4 (rw,noatime,nodiratime)
/dev/sdg1 on /cdh/6 type ext4 (rw,noatime,nodiratime)
/dev/sdh1 on /cdh/7 type ext4 (rw,noatime,nodiratime)
/dev/sdi1 on /cdh/8 type ext4 (rw,noatime,nodiratime) /dev/sdj1 on /cdh/9 type ext4 (rw,noatime,nodiratime)
/dev/sdk1 on /cdh/A type ext4 (rw,noatime,nodiratime)
/dev/sdl1 on /cdh/B type ext4 (rw,noatime,nodiratime)
/dev/sdm1 on /cdh/C type ext4 (rw,noatime,nodiratime)
/dev/sdn1 on /cdh/D type ext4 (rw,noatime,nodiratime)
/dev/sdo1 on /cdh/E type ext4 (rw,noatime,nodiratime)
/dev/sdp1 on /cdh/F type ext4 (rw,noatime,nodiratime)
/dev/sdq1 on /cdh/G type ext4 (rw,noatime,nodiratime) /dev/sdr1 on /cdh/H type ext4 (rw,noatime,nodiratime)
```
