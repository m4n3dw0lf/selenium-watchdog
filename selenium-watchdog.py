#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright (c) 2016-2017 Angelo Moura
#
# This file is part of the program selenium-watchdog
#
# selenium-watchdog is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import urllib
import urllib2
import threading
from time import sleep
from sys import argv
from selenium import webdriver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

try:
	url = argv[1]
	driver = webdriver.Firefox()
	#replace your project URL driver.get("http://<fixedurl>")
	#run only with $selenium-watchdog
	driver.get(url)
except:
	print "usage:\n  python selenium-watchdog.py <URL>"
	exit(0)

version = "0.1"
author = "Angelo Moura(m4n3dw0lf)"

class Selenium(FileSystemEventHandler):
	def on_modified(self, event):
		files = [".html",".ejs",".css",".js"]
		if ".swp" not in str(event) and any(x in str(event) for x in files):
				driver.refresh()

class WatchDog(object):
	def __init__(self):
		event_handler = Selenium()
		observer = Observer()
		observer.schedule(event_handler, path='.', recursive=True)
		observer.start()
    		try:
   			while True:
            			sleep(1)
    		except KeyboardInterrupt:
        		observer.stop()
    		observer.join()

if __name__ == "__main__":
	print "\n[+] selenium-watchdog initialized."
	print "\nPress CTRL+C or close the browser to stop...\n"
	WatchDog()
