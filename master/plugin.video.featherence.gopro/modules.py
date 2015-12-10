#import xbmc, os, subprocess, sys
#import xbmc, xbmcgui, xbmcaddon
import xbmc, xbmcgui, xbmcaddon
import subprocess, os, sys
import xbmcplugin
import urllib
import urllib2
import re

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

def CATEGORIES():
	'''Go-Pro'''
	#YOUList2("GoProCamera", 'UCqhnX4jA0A5paNd1v-zEysw', "", "", '1')
	
	addDir(localize(137),"Go-Pro",3,featherenceserviceicons_path + "se.png","Search Go-Pro Video",'1',58, getAddonFanart(9))
	'''Go-Pro'''
	list = []
	list.append('&youtube_ch=GoProCamera')
	list.append('&youtube_ch=GoProMX')
	list.append('&youtube_ch=GoProTutorials')
	list.append('&youtube_ch=GoProWorldOfficial')
	list.append('&youtube_ch=GoProUncut')
	addDir('Go-Pro',list,17,'https://lh6.ggpht.com/remKtmFiZgZ3yP409xrHZNIIe9M_bV9xEdQM1IOkJw5Ep28lDGVnC7z9iqgv-PsTsHA=w300',"",'1',58, getAddonFanart(9))
	'''Exterme Sport'''
	addDir("Extreme Sport",'plugin://plugin.video.extreme.com',8,"special://home/addons/plugin.video.extreme.com/icon.png","",'1',50, getAddonFanart(9))   
	#addDir(addonString(57).encode('utf-8') + space + addonString(200).encode('utf-8') + space + "1" + space5 + addonString(16).encode('utf-8'),'UCqhnX4jA0A5paNd1v-zEysw',9,'http://i.ytimg.com/i/fm5IpcgGCooON4Mm2vq40A/1.jpg?v=52fcd974',addonString(116).encode('utf-8'),'1',"")