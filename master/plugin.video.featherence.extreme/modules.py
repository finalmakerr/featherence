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
	
	addDir(localize(137),"Go-Pro",3,featherenceserviceicons_path + "se.png","Search Go-Pro Video",'1',58, getAddonFanart(background))
	CATEGORIES_RANDOM() #אקראי
	
	'''Bushido'''
	list = []
	list.append('&youtube_ch=UC7mIy-IFtq1k5xCAhItL_uA')
	list.append('&youtube_ch=bushidoUA')
	addDir('Bushido',list,17,'http://ru2.anyfad.com/items/t1@6d88be0e-7719-49da-beca-fdea83dd4c05/Bushido---put-voina.jpg',"getAPIdata",'&getAPIdata=&youtube_ch=bushidoUA',58, getAddonFanart(background, default="https://i.ytimg.com/vi/9fgTFkC5yWc/maxresdefault.jpg"))
	
	'''Exterme Sport'''
	addon = 'plugin.video.extreme.com'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Extreme Sport','plugin://'+addon,8,thumb,plot,addon,58, getAddonFanart(background,default=fanart, custom=""))
	
	'''Go-Pro'''
	list = []
	list.append('&youtube_ch=GoProCamera')
	list.append('&youtube_ch=GoProMX')
	list.append('&youtube_ch=GoProTutorials')
	list.append('&youtube_ch=GoProWorldOfficial')
	list.append('&youtube_ch=GoProUncut')
	addDir('Go-Pro',list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=GoProCamera',58, getAddonFanart(background, default='getAPIdata', custom="https://i.vimeocdn.com/video/531419538.jpg?mw=1920&mh=1080&q=70"))
	
	'''Masters of Dirt'''
	list = []
	list.append('&youtube_ch=mastersofdirt')
	addDir('getAPIdata',list,17,'getAPIdata',"getAPIdata",'&getAPIdata=&youtube_ch=mastersofdirt',58, getAddonFanart(background, default='getAPIdata', custom="http://static.wixstatic.com/media/575ae7_2ac792df7f324d03ad555e8afef8972a.jpg"))
	
	
	'''XTreme'''
	list = []
	list.append('&youtube_ch=XTremeVideo')
	addDir('getAPIdata',list,17,'getAPIdata',"getAPIdata",'&getAPIdata=&youtube_ch=XTremeVideo',58, getAddonFanart(background, default='getAPIdata', custom="https://i.ytimg.com/vi/m54vzZNGpyc/maxresdefault.jpg"))
	
	
	