#!/bin/bash

df -h | grep "/var/media/" | awk {'print $2,$6'} | awk {'print substr($2, 12, length($2)-1)'} | tee /storage/externalusb.log
SP='/storage/.kodi/addons/skin.htpt/specials/'
#df -h | grep "ABCDEFG" | tee externalusb.log
#awk {'print $4'} | externalusb.log
#sleep 2
#df -h #show devices
TOTALUSB=`wc -l /storage/externalusb.log | grep -o '[0-9]*'` #ls /var/media -1 | wc -l
USB1=`head -1 /storage/externalusb.log`
USB2=`sed -n 2p /storage/externalusb.log`
USB3=`sed -n 3p /storage/externalusb.log`
USB4=`sed -n 4p /storage/externalusb.log`
USB5=`sed -n 5p /storage/externalusb.log`
echo USB1: $USB1
echo USB2: $USB2
echo USB3: $USB3
echo USB4: $USB4
echo USB5: $USB5
echo TOTALUSB: $TOTALUSB


USB1p=`ls /var/media/$USB1/ | grep -iFx "pictures" | wc -l`
USB2p=`ls /var/media/$USB2/ | grep -iFx "pictures" | wc -l`
USB3p=`ls /var/media/$USB3/ | grep -iFx "pictures" | wc -l`
USB4p=`ls /var/media/$USB4/ | grep -iFx "pictures" | wc -l`
USB5p=`ls /var/media/$USB5/ | grep -iFx "pictures" | wc -l`
USB1v=`ls /var/media/$USB1/ | grep -iFx "videos" | wc -l`
USB2v=`ls /var/media/$USB2/ | grep -iFx "videos" | wc -l`
USB3v=`ls /var/media/$USB3/ | grep -iFx "videos" | wc -l`
USB4v=`ls /var/media/$USB4/ | grep -iFx "videos" | wc -l`
USB5v=`ls /var/media/$USB5/ | grep -iFx "videos" | wc -l`

if [ $TOTALUSB -gt 0 ]; then
	if [ $USB1p -eq 0 ]; then
		mkdir /var/media/$USB1/pictures/
		#cp $SP\README.txt /var/media/$USB1/pictures/
		USB1p=`ls /var/media/$USB1/ | grep -iFx "pictures" | wc -l`
		echo USB1p: pictures Folder Created! -$USB1p
	fi
	if [ $USB1v -eq 0 ]; then
		mkdir /var/media/$USB1/videos/
		#cp $SP\README.txt /var/media/$USB1/videos/
		USB1v=`ls /var/media/$USB1/ | grep -iFx "videos" | wc -l`
		
		echo USB1v: videos Folder Created! -$USB1v
	fi
	if [ $USB1p -eq 0 ] && [ $USB1v -eq 0 ]; then
		umount /var/media/$USB1
	fi
fi
if [ $TOTALUSB -gt 1 ]; then
	if [ $USB2p -eq 0 ]; then
		mkdir /var/media/$USB2/pictures/
		#cp $SP\README.txt /var/media/$USB2/pictures/
		USB2p=`ls /var/media/$USB2/ | grep -iFx "pictures" | wc -l`
		echo USB2p: pictures Folder Created! -$USB2p
	fi
	if [ $USB2v -eq 0 ]; then
		mkdir /var/media/$USB2/videos/
		#cp $SP\README.txt /var/media/$USB2/videos/
		USB2v=`ls /var/media/$USB2/ | grep -iFx "videos" | wc -l`
		echo USB2v: videos Folder Created! -$USB2v
	fi
	if [ $USB2p -eq 0 ] && [ $USB2v -eq 0 ]; then
		umount /var/media/$USB2
	fi
fi
if [ $TOTALUSB -gt 2 ]; then
	if [ $USB3p -eq 0 ]; then
		mkdir /var/media/$USB3/pictures/
		#cp $SP\README.txt /var/media/$USB3/pictures/
		USB3p=`ls /var/media/$USB3/ | grep -iFx "pictures" | wc -l`
		echo USB3p: pictures Folder Created! -$USB3p
	fi
	if [ $USB3v -eq 0 ]; then
		mkdir /var/media/$USB3/videos/
		#cp $SP\README.txt /var/media/$USB3/videos/
		USB3v=`ls /var/media/$USB3/ | grep -iFx "videos" | wc -l`
		echo USB3v: videos Folder Created! -$USB3v
	fi
	if [ $USB3p -eq 0 ] && [ $USB3v -eq 0 ]; then
		umount /var/media/$USB3
	fi	
fi
if [ $TOTALUSB -gt 3 ]; then
	if [ $USB4p -eq 0 ]; then
		mkdir /var/media/$USB4/pictures/
		#cp $SP\README.txt /var/media/$USB4/pictures/
		USB4p=`ls /var/media/$USB4/ | grep -iFx "pictures" | wc -l`
		echo USB4p: pictures Folder Created! -$USB4p
	fi
	if [ $USB4v -eq 0 ]; then
		mkdir /var/media/$USB4/videos/
		#cp $SP\README.txt /var/media/$USB4/videos/
		USB4v=`ls /var/media/$USB4/ | grep -iFx "videos" | wc -l`
		echo USB4v: videos Folder Created! -$USB4v
	fi
	if [ $USB4p -eq 0 ] && [ $USB4v -eq 0 ]; then
		umount /var/media/$USB4
	fi	
fi
if [ $TOTALUSB -gt 4 ]; then
	if [ $USB5p -eq 0 ]; then
		mkdir /var/media/$USB5/pictures/
		#cp $SP\README.txt /var/media/$USB5/pictures/
		USB5p=`ls /var/media/$USB5/ | grep -iFx "pictures" | wc -l`
		echo USB5p: pictures Folder Created! -$USB5p
	fi
	if [ $USB5v -eq 0 ]; then
		mkdir /var/media/$USB5/videos/
		#cp $SP\README.txt /var/media/$USB5/videos/
		USB5v=`ls /var/media/$USB5/ | grep -iFx "videos" | wc -l`
		echo USB5v: videos Folder Created! -$USB5v
	fi
	if [ $USB5p -eq 0 ] && [ $USB5v -eq 0 ]; then
		umount /var/media/$USB5
	fi	
fi
#ifconfig eth0 down && sleep 1 & ifconfig eth0 up && sleep 1
#USB1gb=`df -h | grep "/var/media/" | awk {'print $2,$6'} | awk {'print substr($2, 12, length($2)-1)'}`
#echo USB1gb: $USB1gb
#cp $SP\HTPT.txt /var/media/$USB1/
#USB1c=`cp $SP\HTPT.txt /var/media/$USB1/ | grep -i "" | wc -l`
#cp $SP\README.txt /var/media/$USB1/pictures/

#df -h | grep "/var/media/" | awk {'print $2,$6'} | awk {'print substr($2, 12, length($2)-1)'} | tee /storage/externalusb.log
#cp $SP\README.txt /var/media/$USB1/pictures/ >> /storage/externalusb1.log
#ls /var/media/$USB1/

#LAN2=`ifconfig | grep -i "eth0" | wc -l`
#USB1m='ls /var/media/'$USB1'/'
#ls /var/media/$USB2/