# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''


def CATEGORIES109B(General_LanguageL, background): # לימוד שפה
	'''לימוד שפה'''
	
	'''עברית'''
	list = []
	if 'Hebrew' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLMtuxpU4MU-v9oDKLI3shidKa7cN9Nx0o')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),list,17,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
		
	'''אנגלית'''
	list = []
	if 'English' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_ch=UC43wDpoNIpAK2NYfMz1m0Ow')
		list.append('&youtube_ch=UCGwA4GjY4nGMIYvaJiA0EGA')
		list.append('&youtube_pl=PLii5rkhsE0Lc5f1FhF8l-QSDo7XO-0FkG')
		list.append('&youtube_pl=PLii5rkhsE0LdLIVU8_SxHpEXOHvnYENtP')
		list.append('&youtube_pl=PL7CC99F5923D2C971')
		list.append('&youtube_pl=PLxBVrUZUpjI34etgFUUTl2NpGFj1NWZxo')
		list.append('&youtube_pl=PLtUvIcNPXN5-MzCyIXiYgF8Mod2u6eJ2Y')
		list.append('&youtube_pl=PLEA969B1FD7AF939D')
		list.append('&youtube_id=BGa3AqeqRy0')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),list,17,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',50, getAddonFanart(200,custom=""))

	'''אוזבקית'''
	list = []
	if 'Uzbek' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),list,17,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	list = []
	if 'Italian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLMtuxpU4MU-uFtoglNO17szlngoagKuxk')
		list.append('&youtube_pl=PLlBlltNtETtSNVJZWv4_-00hpdtAT0QiU')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),list,17,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	list = []
	if 'Ukrainian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLElG6fwk_0Um8qp98ffY-BJeszcj1WSym')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),list,17,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אינדונזית'''
	list = []
	if 'Indonesian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),list,17,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''אירית'''
	list = []
	if 'Irish' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),list,17,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	list = []
	if 'Bulgarian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),list,17,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	list = []
	if 'Georgian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),list,17,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	list = []
	if 'German' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PL4GK4WMveoGCB9Wt_82b8kgJXCyWHIBt6')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),list,17,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	list = []
	if 'Hindi' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),list,17,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',50, getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	list = []
	if 'Dutch' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLxBVrUZUpjI2s8cLUf6ODFeAoFSADWde3')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),list,17,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	list = []
	if 'Hungarian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),list,17,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''טורקית'''
	list = []
	if 'Turkish' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),list,17,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	list = []
	if 'Japanese' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),list,17,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סינית'''
	list = []
	if 'Chinese' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLtUvIcNPXN5_OBnuhPEhFk1lRQIV2SgxG')
		list.append('&youtube_pl=PL78EBE97DAEDCFAF7')
		list.append('&youtube_pl=PLC30E4E4C09488D3F')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),list,17,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	list = []
	if 'Slovak' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),list,17,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
		
	'''ספרדית'''
	list = []
	if 'Spanish' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLEBEa1iebZw-KpIR675vK8L1zDDQQL-uR')
		list.append('&youtube_pl=PL0YJlHE4h7Wyt4YPyPBfW07PRyj3JbrNx')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),list,17,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''סרבית'''
	list = []
	if 'Serbian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),list,17,"http://www.flagsinformation.com/serbian-flag.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פולנית'''
	list = []
	if 'Polish' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),list,17,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	list = []
	if 'Portuguese' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),list,17,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''פינית'''
	list = []
	if 'Finnish' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),list,17,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))

	'''ערבית'''
	list = []
	if 'Arabic' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),list,17,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	list = []
	if 'French' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PL8gT5mi6j6CwGWl1h5YcVHJnvvtW0ijYo')
		list.append('&youtube_pl=PL8Mfzkj8FPJtDByM2jNim7xwGOv2mZup3')
		list.append('&youtube_pl=PLXkC9K2nb2kAfBZy_U3EFP2h8HUrM2DX3')
		list.append('&youtube_pl=PLMtuxpU4MU-vyJEufkLNGU0iQRm2PaKWt')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),list,17,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	list = []
	if 'Korean' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),list,17,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קזחית'''
	list = []
	if 'Kazakh' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),list,17,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	list = []
	if 'Catalan' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),list,17,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	list = []
	if 'Haitian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),list,17,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רומנית'''
	list = []
	if 'Romanian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),list,17,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''רוסית'''
	list = []
	if 'Russian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLCsBweb0jQ6R7YQqVQTkm3tsYGeOvLb3n')
		list.append('&youtube_pl=PLUaNnetAtmpc_DHLYVT5TPZtm3OkzC5_2')
		list.append('&youtube_pl=PLQce85Dx-J0O9N4QxRz8YI2OIxE4283r5')
		list.append('&youtube_pl=PLVRSbh2c6m9Awf9YVemQmVnvZYneNJi8h')
		list.append('&youtube_pl=PL9O9DK5Lv6JbKp6ti5PG840z1oDYGss9-')
		list.append('&youtube_pl=PLIJoHarO8SfenfyDbaLeNiYG1916BaD4-')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),list,17,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	list = []
	if 'Thai' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=')
	addDir('-' + addonString(10901).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),list,17,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(109010).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',50, getAddonFanart(200, custom=""))
