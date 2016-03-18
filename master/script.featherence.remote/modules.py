# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess, random

from variables import *
from shared_modules import *


def mode5(value):
	'''startup'''
	Remote_Name = getsetting('Remote_Name')
	Remote_Support = getsetting('Remote_Support')
	if Remote_Name != "" and Remote_Name != 'None' and Remote_Support == 'true':
		xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=27&value=0)')

def terminal(command):
	'''Execute commands to OS terminal'''
	import subprocess
	name = 'terminal' ; printpoint = "" ; TypeError = "" ; extra = "" ; output = ""

	process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
	output = process.communicate()[0]
				
	text = str(output) + extra
	try: printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	except Exception, TypeError:
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
		'''---------------------------'''
	return output