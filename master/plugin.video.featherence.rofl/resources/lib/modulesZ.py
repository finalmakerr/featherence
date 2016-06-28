# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''ערוצי טלוויזיה'''

def CATEGORIES10101Z(name, iconimage, desc, background, fanart):
	background = 101
	
	'''פספוסים'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES10102Z(name, iconimage, desc, background, fanart):
	background = 102
	
	'''תוכניות'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES10103Z(name, iconimage, desc, background, fanart):
	background = 103
	
	'''סטנדאפ'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))
	
	
def CATEGORIES10104Z(name, iconimage, desc, background, fanart):
	background = 104
	
	''''''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES10105Z(name, iconimage, desc, background, fanart):
	'''די ג'י ישראליים'''
	background = 105
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))
	
def CATEGORIES10106Z(name, iconimage, desc, background, fanart):
	''''''
	background = 106
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES10107Z(name, iconimage, desc, background, fanart):
	''''''
	background = 107
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES10109Z(name, iconimage, desc, background, fanart):
	''''''
	background = 108
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES11101Z(name, iconimage, desc, background, fanart):
	''''''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES11102Z(name, iconimage, desc, background, fanart):
	''''''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES11104Z(name, iconimage, desc, background, fanart):
	''''''
	background = 114
	
	list = []

	list.append('&youtube_ch=')

		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))

def CATEGORIES11105Z(name, iconimage, desc, background, fanart):
	''''''
	background = 115
	
	list = []

	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))
	
def CATEGORIES118Z(name, iconimage, desc, background, fanart):
	''''''
	background = 118
	
	list = []
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, custom=fanart))