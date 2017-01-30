import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess

pluginprogramfeatherenceemuPath          = xbmcaddon.Addon('plugin.program.featherence.emu').getAddonInfo("path")
sharedlibDir2 = os.path.join(pluginprogramfeatherenceemuPath, '')
sys.path.insert(0, sharedlibDir2)

from variables import *
from modules import *

if systemplatformandroid:
	installemuconsole(force=True)
	os.system( "am start -a android.intent.action.MAIN -n com.retroarch/.BrowserActivity" )

else: notification_common("18","OS is not Android?")