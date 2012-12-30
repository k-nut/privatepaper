#! /usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import ConfigParser
import urllib2

from privatepaper import get_ssid


def setup():
        print "Welcome to privatepaper"
        print "This is the setup guide"

        print "You are connected the a network called %s right now."%(get_ssid())
        print "Would you like to make this your private network (your private wallpaper will only be shown if you are connected to this network)"
        answer = ""
        while answer.lower() not in ["yes", "no"]:
                answer = raw_input("Please Enter Yes or No ")
                if answer.lower() == "yes":
                        private_ssid = get_ssid()
                        print_success("Ok great, I saved that for you")
                elif answer.lower() == "no":
                        private_ssid = raw_input("Please enter your private network's ssid")
                else:
                        print_failure("You have to enter either Yes or No")
        print "Please pick your desired default wallpaper now"
        default_wallpaper = filepicker("Default wallpaper")
        print "Please pick your desired privat wallpaper now"
        private_wallpaper = filepicker("Private wallpaper")


        with open(os.path.expanduser("~/.privatepaper/settings.ini"), "w") as configfile:
                Config = ConfigParser.ConfigParser()
                Config.add_section("Settings")
                Config.set("Settings", "ssid", private_ssid)
                Config.set("Settings", "default_wallpaper", default_wallpaper)
                Config.set("Settings", "private_wallpaper", private_wallpaper)
                Config.write(configfile)

	print "I am now setting this to autostart for you"
	copy_autostart()
	print_success("Done!")
        print "You can of course allways rerun the setup"

def print_success(message):
	print '\033[1;32m%s\033[1;m'%(message)

def print_failure(message):
	print '\033[1;31m%s\033[1;m'%(message)

def zenity_picker(title):
	path_to_image = subprocess.check_output(["zenity", "--file-selection", "--title", title])
	return unicode(path_to_image).replace("\n", "")

def filepicker(title):
	if os.path.exists("/usr/bin/zenity"):
		return zenity_picker(title)
	else:
		path = ""
		while not os.path.exists(path):
			path = raw_input("Please enter the full path for the %s: "%(title))
			path = os.path.expanduser(path)
def copy_autostart():
	original = urllib2.urlopen("https://raw.github.com/k-nut/privatepaper/master/privatepaper.desktop")
	copy = original.read().replace("PATH_TO_PAPER", os.path.expanduser("~/privatepaper/privatepaper.py"))
	with open(os.path.expanduser("~/.config/autostart/privatepaper.desktop"), "w") as new_autostart:
		new_autostart.write(copy)
			

if __name__=="__main__":
	setup()
