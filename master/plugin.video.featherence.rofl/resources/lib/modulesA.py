# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''עמוד הבא'''

def CATEGORIES10101A(name, iconimage, desc, background, fanart):
	background = 101
	
	'''פספוסים'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES10102A(name, iconimage, desc, background, fanart):
	background = 102
	
	'''תוכניות'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES10103A(name, iconimage, desc, background, fanart):
	background = 103
	
	'''סטנדאפ'''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))
	
	
def CATEGORIES10104A(name, iconimage, desc, background, fanart):
	background = 104
	
	''''''
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES10105A(name, iconimage, desc, background, fanart):
	'''די ג'י ישראליים'''
	background = 105
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))
	
def CATEGORIES10106A(name, iconimage, desc, background, fanart):
	''''''
	background = 106
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES10107A(name, iconimage, desc, background, fanart):
	''''''
	background = 107
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES10109A(name, iconimage, desc, background, fanart):
	''''''
	background = 108
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES11101A(name, iconimage, desc, background, fanart):
	''''''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES11102A(name, iconimage, desc, background, fanart):
	''''''
	background = 111
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES11104A(name, iconimage, desc, background, fanart):
	''''''
	background = 114
	
	list = []

	list.append('&youtube_ch=')

		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))

def CATEGORIES11105A(name, iconimage, desc, background, fanart):
	''''''
	background = 115
	
	list = []

	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))
	
def CATEGORIES118A(name, iconimage, desc, background, fanart):
	''''''
	background = 118
	
	list = []
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',50, getAddonFanart(background, custom=fanart))