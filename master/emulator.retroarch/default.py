# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess, random

pluginprogramfeatherenceemuPath          = xbmcaddon.Addon('plugin.program.featherence.emu').getAddonInfo("path")
sharedlibDir2 = os.path.join(pluginprogramfeatherenceemuPath, '')
sys.path.insert(0, sharedlibDir2)

from variables import *
from modules import *
	
if systemplatformlinux:
	fn = dialog.browse(1, 'retroarch', 'files')
	os.system( "chmod a+rx " + emulator_file )
	os.system( "%s '%s' "%(emulator_file,fn.replace("'", "'\\''")) )
	os.system("chmod +x /storage/.kodi/addons/emulator.retroarch/bin/*")
	os.system("export LD_LIBRARY_PATH='/storage/.kodi/addons/emulator.retroarch/lib'")

elif systemplatformwindows:
	os.system("start " + emulator_file + space + launcher_args + space + '--menu')