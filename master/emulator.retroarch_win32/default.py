import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess

pluginprogramfeatherenceemuPath          = xbmcaddon.Addon('plugin.program.featherence.emu').getAddonInfo("path")
sharedlibDir2 = os.path.join(pluginprogramfeatherenceemuPath, '')
sys.path.insert(0, sharedlibDir2)

from variables import *
from modules import *
	
if systemplatformwindows:
	os.system("start " + emulator_file + space + launcher_args + space + '--menu')
else: notification_common("18","OS is not windows x32?")