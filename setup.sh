#!/bin/sh

clear
echo "This is the Privatepaper Installer"
echo "Installing python-gnome"
sudo apt-get install python-gnome2 --quiet --yes
echo "Done"
echo "Checking if zenity is installed"
type zenity >/dev/null 2>&1 || { ZENITY_INSTALLED="Yes"; }

if [ -z "$ZENITY_INSTALLED" ]
then
	echo Zenity is installed. You will have a pretty file picker
else
	echo Zenity is not installed. You can enter the path to the file by hand
	echo or install zenity and have a nice filepicker. Install it [y/n]?
	read install_zenity
	if [ "$install_zenity" = "y" ]
	then
		sudo apt-get install zenity --quiet --yes
		echo "Done!"
	else
		echo "Ok, well do it without zenity."
	fi
fi
touch ~/.privatepaper/settings.ini
mkdir ~/privatepaper
cd ~/privatepaper
wget --no-check-certificate "https://raw.github.com/k-nut/privatepaper/master/privatepaper.py"
wget --no-check-certificate "https://raw.github.com/k-nut/privatepaper/master/setup.py"
echo "Ok, lets start the privatepaper setup. Press return to start"
read start
clear
python setup.py
