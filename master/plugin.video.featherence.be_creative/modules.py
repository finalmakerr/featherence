# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''
	
def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	CATEGORIES_SEARCH(mode=30, url="")
	addDir('-' + addonString(100).encode('utf-8'),'',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',50, getAddonFanart(100, urlcheck_=True)) #My ?
	
	addDir('test','',101,featherenceserviceicons_path + 'music.png','description','1',58, getAddonFanart(101, default="http://p1.pichost.me/i/28/1509965.jpg", urlcheck_=True))

def CATEGORIES100(name, iconimage, desc, fanart):
	'''------------------------------
	---My-?--------------------------
	------------------------------'''
	fanart = 100
	
	'''כפתור ה-? שלי'''
	addDir(addonString_servicefeatherence(86).encode('utf-8') % (addonString(100).encode('utf-8')),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(87).encode('utf-8') + addonString_servicefeatherence(88).encode('utf-8') + addonString_servicefeatherence(89).encode('utf-8'),'s',50, getAddonFanart(fanart, urlcheck_=True))
		
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',50, getAddonFanart("Custom_Playlist1", urlcheck_=True))
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',50, getAddonFanart("Custom_Playlist2", urlcheck_=True))
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',50, getAddonFanart("Custom_Playlist3", urlcheck_=True))
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',50, getAddonFanart("Custom_Playlist4", urlcheck_=True))
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',50, getAddonFanart("Custom_Playlist5", urlcheck_=True))
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',50, getAddonFanart("Custom_Playlist6", urlcheck_=True))
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',50, getAddonFanart("Custom_Playlist7", urlcheck_=True))
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',50, getAddonFanart("Custom_Playlist8", urlcheck_=True))
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',50, getAddonFanart("Custom_Playlist9", urlcheck_=True))
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',50, getAddonFanart("Custom_Playlist10", urlcheck_=True))
	
	'''מעודפים'''
	addDir(localize(1036),"",32,featherenceserviceicons_path + 'star.png','','1',50, getAddonFanart(fanart, urlcheck_=True))

def CATEGORIES101(name, iconimage, desc, fanart):
	background = 101
	list = []
	list.append('&youtube_ch=finalmakerr')
	list.append('&youtube_pl=PLGnTTJWIWt4dcv7Z_cLyZVERGWsuHIt18')
	list.append('&youtube_id=WFwHq6cY040')
	list.append('&youtube_se=Featherence')
	list.append('&dailymotion_pl=x3qyi3')
	list.append('&dailymotion_id=x2aps1v')
	list.append('&sdarot=series_id=815&series_name=%d7%90%d7%92%d7%93%d7%95%d7%aa%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%a9%d7%9c%d7%9e%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f815%2ftales-of-a-wise-king-hebdub-%d7%90%d7%92%d7%93%d7%95%d7%aa-%d7%94%d7%9e%d7%9c%d7%9a-%d7%a9%d7%9c%d7%9e%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	list.append('&custom8=plugin://plugin.video.extreme.com')
	list.append('&custom4=http://62.90.90.56/walla_vod/_definst_/mp4:media/015/242/1524273-40.mp4/playlist.m3u8')
	list.append('&direct4=http://www.supercartoons.net/video/1208/jeepers-its-the-creeper.mp4')
	list.append('&googledrive=0B3qBRwW3mJUBdXZYbGYyaHUtYXc')
	addDir('test',list,17,'https://lh6.ggpht.com/remKtmFiZgZ3yP409xrHZNIIe9M_bV9xEdQM1IOkJw5Ep28lDGVnC7z9iqgv-PsTsHA=w300',"description",'1',50, getAddonFanart(background,custom="https://lh6.ggpht.com/remKtmFiZgZ3yP409xrHZNIIe9M_bV9xEdQM1IOkJw5Ep28lDGVnC7z9iqgv-PsTsHA=w300"))
	
	addon = 'plugin.audio.jango'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('test2','plugin://'+addon,8,thumb,plot,addon,"", getAddonFanart(background, custom=fanart))