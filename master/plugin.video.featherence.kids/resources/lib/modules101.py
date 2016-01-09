# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

		
def CATEGORIES101B(General_LanguageL, background): # השירים הראשונים שלי
	'''השירים הראשונים שלי'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=6LNpGsYpWJw') #שירי ילדים
		list.append('&youtube_id=YtuVAZyWoG4') #שירי ילדים ופעוטות ברצף
		list.append('&youtube_pl=PLpnRNlRK18UaUnOabh_ZysDsOY3QLvjkd') #בייבי אוריינטל
		list.append('&youtube_pl=PL6jaO-hu0IvxLOnGOzzxXbjOR66OdFRO5') #שירי לאה גולדברג
		list.append('&youtube_pl=PL6jaO-hu0IvyOI86Wuth-gXJB2Q2BqJhA') #שירי חיים נחמן ביאליק
		list.append('&youtube_pl=PL6jaO-hu0Ivz2bnvMiXTH1o--x5XQgxN2') #שירי אריק איינשטיין
		
		
		
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL9FDA79DC8AB4A032')
		list.append('&youtube_pl=RDnUeS6gabSkE#t=39')
		list.append('&youtube_pl=PL-GVrImE8wRQ6pGSiA7-9JK4FtQzSQ9aY')
		list.append('&youtube_pl=PLqGi-5GyoD5GaQw8nlzPeO9k2jGz8sa4i')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLrRcLKqPt3gyavbDTaUxFO1l7d8yLpeOU')
		list.append('&youtube_pl=PLiot2aB_8hXmKM3LylkCUc3_-IQUUNUjA')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLQVLcmOq4Pmsdw8VO1VZGX3sm1La3wO5P1')
		list.append('&youtube_pl=PLoxgYfr5QxogVyrw78Z9REkCL7Bj_AKC_')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLnKxEDD1SooTnNjTIiVR_RBKSfS8lK1OX')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLNwxaHxrp1px3znOkmrF48-3-vQ_k9n7O')
		list.append('&youtube_pl=PLlOn3l2a68aMZgCd8PKEr7-ru3rDSlAIa')
		list.append('&youtube_pl=PL7SSS8oSHfGZg2U76Nq8J7iFokm6MHfcC')
		list.append('&youtube_pl=PLt8sqjg0DaDI1grsQ7cy9NbyPaMvNl8nd')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLAB5131587C712D86')
		list.append('&youtube_pl=PL3l5QRRFt2i3DTN9O8uDffJswsf_P97eP')
		list.append('&youtube_pl=PLqDclpzVrDJMe1tIITMxuAnULvUqGhCME')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_id=WjhQvv9kexk')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLJgmMSdWwadtTK4JzHhl5N5YR49ZVcGTK') #Songs
		list.append('&youtube_pl=PLt6kNtUbjfc9YuNnmmzcFWL-UfW38egUx') #Songs
		list.append('&youtube_pl=PLQvtMqjBV1Ay7F96lfk-HPdWiYMlhg5V2') #Songs
		list.append('&youtube_pl=PLJgmMSdWwadtTK4JzHhl5N5YR49ZVcGTK') #Songs
		list.append('&youtube_pl=PLA87EDCE79FC3FD10') #Songs
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10101).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101010).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES101C(General_LanguageL, background): # שירי ילדים
	'''שירים לילדים'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLJemWnQGr_-L-5x3AU3lphFBc4RorWue5') #שירה מקושקשת
		list.append('&youtube_pl=PL6jaO-hu0IvypWmNRJxwG8JP9S2PoDdq-') #
		list.append('&youtube_pl=PLdhkcuUltKcfTUBHVy02eKfRIEnmg7fnn')
		list.append('&youtube_pl=PL62u-p9buEf2WVr1mKj0OgRasxhe-9ZKI') #שירים לקטנטנים
		
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_id=WjhQvv9kexk')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLA87EDCE79FC3FD10') #Songs
		list.append('&youtube_pl=PL465ZjxENzxFbHTHEE4DC1jdoLPW6AzbU')
		list.append('&youtube_pl=PLU57MqhhWBpPRv1jz3_FCJWq9GzvxZNYy') #Songs
		list.append('&youtube_pl=PL_60nYyKEmHgaOaXR1HlEd4GcGnhmmvlW') #Songs
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10110).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101100).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES101D(General_LanguageL, background): # שירי לילה טוב
	'''שירי לילה טוב'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLErYJg2XgxyVYzsbPxH2dzhlWLs9sWGTa')
		list.append('&youtube_pl=PLErYJg2XgxyXTMAJvmFXoW6Qe66Ztw0Fk')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_id=WjhQvv9kexk')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10104).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101040).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES101E(General_LanguageL, background): #שירי דיסני
	'''שירי דיסני'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLCA955BD31C5CA512') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLFF5E78C1F6DD249A') #שירי דיסני
		list.append('&youtube_pl=PLF9B5B06AE8AF9F44')
		
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=PL-s48adn-YXjSIXrWs5sMxHdlS1Kw0qym') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=PLB6E1CC078D067452') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLc6OoqL0xc0ayk2bl5VY_3p-_x3M2E4w-') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=PLCE36BC8BB4712703') #שירי דיסני
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=PLSYmbyGEyJRBiQJ_i0BStz0OrY8ygNsbT') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLfH7vjpTQ7to85hnvrOauTehE73pZ5-D1') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLcHYNoAhXTuRepaK1hkUNF9OVsxv3osUO') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLiXEtCvi0UHMVTirHnhs3e1UyT3-EfnNF') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=PL1EE26AB0AC072016') #שירי דיסני
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLCC17D921DFB7B60D') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLuGgjB40DdA9fTevjAyjhQG3RBCMWNE6J') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=PLN_ZBuiVbEBnpe022Id_BrU7ELKVQBWuv') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL116E3A44431951B8') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PL51UXVpCz6llb5K-ZBOZr8BvEWF0E_oUy') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLyaw8KAXqLF8f2FkLAKJ2QIRths8R8gq2') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLydRNcreO23TxBnHkCh5FdjTTbvYaCKWU') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=PLU3dKB9nWIZ4tsTnNiIcBBvvre2T-R6uu') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PLFDGbLAKgGUU6mL-oR8cZDtenQNqM0gZ8') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL4945869F3C1A0C58') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=PLEE2B87911C60CB5A') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=PLC1_RCnvh7Ps8vHprZwjkKqzB4P7-HVCY') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=PLEoWurB6PfTPuA-G6W0GRF1pj-9g_6dKS') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL8aozOmtKmVrkAr70kP2t6j0EPz-I2SSm') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=PL0B74C49EA4578EF9') #שירי דיסני
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=PLZzjuZRUVoG-25qMwSlGO3EdtJs8L63nd') #שירי דיסני
	addDir('-' + addonString(10102).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101020).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES101I(General_LanguageL, background): #אוסף סיפורים
	'''אוסף סיפורים'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLyDbwArKjNV_8c791W2Ox9LxgSuhBaCtd')
		list.append('&youtube_pl=PL74E72320D1F7932C')
		list.append('&youtube_pl=PL6jaO-hu0Ivzi0gndI5Rb6YYcqut13wlD')
		list.append('&wallaNew=seasonId%3d2867134')
		list.append('&wallaNew=seasonId%3d2585073')
		list.append('&wallaNew=seasonId%3d2535850')
		list.append('&wallaNew=seasonId%3d2554281')
		list.append('&wallaNew=seasonId%3d2535850')
		list.append('&wallaNew=item_id%3D2526364')
		list.append('&wallaNew=item_id%3D2833303')
		list.append('&youtube_id=tl64w59Hh8E')
		list.append('&youtube_id=NPqxLDRQF3M')
		list.append('&youtube_id=CvlF7okXM2g')
		list.append('&youtube_id=uGXiT9zyYa0')
		list.append('&youtube_id=HAXPFap0P0A')
		list.append('&youtube_id=qSOsMgZ1iwk')
		list.append('&youtube_id=RCFSjBSXKHk')
		list.append('&youtube_id=QCFEPr9LLA0')
		list.append('&youtube_id=8-t8ujUVVIQ')
		list.append('&youtube_id=uGXiT9zyYa0')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%20%d7%94%d7%aa%d7%a0%22%d7%9a&url=seriesId%3d2535848')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%94%d7%a1%d7%a4%d7%a8%d7%99%d7%9d&url=seriesId%3d2554280')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%a1%d7%99%d7%a4%d7%95%d7%a8%20%d7%95%d7%a9%d7%99%d7%a8%20%d7%a9%d7%9c%20%d7%9e%d7%99%d7%a8%d7%99%d7%a7%20%d7%a9%d7%a0%d7%99%d7%a8&url=seriesId%3d2585071')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%94%d7%a1%d7%a4%d7%a8%d7%99%d7%9d%202&url=seriesId%3d2867132')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLPY-Zm_mrSakQk3oeJJZ1_oCTl-gI6vR6')
		list.append('&youtube_pl=PLPY-Zm_mrSanrLPeI9LtHemnA_mEvCHlu')
		list.append('&youtube_id=R_LAxjwHhhk')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL274CBF1217E95DC7')
		list.append('&youtube_pl=PL2p1Kj5oOcZGH90kTfikIXc1Gsq5dXD6q')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=PLshJpmmXcDiR2gz7BfjOju14az23kPPhi')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLQVLcmOq4Pmsdw8VO1VZGX3sm1La3wO5P1')
		list.append('&youtube_pl=PLoxgYfr5QxogVyrw78Z9REkCL7Bj_AKC_')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLqDclpzVrDJMJnF-oSA6u2I3dXpez42lE') #Stories
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL11CBE1CF06754974')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLxAqvvj5yysqitHC9C-rq9kdq7brJTNIQ')
		list.append('&youtube_pl=PL0E2603C29E209394')
		list.append('&youtube_id=mMmTAh4_xDc') #Ilya Muromets and Nightingale the Robber (cartoon)
			
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10107).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101070).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

def CATEGORIES101J(General_LanguageL, background): #סיפורי התנ"ך
	'''סיפורי התנ"ך'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2896127&mode=10&name=התנ"ך לילדים - שירים וסיפורים&module=wallavod')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10109).encode('utf-8'),list,17,'http://simania.co.il/bookimages/covers3/37778.jpg',addonString(101090).encode('utf-8'),'1',"", getAddonFanart(background))

def CATEGORIES101M(General_LanguageL, background): #חגים
	'''חגים'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&sdarot=season_id=1&series_id=1263&series_name=%d7%97%d7%92%d7%99%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%20%d7%a2%d7%9d%20%d7%a8%d7%99%d7%a0%d7%aa%20%d7%95%d7%9e%d7%99%d7%9e%d7%99&url=http%3a%2f%2fwww.sdarot.pm%2fwatch%2f1263%2fhagi-israel-em-rinat-vemimi-%d7%97%d7%92%d7%99-%d7%99%d7%a9%d7%a8%d7%90%d7%9c-%d7%a2%d7%9d-%d7%a8%d7%99%d7%a0%d7%aa-%d7%95%d7%9e%d7%99%d7%9e%d7%99')
		list.append('&youtube_pl=PLErYJg2XgxyVi04kFLpJ3QJQ1LDIQqYIH')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL71945E15198250DB')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=') #Stories
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10111).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(101110).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
