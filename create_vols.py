#!/usr/bin/env python

import re

ARR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
EXP = re.compile(r"M=(/cdh/.)")

def listDisks():
  import glob
  return set(glob.glob("/dev/sd?"))

def listMountedDisks():
  with open("/etc/mtab", "r") as f:
    lines = f.readlines()
  return set([ x[:len("/dev/sdX")] for x in lines if x.startswith("/dev/sd") ])

def listBlkIds():
  import os
  with os.popen("sudo blkid", "r") as f:
    lines = f.readlines()
  return lines

def listMountpoints():
  import glob

  return set(glob.glob("/cdh/*"))

disks = listDisks() # asMatches(listBlkIds())
mountpoints = listMountedDisks()

if "__main__" == __name__:
  print "  A: %s" % repr(disks)
  print "  B: %s" % repr(mountpoints)
  print "A-B: %s" % repr(sorted(disks - mountpoints))
  print "B-A: %s" % repr(sorted(mountpoints - disks))

  cmds = list()
  fstabs = list()
  for idx, m in enumerate(sorted(disks - mountpoints)):
    cmd = "./prepare_disk.sh %s /cdh/%s" % (m, ARR[idx])
    cmds.append(cmd)
    fstab = "LABEL=\"M=/cdh/%s\"\t/cdh/%s\text4\tdefaults,noatime,nodiratime\t1\t2" % (ARR[idx], ARR[idx])
    fstabs.append(fstab)


  script = "\n".join(cmds)

  with open("cmds.sh", "w") as f:
    f.write(script + "\n")

  fstab = "\n".join(fstabs)

  with open("append-to-fstab.txt", "w") as f:
    f.write(fstab + "\n")

