#-*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

#list.append('&youtube_pl=PL618DEA0E28636BC2') #Yu-Gi-Oh!
	
'''104'''
def CATEGORIES104B(General_LanguageL, background, background2): #פריקבוי וצ'אם צ'אם
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/160861-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/160861-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f4%f8%e9%f7%e1%e5%e9%20%e5%f6%27%e0%ed%20%f6%27%e0%ed&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1778310')
		list.append('&youtube_id=TpuVTMAktUc')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLRa0vFtcoHevRtQPnBJEJsq7WStrZhM5B') #S2
		list.append('&youtube_pl=PLhbx1Utemog4VPnw_UgSLs_gYZMTpXLE7')
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
		list.append('&youtube_pl=PL_nR8tuy6O1NuYIM2otOy7qSXw6Q81AY2')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10762).encode('utf-8'),list,17,thumb,addonString(107620).encode('utf-8'),'1',0,fanart)

def CATEGORIES104C(General_LanguageL, background, background2): #פלאנט שין
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/195041-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/195041-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f4%ec%e0%f0%e8%20%f9%e9%ef&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1849206')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLg5g_Q8udSqCaVqHfnIiHuVY_7DwkTTCz')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10483).encode('utf-8'),list,17,thumb,addonString(104830).encode('utf-8'),'1',0,fanart)

def CATEGORIES104D(General_LanguageL, background, background2): #ג'ימי ניוטרון
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/77612-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77612-1.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e2%27%e9%ee%e9%20%f0%e9%e5%e8%f8%e5%ef&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1688219')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLjDLgg_nO1v6cN1VUCVKfxPl1nVnTH8I8') #S1
		list.append('&youtube_pl=PLqP78Cshv1ykbs2x0zQm67wpSLauECvA0')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10484).encode('utf-8'),list,17,thumb,addonString(104840).encode('utf-8'),'1',0,fanart)

def CATEGORIES104E(General_LanguageL, background, background2): #משוגעגע
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/278482-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/278482-3.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ee%f9%e5%e2%f2%e2%f2&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2802800')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLB-ixs1gngUMEOU8Wx9j3Y5dpvo2igxkv') #S1
		list.append('&youtube_pl=PLa2x65y820ZQv_Zy8Iy5LE1oP4HyjVFkS')
		list.append('&youtube_pl=PLhdYefsmYuxacwKkayAxxtVnPEXF2QJuS')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLwLVa1RYGXSTOF3NpCLtuOJ3EFCQcMyjJ')
	
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

	addDir(addonString(10485).encode('utf-8'),list,17,thumb,addonString(104850).encode('utf-8'),'1',0,fanart)

def CATEGORIES104F(General_LanguageL, background, background2): #הנוקמים: לוחמי העל
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/192171-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/192171-5.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1677.jpg&mode=3&name=%d7%94%d7%a0%d7%95%d7%a7%d7%9e%d7%99%d7%9d-%d7%9c%d7%95%d7%97%d7%9e%d7%99-%d7%94%d7%a2%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-avengers-earth-s-mightiest-heroes%2fseason%2f1&series_id=1677&series_name=%d7%94%d7%a0%d7%95%d7%a7%d7%9e%d7%99%d7%9d-%d7%9c%d7%95%d7%97%d7%9e%d7%99-%d7%94%d7%a2%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-avengers-earth-s-mightiest-heroes%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1677%2f%d7%94%d7%a0%d7%95%d7%a7%d7%9e%d7%99%d7%9d-%d7%9c%d7%95%d7%97%d7%9e%d7%99-%d7%94%d7%a2%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-avengers-earth-s-mightiest-heroes%2fseason%2f1')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F52%2Fimage%2F555x418%2Favenger_earths_mightiest_heroes.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Avengers%3A%20Earths%20Mightiest%20Heroes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-avengers-earth-s-mightiest-heroes')
		list.append('&youtube_pl=PL3pJWvlMAbHh97E0hvpbEbhDcBE4o7prU') #S1
		list.append('&youtube_pl=PL3pJWvlMAbHhhgf91BsqiGochD6yhbXY1') #S2
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10488).encode('utf-8'),list,17,thumb,addonString(104880).encode('utf-8'),'1',0,fanart)

def CATEGORIES104G(General_LanguageL, background, background2): #מלחמת הכוכבים: המורדים
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/283468-12.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/283468-13.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1362.jpg&mode=3&name=star-wars-rebels-%d7%9e%d7%9c%d7%97%d7%9e%d7%aa-%d7%94%d7%9b%d7%95%d7%9b%d7%91%d7%99%d7%9d-%d7%94%d7%9e%d7%95%d7%a8%d7%93%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=1362&series_name=star-wars-rebels-%d7%9e%d7%9c%d7%97%d7%9e%d7%aa-%d7%94%d7%9b%d7%95%d7%9b%d7%91%d7%99%d7%9d-%d7%94%d7%9e%d7%95%d7%a8%d7%93%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1362%2fstar-wars-rebels-%d7%9e%d7%9c%d7%97%d7%9e%d7%aa-%d7%94%d7%9b%d7%95%d7%9b%d7%91%d7%99%d7%9d-%d7%94%d7%9e%d7%95%d7%a8%d7%93%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLgP379x--W4ZPG7KJzWD6XL0pNGen74a2') #S1
		list.append('&youtube_pl=PLsNE3pORizv4UHWlqw6gaHnjr-mXkSQXm') #S2
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
		list.append('&youtube_pl=PLuMhJMX4b4LkhwV82zgFZF8cF82zj5lKH')
		list.append('&youtube_pl=PL1s_GIH3XuCTp6tbyH-KQHy1DFjWmx-di')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
		list.append('&youtube_pl=PLo-TJArWm5kl3btVopreshVetwb6i3SJt') #S1
		
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

	addDir(addonString(10489).encode('utf-8'),list,17,thumb,addonString(104890).encode('utf-8'),'1',0,fanart)

def CATEGORIES104H(General_LanguageL, background, background2): #LEGO Legends of Chima
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/265393-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/265393-1.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLKMFPiSCwUk3rCsFi4mGgF0easITs__2x')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=ELR0T0TMLbvr0') #S1
		list.append('&youtube_pl=PLhZISbIWzxzV1PrTJ7ZmTF50YW5EtdmJQ') #S1
		list.append('&youtube_pl=PLUkmjfDR7bJDLsrKigF07CWxxxSlwXHuj')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLLOeGExLxyzM1KZs9gemhepkgxARklymE') #S1+
		list.append('&youtube_id=Jc_ciq8MMZU') #S2E2
		list.append('&youtube_id=OKs-XW3awNo') #S3E14
		
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
		list.append('&youtube_pl=PLiWp6bZu2PDZcvYdWx531a2K3dtBvVS4E') #S1
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PL65bSKHWOkkVg217qDvVNZhnR-460066o') #S1
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLt2K1Hf3IgJU27cpWJMxshDhgnN6NsCbH') #S1
		list.append('&youtube_pl=') #
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		pass
		
	
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
		list.append('&youtube_pl=PLQSB0bybEVzazUOx6Uhy5mBWeUMD6hT3u')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=9YaVNsFJ10g') #
		list.append('&youtube_pl=') #
		
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL8MyJbCU5Mi6muRS3QWGFdS9nOQKeKH8S') #S1
		list.append('&youtube_pl=PL8MyJbCU5Mi4RA8hcBp6MjVE4xK6ixVid') #S2
		list.append('&youtube_pl=PLv36p3yPlGlzJc138BRYRwtChMPDkYNVx') #S
	
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
		list.append('&youtube_pl=PLAevrj2yKZu9PbEfkYpnpeoSBvilnEHFA')
		list.append('&youtube_pl=PLTdC8moEK00K0AYc1AU_0swh0yuCOHhjo')
		list.append('&youtube_pl=PLTdC8moEK00K0AYc1AU_0swh0yuCOHhjo')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10490).encode('utf-8'),list,17,thumb,addonString(104900).encode('utf-8'),'1',0,fanart)
	
def CATEGORIES104I(General_LanguageL, background, background2): #דובוני אכפת לי
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/76079-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76079-6.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2546390')
		list.append('&youtube_id=TxDBZPsgy8s')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLR6qb6y-1e97omsW2P0imc3s3DErNPwtM') #S1
		list.append('&youtube_pl=PLLDPut200IH4bkrhnrMv-1ShRLovh5YK6') #S2
		list.append('&youtube_pl=PLXSlB4yMaoJsE2_cZ_OedM7ejD_FpZbEm') #S3
		list.append('&youtube_pl=PL7tKi5y0-xFz6CDbfLwemLkZ2EA2IGRu-')
		list.append('&youtube_pl=PLzIW2YAtLiqpcpKir638OHXUd5qt6llsG')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLDFB56D1BBBA52FA7')
		list.append('&youtube_pl=PLo4DrcUVRBS5EluLbm0el6X0OS4UNY64T')
	
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
		list.append('&youtube_pl=PLB83493E6106A1B3A')
		list.append('&youtube_pl=PL3AB0BEED0A9291CD')
		list.append('&youtube_pl=PL3AB0BEED0A9291CD')
	
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
		list.append('&youtube_pl=PL9BFEB552FFEE2B74')
		list.append('&youtube_pl=PLk9ejlY4-zeLBPv4_mNX9Zu7V-1hDK3w2')
		
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10623).encode('utf-8'),list,17,thumb,addonString(106230).encode('utf-8'),'1',0,fanart)

def CATEGORIES104J(General_LanguageL, background, background2): #נילס הולגרסון
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/90821-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/90821-3.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/90821-2.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f713.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=713&series_name=%d7%a0%d7%99%d7%9c%d7%a1-%d7%94%d7%95%d7%9c%d7%92%d7%a8%d7%a1%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-wonderful-adventures-of-nils%2fseason%2f1&summary=%d7%a0%d7%99%d7%9c%d7%a1%20%d7%94%d7%95%d7%90%20%d7%99%d7%9c%d7%93%20%d7%a9%d7%95%d7%91%d7%91%20%d7%91%d7%9f%2014%20%d7%90%d7%a9%d7%a8%20%d7%97%d7%99%20%d7%91%d7%97%d7%95%d7%95%d7%94%20%d7%91%d7%a9%d7%91%d7%93%d7%99%d7%94.%20%d7%94%d7%95%d7%a8%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%94%d7%9d%20%d7%a2%d7%a0%d7%99%d7%99%d7%9d.%20%d7%95%d7%94%d7%95%d7%90%20%d7%a2%d7%a6%d7%9c%d7%9f%20%d7%95%d7%97%d7%a1%d7%a8%20%d7%9b%d7%9c%20%d7%94%d7%aa%d7%97%d7%a9%d7%91%d7%95%d7%aa%20%d7%91%d7%96%d7%95%d7%9c%d7%aa.%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%94%d7%99%d7%94%20%d7%a0%d7%95%d7%94%d7%92%20%d7%9c%d7%94%d7%aa%d7%90%d7%9b%d7%96%d7%a8%20%d7%9c%d7%97%d7%99%d7%95%d7%aa%20%d7%91%d7%97%d7%95%d7%95%d7%94%20%d7%91%d7%96%d7%9e%d7%a0%d7%95%20%d7%94%d7%a4%d7%a0%d7%95%d7%99%2c%20%d7%a2%d7%93%20%d7%a9%d7%99%d7%95%d7%9d%20%d7%90%d7%97%d7%93%20%d7%94%d7%95%d7%90%20%d7%9c%d7%95%d7%9b%d7%93%20%d7%a9%d7%93%d7%95%d7%9f.%20%d7%94%d7%a9%d7%93%d7%95%d7%9f%20%d7%94%d7%9b%d7%95%d7%a2%d7%a1%20%d7%9e%d7%97%d7%9c%d7%99%d7%98%20%d7%9c%d7%94%d7%a2%d7%a0%d7%99%d7%a9%20%d7%90%d7%aa%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%a2%d7%9c%20%d7%9e%d7%a2%d7%9c%d7%9c%d7%99%d7%95%2c%20%d7%95%d7%9c%d7%a2%d7%9c%20%d7%9b%d7%9f%20%d7%94%d7%95%d7%90%20%d7%9e%d7%9b%d7%95%d7%95%d7%a5%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9c%d7%92%d7%95%d7%93%d7%9c%20%d7%a9%d7%9c%20%d7%a0%d7%a0%d7%a1.%20%d7%91%d7%aa%d7%95%d7%a8%20%d7%a0%d7%a0%d7%a1%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%9e%d7%a1%d7%95%d7%92%d7%9c%20%d7%9b%d7%a2%d7%aa%20%d7%9c%d7%93%d7%91%d7%a8%20%d7%95%d7%9c%d7%94%d7%91%d7%99%d7%9f%20%d7%90%d7%aa%20%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%97%d7%99%d7%99%d7%9d.%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%95%d7%97%d7%99%d7%99%d7%aa%20%d7%94%d7%9e%d7%97%d7%9e%d7%93%20%d7%a9%d7%9c%d7%95%20%d7%90%d7%95%d7%92%d7%99%20%d7%94%d7%90%d7%95%d7%92%d7%a8%20%d7%9e%d7%a6%d7%98%d7%a8%d7%a4%d7%99%d7%9d%20%d7%9c%d7%90%d7%95%d7%95%d7%96%20%d7%94%d7%91%d7%99%d7%aa%20%d7%9e%d7%95%d7%9c%d7%99%20%d7%91%d7%9e%d7%a1%d7%a2%d7%95%20%d7%a2%d7%9d%20%d7%90%d7%95%d7%95%d7%96%d7%99%20%d7%94%d7%91%d7%a8%2c%20%d7%94%d7%9e%d7%95%d7%a0%d7%94%d7%92%d7%99%d7%9d%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%94%d7%9e%d7%a4%d7%a7%d7%93%d7%aa%20%d7%90%d7%a7%d7%94%2c%20%d7%9c%d7%90%d7%96%d7%95%d7%a8%20%d7%94%d7%a6%d7%a4%d7%95%d7%a0%d7%99%20%d7%a9%d7%9c%20%d7%a9%d7%91%d7%93%d7%99%d7%94%2c%20%d7%a9%d7%9d%20%d7%94%d7%a9%d7%9e%d7%a9%20%d7%90%d7%99%d7%a0%d7%94%20%d7%a9%d7%95%d7%a7%d7%a2%d7%aa.%20%d7%91%d7%99%d7%97%d7%93%20%d7%94%d7%9d%20%d7%98%d7%a1%d7%99%d7%9d%20%d7%9c%d7%90%d7%95%d7%a8%d7%9a%20%d7%a9%d7%91%d7%93%d7%99%d7%94%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%a0%d7%99%d7%9c%d7%a1%20%d7%9e%d7%a7%d7%95%d7%95%d7%94%20%d7%9b%d7%99%20%d7%99%d7%a6%d7%9c%d7%99%d7%97%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%d7%94%d7%93%d7%a8%d7%9a%20%d7%9c%d7%91%d7%98%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%9b%d7%99%d7%a9%d7%95%d7%a3%20%d7%95%d7%9c%d7%97%d7%96%d7%95%d7%a8%20%d7%9c%d7%94%d7%99%d7%95%d7%aa%20%d7%92%d7%93%d7%95%d7%9c%20%d7%a9%d7%95%d7%91.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f713%2f%d7%a0%d7%99%d7%9c%d7%a1-%d7%94%d7%95%d7%9c%d7%92%d7%a8%d7%a1%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-wonderful-adventures-of-nils%2fseason%2f1')
		list.append('&youtube_pl=PL_8KXLhQVQMKVZInMgWpGe9osYlO5lcBa') #Hebrew
		list.append('&youtube_pl=PLwXEsK85wc0NYyg8whoBrNpRznTV7r1vP') #Hebrew
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
		list.append('&youtube_pl=PL5xXAWMbhAtlp-Vsrgo5lknESnpIMdrvG') #German
		list.append('&youtube_pl=PL-CILcssSDKHF1X4RVHoVINov3ncHiYGx') #German
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLwSzDIvrlKomOp7zAfJwAbYweV1Tn2w0a') #Dutch
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLE2498963634F01D0') #Hungarian
	
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
		list.append('&youtube_pl=PL8XovLToH9hYd1Yo6gehiq6xiT4fodI3m')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL23B942DCBE599DBF') #French
		list.append('&youtube_pl=PLBC31B0EF15725285') #French
		list.append('&youtube_pl=PL-_HUSbX6NgQ--_qCJzdFifgsADfDLkST') #French
	
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

	addDir(addonString(10468).encode('utf-8'),list,17,thumb,addonString(104680).encode('utf-8'),'1',0,fanart)

def CATEGORIES104K(General_LanguageL, background, background2): #סיפורי מוש
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/82737-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82737-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL9mJOYidEPhoUg_j1fwald53hRuM0hOuc') #סיפורי מוש
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLz_WViLi_Q3e4erK7Ko4w7iZh3vLcQa_t') #סיפורי מוש
	
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
		list.append('&youtube_pl=PL8rtSe8ySfcvUFWHEK7VHNbECKbDxMsou')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL8rtSe8ySfcvUFWHEK7VHNbECKbDxMsou') #סיפורי מוש
	
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
		list.append('&youtube_pl=PLF803EED0CFFE413A') #סיפורי מוש
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLnM6FRWnL-PK-tcWDmrKMkSX7dTW6wZDl')
	
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
		list.append('&youtube_pl=PLp5RH-yn0Nvg4Ujl1c---UJrX5reJd8cS')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10491).encode('utf-8'),list,17,thumb,addonString(104910).encode('utf-8'),'1',0,fanart)

def CATEGORIES104L(General_LanguageL, background, background2): #אגדות האחים גרים
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/111131-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/111131-3.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		
		list.append('&youtube_pl=PLYlrzbISBfkuyDzUwktkKJ8ecy-RZ3AHI') #S1
		list.append('&youtube_pl=PLYlrzbISBfktPBUHxCckXbRxD6KkCapzu') #S2
		list.append('&youtube_pl=PLmNjn7uj9TQUxjlYuWFN0RZg1RUUfu9SG') #Hebrew
		list.append('&youtube_pl=PLxd2PvjbApyUmvVaMyQsaiqJnu4tultQw') #Hebrew
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLE918DC6AFF74BBD3')
		list.append('&youtube_pl=')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL1A36687F1D0E073E')
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
		list.append('&youtube_pl=PL9A89EE24241DACF2')
	
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
		list.append('&youtube_pl=PLC3D9DAFFB4D8323B')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PL84F67208407C7AC3')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		thumb = 'https://upload.wikimedia.org/wikipedia/ar/9/97/%D9%81%D9%8A_%D8%AC%D8%B9%D8%A8%D8%AA%D9%8A_%D8%AD%D9%83%D8%A7%D9%8A%D8%A9.gif'
		list.append('&youtube_pl=PLanXyg33qZLG3QByLzH9W3dkgC8DCXdhS')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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
	
	addDir(addonString(10499).encode('utf-8'),list,17,thumb,addonString(104990).encode('utf-8'),'1',0,fanart)

def CATEGORIES104M(General_LanguageL, background, background2): #סאקורה לוכדת הקלפים
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/70668-13.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70668-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
		list.append('&youtube_pl=PLI6L7wB4bdu30OZnsJosHpBK5E2W_NkbA')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10498).encode('utf-8'),list,17,thumb,addonString(104980).encode('utf-8'),'1',0,fanart)

def CATEGORIES104N(General_LanguageL, background, background2): #נינג'גו - מאסטר הספינג'יצו
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/253323-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/253323-12.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1820.jpg&mode=3&name=ninjago-masters-of-spinjitzu-%d7%a0%d7%99%d7%a0%d7%92-%d7%92%d7%95-%d7%9e%d7%90%d7%a1%d7%98%d7%a8-%d7%94%d7%a1%d7%a4%d7%99%d7%a0%d7%92-%d7%99%d7%a6%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&series_id=1820&series_name=ninjago-masters-of-spinjitzu-%d7%a0%d7%99%d7%a0%d7%92-%d7%92%d7%95-%d7%9e%d7%90%d7%a1%d7%98%d7%a8-%d7%94%d7%a1%d7%a4%d7%99%d7%a0%d7%92-%d7%99%d7%a6%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1820%2fninjago-masters-of-spinjitzu-%d7%a0%d7%99%d7%a0%d7%92-%d7%92%d7%95-%d7%9e%d7%90%d7%a1%d7%98%d7%a8-%d7%94%d7%a1%d7%a4%d7%99%d7%a0%d7%92-%d7%99%d7%a6%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=')
	
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL5833BFE67466AE31') #English
		list.append('&youtube_pl=PLs20ZA0q4gQCBBKghE6rUuVL9VsvVBqvA') #English
		list.append('&dailymotion_pl=x3ul0k') #S1
		list.append('&dailymotion_pl=x43uhy') #S2
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=ELmWM3zMzLY3I') #S1
			list.append('&youtube_pl=ELGbD9SrC9H3Y') #S2
			list.append('&youtube_pl=ELWhYHdg_CkvY') #S3
			list.append('&youtube_pl=PLs20ZA0q4gQCBBKghE6rUuVL9VsvVBqvA') #S4
			list.append('&youtube_pl=ELPq2ykMpt2mLsPSg0c1rFOQ') #S4
			list.append('&youtube_pl=EL8Ms60ICex7TzF-_0x9hoqg') #S5
			
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
		list.append('&youtube_pl=PL2axIq3IX4USVUXhZuE9ZqPLqccTqlpTj') #
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLx3f1q8-kngmvAuHjYhfAayGn9QgV8Ngp') #
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLNqK12R0zSvTt3eq256TuCxfq7SClHu9p') #
		list.append('&youtube_pl=PLMD5TcWgUOO7FuRhuD_fTDuGMXCg3rb9Y') #
		list.append('&youtube_pl=') #
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PL5peNfSV4E_DjFWUtD23GR54c40LkOY5z') #
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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
		list.append('&youtube_pl=PL7qJy8wXdrSjulrGwV3dVrbO5dNl1NG5g') #
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10479).encode('utf-8'),list,17,thumb,addonString(104790).encode('utf-8'),'1',0,fanart)

def CATEGORIES104O(General_LanguageL, background, background2): #אוטובוס הקסמים
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/71416-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/71416-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		thumb = ''
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1032.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1032&series_name=%d7%90%d7%95%d7%98%d7%95%d7%91%d7%95%d7%a1-%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-the-magic-school-bus%2fseason%2f1&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%aa%20%d7%9c%d7%94%d7%a2%d7%a9%d7%a8%d7%aa%20%d7%94%d7%99%d7%93%d7%a2%20%d7%9c%d7%99%d7%9c%d7%93%d7%99%d7%9d%2c%20%d7%93%d7%a8%d7%9a%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%95%20%d7%a9%d7%9c%20%d7%90%d7%95%d7%98%d7%95%d7%91%d7%95%d7%a1%20%d7%a7%d7%a1%d7%9e%d7%99%d7%9d%20%d7%a6%d7%94%d7%95%d7%91%20%d7%94%d7%9e%d7%92%d7%99%d7%a2%20%d7%9c%d7%9b%d7%9c%20%d7%9e%d7%a7%d7%95%d7%9d%20%d7%92%d7%9d%20%d7%94%d7%96%d7%a2%d7%99%d7%a8%20%d7%91%d7%99%d7%95%d7%aa%d7%a8%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%9c%d7%9e%d7%95%d7%93%20%d7%95%d7%9c%d7%97%d7%a7%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%a1%d7%91%d7%99%d7%91%d7%a0%d7%95.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1032%2f%d7%90%d7%95%d7%98%d7%95%d7%91%d7%95%d7%a1-%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-the-magic-school-bus%2fseason%2f1')
		list.append('&youtube_pl=PLojgGSYuCHTB2q0TvkcGuhKteg3hNsZle')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLgeJ6bGP6EDkHog7QpPxB8EcsFTjnl8Ut')
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
		list.append('&youtube_pl=PLt6wYMdXCggoOQDo5tn33e40Hbd5taQFy')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_id=SmOwM4DHaTc')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PL21Max3krxq_L7bvKLVa0u21t4dGHXImT')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLE8_AKSaJse9_IzmzI6GWKkmmBwlDANoN')
	
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
		thumb = 'https://upload.wikimedia.org/wikipedia/ru/thumb/7/7a/%D0%92%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D1%8B%D0%B9_%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81_%28%D0%BF%D0%BE%D1%81%D1%82%D0%B5%D1%80%29.jpg/250px-%D0%92%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D1%8B%D0%B9_%D1%88%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D1%83%D1%81_%28%D0%BF%D0%BE%D1%81%D1%82%D0%B5%D1%80%29.jpg'
		list.append('&youtube_pl=PL4uSs79W8jWvYsux3wxN97wLHdJ-LP-pf')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	
	addDir(addonString(10403).encode('utf-8'),list,17,thumb,addonString(104030).encode('utf-8'),'1',0,fanart)

def CATEGORIES104P(General_LanguageL, background, background2): #Digimon: Digital Monsters / דיגימון: מפלצות דיגיטליות
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/72241-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/72241-8.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f720.jpg&mode=3&name=%d7%93%d7%99%d7%92%27%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=720&series_name=%d7%93%d7%99%d7%92%27%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f720%2fdigimon-%d7%93%d7%99%d7%92-%d7%99%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLKMFPiSCwUk2AWPSN0CngtMfiB8oFWZwX')
		list.append('&youtube_pl=PLk98jt4ayAVJr26ugq6oAD6j0QjfVxSGD')
		list.append('&youtube_pl=PLKMFPiSCwUk3S3KtIMAOv83IiRQNgHp7T') #Fusion S1E1-5
		list.append('&youtube_pl=PLKMFPiSCwUk3nYihy4qmImPx17sQHYF88') #Frontier S1E1-3
		 
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLsUxWIZFayHW37hhKAaOaeD2zyw0-ILsO') #S1
		list.append('&youtube_id=VtQtElW7CqQ') #S1E19-27
		list.append('&youtube_pl=PLXSH0wBFP4_EYuu7mamD67KEffWoh1o3k') #S2
		
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10416).encode('utf-8'),list,17,thumb,addonString(104160).encode('utf-8'),'1',0,fanart)

def CATEGORIES104Q(General_LanguageL, background, background2): #סיילור מון
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/275039-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/275039-1.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f548.jpg&mode=3&name=%d7%a1%d7%99%d7%99%d7%9c%d7%95%d7%a8-%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-sailor-moon%2fseason%2f1&series_id=548&series_name=%d7%a1%d7%99%d7%99%d7%9c%d7%95%d7%a8-%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-sailor-moon%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f548%2f%d7%a1%d7%99%d7%99%d7%9c%d7%95%d7%a8-%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-sailor-moon%2fseason%2f1')
		list.append('&youtube_pl=PLsg4IBMPLqMTJVTYNvRMz5ZP7_q6HH0E4') #Hebrew
		list.append('&youtube_pl=PLFt-xe6eTY8MwVS7xZi9bq9nMZg5b4ClL') #Hebrew
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&name_=Season 1&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F85%2Fimage%2F555x418%2Fsailor-moon-season-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSailor%20Moon%20(1992%E2%80%931993)%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fsailor-moon-season-1')
		list.append('&name_=Season 2&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F86%2Fimage%2F555x418%2Fsailor-moon-season-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSailor%20Moon%20R%20(1993%E2%80%931994)%20Season%202%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fsailor-moon-r-season-2')
		list.append('&youtube_pl=PLA2A7425252E73586') #English
		list.append('&youtube_pl=PL37753E7A32DB1E38') #English #http://ib.huluim.com/show_key_art/18617?size=1600x600
		list.append('&youtube_pl=')
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
		list.append('&youtube_id=wf-owQJJwG0')
		list.append('&youtube_id=q0pnbuHIBHI')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLHXYIWG5iMqZ5i5rHzR-vCoVpnZCyllbb') #Spanish
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLINgVpX-p-GIefI8KNsLMoOQ7Qp-0ygMZ')
		list.append('&youtube_pl=PL0C04B8D69D8C4394') #S2
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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
	
	addDir(addonString(10472).encode('utf-8'),list,17,thumb,addonString(104720).encode('utf-8'),'1',"",fanart)

def CATEGORIES104R(General_LanguageL, background, background2): #Dragon Ball / דראגון בול
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/79275-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/79275-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1815.jpg&mode=3&name=dragon-ball-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&series_id=1815&series_name=dragon-ball-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1815%2fdragon-ball-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLIEbITAtGBebWGyBZQlkiMXwt30WqG9Bd')
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
		list.append('&youtube_pl=PLHwX4SWGT6V6fnZVv1W24dTqnb2CtOAs6')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10528).encode('utf-8'),list,17,thumb,addonString(105280).encode('utf-8'),'1',0,fanart)

def CATEGORIES104S(General_LanguageL, background, background2): #Dragon Ball Z / דראגון בול Z
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/81472-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/81472-77.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		url = os.path.join(templates2_path, '104', 'Dragon Ball Z.txt')
		list.append('&custom_se11='+url) #&name_=Full&
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f293.jpg&mode=3&name=dragon-ball-z-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%96%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=293&series_name=dragon-ball-z-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%96%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f293%2fdragon-ball-z-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%96%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLzPOIgqAmUxsr8WjTdDiNvgIjzOqwwD1O')
		list.append('&youtube_pl=PL6E0EE345D513F341')
		#addDir('googledrive mode=11 custom_se2',url,11,image2,'testing','1',50, image2) #Test
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLIEbITAtGBeYy4Gi9gSZT0GKXndtWEVev')
		list.append('&youtube_pl=PLIEbITAtGBeZ4DNOjaALTh8jDLn8_L4Pa')
		list.append('&youtube_pl=PLIEbITAtGBeZCo9HFoiPSRgrMvyynBy8R')
		
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
		list.append('&youtube_pl=PL7yHJ1OH2RFJvXpnEsBEgLqDprSWuS5rU')
		list.append('&youtube_pl=PL531Q7zcnaMa3lz0rvu5nm4qC5IZb7Zlo')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10525).encode('utf-8'),list,17,thumb,addonString(105250).encode('utf-8'),'1',0,fanart)

def CATEGORIES104T(General_LanguageL, background, background2): #Dragon Ball Super / דראגון בול S
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/295068-9.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/295068-26.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		url = os.path.join(templates2_path, '104', 'Dragon Ball Z.txt')
		list.append('&custom_se11='+url) #&name_=Full&
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1813.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1813&series_name=dragon-ball-super-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%a1%d7%95%d7%a4%d7%a8-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%aa%20%d7%a2%d7%95%d7%a7%d7%91%d7%aa%20%d7%90%d7%97%d7%a8%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%d7%99%d7%95%20%d7%94%d7%97%d7%93%d7%a9%d7%95%d7%aa%20%d7%a9%d7%9c%20%d7%94%d7%9c%d7%95%d7%97%d7%9d%20%d7%94%d7%a2%d7%95%d7%a6%d7%9e%d7%aa%d7%99%2c%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%2c%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%92%d7%9c%d7%94%20%d7%a2%d7%95%d7%9c%d7%9e%d7%95%d7%aa%20%d7%97%d7%93%d7%a9%d7%99%d7%9d%20%d7%95%d7%a4%d7%95%d7%92%d7%a9%20%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%95%d7%90%d7%95%d7%99%d7%91%d7%99%d7%9d%20%d7%97%d7%93%d7%a9%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1813%2fdragon-ball-super-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%a1%d7%95%d7%a4%d7%a8-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLyc2dFYhZECbcZP_64xKT5rN4Sgc3S7Er') #SUB
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10524).encode('utf-8') + space + 'S',list,17,thumb,addonString(105240).encode('utf-8'),'1',0,fanart)

def CATEGORIES104U(General_LanguageL, background, background2): #דראגון בול GT
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/79275-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/79275-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f531.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=531&series_name=dragon-ball-gt-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%92-%d7%99-%d7%98%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%94%d7%94%d7%9e%d7%a9%d7%9a%20%d7%a9%d7%9c%20%d7%94%d7%9c%d7%94%d7%99%d7%98%20%d7%94%d7%99%d7%a4%d7%a0%d7%99%20%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%95%d7%9c%20%d7%96%d7%99!%20%d7%a4%d7%95%d7%9c%d7%a9%d7%99%d7%9d%20%d7%a9%d7%97%d7%95%d7%93%d7%a8%d7%99%d7%9d%20%d7%9c%d7%9e%d7%a7%d7%93%d7%a9%20%d7%94%d7%a9%d7%9e%d7%99%d7%99%d7%9e%d7%99%20%d7%a9%d7%9c%20%d7%93%d7%a0%d7%93%d7%94%2c%20%d7%9e%d7%a0%d7%a1%d7%99%d7%9d%20%d7%9c%d7%92%d7%a0%d7%95%d7%91%20%d7%90%d7%aa%20%d7%9b%d7%93%d7%95%d7%a8%d7%99%20%d7%94%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%95%d7%9c%20%d7%94%d7%a9%d7%97%d7%95%d7%a8%d7%99%d7%9d%2c%20%d7%a9%d7%94%d7%9d%20%d7%9b%d7%93%d7%95%d7%a8%d7%99%d7%9d%20%d7%a8%d7%91%d7%99%20%d7%a2%d7%95%d7%a6%d7%9e%d7%94%20%d7%a9%d7%99%d7%a6%d7%a8%20%d7%92%d7%95%d7%93.%20%d7%94%d7%a4%d7%95%d7%9c%d7%a9%d7%99%d7%9d%20%d7%a7%d7%95%d7%a8%d7%90%d7%99%d7%9d%20%d7%9c%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%9e%d7%98%d7%a8%d7%94%20%d7%9c%d7%91%d7%a7%d7%a9%20%d7%9e%d7%9e%d7%a0%d7%95%20%d7%a9%d7%9c%d7%99%d7%98%d7%94%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d%2c%20%d7%90%d7%91%d7%9c%20%d7%90%d7%96%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%20%d7%9e%d7%a0%d7%a1%d7%94%20%d7%9c%d7%a2%d7%a6%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%94%d7%a4%d7%95%d7%9c%d7%a9%d7%99%d7%9d%20%d7%95%d7%94%d7%9d%20%d7%9e%d7%91%d7%a7%d7%a9%d7%99%d7%9d%20%d7%9e%d7%94%d7%93%d7%a8%d7%a7%d7%95%d7%9f%20%d7%a9%d7%9c%20%d7%9b%d7%93%d7%95%d7%a8%d7%99%20%d7%94%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%95%d7%9c%20%d7%a9%d7%99%d7%94%d7%a4%d7%95%d7%9a%20%d7%90%d7%aa%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%20%d7%9c%d7%99%d7%9c%d7%93%20%d7%a7%d7%98%d7%9f.%3cbr%2f%3e%3cbr%2f%3e%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%20%d7%94%d7%95%d7%a4%d7%9a%20%d7%9c%d7%99%d7%9c%d7%93%20%d7%a7%d7%98%d7%9f%20%d7%95%d7%a9%d7%91%d7%a2%d7%aa%20%d7%9b%d7%93%d7%95%d7%a8%d7%99%20%d7%94%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%95%d7%9c%20%d7%94%d7%a9%d7%97%d7%95%d7%a8%d7%99%d7%9d%20%d7%9e%d7%aa%d7%a4%d7%96%d7%a8%d7%99%d7%9d%20%d7%91%d7%a8%d7%97%d7%91%d7%99%20%d7%94%d7%99%d7%a7%d7%95%d7%9d.%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%20%d7%97%d7%95%d7%96%d7%a8%20%d7%9c%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%2c%20%d7%90%d7%91%d7%9c%20%d7%90%d7%96%20%d7%9e%d7%a1%d7%aa%d7%91%d7%a8%20%d7%9c%d7%95%20%d7%a9%d7%90%d7%9d%20%d7%9c%d7%90%20%d7%99%d7%90%d7%a1%d7%95%d7%a3%20%d7%90%d7%aa%20%d7%a9%d7%91%d7%a2%d7%aa%20%d7%94%d7%9b%d7%93%d7%95%d7%a8%d7%99%d7%9d%20%d7%aa%d7%95%d7%9a%20%d7%a9%d7%a0%d7%94%2c%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%99%d7%99%d7%94%d7%a8%d7%a1.%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%20%d7%99%d7%95%d7%a6%d7%90%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%98%d7%a8%d7%90%d7%a0%d7%a7%d7%a1%20%d7%95%d7%a4%d7%90%d7%9f%20%d7%9c%d7%9e%d7%a1%d7%a2%20%d7%90%d7%9c%20%d7%94%d7%99%d7%a7%d7%95%d7%9d%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%97%d7%a4%d7%a9%20%d7%90%d7%97%d7%a8%20%d7%94%d7%9b%d7%93%d7%95%d7%a8%d7%99%d7%9d.%20%d7%91%d7%9e%d7%94%d7%9c%d7%9a%20%d7%94%d7%9e%d7%a1%d7%a2%20%d7%94%d7%9d%20%d7%9e%d7%92%d7%99%d7%a2%d7%99%d7%9d%20%d7%9c%d7%9b%d7%95%d7%9b%d7%91%d7%99%d7%9d%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%9e%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%a4%d7%95%d7%92%d7%a9%d7%99%d7%9d%20%d7%99%d7%a6%d7%95%d7%a8%d7%99%d7%9d%20%d7%90%d7%9b%d7%96%d7%a8%d7%99%d7%99%d7%9d%20%d7%95%d7%9e%d7%a1%d7%95%d7%9b%d7%a0%d7%99%d7%9d%20%d7%a9%d7%9e%d7%97%d7%a4%d7%a9%d7%99%d7%9d%20%d7%90%d7%aa%20%d7%9b%d7%93%d7%95%d7%a8%d7%99%20%d7%94%d7%93%d7%a8%d7%92%d7%95%d7%9f%20%d7%91%d7%95%d7%9c%20%d7%94%d7%a9%d7%97%d7%95%d7%a8%d7%99%d7%9d%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%97%d7%a1%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%99%d7%a7%d7%95%d7%9d.%20%d7%91%d7%a1%d7%95%d7%a4%d7%95%20%d7%a9%d7%9c%20%d7%93%d7%91%d7%a8%2c%20%d7%a1%d7%95%d7%9f%20%d7%92%d7%95%d7%a7%d7%95%2c%20%d7%98%d7%a8%d7%90%d7%a0%d7%a7%d7%a1%20%d7%95%d7%a4%d7%90%d7%9f%20%d7%9e%d7%a6%d7%9c%d7%99%d7%97%d7%99%d7%9d%20%d7%9c%d7%94%d7%aa%d7%92%d7%91%d7%a8%20%d7%a2%d7%9c%20%d7%94%d7%90%d7%95%d7%99%d7%91%d7%99%d7%9d%20%d7%95%d7%9c%d7%90%d7%a1%d7%95%d7%a3%20%d7%90%d7%aa%20%d7%94%d7%9b%d7%93%d7%95%d7%a8%d7%99%d7%9d%20%d7%94%d7%a9%d7%97%d7%95%d7%a8%d7%99%d7%9d%20%d7%90%d7%97%d7%93%20%d7%9c%d7%90%d7%97%d7%93.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f531%2fdragon-ball-gt-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%92-%d7%99-%d7%98%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLIEbITAtGBearIZ38rXEGiqv-HYtpqFE3')
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
		list.append('&youtube_pl=PLbwudPzS-K_rGz8-m6CE_4oXBWrCnXgm7')
	
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10526).encode('utf-8'),list,17,thumb,addonString(105260).encode('utf-8'),'1',0,fanart)

def CATEGORIES104V(General_LanguageL, background, background2): #Dragon Ball Kai / דראגון בול K
	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/88031-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/88031-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1275.jpg&mode=3&name=dragon-ball-kai-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%a7%d7%90%d7%99-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&series_id=1275&series_name=dragon-ball-kai-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%a7%d7%90%d7%99-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1275%2fdragon-ball-kai-%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%a7%d7%90%d7%99-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10523).encode('utf-8'),list,17,thumb,addonString(105230).encode('utf-8'),'1',0,fanart)

def CATEGORIES104W(General_LanguageL, background, background2): #Digimon Tamers

	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/277575-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/277575-3.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10421).encode('utf-8'),list,17,thumb,addonString(104210).encode('utf-8'),'1',0,fanart)

def CATEGORIES104Y(General_LanguageL, background, background2): #Digimon Fusion

	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/272858-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/272858-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10333).encode('utf-8'),list,17,thumb,addonString(103330).encode('utf-8'),'1',0,fanart)

def CATEGORIES104AA(General_LanguageL, background, background2): #Digimon Xros Wars

	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/202241-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/202241-2.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10331).encode('utf-8'),list,17,thumb,addonString(103310).encode('utf-8'),'1',0,fanart)

def CATEGORIES104AB(General_LanguageL, background, background2): #Digimon Universe: Appli Monsters

	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/317566-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/317566-1.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(10330).encode('utf-8'),list,17,thumb,addonString(103300).encode('utf-8'),'1',0,fanart)

def CATEGORIES104AC(General_LanguageL, background, background2): #Digimon Adventure Tri

	'''סדרות'''
	thumb = 'https://www.thetvdb.com/banners/posters/290290-11.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/290290-3.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
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
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
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

	addDir(addonString(104980).encode('utf-8'),list,17,thumb,addonString(104980).encode('utf-8'),'1',0,fanart)
