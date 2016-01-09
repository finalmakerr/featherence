# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

def CATEGORIES101Z(General_LanguageL, background): #ערוצי טלוויזיה (שירים וסיפורים לילדים)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=TheChuChuTV/playlists') #ערוץ צ'ו-צ'ו
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=UCBbsyG0o_cWlyY46ZRSdYJg/playlists') #ערוץ צ'ו-צ'ו
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES102Z(General_LanguageL, background): #ערוצי טלוויזיה (
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES103Z(General_LanguageL, background): #ערוצי טלוויזיה
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES104Z(General_LanguageL, background): #ערוצי טלוויזיה (סדרות)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES105Z(General_LanguageL, background): #ערוצי טלוויזיה (סרטים)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=getmovies/playlists') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES106Z(General_LanguageL, background): #ערוצי טלוויזיה (פעוטות)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('youtube_ch=UCj10fKNd5h64J_M9YIQu0Zw/playlists')
		list.append('&youtube_ch=UCl0jQT2Cj5brTRt5azL5E6g') #ג'וניור
		list.append('&youtube_ch=UClZXqxeY540_Epab3WDHFGw/playlists') #הופ!
		list.append('&youtube_ch=UCfNjGgy-3XfTzgWoGMt_QOw/playlists') #הופ!
		list.append('youtube_ch=UC8Zlrwmbc3-AjrjTxzqL7Uw/playlists') #צופי
		#ערוץ ניקלודיאון גוניור
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('youtube_ch=UCGxnmQJquvQwlV_ICDfAKNA/playlists')
		list.append('&youtube_ch=') #ערוץ ניקלודיאון גוניור
		list.append('&youtube_ch=UCKcQ7Jo2VAGHiPMfDwzeRUw/playlists') #ערוץ צ'ו-צ'ו
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('youtube_ch=UC4OcQbL1ZRfAhqiOLkyANew/playlists')
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('youtube_ch=BabyTVNederlands/playlists') #Baby TV
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLWo4IqXs7qRCNWAihXvq54pemNXgiw74R') #Baby TV
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('youtube_ch=BabyTVTurkish/playlists') #Baby TV
		list.append('&youtube_ch=') #
		list.append('&youtube_ch=adisebabatv/playlists') #ערוץ עליבאבא
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('youtube_ch=BabyTVGreek/playlists') #Baby TV
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('youtube_ch=babytvjapanese/playlists') #Baby TV
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
		list.append('youtube_ch=babytvspanish/playlists') #Baby TV
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
		list.append('youtube_ch=BabyTVPolski/playlists') #Baby TV
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('youtube_ch=BabyTVBrazil/playlists') #Baby TV
		list.append('youtube_ch=BabyTVPortugues/playlists') #Baby TV
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('youtube_ch=BabyTVArabic/playlists') #Baby TV
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('youtube_ch=BabyTVFrench/playlists') #Baby TV
		list.append('&youtube_ch=nickelodeonjuniorfr/playlists') #ערוץ ניקלודיאון גוניור
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('youtube_ch=BabyTVRussian/playlists')
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES107Z(General_LanguageL, background): #ערוצי טלוויזיה (קטנטנים)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
		list.append('&youtube_ch=MinidiscoUK/playlists') #ערוץ מינידיסקו
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=UChIwMYwfK1S-P1DTtAKIs3A/playlists') #ערוץ מינידיסקו
		list.append('&youtube_ch=') #
		
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=UCRWlUS-tveicl_GxQ6vsCRg/playlists') #ערוץ טיטונוס
		list.append('&youtube_ch=ddcompany/playlists') #ערוץ מינידיסקו
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=UCTpAjwOrvCySeZBfsMXfD9Q/playlists') #ערוץ מינידיסקו
		list.append('&youtube_ch=AnimakidsTV') #AnimakidsTV
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=MinidiscoNL/playlists') #ערוץ מינידיסקו
		list.append('&youtube_ch=ssebastienn/playlists') #ערוץ טיטונוס
		list.append('&youtube_ch=UCCzFnM_wVA6OF_6o4TVPMcQ/playlists') #ערוץ טיטונוס
		list.append('&youtube_ch=UCbExdKOgxC4YQMHjrcGEfCQ/playlists') #ערוץ טיטונוס
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=MinidiscoRU/playlists') #ערוץ מינידיסקו
		list.append('&youtube_ch=UCIOwKErxRgAWecQrVVax2MA/playlists') #רכבות מChaggingtona
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES108Z(General_LanguageL, background): #ערוצי טלוויזיה (ילדים ונוער)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCYFLZdLRZGnmKQBH6RB8IjA/playlists') #ערוץ החינוכית
		list.append('&youtube_ch=UCOFp2_GttW3ljCuOc7r4l7g/playlists') #ערוץ הילדים
		#ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=Nickelodeon/playlists') #ערוץ ניקלודיאון
		list.append('&youtube_ch=UCHiceVclOIFCgAcveITRLLw/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=UCsHe74knLccbgec6WdGAkPQ/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=OfficialNickIndia/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=nickelodeonoffiziell/playlists')
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=mundonickelodeon/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=UCBgfqkarug1n6eM5yqsUwDg/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=canalnickelodeonpt/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=TheNickelodeonarabia/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=nickelodeonfr/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=UCv8R8vF9lR_A_zhu5VOP2iA/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=UCOudV7aMMSQl2GiD-SVNIew/playlists') #ערוץ ניקלודיאון
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=promonickrus/playlists') #ערוץ ניקלודיאון
		list.append('&youtube_ch=UCItWLjJyvP4VZVe6lkBDsog/playlists') #האבות של קריקטורות חינוכיות
		
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES109Z(General_LanguageL, background): #ערוצי טלוויזיה
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32900).encode('utf-8'),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32901).encode('utf-8'),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32929).encode('utf-8'),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32909).encode('utf-8'),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
		list.append('&youtube_ch=ukranima/playlists') #Ukranima
	
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32903).encode('utf-8'),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32927).encode('utf-8'),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32912).encode('utf-8'),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32928).encode('utf-8'),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32906).encode('utf-8'),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32920).encode('utf-8'),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32923).encode('utf-8'),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32902).encode('utf-8'),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32921).encode('utf-8'),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32916).encode('utf-8'),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32911).encode('utf-8'),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32907).encode('utf-8'),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32917).encode('utf-8'),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32908).encode('utf-8'),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32915).encode('utf-8'),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32922).encode('utf-8'),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32918).encode('utf-8'),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32925).encode('utf-8'),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32926).encode('utf-8'),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32904).encode('utf-8'),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32913).encode('utf-8'),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32930).encode('utf-8'),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32919).encode('utf-8'),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32924).encode('utf-8'),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32914).encode('utf-8'),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32905).encode('utf-8'),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + localize(19023) + space + localize(19107) + space + addonString_servicefeatherence(32910).encode('utf-8'),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	