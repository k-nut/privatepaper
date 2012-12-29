#! /usr/bin/env python
# -*- coding: utf8 -*-
import subprocess
import os
import ConfigParser

import sys
import subprocess
import datetime

import gnome
import gnome.ui
import gtk

class Namespace: pass
ns = Namespace()
ns.dialog = None


def main():
    set_private()
    prog = gnome.init ("gnome_save_yourself", "1.0", gnome.libgnome_module_info_get(), sys.argv, [])
    client = gnome.ui.master_client()
    #set up call back for when 'logout'/'Shutdown' button pressed
    client.connect("save-yourself", session_save_yourself)
    client.connect("shutdown-cancelled", shutdown_cancelled)

def session_save_yourself( *args):
    #Lets try to unmount all truecrypt volumes
    set_default()
    return True

def shutdown_cancelled( *args):
    if ns.dialog != None:
        ns.dialog.destroy()
    return True

def set_private():
	Config = ConfigParser.ConfigParser()
	Config.read(os.path.expanduser("~/.privatepaper/settings.ini"))
	if Config.get("Settings", "ssid") == get_ssid():
		path_to_wallpaper = Config.get("Settings", "private_wallpaper")
		change_wallpaper(path_to_wallpaper)

def set_default():
	Config = ConfigParser.ConfigParser()
	Config.read(os.path.expanduser("~/.privatepaper/settings.ini"))
	path_to_wallpaper = Config.get("Settings", "default_wallpaper")
	change_wallpaper(path_to_wallpaper)


def get_ssid():
	iwconfig_out = subprocess.check_output(["iwconfig", "wlan0"])
	ssid = iwconfig_out.split('ESSID:"')[1].split('"')[0]
	return ssid	

	
def change_wallpaper(path_to_image):
	filepath = "file://" + path_to_image
	o = subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", filepath])

if __name__=="__main__":
	main()
	gtk.main()
