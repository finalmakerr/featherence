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
	
	addDir(localize(137),"Go-Pro",3,featherenceserviceicons_path + "se.png","Search Go-Pro Video",'1',0, '')
	CATEGORIES_RANDOM() #אקראי

	'''Go-Pro'''
	thumb = 'http://www.wallpaperinhd.net/file/1958/600x338/16:9/gopro-logo-2100x915-wallpaper_1268410383.jpg'
	fanart = 'https://i.ytimg.com/vi/mrNo5V441so/maxresdefault.jpg'
	list = []
	list.append('&youtube_ch=GoProCamera')
	#list.append('&youtube_ch=GoProMX')
	#list.append('&youtube_ch=GoProTutorials')
	#list.append('&youtube_ch=GoProWorldOfficial')
	#list.append('&youtube_ch=GoProUncut')
	c8 = 'plugin://plugin.video.extreme.com/' ; list.append('&name_=' + 'Extreme Sport' + '&&custom8='+c8)
	ch = 'XTremeVideo' ; list.append('&name_=' + 'XTremeVideo' + '&&youtube_ch='+ch)
	addDir('Go-Pro',list,17,thumb,'getAPIdata','&getAPIdata=&youtube_ch=GoProCamera',0, fanart)

	'''Motorcycles & Cars'''
	thumb = 'https://i.pinimg.com/736x/a9/f4/8b/a9f48b833ed986eb00ebec084118ee23--car-wallpapers-hd-wallpaper.jpg'
	fanart = 'https://www.bikerpunks.com/media/gallery/motorcycle-vs-car-hd-1920x1080.jpg'
	list = []
	se = 'motorcycles / cars drifting stunts' ; list.append('&name_=' + 'WoW!' + '&&youtube_se='+se)
	se = 'CAR MOTORCYCLE RACE VS' ; list.append('&name_=' + 'addonString(30020)' + '&&youtube_se='+se)
	addDir(addonString(30001).encode('utf-8'),list,17,thumb,'www.featherence.com','1',0, fanart)
	
	'''Martial Arts'''
	thumb = 'https://meetyourmartialartsinstructor.files.wordpress.com/2012/06/artes_marciais.jpg'
	fanart = 'https://images2.alphacoders.com/233/233850.jpg'
	list = []
	se = 'K1 FULL FIGHTS' ; list.append('&name_=' + 'K1' + '&&youtube_se='+se + '&videoDuration=long&')
	se = 'BUSHIDO FULL FIGHTS -flight -game -mma -movie -book -pisode' ; list.append('&name_=' + 'Bushido' + '&&youtube_se='+se + '&videoDuration=long&' + '&videoDefinition=any&')
	se = 'MMA FULL FIGHTS' ; list.append('&name_=' + 'MMA' + '&&youtube_se='+se + '&videoDuration=long&')
	se = 'SUMO FULL FIGHTS' ; list.append('&name_=' + 'Sumo' + '&&youtube_se='+se + '&videoDuration=long&')
	se = 'UFC FULL FIGHTS -PRESS CONFERENCE' ; list.append('&name_=' + 'UFC' + '&&youtube_se='+se + '&videoDuration=long&')
	addDir(addonString(30003).encode('utf-8'),list,17,thumb,'www.featherence.com','1',0, fanart)

