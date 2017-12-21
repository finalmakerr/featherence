# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''ערוצי טלוויזיה'''

def CATEGORIES10101Z():
	
	'''מוזיקה ישראלית'''
	list = []

	list.append('&youtube_ch=NMCUnitedEntertaimen')
	list.append('&youtube_ch=23music')
	list.append('&youtube_ch=livni2')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES10102Z():
	
	'''קריוקי ישראלי'''
	list = []

	list.append('&youtube_ch=sharimkaraokeltd/playlists')
	list.append('&youtube_ch=HarifKaraoke')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES10104Z():
	
	'''הופעות חיות ישראליות'''
	list = []

	list.append('&youtube_ch=michalhecht')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES10105Z():
	'''DJS'''
	list = []
	list.append('&youtube_ch=UC4XhqoxGQ1oTifJ8yRsjKnA') #The Best Sets On The Net
	list.append('&youtube_ch=TomorrowlandChannel') #Tomorrowland
	list.append('&youtube_ch=dimitrivegasonline') #Dimitri Vegas & Like Mike
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))
	
def CATEGORIES10106Z():
	'''מוזיקה מזרחית'''
	
	list = []
	se = '"addonString(30006)' + space + 'addonString(30027)"'
	list.append('&youtube_se=' + se + '&videoDefinition=high&')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES10107Z():
	'''קריוקי מזרחי'''
	
	list = []

	list.append('&youtube_ch=sharimkaraokeltd/playlists')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES10109Z():
	'''הופעות חיות מזרחיות'''
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES11101Z():
	'''מוזיקה לועזית'''
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES11102Z():
	'''קריוקי לועזי'''
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES11104Z():
	'''הופעות חיות לועזיות'''
	
	list = []

	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES11109Z():
	''''''
	
	list = []

	list.append('&youtube_ch=') #
	list.append('&youtube_ch=') #
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))
	
def CATEGORIES118Z():
	'''מוזיקה קלאסית'''
	
	list = []

	list.append('&youtube_ch=ClassicalMusicOnly/playlists')
	list.append('&youtube_ch=TopClassicalMusic/playlists')
	list.append('&youtube_ch=ClassicalMusicOn/playlists')
		
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))

def CATEGORIES114Z():
	'''תצוגות אופנה'''
	
	list = []

	list.append('&youtube_ch=FashionChannel')
	list.append('&youtube_ch=FatalefashionIII')
	list.append('&youtube_ch=MultiSabrown')
	list.append('&youtube_ch=StylebyAnna')
	list.append('&youtube_ch=SHOWstudio')
	list.append('&youtube_ch=FatalefashionIII') #FF Channel
	list.append('&youtube_ch=UCkxPf1eZSpKxY3veCPE6uNw')
	addDir('-' + addonString_servicefeatherence(32159).encode('utf-8'),list,5,featherenceserviceicons_path + 'musicbox.png',addonString_servicefeatherence(32160).encode('utf-8'),'1',0,getAddonFanart(custom=fanart))