#!/usr/bin/env python

import re

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

def asMatches(lines):
  matches = [ EXP.search(x) for x in lines ]
  matches = [ x for x in matches if x ]
  matches = [ x.group(1) for x in matches ]
  return set(matches)

def listMountpoints():
  import glob

  return set(glob.glob("/cdh/*"))

disks = listDisks() # asMatches(listBlkIds())
mountpoints = listMountedDisks()

if "__main__" == __name__:
  print "  A: %s" % repr(disks)
  print "  B: %s" % repr(mountpoints)
  print "A-B: %s" % repr(disks - mountpoints)
  print "B-A: %s" % repr(mountpoints - disks)

  for m in (mountpoints - disks):
    print "# sudo rm -rf %s" % m
