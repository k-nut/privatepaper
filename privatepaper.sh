#!/bin/sh


#
# Set all your variables here
# START EDITING HERE
#
OUR_SSID="FRITZ!Box Fon WLAN 7270  "  # The SSID of the network in which you would like to show the private picture
PRIVATE_PIC="file:///home/knut/Arbeitsfläche/aaltsch.jpg" # Path for the private picture
PUBLIC_PIC="file:///usr/share/backgrounds/warty-final-ubuntu.png" # Path for the default picture
#
# STOP EDITING HERE
#


# This gets the wifi network you are connected to at the moment
SSID=`iwconfig wlan0 | awk 'BEGIN{FS="ESSID:"}{print $2}' | sed 's/"//g'`

#echo $SSID | awk '{print length}'
#echo $OUR_SSID | awk '{print length}'

if [ "$SSID" = "$OUR_SSID" ]
then
	gsettings set org.gnome.desktop.background picture-uri $PRIVATE_PIC
else 
	gsettings set org.gnome.desktop.background picture-uri $PUBLIC_PIC
fi


