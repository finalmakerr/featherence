# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
#from modulesZ import *
#from modulesA import *
'''---------------------------'''

def CATEGORIES():
	'''Go-Pro'''
	background = 100
	#YOUList2("GoProCamera", 'UCqhnX4jA0A5paNd1v-zEysw', "", "", '1')
	
	addDir(localize(137),"Go-Pro",3,featherenceserviceicons_path + "se.png","Search Go-Pro Video",'1',58, getAddonFanart(background))
	CATEGORIES_RANDOM() #אקראי
	
	'''Go-Pro'''
	list = []
	list.append('&youtube_ch=GoProCamera')
	list.append('&youtube_ch=GoProMX')
	list.append('&youtube_ch=GoProTutorials')
	list.append('&youtube_ch=GoProWorldOfficial')
	list.append('&youtube_ch=GoProUncut')
	addDir('Go-Pro',list,17,'https://lh6.ggpht.com/remKtmFiZgZ3yP409xrHZNIIe9M_bV9xEdQM1IOkJw5Ep28lDGVnC7z9iqgv-PsTsHA=w300',"",'1',58, getAddonFanart(background))
	
	'''Exterme Sport'''
	addon = 'plugin.video.extreme.com'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Extreme Sport','plugin://'+addon,8,thumb,plot,addon,58, fanart)
	
	'''Bushido'''
	list = []
	list.append('&youtube_ch=UC7mIy-IFtq1k5xCAhItL_uA')
	list.append('&youtube_ch=bushidoUA')
	addDir('Bushido',list,17,'http://ru2.anyfad.com/items/t1@6d88be0e-7719-49da-beca-fdea83dd4c05/Bushido---put-voina.jpg',"",'1',58, getAddonFanart(background, default="https://i.ytimg.com/vi/9fgTFkC5yWc/maxresdefault.jpg"))