# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

def CATEGORIES101Z(General_LanguageL, background, background2): #פספוסים
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))
	
	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=supersimplejapanese') #SuperSimpleSongs
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

def CATEGORIES102Z(General_LanguageL, background, background2): #תוכניות
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=tzchokmeavoda') #צחוק מהעבודה
		list.append('&youtube_ch=AnythingGoesIsrael') #הכל הולך
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
		
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

def CATEGORIES103Z(General_LanguageL, background, background2): #סטנדאפיסטים
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCHaEhu1lOjCfHSHg_R2dpkg') #סטנדאפ ישראל
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))	
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

def CATEGORIES104Z(General_LanguageL, background, background2): #
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

def CATEGORIES105Z(General_LanguageL, background, background2): #ערוצי טלוויזיה (סרטים)
	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערוצי טלוויזיה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(background,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_ch=') #
		list.append('&youtube_ch=ukranima/playlists') #Ukranima
	
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''דנית'''
	list = []
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),list,17,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(background, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יוונית'''
	list = []
	if 'Greek' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),list,17,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צ'כית'''
	list = []
	if 'Czech' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),list,17,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''שוודית'''
	list = []
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_ch=')
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),list,17,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))
	
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_ch=') #
	addDir('-' + addonString_servicefeatherence(32089).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString_servicefeatherence(32082).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(background, custom="", default=background2))

	