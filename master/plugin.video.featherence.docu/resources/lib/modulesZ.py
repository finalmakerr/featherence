# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''ערוצי טלוויזיה'''

def CATEGORIES101Z(name, iconimage, desc, background, fanart):
	'''טבע'''
	background = 101
	list = []
	list.append('&youtube_ch=BBCEarth')
	list.append('&youtube_ch=AnimalPlanetTV')
	list.append('&youtube_ch=UC1BOeEP9-jiSmvME99fneQA/playlists')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10101Z(name, iconimage, desc, background, fanart):
	'''טבע - חיות'''
	background = 10101
	
	list = []
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10102Z(name, iconimage, desc, background, fanart):
	'''טבע - חוקי טבע'''
	background = 10102
	
	list = []
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))
	
def CATEGORIES10103Z(name, iconimage, desc, background, fanart):
	'''טבע - מקומות'''
	background = 10103
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES102Z(name, iconimage, desc, background, fanart):
	'''חלל'''
	background = 102
	
	list = []
	
	list.append('&youtube_ch=NASAtelevision')
	list.append('&youtube_ch=spacelab')
	list.append('&youtube_ch=VideoFromSpace')
	list.append('&youtube_ch=UC7_gcs09iThXybpVgjHZ_7g')
	list.append('&youtube_ch=scishowspace')
	list.append('&youtube_ch=canadianspaceagency')
	list.append('&youtube_ch=HubbleSiteChannel')
	list.append('&youtube_ch=UCmBobPZzLEOQ71AtLwnuntw')
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))
	
def CATEGORIES103Z(name, iconimage, desc, background, fanart):
	'''היסטוריה'''
	background = 103
	
	list = []

	list.append('&youtube_ch=UCQGjxZRfQ8Bt6rnudw2kgUQ')
	list.append('&youtube_ch=UCErKUCncCyBgEdxWAtrj5hg')
	list.append('&youtube_ch=AlternateHistoryHub')
	list.append('&youtube_ch=UC5xIAFuCs4m2S4uPY9dp_Ww')
	list.append('&youtube_ch=BlastfromthePast')
	list.append('&youtube_ch=TheGreatWar')
	list.append('&youtube_ch=UCBcIe5EBAxqK267uyEVibFw')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES104Z(name, iconimage, desc, background, fanart):
	'''מדע'''
	background = 104
	
	list = []
	
	list.append('&youtube_ch=1veritasium')
	list.append('&youtube_ch=CGPGrey')
	list.append('&youtube_ch=UC6107grRI4m0o2-emgoDnAA')
	list.append('&youtube_ch=vsauce')
	list.append('&youtube_ch=AsapSCIENCE')
	list.append('&youtube_ch=scishow')
	list.append('&youtube_ch=crashcourse')
	list.append('&youtube_ch=numberphile')
	list.append('&youtube_ch=education')
	list.append('&youtube_ch=grossscienceshow')
	list.append('&youtube_ch=periodicvideos')
	list.append('&youtube_ch=SteveSpanglerScience')
	list.append('&youtube_ch=CrazyRussianHacker')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10401Z(name, iconimage, desc, background, fanart):
	'''מדע - חברתי'''
	background = 10401
	
	list = []

		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10402Z(name, iconimage, desc, background, fanart):
	'''מדע - טבע'''
	background = 10402
	
	list = []
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10403Z(name, iconimage, desc, background, fanart):
	'''מדע - טכנולוגיה'''
	background = 10403
	
	list = []

	list.append('&youtube_ch=UC76oOi1L0BOsLome8P-mBnw')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES107Z(name, iconimage, desc, background, fanart):
	'''ילדים'''
	background = 107
	
	list = []
	list.append('&youtube_ch=scishowkids')
	list.append('&youtube_ch=crashcoursekids')
	list.append('&youtube_ch=KidsAnimalChannel')
	list.append('&youtube_ch=makemegenius')
	list.append('&youtube_ch=Smartlearningforall')
	list.append('&youtube_ch=hooplakidzlab')
	list.append('&youtube_ch=cUCXVCgDuD_QCkI7gTKU7-tpg')
	list.append('&youtube_ch=UCB_2_OiPFh6FdUvp50_maug')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES11105Z(name, iconimage, desc, background, fanart):
	''''''
	background = 115
	
	list = []

	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
	list.append('&youtube_ch=')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

	
def CATEGORIES110Z(name, iconimage, desc, background, fanart):
	'''אומנות'''
	background = 110
	
	list = []
	list.append('&youtube_ch=markcrilley')
	list.append('&youtube_ch=PESfilm')
	list.append('&youtube_ch=ChrisSamba22')
	list.append('&youtube_ch=EclecticAsylumArt')
	list.append('&youtube_ch=idrawgirls/')
	list.append('&youtube_ch=daarken')
	list.append('&youtube_ch=3dsMaxHowTos')
	list.append('&youtube_ch=CGArtSuccess')
	list.append('&youtube_ch=bluefley00')
	list.append('&youtube_ch=bedavellis')
	list.append('&youtube_ch=AlexanderKoshelkov')
	list.append('&youtube_ch=arieldiaz3d')
	list.append('&youtube_ch=iceblazer17')
	list.append('&youtube_ch=tate')
	list.append('&youtube_ch=smarthistoryvideos')
	list.append('&youtube_ch=guggenheim')
	list.append('&youtube_ch=MoMAvideos')
	list.append('&youtube_ch=UCLCHcL4M0xSwPeEuKGrsGkg')
	list.append('&youtube_ch=Sycra')
	list.append('&youtube_ch=WilliamsShamir')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))
	
def CATEGORIES108Z(name, iconimage, desc, background, fanart):
	'''בעברית'''
	background = 108
	
	list = []

	list.append('&youtube_id=eIOvF0MlMe0')
	list.append('&youtube_id=TOeT5DQSRDc')
	list.append('&youtube_ch=VGVK6cqjoj6Aeyi2x7yQqo0S9Pq8CkZ')
	list.append('&youtube_ch=PL51YAgTlfPj6s0QtcgOpIwKewkEeSN77e')
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))

def CATEGORIES10801Z(name, iconimage, desc, background, fanart):
	'''בעברית - ילדים'''
	background = 10801
	
	list = []
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (name),list,17,featherenceserviceicons_path + 'tv.png',addonString_servicefeatherence(32082).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart))
	