#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess, random

from variables import *
from modules import *
from shared_modules3 import get_params

printpoint = ""

try: params=get_params()
except Exception, TypeError: xbmc.executebuiltin('Addon.OpenSettings('+addonID+')')
mode=None
value=None
value2=None
value3=None
value4=None
value5=None
value6=None

try: mode=int(params["mode"])
except: pass
try: value=str(params["value"])
except: value = ""
try: value2=str(params["value2"])
except: value2 = ""
try: value3=str(params["value3"])
except: value3 = ""
try: value4=str(params["value4"])
except: value4 = ""
try: value5=str(params["value5"])
except: value5 = ""
try: value6=str(params["value6"])
except: value6 = ""

if mode == 5:
	'''------------------------------
	---demon-------------------------
	------------------------------'''
	name = "demon"
	mode5(value)
	'''---------------------------'''

elif mode == 7:
	copykeymaps()
	
elif mode == 27:
	'''------------------------------
	---Remote-Control----------------
	------------------------------'''
	name = "Remote-Control"
	
	Remote_Name = getsetting('Remote_Name')
	Remote_Name2 = getsetting('Remote_Name2')
	Remote_Support = getsetting('Remote_Support')
	Remote_TestingTime = getsetting('Remote_TestingTime')
	Remote_LastDate = getsetting('Remote_LastDate')
	remotes_path = os.path.join(addonPath, 'resources', 'remotes', '')
	
	Remote_Support = setRemote_Support(value, Remote_Name, Remote_Support)

	if Remote_Support != "true":
		if value != '0': dialogok(addonString(32032).encode('utf-8'), addonString(32036).encode('utf-8'),addonString(32101).encode('utf-8'),"")
		sys.exit()

	if Remote_Name == "":
		printpoint = printpoint + "1"
		setProperty('Remote_Name', "", type="home")
		returned = dialogyesno(addonString(32025).encode('utf-8'), addonString(32024).encode('utf-8') + '[CR]' + addonString(19194).encode('utf-8'))
		if returned == 'skip': printpoint = printpoint + "9"
	
	if not "9" in printpoint:
		if value != '0' or Remote_Name == "":
			printpoint = printpoint + "2"
			printpoint = setRemote_Name(Remote_Name, Remote_TestingTime, remotes_path)
			
		else:
			if Remote_Name != "":
				printpoint = printpoint + "3"
				Activate(Remote_Name, Remote_Name2, Remote_TestingTime, remotes_path)

				if datenowS == Remote_LastDate:
					dialogok(addonString(32025).encode('utf-8'), addonString(32034).encode('utf-8'), "", addonString(32035).encode('utf-8'))
				
	setsetting('Remote_Name2',"")

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "Remote_Name" + space2 + Remote_Name + space + "Remote_Name2" + space2 + Remote_Name2
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
	'''---------------------------'''

'''------------------------------
---PRINT-END---------------------
------------------------------'''
text = "TypeError" + space2 + str(TypeError)
printlog(title='default.py', printpoint=printpoint, text=text, level=1, option="")
'''---------------------------'''