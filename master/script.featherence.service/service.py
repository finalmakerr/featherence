import xbmc, xbmcgui
import os, sys
import subprocess
import xbmcaddon

from variables import *
from modules import *
	

	
if os.path.exists(skin_path) and xbmc.getCondVisibility('System.HasAddon(skin.featherence)') and 1 + 1 == 3:
	xbmc.sleep(5000)
	from shared_modules4 import *
	printpoint, guisettings_file_ = guicheck(admin)
	guikeeper(admin, guicheck=printpoint, guiread=guisettings_file_)
	xbmc.sleep(1000)

xbmc.sleep(2000)

if xbmc.getSkinDir() == 'skin.featherence':
	xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=23&value=)')
	mode215('_',admin,'','')
	
	try:
		VolumeLevel = int(xbmcaddon.Addon(addonID).getSetting('VolumeLevel'))
		xbmc.executebuiltin('SetVolume('+str(VolumeLevel)+')')
	except: pass
	
	if not xbmc.getInfoLabel('Skin.HasSetting(StartUpMusic)'):
		if xbmc.getInfoLabel('Skin.String(StartUpMusic)') == "" or not os.path.exists(xbmc.getInfoLabel('Skin.String(StartUpMusic)')): xbmc.executebuiltin('PlayMedia(special://skin/sounds/playfeatherence.mp3)')
		else:
			notification("Trying to play custom file","","",1000)
			xbmc.executebuiltin('PlayMedia('+xbmc.getInfoLabel('Skin.String(StartUpMusic)')+')')
			'''---------------------------'''
	
setsetting_custom1('script.featherence.service','Skin_UpdateLog',"true")

addon = 'plugin.video.featherence.kids'
if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
	setsetting_custom1(addon, 'Addon_UpdateLog', "true")

addon = 'plugin.video.featherence.gopro'
if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
	setsetting_custom1(addon, 'Addon_UpdateLog', "true")

addon = 'plugin.video.featherence.music'
if xbmc.getCondVisibility('System.HasAddon('+addon+')'):
	setsetting_custom1(addon, 'Addon_UpdateLog', "true")

mode101('1',admin, 'TotalMouse')
mode5('', admin, 'demon', '')
