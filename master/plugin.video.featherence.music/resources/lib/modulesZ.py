# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''ערוצי טלוויזיה'''

def CATEGORIES10101Z(name, iconimage, desc, background, fanart):
	background = 101
	
	'''מוזיקה ישראלית'''
	list = []

	list.append('&youtube_ch=NMCUnitedEntertaimen')
	list.append('&youtube_ch=23music')
	list.append('&youtube_ch=livni2')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES10102Z(name, iconimage, desc, background, fanart):
	background = 102
	
	'''קריוקי ישראלי'''
	list = []

	list.append('&youtube_ch=sharimkaraokeltd/playlists')
	list.append('&youtube_ch=HarifKaraoke')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES10104Z(name, iconimage, desc, background, fanart):
	background = 104
	
	'''הופעות חיות ישראליות'''
	list = []

	list.append('&youtube_ch=michalhecht')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES10105Z(name, iconimage, desc, background, fanart):
	'''די ג'י ישראליים'''
	background = 105
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))
	
def CATEGORIES10106Z(name, iconimage, desc, background, fanart):
	'''מוזיקה מזרחית'''
	background = 106
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES10107Z(name, iconimage, desc, background, fanart):
	'''קריוקי מזרחי'''
	background = 107
	
	list = []

	list.append('&youtube_ch=sharimkaraokeltd/playlists')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES10109Z(name, iconimage, desc, background, fanart):
	'''הופעות חיות מזרחיות'''
	background = 108
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES11101Z(name, iconimage, desc, background, fanart):
	'''מוזיקה לועזית'''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES11102Z(name, iconimage, desc, background, fanart):
	'''קריוקי לועזי'''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES11104Z(name, iconimage, desc, background, fanart):
	'''הופעות חיות לועזיות'''
	background = 114
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))

def CATEGORIES11105Z(name, iconimage, desc, background, fanart):
	'''די ג'י לועזיים'''
	background = 115
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))
	
def CATEGORIES118Z(name, iconimage, desc, background, fanart):
	'''מוזיקה קלאסית'''
	background = 118
	
	list = []

	list.append('&youtube_ch=ClassicalMusicOnly/playlists')
	list.append('&youtube_ch=TopClassicalMusic/playlists')
	list.append('&youtube_ch=ClassicalMusicOn/playlists')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1','0',getAddonFanart(background, custom=fanart))