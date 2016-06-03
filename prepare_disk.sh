#!/bin/sh

D=$1
O=$2

if [ -b /dev/sd${D} ]; then
  echo "if [ ! -d $O ]; then mkdir -p $O ; fi"
  echo parted -s -a optimal /dev/sd$D mklabel gpt -- mkpart primary ext4 1 -1
  echo mkfs.ext4 -m 1 -L "M=$O" -E lazy_itable_init=1 -O dir_index,sparse_super,extent /dev/sd${D}1
fi
