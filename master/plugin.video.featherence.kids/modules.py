# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
from modules101 import *
from modules102 import *
from modules104 import *
from modules105 import *
from modules106 import *
from modules107 import *
from modules108 import *
from modules109 import *
from modulesZ import *
from modulesA import *
'''---------------------------'''
	
def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	try: General_Language = getsetting('General_Language')
	except: General_Language = systemlanguage
	
	CATEGORIES_SEARCH(mode=30, url="")
	addDir('-' + addonString(100).encode('utf-8'),'',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0,getAddonFanart(100, urlcheck_=False)) #My Kids
	
	addDir(addonString(101).encode('utf-8'),'',101,featherenceserviceicons_path + 'music.png',addonString(1010).encode('utf-8'),'1',58, "http://p1.pichost.me/i/28/1509965.jpg") #SONGS AND STORIES
	addDir(addonString(102).encode('utf-8'),'',102,featherenceserviceicons_path + 'bank.png',addonString(1020).encode('utf-8'),'1',58, "http://2.bp.blogspot.com/-Dz3-VwZZryE/Uh5ZXg7zCMI/AAAAAAAAdCQ/OmLVkdWI47c/s1600/Disney+Junior+Live+Pirate+and+Princess+Adventure+-+Jake%252C+Izzy+%2526+Cubby.jpg") #SHOWS
	addDir(addonString(104).encode('utf-8'),'',104,featherenceserviceicons_path + 'tvshows.png',addonString(1040).encode('utf-8'),'1',2, "http://www.canadiananimationresources.ca/wp-content/uploads/2012/10/9-Story-Arthur-Couch.jpg") #TV SHOWS
	addDir(addonString(105).encode('utf-8'),'',105,featherenceserviceicons_path + 'movies.png',addonString(1050).encode('utf-8'),'1',1, "http://4.bp.blogspot.com/-Af2HcIQzlg8/UhwQ8lKPucI/AAAAAAAACIA/d7aY4RrxUfk/s1600/bambi-friends-disney-animated-movie-photo.jpg") #MOVIES
	addDir(addonString(106).encode('utf-8'),'',106,featherenceserviceicons_path + 'toddlers.png',addonString(1060).encode('utf-8'),'1',58, "http://1.bp.blogspot.com/-MnUXpmW1n1M/UKfOgAXUmXI/AAAAAAAAbBY/BfoQ1FNgNUk/s1600/duvcar1024x768_en_27.jpg") #Toddlers
	addDir(addonString(107).encode('utf-8'),'',107,featherenceserviceicons_path + 'kids.png',addonString(1070).encode('utf-8'),'1',58, "http://i.imgur.com/cL52CfE.jpg") #Tiny
	addDir(addonString(108).encode('utf-8'),'',108,featherenceserviceicons_path + 'kids2.png',addonString(1080).encode('utf-8'),'1',0,"http://30k0u22sosp4xzag03cfogt1.wpengine.netdna-cdn.com/wp-content/uploads/2015/03/strika-3.jpg") #Kids and Young
	addDir(addonString(109).encode('utf-8'),'',109,featherenceserviceicons_path + 'ud.png',addonString(1090).encode('utf-8'),'1',0,"") #Learn Language
	addDir(addonString(200).encode('utf-8') % (General_Language),'',200,featherenceserviceicons_path + 'ud.png','[COLOR=red]1: %s | 2: %s | 3: %s[/COLOR]' % (General_Language, General_Language2, General_Language3) + '[CR]' + addonString_servicefeatherence(32081).encode('utf-8'),'1',0,"") #Forigen Language
	
	#addDir('קלסיקלטת','plugin://plugin.video.wallaNew.video/?mode=1&module=338&name=קלסיקלטת&url=http://vod.walla.co.il/channel/338/clasicaletet',8,'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTYE2VT8CR2O31MsqAhdaydYrqrCD--HCCdGcs7blBn3Zh92Kwq','','1',0,getAddonFanart(0))
	addDir('ניק','plugin://plugin.video.wallaNew.video/?mode=1&module=nick&name=ניק&url=http://nick.walla.co.il/',8,'http://www.karmieli.co.il/sites/default/files/images/nico.jpg','','1',0,getAddonFanart(0))
	addDir('גוניור','plugin://plugin.video.wallaNew.video/?mode=1&module=nickjr&name=גוניור&url=http://nickjr.walla.co.il/',8,'http://upload.wikimedia.org/wikipedia/he/1/19/%D7%A2%D7%A8%D7%95%D7%A5_%D7%92%27%D7%95%D7%A0%D7%99%D7%95%D7%A8.jpg','','1',0,getAddonFanart(0))
	#addDir('421','http://nickjr.walla.co.il/item/2775381',42,'plot','','1',0,getAddonFanart(0))

def CATEGORIES100(name, iconimage, desc, fanart):
	'''------------------------------
	---My-Kids-----------------------
	------------------------------'''
	fanart = 100
	
	'''כפתור הילדים שלי חדש..'''
	addDir(addonString_servicefeatherence(32156).encode('utf-8'),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(32451).encode('utf-8') + addonString_servicefeatherence(32452).encode('utf-8') + addonString_servicefeatherence(32453).encode('utf-8'),'s',50, getAddonFanart(fanart))
		
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',50,Custom_Playlist1_Fanart)
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',50,Custom_Playlist2_Fanart)
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',50,Custom_Playlist3_Fanart)
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',50,Custom_Playlist4_Fanart)
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',50,Custom_Playlist5_Fanart)
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',50,Custom_Playlist6_Fanart)
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',50,Custom_Playlist7_Fanart)
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',50,Custom_Playlist8_Fanart)
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',50,Custom_Playlist9_Fanart)
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',50,Custom_Playlist10_Fanart)
	
	'''test'''
	exe = printlog(title="test", printpoint="", text="", level=0, option="")
	if exe != "": addDir('test','',999,'','','1',50, '') #Test
	
'''1=SONGS, 2=SHOWS, 3=LITTLE, 4=TVSHOWS, 5=MOVIES, 6=?, 7=BABY, 8=?, 9=OTHERS'''

def CATEGORIES101(name, iconimage, desc, fanart):
	background = 101
	background2 = "" #http://p1.pichost.me/i/28/1509965.jpg"
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES101Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	CATEGORIES101B(General_LanguageL, background, background2) #השירים הראשונים שלי
	CATEGORIES101C(General_LanguageL, background, background2) #שירי ילדים
	CATEGORIES101D(General_LanguageL, background, background2) #שירי לילה טוב
	CATEGORIES101E(General_LanguageL, background, background2) #שירי דיסני
	CATEGORIES101I(General_LanguageL, background, background2) #אוסף סיפורים
	CATEGORIES101M(General_LanguageL, background, background2) #חגים
	CATEGORIES101N(General_LanguageL, background, background2) #יום הולדת
	
	
	'''עכבר העיר ועכבר הכפר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1618.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1618&series_name=%d7%a2%d7%9b%d7%91%d7%a8-%d7%94%d7%a2%d7%99%d7%a8-%d7%95%d7%a2%d7%9b%d7%91%d7%a8-%d7%94%d7%9b%d7%a4%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-the-country-mouse-and-the-city-mouse-adventures%2fseason%2f1&summary=%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%d7%99%d7%94%d7%9d%20%d7%a9%d7%9c%20%d7%90%d7%9e%d7%99%d7%9c%d7%99%20%d7%95%d7%90%d7%9c%d7%9b%d7%a1%d7%a0%d7%93%d7%a8%20%d7%94%d7%9e%d7%98%d7%99%d7%99%d7%9c%d7%99%d7%9d%20%d7%9e%d7%a1%d7%91%d7%99%d7%91%20%d7%9c%d7%a2%d7%95%d7%9c%d7%9d%2c%20%d7%a4%d7%95%d7%92%d7%a9%d7%99%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%95%d7%a4%d7%95%d7%aa%d7%a8%d7%99%d7%9d%20%d7%aa%d7%a2%d7%9c%d7%95%d7%9e%d7%95%d7%aa.%20%d7%a0%d7%a7%d7%a8%d7%90%20%d7%92%d7%9d%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a2%d7%9b%d7%91%d7%a8%20%d7%94%d7%a2%d7%99%d7%a8%20%d7%95%d7%a2%d7%9b%d7%91%d7%a8%20%d7%94%d7%9b%d7%a4%d7%a8%20%2a%2a%2a%2a%2a%d7%94%d7%95%d7%a7%d7%9c%d7%98%20%d7%91%d7%9c%d7%a2%d7%93%d7%99%20%d7%9c%d7%a1%d7%93%d7%a8%d7%95%d7%aa%20%d7%98%d7%99%d7%95%d7%99%2a%2a%2a%2a%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1618%2f%d7%a2%d7%9b%d7%91%d7%a8-%d7%94%d7%a2%d7%99%d7%a8-%d7%95%d7%a2%d7%9b%d7%91%d7%a8-%d7%94%d7%9b%d7%a4%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-the-country-mouse-and-the-city-mouse-adventures%2fseason%2f1')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL33796B8BB9BE81AD') #English
		list.append('&youtube_pl=PL33796B8BB9BE81AD') #English
		list.append('&youtube_id=C90qaiNDWFA') #English
	addDir(addonString(10176).encode('utf-8'),list,17,thumb,addonString(101760).encode('utf-8'),'1',"",fanart)
	
	'''אוסף דיג דיג דוג'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2565012&mode=10&name=דיג דיג דוג: שלוש ארבע לעבודה&module=wallavod')
		list.append('&youtube_id=cRPDgeKNP3s') #דיג דיג דוג 1
		list.append('&youtube_id=2lKQWaQZ4f8') #דיג דיג דוג 3
		list.append('&youtube_id=Cz_zw8yKurM') #דיג דיג דוג לפעוטות
		list.append('&youtube_id=j-53oVXHwlA') #דיג דיג דוג שלוש ארבע לעבודה
	addDir('אוסף דיג דיג דוג',list,17,'','','1',0,fanart)
	
	'''אוסף שירי אריק איינשטיין'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=Y1DUYLhl0H0') #מהופ
	addDir('אוסף שירי אריק איינשטיין',list,17,'','','1',0,fanart)
	
	'''עץ השירים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538763&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538765&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538766&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538767&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538768&mode=10&module=wallavod')
	addDir('עץ השירים',list,17,'','','1',0,fanart)

	'''שירי דתיה בן דור''' 
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL1m90DJcwEbQmbZ8QLo3JCMs38VyioavB')
		list.append('&youtube_pl=PL1m90DJcwEbQmbZ8QLo3JCMs38VyioavB')
		list.append('&youtube_pl=PLAZEBF7w1an9tqCwiQ7rYI8kB2RY1sU7x')
	addDir(addonString(4).encode('utf-8') + space + addonString(10112).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Datia_ben_dor_%D7%93%D7%AA%D7%99%D7%94_%D7%91%D7%9F_%D7%93%D7%95%D7%A8.jpg/250px-Datia_ben_dor_%D7%93%D7%AA%D7%99%D7%94_%D7%91%D7%9F_%D7%93%D7%95%D7%A8.jpg',addonString(101120).encode('utf-8'),'1',0,fanart)
	
	'''שירי עוזי חיטמן''' 
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2538763&mode=10&module=wallavod')
		list.append('&youtube_pl=PLB58E216840771949')
		list.append('&youtube_pl=PL0145D27A0D5E1810')
		list.append('&youtube_pl=PLC740DFBAF8C3F893')
		list.append('&youtube_id=YMLsE_DMPGQ')
		list.append('&youtube_id=21zlKTnPBcU')
	addDir(addonString(10103).encode('utf-8'),list,17,'http://www.lifemusic.co.il/files/singers/big/1248883756s56Ly.jpg',addonString(101030).encode('utf-8'),'1',0,fanart)
	
	'''שירי פרפר נחמד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL51YAgTlfPj45OPEXI-ibfJy8ON0k1ARh')
		list.append('&youtube_pl=PLNWPkdPqwKqtbM6--m50SdENigIXvoAqm') 
	addDir(addonString(10105).encode('utf-8'),list,17,thumb,addonString(101050).encode('utf-8'),'1',0,fanart)
	
	'''שירי מיכל כלפון'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLPWc8VdaIIsAHPacvuyNfA-y8VSxoh4or')
		list.append('&youtube_pl=PL9boemkB6hYz5WlmI-QH_xmRyZDpHKvt9')
	addDir(addonString(10768).encode('utf-8'),list,17,'http://yt3.ggpht.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAAAA/pfQtiUaNjng/s88-c-k-no/photo.jpg',addonString(107680).encode('utf-8'),'1',0,fanart)
	
	'''סיפורי דתיה בן דרור''' 
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLAZEBF7w1an9Evjuibug2h-g0CDGvrJGX')
		list.append('&youtube_id=x9rGd_SVleE')
		list.append('&youtube_id=Si6x12FUdoA')
		list.append('&youtube_id=PH5lD8FpVqM')
		
	addDir(addonString(3).encode('utf-8') + space + addonString(10112).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Datia_ben_dor_%D7%93%D7%AA%D7%99%D7%94_%D7%91%D7%9F_%D7%93%D7%95%D7%A8.jpg/250px-Datia_ben_dor_%D7%93%D7%AA%D7%99%D7%94_%D7%91%D7%9F_%D7%93%D7%95%D7%A8.jpg',addonString(101120).encode('utf-8'),'1',0,fanart)
	
	'''שירי ענבלי בא לי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLPWc8VdaIIsAHPacvuyNfA-y8VSxoh4or')
	addDir(addonString(10106).encode('utf-8'),list,17,'http://www.tel-aviv.gov.il/ToEnjoy/CulterAndArts/DocLib4/inbali.jpg.jpg',addonString(101060).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES101J(General_LanguageL, background, background2) #סיפורי התנ"ך
	
	'''סיפורי סבא טוביה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL6jaO-hu0IvwHsU9bzS8caFo8reAxEseX')
		list.append('&youtube_pl=PLHq0SR_JzssA6InY1XROQZ6TfqV3KbOfE')
	addDir(addonString(3).encode('utf-8') + space + addonString(10108).encode('utf-8'),list,17,'http://images.mouse.co.il/storage/2/e/b-saba.jpg',addonString(101080).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES101A(General_LanguageL, background, background2) #עמוד הבא שירים וסיפורים
	
def CATEGORIES102(name, iconimage, desc, fanart):
	background = 102
	background2 = "" #http://2.bp.blogspot.com/-Dz3-VwZZryE/Uh5ZXg7zCMI/AAAAAAAAdCQ/OmLVkdWI47c/s1600/Disney+Junior+Live+Pirate+and+Princess+Adventure+-+Jake%252C+Izzy+%2526+Cubby.jpg"
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES102Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	
	'''101 כלבים דלמטים'''
	thumb = 'http://www.pashbar.co.il/pictures/show_big_0712083001297352431.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=RxMNt87ghsQ')
	addDir(addonString(10202).encode('utf-8'),list,5,thumb,addonString(102020).encode('utf-8'),'1',0,fanart)
	
	'''Pantomime Collections'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_id=6CSJWnljAiA') #Harvey Grammar Pantomime
		list.append('&youtube_id=P3GzNZ2O3ik') #Nuffield College
		list.append('&youtube_id=mnXhoqpehUo') #Dick Whittington
		list.append('&youtube_id=M4d6d9uDCwc') #
		
		
	addDir('Pantomime Collections',list,17,'','','1',0,fanart)
	
	'''אי המטמון'''
	thumb = 'http://images.mouse.co.il/storage/0/e/ggg--Matmon.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=')
		#list.append('&youtube_id=Cmd0VxJmmBA')
	addDir(addonString(10204).encode('utf-8'),list,5,thumb,addonString(102040).encode('utf-8'),'1',0,fanart)
	
	'''אלאדין'''
	list = []
	fanart = 'http://www.jfuoco.com/images/trips/08/alladin_cast.gif'
	thumb = 'http://www.atmtxphoto.com/Blog/Creative-commons/i-6HJdmnn/0/L/disney-california-adventure-aladdin-stage-show-3-L.jpg'
	if 'Hebrew' in General_LanguageL:
		fanart = 'https://i.ytimg.com/vi/rCnTx-fUa6Y/maxresdefault.jpg'
		thumb = 'http://images.mouse.co.il/storage/8/1/aladin20134412_1136250_0..jpg'
		list.append('&youtube_id=sVCYRfk3Wcc')
		list.append('&youtube_id=aIY0onCV9u0')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=iagPDqOtaKE')
		list.append('&youtube_id=zJi4hGBf5vs')
		list.append('&youtube_id=0Jgf7_WNP6o') #2011
		
	addDir(addonString(10205).encode('utf-8'),list,17,thumb,addonString(102050).encode('utf-8'),'1',0,fanart)
	
	'''אמא אווזה'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_id=V1LEbSnUeM0')
	addDir(addonString(10206).encode('utf-8'),list,5,'https://i.ytimg.com/vi/fE3emlfJRLA/hqdefault.jpg',addonString(102060).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.countrychild.co.uk/wp-content/uploads/2014/12/Mother-Goose-at-Salisbury-Playhouse-credit-Robert-Workman.jpg"))
	
	'''בילבי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=sHMEnVpDJR8')
	addDir(addonString(10207).encode('utf-8'),list,5,'http://i.ytimg.com/vi/2mxOiPccxOs/maxresdefault.jpg',addonString(102070).encode('utf-8'),'1',0,fanart)
	
	'''גאליס המופע'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&dailymotion_id=x2aps1v')
		list.append('&dailymotion_id=x2apt79')
	addDir(addonString(10209).encode('utf-8'), list,17, 'http://up389.siz.co.il/up1/znmi3xqzndjg.jpg',addonString(102090).encode('utf-8'),'1',0,fanart)
	
	'''ג'ק ואפון הפלא'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_id=AWg7mK46Hkw') #Jack and the Beanstalk
		list.append('&youtube_id=Vs8SldXFzic') #English
		
	addDir(addonString(10208).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Jack_and_the_Beanstalk_Giant_-_Project_Gutenberg_eText_17034.jpg/220px-Jack_and_the_Beanstalk_Giant_-_Project_Gutenberg_eText_17034.jpg',addonString(102080).encode('utf-8'),'1',0,fanart)
	
	'''גיבורי האור'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=nwlo00FHCRc')
	addDir(addonString(10211).encode('utf-8'),list,5,'http://www.booknet.co.il/imgs/site/prod/7294276219850b.jpg',addonString(102110).encode('utf-8'),'1',0,fanart)
	
	'''גיגיגיגונת קלטת ילדים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=tKDm79jqRcI')
	addDir(addonString(10213).encode('utf-8'),list,5,'http://erezdvd.co.il/sites/default/files/imagecache/product_full/products/369504.jpg',addonString(102130).encode('utf-8'),'1',0,fanart)
	
	'''דוד חיים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99%20%d7%94%d7%90%d7%95%d7%a8%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90&url=seasonId%3d2884528')
		list.append('&youtube_id=ugmThlqdPJw')
		list.append('&youtube_id=X3j6mQ9VgLI')
		list.append('&youtube_id=T_a52ktWfLc')
		list.append('&youtube_id=FruAxOYP0uw')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-66e32295e3b1741006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%93%D7%95%D7%93+%D7%97%D7%99%D7%99%D7%9D+-+%D7%94%D7%98%D7%99%D7%95%D7%9C+%D7%90%D7%9C+%D7%94%D7%90%D7%95%D7%A6%D7%A8&iconimage=http://img.mako.co.il/2014/09/30/kids_dod_haim_01_1920X1080_02_f.jpg')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-12e2b6e81057e31006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%93%D7%95%D7%93+%D7%97%D7%99%D7%99%D7%9D+2&iconimage=http://img.mako.co.il/2013/05/12/kids_dod_haim_02_1920X1080_f.jpg')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-7f43e7693548e31006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%93%D7%95%D7%93+%D7%97%D7%99%D7%99%D7%9D+-+%D7%94%D7%94%D7%A6%D7%92%D7%94&iconimage=http://img.mako.co.il/2014/07/21/1920X1080_Haim_Theater_f.jpg')
	addDir(addonString(10715).encode('utf-8'),list,5,'http://www.nmcunited.co.il/Images/dynamic/movies/Dod-Haim2.jpg',addonString(107150).encode('utf-8'),'1',0,fanart)
	
	'''היפה והחיה'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		pass
	addDir(addonString(10530).encode('utf-8'),list,5,'https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Beautybeastposter.jpg/220px-Beautybeastposter.jpg',addonString(105300).encode('utf-8'),'1',0,fanart)
	
	'''היפיפייה הנרדמת'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		pass
	addDir(addonString(10531).encode('utf-8'),list,5,'https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Sleeping_beauty_disney.jpg/220px-Sleeping_beauty_disney.jpg',addonString(105310).encode('utf-8'),'1',0,fanart)
	
	'''המכבים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=WnR0EuLWSOo')
	addDir(addonString(10225).encode('utf-8'),list,5,'http://www.ideals.co.il/wp-content/uploads/2015/02/nas3.jpg',addonString(102250).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/NUXjR_WIJfQ/maxresdefault.jpg"))
	
	'''הקוסם מארץ עוץ'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'http://www.habama.co.il/Habama/Upload/Children/%D7%9E%D7%90%D7%A8%D7%A5-%D7%A2%D7%95%D7%A5-%D7%A2%D7%A0%D7%A7-%D7%A7%D7%9E%D7%99%D7%A0%D7%A1%D7%A7%D7%99.jpg'
		list.append('&youtube_id=3rvK4dA5qwY')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=xkYnLdqrORE') #English
		list.append('&youtube_id=TMoIGToMI-4') #English
		list.append('&youtube_id=TnyoyDxm-Fs') #Wizard of Oz
		
	addDir(addonString(10431).encode('utf-8'),list,17,thumb,addonString(104310).encode('utf-8'),'1',0,fanart)
	
	'''הרקולס - המחזמר המלא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=UiqG4WAcvCM')
	addDir(addonString(10227).encode('utf-8'),list,5,'http://moridim.me/images/large/191.jpg',addonString(102270).encode('utf-8'),'1',0,fanart)
	
	'''יובל המבולבל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=6UrdISJBBC4')
		list.append('&youtube_id=C2Rm4IuVWNQ')
		list.append('&youtube_id=CZDniCIenbA')
		list.append('&youtube_id=H9rwsZ1roRQ')
		list.append('&youtube_id=oAkA7DnCBdE')
		#list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-a4c39d434280e31006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%A2%D7%95%D7%9C%D7%9E%D7%95+%D7%A9%D7%9C+%D7%99%D7%95%D7%91%D7%9C+%D7%94%D7%9E%D7%91%D7%95%D7%9C%D7%91%D7%9C&iconimage=http://img.mako.co.il/2013/04/21/1920X1080_yuval_world_f.jpg')
	addDir(addonString(10731).encode('utf-8'),list,17,'http://yt3.ggpht.com/-FHcf2Rxu08A/AAAAAAAAAAI/AAAAAAAAAAA/dxzE2ng3uXI/s88-c-k-no/photo.jpg',addonString(107310).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.ashdodnet.com/dyncontent/t_post/2012/7/24/26370203843604787436.jpg"))
	
	'''ילד פלא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=e5c134277697c')
	addDir(addonString(10231).encode('utf-8'),list,5,'http://shows.myfirsthomepage.co.il/admin/gamePics/yeled_pele7282014125120PM.jpg',addonString(102310).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.tamuseum.org.il/Data/Uploads/%D7%AA%D7%9E%D7%95%D7%A0%D7%94%20%D7%99%D7%9C%D7%93%20%D7%A4%D7%9C%D7%901.JPG"))
	
	'''לירן הקוסם מהאגדות'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=kNS4xMdPIos')
	addDir(addonString(10239).encode('utf-8'),list,5,'http://i.ytimg.com/vi/5gN4SMO8EfE/maxresdefault.jpg',addonString(102390).encode('utf-8'),'1',0,fanart)
	
	'''מותק הילדות התחברו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=1wLhD4yqQxU')
		list.append('&youtube_id=_Lv0UHXaY4I')
		list.append('&youtube_id=j_BClvgFwMw')
		list.append('&youtube_id=_WBgn4iw8gw')
	addDir(addonString(10243).encode('utf-8'),list,17,'http://media.org.il/images/Baby.girls.tap.the.musical.IL.1999_Front.Cover.jpg',addonString(102430).encode('utf-8'),'1',0,fanart)

	'''מותק של פסטיבל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLE915B350E437A7D8')
		list.append('&youtube_pl=PL8C370A361DD07BDB')
		list.append('&youtube_id=t2ksCC_RyLw')
		list.append('&youtube_id=2KQBeOM')
	addDir(addonString(10244).encode('utf-8'),list,5,'http://www.yap.co.il/prdPics/4991_desc3_5_1_1409123377.jpg',addonString(102440).encode('utf-8'),'1',0,fanart)
	
	'''מיכל הקטנה''' 
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%9e%d7%99%d7%9b%d7%9c%20%d7%94%d7%a7%d7%98%d7%a0%d7%94%20%d7%a8%d7%95%d7%a6%d7%94%20%d7%9c%d7%94%d7%99%d7%95%d7%aa%20%d7%92%d7%93%d7%95%d7%9c%d7%94&url=seasonId%3d2888149')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%9e%d7%99%d7%9b%d7%9c%20%d7%94%d7%a7%d7%98%d7%a0%d7%94%20%d7%95%d7%94%d7%98%d7%95%d7%a0%d7%98%d7%95%d7%a0%d7%99%d7%9d&url=seasonId%3d2890384')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2567432&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2698903&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D258362&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-d04048a07975f31006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%9E%D7%99%D7%9B%D7%9C+%D7%94%D7%A7%D7%98%D7%A0%D7%94+%22%D7%94%D7%A9%D7%99%D7%A8+%D7%A9%D7%91%D7%9C%D7%91%22&iconimage=http://img.mako.co.il/2013/06/24/michal_shir_f.jpg')
		list.append('&youtube_id=IEeuv8mtRLI')
	addDir(addonString(10245).encode('utf-8'),list,5,'http://www.pashbar.co.il/pictures/show_big_0523173001376412565.jpg',addonString(102450).encode('utf-8'),'1',"",fanart)
	
	'''מרקו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=XgnCNCt71d8')
	addDir(addonString(10248).encode('utf-8'),list,5,'http://www.ykp.co.il/cd_halev.jpg',addonString(102480).encode('utf-8'),'1',0,fanart)
	
	'''משחקי הפסטיגל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=d2953353ab9e8')
	addDir(addonString(10250).encode('utf-8'),list,5,'http://www.ligdol.co.il/Upload/pestigal2014_poster.jpg',addonString(102500).encode('utf-8'),'1',0,fanart)
	
	'''נסיך מצרים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=LFoX4vn6Obg')
	addDir(addonString(10252).encode('utf-8'),list,5,'http://www.ideals.co.il/wp-content/uploads/2015/02/nas3.jpg',addonString(102520).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/NUXjR_WIJfQ/maxresdefault.jpg"))
	
	'''סינדרלה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=snr9wxyEzpA')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=Hp_ekaM6wLk')
		list.append('&youtube_id=_ywvSa0JSEE')
	addDir(addonString(10255).encode('utf-8'),list,5,'http://afisha.israelinfo.ru/pictures/19949.jpg',addonString(102550).encode('utf-8'),'1',0,fanart)
	
	'''ספר הגונגל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=TlWVoNz_B3o')
	addDir(addonString(10258).encode('utf-8'),list,5,'http://images.mouse.co.il/storage/3/7/ggg--book20090908_2343750_0..jpg',addonString(102580).encode('utf-8'),'1',0,fanart)
	
	'''עמי ותמי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=8d6a2e7a3cd54')
	addDir(addonString(10261).encode('utf-8'),list,5,'http://www.tivon.co.il/vault/Zoar/amitami-B.jpg',addonString(102610).encode('utf-8'),'1',0,fanart)
	
	'''עליבאבא וארבעים השודדים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=gxgvTe3kPGY')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=SmG8F9-ZH-0')	
		
	addDir(addonString(10262).encode('utf-8'),list,5,'http://i.ytimg.com/vi/EMtHOrNBXKU/hqdefault.jpg',addonString(102620).encode('utf-8'),'1',0,fanart)
	
	'''עליסה בארץ הפלאות'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=4Zp-6Ts07Qw')
	addDir(addonString(10263).encode('utf-8'),list,5,'http://images.mouse.co.il/storage/3/0/b--alice.jpg',addonString(102630).encode('utf-8'),'1',0,fanart)
	
	'''פיטר פן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=gTuMB5sz8pY')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=6l70mf7d2Jw')	
	
	addDir(addonString(10267).encode('utf-8'),list,17,'http://i48.tinypic.com/f5ceuq.jpg',addonString(102670).encode('utf-8'),'1',0,fanart)
	
	'''פסטיבל כיף לי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCTxlaUXzxohVekL_Zym-hsw')
		list.append('&youtube_id=lZgpGH9wTHY')
	addDir(addonString(10269).encode('utf-8'),list,5,'http://3.bp.blogspot.com/-LIy_QkefJ-M/UuaoyVJu82I/AAAAAAAAAus/Dpd7rKKbUfM/s1600/KEF2014+POS+copy.jpg',addonString(102690).encode('utf-8'),'1',0,fanart)
	
	'''פסטיגל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCKs_S8Uo5rLCNhlSanFpfFQ')
		list.append('&youtube_ch=UC8z6QWcSpDfeHY0sni4IDwA')
		list.append('&youtube_pl=PLwimDnICcPKPL4MdOLIQrGDMTOAshuQ2l')
	addDir(addonString(10270).encode('utf-8'),list,17,'http://yt3.ggpht.com/-2Nux9ubjSCA/AAAAAAAAAAI/AAAAAAAAAAA/P8I968rchgE/s88-c-k-no/photo.jpg',addonString(102700).encode('utf-8'),'1',"",fanart)
	
	'''צ'פצ'ולה' - מיכל כלפון'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=EKlFN3awN_w')
		list.append('&youtube_id=UC64wDQFgTq9RpI1P8_p-SxA')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-be230098ac9a051006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%A6%27%D7%A4%D7%A6%27%D7%95%D7%9C%D7%94+%D7%95%D7%94%D7%A8%D7%A4%D7%AA%D7%A7%D7%90%D7%95%D7%AA+%D7%94%D7%97%D7%99%D7%95%D7%AA&iconimage=http://img.mako.co.il/2015/10/27/kids_C_animal_adventure_f.jpg')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2728550&mode=10&module=wallavod')
	addDir(addonString(10768).encode('utf-8'),list,17,'http://yt3.ggpht.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAAAA/pfQtiUaNjng/s88-c-k-no/photo.jpg',addonString(107680).encode('utf-8'),'1',0,fanart)
	
	'''רובין הוד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=6nZk0H89jDQ')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=iyke1Yx0y78')
		list.append('&youtube_id=2uMZwF9hlVo')
		list.append('&youtube_id=zOp0eZ08hYE')
		list.append('&youtube_id=Vb72XqW9vOU') #2014
		
	addDir(addonString(10272).encode('utf-8'),list,17,'http://erezdvd.co.il/sites/default/files/imagecache/product_full/products/14810.jpg',addonString(102720).encode('utf-8'),'1',0,fanart)
	
	'''רובין זו קרוזו'''
	thumb = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Robinson_Crusoe_and_Man_Friday_Offterdinger.jpg/170px-Robinson_Crusoe_and_Man_Friday_Offterdinger.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=EVEc0RyDhvM')
		list.append('&youtube_id=kZ4zzYBD4Cs')
		list.append('&youtube_id=KqnsUtNPhFE')
		
	addDir(addonString(10273).encode('utf-8'),list,17,thumb,addonString(102730).encode('utf-8'),'1',0,fanart)
	
	'''רינת גבאי'''
	thumb = 'http://img.mako.co.il/2013/09/16/fantasy50X70-poster_SHOWS_g.jpg'
	fanart = 'https://i.ytimg.com/vi/IZoa3LxE0MY/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=ykKWS-Udw2s')
	addDir(addonString(10274).encode('utf-8'),list,5,thumb,addonString(102740).encode('utf-8'),'1',0,fanart)
	
	'''שורום זורום'''
	thumb = 'http://images1.ynet.co.il/PicServer4/2015/07/30/6201572/01_SM.jpg'
	fanart = 'https://i.ytimg.com/vi/YJJZsGH34NU/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=9rGV96uhqPw')
	addDir(addonString(10284).encode('utf-8'),list,5,thumb,addonString(102840).encode('utf-8'),'1',0,fanart)
	
	'''שלגיה והצייד'''
	thumb = 'http://www.dossinet.me/coverage_pics/1b5d66af0d230ff716d50f07fd6defc0.jpg'
	fanart = 'https://i.ytimg.com/vi/7zaOt1kF6Bw/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=0rPEJ-kD1dc')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=6SIbUd6inRU')
		list.append('&youtube_id=PEK_gfl60R8')
		list.append('&youtube_id=Mif76xXF8zo')
	addDir(addonString(10287).encode('utf-8'),list,17,thumb,addonString(102870).encode('utf-8'),'1',0,fanart)
	
	'''סבא טוביה'''
	thumb = 'http://yt3.ggpht.com/--gG5kz68N_k/AAAAAAAAAAI/AAAAAAAAAAA/37Cr6jMJSCg/s88-c-k-no/photo.jpg'
	fanart = 'https://i.ytimg.com/vi/wBQ__bIiJkI/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLE494A88ED3823578')
	addDir(addonString(10108).encode('utf-8'),list,5,thumb,addonString(1010800).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES102A(General_LanguageL, background, background2) #עמוד הבא שירים וסיפורים
	
def CATEGORIES104(name, iconimage, desc, fanart):
	background = 104
	background2 = "" #http://www.canadiananimationresources.ca/wp-content/uploads/2012/10/9-Story-Arthur-Couch.jpg"
	
	'''חיפוש'''
	if 'Hebrew' in General_LanguageL: addDir('-' + localize(137) + space + 'Sdarot TV','&activatewindow=plugin://plugin.video.sdarot.tv/?mode=6&name=%5bCOLOR%20red%5d%20%d7%97%d7%a4%d7%a9%20%20%5b%2fCOLOR%5d&summary&url=http%3a%2f%2fwww.sdarot.wf%2fsearch',8,featherenceserviceicons_path + 'se.png','http://www.sdarot.wf/','1',0,fanart)
	#if 'English' in General_LanguageL: addDir('-' + localize(137) + space + 'cartoons8 Anime','plugin://plugin.video.cartoons8/?description&iconimage=&mode=8&name=Anime%20-%20Search&url=http%3a%2f%2fchiaanime.co%2fSearch%3fs%3d',8,featherenceserviceicons_path + 'se.png','http://cartoons8.me/','1',0,fanart)
	#if 'English' in General_LanguageL: addDir('-' + localize(137) + space + 'cartoons8 Cartton','plugin://plugin.video.cartoons8/?description&iconimage=&mode=8&name=Cartoon%20-%20Search&url=http%3a%2f%2f9cartoon.me%2fSearch%3fs%3d',8,featherenceserviceicons_path + 'se.png','http://cartoons8.me/','1',0,fanart)
	
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES104Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	
	'''101 כלבים דלמטים'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73719-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73719-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5D101%20Dalmatians%3A%20The%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2F101-dalmations-the-series')
		
	addDir(addonString(10393).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/73719-2.jpg',addonString(10393).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73719-1.jpg"))
	
	'''אאוץ'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1864.jpg&mode=3&name=%d7%90%d7%90%d7%95%d7%a5%27%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1864&series_name=%d7%90%d7%90%d7%95%d7%a5%27%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1864%2foperation-ouch-%d7%90%d7%90%d7%95%d7%a5-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	addDir(addonString(10401).encode('utf-8'),list,6,thumb,addonString(104010).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104L(General_LanguageL, background, background2) #אגדות האחים גרים
	
	'''אגדות המלך שלמה'''
	thumb = 'https://upload.wikimedia.org/wikipedia/he/e/ea/Kingsolomon.jpg'
	fanart = 'https://i.ytimg.com/vi/MFktw6g09l4/hqdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom83=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f815.jpg&mode=3&name=%d7%90%d7%92%d7%93%d7%95%d7%aa%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%a9%d7%9c%d7%9e%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=815&series_name=%d7%90%d7%92%d7%93%d7%95%d7%aa%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%a9%d7%9c%d7%9e%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f815%2ftales-of-a-wise-king-hebdub-%d7%90%d7%92%d7%93%d7%95%d7%aa-%d7%94%d7%9e%d7%9c%d7%9a-%d7%a9%d7%9c%d7%9e%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLOx5NGhretuY8wp75WCY5PQQx8agiZ2IC')
	addDir(addonString(10402).encode('utf-8'),list,17,thumb,addonString(104020).encode('utf-8'),'1',0,fanart)
	
	'''אוגי והמקקים*'''
	thumb = 'https://www.thetvdb.com/banners/posters/82956-3.jpg'
	if 'Hebrew' in General_LanguageL: thumb = 'https://www.thetvdb.com/banners/posters/82956-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82956-3.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2830054')
	list.append('&youtube_pl=PLsN1aN-kzJnOgSDAwE5PPF3IH9fGH57Xx')
	list.append('&youtube_pl=PLDks7iHzd1bV7S9aLZfEtFmoToSrJPPdE')
	addDir(addonString(10429).encode('utf-8'),list,17,thumb,addonString(104290).encode('utf-8'),'1',0,fanart)
	
	'''אווטאר*'''
	thumb = 'https://www.thetvdb.com/banners/posters/74852-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/74852-11.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F8%2Fimage%2F555x418%2Favatar-the-last-airbender-episodes.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAvatar%3A%20The%20Last%20Airbender%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Favatar-the-last-airbender')
	addDir(addonString(10340).encode('utf-8'),list,6,thumb,addonString(103400).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104O(General_LanguageL, background, background2) #אוטובוס הקסמים
	
	'''איירון מן'''
	thumb = 'https://www.thetvdb.com/banners/fanart/original/76278-9.jpg'
	fanart = 'https://www.thetvdb.com/banners/posters/76278-8.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1461.jpg&mode=3&name=%d7%90%d7%99%d7%99%d7%a8%d7%95%d7%9f%20%d7%9e%d7%9f%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1461&series_name=%d7%90%d7%99%d7%99%d7%a8%d7%95%d7%9f%20%d7%9e%d7%9f%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1461%2firon-man-%d7%90%d7%99%d7%99%d7%a8%d7%95%d7%9f-%d7%9e%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F66%2Fimage%2F555x418%2FIron-Man-animated-series.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DIron%20Man%20(TV%20Series%201994-1996)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Firon-man-tv-series-1994-1996')
	
	addDir(addonString(10349).encode('utf-8'),list,6,thumb,addonString(103490).encode('utf-8'),'1',0,fanart)
	
	'''אלאדין'''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73981-5.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73981-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAladdin%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Faladdin')
	if 'Italian' in General_LanguageL:
		list.append('&dailymotion_pl=x3qyi3') #Italian #S1
		list.append('&dailymotion_pl=x46bvx') #Italian #S1
		list.append('&dailymotion_pl=x4129o') #Italian #S2
		list.append('&dailymotion_pl=x412a4') #Italian #S3
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL-fIrVtK0oZpQ7WmzXI04nbenZ-W4nj4Z')
	addDir(addonString(10529).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/73981-5.jpg',addonString(105290).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73981-5.jpg", default=background2))
	
	'''אמיץ הכלב הפחדן'''
	thumb = 'https://www.thetvdb.com/banners/posters/77435-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77435-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F7%2Fimage%2F555x418%2Fcourage-the-cowardly-dog-show.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DCourage%20the%20Cowardly%20Dog%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fcourage-the-cowardly-dog')
	addDir(addonString(10339).encode('utf-8'),list,6,thumb,addonString(103390).encode('utf-8'),'1',0,fanart)
	
	'''אנימניאקס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1104.jpg&mode=3&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1104&series_name=%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1104%2fanimaniacs-%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72879-6.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72879-4.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAnimaniacs%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fanimaniacs')
	addDir(addonString(10404).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/72879-4.jpg',addonString(104040).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/72879-6.jpg", default=background2))
								 
	'''אקס מן'''
	thumb = 'https://www.thetvdb.com/banners/posters/76115-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76115-5.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1104.jpg&mode=3&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1104&series_name=%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1104%2fanimaniacs-%d7%90%d7%a0%d7%99%d7%9e%d7%a0%d7%99%d7%90%d7%a7%d7%a1-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLN0EJVTzRDL9ObPf7m4GCN2BL6Ayreybh')
	addDir(addonString(10405).encode('utf-8'),list,17,thumb,addonString(104050).encode('utf-8'),'1',0,fanart)
							  
	'''אקס-מן: הדור הבא'''
	thumb = 'https://www.thetvdb.com/banners/posters/71168-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/71168-11.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1435.jpg&mode=3&name=%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%3a%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1435&series_name=%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%3a%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1435%2fx-men-evolution-%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f-%d7%94%d7%93%d7%95%d7%a8-%d7%94%d7%91%d7%90-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	addDir(addonString(10406).encode('utf-8'),list,6,thumb,addonString(104060).encode('utf-8'),'1',0,fanart)
	
	'''ארצ'ר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&name_=Season 1&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fseason%2F60%2Fimage%2F555x418%2FArcher_Season_1_Episodes.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DArcher%20(TV%20series)%20Full%20Episodes%20-%20Season%201%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Farcher-full-episodes%2Fseason%2F1')
		list.append('&name_=Season 2&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fseason%2F61%2Fimage%2F555x418%2FArcher_Season_2_Episodes.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DArcher%20(TV%20series)%20Full%20Episodes%20-%20Season%202%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Farcher-full-episodes%2Fseason%2F2')
		
	addDir(addonString(10364).encode('utf-8'),list,6,'https://www.thetvdb.com/banners/_cache/posters/110381-1.jpg',addonString(103640).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://www.thetvdb.com/banners/fanart/original/110381-23.jpg", default=background2))
	
	'''ארתור'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f461.jpg&mode=3&name=%d7%90%d7%a8%d7%aa%d7%95%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=461&series_name=%d7%90%d7%a8%d7%aa%d7%95%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f461%2farthur-%d7%90%d7%a8%d7%aa%d7%95%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2558030')
		list.append('&youtube_pl=PL17sRM9raf1Q-i_fTe45N0UBqNgdnZTD6')
		list.append('&youtube_pl=PLN0EJVTzRDL96B86muPPFwgdymQjlwmLZ')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F74678-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F74678-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DArthur%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Farthur')
	addDir(addonString(10407).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/74678-3.jpg',addonString(104070).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/74678-3.jpg", default=background2))
	
	'''באג בראש'''
	thumb = 'https://images-na.ssl-images-amazon.com/images/M/MV5BYjhlM2ZjNDEtM2M3OS00ODIxLTgzZDUtMzE0MGUzNzZlMDEwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTk5NTYxODM@._V1_.jpg'
	fanart = 'https://i.ytimg.com/vi/mY2o60SVGug/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1497.jpg&mode=3&name=%d7%91%d7%90%d7%92%20%d7%91%d7%a8%d7%90%d7%a9%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1497&series_name=%d7%91%d7%90%d7%92%20%d7%91%d7%a8%d7%90%d7%a9%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1497%2fbug-alert-%d7%91%d7%90%d7%92-%d7%91%d7%a8%d7%90%d7%a9-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	addDir(addonString(10408).encode('utf-8'),list,6,thumb,addonString(104080).encode('utf-8'),'1',0,fanart)	
	
	'''באגס באני'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72514-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72514-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBugs%20Bunny%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbugs-bunny')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F13%2Fimage%2F555x418%2Fbugs-bunny-show.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Bugs%20Bunny%20Show%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-bugs-bunny-show')
		
	addDir(addonString(10385).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/72514-5.jpg',addonString(103850).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/72514-1.jpg", default=background2))
	
	'''באטמן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76168-14.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F76168-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBatman%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbatman-the-animated-series')
		list.append('&name_=The New Batman Adventures&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F57%2Fimage%2F555x418%2FThe-New-Batman-Adventures.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20New%20Batman%20Adventures%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-new-batman-adventures-tv-series')
		
	addDir(addonString(10388).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/76168-3.jpg',addonString(103880).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/76168-14.jpg", default=background2))
	
	'''בארץ הקטקטים'''
	thumb = 'https://www.thetvdb.com/banners/posters/251299-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/251299-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/251299-4.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=https%3A%2F%2Fwww.sdarot.live%2Fmedia%2Fseries%2F1323.jpg&mode=5&name=%D7%A2%D7%95%D7%A0%D7%94%201&season_id=1&series_id=1323&series_name=%D7%91%D7%90%D7%A8%D7%A5-%D7%94%D7%A7%D7%98%D7%A7%D7%98%D7%99%D7%9D-%D7%9E%D7%93%D7%95%D7%91%D7%91-the-littl-bits%2Fseason%2F1&summary=%D7%A1%D7%99%D7%A4%D7%95%D7%A8%D7%9D%20%D7%A9%D7%9C%20%D7%94%D7%A7%D7%98%D7%A7%D7%98%D7%99%D7%9D%20%D7%A9%D7%97%D7%99%D7%99%D7%9D%20%D7%91%D7%A7%D7%95%D7%98%D7%92%26%23039%3B%D7%99%D7%9D%20%D7%A7%D7%98%D7%A0%D7%99%D7%9D%20%D7%9C%D7%9E%D7%A8%D7%92%D7%9C%D7%95%D7%AA%20%D7%94%D7%99%D7%A2%D7%A8%20%D7%95%D7%99%D7%95%D7%A6%D7%90%D7%99%D7%9D%20%D7%9C%D7%94%D7%A8%D7%A4%D7%AA%D7%A7%D7%90%D7%95%D7%AA.%20&url=https%3A%2F%2Fwww.sdarot.live%2Fwatch%2F1323%2F%D7%91%D7%90%D7%A8%D7%A5-%D7%94%D7%A7%D7%98%D7%A7%D7%98%D7%99%D7%9D-%D7%9E%D7%93%D7%95%D7%91%D7%91-the-littl-bits%2Fseason%2F1')
		list.append('&youtube_pl=PLN0EJVTzRDL-WaGew7sZQHQc1l48LSZmp')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLnMOar3QFQYI4IlS9nNLZ_3wFMa-mf2pP') #English
		list.append('&youtube_pl=PLZs0gQed9tMQsC9dAjvjlHeEzibEliBjW') #English
	addDir(addonString(10409).encode('utf-8'),list,17,thumb,addonString(104090).encode('utf-8'),'1',0,fanart)	
	
	'''בוב ספוג מכנס מרובע'''
	thumb = 'https://www.thetvdb.com/banners/posters/75886-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75886-11.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%d7%a2%d7%95%d7%93%20%d7%a4%d7%a8%d7%a7%d7%99%d7%9d&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1688134%26page%3d2')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e1%e5%e1%f1%f4%e5%e2%20%ee%eb%f0%f1%20%ee%f8%e5%e1%f2&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1688133')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f490.jpg&mode=3&name=%d7%91%d7%95%d7%91%d7%a1%d7%a4%d7%95%d7%92%20%d7%9e%d7%9b%d7%a0%d7%a1%20%d7%9e%d7%a8%d7%95%d7%91%d7%a2%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=490&series_name=%d7%91%d7%95%d7%91%d7%a1%d7%a4%d7%95%d7%92%20%d7%9e%d7%9b%d7%a0%d7%a1%20%d7%9e%d7%a8%d7%95%d7%91%d7%a2%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f490%2fspongebob-squarepants-%d7%91%d7%95%d7%91%d7%a1%d7%a4%d7%95%d7%92-%d7%9e%d7%9b%d7%a0%d7%a1-%d7%9e%d7%a8%d7%95%d7%91%d7%a2-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F75886-10.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F75886-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSpongeBob%20SquarePants%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fspongebob-squarepants')
		list.append('&youtube_pl=PLjDLgg_nO1v6sKrBN5fm-XZf2f52ko7E7') #English
	addDir(addonString(10410).encode('utf-8'),list,6,thumb,addonString(104100).encode('utf-8'),'1',0,fanart)
	
	'''בולי איש השלג'''
	thumb = 'https://www.thetvdb.com/banners/posters/261419-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/261419-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.live%2fmedia%2fseries%2f1642.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1642&series_name=%d7%91%d7%95%d7%9c%d7%99%20%d7%90%d7%99%d7%a9%20%d7%94%d7%a9%d7%9c%d7%92%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a2%d7%9c%d7%99%d7%9c%d7%95%d7%aa%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%91%d7%95%d7%9c%d7%99%20%d7%90%d7%99%d7%a9%20%d7%94%d7%a9%d7%9c%d7%92%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%91%d7%9b%d7%a4%d7%a8%20%d7%94%d7%91%d7%95%d7%9c%d7%99%d7%9d.%20%d7%9e%d7%a1%d7%a4%d7%a8%d7%aa%20%d7%a2%d7%9c%20%d7%91%d7%95%d7%9c%d7%99%20%d7%90%d7%99%d7%a9%20%d7%a9%d7%9c%d7%92%20%d7%a9%d7%94%d7%99%d7%a8%d7%97%20%d7%94%d7%a4%d7%99%d7%97%20%d7%91%d7%95%20%d7%95%d7%91%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%a8%d7%95%d7%97%20%d7%97%d7%99%d7%99%d7%9d.%20%d7%a7%d7%a1%d7%9e%d7%95%20%d7%a9%d7%9c%20%d7%94%d7%99%d7%a8%d7%97%20%d7%9e%d7%95%d7%a0%d7%a2%20%d7%9e%d7%94%d7%9d%20%d7%9e%d7%9c%d7%94%d7%a0%d7%9e%d7%a1%20%d7%92%d7%9d%20%d7%91%d7%a7%d7%99%d7%a5%20%d7%95%d7%91%d7%a9%d7%9e%d7%a9%2c%20%d7%95%d7%9b%d7%9a%20%d7%94%d7%9d%20%d7%9e%d7%98%d7%99%d7%99%d7%9c%d7%99%d7%9d%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d%2c%20%d7%9e%d7%a9%d7%97%d7%a7%d7%99%d7%9d%2c%20%d7%a9%d7%95%d7%97%d7%99%d7%9d%20%d7%95%d7%9e%d7%91%d7%9c%d7%99%d7%9d.%20%2a%2a%2a%d7%91%d7%9c%d7%a2%d7%93%d7%99%20%d7%9c%d7%90%d7%aa%d7%a8%20Sdarot.TV%2a%2a%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1642%2fbouli-%d7%91%d7%95%d7%9c%d7%99-%d7%90%d7%99%d7%a9-%d7%94%d7%a9%d7%9c%d7%92-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL0o6qImfDA9rt-5UwjlPs-9pVON7-LPA_')
		list.append('&youtube_id=2j2ISqZ40GU')
		list.append('&youtube_id=oV_sUQa4BLE')
		list.append('&youtube_id=qi5D5LnmrYk')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLSqq8hVJQnpXoxPOXP0L_zOJ0mJ2kuBt_')
		list.append('&youtube_pl=PLSqq8hVJQnpWtEDZBrYgznCfeuu8-1Jd3')
	addDir(addonString(10411).encode('utf-8'),list,17,thumb,addonString(104110).encode('utf-8'),'1',0,fanart)
	
	'''בילבי'''
	thumb = 'https://www.thetvdb.com/banners/posters/78508-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78508-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/78508-3.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1159.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1159&series_name=%d7%91%d7%99%d7%9c%d7%91%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%91%d7%99%d7%9c%d7%91%d7%99%20%d7%94%d7%99%d7%90%20%d7%99%d7%9c%d7%93%d7%94%20%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%aa%20%d7%91%d7%9e%d7%99%d7%a0%d7%94%20%d7%a9%d7%a2%d7%95%d7%a9%d7%94%20%d7%9b%d7%9c%20%d7%9e%d7%94%20%d7%a9%d7%91%d7%90%20%d7%9c%d7%94.%20%d7%94%d7%99%d7%90%20%d7%97%d7%96%d7%a7%d7%94%20%d7%95%d7%90%d7%9e%d7%99%d7%a6%d7%94%2c%20%d7%97%d7%9b%d7%9e%d7%94%20%d7%9e%d7%9b%d7%95%d7%9c%d7%9d%2c%20%d7%a9%d7%95%d7%91%d7%91%d7%94%20%d7%95%d7%91%d7%9c%d7%92%d7%a0%d7%99%d7%a1%d7%98%d7%99%d7%aa%20%d7%9c%d7%90%20%d7%a7%d7%98%d7%a0%d7%94.%20%d7%94%d7%99%d7%90%20%d7%97%d7%99%d7%94%20%d7%91%d7%95%d7%99%d7%9c%d7%94%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%94%3a%20%d7%94%d7%90%d7%97%d7%99%d7%9d%20%d7%98%d7%95%d7%9e%d7%99%20%d7%95%d7%90%d7%a0%d7%99%d7%a7%d7%94%2c%20%d7%94%d7%a7%d7%95%d7%a3%20%22%d7%9e%d7%a8%20%d7%a0%d7%9c%d7%a1%d7%95%d7%9f%22%20%d7%95%d7%94%d7%a1%d7%95%d7%a1%20%d7%a9%d7%9c%d7%94.%20%d7%94%d7%97%d7%91%d7%95%d7%a8%d7%94%20%d7%97%d7%95%d7%95%d7%94%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a8%d7%91%d7%95%d7%aa%20%d7%95%d7%9c%d7%a4%d7%a2%d7%9e%d7%99%d7%9d%20%d7%92%d7%9d%20%d7%9e%d7%a1%d7%aa%d7%91%d7%9b%d7%aa%20%d7%91%d7%a6%d7%a8%d7%95%d7%aa%3b%20%d7%90%d7%91%d7%9c%2c%20%d7%9c%d7%90%20%d7%9c%d7%93%d7%90%d7%95%d7%92%20%d7%91%d7%99%d7%9c%d7%91%d7%99%20%d7%aa%d7%9e%d7%99%d7%93%20%d7%9e%d7%a6%d7%9c%d7%99%d7%97%d7%94%20%d7%9c%d7%94%d7%aa%d7%92%d7%91%d7%a8%20%d7%a2%d7%9c%20%d7%9b%d7%9c%20%d7%94%d7%a7%d7%a9%d7%99%d7%99%d7%9d%20%d7%94%d7%a2%d7%95%d7%9e%d7%93%d7%99%d7%9d%20%d7%91%d7%93%d7%a8%d7%9a%20%d7%91%d7%96%d7%9b%d7%95%d7%aa%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%d7%99%d7%94%20%d7%94%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%99%d7%9d%2c%20%d7%94%d7%90%d7%a0%d7%a8%d7%92%d7%99%d7%94%20%d7%95%d7%94%d7%93%d7%9e%d7%99%d7%95%d7%9f%20%d7%94%d7%9e%d7%a4%d7%95%d7%aa%d7%97%20%d7%a9%d7%9c%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1159%2fpippi-longstocking-%d7%91%d7%99%d7%9c%d7%91%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_id=CBWXP_5gxSw')
		list.append('&youtube_id=kgLCdl2q8XQ')
		list.append('&youtube_id=5tc2MzqqHH8')
		list.append('&youtube_id=L878q4J48L8')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLeagipoZmyfkWkyetCWsJMGy8yBvHdJs-')
	addDir(addonString(10207).encode('utf-8'),list,17,thumb,addonString(102070),'1',0,fanart)
	
	'''בנות הים פיצ'י פיצ'י פיץ'''
	thumb = 'https://www.thetvdb.com/banners/posters/75872-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75872-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f550.jpg&mode=3&name=%d7%91%d7%a0%d7%95%d7%aa%20%d7%94%d7%99%d7%9d%20%d7%a4%d7%99%d7%a6%27%d7%99%20%d7%a4%d7%99%d7%a6%27%d7%99%20%d7%a4%d7%99%d7%a5%27%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=550&series_name=%d7%91%d7%a0%d7%95%d7%aa%20%d7%94%d7%99%d7%9d%20%d7%a4%d7%99%d7%a6%27%d7%99%20%d7%a4%d7%99%d7%a6%27%d7%99%20%d7%a4%d7%99%d7%a5%27%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f550%2fmermaid-melody-pichi-pichi-pitch-%d7%91%d7%a0%d7%95%d7%aa-%d7%94%d7%99%d7%9d-%d7%a4%d7%99%d7%a6-%d7%99-%d7%a4%d7%99%d7%a6-%d7%99-%d7%a4%d7%99%d7%a5-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLXLQCKKIyvStclVXSB76tdtDptKZLscJ_')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLBB047FDCZ8rDOI45Qtom7OmnJPee0MIs')
	if 'Japanish' in General_LanguageL:
		list.append('&youtube_pl=PLBB047FDCZ8rDOI45Qtom7OmnJPee0MIs')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLlDqNLAXdnhj-i12wz939vp61gr41yJOC')
	addDir(addonString(10412).encode('utf-8'),list,17,thumb,addonString(104120).encode('utf-8'),'1',0,fanart)
	
	'''בנימין הפיל'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb767lthA5ZrIux5ierTsdY8X') #בנימין הפיל
		list.append('&youtube_pl=PL1SAyTUFBb74t4LAyNvAwQrPhqpz8aPl9')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb74M_o7qtwLX507S1U11DFdq') #בנימין הפיל
		list.append('&youtube_pl=')
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb76vI6mmDVJW-idZzy5w3O95') #בנימין הפיל
		list.append('&youtube_pl=')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb76lUw0NZmBs5wivH7C2rDjH') #בנימין הפיל
		list.append('&youtube_pl=')
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PL8xBm2jGFeURg8zePCAvOmz0HKF0Buxx9') #בנימין הפיל
		list.append('&youtube_pl=PL1SAyTUFBb74hUX32r6aqasGENGL4YShb')
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb76FQRP8IUUdRWdyvejE7KHg') #בנימין הפיל
		list.append('&youtube_pl=')	
	if 'French' in General_LanguageL:
		list.append('&youtube_id=6M2Ll1ckj-o')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL1SAyTUFBb77CVJW1egme_gOlYTcPsy1X') #בנימין הפיל
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
	addDir(addonString(10434).encode('utf-8'),list,17,'https://s-media-cache-ak0.pinimg.com/736x/3a/bf/04/3abf042ce92ac9656ca71f7de3c6f969.jpg',addonString(104340).encode('utf-8'),'1',0,fanart)
	
	'''בננמן'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78672-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78672-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBananaman%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbananaman')
	addDir(addonString(10497).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/78672-2.jpg',addonString(104970).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/78672-2.jpg", default=background2))
	
	'''בננות בפיג'מות'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F250082-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F250082-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBananas%20in%20Pyjamas%202011%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbananas-in-pyjamas-2011')
	addDir(addonString(10400).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/250082-1.jpg',addonString(104000).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/250082-2.jpg", default=background2))
		
	'''בראץ'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/271251-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/271251-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F271251-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F271251-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBratz%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbratz')
		
	addDir(addonString(10386).encode('utf-8'),list,6,thumb,addonString(103860).encode('utf-8'),'1',0,fanart)
	
	'''ברבי'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/266242-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/266242-1.jpg'
	list = []
	
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLL-dZ_buCnGLL_5O0KJQE68_2Vqb55tls') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F266242-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F266242-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBarbie%3A%20Life%20in%20the%20Dreamhouse%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbarbie-life-in-the-dreamhouse')
		list.append('&youtube_pl=PLUyVAz5vm69lBuq2509ziZzWomSBhd4x-') #English
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=PL3_OyqmNQ5jogMj02awwJgqv138pqmIue') #Thai
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL6jk7-ujY14TgQzza2Tz9DL7CfaPMDvC2') #Spanish
		list.append('&youtube_id=zrsIpOZHuBo')
		
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLHRg_DI8OiY6GsdaIO6qTnlO7BBJlajDP') #Dutch
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PL7tHlGdGn8tgNocLA1u0rfj_vSn3PUqSS') #Portuguese
	addDir(addonString(10230).encode('utf-8'),list,17,thumb,addonString(102300).encode('utf-8'),'1',0,fanart)
	
	'''ג'רג מלך הג'ונגל'''
	thumb = 'https://www.thetvdb.com/banners/posters/81177-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/81177-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1909.jpg&mode=3&name=%d7%92%27%d7%95%d7%a8%d7%92%27%20%d7%9e%d7%9c%d7%9a%20%d7%94%d7%92%27%d7%95%d7%a0%d7%92%d7%9c%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1909&series_name=%d7%92%27%d7%95%d7%a8%d7%92%27%20%d7%9e%d7%9c%d7%9a%20%d7%94%d7%92%27%d7%95%d7%a0%d7%92%d7%9c%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1909%2fgeorge-of-the-jungle-%d7%92-%d7%95%d7%a8%d7%92-%d7%9e%d7%9c%d7%9a-%d7%94%d7%92-%d7%95%d7%a0%d7%92%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_ch=georgeofthejungle')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL8nZ8iRaXhPtLSc4lUlebFnJdGMlwhsxl')
		list.append('&youtube_pl=PLJPtmireMHHOChS-zR2GBlyiQ8RRK2b7a')
		
	addDir(addonString(10413).encode('utf-8'),list,17,thumb,addonString(104130).encode('utf-8'),'1',0,fanart)
	
	'''גבעת ווטרשיפ'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/77469-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/77469-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F77469-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F77469-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DWatership%20Down%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fwatership-down')
		
	addDir(addonString(10365).encode('utf-8'),list,6,thumb,addonString(103650).encode('utf-8'),'1',0,fanart)
	
	'''גברת פלפלת'''
	thumb = 'https://www.thetvdb.com/banners/posters/131361-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/131361-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/131361-3.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1314.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1314&series_name=%d7%92%d7%91%d7%a8%d7%aa%20%d7%a4%d7%9c%d7%a4%d7%9c%d7%aa%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%d7%99%d7%94%20%d7%a9%d7%9c%20%d7%92%d7%91%d7%a8%d7%aa%20%d7%a4%d7%9c%d7%a4%d7%9c%d7%aa%20%d7%94%d7%a7%d7%a9%d7%99%d7%a9%d7%94%20%d7%94%d7%a0%d7%97%d7%9e%d7%93%d7%94%20%d7%a9%d7%94%d7%9b%d7%a3%20%d7%94%d7%9e%d7%99%d7%95%d7%97%d7%93%20%d7%a9%d7%9c%d7%94%20%d7%99%d7%9b%d7%95%d7%9c%20%d7%9c%d7%9b%d7%95%d7%95%d7%a5%20%d7%90%d7%95%d7%aa%d7%94%20%d7%9c%d7%92%d7%95%d7%93%d7%9c%20%d7%90%d7%a6%d7%91%d7%a2%d7%95%d7%a0%d7%99.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1314%2flittle-mrs-pepperpot-%d7%92%d7%91%d7%a8%d7%aa-%d7%a4%d7%9c%d7%a4%d7%9c%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLkLrihhmnxYGoIg5xDLAR-hzpsvRgeabM')
	addDir(addonString(10414).encode('utf-8'),list,17,thumb,addonString(104140).encode('utf-8'),'1',0,fanart)
	
	'''ג'וני טסט'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/134991-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/134991-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F134991-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F134991-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DJohnny%20Test%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fjohnny-test')
		list.append('&youtube_ch=UCW6tWb2c7rCLDYIdfYCLW9Q')
	addDir(addonString(10375).encode('utf-8'),list,17,thumb,addonString(103750).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104D(General_LanguageL, background, background2) #ג'ימי ניוטרון
	CATEGORIES104I(General_LanguageL, background, background2) #דובוני אכפת לי
	
	'''Doraemon / דורימון'''
	thumb = 'https://www.thetvdb.com/banners/posters/75141-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75141-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL95CWWe9DuaJ6xtv1V8ZxDvoG_cB3z4bc')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2015-04-23doraemon-us-2014S.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D43853389a93dbcf030c79b161177de52b6409c05-1481270506-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Doraemon%20US%20(2014)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F1872%2Fdoraemon-us-2014%2F&name_=Season1&')
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2015-07-22doraemon-us-season-2-20152.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D43853389a93dbcf030c79b161177de52b6409c05-1481270506-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Doraemon%20US%20Season%202%20(2015)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F4724%2Fdoraemon-us-season-2-2015%2F&name_=Season2&')
	addDir(addonString(10415).encode('utf-8'),list,17,thumb,addonString(104150).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES104P(General_LanguageL, background, background2) #דיגימון
	CATEGORIES104W(General_LanguageL, background, background2) #Digimon Tamers
	CATEGORIES104Y(General_LanguageL, background, background2) #Digimon Fusion
	CATEGORIES104AA(General_LanguageL, background, background2) #Digimon Xros Wars
	CATEGORIES104AB(General_LanguageL, background, background2) #Digimon Universe: Appli Monsters
	CATEGORIES104AC(General_LanguageL, background, background2) #Digimon Adventure Tri
	
	'''דנבר הדינוזאור האחרון'''
	thumb = 'https://www.thetvdb.com/banners/posters/73737-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73737-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F68%2Fimage%2F555x418%2Fgreen-latern.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGreen%20Lantern%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fgreen-lantern-the-animated-series-full-episodes')
		list.append('&youtube_pl=PLWIkOi4pSkd8b3DGMHT5UkKZPZ_KzheUu')
		list.append('&youtube_pl=PLb1xghMkI5XmVJubEwR1WH6qq6QPOMXSz')
	
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL74D068B7A8C01DBB')
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLcFEa8vQIcKtU1VknkYflFnH7DjtBwaHt')
	
	if 'Italiano' in General_LanguageL:
		list.append('&youtube_pl=PL282B62C90158252C')
	
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLZsA2bTSVjpRV57QDRH25-HFKRG5HCWaZ')
	
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PL3EB7946A98ACC0CD')
		
		
	addDir(addonString(10426).encode('utf-8'),list,17,thumb,addonString(104260).encode('utf-8'),'1',"",fanart)
	
	'''דני שובבני'''
	thumb = 'https://www.thetvdb.com/banners/posters/76423-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76423-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f448.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=448&series_name=dennis-the-menace-%d7%93%d7%a0%d7%99-%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary=%d7%93%d7%a0%d7%99%20%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99%20%d7%94%d7%95%d7%90%20%d7%99%d7%9c%d7%93%20%d7%a9%d7%9c%d7%90%20%d7%9e%d7%a4%d7%a1%d7%99%d7%a7%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%a9%d7%98%d7%95%d7%99%d7%95%d7%aa%2c%20%d7%9c%d7%94%d7%a6%d7%99%d7%a7%20%d7%9c%d7%a9%d7%9b%d7%a0%d7%99%d7%9d%2c%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%a0%d7%96%d7%a7%d7%99%d7%9d%20%d7%95%d7%91%d7%a7%d7%99%d7%a6%d7%95%d7%a8%20%d7%9c%d7%94%d7%99%d7%95%d7%aa%20%d7%9b%d7%9e%d7%95%20%d7%9b%d7%9c%20%d7%99%d7%9c%d7%93%20%d7%91%d7%9f%20%d7%92%d7%99%d7%9c%d7%95.%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%9b%d7%9c%d7%91%d7%95%20%d7%94%d7%9e%d7%95%d7%a4%d7%a8%d7%a2%20%d7%91%d7%a9%d7%9d%20%d7%a8%d7%90%d7%a3%2c%20%d7%93%d7%a0%d7%99%20%d7%9e%d7%97%d7%95%d7%9c%d7%9c%20%d7%9e%d7%94%d7%95%d7%9e%d7%95%d7%aa%20%d7%91%d7%a9%d7%9b%d7%95%d7%a0%d7%94%2c%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%9b%d7%95%d7%95%d7%a0%d7%95%d7%aa%d7%99%d7%95%20%d7%94%d7%98%d7%95%d7%91%d7%95%d7%aa%2c%20%d7%94%d7%a8%d7%a6%d7%95%d7%9f%20%d7%94%d7%9e%d7%95%d7%98%d7%a2%d7%94%20%d7%9c%d7%a2%d7%96%d7%95%d7%a8%20%d7%95%d7%94%d7%a1%d7%a7%d7%a8%d7%a0%d7%95%d7%aa%20%d7%a9%d7%9c%d7%95%20%d7%a9%d7%90%d7%99%d7%a0%d7%94%20%d7%99%d7%95%d7%93%d7%a2%d7%aa%20%d7%a9%d7%95%d7%91%d7%a2%20%d7%9e%d7%95%d7%91%d7%99%d7%9c%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9c%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%95%d7%9b%d7%99%d7%95%d7%a4%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f448%2fdennis-the-menace-%d7%93%d7%a0%d7%99-%d7%a9%d7%95%d7%91%d7%91%d7%a0%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2548246')
		list.append('&youtube_pl=PL68ECBFC6278EB7BE') #Hebrew
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PL810CC2AF30CEFF13') #Serbian
	addDir(addonString(10417).encode('utf-8'),list,17,thumb,addonString(104170).encode('utf-8'),'1',"",fanart)
	
	'''דן דין השופט'''
	thumb = 'https://www.thetvdb.com/banners/posters/158531-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/158531-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/158531-5.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1009.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1009&series_name=%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%94%d7%a9%d7%95%d7%a4%d7%98%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%94%d7%95%d7%90%20%d7%a9%d7%95%d7%a4%d7%98%20%d7%97%d7%9b%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%a0%d7%a7%d7%a8%d7%90%20%d7%a2%22%d7%99%20%d7%94%d7%92%d7%9e%d7%93%d7%99%d7%9d%20%d7%91%d7%9b%d7%9c%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%a4%d7%aa%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%91%d7%a2%d7%99%d7%95%d7%aa%d7%99%d7%94%d7%9d.%20%d7%a0%d7%a2%d7%96%d7%a8%20%d7%91%d7%a2%d7%95%d7%96%d7%a8%d7%95%2c%20%d7%91%d7%99%d7%a0%d7%95%2c%20%d7%93%d7%9f%20%d7%93%d7%99%d7%9f%20%d7%a2%d7%a3%20%d7%9c%d7%9b%d7%9c%20%d7%9e%d7%a7%d7%95%d7%9d%20%d7%a2%d7%9c%20%d7%92%d7%91%d7%95%20%d7%a9%d7%9c%20%d7%98%d7%99%d7%9c%d7%99%20%d7%94%d7%91%d7%a8%d7%91%d7%95%d7%a8.%20%d7%94%d7%92%d7%9e%d7%93%d7%99%d7%9d%20%d7%a6%d7%a8%d7%99%d7%9b%d7%99%d7%9d%20%d7%9c%d7%94%d7%99%d7%96%d7%94%d7%a8%20%d7%9e%d7%94%d7%98%d7%a8%d7%95%d7%9c%d7%99%d7%9d%20%d7%94%d7%a8%d7%a2%d7%99%d7%9d%20%d7%a9%d7%9e%d7%aa%d7%a0%d7%9b%d7%9c%d7%99%d7%9d%20%d7%9c%d7%94%d7%9d%20%d7%91%d7%9b%d7%9c%20%d7%94%d7%96%d7%93%d7%9e%d7%a0%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1009%2fthe-wisdom-of-the-gnomes-%d7%93%d7%9f-%d7%93%d7%99%d7%9f-%d7%94%d7%a9%d7%95%d7%a4%d7%98-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	addDir(addonString(10418).encode('utf-8'),list,6,thumb,addonString(104180).encode('utf-8'),'1',0,fanart)	
	
	CATEGORIES104R(General_LanguageL, background, background2) #דראגון בול
	CATEGORIES104S(General_LanguageL, background, background2) #דראגון בול Z
	CATEGORIES104T(General_LanguageL, background, background2) #דראגון בול S
	CATEGORIES104U(General_LanguageL, background, background2) #דראגון בול GT
	CATEGORIES104V(General_LanguageL, background, background2) #דראגון בול K
	
	'''האגדה של קורה'''
	thumb = 'https://www.thetvdb.com/banners/posters/251085-15.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/251085-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&name_=Season 1&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F75%2Fimage%2F555x418%2Flegend-of-korra-book-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Legend%20of%20Korra%20Season%201%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-legend-of-korra-book-1')
		list.append('&name_=Season 2&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F76%2Fimage%2F555x418%2Flegend-of-korra-book-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Legend%20of%20Korra%20Season%202%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-legend-of-korra-book-2')
		list.append('&name_=Season 3&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F77%2Fimage%2F555x418%2Flegend-of-korra-book-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Legend%20of%20Korra%20Season%203%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-legend-of-korra-book-3')
		list.append('&name_=Season 4&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F78%2Fimage%2F555x418%2Flegend-of-korra-book-4.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Legend%20of%20Korra%20Season%204%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-legend-of-korra-book-4')
	addDir(addonString(10356).encode('utf-8'),list,6,thumb,addonString(103560).encode('utf-8'),'1',0,fanart)
	
	'''Maya the Bee / הדבורה מאיה'''
	thumb = 'https://www.thetvdb.com/banners/posters/73518-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73518-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f720.jpg&mode=3&name=%d7%93%d7%99%d7%92%27%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=720&series_name=%d7%93%d7%99%d7%92%27%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f720%2fdigimon-%d7%93%d7%99%d7%92-%d7%99%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLfcYs4SRZfuKJs0CL98BF0_OOGRWlmpdQ')
	addDir(addonString(10419).encode('utf-8'),list,17,thumb,addonString(104190).encode('utf-8'),'1',0,fanart)
	
	'''The Ultimate Book of Spells / הובוס ספר הקסמים הגדול'''
	thumb = 'https://www.thetvdb.com/banners/posters/77793-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77793-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1532.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1532&series_name=%d7%94%d7%95%d7%91%d7%95%d7%a1%20%d7%a1%d7%a4%d7%a8%20%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d%20%d7%94%d7%92%d7%93%d7%95%d7%9c%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9e%d7%92%d7%95%d7%9c%d7%9c%d7%aa%20%d7%90%d7%aa%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%9d%20%d7%a9%d7%9c%20%d7%a9%d7%9c%d7%95%d7%a9%d7%94%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%a9%d7%94%d7%95%d7%9c%d7%9b%d7%99%d7%9d%20%d7%9c%d7%9c%d7%9e%d7%95%d7%93%20%d7%91%d7%a4%d7%a0%d7%99%d7%9e%d7%99%d7%94%20%d7%9c%d7%a7%d7%95%d7%a1%d7%9e%d7%99%d7%9d%2c%20%d7%a9%d7%9d%20%d7%94%d7%9d%20%d7%9e%d7%a7%d7%91%d7%9c%d7%99%d7%9d%20%d7%9c%d7%99%d7%93%d7%99%d7%94%d7%9d%20%d7%90%d7%aa%20%d7%94%d7%95%d7%91%d7%95%d7%a1%2c%20%d7%a1%d7%a4%d7%a8%20%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d%20%d7%94%d7%92%d7%93%d7%95%d7%9c%2c%20%d7%90%d7%a9%d7%a8%20%d7%9c%d7%95%d7%a7%d7%97%20%d7%90%d7%95%d7%aa%d7%9d%20%d7%9c%d7%9e%d7%a2%d7%9e%d7%a7%d7%99%20%d7%94%d7%90%d7%93%d7%9e%d7%94%20%d7%95%d7%9e%d7%a1%d7%91%d7%99%d7%a8%20%d7%9c%d7%94%d7%9d%20%d7%a9%d7%a2%d7%9c%d7%99%d7%94%d7%9d%20%d7%9c%d7%94%d7%99%d7%9c%d7%97%d7%9d%20%d7%91%d7%96%d7%a8%d7%9c%d7%a7%2c%20%d7%a7%d7%95%d7%a1%d7%9d%20%d7%a2%d7%9c%d7%99%d7%95%d7%9f%20%d7%a9%d7%a0%d7%9b%d7%9c%d7%90%20%d7%91%d7%9e%d7%a2%d7%9e%d7%a7%d7%99%20%d7%94%d7%90%d7%93%d7%9e%d7%94%20%d7%a2%d7%9c-%d7%99%d7%93%d7%99%20%d7%9e%d7%95%d7%a2%d7%a6%d7%aa%20%d7%94%d7%a7%d7%95%d7%a1%d7%9e%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1532%2fthe-ultimate-book-of-spells-%d7%94%d7%95%d7%91%d7%95%d7%a1-%d7%a1%d7%a4%d7%a8-%d7%94%d7%a7%d7%a1%d7%9e%d7%99%d7%9d-%d7%94%d7%92%d7%93%d7%95%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=5VMJY095Bdw&list=PL4CFD7A57188E27EF') #English
	addDir(addonString(10420).encode('utf-8'),list,17,thumb,addonString(104200).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... Man / היה היה - האדם'''
	thumb = 'https://www.thetvdb.com/banners/posters/79849-19.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/79849-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%d7%94%d7%97%d7%99%d7%99%d7%9d&url=seriesId%3d2520985')
		list.append('&youtube_pl=PLPO4_vX2WeIV8QjNMKILbbGXwxY0H3jgZ')
		list.append('&youtube_pl=PL7sOvsxkL3kvJJKw4pKWvI1z3yxjmy2or')
		list.append('&youtube_pl=PLaKQk3jt0eydFOgVJq5z9VjANdEokSzwK')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLzxz9oRKpLXFchbBZ_tKZA9cWT2TYd_q_')
		
	addDir(addonString(10320).encode('utf-8'),list,17,thumb,addonString(103200).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... Life / היה היה - החיים'''
	thumb = 'https://www.thetvdb.com/banners/posters/79158-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/79158-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%D7%94%D7%99%D7%94+%D7%94%D7%99%D7%94+%D7%94%D7%97%D7%99%D7%99%D7%9D+%D7%A2%D7%95%D7%A0%D7%94+1&url=seriesId%3d2520994')
		list.append('&youtube_pl=PLXMxuZI8uq9KidUj9TVY3PHQlYbesoHoL')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL8D1D0E1DB8598123')
		
	addDir(addonString(10321).encode('utf-8'),list,17,thumb,addonString(103210).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... Space / היה היה - החלל'''
	thumb = 'https://www.thetvdb.com/banners/posters/81153-14.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/81153-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLKnJDcjkfEp2pEZ-MZ9vetcGnSrKUsOxa')
		list.append('&youtube_pl=PLKnJDcjkfEp2u2cdLowGr-hb1XLOqpFCS')
		
	addDir(addonString(10322).encode('utf-8'),list,17,thumb,addonString(103220).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... The Americas / היה היה - אמריקה'''
	thumb = 'https://www.thetvdb.com/banners/posters/81661-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/81661-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLKnJDcjkfEp0WhkE1ROjSp-96p9TO0WKN')
		
	addDir(addonString(10323).encode('utf-8'),list,17,thumb,addonString(103230).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... The Explorers / היה היה - היה היה - גילוי ארצות'''
	thumb = 'https://www.thetvdb.com/banners/posters/83005-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/83005-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94&url=seriesId%3d2520966')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94&url=seriesId%3d2520965')
		list.append('&youtube_pl=PLPO4_vX2WeIV8QjNMKILbbGXwxY0H3jgZ')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLKnJDcjkfEp1Nh-XSqK8ulP6Y9AKjd5UQ')
		
	addDir(addonString(10324).encode('utf-8'),list,17,thumb,addonString(103240).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... The Discoverers / היה היה - ממציאים'''
	thumb = 'https://www.thetvdb.com/banners/posters/82342-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82342-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2914073')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLKnJDcjkfEp1dW0x_OfvltJyZ9nwjttzL')
		
	addDir(addonString(10325).encode('utf-8'),list,17,thumb,addonString(103250).encode('utf-8'),'1',0,fanart)
	
	'''Once Upon a Time... Planet Earth / היה היה - כדור הארץ'''
	thumb = 'https://www.thetvdb.com/banners/posters/82342-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82342-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%94%d7%99%d7%94%20%d7%94%d7%99%d7%94%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5&url=seriesId%3d2521001')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLKnJDcjkfEp0u7ANUOXvxHB6g6OnDyvMb')
		
	addDir(addonString(10326).encode('utf-8'),list,17,thumb,addonString(103260).encode('utf-8'),'1',0,fanart)
	
	'''הדרדסים'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/75719-7.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/75719-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f236.jpg&mode=3&name=%d7%94%d7%93%d7%a8%d7%93%d7%a1%d7%99%d7%9d%20-%20%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=236&series_name=%d7%94%d7%93%d7%a8%d7%93%d7%a1%d7%99%d7%9d%20-%20%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f236%2fthe-smurfs-%d7%94%d7%93%d7%a8%d7%93%d7%a1%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&custom8=plugin://plugin.video.hotVOD.video/?mode=3&module=%2fCmn%2fApp%2fVideo%2fCmmAppVideoApi_AjaxItems%2f0%2c13776%2c&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7290%d7%99%d7%9d%20&url=http%3a%2f%2fhot.ynet.co.il%2fExt%2fComp%2fHot%2fTopSeriesPlayer_Hot%2fCdaTopSeriesPlayer_VidItems_Hot%2f0%2c13031%2cL-10842-525-0-0%2c00.html')
		list.append('&youtube_pl=PLo3vmw8N0knb9tZuIy7AR9fMPTUzr1oiI')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F75719-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F75719-7.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Smurfs%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-smurfs')
		list.append('&youtube_pl=PLaE8D0PEpUTtHl3NzB3VfscnmW68cZC58')
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLITCTw1CghePN4J1nA4hwRzKaxGhxlV4e')
	
	addDir(addonString(10422).encode('utf-8'),list,17,thumb,addonString(104220).encode('utf-8'),'1',0,fanart)

	'''Snorks / הזרבובים'''
	thumb = 'https://www.thetvdb.com/banners/posters/76305-6.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76305-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1313.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1313&series_name=%d7%94%d7%96%d7%a8%d7%91%d7%95%d7%91%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%96%d7%a8%d7%91%d7%95%d7%91%d7%99%d7%9d%20%d7%94%d7%9d%20%d7%99%d7%a6%d7%95%d7%a8%d7%99%d7%9d%20%d7%aa%d7%aa%20%d7%9e%d7%99%d7%9e%d7%99%d7%99%d7%9d%2c%20%d7%a2%d7%9c%d7%99%d7%96%d7%99%d7%9d%2c%20%d7%a1%d7%a1%d7%92%d7%95%d7%a0%d7%99%d7%99%d7%9d%2c%20%d7%a9%d7%9e%d7%a9%d7%aa%d7%9e%d7%a9%d7%99%d7%9d%20%d7%91%d7%a9%d7%a0%d7%95%d7%a8%d7%a7%d7%9c%20%d7%a9%d7%a2%d7%9c%20%d7%a8%d7%90%d7%a9%d7%9d%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%a0%d7%95%d7%a2%20%d7%91%d7%9e%d7%94%d7%99%d7%a8%d7%95%d7%aa%20%d7%91%d7%9e%d7%99%d7%9d%20%d7%95%d7%9b%d7%93%d7%99%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%9e%d7%95%d7%a1%d7%99%d7%a7%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1313%2fthe-snorks-%d7%94%d7%96%d7%a8%d7%91%d7%95%d7%91%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_id=1BgMQNYKatk') #Hebrew
		list.append('&youtube_pl=PLR7DTcU2p0QiY-wI8KC6f01uzKLDZcuAc') #Broken
	
	if 'English' in General_LanguageL:
		list.append('&youtube_id=SauxsOm11JE')
		list.append('&youtube_id=elZSpa0-5vI')
		list.append('&youtube_id=_ok40wUT4w4')
		
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PL87cYpQYTLNfDUqE2FbdU8lAiennUBQKU')
		list.append('&youtube_pl=PLUbANs2QiCwRoTM0-XfaBEh89H9Pc1j5n')
	
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_id=yqw88vSVjQE')
		
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLKwvqirafaPvscDtby0-s04w2eMQhM2ju')
		
	addDir(addonString(10423).encode('utf-8'),list,6,thumb,addonString(104230).encode('utf-8'),'1',0,fanart)
	
	'''החתולים הסמוראים'''
	thumb = 'https://www.thetvdb.com/banners/posters/77089-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77089-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLR7DTcU2p0QhPmznEmitRHkv5RcUG3E-s') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLS4APdRj5MZdhdNEmwWUcZL_Tx_skioQX') #English
	addDir(addonString(10424).encode('utf-8'),list,17,thumb,addonString(104240).encode('utf-8'),'1',0,fanart)
	
	'''סוכן חשאי: עכבר'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/300969-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/300969-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F300969-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F300969-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDanger%20Mouse%20(2015)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdanger-mouse-2015')
		
	addDir(addonString(10398).encode('utf-8'),list,6,thumb,addonString(103980).encode('utf-8'),'1',0,fanart)
	
	'''Fables of the Green Forest / סיפורי היער הירוק'''
	list = []
	thumb = 'https://www.thetvdb.com/banners/posters/263488-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/263488-1.jpg'
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLGnTTJWIWt4c29JQVtq4KGqIurcstibnt')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLmNp3u5r93jaT6gqMq8-hZqYoL2z5U9sY')
	
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PLo9BPxZp4fUeUK5lrAHqTDsaoLeoRMR6F')
	
	if 'Persian' in General_LanguageL:
		list.append('&youtube_pl=PLo9BPxZp4fUeUK5lrAHqTDsaoLeoRMR6F')
		
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLZ4POPAfakSGuNfFkFX3SvkrkOHVfDXNt')
		
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLKY9qcuiW3a2Hl3yeVPalp3tFKoHSXjvF')
		

	if 'Japanish' in General_LanguageL:
		list.append('&youtube_pl=PL47D11FE0DE4DAAA8')
		
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLqocpp7Qra0k7vJQAtsT_tlzJY-FuAFOh')
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLLNbiNjUM-8BMvNcsPSgmmKh12w02TWmg')


	addDir(addonString(10639).encode('utf-8'),list,17,thumb,addonString(106390).encode('utf-8'),'1',0,fanart)
	
	'''Heathcliff / היתקליף'''
	thumb = 'https://www.thetvdb.com/banners/posters/259517-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/259517-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2549973')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL3qYiMswhauCyACTWt3otYgpPxWitR8hf')
		list.append('&youtube_pl=PLAEyhCIv-X253BV8VQJ3agJSLCnTTVpLG')
	
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLWBDfHynTzdwgWWw1olAWXTlUeJKvRYpU')
		list.append('&youtube_pl=')	

	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=PLovF9Z5TJjw-oEbBB3iGcKEXpk5JDnsiO')
		list.append('&youtube_pl=')	
		
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLdLOL3PeA3mrqjMcLeAhjMYws7945WkXB')
		list.append('&youtube_pl=')
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLc6qwHwxvejYiJh5xbMlwu1It61HWgJSb')
		list.append('&youtube_pl=')
	
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PLt_luoZum2FHcglJhP9YzZumJeMhvUVer')
		list.append('&youtube_pl=')

	addDir(addonString(10626).encode('utf-8'),list,17,thumb,addonString(106260).encode('utf-8'),'1',0,fanart)
	
	'''3000 Leagues in Search of Mother / הלב'''
	thumb = 'https://www.thetvdb.com/banners/posters/122151-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/122151-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f745.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=745&series_name=%d7%94%d7%9c%d7%91%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%9e%d7%a8%d7%a7%d7%95%20%d7%94%d7%95%d7%90%20%d7%91%d7%9f%20%d7%9c%d7%9e%d7%a9%d7%a4%d7%97%d7%94%20%d7%a2%d7%a0%d7%99%d7%99%d7%94%20%d7%94%d7%97%d7%99%d7%94%20%d7%91%d7%92%d7%a0%d7%95%d7%90%d7%94%20%d7%a9%d7%91%d7%90%d7%99%d7%98%d7%9c%d7%99%d7%94.%20%d7%91%d7%a9%d7%9c%20%d7%94%d7%9e%d7%a6%d7%91%20%d7%94%d7%9b%d7%9c%d7%9b%d7%9c%d7%99%20%d7%94%d7%a7%d7%a9%d7%94%2c%20%d7%a0%d7%90%d7%9c%d7%a6%d7%aa%20%d7%90%d7%9e%d7%95%20%d7%a9%d7%9c%20%d7%9e%d7%a8%d7%a7%d7%95%20%d7%9c%d7%a0%d7%a1%d7%95%d7%a2%20%d7%9c%d7%90%d7%a8%d7%92%d7%a0%d7%98%d7%99%d7%a0%d7%94%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%a2%d7%96%d7%95%d7%a8%20%d7%91%d7%a4%d7%a8%d7%a0%d7%a1%d7%aa%20%d7%94%d7%9e%d7%a9%d7%a4%d7%97%d7%94.%20%d7%9e%d7%a8%d7%a7%d7%95%20%d7%94%d7%a7%d7%98%d7%9f%20%d7%90%d7%99%d7%a0%d7%95%20%d7%99%d7%9b%d7%95%d7%9c%20%d7%9c%d7%a2%d7%9e%d7%95%d7%93%20%d7%91%d7%92%d7%a2%d7%92%d7%95%d7%a2%d7%99%d7%9d%2c%20%d7%94%d7%95%d7%90%20%d7%9e%d7%aa%d7%92%d7%a0%d7%91%20%d7%9c%d7%a1%d7%a4%d7%99%d7%a0%d7%94%20%d7%95%d7%99%d7%95%d7%a6%d7%90%20%d7%9c%d7%97%d7%a4%d7%a9%20%d7%90%d7%97%d7%a8%20%d7%90%d7%9e%d7%95.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f745%2fmarco-%d7%94%d7%9c%d7%91-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL_8KXLhQVQMLx3W2W6YXTmaNHoPmlLl28')
	addDir(addonString(10425).encode('utf-8'),list,17,thumb,addonString(104250).encode('utf-8'),'1',0,fanart)
	
	'''Hello Kitty and Friends / הלו קיטי וחברים'''
	thumb = 'https://www.thetvdb.com/banners/posters/125211-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/125211-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1684.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1684&series_name=%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa-%d7%94%d7%9c%d7%95-%d7%a7%d7%99%d7%98%d7%99-%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-hello-kitty-and-friends%2fseason%2f1&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9e%d7%9c%d7%95%d7%95%d7%94%20%d7%90%d7%aa%20%d7%a7%d7%99%d7%98%d7%99%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%94%20%d7%94%d7%98%d7%95%d7%91%d7%99%d7%9d.%20%d7%94%d7%9d%20%d7%9c%d7%95%d7%9e%d7%93%d7%99%d7%9d%20%d7%a9%d7%99%d7%a2%d7%95%d7%a8%d7%99%d7%9d%20%d7%97%d7%a9%d7%95%d7%91%d7%99%d7%9d%20%d7%91%d7%9b%d7%99%d7%aa%d7%94%20%d7%95%d7%9e%d7%97%d7%95%d7%a6%d7%94%20%d7%9c%d7%94%20%d7%a2%d7%9c%20%d7%97%d7%91%d7%a8%d7%95%d7%aa%20%d7%95%d7%9e%d7%a4%d7%aa%d7%97%d7%99%d7%9d%20%d7%99%d7%97%d7%a1%d7%99%20%d7%97%d7%91%d7%a8%d7%95%d7%aa%20%d7%a2%d7%9d%20%d7%93%d7%9e%d7%95%d7%99%d7%95%d7%aa%20%d7%97%d7%93%d7%a9%d7%95%d7%aa.%20%d7%91%d7%9b%d7%9c%20%d7%9e%d7%a7%d7%95%d7%9d%20%d7%91%d7%95%20%d7%94%d7%9d%20%d7%a0%d7%9e%d7%a6%d7%90%d7%99%d7%9d%20%d7%94%d7%9d%20%d7%a0%d7%9e%d7%a6%d7%90%d7%99%d7%9d%20%d7%94%d7%9d%20%d7%9e%d7%92%d7%9c%d7%99%d7%9d%20%d7%a9%d7%97%d7%91%d7%a8%d7%95%d7%aa%20%d7%98%d7%95%d7%91%d7%94%20%d7%aa%d7%9e%d7%99%d7%93%20%d7%a2%d7%95%d7%96%d7%a8%d7%aa%20%d7%91%d7%9b%d7%9c%20%d7%a6%d7%a8%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1684%2f%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa-%d7%94%d7%9c%d7%95-%d7%a7%d7%99%d7%98%d7%99-%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-hello-kitty-and-friends%2fseason%2f1')
		pass
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL_li6wrWZhCA-MeGb1AR8BCsQLpzXkdqq') #English
	addDir(addonString(10721).encode('utf-8'),list,17,thumb,addonString(107210).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES104F(General_LanguageL, background, background2) #סדרות - הנוקמים: לוחמי העל
	
	'''Moomin / המומינים'''
	thumb = 'https://www.thetvdb.com/banners/posters/85199-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/85199-6.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f366.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=366&series_name=%d7%94%d7%9e%d7%95%d7%9e%d7%99%d7%a0%d7%99%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%9e%d7%95%d7%9e%d7%99%d7%a0%d7%99%d7%9d%20%d7%94%d7%9d%20%d7%99%d7%a6%d7%95%d7%a8%d7%99%d7%9d%20%d7%97%d7%91%d7%99%d7%91%d7%99%d7%9d%2c%20%d7%94%d7%92%d7%a8%d7%99%d7%9d%20%d7%91%d7%a2%d7%9e%d7%a7%20%d7%9e%d7%95%d7%a4%d7%9c%d7%90%20%d7%a9%d7%91%d7%9e%d7%9e%d7%9c%d7%9b%d7%aa%20%d7%a4%d7%a0%d7%98%d7%96%d7%99%d7%94.%20%d7%94%d7%9d%20%d7%9c%d7%91%d7%a0%d7%99%d7%9d%20%d7%95%d7%9e%d7%a8%d7%90%d7%9d%20%d7%9e%d7%96%d7%9b%d7%99%d7%a8%20%d7%9e%d7%a8%d7%90%d7%94%20%d7%a9%d7%9c%20%d7%94%d7%99%d7%a4%d7%95%d7%a4%d7%95%d7%98%d7%9d.%20%d7%94%d7%a6%d7%98%d7%a8%d7%a4%d7%95%20%d7%9c%d7%9e%d7%a9%d7%a4%d7%97%d7%aa%20%d7%9e%d7%95%d7%9e%d7%99%d7%9f%20%d7%95%d7%9c%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%d7%99%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f366%2fthe-moomins-%d7%94%d7%9e%d7%95%d7%9e%d7%99%d7%a0%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLofb-8yEl5BTeMeGHneOhJaETOrMWewPV')
		list.append('&youtube_pl=PL_8KXLhQVQMLvEJlwakyjEeFfOgGQKaCo')
		list.append('&youtube_pl=PL_8KXLhQVQMLB8AzFqkq5Tg7c_8ZX8RRb')
		list.append('&youtube_pl=PLN0EJVTzRDL-IJiTK4_B1ni8tlRNQvaBg')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLZs0gQed9tMS75zW8XwafIT_nRjYOg7Tn') #English
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=PL3Fa6uLkHmwYTX2ZNzgIk4nqCwgHjssH8') #	
		
	addDir(addonString(10427).encode('utf-8'),list,17,thumb,addonString(104270).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.licensing.biz/files/0%200moo1.jpg"))
	
	'''The Little Lulu Show / המופע של לולו'''
	thumb = 'https://www.thetvdb.com/banners/posters/70579-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70579-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f460.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=460&series_name=%d7%94%d7%9e%d7%95%d7%a4%d7%a2%20%d7%a9%d7%9c%20%d7%9c%d7%95%d7%9c%d7%95%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%20%d7%9e%d7%a1%d7%a4%d7%a8%d7%aa%20%d7%a2%d7%9c%20%d7%99%d7%9c%d7%93%d7%94%20%d7%a7%d7%98%d7%a0%d7%94%2c%20%d7%9e%d7%a6%d7%97%d7%99%d7%a7%d7%94%2c%20%d7%9e%d7%a9%d7%a2%d7%a9%d7%a2%d7%aa%20%d7%95%d7%a9%d7%95%d7%91%d7%91%d7%94%20%d7%91%d7%a9%d7%9d%20%d7%9c%d7%95%d7%9c%d7%95%20%d7%9e%d7%95%d7%a4%d7%98.%20%d7%9c%d7%95%d7%9c%d7%95%20%d7%91%d7%a2%d7%9c%d7%aa%20%d7%a9%d7%99%d7%a2%d7%a8%20%d7%90%d7%a8%d7%95%d7%9a%2c%20%d7%a9%d7%97%d7%95%d7%a8%20%d7%95%d7%9e%d7%aa%d7%95%d7%9c%d7%aa%d7%9c%20%d7%a9%d7%9c%d7%a8%d7%95%d7%91%20%d7%90%d7%a1%d7%95%d7%a3%20%d7%91%d7%a7%d7%95%d7%a7%d7%95%20%d7%92%d7%91%d7%95%d7%94%2c%20%d7%a2%d7%99%d7%a0%d7%99%d7%99%d7%9d%20%d7%a9%d7%97%d7%95%d7%a8%d7%95%d7%aa%20%d7%95%d7%aa%d7%9e%d7%99%d7%93%20%d7%9c%d7%95%d7%91%d7%a9%d7%aa%20%d7%a9%d7%9e%d7%9c%d7%94%20%d7%90%d7%93%d7%95%d7%9e%d7%94.%d7%91%d7%9e%d7%94%d7%9c%d7%9a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%a1%d7%95%d7%91%d7%91%d7%99%d7%9d%20%d7%90%d7%aa%20%d7%9c%d7%95%d7%9c%d7%95%20%d7%90%d7%a0%d7%a9%d7%99%d7%9d%20%d7%95%d7%9e%d7%9b%d7%a8%d7%99%d7%9d%20%d7%9b%d7%9e%d7%95%20%d7%90%d7%99%d7%9e%d7%94%20%d7%94%d7%93%d7%90%d7%92%d7%a0%d7%99%d7%aa%2c%20%d7%90%d7%91%d7%99%d7%94%20%d7%94%d7%a2%d7%a6%d7%9c%d7%9f%2c%20%d7%97%d7%91%d7%a8%d7%aa%d7%94%20%d7%94%d7%98%d7%95%d7%91%d7%94%20%d7%90%d7%a0%d7%a0%d7%99%2c%20%d7%97%d7%91%d7%a8%d7%94%20%d7%94%d7%98%d7%95%d7%91%20%d7%98%d7%95%d7%91%d7%99%2c%20%d7%94%d7%99%d7%9c%d7%93%20%d7%94%d7%a2%d7%a9%d7%99%d7%a8%20%d7%95%d7%95%d7%99%d7%9c%d7%91%d7%a8%2c%20%d7%90%d7%95%d7%99%d7%91%d7%aa%d7%94%20%d7%94%d7%9e%d7%95%d7%a9%d7%91%d7%a2%d7%aa%20%d7%95%d7%94%d7%99%d7%a4%d7%94%20%d7%92%d7%9c%d7%95%d7%a8%d7%99%d7%94%2c%20%d7%90%d7%94%d7%95%d7%91%d7%94%20%d7%a9%d7%9c%20%d7%92%d7%9c%d7%95%d7%a8%d7%99%d7%94%2c%20%d7%95%d7%90%d7%95%d7%99%d7%91%d7%94%20%d7%a9%d7%9c%20%d7%9c%d7%95%d7%9c%d7%95%20%d7%a0%d7%99%d7%a7%d7%95%d7%9c%d7%a1.%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%20%d7%9e%d7%97%d7%95%d7%9c%d7%a7%d7%aa%20%d7%9c-2%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%d7%9d%20%d7%9c%d7%9b%d7%9c%20%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%2c%20%d7%96%d7%9e%d7%9f%20%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%20%d7%94%d7%95%d7%90%20%d7%9b%d7%97%d7%a6%d7%99%20%d7%a9%d7%a2%d7%94%20%d7%95%d7%9b%d7%9c%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%20%d7%94%d7%95%d7%90%20%d7%9b%d7%a8%d7%91%d7%a2%20%d7%a9%d7%a2%d7%94.%20%d7%91%d7%9b%d7%9c%20%d7%aa%d7%97%d7%99%d7%9c%d7%aa%20%d7%90%d7%95%20%d7%a1%d7%99%d7%95%d7%9d%20%d7%a7%d7%98%d7%a2%20%d7%9c%d7%95%d7%9c%d7%95%20%d7%9e%d7%a6%d7%99%d7%92%d7%94%20%d7%9e%d7%95%d7%a4%d7%a2%20%d7%a1%d7%98%d7%a0%d7%93%d7%90%d7%a4%20%d7%a9%d7%91%d7%95%20%d7%94%d7%99%d7%90%20%d7%9e%d7%aa%d7%91%d7%93%d7%97%d7%aa%20%d7%a2%d7%9c%20%d7%97%d7%a9%d7%91%d7%95%d7%9f%20%d7%97%d7%91%d7%a8%d7%99%d7%94%20%d7%95%d7%a2%d7%9c%20%d7%94%d7%9e%d7%a7%d7%a8%d7%94%20%d7%a9%d7%a7%d7%a8%d7%94%20%d7%91%d7%90%d7%95%d7%aa%d7%95%20%d7%94%d7%a4%d7%a8%d7%a7.%20%d7%91%d7%a0%d7%95%d7%a1%d7%a3%20%d7%99%d7%a9%d7%a0%d7%9d%20%d7%a1%d7%a8%d7%98%d7%95%d7%a0%d7%99-%d7%91%d7%99%d7%a0%d7%99%d7%99%d7%9d%20%d7%a7%d7%a6%d7%a8%d7%99%d7%9d%20%d7%9c%d7%9c%d7%90%20%d7%93%d7%99%d7%91%d7%95%d7%a8.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f460%2fthe-little-lulu-show-%d7%94%d7%9e%d7%95%d7%a4%d7%a2-%d7%a9%d7%9c-%d7%9c%d7%95%d7%9c%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLVH181b17p3ZfXPIemTyuQInMBUaf6bXH')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL9Tf3rDOT4eW8jTFyBzZd4f9y4lix95Td') #English
	addDir(addonString(10428).encode('utf-8'),list,17,thumb,addonString(104280).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://orig01.deviantart.net/efcd/f/2013/070/c/b/lulu_loves_tubby_by_re_ed-d5xrhne.jpg"))
	
	'''The Little Flying Bears / המעופפים הנועזים'''
	thumb = 'https://www.thetvdb.com/banners/posters/249322-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/249322-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/249322-3.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1387.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1387&series_name=%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a4%d7%99%d7%9d%20%d7%94%d7%a0%d7%95%d7%a2%d7%96%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%93%d7%95%d7%91%d7%99%d7%9d%20%d7%a7%d7%98%d7%a0%d7%99%d7%9d%20%d7%a2%d7%9d%20%d7%9b%d7%a0%d7%a4%d7%99%d7%99%d7%9d%20%d7%a9%d7%95%d7%9e%d7%a8%d7%99%d7%9d%20%d7%a2%d7%9c%20%d7%94%d7%99%d7%a2%d7%a8%20%d7%95%d7%94%d7%a1%d7%91%d7%99%d7%91%d7%94%20%d7%9e%d7%a4%d7%a0%d7%99%20%d7%96%d7%95%d7%92%20%d7%a9%d7%95%d7%a2%d7%9c%d7%99%d7%9d%20%d7%a2%d7%a8%d7%9e%d7%95%d7%9e%d7%99%d7%99%d7%9d%20%d7%95%d7%90%d7%a1%d7%95%d7%a0%d7%95%d7%aa%20%d7%98%d7%91%d7%a2%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1387%2fthe-little-flying-bears-%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a4%d7%99%d7%9d-%d7%94%d7%a0%d7%95%d7%a2%d7%96%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLR7DTcU2p0QhYwFJuI0zFXFmAN-q6n4A0')
		list.append('&youtube_pl=PL_8KXLhQVQMLhguXwe-d2HjvficZsfbEj')
		
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=PLHbwPevLSfBRPuKWOrtxYDPlbIntcfviv') #Slovak
		
	if 'Croatian' in General_LanguageL:
		list.append('&youtube_pl=PL741A6F9BEA016A4E') #Croatian
		
	addDir(addonString(10430).encode('utf-8'),list,17,thumb,addonString(104300).encode('utf-8'),'1',0,fanart)
	
	'''Princess Sissi / הנסיכה סיסי'''
	thumb = 'https://www.thetvdb.com/banners/posters/76939-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76939-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyGMBieogtC7uVwJr07JNIwL')
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=PLB7F61D166BE8DCFB')
	if 'Italiano' in General_LanguageL:
		list.append('&youtube_pl=PLA283C960B1F4F3C0')
		list.append('&youtube_pl=PLIsDVmWmkg9F3HM8EgHEXR8KWCjZXpFH1')
		list.append('&youtube_pl=PLA283C960B1F4F3C0')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLU29Q4rBWGxGc7EMZ6-3Fawe4_n_QCp50')
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=PLB7F61D166BE8DCFB')
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=PLB7F61D166BE8DCFB')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLPZ1XC7N-0RUAtKzH6N987SwNqcp5W2XG')
	addDir(addonString(10492).encode('utf-8'),list,17,thumb,addonString(104920).encode('utf-8'),'1',0,fanart)
	
	'''The Incredible Hulk / הענק הירוק'''
	thumb = 'https://www.thetvdb.com/banners/posters/77155-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77155-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1738.jpg&mode=3&name=%d7%94%d7%a2%d7%a0%d7%a7%20%d7%94%d7%99%d7%a8%d7%95%d7%a7%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1738&series_name=%d7%94%d7%a2%d7%a0%d7%a7%20%d7%94%d7%99%d7%a8%d7%95%d7%a7%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1738%2fthe-incredible-hulk-%d7%94%d7%a2%d7%a0%d7%a7-%d7%94%d7%99%d7%a8%d7%95%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL5884348CE48B25A6')
	addDir(addonString(10432).encode('utf-8'),list,17,thumb,addonString(104320).encode('utf-8'),'1',0,fanart)
	
	'''The Wonderful Wizard of Oz / הקוסם מארץ עוץ'''
	thumb = 'https://www.thetvdb.com/banners/posters/83855-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/83855-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1078.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1078&series_name=%d7%94%d7%a7%d7%95%d7%a1%d7%9d%20%d7%9e%d7%90%d7%a8%d7%a5%20%d7%a2%d7%95%d7%a5%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%94%20%d7%99%d7%a4%d7%a0%d7%99%d7%aa%20%d7%94%d7%9e%d7%91%d7%95%d7%a1%d7%a1%d7%aa%20%d7%a2%d7%9c%20%d7%90%d7%a8%d7%91%d7%a2%d7%94%20%d7%9e%d7%a1%d7%93%d7%a8%d7%aa%20%d7%a1%d7%a4%d7%a8%d7%99%20%d7%a2%d7%95%d7%a5%20%d7%94%d7%9e%d7%a7%d7%95%d7%a8%d7%99%d7%99%d7%9d%20%d7%9e%d7%90%d7%aa%20%d7%9c%d7%99%d7%99%d7%9e%d7%9f%20%d7%a4%d7%a8%d7%a0%d7%a7%20%d7%91%d7%90%d7%95%d7%9d%20%d7%95%d7%9e%d7%a8%d7%97%d7%99%d7%91%d7%94%20%d7%9e%d7%a2%d7%91%d7%a8%20%d7%9c%d7%a1%d7%99%d7%a4%d7%95%d7%a8%20%d7%94%d7%9e%d7%a7%d7%95%d7%a8%d7%99%20%d7%9b%d7%95%d7%9c%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%94%d7%aa%d7%a8%d7%97%d7%a9%d7%95%d7%99%d7%95%d7%aa%20%d7%90%d7%a9%d7%a8%20%d7%a7%d7%a8%d7%95%20%d7%9c%d7%90%d7%97%d7%a8%20%d7%a9%d7%93%d7%95%d7%a8%d7%95%d7%aa%d7%99%20%d7%a2%d7%96%d7%91%d7%94%20%d7%90%d7%aa%20%d7%90%d7%a8%d7%a5%20%d7%a2%d7%95%d7%a5.%20&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1078%2fthe-wonderful-wizard-of-oz-%d7%94%d7%a7%d7%95%d7%a1%d7%9d-%d7%9e%d7%90%d7%a8%d7%a5-%d7%a2%d7%95%d7%a5-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLrm9dDLqwrHnZF86MMTIb-Q3LSKLGLTDQ')
		list.append('&youtube_pl=PL6cgUTK_W5ypfpul22dpMBSSOrya57p-X')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLS3SOlSTtJcDe-vQ-T46r_cB1U_ENAuKF') #English
		list.append('&youtube_pl=PLEUj0OPG9zo6opg5r3HH-78KWAw6FRw87') #English
	addDir(addonString(10431).encode('utf-8'),list,17,thumb,addonString(104310).encode('utf-8'),'1',0,fanart)
	
	'''הרפתקאות החתול במגפיים'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/290174-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/290174-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F290174-4.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F290174-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Adventures%20Of%20Puss%20In%20Boots%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-adventures-of-puss-in-boots')
	if 'Dutch' in General_LanguageL:
		pass
	
	addDir(addonString(10496).encode('utf-8'),list,6,thumb,addonString(104960).encode('utf-8'),'1',0,fanart)
	
	'''The Pink Panther / הפנתר הורוד'''
	thumb = 'https://www.thetvdb.com/banners/posters/71554-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/71554-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1347.jpg&mode=3&name=%d7%94%d7%a4%d7%a0%d7%aa%d7%a8%20%d7%94%d7%95%d7%95%d7%a8%d7%95%d7%93%20%2a%d7%90%d7%99%d7%9c%d7%9d%2a&series_id=1347&series_name=%d7%94%d7%a4%d7%a0%d7%aa%d7%a8%20%d7%94%d7%95%d7%95%d7%a8%d7%95%d7%93%20%2a%d7%90%d7%99%d7%9c%d7%9d%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1347%2fthe-pink-panther-cartoons-%d7%94%d7%a4%d7%a0%d7%aa%d7%a8-%d7%94%d7%95%d7%95%d7%a8%d7%95%d7%93-%d7%90%d7%99%d7%9c%d7%9d')
	list.append('&youtube_ch=PinkPanthersShow')
	list.append('&youtube_pl=PL6cOKIs-_ungXuX1X2Phr1EZegne4nk-h')
	list.append('&youtube_pl=PL459EEABC17B35E51')
	addDir(addonString(10433).encode('utf-8'),list,17,thumb,addonString(104330).encode('utf-8'),'1',0,fanart)
	
	'''The Penguins of Madagascar / הפינגווינים ממדגסקר'''
	thumb = 'https://www.thetvdb.com/banners/posters/85075-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/85075-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f416.jpg&mode=3&name=%d7%94%d7%a4%d7%99%d7%a0%d7%92%d7%95%d7%95%d7%99%d7%a0%d7%99%d7%9d%20%d7%9e%d7%9e%d7%93%d7%92%d7%a1%d7%a7%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=416&series_name=%d7%94%d7%a4%d7%99%d7%a0%d7%92%d7%95%d7%95%d7%99%d7%a0%d7%99%d7%9d%20%d7%9e%d7%9e%d7%93%d7%92%d7%a1%d7%a7%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f416%2fthe-penguins-of-madagascar-%d7%94%d7%a4%d7%99%d7%a0%d7%92%d7%95%d7%95%d7%99%d7%a0%d7%99%d7%9d-%d7%9e%d7%9e%d7%93%d7%92%d7%a1%d7%a7%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLoAFYXAZNpvo-8i3MUajyo4vFDKGHmuWq') #English
	addDir(addonString(10435).encode('utf-8'),list,17,thumb,addonString(104350).encode('utf-8'),'1',"",fanart)
	
	'''הרוזן דאקולה'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/76307-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/76307-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76307-4.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F76307-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DCount%20Duckula%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fcount-duckula')
	addDir(addonString(10382).encode('utf-8'),list,6,thumb,addonString(103820).encode('utf-8'),'1',"",fanart)
	
	'''הרקולס'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/72163-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/72163-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72163-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72163-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDisney%92s%20Hercules%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdisneys-hercules')
	addDir(addonString(10381).encode('utf-8'),list,6,thumb,addonString(103810).encode('utf-8'),'1',"",fanart)
	
	'''Axe Cop / השוטר גרזן'''
	thumb = 'https://www.thetvdb.com/banners/posters/268186-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/268186-6.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f589.jpg&mode=3&name=%d7%94%d7%a9%d7%95%d7%98%d7%a8%20%d7%92%d7%a8%d7%96%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=589&series_name=%d7%94%d7%a9%d7%95%d7%98%d7%a8%20%d7%92%d7%a8%d7%96%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f589%2faxe-cop-%d7%94%d7%a9%d7%95%d7%98%d7%a8-%d7%92%d7%a8%d7%96%d7%9f-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLouuoG3C0vOBFIK7bFajnhA06ToGxa4VE') #English
	addDir(addonString(10436).encode('utf-8'),list,17,thumb,addonString(104360).encode('utf-8'),'1',"",fanart)
	
	'''וואן-פאנץ' מאן'''
	thumb = 'https://www.thetvdb.com/banners/posters/293088-6.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/293088-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F88%2Fimage%2F555x418%2FOne-Punch-Man.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DOne-Punch%20Man%20(TV%20Series)%20Dub%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fone-punch-man-full-episodes')
		
	addDir(addonString(10363).encode('utf-8'),list,6,thumb,addonString(103630).encode('utf-8'),'1',0,fanart)
	
	'''Wolverine and the X-Men / וולברין והאקס מן'''
	thumb = 'https://www.thetvdb.com/banners/posters/82870-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82870-7.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1578.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1578&series_name=%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f%20%d7%95%d7%94%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a9%d7%a0%d7%94%20%d7%90%d7%97%d7%a8%d7%99%20%d7%a4%d7%99%d7%a6%d7%95%d7%a5%20%d7%9e%d7%a1%d7%aa%d7%95%d7%a8%d7%99%20%d7%91%d7%91%d7%99%d7%aa%20%d7%94%d7%a1%d7%a4%d7%a8%20%d7%9c%d7%9e%d7%95%d7%98%d7%a0%d7%98%d7%99%d7%9d%20%d7%9c%d7%95%d7%92%d7%9f%20%d7%9e%d7%aa%d7%a2%d7%9e%d7%aa%20%d7%a9%d7%95%d7%91%20%d7%9e%d7%95%d7%9c%20%d7%9e%d7%95%d7%a1%20%d7%a9%d7%9e%d7%9b%d7%a0%d7%99%d7%a1%20%d7%9c%d7%9b%d7%9c%d7%90%20%d7%9e%d7%a9%d7%a4%d7%97%d7%94%20%d7%a9%d7%94%d7%97%d7%91%d7%99%d7%90%d7%94%20%d7%90%d7%aa%20%d7%9c%d7%95%d7%92%d7%9f.%20%d7%94%d7%90%d7%a0%d7%a7%20%d7%9e%d7%a0%d7%a1%d7%94%20%d7%9c%d7%a4%d7%a2%d7%a0%d7%97%20%d7%90%d7%aa%20%d7%94%d7%a4%d7%99%d7%a6%d7%95%d7%a5%20%d7%91%d7%91%d7%99%d7%94%22%d7%a1%20%d7%95%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%9c%d7%95%d7%92%d7%9f%20%d7%9e%d7%aa%d7%9b%d7%95%d7%a0%d7%9f%20%d7%9c%d7%9e%d7%9c%d7%97%d7%9e%d7%94%20%d7%94%d7%a7%d7%a8%d7%95%d7%91%d7%94.%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f%20%d7%95%d7%90%d7%a7%d7%a1%20%d7%9e%d7%9f%20-%20%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f%20%d7%9e%d7%90%d7%97%d7%93%20%d7%90%d7%aa%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%90%d7%a7%d7%a1%20%d7%9e%d7%9f-%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%9e%d7%95%d7%98%d7%a0%d7%98%d7%99%d7%9d%20%d7%a8%d7%95%d7%93%d7%a4%d7%99%20%d7%94%d7%a9%d7%9c%d7%95%d7%9d.%20%d7%94%d7%a6%d7%95%d7%95%d7%aa%20%d7%9e%d7%aa%d7%9e%d7%95%d7%93%d7%93%20%d7%92%d7%9d%20%d7%9e%d7%95%d7%9c%20%d7%90%d7%95%d7%99%d7%91%d7%99%d7%9d%20%d7%9e%d7%95%d7%98%d7%a0%d7%98%d7%99%d7%9d%20%d7%91%d7%94%d7%a0%d7%94%d7%92%d7%aa%d7%95%20%d7%a9%d7%9c%20%d7%9e%d7%92%d7%a0%d7%98%d7%95%2c%20%d7%95%d7%92%d7%9d%20%d7%9e%d7%95%d7%9c%20%d7%91%d7%a0%d7%99%20%d7%90%d7%93%d7%9d%2c%20%d7%91%d7%a4%d7%99%d7%a7%d7%95%d7%93%d7%95%20%d7%a9%d7%9c%20%d7%94%d7%a1%d7%a0%d7%90%d7%98%d7%95%d7%a8%20%d7%a7%d7%9c%d7%99%2c%20%d7%95%d7%9e%d7%a0%d7%a1%d7%94%20%d7%9c%d7%9e%d7%a0%d7%95%d7%a2%20%d7%9e%d7%9c%d7%97%d7%9e%d7%94%20%d7%91%d7%99%d7%9f%20%d7%91%d7%a0%d7%99%20%d7%94%d7%90%d7%93%d7%9d%20%d7%9c%d7%9e%d7%95%d7%98%d7%a0%d7%98%d7%99%d7%9d%20%d7%a9%d7%aa%d7%91%d7%99%d7%90%20%d7%9c%d7%94%d7%a8%d7%a1%20%d7%a2%d7%95%d7%9c%d7%9e%d7%99%2f&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1578%2fwolverine-and-the-x-men-%d7%95%d7%95%d7%9c%d7%91%d7%a8%d7%99%d7%9f-%d7%95%d7%94%d7%90%d7%a7%d7%a1-%d7%9e%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLR7DTcU2p0QhGsv3LuA3GnCJWjoPBCafl') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL5BE97D3FB689E48E') #English
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLB90059899E3B7CD0') #Portuguese
		list.append('&youtube_pl=PLzbICfFWEQ6frJukA5mzLSlpJbIARy37f') #Portuguese
	addDir(addonString(10437).encode('utf-8'),list,17,thumb,addonString(104370).encode('utf-8'),'1',"",fanart)
	
	'''Invader ZIM / זים הפולש'''
	thumb = 'https://www.thetvdb.com/banners/posters/75545-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75545-9.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F58%2Fimage%2F555x418%2Finvader-zim-featured.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DInvader%20ZIM%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Finvader-zim-tv-series-2001-2004')
		
	addDir(addonString(10344).encode('utf-8'),list,6,thumb,addonString(103440).encode('utf-8'),'1',0,fanart)
	
	'''Bosco Adventure / חבורת הצב המעופף'''
	thumb = 'https://www.thetvdb.com/banners/posters/251801-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/251801-5.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/251801-2.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1050.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1050&series_name=%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%94%d7%a6%d7%91%20%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a3%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%90%d7%a8%d7%a5%20%d7%94%d7%9e%d7%a2%d7%99%d7%99%d7%a0%d7%95%d7%aa%20%d7%a0%d7%9b%d7%91%d7%a9%d7%aa%20%d7%91%d7%99%d7%93%d7%99%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%20%d7%94%d7%a8%d7%a9%d7%a2%20%d7%a9%d7%9c%20%d7%9e%d7%a4%d7%9c%d7%a6%d7%aa%20%d7%91%d7%a9%d7%9d%20%d7%a1%d7%a7%d7%95%d7%a8%d7%a4%d7%99%d7%95%d7%9f%20%d7%9c%d7%a4%d7%a0%d7%99%20%d7%9c%d7%99%d7%a7%d7%95%d7%99%20%d7%94%d7%97%d7%9e%d7%94%20%d7%94%d7%9e%d7%9c%d7%90%20%d7%94%d7%9e%d7%aa%d7%a7%d7%a8%d7%91.%20%d7%a2%d7%9c%20%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94%20%d7%9c%d7%99%d7%a7%d7%99%2c%20%d7%9c%d7%94%d7%a6%d7%9c%d7%99%d7%97%20%d7%9c%d7%97%d7%96%d7%95%d7%a8%20%d7%9c%d7%90%d7%a8%d7%a5%20%d7%94%d7%9e%d7%a2%d7%99%d7%99%d7%a0%d7%95%d7%aa%20%d7%95%d7%9c%d7%a9%d7%91%d7%aa%20%d7%a2%d7%9c%20%d7%9b%d7%a1%20%d7%94%d7%9e%d7%9c%d7%9b%d7%95%d7%aa%20%d7%91%d7%98%d7%a8%d7%9d%20%d7%9c%d7%99%d7%a7%d7%95%d7%99%20%d7%94%d7%97%d7%9e%d7%94%20%d7%99%d7%aa%d7%a8%d7%97%d7%a9.%20%d7%a8%d7%a7%20%d7%9b%d7%9a%20%d7%94%d7%99%d7%90%20%d7%aa%d7%a9%d7%97%d7%a8%d7%a8%20%d7%9b%d7%95%d7%97%20%d7%a2%d7%a6%d7%95%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%99%d7%94%d7%a8%d7%95%d7%a1%20%d7%90%d7%aa%20%d7%94%d7%9b%d7%95%d7%91%d7%a9%d7%99%d7%9d.%20%d7%a2%d7%9c%20%d7%9e%d7%a0%d7%aa%20%d7%9c%d7%9e%d7%a0%d7%95%d7%a2%20%d7%9e%d7%9e%d7%a0%d7%94%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%9b%d7%9f%2c%20%d7%94%d7%99%d7%90%20%d7%a0%d7%97%d7%98%d7%a4%d7%94%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%a8%d7%a9%d7%a2%d7%99%d7%9d%20%d7%91%d7%a1%d7%a4%d7%99%d7%a0%d7%94%20%d7%94%d7%a0%d7%a7%d7%a8%d7%90%d7%aa%20%22%d7%94%d7%a2%d7%a7%d7%a8%d7%91%22.%20%d7%a7%d7%91%d7%95%d7%a6%d7%aa%20%d7%97%d7%99%d7%95%d7%aa%20%d7%9e%d7%99%d7%a2%d7%a8%20%d7%91%d7%95%d7%a1%d7%a7%d7%95%20%d7%99%d7%95%d7%a6%d7%90%d7%95%d7%aa%20%d7%9c%d7%94%d7%a9%d7%99%d7%91%20%d7%90%d7%aa%20%d7%9c%d7%99%d7%a7%d7%99%20%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94%20%d7%9c%d7%90%d7%a8%d7%a5%20%d7%94%d7%9e%d7%a2%d7%99%d7%99%d7%a0%d7%95%d7%aa%20%d7%91%d7%9e%d7%a1%d7%a2%20%d7%91%d7%91%d7%9c%d7%95%d7%9f%20%d7%9e%d7%a2%d7%95%d7%a4%d7%a3%20%d7%91%d7%a6%d7%95%d7%a8%d7%aa%20%d7%a6%d7%91.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1050%2fbosco-adventure-%d7%97%d7%91%d7%95%d7%a8%d7%aa-%d7%94%d7%a6%d7%91-%d7%94%d7%9e%d7%a2%d7%95%d7%a4%d7%a3-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_id=IkzdDqeR7kQ')
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=PLHPshmrm2yZYGLnm5_DjUEDhovX0dJ85Z') #Ukrainian
	addDir(addonString(10438).encode('utf-8'),list,6,thumb,addonString(104380).encode('utf-8'),'1',"",fanart)
	
	'''Back at the Barnyard / חברים בחווה'''
	thumb = 'https://www.thetvdb.com/banners/posters/119061-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/119061-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f1%e5%f4%f8%20%f9%e8%e5%fa%f0%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2662395')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f646.jpg&mode=3&name=%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%91%d7%97%d7%95%d7%95%d7%94%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=646&series_name=%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%91%d7%97%d7%95%d7%95%d7%94%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f646%2fback-at-the-barnyard-%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%91%d7%97%d7%95%d7%95%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLYQo3vRiiRc4YxLzsXZV2dT7IGP3MF-N7')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLCnZ4jf66RYIuf5W_ZLYsgNYLaCr4nAs4') #English
	addDir(addonString(10439).encode('utf-8'),list,17,thumb,addonString(104390).encode('utf-8'),'1',0,fanart)	
	
	'''Inspector Gadget / חוש חש הבלש'''
	thumb = 'https://www.thetvdb.com/banners/posters/73693-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73693-6.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = ''
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1397.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1397&series_name=%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%20%d7%94%d7%91%d7%9c%d7%a9%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%a7%d7%95%d7%9e%d7%99%d7%aa%2c%20%22%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%22%20%d7%94%d7%95%d7%90%20%d7%91%d7%9c%d7%a9%20%d7%9e%d7%a4%d7%95%d7%96%d7%a8%2c%20%d7%9e%d7%92%d7%95%d7%a9%d7%9d%20%d7%95%d7%9c%d7%90%20%d7%99%d7%95%d7%a6%d7%9c%d7%97%20%d7%a9%d7%91%d7%92%d7%95%d7%a4%d7%95%20%d7%94%d7%95%d7%a9%d7%aa%d7%9c%d7%95%20%d7%90%d7%99%d7%91%d7%a8%d7%99%d7%9d%20%d7%91%d7%99%d7%95%d7%a0%d7%99%d7%99%d7%9d%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%a7%d7%a0%d7%99%d7%9d%20%d7%9c%d7%95%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%20%d7%a2%d7%9c%20%d7%98%d7%91%d7%a2%d7%99%d7%99%d7%9d.%20%d7%90%d7%95%d7%99%d7%91%d7%95%20%d7%94%d7%a2%d7%99%d7%a7%d7%a8%d7%99%20%d7%94%d7%95%d7%90%20%d7%93%d7%95%d7%a7%d7%98%d7%95%d7%a8%20%d7%a8%d7%a9%d7%a2%20%d7%95%d7%9e%d7%a1%d7%aa%d7%95%d7%a8%d7%99%2c%20%d7%9e%d7%a0%d7%94%d7%99%d7%92%20%d7%90%d7%a8%d7%92%d7%95%d7%9f%20%d7%a4%d7%a9%d7%a2.%20%d7%9c%d7%97%d7%95%d7%a9%20%d7%97%d7%a9%20%d7%a2%d7%95%d7%96%d7%a8%d7%99%d7%9d%20%d7%90%d7%97%d7%99%d7%99%d7%a0%d7%99%d7%aa%d7%95%20%d7%a7%d7%a8%d7%9f%20%d7%95%d7%9b%d7%9c%d7%91%d7%94%20%d7%94%d7%97%d7%9b%d7%9d%20%22%d7%9e%d7%95%d7%97%22%2c%20%d7%9b%d7%9e%d7%95%20%d7%92%d7%9d%20%d7%a9%d7%a0%d7%99%20%d7%94%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%99%d7%9d%20%d7%a4%d7%99%d7%93%d7%92%27%d7%98%20%d7%95%d7%93%d7%99%d7%92%27%d7%98%20%d7%94%d7%9e%d7%9b%d7%95%d7%a0%d7%99%d7%9d%20%22%d7%94%d7%97%d7%95%d7%a9%d7%97%d7%a9%d7%99%d7%9d%22.%20%d7%94%d7%9d%20%d7%9e%d7%a6%d7%99%d7%9c%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9e%d7%a1%d7%9b%d7%a0%d7%95%d7%aa%20%d7%95%d7%9e%d7%9b%d7%95%d7%95%d7%a0%d7%99%d7%9d%20%d7%90%d7%95%d7%aa%d7%95%20%d7%9c%d7%a1%d7%99%d7%9b%d7%95%d7%9c%20%d7%94%d7%a4%d7%a9%d7%a2%20%d7%9e%d7%91%d7%9c%d7%99%20%d7%a9%d7%94%d7%95%d7%90%20%d7%9e%d7%95%d7%93%d7%a2%20%d7%9c%d7%9b%d7%9a%20%d7%91%d7%9b%d7%9c%d7%9c.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1397%2finspector-gadget-%d7%97%d7%95%d7%a9-%d7%97%d7%a9-%d7%94%d7%91%d7%9c%d7%a9-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2555838')
		list.append('&youtube_pl=PLcnOogeoQ4TrfP9mO57AQY543KTLaTl8N')
		list.append('&youtube_id=MbgrFDbE3b0')
		list.append('&youtube_id=kWmBP09MM9w')
		list.append('&youtube_id=P3gW3zPEhjY')
		list.append('&youtube_id=uj9miIc0Ow4')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLzsJ0eqQdfa6tDzsMSoC3cNFyhTLUW8Y-') #English
		list.append('&youtube_pl=PLWXd7CnPnkybfU-_26JRUtOR1-ItqJ6-l') #English
	addDir(addonString(10440).encode('utf-8'),list,17,thumb,addonString(104400).encode('utf-8'),'1',0,fanart)
	
	'''Inspector Gadget 2015 / חוש חש הבלש (2015)'''
	thumb = 'https://www.thetvdb.com/banners/posters/290688-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/290688-1.jpg'
	plot = "Inspector Gadget, the world's favorite bumbling detective, is back in this all-new animated series that also sees the return of his nemesis, the evil Dr. Claw. With his nephew Talon by his side, Dr. Claw has reactivated his global crime syndicate M.A.D. and has his sights on taking over the world, unless Gadget, his niece Penny and her dog Brain can stop him -- again."
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F290688-2.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F290688-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DInspector%20Gadget%202015%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Finspector-gadget-2015')
	addDir(addonString(10440).encode('utf-8') + space + '(2015)',list,6,thumb,plot,'1',0,fanart)
	
	'''Almost Naked Animals / חיות בקצר'''
	thumb = 'https://www.thetvdb.com/banners/posters/250281-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/250281-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1565.jpg&mode=3&name=%d7%97%d7%99%d7%95%d7%aa%20%d7%91%d7%a7%d7%a6%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1565&series_name=%d7%97%d7%99%d7%95%d7%aa%20%d7%91%d7%a7%d7%a6%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1565%2falmost-naked-animals-%d7%97%d7%99%d7%95%d7%aa-%d7%91%d7%a7%d7%a6%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLLSc-PLxC0fDK_KKFnOqYjpWZfeOlqBdz6uc5mk')
		list.append('&youtube_pl=PLa6NpPOElbKAbujKC5-PI_kqLP8Wv6qsL')
	addDir(addonString(10493).encode('utf-8'),list,17,thumb,addonString(104930).encode('utf-8'),'1',0,fanart)
	
	'''Larva / חיים בביוב*'''
	thumb = 'https://www.thetvdb.com/banners/posters/271218-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/271218-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1605.jpg&mode=3&name=%d7%97%d7%99%d7%99%d7%9d%20%d7%91%d7%91%d7%99%d7%95%d7%91%20-%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1605&series_name=%d7%97%d7%99%d7%99%d7%9d%20%d7%91%d7%91%d7%99%d7%95%d7%91%20-%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1605%2flarva-%d7%97%d7%99%d7%99%d7%9d-%d7%91%d7%91%d7%99%d7%95%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLxA7z7YQAqR7OCDM5-Cc4O-Nuswd8ChZ7')
		list.append('&youtube_pl=PLCAz374llh8UZxgCmKrBgdxPbjv6DdV3W')
		list.append('&youtube_pl=PLVkmXbocRodPcTHEC9P2JtcO3xn1NbRz9')
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=PLjDLgg_nO1v4dctdGzRJOy-yd0sHJk8oa')
	addDir(addonString(10441).encode('utf-8'),list,6,thumb,addonString(104410).encode('utf-8'),'1',"",fanart)
	
	'''Nerds and Monsters / חנונים ומפלצות'''
	thumb = 'https://www.thetvdb.com/banners/posters/279548-1.jpg'
	fanart = 'http://slaphappycartoons.com/wp-content/uploads/2016/09/NERDS-and-MONSTERS_link.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1664.jpg&mode=3&name=%d7%97%d7%a0%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%9e%d7%a4%d7%9c%d7%a6%d7%95%d7%aa%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1664&series_name=%d7%97%d7%a0%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%9e%d7%a4%d7%9c%d7%a6%d7%95%d7%aa%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1664%2fnerds-and-monsters-%d7%97%d7%a0%d7%95%d7%a0%d7%99%d7%9d-%d7%95%d7%9e%d7%a4%d7%9c%d7%a6%d7%95%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLXZL-qLQhCnYMJh0r02R7-9YUqDxyg3z0')
	addDir(addonString(10442).encode('utf-8'),list,17,thumb,addonString(104420).encode('utf-8'),'1',"",fanart)
	
	'''ThunderCats /חתולי הרעם'''
	thumb = 'https://www.thetvdb.com/banners/posters/70355-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70355-9.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1786.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1786&series_name=%d7%97%d7%aa%d7%95%d7%9c%d7%99%20%d7%94%d7%a8%d7%a2%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%91%d7%9e%d7%a9%d7%9a%20%d7%93%d7%95%d7%a8%d7%95%d7%aa%20%d7%90%d7%a8%d7%95%d7%9b%d7%99%d7%9d%2c%20%d7%97%d7%aa%d7%95%d7%9c%d7%99%20%d7%94%d7%a8%d7%a2%d7%9d%20%d7%97%d7%99%d7%95%20%d7%91%d7%a9%d7%9c%d7%95%d7%95%d7%94%20%d7%95%d7%91%d7%a0%d7%a2%d7%99%d7%9e%d7%99%d7%9d%2c%20%d7%90%d7%9a%20%d7%9c%d7%90%d7%97%d7%a8%20%d7%a9%d7%9e%d7%9e%d7%9c%d7%9b%d7%aa%d7%9d%2c%20%d7%98%d7%a0%d7%93%d7%a8%d7%94%2c%20%d7%94%d7%95%d7%a9%d7%9e%d7%93%d7%94%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%9e%d7%9e%d7%95%d7%a8%d7%a2%20%d7%94%d7%90%d7%9b%d7%96%d7%a8%2c%20%d7%94%d7%9d%20%d7%92%d7%95%d7%9c%d7%99%d7%9d%20%d7%9c%d7%9b%d7%95%d7%9b%d7%91%20%22%d7%90%d7%a8%d7%a5%20%d7%94%d7%a9%d7%9c%d7%99%d7%a9%d7%99%22.%20%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%97%d7%aa%d7%95%d7%9c%d7%99%20%d7%94%d7%a8%d7%a2%d7%9d%2c%20%d7%91%d7%a8%d7%90%d7%a9%d7%95%d7%aa%20%d7%91%d7%a0%d7%95%20%d7%a9%d7%9c%20%d7%9e%d7%95%d7%a9%d7%9c%20%d7%98%d7%a0%d7%93%d7%95%d7%a8%d7%94%20%d7%94%d7%9e%d7%95%d7%a9%d7%9e%d7%93%d7%aa%2c%20%d7%99%d7%95%d7%a6%d7%90%d7%aa%20%d7%9c%d7%9e%d7%a1%d7%a2%20%d7%90%d7%9e%d7%99%d7%a5%20%d7%91%d7%9e%d7%98%d7%a8%d7%94%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%22%d7%a1%d7%a4%d7%a8%20%d7%94%d7%9e%d7%95%d7%a4%d7%aa%d7%99%d7%9d%22%2c%20%d7%91%d7%a2%d7%96%d7%a8%d7%aa%d7%95%20%d7%99%d7%95%d7%9b%d7%9c%d7%95%20%d7%9c%d7%a2%d7%a6%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%9e%d7%9e%d7%95%d7%a8%d7%a2.%20%d7%91%d7%9e%d7%94%d7%a8%d7%94%2c%20%d7%94%d7%9d%20%d7%99%d7%91%d7%99%d7%a0%d7%95%20%d7%9b%d7%99%20%d7%a2%d7%9c%d7%99%d7%94%d7%9d%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%d7%94%d7%a1%d7%a4%d7%a8%20%d7%91%d7%9e%d7%94%d7%a8%d7%94%2c%20%d7%90%d7%9a%20%d7%99%d7%95%d7%aa%d7%a8%20%d7%97%d7%a9%d7%95%d7%91%20%d7%9e%d7%9b%d7%9a%20%e2%80%93%20%d7%9c%d7%95%d7%95%d7%93%d7%90%20%d7%a9%d7%9c%d7%90%20%d7%99%d7%94%d7%99%d7%94%20%d7%91%d7%99%d7%93%d7%99%d7%94%d7%9d%20%d7%a9%d7%9c%20%d7%90%d7%9c%d7%95%20%d7%94%d7%9e%d7%91%d7%a7%d7%a9%d7%99%d7%9d%20%d7%9c%d7%96%d7%a8%d7%95%d7%a2%20%d7%94%d7%a8%d7%a1%20%d7%95%d7%97%d7%95%d7%a8%d7%91%d7%9f.%20&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1786%2fthundercats-%d7%97%d7%aa%d7%95%d7%9c%d7%99-%d7%94%d7%a8%d7%a2%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_id=tVRhbs4wjhM')
		list.append('&youtube_id=ktSs9OT7Dqk')
		list.append('&youtube_id=xgu7gcM689A')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL4CFA334404DEC69F') #English
		list.append('&youtube_pl=PLcbFHwFk2aTDCIXkYyTavn8DO8kA5t7FE')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLjiShxUr9GYBkN3-bYt5Y5P-vMPpaeHZQ')
	addDir(addonString(10443).encode('utf-8'),list,17,thumb,addonString(104430).encode('utf-8'),'1',"",fanart)

	'''Tak and the Power of Juju / טאק וכוח הג'וג'ו'''
	thumb = 'https://www.thetvdb.com/banners/posters/168761-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/168761-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1790.jpg&mode=3&name=%d7%98%d7%90%d7%a7%20%d7%95%d7%9b%d7%95%d7%97%20%d7%94%d7%92%27%d7%95%d7%92%27%d7%95%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1790&series_name=%d7%98%d7%90%d7%a7%20%d7%95%d7%9b%d7%95%d7%97%20%d7%94%d7%92%27%d7%95%d7%92%27%d7%95%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1790%2ftak-and-the-power-of-juju-%d7%98%d7%90%d7%a7-%d7%95%d7%9b%d7%95%d7%97-%d7%94%d7%92-%d7%95%d7%92-%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLPQjX_uthHq6OJLhZRr6G2jQtBMC8VIKr')
	addDir(addonString(10494).encode('utf-8'),list,17,thumb,addonString(104940).encode('utf-8'),'1',0,fanart)
	
	'''David the Gnome / טוב טוב הגמד'''
	thumb = 'https://www.thetvdb.com/banners/posters/70815-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70815-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/70815-10.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1581.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1581&series_name=%d7%98%d7%95%d7%91%20%d7%98%d7%95%d7%91%20%d7%94%d7%92%d7%9e%d7%93%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%98%d7%95%d7%91%d7%98%d7%95%d7%91%20%d7%94%d7%95%d7%90%20%d7%92%d7%9e%d7%93%20%d7%a0%d7%93%d7%99%d7%91%20%d7%95%d7%98%d7%95%d7%91%20%d7%9c%d7%91%20%d7%94%d7%99%d7%95%d7%a6%d7%90%20%d7%a2%d7%9d%20%d7%90%d7%a9%d7%aa%d7%95%20%d7%98%d7%95%d7%98%d7%99%20%d7%9c%d7%98%d7%a4%d7%9c%20%d7%94%d7%99%d7%98%d7%91%20%d7%91%d7%97%d7%99%d7%95%d7%aa%20%d7%94%d7%99%d7%a2%d7%a8%20%d7%95%d7%9c%d7%94%d7%aa%d7%9e%d7%95%d7%93%d7%93%20%d7%9e%d7%95%d7%9c%20%d7%94%d7%98%d7%a8%d7%95%d7%9c%d7%99%d7%9d%20%d7%95%d7%91%d7%a0%d7%99%20%d7%94%d7%90%d7%93%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1581%2fthe-world-of-david-the-gnome-%d7%98%d7%95%d7%91-%d7%98%d7%95%d7%91-%d7%94%d7%92%d7%9e%d7%93-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&dailymotion_pl=x4932d') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLrEuz9dJQmAkIYkhcB4iZpoOlUDnMNDif') #English
		list.append('&youtube_pl=PL0630E307D00F8411') #English
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL72AD87F35AE91F6E') #French
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL9-GLKMfFv9WHO9fJcaCx9GeOF9q8-Lo1') #Italian
	if 'Spanish' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/70815-7.jpg'
	if 'Dutch' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/70815-4.jpg'

	addDir(addonString(10444).encode('utf-8'),list,17,thumb,addonString(104440).encode('utf-8'),'1',0,fanart)
	
	'''Totally Spies / טוטלי ספייס'''
	thumb = 'https://www.thetvdb.com/banners/posters/77625-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77625-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f462.jpg&mode=3&name=%d7%98%d7%95%d7%98%d7%9c%d7%99%20%d7%a1%d7%a4%d7%99%d7%99%d7%a1%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=462&series_name=%d7%98%d7%95%d7%98%d7%9c%d7%99%20%d7%a1%d7%a4%d7%99%d7%99%d7%a1%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f462%2ftotally-spies-%d7%98%d7%95%d7%98%d7%9c%d7%99-%d7%a1%d7%a4%d7%99%d7%99%d7%a1-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLFP5pUyg4YtCFkEzFyhKbFs2KL_8SxVFM') #English
		list.append('&youtube_pl=PLDIydMBGHDvKUHM_a0qca8Nrj1SxWwgO-') #English
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLby7JALZWGy53rZr4yXo4BkjpwXLhmNFI') #Russian
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PL37423D9401198B55') #Serbian
	addDir(addonString(10445).encode('utf-8'),list,17,thumb,addonString(104450).encode('utf-8'),'1',"",fanart)
	
	'''Tom and Jerry / טום וג'רי*'''
	thumb = 'https://www.thetvdb.com/banners/posters/72860-11.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/72860-17.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F22%2Fimage%2F555x418%2FThe_Cleveland_Show_.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Cleveland%20Show%20(2009%E2%80%932013)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-cleveland-show-2009-2013-tv-series')
	list.append('&youtube_pl=PLN0EJVTzRDL-jbMDnITZcYO48kE1Hv3mc')
	list.append('&youtube_pl=PLs3DueTtwGGppFDT2xv9zVBf4mz6RuOLj')
	list.append('&youtube_pl=PL6hnqKp_bygo_2MFE6j3WWLitYXwhHGx3')
	list.append('&youtube_pl=PLAWEtMG6fBxDZh5154CQaa1bYd5LXjrEE')
	addDir(addonString(10446).encode('utf-8'),list,17,thumb,addonString(104460).encode('utf-8'),'1',0,fanart)
	
	'''Adventures of Tom Sawyer / טום סויר'''
	thumb = 'https://www.thetvdb.com/banners/posters/80944-10.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/80944-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1438.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1438&series_name=%d7%98%d7%95%d7%9d%20%d7%a1%d7%95%d7%99%d7%99%d7%a8%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%98%d7%95%d7%9d%20%d7%a1%d7%95%d7%99%d7%99%d7%a8%20%d7%94%d7%95%d7%90%20%d7%a0%d7%a2%d7%a8%20%d7%a6%d7%a2%d7%99%d7%a8%20%d7%94%d7%92%d7%93%d7%9c%20%d7%9c%d7%90%d7%95%d7%a8%d7%9a%20%d7%a0%d7%94%d7%a8%20%d7%94%d7%9e%d7%99%d7%a1%d7%99%d7%a1%d7%99%d7%a4%d7%99%20%d7%91%d7%90%d7%9e%d7%a6%d7%a2%20%d7%94%d7%9e%d7%90%d7%94%20%d7%94-19.%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%a8%d7%95%20%d7%94%d7%90%d7%a7%d7%9c%d7%91%d7%a8%d7%99%20%d7%a4%d7%99%d7%9f%2c%20%d7%94%d7%95%d7%90%20%d7%9e%d7%91%d7%9c%d7%94%20%d7%90%d7%aa%20%d7%96%d7%9e%d7%a0%d7%95%20%d7%91%d7%94%d7%91%d7%a8%d7%96%d7%94%20%d7%9e%d7%91%d7%99%d7%aa%20%d7%94%d7%a1%d7%a4%d7%a8%2c%20%d7%91%d7%93%d7%99%d7%92%2c%20%d7%91%d7%98%d7%99%d7%a4%d7%95%d7%a1%20%d7%a2%d7%9c%20%d7%a2%d7%a6%d7%99%d7%9d%20%d7%95%d7%91%d7%97%d7%99%d7%a4%d7%95%d7%a9%20%d7%90%d7%97%d7%a8%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1438%2ftom-sawyer-%d7%98%d7%95%d7%9d-%d7%a1%d7%95%d7%99%d7%99%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLStjg118dmDO9ReHlRp5abjNBR5yJ1kpK') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLGU_lKDKx9IZHY1DfhcKaceLT_WJEc0wL') #Spanish
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLiItfFtbus3Dq0IueYp8XJOkWXwDW7K1V') #French
	addDir(addonString(10447).encode('utf-8'),list,17,thumb,addonString(104470).encode('utf-8'),'1',0,fanart)
	
	'''Turbo FAST / טורבו צוות פגז'''
	thumb = 'https://www.thetvdb.com/banners/posters/268855-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/268855-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1615.jpg&mode=3&name=%d7%98%d7%95%d7%a8%d7%91%d7%95%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%a4%d7%92%d7%96%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1615&series_name=%d7%98%d7%95%d7%a8%d7%91%d7%95%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%a4%d7%92%d7%96%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1615%2fturbo-fast-%d7%98%d7%95%d7%a8%d7%91%d7%95-%d7%a6%d7%95%d7%95%d7%aa-%d7%a4%d7%92%d7%96-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=UCsW-cNhlQipm64Nw6YfRzDg') #English
	addDir(addonString(10448).encode('utf-8'),list,17,thumb,addonString(104480).encode('utf-8'),'1',"",fanart)
	
	'''Titeuf / טיטוף'''
	thumb = 'https://www.thetvdb.com/banners/posters/100991-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/100991-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f661.jpg&mode=3&name=%d7%98%d7%99%d7%98%d7%95%d7%a3%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=661&series_name=%d7%98%d7%99%d7%98%d7%95%d7%a3%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f661%2ftiteuf-%d7%98%d7%99%d7%98%d7%95%d7%a3-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLVaxnIxB-SSnTOY3UdnW1ydxMLkv2m3vr')	
	addDir(addonString(10449).encode('utf-8'),list,17,thumb,addonString(104490).encode('utf-8'),'1',"",fanart)
	
	'''Chip 'n Dale Rescue Rangers / יחידת ההצלה של צ'יפ ודייל'''
	thumb = 'https://www.thetvdb.com/banners/posters/75477-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75477-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F75477-6.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F75477-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DChip%20%27n%20Dale%20Rescue%20Rangers%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fchip-and-dale-rescue-rangers')
		
	addDir(addonString(10383).encode('utf-8'),list,6,thumb,addonString(103830).encode('utf-8'),'1',0,fanart)
	
	'''PJ Masks / כוח פיג'יי'''
	thumb = 'https://www.thetvdb.com/banners/posters/300921-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/300921-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F300921-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F300921-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DPJ%20Masks%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpj-masks')
		
	addDir(addonString(10394).encode('utf-8'),list,6,thumb,addonString(103940).encode('utf-8'),'1',0,fanart)
	
	'''T.U.F.F. Puppy / כלב חשאי'''
	thumb = 'https://www.thetvdb.com/banners/posters/196351-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/196351-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f778.jpg&mode=3&name=%d7%9b%d7%9c%d7%91%20%d7%97%d7%a9%d7%90%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=778&series_name=%d7%9b%d7%9c%d7%91%20%d7%97%d7%a9%d7%90%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f778%2ftuff-puppy-%d7%9b%d7%9c%d7%91-%d7%97%d7%a9%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%eb%ec%e1%20%e7%f9%e0%e9&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2503183')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ec%fa%f4%e5%f1%20%e0%fa%20%e1%ec%e9%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2853374')
		list.append('&youtube_id=70mN9C1VigM')
		list.append('&youtube_id=EZg4C1koHJE')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL0FiPoE71AM1UH15ojxY5C5vj5uSv6eaz')
	addDir(addonString(10450).encode('utf-8'),list,17,thumb,addonString(104500).encode('utf-8'),'1',0,fanart)
	
	'''Lucky Luke / לאקי לוק'''
	thumb = 'https://www.thetvdb.com/banners/posters/71558-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/71558-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1446.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1446&series_name=%d7%9c%d7%90%d7%a7%d7%99%20%d7%9c%d7%95%d7%a7%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%a2%d7%9c%d7%99%d7%9c%d7%95%d7%aa%d7%99%d7%95%20%d7%94%d7%9e%d7%a9%d7%a2%d7%a9%d7%a2%d7%95%d7%aa%20%d7%a9%d7%9c%20%d7%94%d7%91%d7%95%d7%a7%d7%a8%20%d7%9c%d7%90%d7%a7%d7%99%20%d7%9c%d7%95%d7%a7%2c%20%d7%90%d7%a9%d7%a8%20%d7%99%d7%93%d7%95%d7%a2%20%d7%9b%d7%90%d7%a7%d7%93%d7%95%d7%97%d7%9f%20%d7%94%d7%9e%d7%94%d7%99%d7%a8%20%d7%99%d7%95%d7%aa%d7%a8%20%d7%90%d7%a4%d7%99%d7%9c%d7%95%20%d7%9e%d7%94%d7%a6%d7%9c%20%d7%a9%d7%9c%20%d7%a2%d7%a6%d7%9e%d7%95.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1446%2flucky-luke-%d7%9c%d7%90%d7%a7%d7%99-%d7%9c%d7%95%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLVe-nXljLcEw1z0KRytUl_Lssg8qujUCH')
	if 'English' in General_LanguageL:	
		list.append('&youtube_pl=PLCD5B9AD1151F3E0B') #English
		list.append('&youtube_pl=PLBuQjTjLLLgzAxxC6lysDD-WO6x0CPFBQ') #English
	addDir(addonString(10451).encode('utf-8'),list,17,thumb,addonString(104510).encode('utf-8'),'1',"",fanart)
	
	'''Justice League / ליגת הצדק'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/76320-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/76320-11.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:	
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76320-11.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F76320-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DJustice%20League%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fjustice-league')
	
	addDir(addonString(10374).encode('utf-8'),list,6,thumb,addonString(103740).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES104H(General_LanguageL, background, background2) #צ'ימה
	
	'''Maya & Miguel / מאיה ומיגל'''
	thumb = 'https://www.thetvdb.com/banners/posters/73370-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73370-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1264.jpg&mode=3&name=%d7%9e%d7%90%d7%99%d7%94%20%d7%95%d7%9e%d7%99%d7%92%d7%9c%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1264&series_name=%d7%9e%d7%90%d7%99%d7%94%20%d7%95%d7%9e%d7%99%d7%92%d7%9c%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1264%2fmaya-miguel-%d7%9e%d7%90%d7%99%d7%94-%d7%95%d7%9e%d7%99%d7%92%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLvx5W_59a3514Kf8NIdDRBoFhe3TQUKds')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL_ZweOlCch9Y3VgJQMq44umQJJdWBtimm') #English
	addDir(addonString(10452).encode('utf-8'),list,17,thumb,addonString(104520).encode('utf-8'),'1',0,fanart)
	
	'''Masha and the Bear / מאשה והדוב*'''
	thumb = 'https://www.thetvdb.com/banners/posters/136401-13.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/136401-10.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&dailymotion_pl=x47br7')
	if 'Russian' in General_LanguageL or 1 + 1 == 2:
		list.append('&youtube_pl=PLXnIohISHNIuH97pzQYV5O96-Q7-VwhRV')
		list.append('&youtube_pl=PL4-zn_348odBKcfUeZznqhkc_-UYtWnep')
		list.append('&youtube_pl=PLdAdTJgxziWAXNLIR5oeHbUT8HDnXOjAt')
		list.append('&youtube_pl=PLXnIohISHNIvsnUNe8RwvhksUSFzdQsiT')
		list.append('&youtube_pl=PLPYC---L3hwl7yImm5Rk3Iol0Efln7CDe')
	addDir(addonString(10241).encode('utf-8'),list,17,thumb,addonString(102410).encode('utf-8'),'1',0,fanart)
	
	'''מולי וצומי'''
	thumb = 'https://he.wikipedia.org/wiki/%D7%9E%D7%95%D7%9C%D7%99_%D7%95%D7%A6%D7%95%D7%9E%D7%99#/media/File:Muliandzumi.jpeg'
	fanart = 'https://i.ytimg.com/vi/0Kc3es1dd0g/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2077.jpg&mode=3&name=%d7%9e%d7%95%d7%9c%d7%99%20%d7%95%d7%a6%d7%95%d7%9e%d7%99&series_id=2077&series_name=%d7%9e%d7%95%d7%9c%d7%99%20%d7%95%d7%a6%d7%95%d7%9e%d7%99&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2077%2fmuli-and-tzumi-%d7%9e%d7%95%d7%9c%d7%99-%d7%95%d7%a6%d7%95%d7%9e%d7%99')
		list.append('&youtube_pl=PLfcYs4SRZfuJHmb8y_BpUpzAsm1guoAlK')
	addDir(addonString(10453).encode('utf-8'),list,17,thumb,addonString(104530).encode('utf-8'),'1',0,fanart)
		
	'''Monster High . מונסטר היי'''
	thumb = 'https://www.thetvdb.com/banners/posters/247261-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/247261-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1594.jpg&mode=3&name=%d7%9e%d7%95%d7%a0%d7%a1%d7%98%d7%a8%20%d7%94%d7%99%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1594&series_name=%d7%9e%d7%95%d7%a0%d7%a1%d7%98%d7%a8%20%d7%94%d7%99%d7%99%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1594%2fmonster-high-%d7%9e%d7%95%d7%a0%d7%a1%d7%98%d7%a8-%d7%94%d7%99%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLq7XN-iC2Vqxe8H7-GCZoKzYTKmpDwFpz') #English
		list.append('&youtube_pl=PLq7XN-iC2Vqz1MIctpY7goTjf1mZv2F9Q') #English
		list.append('&youtube_pl=PLq7XN-iC2VqyFHnAVKvvATh7DJximiNrq') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLq7XN-iC2VqyruMLBI8MdvJjLub5URhtY') #Spanish
	
	addDir(addonString(10454).encode('utf-8'),list,17,thumb,addonString(104540).encode('utf-8'),'1',"",fanart)
	
	'''Winx Club / מועדון ווינX'''
	thumb = 'https://www.thetvdb.com/banners/posters/74256-13.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/74256-12.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f456.jpg&mode=3&name=%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f%20%d7%95%d7%95%d7%99%d7%a0%d7%a7%d7%a1%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=456&series_name=%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f%20%d7%95%d7%95%d7%99%d7%a0%d7%a7%d7%a1%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f456%2fwinx-club-%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f-%d7%95%d7%95%d7%99%d7%a0%d7%a7%d7%a1-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLby7JALZWGy6xV7aec0CC9LFdeaEgsM_g') #Hebrew
		list.append('&youtube_pl=PLsvJJHNjHidCEbC_IM4LC7Mp56wQ-3A4H') #Hebrew
		
		list.append('&dailymotion_pl=x3j85r') #S4
		list.append('&dailymotion_pl=x3v205') #S5
		list.append('&dailymotion_pl=x3w6u5') #S6
		list.append('&dailymotion_pl=x3tlpa') #S6
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLJg404csJ854N08KuIMR9prlfveYScLIz') #English
		list.append('&dailymotion_pl=x3ibmc') #S6
		list.append('&dailymotion_pl=x3rvbd') #S7
		
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLQvqWmQTCX-jR_xRqX-ouF8dbWC0yNz9t') #Spanish
		list.append('&youtube_pl=PLQvqWmQTCX-jBHlk7d79ZSeHLc5nV8Rzk') #Spanish
		
		list.append('&dailymotion_pl=x40gnb') #S3
		list.append('&dailymotion_pl=x449l3') #S7
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL80E8353D11F3BBE4') #French
	addDir(addonString(10455).encode('utf-8'),list,17,thumb,addonString(104550).encode('utf-8'),'1',"",fanart)
	
	'''Camp Lakebottom / מחנה הפחד'''
	thumb = 'https://www.thetvdb.com/banners/posters/271353-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/271353-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1616.jpg&mode=3&name=%d7%9e%d7%97%d7%a0%d7%94%20%d7%94%d7%a4%d7%97%d7%93%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1616&series_name=%d7%9e%d7%97%d7%a0%d7%94%20%d7%94%d7%a4%d7%97%d7%93%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1616%2fcamp-lakebottom-%d7%9e%d7%97%d7%a0%d7%94-%d7%94%d7%a4%d7%97%d7%93-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLGPMEy1jNEDZtmvAZQoddwLgK0GoAJGeV') #English
	addDir(addonString(10456).encode('utf-8'),list,17,thumb,addonString(104560).encode('utf-8'),'1',"",fanart)
	
	'''Trolls of Troy / מטורללים'''
	thumb = 'https://www.thetvdb.com/banners/posters/322822-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/322822-1.jpg'
	list = [] #Nick #Hot
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1667.jpg&mode=3&name=%d7%9e%d7%98%d7%95%d7%a8%d7%9c%d7%9c%d7%99%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1667&series_name=%d7%9e%d7%98%d7%95%d7%a8%d7%9c%d7%9c%d7%99%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1667%2ftrolls-of-troy-%d7%9e%d7%98%d7%95%d7%a8%d7%9c%d7%9c%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLf5Wskorw9t6lSLxSpE9acGNYSGkirYp0')
	addDir(addonString(10457).encode('utf-8'),list,6,thumb,addonString(104570).encode('utf-8'),'1',"",fanart)
		
	'''Mighty Max / מייטי מקס'''
	thumb = 'https://www.thetvdb.com/banners/posters/76413-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76413-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&dailymotion_id=x17xn3s')
		list.append('&youtube_id=4t-8ebOB_I8') #S2E1
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLBA98D24AE96BD6CB') #S1-2
		list.append('&youtube_pl=PLWwnLtb5fzbaRqn_PpAQSXNOVyue_S8Bq') #S1
	if 'French' in General_LanguageL:
		list.append('&dailymotion_pl=xt1pg')
	if 'Italian' in General_LanguageL:
		list.append('&dailymotion_pl=x18qqjs')
	if 'Catalan' in General_LanguageL:
		list.append('&dailymotion_pl=x41v8u')
	
	addDir(addonString(10495).encode('utf-8'),list,17,thumb,addonString(104950).encode('utf-8'),'1',0,fanart)
	
	'''Mickey Mouse / מיקי מאוס'''
	thumb = 'https://www.thetvdb.com/banners/fanart/original/78988-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78988-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1490.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1490&series_name=%d7%9e%d7%99%d7%a7%d7%99%20%d7%9e%d7%90%d7%95%d7%a1&summary=%d7%9e%d7%99%d7%a7%d7%99%20%d7%9e%d7%90%d7%95%d7%a1%20%d7%94%d7%95%d7%90%20%d7%93%d7%9e%d7%95%d7%aa%20%d7%94%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%95%d7%94%d7%a7%d7%95%d7%9e%d7%99%d7%a7%d7%a1%20%d7%94%d7%91%d7%93%d7%99%d7%95%d7%a0%d7%99%d7%aa%20%d7%94%d7%9e%d7%a4%d7%95%d7%a8%d7%a1%d7%9e%d7%aa%20%d7%91%d7%99%d7%95%d7%aa%d7%a8%20%d7%a9%d7%94%d7%95%d7%9e%d7%a6%d7%90%d7%94%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%95%d7%95%d7%9c%d7%98%20%d7%93%d7%99%d7%a1%d7%a0%d7%99.%d7%93%d7%9e%d7%95%d7%aa%d7%95%20%d7%91%d7%a6%d7%95%d7%a8%d7%aa%20%d7%a2%d7%9b%d7%91%d7%a8%20%d7%95%d7%9e%d7%9b%d7%90%d7%9f%20%d7%a9%d7%9e%d7%94.%20%d7%91%d7%a0%d7%95%d7%91%d7%9e%d7%91%d7%a8%201978%20%d7%9c%d7%9b%d7%91%d7%95%d7%93%20%d7%99%d7%95%d7%9d%20%d7%94%d7%95%d7%9c%d7%93%d7%aa%d7%95%20%d7%94-50%2c%20%d7%94%d7%a4%d7%9a%20%d7%9e%d7%99%d7%a7%d7%99%20%d7%9e%d7%90%d7%95%d7%a1%20%d7%9c%d7%93%d7%9e%d7%95%d7%aa%20%d7%94%d7%9e%d7%a6%d7%95%d7%99%d7%99%d7%a8%d7%aa%20%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94%20%d7%a9%d7%a7%d7%99%d7%91%d7%9c%d7%94%20%d7%9b%d7%95%d7%9b%d7%91%20%d7%91%d7%a9%d7%93%d7%a8%d7%aa%20%d7%94%d7%9b%d7%95%d7%9b%d7%91%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%94%d7%95%d7%9c%d7%99%d7%95%d7%95%d7%93.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1490%2fmickey-mouse-%d7%9e%d7%99%d7%a7%d7%99-%d7%9e%d7%90%d7%95%d7%a1')
		list.append('&youtube_pl=PLRnOaTF6ebYr6lGEgf6g338-tVEdbDrpQ') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLzmYALoiB7Iu06wVm_j9wNLp3kMIMGprt') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLuVSRZz8Gp_SRZiUdbGQiDyVeWtGBignf') #Spanish
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=PLuVSRZz8Gp_S3LydxhuuBrgOGFWxwta5i') #Catalan
	addDir(addonString(10458).encode('utf-8'),list,17,thumb,addonString(104580).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://2.bp.blogspot.com/-D9F8GNiT1yg/Uh-cUtD8p-I/AAAAAAAABY0/2ja3WYAkTcY/s1600/Disney-Mickey-Mouse-Characters-Wallpaper.jpg", default=background2))
	
	'''Mikmak / מיקמק'''
	thumb = 'https://i.ytimg.com/vi/EYtgo9he7-U/maxresdefault.jpg'
	fanart = 'https://i.ytimg.com/vi/lXvVe_lKyTs/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f861.jpg&mode=3&name=%d7%9e%d7%99%d7%a7%d7%9e%d7%a7%20%3a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=861&series_name=%d7%9e%d7%99%d7%a7%d7%9e%d7%a7%20%3a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f861%2fmikmak-hasidra-%d7%9e%d7%99%d7%a7%d7%9e%d7%a7-%d7%94%d7%a1%d7%93%d7%a8%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL663sDNTault52-VzCCu4w0CfnoAtrmRg')
		list.append('&youtube_pl=PL663sDNTaulu5KpP6eyz9Xr3caOQUDEl_')
		list.append('&youtube_pl=PL663sDNTault52-VzCCu4w0CfnoAtrmRg')
		list.append('&youtube_id=1CshWmAFinY')
		list.append('&youtube_id=a5WNY-FMMyQ')
	addDir(addonString(10459).encode('utf-8'),list,17,thumb,addonString(104590).encode('utf-8'),'1',"",fanart)
	
	'''מלחמת הכוכבים: המורדים'''
	CATEGORIES104G(General_LanguageL, background, background2)
	
	'''Briefe von Felix / פליקס הארנב'''
	thumb = 'https://www.thetvdb.com/banners/posters/117301-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/117301-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLtcsu9_D0HqT0GQQOAZa0IojDpHPo6bOf') #Hebrew
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLNaowF97PdRVElGqD9b2O63gZ3E3rkdTn') #German
	addDir(addonString(10460).encode('utf-8'),list,17,thumb,addonString(104600).encode('utf-8'),'1',0,fanart)
	
	'''Around the World With Willy Fog / מסביב לעולם עם וילי פוג'''
	thumb = 'https://www.thetvdb.com/banners/posters/80357-9.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/80357-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2098.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=2098&series_name=%d7%9e%d7%a1%d7%91%d7%99%d7%91%20%d7%9c%d7%a2%d7%95%d7%9c%d7%9d%20%d7%91-80%20%d7%99%d7%95%d7%9d%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9c%d7%95%d7%a7%d7%97%d7%aa%20%d7%90%d7%aa%20%d7%94%d7%a1%d7%99%d7%a4%d7%95%d7%a8%20%d7%9c%d7%9b%d7%99%d7%95%d7%95%d7%9f%20%d7%94%d7%95%d7%9e%d7%95%d7%a8%d7%99%d7%a1%d7%98%d7%99%20%d7%95%d7%a9%d7%95%d7%a0%d7%94%20%d7%9e%d7%94%d7%9e%d7%a7%d7%95%d7%a8%20%d7%94%d7%a1%d7%a4%d7%a8%d7%95%d7%aa%d7%99.%20%d7%a4%d7%99%d7%9c%d7%99%d7%90%d7%a1%20%d7%a4%d7%95%d7%92%20%d7%9e%d7%aa%d7%a2%d7%a8%d7%91%20%d7%a2%d7%9d%20%d7%9c%d7%95%d7%a8%d7%93%20%d7%9e%d7%99%d7%99%d7%96%20%d7%a9%d7%99%d7%a7%d7%99%d7%a3%20%d7%90%d7%aa%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%91%2080%20%d7%99%d7%95%d7%9d%20%d7%91%d7%9b%d7%93%d7%99%20%d7%a9%d7%99%d7%a8%d7%a9%d7%94%20%d7%9c%d7%95%20%d7%9c%d7%94%d7%a0%d7%a9%d7%90%20%d7%9c%d7%90%d7%97%d7%99%d7%99%d7%a0%d7%99%d7%aa%20%d7%a9%d7%9c%d7%95%2c%20%d7%91%d7%9c%d7%99%d7%a0%d7%93%d7%94%20%d7%9e%d7%99%d7%99%d7%96(%d7%95%d7%9c%d7%90%20%d7%9c%d7%a0%d7%a1%d7%99%d7%9b%d7%94%20%d7%90%d7%95%d7%93%d7%94).%20%d7%9c%d7%95%d7%a8%d7%93%20%d7%9e%d7%99%d7%99%d7%96%20%d7%a9%d7%95%d7%9c%d7%97%20%d7%90%d7%aa%20%d7%94%d7%9e%d7%a9%d7%a8%d7%aa%20%d7%94%d7%a8%d7%a9%d7%a2%20%d7%a9%d7%9c%d7%95(%d7%9c%d7%90%20%d7%91%d7%9c%d7%a9%20%d7%91%d7%a8%d7%99%d7%98%d7%99)%20%d7%91%d7%a2%d7%9c%20%d7%a4%d7%99%d7%a6%d7%95%d7%9c%20%d7%94%d7%90%d7%99%d7%a9%d7%99%d7%95%d7%aa%2c%20%d7%9e%d7%a8%20%d7%a4%d7%99%d7%a7%d7%a1%2c%20%d7%91%d7%9b%d7%93%d7%99%20%d7%9c%d7%a2%d7%a6%d7%95%d7%a8%20%d7%91%d7%a2%d7%93%d7%9d%20%d7%91%d7%9b%d7%9c%20%d7%9e%d7%97%d7%99%d7%a8.%20%d7%94%d7%9e%d7%a9%d7%a8%d7%aa%20%d7%a9%d7%9c%20%d7%a4%d7%95%d7%92%2c%20%d7%a4%d7%a1%d7%a4%d7%a8%d7%98%d7%95%2c%20%d7%a6%d7%95%d7%a2%d7%a7%20%d7%9b%d7%9c%20%d7%94%d7%96%d7%9e%d7%9f%20%22%d7%a4%d7%99%d7%a7%d7%a1%20%d7%98%d7%a8%d7%99%d7%a7%d7%a1%2c%20%d7%a4%d7%99%d7%a7%d7%a1%20%d7%98%d7%a8%d7%99%d7%a7%d7%a1%22%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%a4%d7%99%d7%a7%d7%a1%20%d7%97%d7%95%d7%a9%d7%a3%20%d7%9e%d7%9c%d7%9b%d7%95%d7%93%d7%aa%20%d7%97%d7%93%d7%a9%d7%94%20%d7%91%d7%93%d7%a8%d7%9b%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2098%2faround-the-world-in-eighty-days-%d7%9e%d7%a1%d7%91%d7%99%d7%91-%d7%9c%d7%a2%d7%95%d7%9c%d7%9d-%d7%91-80-%d7%99%d7%95%d7%9d-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		pass
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL1BAF9E4D733BF48B') #Dutch
		list.append('&youtube_pl=PL250AA5EDA0ED364A1') #Dutch
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL9-GLKMfFv9UxrkzbGzPjtZSlk25xmS6T') #Italian
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL39408FA9CAE12F76') #French
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL859115B075C9FC75') #Russian
		list.append('&youtube_pl=PL7BCE3AB0D5BBD87C') #Russian
	
	addDir(addonString(10461).encode('utf-8'),list,17,thumb,addonString(104610).encode('utf-8'),'1',"",fanart)
	
	'''Babar / מסיפורי המלך בבר'''
	thumb = 'https://www.thetvdb.com/banners/posters/77278-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77278-5.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1657.jpg&mode=3&name=%d7%9e%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%91%d7%91%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1657&series_name=%d7%9e%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%20%d7%94%d7%9e%d7%9c%d7%9a%20%d7%91%d7%91%d7%a8%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1657%2fbabar-%d7%9e%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99-%d7%94%d7%9e%d7%9c%d7%9a-%d7%91%d7%91%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLqcqK3dfusFJIWQ5DU_EUFPoRiPIdKj7H') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=UCFe57hUldf3jWklSRCuztgg') #English
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLIB_OgW7nli5rQJ3MfAEg5xLpo3FuMHUS')
		
	addDir(addonString(10462).encode('utf-8'),list,17,thumb,addonString(104620).encode('utf-8'),'1',"",fanart)
	
	'''Monster by Mistake / מפלצת בטעות'''
	thumb = 'https://www.thetvdb.com/banners/posters/70478-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70478-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f819.jpg&mode=3&name=%d7%9e%d7%a4%d7%9c%d7%a6%d7%aa%20%d7%91%d7%98%d7%a2%d7%95%d7%aa%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=819&series_name=%d7%9e%d7%a4%d7%9c%d7%a6%d7%aa%20%d7%91%d7%98%d7%a2%d7%95%d7%aa%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f819%2fmonster-by-mistake-%d7%9e%d7%a4%d7%9c%d7%a6%d7%aa-%d7%91%d7%98%d7%a2%d7%95%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLCWuG3cXW_gboBSGpMvkHlNxqY0pG1HII') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_id=H2WSULnUyTA') #English
	addDir(addonString(10463).encode('utf-8'),list,6,thumb,addonString(104630).encode('utf-8'),'1',0,fanart)
	
	'''Hero Factory / מפעל הגיבורים'''
	thumb = 'https://www.thetvdb.com/banners/posters/190011-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/190011-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ee%f4%f2%ec%20%e4%e2%e9%e1%e5%f8%e9%ed&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1883282')
		list.append('&youtube_pl=PLuQCYUv97StTYPWiHQ70kxF6MLp_h8jEW') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLpXGrlS-zgkq5uuIfhl0hvocjnvOeXAcm') #English
	addDir(addonString(10487).encode('utf-8'),list,17,thumb,addonString(104870).encode('utf-8'),'1',0,fanart)
	
	'''Max & Shred / מקס ושרד'''
	thumb = 'https://www.thetvdb.com/banners/posters/286828-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/286828-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ee%f7%f1%20%e5%f9%f8%e3&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2851543')
		list.append('&youtube_pl=') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLugK-QLYyzSwRCsGOlt_fIN97UTEp5ulz') #English
	addDir(addonString(10828).encode('utf-8'),list,6,thumb,addonString(108280).encode('utf-8'),'1',0,fanart)

	'''Max Steel / מקס סטיל'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/268065-2.jpg'
	fanart = 'https://thetvdb.com/banners/fanart/original/268065-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1637.jpg&mode=3&name=%d7%9e%d7%a7%d7%a1%20%d7%a1%d7%98%d7%99%d7%9c%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1637&series_name=%d7%9e%d7%a7%d7%a1%20%d7%a1%d7%98%d7%99%d7%9c%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1637%2fmax-steel-%d7%9e%d7%a7%d7%a1-%d7%a1%d7%98%d7%99%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F268065-3.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F268065-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMax%20Steel%20(2013)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmax-steel-2013')
		list.append('&youtube_pl=PLqXC-FsML6on-N7kHFe4OLhTXZEPmj8A4') #English
		list.append('&youtube_pl=PLNVb4XeGx1kIO7u39mIT88QDxBgsF-dUA') #English
		list.append('&youtube_pl=PLqXC-PLEqwPYouHqaJwNaYQ_4vv7reSQXjO9gXO') #English
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLc6DM_HUHuJXuawQJtspo2-LMNEzp5z1a') #German
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=PLc6DM_HUHuJVKREFwsZx9EcVL7YmEk4Ar') #Greek
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLc6DM_HUHuJXa9FOdAzxUAPtGsqtbI0nP') #Spanish
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLc6DM_HUHuJXPFouQplvWEPcJZWJfZ2KS') #Turkish
	if 'Brazilian' in General_LanguageL:
		list.append('&youtube_pl=PLc6DM_HUHuJXXqRy06F3n3ixMvG1mztA8') #Brazilian

	addDir(addonString(10464).encode('utf-8'),list,6,thumb,addonString(104640).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES104E(General_LanguageL, background, background2) #משוגעגע
	
	'''Fairy Tale Police Department / משטרת האגדות'''
	thumb = 'https://www.thetvdb.com/banners/posters/277637-1.jpg'
	fanart = 'https://images-na.ssl-images-amazon.com/images/M/MV5BYWQxYTM5YzUtNjY3Ni00MTYxLTg0ZDAtYzZhNDYzMmMxMDRiXkEyXkFqcGdeQXVyMTA1NjQ5ODU@._V1_.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLR7DTcU2p0QiaEmc56lGHMpxW4ladE93X') #Hebrew
		list.append('&youtube_pl=PLWS_jfm9LLlk2ONsN9KrpUaublCKZuCY8') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL-b1n-EI-zIIRAwSuMTHbhrYUX4aeHNHL') #English
	addDir(addonString(10465).encode('utf-8'),list,17,thumb,addonString(104650).encode('utf-8'),'1',"",fanart)
	
	'''Adams Family / משפחת אדמס'''
	thumb = 'https://www.thetvdb.com/banners/posters/77313-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77313-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F53%2Fimage%2F555x418%2Fthe-addams-family-1992.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Addams%20Family%20(1992)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-addams-family-1992-tv-series')
		
	addDir(addonString(10342).encode('utf-8'),list,6,thumb,addonString(103420).encode('utf-8'),'1',0,fanart)
	
	'''The Simpsons / משפחת סימפסון'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/71663-15.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/71663-25.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f57.jpg&mode=3&name=%d7%9e%d7%a9%d7%a4%d7%97%d7%aa%20%d7%a1%d7%99%d7%9e%d7%a4%d7%a1%d7%95%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=57&series_name=%d7%9e%d7%a9%d7%a4%d7%97%d7%aa%20%d7%a1%d7%99%d7%9e%d7%a4%d7%a1%d7%95%d7%9f%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f57%2fthe-simpsons-%d7%9e%d7%a9%d7%a4%d7%97%d7%aa-%d7%a1%d7%99%d7%9e%d7%a4%d7%a1%d7%95%d7%9f-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLeY7w-PAPTxgVYpTYrGWr01Bbqf-FcXNn')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F71663-25.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F71663-15.jpg&mode=1&name=%5BB%5D%5BCOLOR%20white%5DThe%20Simpsons%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.kisspanda.net%2Fthe-simpsons%2F')
		list.append('&youtube_pl=PLeY7w-PAPTxgVYpTYrGWr01Bbqf-FcXNn')
		
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_id=fZeepoLKRes') #Spanish
	addDir(addonString(10466).encode('utf-8'),list,17,thumb,addonString(104660).encode('utf-8'),'1',0,fanart)
	
	'''The Flintstones / משפחת קדמוני'''
	thumb = 'https://www.thetvdb.com/banners/posters/76171-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76171-9.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F14%2Fimage%2F555x418%2FThe-Flintstone-TV-series.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Flintstones%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-flintstones-tv-series')
		
	addDir(addonString(10338).encode('utf-8'),list,6,thumb,addonString(103380).encode('utf-8'),'1',0,fanart)
	
	'''Naruto / נארוטו'''
	thumb = 'https://www.thetvdb.com/banners/posters/78857-10.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78857-36.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f612.jpg&mode=3&name=%d7%a0%d7%90%d7%a8%d7%95%d7%98%d7%95%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=612&series_name=%d7%a0%d7%90%d7%a8%d7%95%d7%98%d7%95%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f612%2fnaruto-%d7%a0%d7%90%d7%a8%d7%95%d7%98%d7%95-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL6PhB-zwNh9ZLpW3fvZ3O_8AoU5qw2OkD') #English
	addDir(addonString(10467).encode('utf-8'),list,6,thumb,addonString(104670).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES104J(General_LanguageL, background, background2) #נילס הולגרסון
	
	CATEGORIES104N(General_LanguageL, background, background2) #נינג'גו - מאסטר הספינג'יצו
	
	CATEGORIES104M(General_LanguageL, background, background2) #סאקורה לוכדת הקלפים
	
	'''Sabrina the Animated Series / סברינה המכשפה הצעירה'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/71811-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/71811-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1154.jpg&mode=3&name=%d7%a1%d7%91%d7%a8%d7%99%d7%a0%d7%94%20%d7%94%d7%9e%d7%9b%d7%a9%d7%a4%d7%94%20%d7%94%d7%a6%d7%a2%d7%99%d7%a8%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1154&series_name=%d7%a1%d7%91%d7%a8%d7%99%d7%a0%d7%94%20%d7%94%d7%9e%d7%9b%d7%a9%d7%a4%d7%94%20%d7%94%d7%a6%d7%a2%d7%99%d7%a8%d7%94%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1154%2fsabrina-the-animated-series-%d7%a1%d7%91%d7%a8%d7%99%d7%a0%d7%94-%d7%94%d7%9e%d7%9b%d7%a9%d7%a4%d7%94-%d7%94%d7%a6%d7%a2%d7%99%d7%a8%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLkGxGUmfDKPkOOYKrd8gpnwDa40NsBmUv') #Hebrew
		list.append('&youtube_pl=PLIR_swtdpOGk6ckBBUEvuorr5Dzh7gtze') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F71811-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F71811-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSabrina%20the%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fsabrina-the-animated-series')
		list.append('&youtube_pl=PLqcNVz8UuCsJRznsI9nDbIgVL-aJ6daZy') #English
		list.append('&youtube_pl=PLk0ITqthka1BOtOa4uq3CGk3rVyMlZSry') #English
	addDir(addonString(10469).encode('utf-8'),list,17,thumb,addonString(104690).encode('utf-8'),'1',"",fanart)
	
	'''Sonic X / סוניק X'''
	thumb = 'https://www.thetvdb.com/banners/posters/72459-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/72459-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f459.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=459&series_name=%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20X%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%a2%d7%9c%d7%99%d7%9c%d7%94%20%d7%9e%d7%aa%d7%97%d7%99%d7%9c%d7%94%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%91%d7%a2%d7%aa%20%d7%a0%d7%a1%d7%99%d7%95%d7%9f%20%d7%9c%d7%94%d7%a6%d7%99%d7%9c%20%d7%90%d7%aa%20%d7%a7%d7%a8%d7%99%d7%9d%20%d7%9e%d7%99%d7%93%d7%99%20%d7%93%d7%95%d7%a7%d7%98%d7%95%d7%a8%20%d7%90%d7%92%d7%9e%d7%9f%20-%20%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9e%d7%a9%d7%95%d7%92%d7%a8%d7%99%d7%9d%20%d7%9e%d7%a4%d7%9c%d7%a0%d7%98%d7%aa%20%d7%9e%d7%95%d7%91%d7%99%d7%95%d7%a1%20%d7%9c%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%91%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%90%d7%92%d7%9e%d7%9f%20%d7%95%d7%9e%d7%95%d7%a6%d7%90%d7%99%d7%9d%20%d7%a2%d7%a6%d7%9e%d7%9d%20%d7%91%d7%9e%d7%a8%d7%9b%d7%96%20%d7%94%d7%a2%d7%99%d7%a8%20%d7%a1%d7%98%d7%99%d7%99%d7%a9%d7%9f%20%d7%a1%d7%a7%d7%95%d7%95%d7%a8%20(Station%20Square)%20%d7%a4%d7%a8%d7%98%20%d7%9c%d7%90%d7%92%d7%9e%d7%9f%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%a9%d7%95%d7%92%d7%a8%20%d7%9c%d7%90%d7%99.%20%d7%91%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%d7%a4%d7%95%d7%92%d7%a9%20%d7%91%d7%97%d7%95%d7%a8%20%d7%a6%d7%a2%d7%99%d7%a8%20%d7%91%d7%a9%d7%9d%20%d7%9b%d7%a8%d7%99%d7%a1%20%d7%aa%d7%95%d7%a8%d7%a0%d7%93%d7%99%d7%99%d7%a7%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%90%d7%a8%d7%97%20%d7%90%d7%aa%20%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%91%d7%91%d7%99%d7%aa%d7%95.%20%d7%9b%d7%a2%d7%aa%20%d7%a2%d7%9c%20%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9c%d7%9e%d7%a0%d7%95%d7%a2%20%d7%9e%d7%93%d7%95%d7%a7%d7%98%d7%95%d7%a8%20%d7%90%d7%92%d7%9e%d7%9f%20%d7%95%d7%a2%d7%95%d7%96%d7%a8%d7%99%d7%95%20%d7%9e%d7%9c%d7%94%d7%a9%d7%aa%d7%9c%d7%98%20%d7%a2%d7%9c%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%95%d7%a2%d7%9c%20%d7%99%d7%94%d7%9c%d7%95%d7%9e%d7%99%20%d7%94%d7%9b%d7%90%d7%95%d7%a1.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f459%2fsonic-x-%d7%a1%d7%95%d7%a0%d7%99%d7%a7-x-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_id=AGuOahTZjjo') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLjkvw-XFL7UO4W3PcxdjXVWl-CNhm3DC7') #English
		list.append('&youtube_pl=PLEHMqhHsi5QWX6Sd2yK5irNNPFD5QSWWz') #English
		list.append('&youtube_pl=PLYEPskF2zHF6ztSidztkpjbi_7IqBDcMx') #English
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLk_S0ES7k_qA9lmnEtiTDzV6UxrkuKApr') #Polish
		list.append('&youtube_pl=PL-OG25DoK_1WRj1JafwlyxzbzqzqQgzy6') #Polish
	addDir(addonString(10470).encode('utf-8'),list,17,thumb,addonString(104700).encode('utf-8'),'1',"",fanart)
	
	'''Adventures of Sonic the Hedgehog / סוניק הקיפוד'''
	thumb = 'https://www.thetvdb.com/banners/posters/73630-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73630-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%a1%d7%95%d7%a0%d7%99%d7%a7&url=seriesId%3d2847535')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1518.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1518&series_name=%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%9c%d7%a1%d7%95%d7%a0%d7%99%d7%a7%20%d7%94%d7%a7%d7%99%d7%a4%d7%95%d7%93%20%d7%99%d7%a9%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%20%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%99%d7%9d%20%d7%a9%d7%9e%d7%90%d7%a4%d7%a9%d7%a8%d7%99%d7%9d%20%d7%9c%d7%95%20%d7%9c%d7%a0%d7%95%d7%a2%20%d7%91%d7%9e%d7%94%d7%99%d7%a8%d7%95%d7%aa%20%d7%95%d7%9c%d7%a1%d7%99%d7%99%d7%a2%20%d7%9c%d7%a9%d7%90%d7%a8%20%d7%9c%d7%95%d7%97%d7%9e%d7%99%20%d7%94%d7%97%d7%99%d7%a8%d7%95%d7%aa%20%d7%9c%d7%94%d7%99%d7%9c%d7%97%d7%9d%20%d7%91%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a0%d7%99%d7%a7%20%d7%94%d7%a8%d7%a9%d7%a2%20%d7%95%d7%91%d7%a2%d7%95%d7%a9%d7%94%20%d7%93%d7%91%d7%a8%d7%95%20%d7%99%d7%91%d7%91%d7%a0%d7%99%2c%20%d7%a9%d7%9e%d7%a0%d7%a1%d7%99%d7%9d%20%d7%9c%d7%94%d7%a4%d7%95%d7%9a%20%d7%90%d7%aa%20%d7%9b%d7%95%d7%9c%d7%9d%20%d7%9c%d7%9e%d7%a9%d7%a8%d7%aa%d7%99%d7%9d%20%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%99%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1518%2fsonic-the-hedgehog-%d7%a1%d7%95%d7%a0%d7%99%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL8w7FER3tTVB9hNreSe1l_qVOV-bLtxY1') #English
		list.append('&youtube_pl=PL_LA4m8CuQky60SVswr5tFqQxqKB997iI') #English
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PL9ieY-C9TKmJ5CrvBzjHaFT_M0M1pbP8o') #Portuguese
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLj8nCHarKPBNR5WeXivy6OXOMwiq13I4J') #Spanish
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLEA183AF7E0AB5E03') #French
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL046656EF6D2E6674') #Dutch
	addDir(addonString(10471).encode('utf-8'),list,17,thumb,addonString(104710).encode('utf-8'),'1',"",fanart)
	
	'''As Told by Ginger / סיפורי ג'ינג'ר'''
	thumb = 'https://www.thetvdb.com/banners/posters/81705-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/81705-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F48%2Fimage%2F555x418%2FAs_Told_By_Ginger.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAs%20Told%20by%20Ginger%20(TV%20Series)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fas-told-by-ginger-tv-series')
		
	addDir(addonString(10337).encode('utf-8'),list,6,thumb,addonString(103370).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104K(General_LanguageL, background, background2) #סיפורי מוש
	CATEGORIES104Q(General_LanguageL, background, background2) #סיילור מון
	
	'''Samurai Jack / סמוראי ג'ק'''
	thumb = 'https://www.thetvdb.com/banners/posters/75164-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/75164-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f781.jpg&mode=3&name=%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99%20%d7%92%27%d7%a7%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=781&series_name=%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99%20%d7%92%27%d7%a7%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f781%2fsamurai-jack-%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99-%d7%92-%d7%a7-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=ELPVbaRdOOKNE') #English
		list.append('&youtube_pl=EL4Pg00crNGI8') #English
		list.append('&youtube_pl=ELuFHychuxQ-8') #English
		list.append('&youtube_pl=PLegU20VWl5AVo8uIzYAkfxcrVbQOUV1ox') #English
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLF347DDA292C0B8D2') #Japanish
	addDir(addonString(10473).encode('utf-8'),list,17,thumb,addonString(104730).encode('utf-8'),'1',"",fanart)
	
	'''Sandokan / סנדוקאן'''
	thumb = 'https://www.thetvdb.com/banners/posters/266197-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/266197-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/266197-2.jpg'
		list.append('&youtube_pl=PLR7DTcU2p0QgWYVQap5zPK0MkwJizYku_') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLL7dcgwYKsm1SSm_ats6bW7UQ61ADzw-X') #English
		list.append('&youtube_pl=PLA9E141AA1CEBEF5A') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLfH8EZSX2voZXwKsPe5Yoi6ifBD7DrfDs') #Spanish
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL9873BAE8277C0C38') #Dutch
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLF93CFD76BC5D322A') #French
	
	addDir(addonString(10474).encode('utf-8'),list,17,thumb,addonString(104740).encode('utf-8'),'1',0,fanart)
	
	'''Spider-Man / ספיידרמן (אוסף)'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/73750-5.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/73750-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f781.jpg&mode=3&name=%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99%20%d7%92%27%d7%a7%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=781&series_name=%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99%20%d7%92%27%d7%a7%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f781%2fsamurai-jack-%d7%a1%d7%9e%d7%95%d7%a8%d7%90%d7%99-%d7%92-%d7%a7-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f723.jpg&mode=3&name=%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f%20%d7%90%d7%99%d7%a9%20%d7%94%d7%a2%d7%9b%d7%91%d7%99%d7%a9%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%20%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=723&series_name=%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f%20%d7%90%d7%99%d7%a9%20%d7%94%d7%a2%d7%9b%d7%91%d7%99%d7%a9%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f723%2fultimate-spider-man-%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f-%d7%90%d7%99%d7%a9-%d7%94%d7%a2%d7%9b%d7%91%d7%99%d7%a9-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f800.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=800&series_name=%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f%3a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%aa%20%d7%94%d7%97%d7%93%d7%a9%d7%94%20-%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%94%d7%a4%d7%a7%d7%94%20%d7%97%d7%93%d7%a9%d7%94%20%d7%9e%d7%90%d7%95%d7%9c%d7%a4%d7%a0%d7%99%20%d7%a7%d7%95%d7%9c%d7%95%d7%9e%d7%91%d7%99%d7%94%20%d7%90%d7%95%d7%93%d7%95%d7%aa%20%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f%2c%20%d7%92%d7%99%d7%91%d7%95%d7%a8%20%d7%94%d7%a7%d7%95%d7%9e%d7%99%d7%a7%d7%a1%20%d7%94%d7%9e%d7%a4%d7%95%d7%a8%d7%a1%d7%9d.%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9e%d7%a9%d7%9c%d7%91%d7%aa%20%d7%90%d7%aa%20%d7%9e%d7%99%d7%98%d7%91%20%d7%94%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%94%d7%93%d7%99%d7%92%d7%99%d7%98%d7%9c%d7%99%d7%aa%20%d7%a2%d7%9d%20%d7%90%d7%97%d7%aa%20%d7%94%d7%93%d7%9e%d7%95%d7%99%d7%95%d7%aa%20%d7%94%d7%90%d7%94%d7%95%d7%91%d7%95%d7%aa%20%d7%91%d7%aa%d7%95%d7%9c%d7%93%d7%95%d7%aa%20%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99%20%d7%94%d7%a2%d7%9c.%20%d7%9e%d7%94%d7%93%d7%95%d7%a8%d7%94%20%d7%91%d7%aa%202%20%d7%aa%d7%a7%d7%9c%d7%99%d7%98%d7%95%d7%a8%d7%99%d7%9d%20%d7%94%d7%9b%d7%95%d7%9c%d7%9c%d7%99%d7%9d%2013%20%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%95%d7%9b%d7%9f%20%d7%aa%d7%95%d7%a1%d7%a4%d7%95%d7%aa%20%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%95%d7%aa%20%d7%a8%d7%91%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f800%2fspider-man-the-new-animation-series-%d7%a1%d7%a4%d7%99%d7%99%d7%93%d7%a8%d7%9e%d7%9f-%d7%94%d7%a1%d7%93%d7%a8%d7%94-%d7%94%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%aa-%d7%94%d7%97%d7%93%d7%a9%d7%94-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78416-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78416-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSpider-Man%3A%20The%20New%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fspider-man-the-new-animated-series')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73750-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73750-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSpider-Man%20(1994)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fspider-man-the-animated-series')
		list.append('&youtube_pl=PLZs0gQed9tMSElYC30JlPa40L7oFWmQ_C') #English
		list.append('&youtube_pl=PL1EA385D86ED1BF85') #English
		list.append('&youtube_pl=PLIEbITAtGBeZUo2UUyjW6iQayfMXv8SCy') #English
		
	addDir(addonString(10475).encode('utf-8'),list,6,thumb,addonString(104750).encode('utf-8'),'1',0,fanart)
	
	'''The Jungle Book: The Adventures of Mowgli / ספר הגונגל: ההרפתקאות של מוגלי'''
	thumb = 'https://www.thetvdb.com/banners/posters/248254-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/248254-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLqcNVz8UuCsJYRDi1XZW3By4KEq4mHg20')
		list.append('&youtube_pl=PLwIu19ptPXDzGsGMVv2P3puYoDuFVvFCZ')
		
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PL4eNR_m-ysh-3hy-ADCehyREw7EGpv0z-')
	
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=PLPN067tVwPBn7xerpZ2TLIDxi2F_TTVgy')
		
	addDir(addonString(10258).encode('utf-8'),list,17,thumb,addonString(102580).encode('utf-8'),'1',0,fanart)
	
	'''Scooby-Doo / סקובי דו'''
	thumb = 'https://www.thetvdb.com/banners/posters/78260-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78260-9.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1429.jpg&mode=3&name=%d7%a1%d7%a7%d7%95%d7%91%d7%99%20%d7%93%d7%95%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&series_id=1429&series_name=%d7%a1%d7%a7%d7%95%d7%91%d7%99%20%d7%93%d7%95%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1429%2fscooby-doo-%d7%a1%d7%a7%d7%95%d7%91%d7%99-%d7%93%d7%95-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F43%2Fimage%2F555x418%2Fscooby-doo-where-are-you.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DScooby-Doo%2C%20Where%20Are%20You!%20(1969-1978)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fscooby-doo-where-are-you-1969-1978')
		list.append('&youtube_pl=ELXAmZ_OYm38M') #English
		list.append('&youtube_pl=ELPruZJpaRnmo') #English
		list.append('&youtube_pl=ELtUasJElSQn8') #English
		list.append('&youtube_pl=ELRhaVYhLImsM') #English
		list.append('&youtube_pl=ELh5rokX6BnT0') #English
	addDir(addonString(10476).encode('utf-8'),list,17,thumb,addonString(104760).encode('utf-8'),'1',"",fanart)
	
	'''Power Rangers / פאוור ריינג'רס'''
	thumb = 'http://www.thetvdb.com/banners/_cache/posters/72553-6.jpg'
	fanart = 'http://www.thetvdb.com/banners/fanart/original/72553-5.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2099.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=2099&series_name=%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%91%d7%97%d7%9c%d7%9c%20-%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%9c%d7%90%d7%97%d7%a8%20%d7%a9%d7%93%d7%99%d7%95%d7%90%d7%98%d7%95%d7%a7%d7%a1%20%d7%94%d7%a8%d7%a1%d7%94%20%d7%90%d7%aa%20%d7%9e%d7%a8%d7%9b%d7%96%20%d7%94%d7%91%d7%a7%d7%a8%d7%94%20%d7%95%d7%a9%d7%95%d7%91%20%d7%90%d7%99%d7%91%d7%93%d7%95%20%d7%94%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%90%d7%aa%20%d7%9b%d7%95%d7%97%d7%95%d7%aa%d7%99%d7%94%d7%9d%2c%20%d7%94%d7%9d%20%d7%9e%d7%97%d7%9c%d7%99%d7%98%d7%99%d7%9d%20%d7%9c%d7%a6%d7%90%d7%aa%20%d7%9c%d7%97%d7%9c%d7%9c%20%d7%9c%d7%9e%d7%a7%d7%95%d7%9d%20%d7%91%d7%98%d7%95%d7%97%20%d7%91%d7%95%20%d7%90%d7%99%d7%9f%20%d7%9c%d7%94%d7%9d%20%d7%90%d7%95%d7%99%d7%91%d7%99%d7%9d%20%d7%95%d7%9e%d7%a9%d7%90%d7%99%d7%a8%d7%99%d7%9d%20%d7%90%d7%aa%20%d7%92%27%d7%a1%d7%98%d7%99%d7%9f%20%d7%9e%d7%90%d7%97%d7%95%d7%a8.%20%d7%90%d7%9a%20%d7%94%d7%9d%20%d7%9c%d7%90%20%d7%99%d7%95%d7%93%d7%a2%d7%99%d7%9d%20%d7%a9%d7%92%d7%9d%20%d7%a9%d7%9d%20%d7%9e%d7%a6%d7%a4%d7%95%d7%aa%20%d7%9c%d7%94%d7%9d%20%d7%9b%d7%9e%d7%94%20%d7%94%d7%a4%d7%aa%d7%a2%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2099%2fpower-rangers-in-space-%d7%a4%d7%90%d7%95%d7%95%d7%a8-%d7%a8%d7%99%d7%99%d7%a0%d7%92-%d7%a8%d7%a1-%d7%91%d7%97%d7%9c%d7%9c-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2129.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=2129&series_name=%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%93%d7%99%d7%a0%d7%95%20%d7%a6%27%d7%90%d7%a8%d7%92%27&summary=%d7%a2%d7%9c%20%d7%a4%d7%a0%d7%99%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%a4%d7%a8%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%2c%20%d7%97%d7%99%d7%99%d7%96%d7%a8%20%d7%94%d7%a4%d7%a7%d7%99%d7%93%20%d7%90%d7%91%d7%a0%d7%99%20%d7%97%d7%9f%20%d7%a8%d7%91%d7%95%d7%aa%20%d7%a2%d7%95%d7%a6%d7%9e%d7%94%20%d7%90%d7%a6%d7%9c%2010%20%d7%93%d7%99%d7%a0%d7%95%d7%96%d7%90%d7%95%d7%a8%d7%99%d7%9d%2c%20%d7%90%d7%91%d7%9c%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%94%d7%93%d7%99%d7%a0%d7%95%d7%96%d7%90%d7%95%d7%a8%d7%99%d7%9d%20%d7%a0%d7%9b%d7%97%d7%93%d7%95%2c%20%d7%90%d7%91%d7%a0%d7%99%20%d7%94%d7%97%d7%9f%20%d7%90%d7%91%d7%93%d7%95.%20%d7%a2%d7%9b%d7%a9%d7%99%d7%95%20%d7%a6%d7%99%d7%99%d7%93%20%d7%a8%d7%90%d7%a9%d7%99%d7%9d%20%d7%92%d7%9c%d7%a7%d7%98%d7%99%20%d7%a0%d7%97%d7%95%d7%a9%20%d7%91%d7%93%d7%a2%d7%aa%d7%95%20%d7%9c%d7%94%d7%a9%d7%99%d7%91%20%d7%90%d7%aa%20%d7%90%d7%91%d7%a0%d7%99%20%d7%94%d7%97%d7%9f%20%d7%95%d7%9c%d7%94%d7%a8%d7%95%d7%a1%20%d7%90%d7%aa%20%d7%9b%d7%95%d7%9b%d7%91%20%d7%94%d7%9c%d7%9b%d7%aa%20%d7%a9%d7%9c%d7%a0%d7%95.%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%97%d7%93%d7%a9%20%d7%a9%d7%9c%20%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%97%d7%99%d7%99%d7%91%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%d7%90%d7%91%d7%a0%d7%99%20%d7%94%d7%97%d7%9f%20%d7%94%d7%90%d7%91%d7%95%d7%93%d7%95%d7%aa%20%d7%95%d7%9c%d7%94%d7%a9%d7%aa%d7%9e%d7%a9%20%d7%91%d7%9e%d7%98%d7%a2%d7%a0%d7%99%20%d7%94%d7%93%d7%99%d7%a0%d7%95%20%d7%a2%d7%9c%20%d7%9e%d7%a0%d7%aa%20%d7%9c%d7%97%d7%9e%d7%a9%20%d7%90%d7%aa%20%d7%90%d7%a8%d7%a1%d7%a0%d7%9c%20%d7%94%d7%96%d7%95%d7%a8%d7%93%d7%99%d7%9d%20%d7%95%d7%9e%d7%92%d7%94%20%d7%96%d7%95%d7%a8%d7%93%d7%99%d7%9d%20%d7%a2%d7%9c%20%d7%9e%d7%a0%d7%aa%20%d7%9c%d7%94%d7%a6%d7%99%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2129%2fpower-rangers-dino-charge-%d7%a4%d7%90%d7%95%d7%95%d7%a8-%d7%a8%d7%99%d7%99%d7%a0%d7%92-%d7%a8%d7%a1-%d7%93%d7%99%d7%a0%d7%95-%d7%a6-%d7%90%d7%a8%d7%92')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1709.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1709&series_name=%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%a1%d7%99%d7%91%d7%95%d7%91%d7%99%d7%9d%20%d7%9c%d7%93%d7%a7%d7%94&summary=%d7%94%d7%a2%d7%95%d7%a0%d7%94%20%d7%94-17%20%d7%a9%d7%9c%20%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%9e%d7%aa%d7%a8%d7%97%d7%a9%d7%aa%20%d7%91%d7%a9%d7%a0%d7%94%20%d7%9c%d7%90%20%d7%99%d7%93%d7%95%d7%a2%d7%94%20%d7%91%d7%a2%d7%aa%d7%99%d7%93.%20%d7%95%d7%99%d7%a8%d7%95%d7%a1%20%d7%9e%d7%97%d7%a9%d7%91%20%d7%94%d7%a8%d7%a1%d7%a0%d7%99%20%d7%91%d7%a2%d7%9c%20%d7%91%d7%99%d7%a0%d7%94%20%d7%9e%d7%9c%d7%90%d7%9b%d7%95%d7%aa%d7%99%d7%aa%20%d7%91%d7%a9%d7%9d%20%22%d7%95%d7%a0%d7%92%27%d7%99%d7%a7%d7%a1%22%20%d7%a4%d7%95%d7%aa%d7%97%20%d7%9e%d7%9c%d7%97%d7%9e%d7%94%20%d7%a0%d7%92%d7%93%20%d7%94%d7%90%d7%a0%d7%95%d7%a9%d7%95%d7%aa.%20%d7%95%d7%a0%d7%92%27%d7%99%d7%a7%d7%a1%20%d7%9e%d7%a6%d7%9c%d7%99%d7%97%20%d7%9c%d7%94%d7%a9%d7%aa%d7%9c%d7%98%20%d7%a2%d7%9c%20%d7%9b%d7%9c%20%d7%a8%d7%a9%d7%aa%d7%95%d7%aa%20%d7%94%d7%aa%d7%a7%d7%a9%d7%95%d7%a8%d7%aa%20%d7%91%d7%a8%d7%97%d7%91%d7%99%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%95%d7%91%d7%9e%d7%a7%d7%91%d7%99%d7%9c%20%d7%9e%d7%a7%d7%99%d7%9d%20%d7%a6%d7%91%d7%90%20%d7%a9%d7%9c%20%d7%97%d7%99%d7%99%d7%9c%d7%99%d7%9d%20%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%99%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%a9%d7%aa%d7%9c%d7%98%20%d7%aa%d7%95%d7%9a%203%20%d7%a9%d7%a0%d7%99%d7%9d%20%d7%a2%d7%9c%20%d7%9b%d7%9c%20%d7%94%d7%a2%d7%a8%d7%99%d7%9d%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9e%d7%9c%d7%91%d7%93%20%d7%94%d7%a2%d7%99%d7%a8%20%d7%a7%d7%95%d7%a8%d7%99%d7%a0%d7%aa%27%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%95%d7%92%d7%a0%d7%aa%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%9b%d7%99%d7%a4%d7%aa%20%d7%9e%d7%92%d7%9f%20%d7%a2%d7%a0%d7%a7%d7%99%d7%aa%20%d7%95%d7%91%d7%9c%d7%aa%d7%99%20%d7%97%d7%93%d7%99%d7%a8%d7%94.%d7%91%d7%a2%d7%a7%d7%91%d7%95%d7%aa%20%d7%9b%d7%9a%2c%20%d7%93%22%d7%a8%20%d7%a7%d7%99%d7%99%20%d7%9e%d7%a7%d7%99%d7%9e%d7%94%20%d7%a7%d7%91%d7%95%d7%a6%d7%94%20%d7%97%d7%93%d7%a9%d7%94%20%d7%a9%d7%9c%20%d7%9c%d7%95%d7%97%d7%9e%d7%99%d7%9d%20%d7%91%d7%a2%d7%9c%d7%99%20%d7%9b%d7%95%d7%97%d7%95%d7%aa-%d7%a2%d7%9c%20(%d7%94%22%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%22)%20%d7%90%d7%a9%d7%a8%20%d7%a6%d7%a8%d7%99%d7%9b%d7%99%d7%9d%20%d7%9c%d7%94%d7%99%d7%9c%d7%97%d7%9d%20%d7%91%d7%9b%d7%95%d7%97%d7%95%d7%aa%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%95%d7%a0%d7%92%27%d7%99%d7%a7%d7%a1%20%d7%95%d7%9c%d7%94%d7%92%d7%9f%20%d7%a2%d7%9c%20%d7%94%d7%9e%d7%a2%d7%95%d7%96%20%d7%94%d7%90%d7%97%d7%a8%d7%95%d7%9f%20%d7%a9%d7%9c%20%d7%94%d7%90%d7%a0%d7%95%d7%a9%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1709%2fpower-rangers-rpm-%d7%a4%d7%90%d7%95%d7%95%d7%a8-%d7%a8%d7%99%d7%99%d7%a0%d7%92-%d7%a8%d7%a1-%d7%a1%d7%99%d7%91%d7%95%d7%91%d7%99%d7%9d-%d7%9c%d7%93%d7%a7%d7%94')
		
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2617840')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2595189')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2520794')
		list.append('&youtube_pl=PLerLBKQYk11GAK1aviMgeEF2L6F3mWAEn') #Hebrew
		list.append('&youtube_pl=PLLIUYaEsBH6ZsDjq2ZJOnN4I4oMKNxqbZ') #Hebrew
		list.append('&youtube_pl=PLKMFPiSCwUk0w5bwxxxzob5tCGjnY4LfY') #Hebrew
		list.append('&youtube_pl=PLKMFPiSCwUk01oKz850en3WtD80zdmGus') #S14
	
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fwww.thetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72553-5.jpg&iconimage=http%3A%2F%2Fwww.thetvdb.com%2Fbanners%2F_cache%2Fposters%2F72553-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMighty%20Morphin%20Power%20Rangers%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmighty-morphin-power-rangers')
		list.append('&youtube_pl=PL5JnXzSWCdmd2i9k0mYlncHE3N11wa5sZ') #English
		list.append('&youtube_pl=PLN9GsozMMP5qugRIjDC4eAf3dF9ucONlr') #English
		list.append('&youtube_pl=PL32C56A2FCDA5B66D') #English
		list.append('&youtube_pl=PLC6071322045E33D9') #English
		list.append('&youtube_pl=PLC6071322045E33D9') #English
		list.append('&youtube_pl=PLhNIJQtTs5KLuj9S7gwqbH7G3rB1MXblb') #English
		list.append('&dailymotion_pl=x3n97x') #English
		list.append('&dailymotion_pl=x3m0wa') #English
	addDir(addonString(10477).encode('utf-8'),list,17,thumb,addonString(104770).encode('utf-8'),'1',"",fanart)
	
	'''Pokémon / פוקימון'''
	thumb = 'https://www.thetvdb.com/banners/posters/76703-6.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76703-7.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f433.jpg&mode=3&name=%d7%a4%d7%95%d7%a7%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=433&series_name=%d7%a4%d7%95%d7%a7%d7%99%d7%9e%d7%95%d7%9f%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f433%2fpokemon-%d7%a4%d7%95%d7%a7%d7%99%d7%9e%d7%95%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&dailymotion_pl=x34tag') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=UCBj2rgCsSoTlXPwuC69Bv2Q') #English
		list.append('&youtube_pl=PLYi30KTSgtG8xQtFGsYIiN4xX7NGq6sOK') #English
		list.append('&dailymotion_pl=x30xbc') #English
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2fchiaanime.co%2fuploads%2fthumbs%2f2015-04-06pokemon-1998b.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bcf_clearance%3da94a6c04fae90f972b0c79707c6338174f9b374f-1470303970-86400%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=Pokemon%20(1998)&url=http%3a%2f%2fchiaanime.co%2fAnime%2f1585%2fpokemon-1998%2f')
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_id=x2kmbwv') #Hindi
	
	addDir(addonString(10478).encode('utf-8'),list,17,thumb,addonString(104780).encode('utf-8'),'1',"",fanart)
	
	'''פוקימון (Black & White)'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2fchiaanime.co%2fuploads%2fthumbs%2f2015-07-06pokemon-black-amp-white-dubbedb.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bcf_clearance%3da94a6c04fae90f972b0c79707c6338174f9b374f-1470303970-86400%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=Pokemon%3a%20Black%20%26%20White%20(Dubbed)&url=http%3a%2f%2fchiaanime.co%2fAnime%2f4051%2fpokemon-black-amp-white-dubbed%2f')
	addDir(addonString(10478).encode('utf-8') + space + '(Black & White)',list,6,'http://assets.pokemon.com/assets/cms2/img/watch-pokemon-tv/seasons/season14/season14_logo_169_en.jpg',addonString(104780).encode('utf-8'),'1',"",getAddonFanart(background, custom="http://gearnuke.com/wp-content/uploads/2014/02/pokemon-black-and-white-anime-1.png", default=background2))
	
	'''פוקימון (Diamond & Pearl 2006-2010)'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2fchiaanime.co%2fuploads%2fthumbs%2f2015-04-23pokemon-diamond-amp-pearl-dubl.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bcf_clearance%3da94a6c04fae90f972b0c79707c6338174f9b374f-1470303970-86400%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=Pokemon%20Diamond%20%26%20Pearl%20(2006%20-%202010)%20(Dubbed)&url=http%3a%2f%2fchiaanime.co%2fAnime%2f1870%2fpokemon-diamond-amp-pearl-dub%2f')
	addDir(addonString(10478).encode('utf-8') + space + '(Diamond & Pearl 2006-2010)',list,6,'http://www.anime-planet.com/images/anime/covers/pokemon-diamond-and-pearl-1142.jpg',addonString(104780).encode('utf-8'),'1',"",getAddonFanart(background, custom="https://i.ytimg.com/vi/RbPUbGcng3U/maxresdefault.jpg", default=background2))
	
	'''פיטר פן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1000.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1000&series_name=%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%94%d7%97%d7%99%d7%a0%d7%95%d7%9b%d7%99%d7%aa%20%d7%97%d7%95%d7%96%d7%a8%d7%aa%20%d7%9c%d7%a9%d7%93%d7%a8%20%d7%90%d7%aa%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%a7%d7%9c%d7%a1%d7%99%d7%aa%20%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%2c%20%d7%94%d7%9e%d7%91%d7%95%d7%a1%d7%a1%d7%aa%20%d7%a2%d7%9c%20%d7%a1%d7%a4%d7%a8%d7%95%20%d7%a9%d7%9c%20%d7%92%27%d7%99%d7%99%d7%9e%d7%a1%20%d7%9e%d7%aa%d7%99%d7%95%20%d7%91%d7%a8%d7%99%2c%20%d7%a1%d7%a4%d7%a8%20%d7%a9%d7%99%d7%a6%d7%90%20%d7%91%d7%a9%d7%a0%d7%aa%201911%20%d7%aa%d7%97%d7%aa%20%d7%94%d7%a9%d7%9d%20%22%d7%a4%d7%99%d7%98%d7%a8%20%d7%95%d6%bc%d7%95%d7%95%d7%a0%d7%93%d7%99%22.%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%aa%20%d7%9e%d7%95%d7%a0%d7%94%2041%20%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%2c%20%d7%95%d7%94%d7%99%d7%90%20%d7%a9%d7%95%d7%93%d7%a8%d7%94%20%d7%91%d7%a9%d7%a0%d7%95%d7%aa%20%d7%94%d7%aa%d7%a9%d7%a2%d7%99%d7%9d%20%d7%91%d7%94%d7%a6%d7%9c%d7%97%d7%94%20%d7%a8%d7%91%d7%94.%20%d7%91%d7%99%d7%9f%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%20%d7%94%d7%93%d7%9e%d7%95%d7%99%d7%95%d7%aa%20%d7%90%d7%a4%d7%a9%d7%a8%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%d7%97%d7%a0%d7%99%20%d7%a0%d7%97%d7%9e%d7%99%d7%90%d7%a1%2c%20%d7%90%d7%a4%d7%99%20%d7%91%d7%9f%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%20%d7%95%d7%a2%d7%95%d7%93%d7%93%20%d7%95%d7%9e%d7%a0%d7%a9%d7%94.%d7%aa%d7%a7%d7%a6%d7%99%d7%a8%20%d7%94%d7%a2%d7%9c%d7%99%d7%9c%d7%94%3a%20%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%2c%20%d7%94%d7%99%d7%9c%d7%93%20%d7%a9%d7%9e%d7%a1%d7%a8%d7%91%20%d7%9c%d7%94%d7%aa%d7%91%d7%92%d7%a8%2c%20%d7%97%d7%99%20%d7%91%d7%90%d7%a8%d7%a5%20%22%d7%9c%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%90%22%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%94%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%94%d7%90%d7%91%d7%95%d7%93%d7%99%d7%9d%20-%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%a9%d7%90%d7%91%d7%93%d7%95%20%d7%9c%d7%94%d7%95%d7%a8%d7%99%d7%94%d7%9d.%20%d7%9e%d7%93%d7%99%20%d7%a4%d7%a2%d7%9d%20%d7%91%d7%a4%d7%a2%d7%9d%2c%20%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%20%d7%9e%d7%92%d7%99%d7%a2%20%d7%9c%d7%a2%d7%95%d7%9c%d7%9e%d7%a0%d7%95%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%94%d7%a7%d7%a9%d7%99%d7%91%20%d7%9c%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%99%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%a9%d7%9e%d7%a1%d7%a4%d7%a8%d7%95%d7%aa%20%d7%90%d7%99%d7%9e%d7%94%d7%95%d7%aa%20%d7%9c%d7%99%d7%9c%d7%93%d7%99%d7%94%d7%9f%20%d7%9c%d7%a4%d7%a0%d7%99%20%d7%94%d7%a9%d7%99%d7%a0%d7%94.%20%d7%9b%d7%9a%20%d7%94%d7%95%d7%90%20%d7%9e%d7%9b%d7%99%d7%a8%20%d7%90%d7%aa%20%d7%95%d7%95%d7%a0%d7%93%d7%99%20%d7%95%d7%90%d7%aa%20%d7%90%d7%97%d7%99%d7%94%2c%20%d7%9e%d7%9c%d7%9e%d7%93%20%d7%90%d7%95%d7%aa%d7%9d%20%d7%9c%d7%a2%d7%95%d7%a3%20%d7%95%d7%9c%d7%95%d7%a7%d7%97%20%d7%90%d7%95%d7%aa%d7%9d%20%d7%9c%d7%98%d7%99%d7%95%d7%9c%20%d7%91%d7%90%d7%a8%d7%a5%20%22%d7%9c%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%90%22%20-%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%a9%d7%91%d7%94%20%d7%9c%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%90%20%d7%9e%d7%aa%d7%91%d7%92%d7%a8%d7%99%d7%9d.%d7%91%d7%93%d7%a8%d7%9a%20%d7%9c%d7%a9%d7%9d%20%d7%95%d7%91%d7%97%d7%96%d7%a8%d7%94%2c%20%d7%94%d7%97%d7%91%d7%95%d7%a8%d7%94%20%d7%a2%d7%95%d7%91%d7%a8%d7%aa%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a8%d7%91%d7%95%d7%aa%3a%20%d7%98%d7%99%d7%a0%d7%a7%d7%a8%d7%91%d7%9c%2c%20%d7%94%d7%a4%d7%99%d7%94%20%d7%a9%d7%9e%d7%a6%d7%98%d7%a8%d7%a4%d7%aa%20%d7%9c%d7%9e%d7%a1%d7%a2%d7%95%d7%aa%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%2c%20%d7%90%d7%99%d7%a0%d7%94%20%d7%9e%d7%97%d7%91%d7%91%d7%aa%20%d7%90%d7%aa%20%d7%95%d7%95%d7%a0%d7%93%d7%99%2c%20%d7%95%d7%9b%d7%9e%d7%95%20%d7%9b%d7%9f%20%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%20%d7%a6%d7%a8%d7%99%d7%9a%20%d7%9c%d7%94%d7%aa%d7%9e%d7%95%d7%93%d7%93%20%d7%a2%d7%9d%20%d7%90%d7%95%d7%99%d7%91%d7%95%20%d7%94%d7%92%d7%93%d7%95%d7%9c%2c%20%d7%a7%d7%a4%d7%98%d7%9f%20%d7%94%d7%95%d7%a7%2c%20%d7%95%d7%a2%d7%9d%20%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%94%d7%a4%d7%99%d7%a8%d7%90%d7%98%d7%99%d7%9d%20%d7%a9%d7%9c%d7%95.%d7%a4%d7%99%d7%98%d7%a8%20%d7%a4%d7%9f%20%d7%94%d7%95%d7%90%20%d7%a7%d7%9c%d7%a1%d7%99%d7%a7%d7%94%20%d7%95%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%a9%d7%a9%d7%95%d7%93%d7%a8%d7%94%20%d7%90%d7%96%2c%20%d7%9c%d7%a4%d7%a0%d7%99%20%d7%9b%d7%a9%d7%a0%d7%99%20%d7%a2%d7%a9%d7%95%d7%a8%d7%99%d7%9d%20%d7%9b%d7%90%d7%9e%d7%95%d7%a8%2c%20%d7%a6%d7%91%d7%a8%d7%94%20%d7%9c%d7%94%20%d7%9e%d7%a2%d7%a8%d7%99%d7%a6%d7%99%d7%9d%20%d7%a8%d7%91%d7%99%d7%9d.%20%d7%9c%d7%9c%d7%90%20%d7%a1%d7%a4%d7%a7%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%aa%d7%a7%d7%91%d7%a6%d7%9d%20%d7%a9%d7%95%d7%91%20%d7%92%d7%9d%20%d7%94%d7%99%d7%95%d7%9d%20%d7%95%d7%9c%d7%94%20%d7%99%d7%a6%d7%98%d7%a8%d7%a4%d7%95%20%d7%9e%d7%a2%d7%a8%d7%99%d7%a6%d7%99%d7%9d%20%d7%97%d7%93%d7%a9%d7%99%d7%9d.%d7%9e%d7%a1%d7%a4%d7%a8%20%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%3a%2041%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%99%d7%9d%3a%20%d7%97%d7%a0%d7%99%20%d7%a0%d7%97%d7%9e%d7%99%d7%90%d7%a1%2c%20%d7%90%d7%a4%d7%99%20%d7%91%d7%9f%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%2c%20%d7%a2%d7%95%d7%93%d7%93%20%d7%9e%d7%a0%d7%a9%d7%94%2c%d7%99%d7%95%d7%a8%d7%9d%20%d7%92%d7%9c%2c%20%d7%94%d7%95%d7%9c%d7%a6%d7%9e%d7%9f%20%d7%a8%d7%95%d7%aa%d7%99%2c%20%d7%a9%d7%9e%d7%95%d7%9c%d7%99%d7%a7%20%d7%99%d7%a4%d7%a8%d7%97%2c%20%d7%9b%d7%94%d7%9f%20%d7%a9%d7%9e%d7%a2%d7%95%d7%9f%2c%20%d7%a0%d7%95%d7%a0%d7%99%20%d7%a4%d7%96%d7%99%d7%aa%2c%20%d7%98%d7%a8%d7%99%d7%a4%d7%95%d7%9f-%d7%a8%d7%a9%d7%a3%20%d7%9b%d7%a0%d7%a8%d7%aa%20%d7%a9%d7%a0%d7%aa%20%d7%94%d7%a4%d7%a7%d7%94%3a%201990&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1000%2fpeter-pan-%d7%a4%d7%99%d7%98%d7%a8-%d7%a4%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL_8KXLhQVQMIMJ_lQkl0Z393wwTtRgg_i') #Hebrew
		list.append('&youtube_pl=PLiDCIQSNnvwc-FqtPLIy3i3i5p0UoB5Fr') #Hebrew
	if 'Haitian' in General_LanguageL:
		list.append('&dailymotion_pl=x3kky6') #קרואלית איטית
	if 'French' in General_LanguageL:
		list.append('&dailymotion_pl=xe92x') #French
		list.append('&dailymotion_pl=x1hqyr') #French
	if 'Italian' in General_LanguageL:
		list.append('&dailymotion_pl=x41cih') #Italian
	addDir(addonString(10267).encode('utf-8'),list,17,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSpAqoUxOIErj3Kgl4053S4oixnvZCcvoJwhf83xupmupsHWKh8',addonString(102670).encode('utf-8'),'1',0,fanart)
	
	'''Pinocchio / פינוקיו'''
	thumb = 'https://www.thetvdb.com/banners/posters/308283-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/308283-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f904.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=904&series_name=%d7%a4%d7%99%d7%a0%d7%95%d7%a7%d7%99%d7%95%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%92%27%d7%a4%d7%98%d7%95%2c%20%d7%94%d7%a0%d7%92%d7%a8%20%d7%94%d7%91%d7%95%d7%93%d7%93%2c%20%d7%92%d7%99%d7%9c%d7%a3%20%d7%9e%d7%91%d7%95%d7%9c%20%d7%a2%d7%a5%20%d7%91%d7%95%d7%91%d7%94%20%d7%a9%d7%a0%d7%99%d7%a2%d7%95%d7%a8%d7%94%20%d7%9c%d7%97%d7%99%d7%99%d7%9d%20%d7%95%d7%94%d7%a4%d7%9b%d7%94%20%d7%9c%d7%91%d7%9f%20%d7%a9%d7%9e%d7%a2%d7%95%d7%9c%d7%9d%20%d7%9c%d7%90%20%d7%94%d7%99%d7%94%20%d7%9c%d7%95.%20%d7%a4%d7%99%d7%a0%d7%95%d7%a7%d7%99%d7%95%20%d7%94%d7%a9%d7%95%d7%91%d7%91%20%d7%a0%d7%a9%d7%9c%d7%97%20%d7%9c%d7%91%d7%99%22%d7%a1%2c%20%d7%90%d7%9a%20%d7%91%d7%a8%d7%97%20%d7%9e%d7%94%d7%91%d7%99%d7%aa%2c%20%d7%95%d7%99%d7%a6%d7%90%20%d7%9c%d7%92%d7%9c%d7%95%d7%aa%20%d7%90%d7%aa%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%95%d7%9c%d7%a2%d7%91%d7%95%d7%a8%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%a8%d7%91%d7%95%d7%aa%20%d7%a2%d7%9d%20%d7%94%d7%91%d7%a8%d7%95%d7%95%d7%96%d7%94%20%d7%91%d7%9c%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f904%2fthe-adventures-of-pinocchio-%d7%a4%d7%99%d7%a0%d7%95%d7%a7%d7%99%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL17BB1526E0625514') #Hebrew
		list.append('&youtube_pl=PLwXEsK85wc0OQV1DgaY4zC0_CiB8ZD5j9') #Hebrew
	addDir(addonString(10480).encode('utf-8'),list,17,thumb,addonString(104800).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104C(General_LanguageL, background, background2) #פלאנט שין
	CATEGORIES104B(General_LanguageL, background, background2) #פריקבוי וצ'אם צ'אם
	
	'''Ninja Turtles / צבי הנינג'ה 1 (1987)''' #NICK (WALLA)
	thumb = 'https://www.thetvdb.com/banners/posters/74582-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/74582-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f636.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=636&series_name=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%20%2a%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&summary=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%20%d7%94%d7%99%d7%90%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%95%d7%a4%d7%a2%d7%95%d7%9c%d7%94%20%d7%a4%d7%95%d7%a4%d7%95%d7%9c%d7%a8%d7%99%d7%aa%20%d7%94%d7%9e%d7%91%d7%95%d7%a1%d7%a1%d7%aa%20%d7%91%d7%9e%d7%a7%d7%95%d7%a8%20%d7%a2%d7%9c%20%d7%a7%d7%95%d7%9e%d7%99%d7%a7%d7%a1%20%d7%9c%d7%9e%d7%91%d7%95%d7%92%d7%a8%d7%99%d7%9d.%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%95%d7%a4%d7%a7%d7%94%20%d7%9c%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%91%d7%9e%d7%a7%d7%95%d7%a8%20%d7%9c%d7%a2%d7%a8%d7%95%d7%a5%20%d7%a1%d7%99%d7%a0%d7%93%d7%99%d7%a7%d7%a6%d7%99%d7%94%2c%20%d7%95%d7%90%d7%97%d7%a8%20%d7%9b%d7%9a%20%d7%a2%d7%91%d7%a8%d7%94%20%d7%9c-CBS.%20%d7%94%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%20%d7%a9%d7%95%d7%93%d7%a8%d7%94%20%d7%91%d7%99%d7%9f%20%d7%94%d7%a9%d7%a0%d7%99%d7%9d%201987%20%d7%9c-1996.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f636%2fteenage-mutant-ninja-turtles-%d7%a6%d7%91%d7%99-%d7%94%d7%a0%d7%99%d7%a0%d7%92-%d7%94-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_id=W7B3NXG0aDY')
		list.append('&youtube_id=E7naeIx3rqo')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78064-4.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78064-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DNinja%20Turtles%3A%20The%20Next%20Mutation%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fninja-turtles-the-next-mutation')
		list.append('&youtube_pl=PL6fJmjt84zZjpEMYCLgX689DlYHAOY5eO') #English
		list.append('&youtube_pl=PLJOXtFyZkYoeQSXGSDHqhuX4Q2P777dl1') #English
		list.append('&youtube_pl=PLwGuYe9NVBWmp2zRCeqAFBCy8IYEPOEd_') #English #S3
	addDir(addonString(10580).encode('utf-8') + space + '1',list,17,thumb,addonString(105800).encode('utf-8'),'1',0,fanart)
	
	'''צבי הנינג'ה 2 (2012)'''
	thumb = 'https://www.thetvdb.com/banners/posters/261451-8.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/261451-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%d7%a2%d7%95%d7%93%20%d7%a4%d7%a8%d7%a7%d7%99%d7%9d&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2594836%26page%3d2')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1670.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1670&series_name=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%3a%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%9e%d7%90%d7%a1%d7%98%d7%a8%20%d7%a6%27%d7%95%d7%a0%d7%92%20%d7%90%d7%99%2c%20%d7%99%d7%93%d7%99%d7%93%d7%95%20%d7%94%d7%95%d7%95%d7%aa%d7%99%d7%a7%20%d7%a9%d7%9c%20%d7%a1%d7%a4%d7%9c%d7%99%d7%a0%d7%98%d7%a8%2c%20%d7%97%d7%95%d7%9c%d7%94%20%d7%9e%d7%90%d7%93.%20%d7%9c%d7%a4%d7%a0%d7%99%20%d7%9e%d7%95%d7%aa%d7%95%2c%20%d7%94%d7%95%d7%90%20%d7%9e%d7%91%d7%a7%d7%a9%20%d7%9e%d7%91%d7%aa%d7%95%20%d7%94%d7%9e%d7%90%d7%95%d7%9e%d7%a6%d7%aa%20%d7%9c%d7%94%d7%aa%d7%90%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92%27%d7%94%20%d7%90%d7%a9%d7%a8%20%d7%91%d7%99%d7%9e%d7%99%d7%9d%20%d7%90%d7%9c%d7%94%20%d7%94%d7%aa%d7%91%d7%92%d7%a8%d7%95%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%94%d7%a6%d7%99%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%90%d7%a0%d7%95%d7%a9%d7%95%d7%aa%20%d7%9e%d7%a4%d7%a0%d7%99%20%d7%93%d7%a8%d7%a7%d7%95%d7%9f-%d7%9c%d7%95%d7%a8%d7%93%2c%20%d7%90%d7%a9%d7%a8%20%d7%94%d7%a9%d7%aa%d7%97%d7%a8%d7%a8%20%d7%9e%d7%90%d7%a8%d7%a5%20%d7%94%d7%97%d7%9c%d7%95%d7%9e%d7%95%d7%aa%20%d7%95%d7%9e%d7%aa%d7%9b%d7%95%d7%95%d7%9f%20%d7%9c%d7%a9%d7%9c%d7%95%d7%98%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d.%20%d7%91%d7%aa%d7%95%20%d7%a9%d7%9c%20%d7%a6%27%d7%95%d7%a0%d7%92%20%d7%90%d7%99%20-%20%d7%9e%d7%99%d7%99%20%d7%95%d7%99%d7%99%20%d7%a6%27%d7%99%20(%d7%90%d7%a9%d7%a8%20%d7%aa%d7%99%d7%a7%d7%a8%d7%90%20%d7%91%d7%a2%d7%aa%d7%99%d7%93%3a%20%d7%95%d7%a0%d7%95%d7%a1%20%d7%93%d7%94%20%d7%9e%d7%99%d7%9c%d7%95)%20%d7%94%d7%99%d7%90%20%d7%9c%d7%9e%d7%a2%d7%a9%d7%94%20%d7%90%d7%97%d7%aa%20%d7%9e%d7%94%d7%a6%d7%91%d7%99%d7%9d%20%d7%a9%d7%a0%d7%a4%d7%9c%d7%95%20%d7%9c%d7%aa%d7%95%d7%9a%20%d7%94%d7%91%d7%a8%d7%99%d7%9b%d7%94%20%d7%94%d7%97%d7%95%d7%9e%d7%a6%d7%aa%d7%99%d7%aa%20%d7%91%d7%99%d7%9c%d7%93%d7%95%d7%aa%d7%94%2c%20%d7%90%d7%9a%20%d7%94%d7%92%d7%99%d7%a2%d7%94%20%d7%9c%d7%a9%d7%a0%d7%97%d7%90%d7%99%20%d7%9b%d7%91%d7%aa%d7%95%20%d7%94%d7%9e%d7%90%d7%95%d7%9e%d7%a6%d7%aa%20%d7%a9%d7%9c%20%d7%a6%27%d7%95%d7%a0%d7%92%20%d7%90%d7%99.%20%d7%91%d7%9e%d7%94%d7%9c%d7%9a%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9c%d7%99%d7%90%d7%95%d7%a0%d7%a8%d7%93%d7%95%2c%20%d7%a8%d7%a4%d7%90%d7%9c%2c%20%d7%9e%d7%99%d7%9b%d7%90%d7%9c%d7%90%d7%a0%d7%92%27%d7%9c%d7%95%2c%20%d7%93%d7%95%d7%a0%d7%98%d7%9c%d7%95%20%d7%95%d7%a1%d7%a4%d7%9c%d7%99%d7%a0%d7%98%d7%a8%20%d7%9e%d7%aa%d7%90%d7%97%d7%93%d7%99%d7%9d%20%d7%a2%d7%9d%20%d7%95%d7%a0%d7%95%d7%a1%2c%20%d7%95%d7%a0%d7%9c%d7%97%d7%9e%d7%99%d7%9d%20%d7%99%d7%97%d7%93%20%d7%91%d7%90%d7%95%d7%99%d7%91%d7%99%d7%94%d7%9d%20%d7%94%d7%97%d7%93%d7%a9%d7%99%d7%9d%20%d7%93%d7%a8%d7%a7%d7%95%d7%9f-%d7%9c%d7%95%d7%93%2c%20%d7%a2%d7%95%d7%96%d7%a8%d7%95%20%d7%95%d7%99%d7%a7%2c%20%d7%91%d7%95%d7%9f-%d7%a1%d7%98%d7%99%d7%9c%2c%20%d7%93%d7%95%d7%a7%d7%98%d7%95%d7%a8%20%d7%a7%d7%95%d7%95%d7%99%d7%96%20%d7%95%d7%94%d7%90%d7%95%d7%99%d7%91%20%d7%94%d7%95%d7%95%d7%aa%d7%99%d7%a7%2c%20%d7%a9%d7%a8%d7%93%d7%a8.%20%d7%9c%d7%90%d7%97%d7%a8%20%d7%a1%d7%95%d7%a3%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%2c%20%d7%94%d7%a6%d7%91%d7%99%d7%9d%20%d7%a0%d7%9c%d7%97%d7%9e%d7%95%20%d7%9c%d7%a6%d7%93%20%d7%94%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%91%d7%a1%d7%93%d7%a8%d7%94%20%22%d7%a4%d7%90%d7%95%d7%95%d7%a8%20%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1%20%d7%91%d7%97%d7%9c%d7%9c%22%20%d7%a0%d7%92%d7%93%20%d7%94%d7%90%d7%95%d7%99%d7%91%d7%aa%20%d7%a9%d7%9c%d7%94%d7%9d%20%d7%90%d7%a1%d7%98%d7%a8%d7%95%d7%a0%d7%9e%d7%94%2c%20%d7%90%d7%a9%d7%a8%20%d7%a9%d7%9c%d7%98%d7%94%20%d7%91%d7%9e%d7%95%d7%97%d7%95%d7%aa%d7%99%d7%94%d7%9d%20%d7%a9%d7%9c%20%d7%94%d7%a6%d7%91%d7%99%d7%9d%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%97%d7%a1%d7%9c%20%d7%90%d7%aa%20%d7%94%d7%a8%d7%99%d7%99%d7%a0%d7%92%27%d7%a8%d7%a1.%20%2a%2a%2a%d7%91%d7%9c%d7%a2%d7%93%d7%99%20%d7%9c%d7%90%d7%aa%d7%a8%20Sdarot.TV%2a%2a%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1670%2fninja-turtles-the-next-mutation-%d7%a6%d7%91%d7%99-%d7%94%d7%a0%d7%99%d7%a0%d7%92-%d7%94-%d7%94%d7%93%d7%95%d7%a8-%d7%94%d7%91%d7%90-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2623650')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?%23039%3b%d7%94%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90&mode=2&module=338&name=%d7%a6%d7%91%d7%99%20%d7%94%d7%a0%d7%99%d7%a0%d7%92&url=http%3a%2f%2fvod.walla.co.il%2ftvshow%2f2623645%2fninja-turtles-the-next-mutation')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F261451-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F261451-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DTeenage%20Mutant%20Ninja%20Turtles%20(2012)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fteenage-mutant-ninja-turtles-2012')
		list.append('&youtube_pl=PL2DB18B47B9E7A3DA') #English
		list.append('&youtube_pl=PL38jdb5xOHbE5ROUr9v1qDFU28Q8XO3RO') #English #S1
		list.append('&youtube_pl=PLjX9hKnb2rTVo7_1slvotGkIExpVEL-nL') #English
		list.append('&youtube_pl=PLjX9hKnb2rTVo7_1slvotGkIExpVEL-nL') #English #S1
		list.append('&youtube_pl=PLjX9hKnb2rTWJsXtTTKIDvHa0swXHEtVT') #English #S4
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLpPLzEufnyNMudPzz__ekbSEdC0_h95c9') #Spanish
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL60657681808C7A03') #French
	addDir(addonString(10580).encode('utf-8') + space + '2',list,17,thumb,addonString(105800).encode('utf-8'),'1',0,fanart)
	
	'''Charlie Brown / צ'ארלי בראון'''
	thumb = 'https://www.thetvdb.com/banners/posters/78225-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78225-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL0JlJB5gdQUHOAfdfCNwzCJt5kvMwDGAP')
		list.append('&youtube_pl=PLeagipoZmyfmLmP1HKhyY-h7-Iwjkk52M')
		
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLMxgaYQNtoym-Ty6CUwpMNdUUPte7cmpU')	
	if 'German' in General_LanguageL:
		list.append('&youtube_id=u-j64okEHCs')		
		
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_id=4SvYGfe-Mqc')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir(addonString(10482).encode('utf-8'),list,17,thumb,addonString(104820).encode('utf-8'),'1',0,fanart)
	
	'''Charlie and Lola / צ'ארלי ולולה'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/75933-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/75933-4.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F75933-4.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F75933-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DCharlie%20and%20Lola%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fcharlie-and-lola')
		list.append('&youtube_pl=PLZQUucKQBgQS8e_kSFvkK7-XVOOl3pk0s')
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PL6fnIGiFPIz2kuqqtCoitGkA_GCA60YPa')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLb2tIcS0W1xX4E67Enb395Ebp_bhkrM6L')
	addDir(addonString(10399).encode('utf-8'),list,17,thumb,addonString(103990).encode('utf-8'),'1',0,fanart)
	
	'''Kung Fu Panda: Legends of Awesomeness / קונג פו פנדה: אגדת המגניבות'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/250632-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/250632-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F250632-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F250632-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DKung%20Fu%20Panda%3A%20Legends%20of%20Awesomeness%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fkung-fu-panda-legends-of-awesomeness')
	addDir(addonString(10373).encode('utf-8'),list,6,thumb,addonString(103730).encode('utf-8'),'1',0,fanart)
	
	'''Casper / קספר'''
	thumb = 'https://www.thetvdb.com/banners/posters/76994-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/76994-2.jpg'
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL-fIrVtK0oZoMiDgF8qocU5yN1Rsr5qKa')
	addDir(addonString(10481).encode('utf-8'),list,17,thumb,addonString(104810).encode('utf-8'),'1',0,fanart)
	
	'''Transformers / רובוטריקים'''
	thumb = 'https://www.thetvdb.com/banners/posters/72499-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/72499-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1395.jpg&mode=3&name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1395&series_name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1395%2ftransformers-hebdub-%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLE509500608BCEB9A') #English
		list.append('&youtube_pl=PLEF9DC7B987249D43') #English
		list.append('&youtube_pl=ELh2QPH8jbzz4') #English
		list.append('&youtube_pl=PLfp_r1A709h-H--XWKvJcD6_ALO5Qt22h') #English
		list.append('&youtube_pl=PL72F5C7FFA297740E') #English #S3 S4
	
	addDir(addonString(10582).encode('utf-8') + space + '1' + space + '(1992)',list,17,thumb,addonString(105820).encode('utf-8'),'1',0,fanart)

	'''Transformers: Prime / רובוטריקים'''
	thumb = 'https://www.thetvdb.com/banners/posters/205901-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/205901-1.jpg'
	plot = "Roll out with Optimus Prime, Bumblebee, Arcee, Ratchet, Bulkhead, and the rest of the heroic Autobots as they battle the evil Decepticons. Now that big bad Megatron has returned with a mysterious and dangerous element, Team Prime must prepare for an epic battle. But that's not so easy when they have to guard over Jack, Miko, and Raf, three normal kids who’ve accidentally discovered the Autobots. As Team Prime works to defend Earth from destruction, the drama gets just as intense as the heavy metal action."
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1451.jpg&mode=3&name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%d7%a4%d7%a8%d7%99%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1451&series_name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%d7%a4%d7%a8%d7%99%d7%99%d7%9d%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1451%2ftransformers-prime-hebdub-%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d-%d7%a4%d7%a8%d7%99%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLpDv_jA6rpIQrDFRGpLv8Er-taOeq7sPR') #English
		list.append('&youtube_pl=PL-j7p6cmFFmwbRdp3lQVX5uEdmtT94zXA') #English
		
	addDir(addonString(10582).encode('utf-8') + space + ': Prime',list,6,thumb,plot,'1',0,fanart)
	
	'''Transformers: Energon / רובוטריקים'''
	thumb = 'https://www.thetvdb.com/banners/posters/72776-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/72776-1.jpg'
	plot = "It's been 10 Earth years since the last battle against Unicron involving him and Megatron disappearing into deep space. The Autobots and Decepticons have been working together and have set up mining post for mining Energon in which to use the Energon to restore Cybertron. But a bad guy called Alpha Q (AKA Alpha Quintesson) has sent a Decepticon named Scorponok and a group of drones called the Terrorcons to raid the mining settlements and steal the Energon so they can restore and power up Unicron and revive Megatron with the help of the Decepticons. But a resurrected Megatron has other plans with Unicron since he has plans to control him. Scorponok and Alpha Q have different plans for Unicron and that is to use Unicron's power to re-create things like his home planet, and destroy Megatron once and for all. It's up to Optimus Prime, the Autobots, and the Omnicons along with a teenage boy n"
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		pass
	
	addDir(addonString(10582).encode('utf-8') + space + ': Energon',list,6,thumb,plot,'1',0,fanart)
	
	'''Transformers: Rescue Bots / רובוטריקים'''
	thumb = 'https://www.thetvdb.com/banners/posters/256349-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/256349-1.jpg'
	plot = "Meet the Rescue Bots! Chase, Heatwave, Blades, and Boulder are given a very important mission by Optimus Prime: Protect and learn about mankind. Stationed undercover on a technologically advanced island called Griffon Rock, they team up with a family of first responders, including a Chief Police Man: Charlie Burns, a Fire Fighter: Kade Burns, a Helicopter Pilot: Dani Burns, and a Construction Engineer: Graham Burns. With help from Cody Burns, the Burns family's youngest, the Rescue Bots keep the peace and keep people safe in their new home. And along the way, they learn what it really means to be a hero."
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	addDir(addonString(10582).encode('utf-8') + space + ' :Rescue Bots',list,6,thumb,plot,'1',0,fanart)
	
	'''Transformers: Robots in Disguise / רובוטריקים'''
	thumb = 'https://www.thetvdb.com/banners/posters/292171-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/292171-5.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1665.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1665&series_name=%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%20%d7%91%d7%94%d7%a1%d7%95%d7%95%d7%90%d7%94%20-%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%9e%d7%99%d7%aa%d7%95%d7%9c%d7%95%d7%92%d7%99%d7%aa%20%d7%97%d7%95%d7%96%d7%a8%d7%aa%20%d7%91%d7%92%d7%a8%d7%a1%d7%94%20%d7%9e%d7%97%d7%95%d7%93%d7%a9%d7%aa%2c%20%d7%9e%d7%95%d7%aa%d7%97%d7%aa%20%d7%99%d7%95%d7%aa%d7%a8%2c%20%d7%9e%d7%a6%d7%97%d7%99%d7%a7%d7%94%20%d7%99%d7%95%d7%aa%d7%a8%20%d7%95%d7%a2%d7%9d%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%97%d7%93%d7%a9.%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%9e%d7%95%d7%a4%d7%99%d7%a2%20%d7%a6%d7%91%d7%90%20%d7%97%d7%93%d7%a9%20%d7%a9%d7%9c%20%d7%a9%d7%a7%d7%a8%d7%a0%d7%99%d7%a7%d7%99%d7%9d%2c%20%d7%90%d7%95%d7%99%d7%91%d7%99%d7%94%d7%9d%20%d7%94%d7%a0%d7%a6%d7%97%d7%99%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%94%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%2c%20%d7%94%d7%9e%d7%90%d7%99%d7%99%d7%9e%d7%99%d7%9d%20%d7%a2%d7%9c%20%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5%20%d7%95%d7%aa%d7%95%d7%a9%d7%91%d7%99%d7%95%20%e2%80%93%20%d7%9e%d7%aa%d7%92%d7%91%d7%a9%20%d7%a6%d7%95%d7%95%d7%aa%20%d7%97%d7%93%d7%a9%20%d7%a9%d7%9c%20%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d%2c%20%d7%91%d7%9e%d7%98%d7%a8%d7%94%20%d7%9c%d7%94%d7%99%d7%9c%d7%97%d7%9d%20%d7%95%d7%9c%d7%a2%d7%a6%d7%95%d7%a8%20%d7%90%d7%aa%20%d7%94%d7%a6%d7%91%d7%90%20%d7%94%d7%9e%d7%a8%d7%95%d7%a9%d7%a2.%20%2a%2a%2a%2a%2a%d7%91%d7%9c%d7%a2%d7%93%d7%99%20%d7%9c%d7%a1%d7%93%d7%a8%d7%95%d7%aa%20%d7%98%d7%99%d7%95%d7%99%2a%2a%2a%2a%2a&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1665%2ftransformers-robots-in-disguise-%d7%a8%d7%95%d7%91%d7%95%d7%98%d7%a8%d7%99%d7%a7%d7%99%d7%9d-%d7%91%d7%94%d7%a1%d7%95%d7%95%d7%90%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL7857F7FC0CE2EC05') #English
		
	addDir(addonString(10582).encode('utf-8') + space + ' :Robots in Disguise',list,6,thumb,addonString(105820).encode('utf-8'),'1',0,fanart)

	'''Alfred J. Kwak / שאלתיאל קוואק'''
	thumb = 'https://www.thetvdb.com/banners/posters/80686-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/80686-4.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://www.thetvdb.com/banners/posters/80686-4.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1137.jpg&mode=3&name=%d7%a9%d7%90%d7%9c%d7%aa%d7%99%d7%90%d7%9c%20%d7%a7%d7%95%d7%95%d7%90%d7%a7%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&series_id=1137&series_name=%d7%a9%d7%90%d7%9c%d7%aa%d7%99%d7%90%d7%9c%20%d7%a7%d7%95%d7%95%d7%90%d7%a7%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2a&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1137%2falfred-j-kwak-%d7%a9%d7%90%d7%9c%d7%aa%d7%99%d7%90%d7%9c-%d7%a7%d7%95%d7%95%d7%90%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PL_8KXLhQVQMKOtRoV1SuOu95dvVo-ea2J') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL5p6VZkX3u2XOrTAP_nmXjms-LWvVBcBts') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLMUK7XxmIwPAAlqAgdewVL-ZhBb8nYop3') #Spanish
		list.append('&youtube_pl=PLr3j2qexlLJknHyg4PhqDolInwT2w_sOe') #Spanish
	if 'Finish' in General_LanguageL:
		list.append('&youtube_pl=PLAI8n3kFtznCVkl-wvK20s5CNZ7X3y2Hr') #Finish
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PL83EB11DD1D5EF206') #German
		list.append('&youtube_pl=PLxrn5FVkko2aSQ1VtJqsCdPeThBy82t26') #German
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL3EF10E10A9956F05') #Dutch
		list.append('&youtube_pl=PLqmrnUMcT7FlnkkfRj9_FsMbxe2cet0lU') #Dutch
		
	addDir(addonString(10583).encode('utf-8'),list,17,thumb,addonString(105830).encode('utf-8'),'1',0,fanart)
	
	'''Marvel's Guardians of the Galaxy / שומרי הגלקסיה'''
	thumb = 'https://www.thetvdb.com/banners/posters/293614-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/293614-6.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F293614-4.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F293614-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMarvel%27s%20Guardians%20of%20the%20Galaxy%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fguardians-of-the-galaxy-2015')
		
	addDir(addonString(10378).encode('utf-8'),list,6,thumb,addonString(103780).encode('utf-8'),'1',0,fanart)
	
	'''Snow White and the Seven Dwarfs / שלגיה ושבעת הגמדים'''
	thumb = 'http://www.coloring4fun.com/wp-content/uploads/2013/03/snow-white-600x300.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL_8KXLhQVQMKKrMMm0glr1TMQoxCjFuTk') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLtgj60MypUp_mvrhlG1TGZteM-HBh_vzv') #English
	addDir(addonString(10589).encode('utf-8'),list,17,thumb,addonString(105890).encode('utf-8'),'1',0,fanart)
	
	'''Dogtanian and the Three Muskehound / שלושת המוסקטרים'''
	thumb = 'https://www.thetvdb.com/banners/posters/74972-7.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/74972-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLyTuZsx2zEs8yu8SWz0FfYxCxKmc6cmVU') #English
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLo1kzli4cgLeBUsyInDov6DqME6y1CvXz') #French
		
	addDir(addonString(10486).encode('utf-8'),list,17,thumb,addonString(104860).encode('utf-8'),'1',0,fanart)
	
	'''Æon Flux'''
	thumb = 'https://www.thetvdb.com/banners/posters/78660-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/78660-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F65%2Fimage%2F555x418%2Faeon-flux.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAeon%20Flux%20(TV%20Series%201991-1995)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Faeon-flux-full-episodes')
		
	addDir(addonString(10348).encode('utf-8'),list,6,thumb,addonString(103480).encode('utf-8'),'1',0,fanart)
	
	'''Andy Pandy'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/256538-1.jpg'
	fanart = 'https://thetvdb.com/banners/fanart/original/256538-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F256538-1.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F256538-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAndy%20Pandy%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fandy-pandy')
		
	addDir(addonString(10392).encode('utf-8'),list,6,thumb,addonString(103920).encode('utf-8'),'1',0,fanart)
	
	'''Angry Birds Toons'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/267834-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/267834-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F267834-3.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F267834-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAngry%20Birds%20Toons%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fangry-birds-toons')
		
	addDir(addonString(10391).encode('utf-8'),list,6,thumb,addonString(103910).encode('utf-8'),'1',0,fanart)
	
	'''Aquaman'''
	thumb = 'https://www.thetvdb.com/banners/posters/82143-6.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/82143-4.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F84%2Fimage%2F555x418%2FAquaman.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DAquaman%20(1968%20TV%20Series)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Faquaman-1968-episodes')
		
	addDir(addonString(10361).encode('utf-8'),list,6,thumb,addonString(103610).encode('utf-8'),'1',0,fanart)
	
	'''A Pup Named Scooby-Doo'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/73546-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/73546-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73546-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73546-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DA%20Pup%20Named%20Scooby-Doo%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fa-pup-named-scooby-doo')
		
	addDir(addonString(10396).encode('utf-8'),list,6,thumb,addonString(103960).encode('utf-8'),'1',0,fanart)

	'''Ben 10'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/79567-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/79567-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F79567-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F79567-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBen%2010%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fben-10')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F9%2Fimage%2F555x418%2FBen-10-Omniverse2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBen%2010%3A%20Omniverse%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fben-10-omniverse')
		
	addDir(addonString(10387).encode('utf-8'),list,6,thumb,addonString(103870).encode('utf-8'),'1',0,fanart)
	
	'''Buzz Lightyear of Star Command'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/72474-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/72474-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72474-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72474-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBuzz%20Lightyear%20of%20Star%20Command%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbuzz-lightyear-of-star-command')
		
	addDir(addonString(10384).encode('utf-8'),list,6,thumb,addonString(103840).encode('utf-8'),'1',0,fanart)
	
	'''Cybersix'''
	thumb = 'https://www.thetvdb.com/banners/posters/77193-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77193-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F251807-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F251807-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGreen%20Lantern%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fgreen-lantern-the-animated-series')
		
	addDir(addonString(10354).encode('utf-8'),list,6,thumb,addonString(103540).encode('utf-8'),'1',0,fanart)
	
	'''DC Super Friends'''
	thumb = 'https://www.thetvdb.com/banners/posters/300228-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/300228-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F70%2Fimage%2F555x418%2Fdc-superfriends.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDC%20Super%20Friends%20(2015%20TV%20Series)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fdc-super-friends-full-episodes')
		
	addDir(addonString(10351).encode('utf-8'),list,6,thumb,addonString(103510).encode('utf-8'),'1',0,fanart)
		
	'''Dragons'''
	thumb = 'https://www.thetvdb.com/banners/posters/261202-5.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/261202-11.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&name_=Race to the Edge&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F61%2Fimage%2F555x418%2Fdragons_race_edge.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DRace%20to%20the%20Edge%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Frace-to-the-edge')
		list.append('&name_=Defenders of Berk&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F60%2Fimage%2F555x418%2FDefenders_of_berk_1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDragons%20Defenders%20of%20Berk%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fdragons-defenders-of-berk')
		list.append('&name_=Riders of Berk&&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F59%2Fimage%2F555x418%2Fdragons-riders-of-berk.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDragons%20Riders%20of%20Berk%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fdragon-riders-of-berk')
		
	addDir(addonString(10345).encode('utf-8'),list,6,thumb,addonString(103450).encode('utf-8'),'1',0,fanart)
	
	'''Ed, Edd n Eddy'''
	thumb = 'https://www.thetvdb.com/banners/posters/77466-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/77466-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F64%2Fimage%2F555x418%2Fed-edd-n-eddy.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DEd%2C%20Edd%20n%20Eddy%20(TV%20Series%201999-2009)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fed-edd-n-eddy-full-episodes')
		
	addDir(addonString(10347).encode('utf-8'),list,6,thumb,addonString(103470).encode('utf-8'),'1',0,fanart)
	
	'''Generator Rex'''
	thumb = 'https://www.thetvdb.com/banners/posters/158551-6.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/158551-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F63%2Fimage%2F555x418%2Fgenerator-rex.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGenerator%20Rex%20(TV%20Series%202010-2013)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fgenerator-rex-tv-series-2010-2013')
		
	addDir(addonString(10346).encode('utf-8'),list,6,thumb,addonString(103460).encode('utf-8'),'1',0,fanart)
	
	'''Green Lantern'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/251807-6.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/251807-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F251807-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F251807-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGreen%20Lantern%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fgreen-lantern-the-animated-series')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F68%2Fimage%2F555x418%2Fgreen-latern.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGreen%20Lantern%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fgreen-lantern-the-animated-series-full-episodes')
		
	addDir(addonString(10377).encode('utf-8'),list,6,thumb,addonString(103770).encode('utf-8'),'1',0,fanart)
	
	'''Police Academy The Animated Series'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/73197-1.jpg'
	fanart = 'https://thetvdb.com/banners/fanart/original/73197-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73197-2.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73197-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DPolice%20Academy%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpolice-academy-the-animated-series')
		
	addDir(addonString(10372).encode('utf-8'),list,6,thumb,addonString(103720).encode('utf-8'),'1',0,fanart)
	
	'''Marvel's Avengers Assemble'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/264030-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/264030-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F264030-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F264030-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMarvel%27s%20Avengers%20Assemble%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Favengers-assemble')
		
	addDir(addonString(10389).encode('utf-8'),list,6,thumb,addonString(103890).encode('utf-8'),'1',0,fanart)
	
	'''Marvel’s Hulk and the Agents of S.M.A.S.H'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/267543-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/267543-12.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F267543-12.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F267543-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMarvel%92s%20Hulk%20and%20the%20Agents%20of%20S.M.A.S.H%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fhulk-and-the-agents-of-s.m.a.s.h.')
		
	addDir(addonString(10376).encode('utf-8'),list,6,thumb,addonString(103760).encode('utf-8'),'1',0,fanart)

	'''Over the Garden Wall'''
	thumb = 'https://www.thetvdb.com/banners/posters/281643-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/281643-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F46%2Fimage%2F555x418%2FOver_the_Garden_Wall_.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DOver%20the%20Garden%20Wall%20(TV%20Miniseries)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fover-the-garden-wall-tv-miniseries')
		
	addDir(addonString(10335).encode('utf-8'),list,6,thumb,addonString(103350).encode('utf-8'),'1',0,fanart)
	
	'''Road Rovers'''
	thumb = 'https://www.thetvdb.com/banners/posters/71526-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/71526-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F72%2Fimage%2F555x418%2Froad-rovers-by-seriojainc.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DRoad%20Rovers%20(TV%20Series%201996-1997)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Froad-rovers-full-episodes')
		
	addDir(addonString(10353).encode('utf-8'),list,6,thumb,addonString(103530).encode('utf-8'),'1',0,fanart)
	
	'''Robin Hood: Mischief in Sherwood'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/288513-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/288513-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F288513-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F288513-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DRobin%20Hood%3A%20Mischief%20in%20Sherwood%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Frobin-hood-mischief-in-sherwood')
		list.append('&youtube_pl=PLzGCiioJcFaZG5a2TTcgeKBQUjx6oqsjF') #English
		
	addDir(addonString(10395).encode('utf-8'),list,17,thumb,addonString(103950).encode('utf-8'),'1',0,fanart)
	
	'''סופרמן'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/71788-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/71788-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F71788-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F71788-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSuperman%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fsuperman-the-animated-series')
		
	addDir(addonString(10370).encode('utf-8'),list,6,thumb,addonString(103700).encode('utf-8'),'1',0,fanart)
	
	'''Frisky Dingo'''
	thumb = 'https://www.thetvdb.com/banners/posters/79930-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/79930-6.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F87%2Fimage%2F555x418%2Ffrisky-dingo.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DFrisky%20Dingo%20(TV%20Series%202006-2008)%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Ffrisky-dingo-full-episodes')
		
	addDir(addonString(10362).encode('utf-8'),list,6,thumb,addonString(103620).encode('utf-8'),'1',0,fanart)
	
	'''Tarzan and Jane'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/322362-1.jpg'
	fanart = 'https://thetvdb.com/banners/fanart/original/322362-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F322362-1.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F322362-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DTarzan%20and%20Jane%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ftarzan-and-jane-2017')
		
	addDir(addonString(10369).encode('utf-8'),list,6,thumb,addonString(103690).encode('utf-8'),'1',0,fanart)
	
	'''The Animals of Farthing Wood'''
	thumb = 'https://thetvdb.com/banners/_cache/posters/74638-1.jpg'
	fanart = 'https://thetvdb.com/banners/fanart/original/74638-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F74638-1.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F74638-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Animals%20of%20Farthing%20Wood%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fanimals-of-farthing-wood')
		
	addDir(addonString(10390).encode('utf-8'),list,6,thumb,addonString(103900).encode('utf-8'),'1',0,fanart)
	
	'''The Best of Mr. Peabody'''
	thumb = 'http://www.cartoonson.com/_resources/Cartoons/show/54/image/555x418/The_Mr._Peabody__Sherman_Show_1959-1962.jpg'
	fanart = 'http://www.cartoonson.com/_resources/Cartoons/show/54/image/555x418/The_Mr._Peabody__Sherman_Show_1959-1962.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F54%2Fimage%2F555x418%2FThe_Mr._Peabody__Sherman_Show_1959-1962.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Best%20of%20Mr.%20Peabody%20%26%20Sherman%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-best-of-mr-peabody-and-sherman')
		
	addDir(addonString(10343).encode('utf-8'),list,6,thumb,addonString(103430).encode('utf-8'),'1',0,fanart)
	
	'''The Buzz on Maggie'''
	thumb = 'http://www.cartoonson.com/_resources/Cartoons/show/83/image/555x418/maggie-the-fly.jpg'
	fanart = 'http://www.cartoonson.com/_resources/Cartoons/show/83/image/555x418/maggie-the-fly.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F83%2Fimage%2F555x418%2Fmaggie-the-fly.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Buzz%20on%20Maggie%20(2005-2006)%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-buzz-on-maggie')
		
	addDir(addonString(10360).encode('utf-8'),list,6,thumb,addonString(103600).encode('utf-8'),'1',0,fanart)
	
	'''The Deep'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/304075-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/304075-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F304075-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F304075-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Deep%20(2016)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-deep-2016')
		
	addDir(addonString(10368).encode('utf-8'),list,6,thumb,addonString(103680).encode('utf-8'),'1',0,fanart)
	
	'''The Mozart Band'''
	thumb = 'https://i1.ytimg.com/sh/Qt0yd__tuiM/showposter.jpg?v=503372e5'
	plot = 'The Mozart Band (original Spanish title, La banda de Mozart) is a 1995 animated television series produced by the BRB Internacional and Marathon Animation studios.'
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=ELkJDYNzDnzgo') #English
		list.append('&youtube_pl=PLL7dcgwYKsm0diDe04UG4TyPRm5p8IS8_') #English
	addDir('The Mozart Band',list,17,thumb,plot,'',58, getAddonFanart(background, custom="https://i.ytimg.com/vi/Us4ZsVZiZjQ/maxresdefault.jpg", default=background2))
	
	'''The New Adventures of Peter Pan'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/266080-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/266080-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F266080-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F266080-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20New%20Adventures%20of%20Peter%20Pan%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-new-adventures-of-peter-pan')
		
	addDir(addonString(10367).encode('utf-8'),list,6,thumb,addonString(103670).encode('utf-8'),'1',0,fanart)
	
	'''The New Adventures of Winnie the Pooh'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/78442-11.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/78442-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78442-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78442-11.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20New%20Adventures%20of%20Winnie%20the%20Pooh%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-new-adventures-of-winnie-the-pooh')
		
	addDir(addonString(10366).encode('utf-8'),list,6,thumb,addonString(103660).encode('utf-8'),'1',0,fanart)
	
	'''The Oblongs'''
	thumb = 'https://www.thetvdb.com/banners/posters/73302-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73302-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F82%2Fimage%2F555x418%2Fthe-obolongs1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Oblongs%20(TV%20Series%202001-2002)%20Episodes%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-oblongs-full-episodes')
		
	addDir(addonString(10359).encode('utf-8'),list,6,thumb,addonString(103590).encode('utf-8'),'1',0,fanart)
	
	'''The Porky Pig Show'''
	thumb = 'http://www.cartoonson.com/_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg'
	fanart = 'http://www.cartoonson.com/_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F80%2Fimage%2F555x418%2Fporky_pig_wallpaper.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Porky%20Pig%20Show%20(1964-1967)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-porky-pig-full-episodes')
		
	addDir(addonString(10358).encode('utf-8'),list,6,thumb,addonString(103580).encode('utf-8'),'1',0,fanart)
	
	'''The Ripping Friends'''
	thumb = 'http://www.cartoonson.com/_resources/Cartoons/show/79/image/555x418/ripping-friends.jpg'
	fanart = 'http://www.cartoonson.com/_resources/Cartoons/show/79/image/555x418/ripping-friends.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F79%2Fimage%2F555x418%2Fripping-friends.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Ripping%20Friends%20(2001-2002)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-ripping-friends-episodes')
		
	addDir(addonString(10357).encode('utf-8'),list,6,thumb,addonString(103570).encode('utf-8'),'1',0,fanart)
	
	'''Scooby's Laff-A Lympics'''
	thumb = 'http://www.cartoonson.com/_resources/Cartoons/show/71/image/555x418/laff-a-lympics1.jpg'
	fanart = 'http://www.cartoonson.com/_resources/Cartoons/show/71/image/555x418/laff-a-lympics1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F71%2Fimage%2F555x418%2Flaff-a-lympics1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DScooby%27s%20Laff-A%20Lympics%20(TV%20Series%201977%E2%80%931979)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fscoobys-laff-a-lympics-full-episodes')
		
	addDir(addonString(10352).encode('utf-8'),list,6,thumb,addonString(103520).encode('utf-8'),'1',0,fanart)
	
	'''SWAT Kats: The Radical Squadron'''
	thumb = 'https://www.thetvdb.com/banners/posters/70545-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/70545-4.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F71%2Fimage%2F555x418%2Flaff-a-lympics1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DScooby%27s%20Laff-A%20Lympics%20(TV%20Series%201977%E2%80%931979)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fscoobys-laff-a-lympics-full-episodes')
		
	addDir(addonString(10355).encode('utf-8'),list,6,thumb,addonString(103550).encode('utf-8'),'1',0,fanart)
	
	'''Recess'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/71780-3.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/71780-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F71780-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F71780-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DRecess%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Frecess')
		
	addDir(addonString(10371).encode('utf-8'),list,6,thumb,addonString(103710).encode('utf-8'),'1',0,fanart)
	
	'''Walt Disney Cartoons*'''
	thumb = 'http://thetvdb.com/banners/fanart/original/72514-4.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.supercartoons/?image=C%3a%5cUsers%5cgal%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.supercartoons%5cresources%5cartwork%5ccharacters.png&mode=400&page=1&title=Characters')
	list.append('&custom4=plugin://plugin.video.supercartoons/?mode=100&title=Kids+Time+%2810+Random+Cartoons%29&image=C%3A%5CUsers%5Cgal%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.supercartoons%5Cresources%5Cartwork%5Ckidstime.png&page=1')
	list.append('&youtube_pl=PLhGipfv0juZWh-OMeXOvJ-Ibt9wZtdJK1') #English
	list.append('&youtube_pl=PL7spvnQF9O-j1qnZLPTyLYfmQAifdSfN9') #English
	list.append('&youtube_pl=PL7spvnQF9O-hVKRHmNu8uTJeNF5mr6oGj') #English
	list.append('&youtube_id=OM6xvpzqCUA') #English
	list.append('&youtube_id=Q8AZ16uBhr8') #English
	list.append('&youtube_id=2n7UgwWGUeQ') #English
	list.append('&youtube_id=1-x1kz3OHvw') #English
	list.append('&youtube_id=-VbQoS7O4Ls') #English
	list.append('&youtube_id=8Qa_OCHDsOc') #English
	list.append('&youtube_id=xLZhlP-PQ5A') #English
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72514-4.jpg&iconimage=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fb%2Fbd%2FLooney_Tunes_Golden_Collection_-_Volume_4.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DLooney%20Tunes%20Golden%20Collection%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Flooney-tunes-golden-collection')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72514-19.jpg&iconimage=http%3A%2F%2Fimages2.static-bluray.com%2Fmovies%2Fcovers%2F101211_front.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DLooney%20Tunes%20Platinum%20Collection%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Flooney-tunes-platinum-collection')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F248368-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F248368-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Looney%20Tunes%20Show%20(2011)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-looney-tunes-show-2011')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL7spvnQF9O-gzBQghS5lQ9T6kmU3CExZw') #Spanish
	addDir('Walt Disney Cartoons',list,17,thumb,'','plugin.video.supercartoons',58, getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/72514-4.jpg", default=background2))
	
	'''Yo Yogi!'''
	thumb = 'https://www.thetvdb.com/banners/posters/73471-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/73471-2.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F47%2Fimage%2F555x418%2FYo_Yogi_.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DYo%20Yogi!%20(TV%20Series%201991-1992)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fyo-yogi-tv-series-1991-1992')
		
	addDir(addonString(10336).encode('utf-8'),list,6,thumb,addonString(103360).encode('utf-8'),'1',0,fanart)
	
	'''Young Justice'''
	thumb = 'https://www.thetvdb.com/banners/posters/192061-10.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/192061-12.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F69%2Fimage%2F555x418%2FYoung_Justice.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DYoung%20Justice%20(2010%20TV%20Series)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fyoung-justice-full-episodes')
		
	addDir(addonString(10350).encode('utf-8'),list,6,thumb,addonString(103500).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES104A(General_LanguageL, background, background2) #עמוד הבא הצגות ילדים
	
def CATEGORIES105(name, iconimage, desc, fanart):
	background = 105
	background2 = "" #http://4.bp.blogspot.com/-Af2HcIQzlg8/UhwQ8lKPucI/AAAAAAAACIA/d7aY4RrxUfk/s1600/bambi-friends-disney-animated-movie-photo.jpg"
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES105Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	CATEGORIES105B(General_LanguageL, background, background2) #סרטים לילדים ב-
	CATEGORIES105C(General_LanguageL, background, background2) #סרטים עם תרגום ב-
	CATEGORIES105A(General_LanguageL, background, background2) #עמוד הבא סרטים
	
def CATEGORIES106(name, iconimage, desc, fanart):
	'''לפעוטות'''
	background = 106
	background2 = "" #http://1.bp.blogspot.com/-MnUXpmW1n1M/UKfOgAXUmXI/AAAAAAAAbBY/BfoQ1FNgNUk/s1600/duvcar1024x768_en_27.jpg"
	
	'''אקראי'''
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES106Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	
	'''ערוצי טלוויזיה'''
	
	CATEGORIES106F(General_LanguageL, background, background2) #אוליבר
	
	'''אוצר מילים עם נוני'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLErYJg2XgxyXmgk6cyROtlJh2g-Fk_T6n')
		list.append('&youtube_pl=PLD6olaR57ZFlhTg5XRloT_rbJ8VgjlDsp')
		list.append('&youtube_id=hu7Wa2URXi4')
		list.append('&youtube_id=zSHKufiJvL4')
	if 'English' in General_LanguageL:
		pass
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLI3Ou6qeL8cutZ2J0QOw8c1t7Ee0coj8b')
		list.append('&youtube_pl=PLqYzUBrrH-OtK-g_DUdPV0_suL-cbcbZE')
		list.append('&youtube_pl=PLJW3gU5Gp3s1YKMixqWNl_CaILIRCI1wi')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLnc7YfgjG-D-R4By7CzjnL-XvakeClrFW')
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL85EfYJjPp_DCOSmJGpuK89OCRrMPYS6n')
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=PLxfqqYFhVYmGv1sYp5DXj1kyXrmT8B4pI')

	addDir(addonString(10602).encode('utf-8'),list,17,'http://i.ytimg.com/vi/m67adbe1SOg/0.jpg',addonString(106020).encode('utf-8'),'1',0,fanart)
	
	'''בואלה וקואלה*'''
	thumb = ''
	fanart = 'https://lh5.ggpht.com/Yq719nfYOCeafMVVZwlL7TONN1gxd4jKhkE9L4YcKwViWdBhAEi-WEeLBboTtQFOGGc=h900'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL63295318280A7354')
		list.append('&youtube_pl=PL4F7EE458D510EE96')
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL8F17B3FB69BA627F')
		list.append('&youtube_pl=PL0E88F6019272E685')
		
	
	addDir(addonString(10611).encode('utf-8'),list,17,'http://ww1.prweb.com/prfiles/2006/08/14/424791/uptotenBoowaKwala.jpg',addonString(106110).encode('utf-8'),'1',0,fanart)
	
	'''בייבי איינשטיין*'''
	thumb = 'https://yt3.ggpht.com/-aRd660Gwyzg/AAAAAAAAAAI/AAAAAAAAAAA/_1rP7GM5bvk/s288-c-k-no-mo-rj-c0xffffff/photo.jpg'
	fanart = 'https://images-na.ssl-images-amazon.com/images/I/71PRm7SiSnL._SL1500_.jpg'
	list = []

	list.append('&youtube_pl=PLk2f9iGbtyhsJBj1PVTo54k51hfGClZVb') #Arts
	list.append('&youtube_pl=PLk2f9iGbtyhuwYb9Y4BPGzUiktRUrANZI') #Animals
	list.append('&youtube_pl=PLk2f9iGbtyhtBkgeCknuMEdaVz65ZAgrE') #Music
	list.append('&youtube_pl=PLk2f9iGbtyhvc_8g9aTKHofXLaZ8dEo43') #Nature
	
	addDir(addonString(10603).encode('utf-8'),list,17,thumb,addonString(106030).encode('utf-8'),'1',0,fanart)
	
	'''בילי בם בם'''
	CATEGORIES106D(General_LanguageL, background, background2)
	
	'''בינג'''
	thumb = 'https://i.ytimg.com/vi/HWq9EuKkimI/hqdefault.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqJ4NDGmEMQXirjzWpATU1-3')
	addDir('בינג',list,17,thumb,'','1',0,fanart)
	
	'''ברנרד*'''
	thumb = 'https://www.thetvdb.com/banners/posters/80029-4.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/80029-5.jpg'
	list = []
	list.append('&youtube_pl=PLegWv2p63OBOSDqXOiBigHgsq_Ep2kaKY')
	list.append('&youtube_pl=PLKLzBLbyOE9vMP4ZQaylo9gst_fgVTS01')
	list.append('&youtube_pl=PLKLzBLbyOE9u1GYfAp6BL_e5zLmlTGoYP')
	addDir(addonString(10615).encode('utf-8'),list,17,thumb,addonString(106150).encode('utf-8'),'1',0,fanart)
	
	'''גילגולון'''
	thumb = 'https://i.ytimg.com/vi/JH8wKDynqNY/hqdefault.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqJpX20e1Twkc18L3a5neRMl')
	addDir('גילגולון',list,17,thumb,'','1',0,fanart)
	
	'''דביבוני בונבוני'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqJ8NnaZsoLeuWiQLYaEarDu')
	addDir('דביבוני בונבוני',list,17,'https://i.ytimg.com/vi/ZUXYkF9uQNY/hqdefault.jpg','','1',0,fanart)
	
	CATEGORIES106G(General_LanguageL, background, background2) #דובוני אכפת לי (חדש)
	
	'''דובים ונהנים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqIaAW5pDJO8ThJ_rrohsRLE')
	addDir(addonString(10617).encode('utf-8'),list,17,'http://luli.tv/Img/Albums/556/medium/%D7%93%D7%95%D7%91%D7%99%D7%9D-%D7%95%D7%A0%D7%94%D7%A0%D7%99%D7%9D3.jpg',addonString(106170).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES106E(General_LanguageL, background, background2) #דרקו	
	
	'''Dinopaws*'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/278713-1.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/278713-3.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F278713-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F278713-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDinopaws%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdinopaws')
		list.append('&youtube_pl=PLCI_BIMJR-XFv8VwHFKt1R3LCPMKqbraf')
		list.append('&youtube_id=Vo2N47-NFPQ&t=573s')
		list.append('&youtube_id=rkjrQ7oMpg0')
		
	addDir(addonString(10610).encode('utf-8'),list,17,thumb,addonString(106100).encode('utf-8'),'1',0,fanart)
	
	'''הגלופסים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2593551')
		
	addDir(addonString(10624).encode('utf-8'),list,17,'http://msc.walla.co.il/w/w-160/1448200-29.jpg',addonString(106240).encode('utf-8'),'1',0,fanart)
	
	'''הארי הארנב'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLnraPnhPHcc7NZwbC41nphBAe-1jxXVSN')
		list.append('&youtube_id=DvYvtAoKye0')
	addDir(addonString(10618).encode('utf-8'),list,17,'https://i.ytimg.com/vi/_GASnq3zBuE/hqdefault.jpg',addonString(106180).encode('utf-8'),'1',0,fanart)
	
	'''הגן הקסום'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqITKBrRwiH7gr_BEzC8d7qU')
	addDir('הגן הקסום',list,17,'http://simania.co.il/bookimages/covers64/644273.jpg','','1',0,fanart)
	
	CATEGORIES107L(General_LanguageL, background, background2) #דוק רופאת הצעצועים
	
	'''הכבשה שושנה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2819037&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2819043&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2819050&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2817560&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2817583&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2817533&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2820067&mode=10&module=wallavod')
		list.append('&youtube_pl=PLC47880737B43FF96')
	addDir(addonString(10619).encode('utf-8'),list,17,thumb,addonString(106190).encode('utf-8'),'1',0,fanart)
	
	'''הנימנונמים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2556132')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f873.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=873&series_name=%d7%94%d7%a0%d7%99%d7%9e%d7%a0%d7%95%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-hanimnumim%2fseason%2f1&summary=%d7%a1%d7%93%d7%a8%d7%94%20%d7%94%d7%9e%d7%99%d7%95%d7%a2%d7%93%d7%aa%20%d7%9c%d7%92%d7%99%d7%9c%20%d7%94%d7%a8%d7%9a.%20%d7%a9%d7%9c%d7%95%d7%a9%20%d7%91%d7%95%d7%91%d7%95%d7%aa%20%d7%9b%d7%95%d7%9b%d7%91%20(%d7%a0%d7%99%d7%9e%d7%95%2c%20%d7%9e%d7%95%d7%a0%d7%94%20%d7%95%d7%9e%d7%99%d7%9d)%20%d7%97%d7%99%d7%95%d7%aa%20%d7%91%d7%a9%d7%9e%d7%99%d7%99%d7%9d%20%d7%91%d7%99%d7%9f%20%d7%94%d7%a2%d7%a0%d7%a0%d7%99%d7%9d%2c%20%d7%95%d7%a2%d7%95%d7%a1%d7%a7%d7%95%d7%aa%20%d7%91%d7%a9%d7%90%d7%9c%d7%94%20%d7%94%d7%9e%d7%92%d7%99%d7%a2%d7%94%20%d7%9c%d7%90%d7%95%d7%96%d7%a0%d7%99%d7%94%d7%9d%20%d7%9e%d7%97%d7%93%d7%a8%d7%95%20%d7%a9%d7%9c%20%d7%99%d7%9c%d7%93%2c%20%d7%a9%d7%92%d7%a8%20%d7%91%d7%9b%d7%93%d7%95%d7%a8%20%d7%94%d7%90%d7%a8%d7%a5.%20%d7%90%d7%91%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%94%d7%99%d7%9c%d7%93%20%d7%91%d7%93%d7%99%d7%95%d7%a7%20%d7%9e%d7%a1%d7%99%d7%99%d7%9d%20%d7%9c%d7%a1%d7%a4%d7%a8%20%d7%9c%d7%95%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%20-%20%d7%a9%d7%aa%d7%9e%d7%99%d7%93%20%d7%9e%d7%a1%d7%aa%d7%99%d7%99%d7%9d%20%d7%91%d7%a9%d7%90%d7%9c%d7%94%2c%20%d7%90%d7%99%d7%aa%d7%94%20%d7%9e%d7%aa%d7%9e%d7%95%d7%93%d7%93%d7%99%d7%9d%20%d7%94%d7%a0%d7%99%d7%9e%d7%a0%d7%95%d7%9e%d7%99%d7%9d.%20&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f873%2f%d7%94%d7%a0%d7%99%d7%9e%d7%a0%d7%95%d7%9e%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-hanimnumim%2fseason%2f1')
	addDir(addonString(10620).encode('utf-8'),list,6,thumb,addonString(106200).encode('utf-8'),'1',0,fanart)
	
	'''הפוני הקטן שלי'''
	thumb = ''
	fanart = 'http://thetvdb.com/banners/fanart/original/212171-14.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLdzmRSlbGryE9L5scgIBO34txlYgb1Jk_')
		list.append('&youtube_id=https://www.youtube.com/watch?v=MXn5_kRMums')
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F212171-14.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F212171-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMy%20Little%20Pony%3A%20Friendship%20Is%20Magic%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmy-little-pony-friendship-is-magic')
		list.append('&youtube_pl=PLAWEtMG6fBxBBUuPekG_KXaMYX3wA9EPW')
		list.append('&youtube_pl=PLAWEtMG6fBxDSWB3kuK13fba-CTHDse08')
		
	addDir(addonString(10625).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/212171-5.jpg',addonString(106250).encode('utf-8'),'1',0,fanart)
	
	'''ויפו הכלב המעופף'''
	CATEGORIES106C(General_LanguageL, background, background2)

	'''זובומפו zoboomafoo'''
	thumb = ''
	fanart = 'http://i.huffpost.com/gen/2271948/images/o-ZOBOOMAFOO-DEAD-facebook.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=UCgkPirt3MeBXLJ82Q5Rue-w') 
	addDir('zoboomafoo',list,17,'http://images.techtimes.com/data/images/full/25401/zoboomafoo2-jpg.jpg?w=600','','1',0,fanart)
	
	'''זומזומים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqLCFVU5Jtu1c76X0fT3KNG4')
	addDir('זומזומים',list,17,'https://i.ytimg.com/vi/nhqjS1EKsW8/hqdefault.jpg','','1',0,fanart)
	
	''''''
	
	'''טונקי'''
	
	'''טוקטוק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqKkr82pGJe-bk1pMMxFg_b-')
	addDir('טוקטוק',list,17,'https://i.ytimg.com/vi/Cv7uEqCzgDk/hqdefault.jpg','','1',0,fanart)
	
	'''טיגה וטוגה'''
	thumb = ''
	fanart = ''
	list = []
	
	'''טין טן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqIJm4WwQGG8pIJ5OeUAsFN9')
	addDir('טין טן',list,17,'https://i.ytimg.com/vi/Qa9JAroeS4I/hqdefault.jpg','','1',0,fanart)
	
	'''טיפה טופה'''
	thumb = ''
	fanart = ''
	list = []
	
	'''יש לנחש עם חן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=iNxcJ2GNJgA')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f883.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=883&series_name=%d7%99%d7%a9-%d7%9c%d7%a0%d7%97%d7%a9-%d7%a2%d7%9d-%d7%97%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-yesh-lenahesh%2fseason%2f1&summary=%d7%97%d7%9f%20%d7%94%d7%95%d7%90%20%d7%97%d7%aa%d7%9c%d7%aa%d7%95%d7%9c%20%d7%97%d7%9e%d7%95%d7%93%20%d7%95%d7%a1%d7%a7%d7%a8%d7%9f%2c%20%d7%a9%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9e%d7%97%d7%a4%d7%a9%20%d7%aa%d7%a9%d7%95%d7%91%d7%95%d7%aa%20%d7%9c%d7%a9%d7%90%d7%9c%d7%95%d7%aa%20%d7%a2%d7%9c%20%d7%a4%d7%9c%d7%90%d7%99%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%94%d7%a1%d7%95%d7%91%d7%91%20%d7%90%d7%95%d7%aa%d7%95.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f883%2f%d7%99%d7%a9-%d7%9c%d7%a0%d7%97%d7%a9-%d7%a2%d7%9d-%d7%97%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-yesh-lenahesh%2fseason%2f1')
	addDir('יש לנחש עם חן',list,17,thumb,'','1',"",fanart)
	
	'''מוסטי'''
	thumb = ''
	fanart = ''
	list = []
	
	'''מיילו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqJI6GrNCJO9yjyXbZHS9X-F')
	if 'French' in General_LanguageL:
		list.append('&youtube_id=0oFDMV7OlUE')
		list.append('&dailymotion_id=x6ibte')
		list.append('&dailymotion_id=x6jo89')

	addDir(addonString(10616).encode('utf-8'),list,17,'https://i.ytimg.com/vi/Us7tmcvl01w/hqdefault.jpg',addonString(106160).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES106H(General_LanguageL, background, background2) #מיפי
	
	'''מספרי משימה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLn0MlLMGvwMVJrWgO028RM6UJrax1ItDr')
	
	addDir('מספרי משימה',list,17,'http://i.ytimg.com/vi/DjUCZgrL8cY/hqdefault.jpg',addonString(106000).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES106I(General_LanguageL, background, background2) #פוקיו
	
	'''פים ופימבה*'''
	thumb = ''
	fanart = ''
	list = []
	list.append('&youtube_pl=PLvIdvaV3orE-FmApmbSoDRXPVnlNW5TAS')
	list.append('&youtube_pl=PLTNonj9ImqaI2F7DHlMxZ3VDn8gwpaTKe')
	list.append('&youtube_pl=PLaorT66MlVdw0Ebw7cVh44jKZUQZjMbfJ')
	list.append('&youtube_pl=PLxXOTs-eZ3U4MB90gIXs7OzGyvY6l260K')
	
	list.append('&youtube_pl=PLXpVk0zgung3azsj24E2V1pkcsP8xAjDA') #English
	
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLCya5IM-g-FHu4jlq53yXU0FcnxWfX3U1')
	addDir(addonString(10638).encode('utf-8'),list,17,'http://msc.wcdn.co.il/archive/941107-54.jpg',addonString(106380).encode('utf-8'),'1',58,fanart)
	
	'''פיצי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL5kivPlEfMCTa3yiShQstAKsvzsdZIbkx')
		list.append('&youtube_id=FKRVfhMczq8')
	addDir(addonString(10647).encode('utf-8'),list,17,'http://i.ytimg.com/vi/Y02LzkHJ_Uk/hqdefault.jpg',addonString(106470).encode('utf-8'),'1',0,fanart)
	
	'''פראגל רוק'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/139151-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/139151-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F139151-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F139151-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DFraggle%20Rock%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ffraggle-rock')
	if 'Spanish' in General_LanguageL:
		pass
	addDir(addonString(10380).encode('utf-8'),list,6,thumb,addonString(103800).encode('utf-8'),'1',"",fanart)
	
	'''צוות צבע'''
	thumb = 'https://s-media-cache-ak0.pinimg.com/236x/cd/1b/b4/cd1bb434a41ed5449675dc8e3bc0b2fa.jpg'
	fanart = 'https://i.ytimg.com/vi/5y4KQA2cUCQ/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		fanart = 'https://i.ytimg.com/vi/A5A76OjQgkY/maxresdefault.jpg'
		list.append('&youtube_pl=PLnraPnhPHcc5UHxWzmRs2Bk73ehPTfF6c')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLqsYSvVJ2b7FMUey_eHPu5KYhqdqJRERw')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_id=2kySIhYzIb4')
		list.append('&youtube_id=3FgxKAIQfyU')
	addDir(addonString(10656).encode('utf-8'),list,17,thumb,addonString(106560).encode('utf-8'),'1',"",fanart)
	
	'''צ'רלי ודודו'''
	list = []
	thumb = ''
	fanart = ''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqK3NlYz7T3fz6XGRfTVk2FH')
		list.append('&youtube_id=k-bXuLHXDU4')
	addDir(addonString(10657).encode('utf-8'),list,17,'https://i.ytimg.com/vi/QLtv1_pibW8/hqdefault.jpg',addonString(106570).encode('utf-8'),'1',0,fanart)
	''''''
	
	'''קוקו הארנב'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqLxJd-fvXvoQFuxMXBt8k1g')
		list.append('&youtube_id=WIug1uuY3OM')
	addDir(addonString(10661).encode('utf-8'),list,17,'http://www.luli.tv/Img/Albums/377/medium/koko.jpg',addonString(106610).encode('utf-8'),'1',0,fanart)
	
	'''קטני'''
	thumb = ''
	fanart = 'http://ecx.images-amazon.com/images/I/91h3597ypWL._SL1500_.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLbHXbhgZi5cL97NlobjLHNtBwIA9VHcmw') #קטני
		
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL004FC6C7ABCC0EB6') #קטני
		list.append('&youtube_pl=PLgrW7n7d9dGhal0a58isK-zn6dutfDtYO') #קטני
		list.append('&youtube_pl=PL569CDAE96B5E3F55') #קטני
		list.append('&youtube_pl=PLXpYKJNcYOf23gX6NX4oEAakBjoKtcTVN') #קטני
		
		
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLporszkvR1VfMzI9-XGFpgB0Nk_d5FcUj') #קטני
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLD03iNFvg_Iu6zly-qEhAu6UVEGkDxC6X') #קטני
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLaeO-USZ2EjxD1hW8atjt4dG6YWfEd9ov') #קטני
	
		
	addDir(addonString(10662).encode('utf-8'),list,17,'http://ecx.images-amazon.com/images/I/51cnuhgYF7L.jpg',addonString(106620).encode('utf-8'),'1',58, fanart)
	
	'''קמי'''
	thumb = ''
	fanart = ''
	list = []
	
	'''קרוסלת הקסמים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqLUEkMOnwJQhkETZikw27J5')
	addDir('קרוסלת הקסמים',list,17,'https://i.ytimg.com/vi/zxcbz-Ix8aU/hqdefault.jpg','','1',0,fanart)
	
	'''שבט גולו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqIuUXjhWsQI1LpD2jFs7Doj')
	addDir('שבט גולו',list,17,'https://i.ytimg.com/vi/J58qhUyUtzg/hqdefault.jpg','','1',0,fanart)
	
	'''תולי האהוב'''
	thumb = ''
	fanart = ''
	list = []
	
	'''תפודים קטנים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqILDjwXEF1zHTBwzbmnA-HT')
	addDir('תפודים קטנים',list,17,'https://i.ytimg.com/vi/8HVk4ODOl8g/hqdefault.jpg','','1',0,fanart)
	
	'''Tinga Tinga Tales'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/142731-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/142731-1.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F142731-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F142731-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DTinga%20Tinga%20Tales%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ftinga-tinga-tales')
		
	addDir(addonString(10663).encode('utf-8'),list,6,thumb,addonString(106630).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES106A(General_LanguageL, background, background2) #עמוד הבא פעוטות
	
def CATEGORIES107(name, iconimage, desc, fanart):
	background = 107
	background2 = ""
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES107Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	
	'''***'''
	thumb = ''
	fanart = 'https://i.ytimg.com/vi/iibZa2tbGEg/maxresdefault.jpg'
	list = []
	list.append('&youtube_ch=UCDZgrBvmY6tXt8gb4Z-7w9A') #Jude Bryant
	list.append('&youtube_ch=UCvTHynhs6QldpcAJ_a3jl5g') #Kids Funny Cars Toons
	list.append('&youtube_ch=UCtsIgvwaT1icVCi0Xbv1s0A') #Colors Kids TV
	addDir('-' + 'Suprize Party :)',list,17,"http://www.bestsurpriseeggvideos.com/wp-content/uploads/2015/12/24-surprise-eggs-unboxing-LPS-My-Little-PONY-The-SMURFS-Party-Animals-Shrek-Disney-eggs-Compilatio-750x400.jpeg","I don't know why.. but kids are loving it :)",'1',0,fanart)
	
	CATEGORIES107D(General_LanguageL, background, background2) #אדיבו
	
	CATEGORIES107I(General_LanguageL, background, background2) #צוות אומי זומי
	
	CATEGORIES107J(General_LanguageL, background, background2) #ארמון החיות
	
	'''בגינה של לין'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%90%d7%95%d7%9e%d7%99%20%d7%96%d7%95%d7%9e%d7%99&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1744439')
		list.append('&youtube_pl=PLPWc8VdaIIsDcjHMTBavJG-Rm8p0wvvW_')
	addDir(addonString(10705).encode('utf-8'),list,17,'http://img.youtube.com/vi/lQt9W6DU5dQ/0.jpg',addonString(107110).encode('utf-8'),'1',"",fanart)
	
	'''ג'ורג׳ הסקרן'''
	thumb = ''
	fanart = 'http://thetvdb.com/banners/fanart/original/79429-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		#list.append('&youtube_id=LGiMNrwwH4Y')
	
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F79429-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F79429-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DCurious%20George%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fcurious-george')
	addDir(addonString(10716).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/79429-5.jpg',addonString(107160).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES107C(General_LanguageL, background, background2) #קטנטנים - בוב הבנאי
	CATEGORIES107S(General_LanguageL, background, background2) #קטנטנים - בוב הבנאי+
	
	'''בומבה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=BumbaKanaal/playlists')
		list.append('&youtube_pl=PLITCTw1CghePbU3EjP9D3qcRCOHFkJmJ1')
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=ChaineDeBumba/playlists')
		
	addDir(addonString(10703).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Bumba-plopsaindoor.jpg/266px-Bumba-plopsaindoor.jpg',addonString(107030).encode('utf-8'),'1',"",fanart)
	
	'''בחצר של פופיק'''
	thumb = ''
	fanart = 'https://i.ytimg.com/vi/pE28_ALY-lE/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2015%2f08%2f30%2fpupik_yard_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fpupik-yard-s1')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f883.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=883&series_name=%d7%99%d7%a9-%d7%9c%d7%a0%d7%97%d7%a9-%d7%a2%d7%9d-%d7%97%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-yesh-lenahesh%2fseason%2f1&summary=%d7%97%d7%9f%20%d7%94%d7%95%d7%90%20%d7%97%d7%aa%d7%9c%d7%aa%d7%95%d7%9c%20%d7%97%d7%9e%d7%95%d7%93%20%d7%95%d7%a1%d7%a7%d7%a8%d7%9f%2c%20%d7%a9%d7%99%d7%97%d7%93%20%d7%a2%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9e%d7%97%d7%a4%d7%a9%20%d7%aa%d7%a9%d7%95%d7%91%d7%95%d7%aa%20%d7%9c%d7%a9%d7%90%d7%9c%d7%95%d7%aa%20%d7%a2%d7%9c%20%d7%a4%d7%9c%d7%90%d7%99%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%94%d7%a1%d7%95%d7%91%d7%91%20%d7%90%d7%95%d7%aa%d7%95.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f883%2f%d7%99%d7%a9-%d7%9c%d7%a0%d7%97%d7%a9-%d7%a2%d7%9d-%d7%97%d7%9f-%d7%9e%d7%93%d7%95%d7%91%d7%91-yesh-lenahesh%2fseason%2f1')
		list.append('&youtube_pl=PLth1a195qHsiYX3v_ICFAlJtnG5Yr4J0-')
	addDir('בחצר של פופיק',list,17,'http://img.mako.co.il/2016/03/07/kids_420X600_pupik_yard.jpg',addonString(108990).encode('utf-8'),'1',0,fanart)
	
	'''בלייז ומכוניות הענק'''
	thumb = ''
	fanart = 'http://4.bp.blogspot.com/-lzXysVf6vg0/UyINE-X3B3I/AAAAAAAAXXs/XCoe51pywtw/s1600/Blaze_and_the_Monster_Machines_Nickelodeon_Preschool_Nick_Jr.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%91%d7%9c%d7%99%d7%99%d7%96%20%d7%95%d7%9e%d7%9b%d7%95%d7%a0%d7%99%d7%95%d7%aa%20%d7%94%d7%a2%d7%a0%d7%a7&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2868092')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLcj83Ngp_IlMC0eE45W0FBily_QmTtgMQ')
		list.append('&youtube_pl=')
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL3qHjxSSl7AHN2XTwmBo-zD4rM4m0re19')	
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLhsTwJBjtycgz2VmCTX-hkemfrB-vpiau')
		list.append('&youtube_pl=PLy4w2NOU7fm5HcLNdv0yFrBoE7YG9JJrm')
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PLAyhcT8ZqFWNIWMFjt7l3LqJq0StcHocj')
	addDir(addonString(10708).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Blaze_and_the_Monster_Machines_logo.png/250px-Blaze_and_the_Monster_Machines_logo.png',addonString(107080).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES107E(General_LanguageL, background, background2) #דובי קטן
	
	'''ברבונסקי'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLqjVAzhugdWLoyjj0vJz405G-hS74QL1P')
		list.append('&youtube_pl=PLqjVAzhugdWK-f5YBHgywxM-6t-DvDjWN')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLogBXxHVJONDRWSpXcDV6qK9nM_WP-q_n')
		list.append('&youtube_pl=PLogBXxHVJONDRWSpXcDV6qK9nM_WP-q_n')
		list.append('&youtube_id=j4tavakwmcg')
	addDir(addonString(10710).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/ru/4/4d/%D0%91%D0%B0%D1%80%D0%B1%D0%BE%D1%81%D0%BA%D0%B8%D0%BD%D1%8B.png',addonString(107100).encode('utf-8'),'1',0,fanart)
	
	'''דוח דלעת'''
	thumb = ''
	fanart = 'https://i.ytimg.com/vi/q-1z1VdRXp0/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLR7DTcU2p0QhuQU-SWBGtywN6Zt1bapZt') #Hebrew
	addDir(addonString(10714).encode('utf-8'),list,17,'http://juniortv.co.il/wp-content/uploads/2015/08/EP008_Still_004-825x510.jpg',addonString(107140).encode('utf-8'),'1',0,fanart)
	
	'''דורה וחברים'''
	thumb = ''
	fanart = 'http://www.trbimg.com/img-53ee62bb/turbine/la-et-st-dora-and-friends-into-the-city-review-20140815'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%93%d7%95%d7%a8%d7%94%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%9d&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2831952')
		list.append('&custom4=http://62.90.90.56/walla_vod/_definst_/mp4:media/015/242/1524273-40.mp4/playlist.m3u8')
		list.append('&youtube_id=-aeSQFWB1pA')
		list.append('&youtube_id=zbSxLv4HH3I')
		list.append('&youtube_id=_CbY8wBblCw')
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2015-04-17dora-and-friends-into-the-city-y.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D43853389a93dbcf030c79b161177de52b6409c05-1481270506-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Dora%20and%20Friends%3A%20Into%20the%20City!%20Season%201%20(2014)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F1771%2Fdora-and-friends-into-the-city-%2F&name_=Season 1&')
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2016-02-05dora-and-friends-into-the-city-season-2-2016y.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D43853389a93dbcf030c79b161177de52b6409c05-1481270506-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Dora%20and%20Friends%3A%20Into%20the%20City!%20Season%202%20(2016)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F9780%2Fdora-and-friends-into-the-city-season-2-2016%2F&name_Season 2&')
		list.append('&youtube_id=3TQAy66Mpug')
		list.append('&youtube_pl=PLYUPX95OFYmglVK0H8V6pQYWv7xCgCLwA')
		list.append('&youtube_pl=PLwC1cnFbggP0lFxJboaw8moC5qj_P2V0f')
		list.append('&youtube_pl=EL1q_Il1879aRo4teP2it5Cg')
		
	addDir(addonString(10711).encode('utf-8'),list,17,'http://www.2bdaddy.co.il/wp-content/uploads/unnamed-25.jpg',addonString(107110).encode('utf-8'),'1',0,fanart)
	
	'''דינוזאורים'''
	thumb = ''
	fanart = 'http://thetvdb.com/banners/fanart/original/76461-6.jpg'
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76461-6.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F76461-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDinosaurs%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdinosaurs')
	addDir(addonString(10397).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/76461-6.jpg',addonString(103970).encode('utf-8'),'1',0,fanart)
	
	'''דינו דן'''
	thumb = ''
	fanart = 'http://images.nickjr.com/nickjr/properties/dino-dan/property-header-dino-dan-desktop-portrait-2x.png?quality=0.75'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL0zAFNbEotfkBCaGmpE0PHyRDjk7yOkgv')
	addDir('דינו דן',list,17,'http://www.hop.co.il/wp-content/uploads/2015/07/%D7%93%D7%99%D7%A0%D7%95%D7%96%D7%90%D7%95%D7%A8%D7%99%D7%9D-%D7%91%D7%94%D7%95%D7%A4.png','','1',0,fanart)
	
	'''דר דוור'''
	thumb = ''
	fanart = 'http://thetvdb.com/banners/fanart/original/83719-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1577.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1577&series_name=%d7%93%d7%9f-%d7%94%d7%93%d7%95%d7%95%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-postman-pat%2fseason%2f1&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%9e%d7%93%d7%95%d7%91%d7%91%d7%aa%2c%20%d7%95%d7%91%d7%9e%d7%a8%d7%9b%d7%96%d7%94%20%d7%94%d7%92%d7%99%d7%91%d7%95%d7%a8%20%d7%94%d7%a8%d7%90%d7%a9%d7%99%20-%20%d7%93%d7%9f%20%d7%a7%d7%9c%d7%99%d7%a4%d7%98%d7%95%d7%9f%2c%20%d7%94%d7%93%d7%95%d7%95%d7%a8%20%d7%a9%d7%9c%20%d7%9b%d7%a4%d7%a8%20%d7%94%d7%a2%d7%9e%d7%a7.%d7%93%d7%9f%2c%20%d7%90%d7%a9%d7%aa%d7%95%20%d7%a9%d7%a8%d7%94%2c%20%d7%91%d7%a0%d7%9d%20%d7%90%d7%95%d7%a8%d7%9f%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%a0%d7%95%d7%a1%d7%a4%d7%99%d7%9d%20%d7%9e%d7%9b%d7%a4%d7%a8%20%d7%94%d7%a2%d7%9e%d7%a7%2c%20%d7%a4%d7%95%d7%aa%d7%a8%d7%99%d7%9d%20%d7%9b%d7%9c%20%d7%91%d7%a2%d7%99%d7%94%20%d7%94%d7%a0%d7%99%d7%a6%d7%91%d7%aa%20%d7%91%d7%a4%d7%a0%d7%99%d7%94%d7%9d%2c%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%97%d7%a9%d7%99%d7%91%d7%94%20%d7%97%d7%99%d7%95%d7%91%d7%99%d7%aa%2c%20%d7%95%d7%94%d7%aa%d7%97%d7%a9%d7%91%d7%95%d7%aa%20%d7%9e%d7%aa%d7%9e%d7%93%d7%aa%20%d7%91%d7%96%d7%95%d7%9c%d7%aa.%d7%93%d7%9f%20%d7%9e%d7%a2%d7%95%d7%a8%d7%91%20%d7%91%d7%97%d7%99%d7%99%20%d7%9b%d7%a4%d7%a8%20%d7%94%d7%a2%d7%9e%d7%a7%2c%20%d7%94%d7%95%d7%90%20%d7%95%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9e%d7%a0%d7%a1%d7%99%d7%9d%20%d7%9c%d7%a2%d7%96%d7%95%d7%a8%20%d7%96%d7%94%20%d7%9c%d7%96%d7%94%20%d7%91%d7%93%d7%a8%d7%9b%d7%99%d7%9d%20%d7%99%d7%a6%d7%99%d7%a8%d7%aa%d7%99%d7%95%d7%aa%2c%20%d7%94%d7%9d%20%d7%a0%d7%90%d7%9e%d7%a0%d7%99%d7%9d%20%d7%95%d7%a1%d7%95%d7%91%d7%9c%d7%a0%d7%99%d7%99%d7%9d%20%d7%90%d7%97%d7%93%20%d7%9b%d7%9c%d7%a4%d7%99%20%d7%94%d7%a9%d7%a0%d7%99.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1577%2f%d7%93%d7%9f-%d7%94%d7%93%d7%95%d7%95%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-postman-pat%2fseason%2f1')
		list.append('&youtube_pl=PL_8KXLhQVQMK05YV3wTQ4SZyEo2kWDvNH')
	
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F83719-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F83719-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DPostman%20Pat%3A%20Special%20Delivery%20Service%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpostman-pat-special-delivery-service')
		list.append('&youtube_pl=PLaeuNQbB1tFI7ShCF4nwUDGP5wTHJyGPl')
		list.append('&youtube_pl=PLjfYltP-bYWL49ewqpIB3W4I4sP-kxAqb')
		list.append('&youtube_pl=PLpRBkxy1E2MGvrVUYAdPMOJjDm5Bh_ny6')
		
	addDir(addonString(10712).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/83719-2.jpg','','1',0,fanart)

	'''דן ומוזלי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2015%2f07%2f23%2fdan_muzli_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fdan-and-muzli-s1')
	addDir(addonString(10713).encode('utf-8'),list,6,'http://img.mako.co.il/2015/07/23/dan_muzli_f.jpg','','1',0,fanart)
	
	'''דן מדען'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=_RaEmzVsXuc')
		list.append('&youtube_id=pWAW2WIveb4')
		list.append('&youtube_id=W4BgnDYJoI8')
		list.append('&youtube_id=tb0PCFSwWjA')
	addDir('דן מדען',list,17,'http://www.ishim.co.il/i/9/929.jpg','','1',0,fanart)
	
	'''הדוד חיים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTNonj9ImqaIuFt2AyqdYFx6bCnKoFsIc')
		list.append('&youtube_id=VQLASGxELwc')
		list.append('&youtube_id=5yOKydYwMmk')
	addDir(addonString(10715).encode('utf-8'),list,17,'http://www.yap.co.il/prdPics/4298_desc3_2_2_1390119036.jpg',addonString(107150).encode('utf-8'),'1',0,fanart)
	
	'''הופלה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLfcYs4SRZfuI2EVify6lL8SwUc11oJ_UL')
	addDir('הופלה',list,17,'https://i.ytimg.com/vi/JJ7ZxtIBzCI/default.jpg','','1',0,fanart)
	
	'''הורים וגורים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL51YAgTlfPj5sp5nUKFuwuUddCXYjiH8F')
	addDir(addonString(10717).encode('utf-8'),list,17,'https://i.ytimg.com/vi/2QOPSd1hKhQ/default.jpg',addonString(107200).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES107H(General_LanguageL, background, background2) #החברים של ברני
	CATEGORIES107O(General_LanguageL, background, background2) #החיוך של רוזי
	
	'''היי בינבה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1142.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1142&series_name=%d7%94%d7%99%d7%99-%d7%91%d7%99%d7%a0%d7%91%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-bumpety-boo%2fseason%2f1&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9e%d7%aa%d7%9e%d7%a7%d7%93%d7%aa%20%d7%91%d7%91%d7%95%d7%91%d7%99%2c%20%d7%a0%d7%a2%d7%a8%20%d7%a6%d7%a2%d7%99%d7%a8%20%d7%90%d7%a9%d7%a8%20%d7%97%d7%9c%d7%9d%20%d7%aa%d7%9e%d7%99%d7%93%20%d7%a2%d7%9c%20%d7%9e%d7%9b%d7%95%d7%a0%d7%99%d7%aa%20%d7%9e%d7%a9%d7%9c%d7%95%20%d7%95%d7%91%d7%91%d7%99%d7%a0%d7%91%d7%94%2c%20%d7%9e%d7%9b%d7%95%d7%a0%d7%99%d7%aa%20%d7%a6%d7%94%d7%95%d7%91%d7%94%20%d7%a7%d7%98%d7%a0%d7%94%20%d7%95%d7%9e%d7%93%d7%91%d7%a8%d7%aa%20%d7%a9%d7%91%d7%a7%d7%a2%d7%94%20%d7%9e%d7%aa%d7%95%d7%9a%20%d7%91%d7%99%d7%a6%d7%94%20%d7%9e%d7%95%d7%96%d7%a8%d7%94%20%d7%91%d7%aa%d7%95%d7%9a%20%d7%9e%d7%a9%d7%97%d7%98%d7%aa%20%d7%a8%d7%9b%d7%91.%20%d7%91%d7%95%d7%91%d7%99%2c%20%d7%90%d7%a9%d7%a8%20%d7%a9%d7%95%d7%9e%d7%a2%20%d7%90%d7%95%d7%aa%d7%94%20%d7%91%d7%95%d7%9b%d7%94%2c%20%d7%99%d7%95%d7%a6%d7%90%20%d7%9c%d7%a2%d7%96%d7%a8%d7%aa%d7%94%20%d7%a8%d7%92%d7%a2%20%d7%9c%d7%a4%d7%a0%d7%99%20%d7%a9%d7%94%d7%99%d7%90%20%d7%a0%d7%94%d7%a8%d7%a1%d7%aa%2c%20%d7%95%d7%9e%d7%90%d7%96%20%d7%94%d7%9d%20%d7%a0%d7%a2%d7%a9%d7%99%d7%9d%20%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%98%d7%95%d7%91%d7%99%d7%9d.%20%d7%91%d7%99%d7%a0%d7%91%d7%94%2c%20%d7%91%d7%95%d7%91%d7%99%20%d7%95%d7%94%d7%9b%d7%9c%d7%91%20%d7%a9%d7%9c%d7%95%2c%20%d7%a4%d7%95%d7%a0%d7%a4%d7%95%d7%9f%20%d7%99%d7%95%d7%a6%d7%90%d7%99%d7%9d%20%d7%99%d7%97%d7%93%d7%99%d7%95%20%d7%9c%d7%9e%d7%a1%d7%a2%20%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa%20%d7%91%d7%a2%d7%95%d7%9c%d7%9d%20%d7%91%d7%9e%d7%98%d7%a8%d7%94%20%d7%9c%d7%9e%d7%a6%d7%95%d7%90%20%d7%90%d7%aa%20%d7%90%d7%9e%d7%94%d6%bc%20%d7%a9%d7%9c%20%d7%91%d7%99%d7%a0%d7%91%d7%94.%20%d7%94%d7%9d%20%d7%a0%d7%90%d7%9c%d7%a6%d7%99%d7%9d%20%d7%9c%d7%94%d7%aa%d7%97%d7%9e%d7%a7%20%d7%9e%d7%96%d7%a2%d7%9d%20%d7%94%d7%a8%d7%a9%d7%a2%20%d7%a9%d7%9e%d7%a0%d7%a1%d7%94%20%d7%9c%d7%aa%d7%a4%d7%95%d7%a1%20%d7%90%d7%aa%20%d7%91%d7%99%d7%a0%d7%91%d7%94%20%d7%91%d7%9b%d7%9c%20%d7%94%d7%96%d7%93%d7%9e%d7%a0%d7%95%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1142%2f%d7%94%d7%99%d7%99-%d7%91%d7%99%d7%a0%d7%91%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-bumpety-boo%2fseason%2f1')
		list.append('&youtube_pl=PLsCZljh6GgKUyE7rFV66powMC1H7XrXx3')
		list.append('&youtube_id=YUNtUxIc708')
	addDir(addonString(10719).encode('utf-8'),list,6,thumb,addonString(107190).encode('utf-8'),'1',0,fanart)
	
	'''הרפתקאות הלו קיטי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLsu9uBjRGa__a0Mj54uZl25lod_e1_9A9')
		list.append('&youtube_pl=PL-_BcMXVkaspyjwz7S5Hs_Rgih0F1d8_d')
		list.append('&youtube_pl=PLfcYs4SRZfuI1H_eTSxA61k7_-zUOQIqC')
	
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLy_oDopn4AKRnE4OMtOX_yn3kDjg1yRvv')
	
	addDir(addonString(10721).encode('utf-8'),list,17,'http://www.ligdol.co.il/Upload/hello%20kitty285.jpg',addonString(107210).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES107K(General_LanguageL, background, background2) #הנסיכה סופייה
	
	'''הסוד של מיה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%94%d7%a1%d7%95%d7%93%20%d7%a9%d7%9c%20%d7%9e%d7%99%d7%94&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1688505')
		list.append('&youtube_pl=PLPWc8VdaIIsCGEVOC2iJxnWNEjI13xbnA')
	addDir(addonString(10723).encode('utf-8'),list,17,'http://msc.wcdn.co.il/w-2-1/w-300/768225-54.jpg',addonString(107230).encode('utf-8'),'1',0,fanart)
	
	'''הרמזים של בלו'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492577-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492577-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%94%d7%a8%d7%9e%d7%96%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%91%d7%9c%d7%95&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1764817')
	addDir('הרמזים של בלו',list,17,thumb,"",'1',0,fanart)
	
	'''הרפתקאות פיטר הארנב'''
	thumb = ''
	fanart = 'http://thetvdb.com/banners/fanart/original/267185-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLfcYs4SRZfuLix_YttCD6wumoY6IihOKQ')
		list.append('&youtube_pl=PLwSKZ4wsGYZGAAvTj9qWRz9S-7GfusSZ7')
		
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLkgGhNvMiBBq8bSAqYKZ0zeI5auB0qJnu')
		list.append('&youtube_pl=PLkgGhNvMiBBqXusYRqb43sOgrsT4te7bi')
		list.append('&youtube_id=YUfrUExon0s')
		list.append('&youtube_id=N8JsjlMSLUo')
		list.append('&youtube_id=LMN6UckXUGE')
		list.append('&youtube_id=RmpR4Qs5CdU')
		list.append('&youtube_id=5s_rP-diU3M')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F267185-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F120621-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20World%20of%20Peter%20Rabbit%20and%20Friends%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpeter-rabbit')
		
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL0UFi8iC0JNjS4_7sCE3VrhjYVLt_se2p')
		list.append('&youtube_id=nKa2S_RtWMY')
		list.append('&youtube_id=VIPr6R4AWIM')
		list.append('&youtube_id=PE1v84f_hXk')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir(addonString(10724).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/120621-1.jpg',addonString(107240).encode('utf-8'),'1',0,fanart)
	
	'''זמן לזוז'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492582-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492582-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%96%d7%9e%d7%9f%20%d7%9c%d7%96%d7%95%d7%96&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2696342')
	addDir(addonString(10725).encode('utf-8'),list,17,thumb,addonString(107250).encode('utf-8'),'1',0,fanart)
	
	'''וונדה והחייזר'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492578-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492578-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%95%d7%95%d7%a0%d7%93%d7%94%20%d7%95%d7%94%d7%97%d7%99%d7%99%d7%96%d7%a8&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2854550')
	
	addDir('וונדה והחייזר',list,17,thumb,"",'1',0,fanart)
	
	'''וונדר פטס'''
	thumb = 'https://img.wcdn.co.il/f_auto,w_200/2/4/9/2/2492579-46.jpg'
	fanart = 'https://img.wcdn.co.il/f_auto,w_200/2/4/9/2/2492579-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%95%d7%95%d7%a0%d7%93%d7%a8%20%d7%a4%d7%98%d7%a1&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1724550')
	addDir(addonString(10741).encode('utf-8'),list,17,thumb,addonString(107410).encode('utf-8'),'1',0,fanart)
	
	'''ויקי וג'וני'''
	thumb = ''
	fanart = 'https://i.ytimg.com/vi/498POdZHRDA/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLegWv2p63OBNcqEDI7eVkARiWIbtbUZUS')
		list.append('&youtube_pl=PLE27B67D526863479')
	
	addDir(addonString(10726).encode('utf-8'),list,17,'https://i.ytimg.com/vi/fPnWeHeSxjw/mqdefault.jpg',addonString(107260).encode('utf-8'),'1',0,fanart)
	
	'''ורדינון אמן הילדים'''
	thumb = 'http://www.myfirsthomepage.co.il/mfhp/image/tv/vardinon.jpg'
	fanart = 'https://i.ytimg.com/vi/9YVBM63Lr00/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UC5ZXek-PKBbys-xIt1FliMQ')
	
	addDir(addonString(10788).encode('utf-8'),list,17,thumb,addonString(107880).encode('utf-8'),'1',0,fanart)
	
	'''זאק וקוואק'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492580-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492580-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%95%d7%95%d7%a0%d7%93%d7%a8%20%d7%a4%d7%98%d7%a1&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1724550')
		list.append('&youtube_pl=PL_8KXLhQVQMJM70o-LA7S6ufWVvLCJF9m')
		
	addDir('זאק וקוואק',list,17,thumb,'','1',0,fanart)
	
	'''זהבית ופזית'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492581-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492581-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%96%d7%94%d7%91%d7%99%d7%aa%20%d7%95%d7%a4%d7%96%d7%99%d7%aa&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2920425')
		
	addDir(addonString(10743).encode('utf-8'),list,17,thumb,addonString(107430).encode('utf-8'),'1',0,fanart)
	
	'''חבורת 7ג'''
	thumb = 'http://www.disney.co.il/disney-channel/sites/default/files/local_territories/il-IL/hero_slides/il_7D_brs_gbl_1.png'
	fanart = 'http://img3.wikia.nocookie.net/__cb20140709082318/disney/images/a/a4/The_7D.png'
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLe-Na2ky4G0AeFESccRuVngVs5dF7HtDe')
				
	addDir(addonString(10738).encode('utf-8'),list,17,thumb,addonString(107380).encode('utf-8'),'1',0,fanart)
	
	'''חבורת הגופים'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492583-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492583-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%97%d7%91%d7%95%d7%a8%d7%aa%20%d7%94%d7%92%d7%95%d7%a4%d7%99%d7%9d&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2518204')
	
	if 'English' in General_LanguageL:
		pass
				
	addDir(addonString(10753).encode('utf-8'),list,17,thumb,addonString(107530).encode('utf-8'),'1',0,fanart)
	
	'''חבורת החצר'''
	thumb = 'https://i.ytimg.com/vi/LXhoQcLeyt0/mqdefault.jpg'
	fanart = 'https://i.ytimg.com/vi/jOYv12AcqMA/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLn92uhkZaRGwsVJc7EaCsZAWnD_AZW02o')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLYpg2jvVNY-PfH6fm_Erv0aIn-BPhnL5x&index')
				
	addDir(addonString(10739).encode('utf-8'),list,17,thumb,addonString(107390).encode('utf-8'),'1',0,fanart)
	
	'''טימותי הולך לבית הספר'''
	list = []
	thumb = 'http://www.musicaneto.com/wp-content/themes/musica-mod/js/timthumb.php?src=http://www.musicaneto.com/wp-content/uploads/2014/02/7290014697874.jpg&w=183&h=250'
	fanart = 'https://i.ytimg.com/vi/JXHpZieVam8/maxresdefault.jpg'
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1736.jpg&mode=3&name=%d7%98%d7%99%d7%9e%d7%95%d7%aa%d7%99-%d7%94%d7%95%d7%9c%d7%9a-%d7%9c%d7%91%d7%99%d7%aa-%d7%94%d7%a1%d7%a4%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-timothy-goes-to-school%2fseason%2f1&series_id=1736&series_name=%d7%98%d7%99%d7%9e%d7%95%d7%aa%d7%99-%d7%94%d7%95%d7%9c%d7%9a-%d7%9c%d7%91%d7%99%d7%aa-%d7%94%d7%a1%d7%a4%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-timothy-goes-to-school%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1736%2f%d7%98%d7%99%d7%9e%d7%95%d7%aa%d7%99-%d7%94%d7%95%d7%9c%d7%9a-%d7%9c%d7%91%d7%99%d7%aa-%d7%94%d7%a1%d7%a4%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-timothy-goes-to-school%2fseason%2f1')
		list.append('&youtube_pl=PLtE3COCsPAWm5JRiKxtfQjUEVy7YiVUMO')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLyJA77GdW64bIjAcK-N9oIEdqStHqjXLL') #English
		list.append('&youtube_pl=PLyJA77GdW64YTdJSP4jIy1GclZ82KcSqq') #English
	addDir(addonString(10728).encode('utf-8'),list,17,thumb,addonString(107280).encode('utf-8'),'1',0,fanart)	
	
	'''טימי טיים*'''
	thumb = ''
	fanart = ''
	list = []
	list.append('&youtube_pl=PLnw_wYZBfzuMvORLwC7HYsR2qpxXeZucu') #TIMMY TIME
	list.append('&youtube_pl=PLLkqDC9xIu8Z7Aflrjr9SVbULT-42942l')
	list.append('&youtube_pl=PLnw_wYZBfzuNfTcbuUfPrDov2jC8APZk0')
	list.append('&youtube_id=_vb2lCx36bA')
	
	addDir(addonString(10732).encode('utf-8'),list,17,'http://blog.tapuz.co.il/drrd/images/662689_1158.jpg',addonString(107320).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://ichef.bbci.co.uk/childrens-responsive-ichef/r/720/1x/cbeebies/cbeebies-timmytime-img-timmytimegroup_432_243.jpg", default=background2))
	
	'''טל והטלטלים'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492585-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492585-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%98%d7%9c%20%d7%95%d7%94%d7%aa%d7%9c%d7%aa%d7%9c%d7%99%d7%9d&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2947159')
	if 'English' in General_LanguageL:
		pass
				
	addDir(addonString(10754).encode('utf-8'),list,17,thumb,addonString(107540).encode('utf-8'),'1',0,fanart)
	
	'''טלטאביז'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTleo-h9TFqLYGm9ibuEYE-4kUMvb7vHw')
		list.append('&youtube_pl=PLBDE473A2E30EE847')
		list.append('&youtube_id=TGmpQKg2NtQ')
		list.append('&youtube_id=mAlgerULqyU')
		list.append('&youtube_id=3cJYHKsa52E')
		list.append('&youtube_id=BOzl3RHn4Io')
		list.append('&youtube_id=VZzivZvWidI')
		list.append('&youtube_id=NN_gqjA8jJQ')
		list.append('&youtube_id=AL0RVZMr-VY') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_id=C_Km9NYD-Pw') #English
		list.append('&youtube_id=d_zk--Iconw') #English
		list.append('&youtube_id=d3yfZlIUwF4')
		list.append('&youtube_id=GUWpiwVZ-gI')
		list.append('&youtube_id=wTm5rDg8tqI')
		list.append('&youtube_id=1E9Z0-ppTl0')
		list.append('&youtube_id=JdKoA4lIENc')
		list.append('&youtube_id=GI4j0xDtU5Y')
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLiYnki7YcURvX8um3QXUYBflo7nPajnG3') #טלטאביז
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL58leaokT4HSFmnwtRrjvXQg9SZqnjsaG') #טלטאביז
		list.append('&youtube_pl=PLGmqLSExAs-IEWUaGV7T4usQeWG0KpsMx')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLS6A4SYN00LYYloR80D1aubcjcEO0o376') #טלטאביז
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL718qI31wRq9nDjjDvBvLzFo3SxpKve-p') #טלטאביז
	addDir(addonString(10729).encode('utf-8'),list,17,'http://ia.media-imdb.com/images/M/MV5BMjE3MDcyMjcxN15BMl5BanBnXkFtZTYwNDQzNTQ5._V1_UX182_CR0,0,182,268_AL_.jpg',addonString(107290).encode('utf-8'),'1',0,fanart)
	
	'''טום הטרקטור*'''
	thumb = 'https://i.ytimg.com/vi/M0o7XHPxKeE/maxresdefault.jpg'
	fanart = 'https://i.ytimg.com/vi/M0o7XHPxKeE/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
	if 'English' in General_LanguageL:
		list.append('&youtube_id=RSkO-UDe0yg')
		list.append('&youtube_id=Q28RkBLRnF0')

	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL7888E4250CBA46CA') #טום הטרקטור
		list.append('&youtube_id=lPXDH3JRyuw')
		list.append('&youtube_pl=PLdAOY_vKneiCyW2fL6qpc_Qkhiyr-BvPU')
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLdAOY_vKneiA-HbHaL2Xh8V4FGz_oCZt3') #טום הטרקטור
		list.append('&youtube_pl=')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_id=HrozQ_qBqWk')
		list.append('&youtube_id=IToAJBRgUJ0')
		
		
		list.append('&youtube_pl=') #טום הטרקטור
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=') #טום הטרקטור
	
	addDir(addonString(10733).encode('utf-8'),list,17,thumb,addonString(107330).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יובל המבולבל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=7yuval')
		list.append('&youtube_pl=PLzAqQoYm2t2xi_8LMKWYVfW0DjchcSzv0')
		list.append('&youtube_pl=PLfcYs4SRZfuIrU-AvQvAoJ01gW-EnlfHw')
	addDir('יובל המבולבל',list,17,'http://images1.ynet.co.il/PicServer3/2013/05/29/4652192/3977474099288408529no.jpg',addonString(107310).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.ashdodnet.com/dyncontent/t_post/2012/7/24/26370203843604787436.jpg", default=background2))
	
	'''יצירה בקצרה'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492588-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492588-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%99%d7%a6%d7%99%d7%a8%d7%94%20%d7%91%d7%a7%d7%a6%d7%a8%d7%94&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2656308')
		list.append('&youtube_pl=PLPWc8VdaIIsC0SPM0_dgOVIDn5vcCH8Ti')
		list.append('&youtube_pl=PLPWc8VdaIIsD85fRihIJFTzwt9v_JX2t6')
	addDir('יצירה בקצרה',list,17,thumb,addonString(107340).encode('utf-8'),'1',0,fanart)
	
	'''כח הקצב'''
	thumb = 'http://www.yap.co.il/prdPics/257_desc3_3_2_1341484277.jpg'
	fanart = 'http://www.yap.co.il/prdPics/big_867_preview_file.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLXXwLmObrlLp9gaoOaDKurj0EYkj4YcW6')
		list.append('&youtube_pl=PL80p1yIa4Vwb-C2hIlvvb5qb5B0rm18yA')
		
	addDir('כח הקצב',list,17,thumb,'','1',0,fanart)
	
	'''מגלים עם דורה'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/74697-5.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/74697-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%9e%d7%92%d7%9c%d7%99%d7%9d%20%d7%a2%d7%9d%20%d7%93%d7%95%d7%a8%d7%94&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f1688309')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f855.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=855&series_name=%d7%9e%d7%92%d7%9c%d7%99%d7%9d-%d7%a2%d7%9d-%d7%93%d7%95%d7%a8%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-dora-the-explorer%2fseason%2f1&summary=%d7%93%d7%95%d7%a8%d7%94%20%d7%94%d7%99%d7%9c%d7%93%d7%94%20%d7%a9%d7%9e%d7%9c%d7%9e%d7%93%d7%aa%20%d7%90%d7%95%d7%aa%d7%a0%d7%95%20%d7%90%d7%a0%d7%92%d7%9c%d7%99%d7%aa%20%d7%91%d7%a6%d7%95%d7%a8%d7%94%20%d7%a9%d7%9b%d7%99%d7%a3%20%d7%9c%d7%9c%d7%9e%d7%95%d7%93%20%d7%91%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f855%2f%d7%9e%d7%92%d7%9c%d7%99%d7%9d-%d7%a2%d7%9d-%d7%93%d7%95%d7%a8%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-dora-the-explorer%2fseason%2f1')
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F74697-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F74697-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDora%20the%20Explorer%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdora-the-explorer')

	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLLk0B1a2FT0apXz3ZVHdZ-QprLGuwrU_S')
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL3qHjxSSl7AG4pvTCQWLA97yw10nNspZB')
		list.append('&youtube_id=6q3_SCXFX0U')
		list.append('&youtube_id=rhduMp-AB7Y')
		
		
	addDir(addonString(10740).encode('utf-8'),list,6,thumb,addonString(107400).encode('utf-8'),'1',0,fanart)
	
	'''מולי וצומי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2077.jpg&mode=3&name=%d7%9e%d7%95%d7%9c%d7%99-%d7%95%d7%a6%d7%95%d7%9e%d7%99-muli-and-tzumi%2fseason%2f1&series_id=2077&series_name=%d7%9e%d7%95%d7%9c%d7%99-%d7%95%d7%a6%d7%95%d7%9e%d7%99-muli-and-tzumi%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2077%2f%d7%9e%d7%95%d7%9c%d7%99-%d7%95%d7%a6%d7%95%d7%9e%d7%99-muli-and-tzumi%2fseason%2f1')
	addDir(addonString(10742).encode('utf-8'),list,17,'http://www.yap.co.il/prdPics/4309_desc3_2_1_1390393153.jpg',addonString(107420).encode('utf-8'),'1',0,fanart)
	
	'''מיילס מהמחר'''
	thumb = ''
	fanart = 'http://cdnvideo.dolimg.com/cdn_assets/30d9ad46a7c968160f425855f200136ab610fb3e.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLVwL64lSxWWxwkyH-xdNi5bfgyJ_UcudA')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL1fY_FCMpjVJd2U25MFEfgjR9lx-VUntI')
		list.append('&youtube_pl=PL1fY_FCMpjVKjqfzzwqrRgJH_9M7C-Vnj')
		
		
	addDir(addonString(10759).encode('utf-8'),list,17,'https://lumiere-a.akamaihd.net/v1/images/il_dj_props_miles_n_f4577f7d.png',addonString(107590).encode('utf-8'),'1',0,fanart)
	
	'''לה לה לופסי'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492590-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492590-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%9c%d7%94%20%d7%9c%d7%94%20%d7%9c%d7%95%d7%a4%d7%a1%d7%99&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2548392')
		
	if 'English' in General_LanguageL:
		pass
	
	addDir(addonString(10758).encode('utf-8'),list,17,thumb,addonString(107580).encode('utf-8'),'1',0,fanart)
	
	'''לונטיק'''
	thumb = 'https://yt3.ggpht.com/-PQGvx_HtSm0/AAAAAAAAAAI/AAAAAAAAAAA/zhHb-7-fKnk/s100-c-k-no/photo.jpg'
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLqjVAzhugdWJ8Jb_LhDP96B7lMPPDF3Jy')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_id=cW8hxIEE-8g')
		list.append('&youtube_pl=PL96FE73DBEC97346F')
		list.append('&youtube_pl=PLB5181F5EC192226F')

	
	addDir(addonString(10751).encode('utf-8'),list,17,thumb,addonString(107510).encode('utf-8'),'1',0,fanart)
	
	'''מועדון החברים של מיקי מאוס'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/79854-2.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/79854-6.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'http://aretheyoldenough.com/wp-content/uploads/2014/12/mickey-mouse-clubhouse-2.jpg'
		fanart = 'http://s2.dmcdn.net/IRKa_/1280x720-nzB.jpg'
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1656.jpg&mode=3&name=%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f-%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%99%d7%a7%d7%99-%d7%9e%d7%90%d7%95%d7%a1-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-mickey-mouse-club%2fseason%2f1&series_id=1656&series_name=%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f-%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%99%d7%a7%d7%99-%d7%9e%d7%90%d7%95%d7%a1-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-mickey-mouse-club%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1656%2f%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f-%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%99%d7%a7%d7%99-%d7%9e%d7%90%d7%95%d7%a1-%d7%9e%d7%93%d7%95%d7%91%d7%91-the-mickey-mouse-club%2fseason%2f1')
		list.append('&youtube_pl=PLVwL64lSxWWwxYwb9KJCqp9Knh-o70C4V')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F79854-6.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F79854-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMickey%20Mouse%20Clubhouse%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmickey-mouse-clubhouse')
		list.append('&youtube_pl=PLI-nQtOHVKRu0erW8Khquk1pRvEHDpR7i') #English
		list.append('&youtube_pl=PLmC05rj_6ViYvReMLbUEmNgyrKWrmpA4c') #English
		list.append('&youtube_pl=PL6hnqKp_bygo9OPZYYVy_h2rZ3lBzhNtU')
	addDir(addonString(10744).encode('utf-8'),list,17,thumb,addonString(107440).encode('utf-8'),'1',0,fanart)
	
	'''מועדון המאפים הטובים'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492592-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492592-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%9e%d7%95%d7%a2%d7%93%d7%95%d7%9f%20%d7%94%d7%9e%d7%90%d7%a4%d7%99%d7%9d%20%d7%94%d7%98%d7%95%d7%91%d7%99%d7%9d&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2690008')
		list.append('&youtube_pl=PLPWc8VdaIIsDUd9awquJznDcL_aSyi00T')
		list.append('&youtube_pl=PLPWc8VdaIIsCfrHCUj7XKDG_rvLwE9V-p')
	addDir('מועדון המאפים הטובים',list,17,thumb,"",'1',"",fanart)
	
	'''מיכל הקטנה'''
	thumb = 'http://www.pashbar.co.il/pictures/show_big_0523173001376412565.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLTNonj9ImqaKElCJ-4e8X_3BzXvzEYU_0')
	addDir(addonString(10245).encode('utf-8'),list,17,thumb,addonString(102450).encode('utf-8'),'1',0,fanart)
	
	'''מיץ ושיר'''
	thumb = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492594-46.jpg'
	fanart = 'http://img.wcdn.co.il/f_auto,w_200,t_41/2/4/9/2/2492594-46.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%9e%d7%99%d7%a5%20%d7%95%d7%a9%d7%99%d7%a8&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2918769')
	addDir(addonString(10785).encode('utf-8'),list,17,thumb,addonString(107850).encode('utf-8'),'1',0,fanart)
	
	'''מיקי כוכבת הילדים'''
	thumb = 'http://yt3.ggpht.com/-LQQaGMJh2g0/AAAAAAAAAAI/AAAAAAAAAAA/KebzcCn-y_Y/s88-c-k-no/photo.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=mikikids')
		list.append('&youtube_id=5Zf0uSGOzlA')
		list.append('&youtube_id=BKCAXKFXwEg')
		list.append('&youtube_id=zGyEGXx3qkU')
	addDir('מיקי כוכבת הילדים',list,17,thumb,addonString(107460).encode('utf-8'),'1',0,fanart)
	
	'''מפרץ ההרפתקאות'''
	thumb = 'http://thetvdb.com/banners/_cache/posters/272472-6.jpg'
	fanart = 'http://thetvdb.com/banners/fanart/original/272472-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%ee%f4%f8%f5%20%e4%e4%f8%f4%fa%f7%e0%e5%fa&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2836047')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1990.jpg&mode=3&name=paw-patrol-%d7%9e%d7%a4%d7%a8%d7%a5-%d7%94%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=1990&series_name=paw-patrol-%d7%9e%d7%a4%d7%a8%d7%a5-%d7%94%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1990%2fpaw-patrol-%d7%9e%d7%a4%d7%a8%d7%a5-%d7%94%d7%94%d7%a8%d7%a4%d7%aa%d7%a7%d7%90%d7%95%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2f9cartoon.me%2fuploads%2fthumbs%2f2015-03-25paw-patrol-season-1-20131.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd050ec12fafe2c97100f5553b706772be1471118127%3bcf_clearance%3d9c4658d06500305d4041a897dfab38cfec5762d3-1475336188-86400%3b__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bPHPSESSID%3d86f31d8264a864fcba222bbadb97477b%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=PAW%20Patrol%20Season%201%20(2013)&url=http%3a%2f%2f9cartoon.me%2fCartoon%2f1347%2fpaw-patrol-season-1-2013%2f') #S1
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2f9cartoon.me%2fuploads%2fthumbs%2f2015-03-27paw-patrol-season-2-20142.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd050ec12fafe2c97100f5553b706772be1471118127%3bcf_clearance%3d9c4658d06500305d4041a897dfab38cfec5762d3-1475336188-86400%3b__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bPHPSESSID%3d86f31d8264a864fcba222bbadb97477b%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=PAW%20Patrol%20Season%202%20(2014)&url=http%3a%2f%2f9cartoon.me%2fCartoon%2f1427%2fpaw-patrol-season-2-2014%2f') #S2
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3a%2f%2f9cartoon.me%2fuploads%2fthumbs%2f2015-11-27paw-patrol-season-3-20153.jpg%7cUser-Agent%3dMozilla%2f5.0%20(Windows%20NT%206.1%3b%20rv%3a32.0)%20Gecko%2f20100101%20Firefox%2f32.0%26Cookie%3d__cfduid%3dd050ec12fafe2c97100f5553b706772be1471118127%3bcf_clearance%3d9c4658d06500305d4041a897dfab38cfec5762d3-1475336188-86400%3b__cfduid%3dd48ee3d5e8750d48c2c735e712c4476201468881294%3b__cfduid%3dde0bb4156da99183db0cc6a7c8325a0041470303966%3bPHPSESSID%3d86f31d8264a864fcba222bbadb97477b%3bPHPSESSID%3d0918e9805af889f932d3f1f7083de44b%3bPHPSESSID%3d71nhps357p41n36mj2h76hs486%3b&mode=2&name=PAW%20Patrol%20Season%203%20(2015)&url=http%3a%2f%2f9cartoon.me%2fCartoon%2f9376%2fpaw-patrol-season-3-2015%2f') #S3
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F198851-7.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F198851-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Octonauts%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-octonauts')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F272472-3.jpg&iconimage=http%3A%2F%2Fwww.toonzone.net%2Fwp-content%2Fuploads%2F2015%2F01%2FPawPatrolMarshallChaseOnTheCase.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DPaw%20Patrol%3A%20Marshall%20%26%20Chase%20on%20the%20Case%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpaw-patrol-marshall-chase-on-the-case')
		list.append('&youtube_pl=PLXy_2ruQsWDHp0hhXgeK2a8V9aafoinl5')
	
	if 'Russian' in General_LanguageL:
		list.append('&youtube_id=') #
		list.append('&youtube_pl=PLrMeN4frlTDz_gBWYQVUYAOUCVpDPQxLf')

	if 'French' in General_LanguageL:
		list.append('&youtube_id=') #
		list.append('&youtube_pl=PL3qHjxSSl7AEHp-CofQtv_DiIBe-MJrRQ')		
		
	addDir(addonString(10752).encode('utf-8'),list,6,thumb,addonString(107520).encode('utf-8'),'1',0,fanart)
	
	'''מר עגבניה'''
	thumb = 'http://media.israel-music.com/images/7290014394605.jpg'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLwimDnICcPKMSeyub1DLM_2jG4aPjqI7n')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f859.jpg&mode=3&name=%d7%99%d7%95%d7%91%d7%9c-%d7%94%d7%9e%d7%91%d7%95%d7%9c%d7%91%d7%9c-%d7%9e%d7%a8-%d7%a2%d7%92%d7%91%d7%a0%d7%99%d7%94-yuval-hamebulbal-mar-hagvaniya%2fseason%2f1&series_id=859&series_name=%d7%99%d7%95%d7%91%d7%9c-%d7%94%d7%9e%d7%91%d7%95%d7%9c%d7%91%d7%9c-%d7%9e%d7%a8-%d7%a2%d7%92%d7%91%d7%a0%d7%99%d7%94-yuval-hamebulbal-mar-hagvaniya%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f859%2f%d7%99%d7%95%d7%91%d7%9c-%d7%94%d7%9e%d7%91%d7%95%d7%9c%d7%91%d7%9c-%d7%9e%d7%a8-%d7%a2%d7%92%d7%91%d7%a0%d7%99%d7%94-yuval-hamebulbal-mar-hagvaniya%2fseason%2f1')
	addDir(addonString(10798).encode('utf-8'),list,17,thumb,addonString(107980).encode('utf-8'),'1',0,fanart)
	
	'''מר למה וגברת ככה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%9e%d7%a8%20%d7%9c%d7%9e%d7%94%20%d7%95%d7%92%d7%91%d7%a8%d7%aa%20%d7%9b%d7%9b%d7%94&url=seriesId%3d2891414')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%ee%f8%20%ec%ee%e4%20%e5%e2%e1%f8%fa%20%eb%eb%e4&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2743907')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1744.jpg&mode=3&name=%d7%9e%d7%a8-%d7%9c%d7%9e%d7%94-%d7%95%d7%92%d7%91%d7%a8%d7%aa-%d7%9b%d7%9b%d7%94-mr-lama-vegveret-kaha%2fseason%2f1&series_id=1744&series_name=%d7%9e%d7%a8-%d7%9c%d7%9e%d7%94-%d7%95%d7%92%d7%91%d7%a8%d7%aa-%d7%9b%d7%9b%d7%94-mr-lama-vegveret-kaha%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1744%2f%d7%9e%d7%a8-%d7%9c%d7%9e%d7%94-%d7%95%d7%92%d7%91%d7%a8%d7%aa-%d7%9b%d7%9b%d7%94-mr-lama-vegveret-kaha%2fseason%2f1')
		list.append('&youtube_pl=PLPWc8VdaIIsC8iEN7EhY46jmy93imkpHI')
	addDir(addonString(10748).encode('utf-8'),list,17,'http://msc.wcdn.co.il/archive/1673912-35.gif',addonString(107480).encode('utf-8'),'1',"",fanart)
	
	'''משחקי החשיבה של רוני'''
	thumb = 'http://www.ronithinkinggames.com/uploads/5/0/2/9/50295455/2504889.png'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=http://62.90.90.56/walla_vod/_definst_/mp4:media/020/504/2050413-40.mp4/playlist.m3u8')
		list.append('&custom4=http://62.90.90.56/walla_vod/_definst_/mp4:media/020/504/2050418-40.mp4/playlist.m3u8')
	addDir(addonString(10750).encode('utf-8'),list,17,thumb,addonString(107500).encode('utf-8'),'1',"",fanart)
	
	'''משפחת יומולדת'''
	thumb = 'http://msc.wcdn.co.il/archive/1620289-35.gif'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLPWc8VdaIIsBOUPxtM2CD7yGs1D8NCM_Z')
	addDir(addonString(10749).encode('utf-8'),list,17,thumb,addonString(107490).encode('utf-8'),'1',"",fanart)
	
	'''סיפורי פיות'''
	thumb = 'http://isc.wcdn.co.il/w9/skins/nick_jr/17/header_pic_2745.png'
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f1%e9%f4%e5%f8%e9%20%f4%e9%e5%fa&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2678298')
		list.append('&youtube_pl=PLPWc8VdaIIsD8YvtRkkqjYC5SF7TKvAcM')
	addDir(addonString(10755).encode('utf-8'),list,17,thumb,addonString(107550).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES107P(General_LanguageL, background, background2) #סימסאלה גרים
	CATEGORIES107G(General_LanguageL, background, background2) #סמי הכבאי
	
	'''קלימרו'''
	thumb = 'http://board.il.ikariam.gameforge.com/wcf/images/avatars/avatar-811.gif'
	fanart = 'https://i.ytimg.com/vi/Uci_grLDJVo/maxresdefault.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLfcYs4SRZfuKZcfWNbg4f6tMHe3olHtlj')
	addDir('קלימרו',list,17,thumb,addonString(107720).encode('utf-8'),'1',0,fanart)
	
	'''סקרדי הסנאי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1679.jpg&mode=3&name=%d7%a1%d7%a7%d7%a8%d7%93%d7%99-%d7%94%d7%a1%d7%a0%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-scaredy-squirrel%2fseason%2f1&series_id=1679&series_name=%d7%a1%d7%a7%d7%a8%d7%93%d7%99-%d7%94%d7%a1%d7%a0%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-scaredy-squirrel%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1679%2f%d7%a1%d7%a7%d7%a8%d7%93%d7%99-%d7%94%d7%a1%d7%a0%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-scaredy-squirrel%2fseason%2f1')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLdTNDKNBE8qfyXihNTPzt0rpBYkL07iXw') #English
		list.append('&youtube_pl=ELVEOAQSX3iU83mCsvSXiaUQ') #English
		list.append('&youtube_pl=ELlz0nRWbqZOISrBkk-GrPXg') #English
		list.append('&youtube_pl=ELsRinC_2rDZJq4rrylfjurw') #English
		list.append('&youtube_pl=ELAVmZC-xyw-toK-qc1PCOrw') #English
	addDir(addonString(10764).encode('utf-8'),list,17,thumb,addonString(107640).encode('utf-8'),'1',"",fanart)
	
	'''עולמו הקסום של מקס''' #NICK
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2108.jpg&mode=3&name=%d7%a2%d7%95%d7%9c%d7%9e%d7%95-%d7%94%d7%a7%d7%a1%d7%95%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%a7%d7%a1-the-magic-world-of-max%2fseason%2f1&series_id=2108&series_name=%d7%a2%d7%95%d7%9c%d7%9e%d7%95-%d7%94%d7%a7%d7%a1%d7%95%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%a7%d7%a1-the-magic-world-of-max%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2108%2f%d7%a2%d7%95%d7%9c%d7%9e%d7%95-%d7%94%d7%a7%d7%a1%d7%95%d7%9d-%d7%a9%d7%9c-%d7%9e%d7%a7%d7%a1-the-magic-world-of-max%2fseason%2f1')
		list.append('&youtube_pl=PLPWc8VdaIIsCeVQhASYBNmykK4gKh0DCe') #Hebrew
	addDir(addonString(10760).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer3/2013/07/21/4745895/max_01.jpg',addonString(107600).encode('utf-8'),'1',0,fanart)
	
	'''פיקסי'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLqjVAzhugdWJh5cXk3Y39ti4jm-2PohHY')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLC72B44008078E9FE')
		list.append('&youtube_pl=PLK7zXb6tNkibmTrztTTHZjd6QignUW4Cq')
		list.append('&youtube_pl=PLbDVT2u1fI0CNahEm2F8SSlZrDN5GrbJn')
	addDir(addonString(10761).encode('utf-8'),list,17,'http://www.youloveit.ru/uploads/gallery/main/791/youloveit_ru_fixiki_kartinki18.jpg',addonString(107610).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://i.vimeocdn.com/video/456717428_1280x720.jpg", default=background2))

	'''פנו דרך לנאדי''' #HOP
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a0%d7%90%d7%93%d7%99%20%d7%a2%d7%95%d7%a0%d7%94%203&url=seasonId%3d2660748')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2092.jpg&mode=3&name=%d7%a4%d7%a0%d7%95-%d7%93%d7%a8%d7%9a-%d7%9c%d7%a0%d7%90%d7%93%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-make-way-for-noddy%2fseason%2f1&series_id=2092&series_name=%d7%a4%d7%a0%d7%95-%d7%93%d7%a8%d7%9a-%d7%9c%d7%a0%d7%90%d7%93%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-make-way-for-noddy%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2092%2f%d7%a4%d7%a0%d7%95-%d7%93%d7%a8%d7%9a-%d7%9c%d7%a0%d7%90%d7%93%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-make-way-for-noddy%2fseason%2f1')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLMgRbqukGSM7jcZwAspOG2i_qX0bZh0I2') #English
		list.append('&youtube_pl=PLNkpbQ4RaGfGnnaYTPCiWoNX2dR55knsX') #English
		list.append('&youtube_pl=PLqTEO1gxHq0yU-J9nTyDvFwiBxuZ_ZGQe') #English
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLZOr1wY3tRc_3SOdbUEdx_4wfGbFaEZx5') #Russian
		list.append('&youtube_pl=PL_kLJ0xxgnewKOhcrWAOzb9_aC0nGigUS') #Russian
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLsmSkb0Izi0ukIPOXrYXs5pjFaBIvtW99') #Portuguese
		list.append('&youtube_pl=PL1BE733471D322384') #Portuguese
	
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLE1dWDmNOYmqFeosjy_1GfVv8b-w8FIz5') #Hungarian
	addDir(addonString(10763).encode('utf-8'),list,6,thumb,addonString(107630).encode('utf-8'),'1',"",fanart)
	
	'''פליפר ולופקה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1153.jpg&mode=3&name=%d7%a4%d7%9c%d7%99%d7%a4%d7%a8-%d7%95%d7%9c%d7%95%d7%a4%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-flipper-and-lopaka%2fseason%2f1&series_id=1153&series_name=%d7%a4%d7%9c%d7%99%d7%a4%d7%a8-%d7%95%d7%9c%d7%95%d7%a4%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-flipper-and-lopaka%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1153%2f%d7%a4%d7%9c%d7%99%d7%a4%d7%a8-%d7%95%d7%9c%d7%95%d7%a4%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-flipper-and-lopaka%2fseason%2f1')
		list.append('&youtube_pl=PLerEkB0tFW3aCqMAK0gzZkkF0QjxQx-4h')
		list.append('&youtube_pl=PLerEkB0tFW3brFpEnqz3N4vU6L4NUBQi3')
	addDir(addonString(10765).encode('utf-8'),list,17,thumb,addonString(107650).encode('utf-8'),'1',0,fanart)
	
	'''פפה החזיר''' #NICK JR
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=UCcp5Afr_1qXMhn3UfDhtc6g/playlists')
		list.append('&youtube_pl=PLFEgnf4tmQe8P9-hSy8io-PyK2LLIVuAz')
		list.append('&youtube_pl=PLFEgnf4tmQe_YHkXH2p7X-dqnBzR0FIJn')
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F79222-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F79222-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DPeppa%20Pig%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fpeppa-pig')
		
		list.append('&youtube_id=aNNB7LPwHkQ')
		list.append('&youtube_id=Ws2NXmtp61Y')
		list.append('&youtube_id=xhap8ezkfCE')
		list.append('&youtube_id=u9zAJz2wyG8') #פפה החזיר
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_id=N-MLaRXIivY')
		list.append('&youtube_id=DvAZRg_VeSg')
		
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLAEVaVVl7Uh6jf0Lk_2gK-5AoZor_SZ_Z')
		list.append('&youtube_pl=PLrpvkUYQuRUFKClj669y7JFEgr2AkwEPI')
		list.append('&youtube_id=VWbYAAVsKHs')	
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_ch=OficialPeppa/playlists')
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=CanaleUfficialePeppa/playlists')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_ch=OfficialPeppaRussia/playlists')
		
		list.append('&youtube_pl=PLOgjrDemRWxKAYykYCyyHjhLg-AnVL_WJ')
		
	addDir(addonString(10766).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/79222-1.jpg',addonString(107660).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/79222-3.jpg.jpg", default=background2))
	
	'''צ'פצ'ולה' - מיכל כלפון'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UC64wDQFgTq9RpI1P8_p-SxA')
		list.append('&youtube_id=_Jsa4Ml77-I')
		list.append('&youtube_id=BduVyZALCYs')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2728301&mode=10&module=wallavod')
		list.append('&custom4=plugin://plugin.video.wallaNew.video/?url=item_id%3D2728353&mode=10&module=wallavod')
	addDir(addonString(10768).encode('utf-8'),list,17,'https://lh5.googleusercontent.com/-4Rd1GQEZnaM/AAAAAAAAAAI/AAAAAAAAChQ/YOHq90H_OZk/photo.jpg',addonString(107680).encode('utf-8'),'1',0,fanart)
	
	'''קאט דה רופ*'''
	thumb = ''
	fanart = ''
	list = []
	list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1544.jpg&mode=3&name=om-nom-stories-%d7%a7%d7%90%d7%98-%d7%93%d7%94-%d7%a8%d7%95%d7%a4-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&series_id=1544&series_name=om-nom-stories-%d7%a7%d7%90%d7%98-%d7%93%d7%94-%d7%a8%d7%95%d7%a4-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1544%2fom-nom-stories-%d7%a7%d7%90%d7%98-%d7%93%d7%94-%d7%a8%d7%95%d7%a4-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
	list.append('&youtube_pl=PLVxGcyI6KPth2dKNkp-0dH2VYCJCppzDE')
	list.append('&youtube_pl=PLqYXYWudQqfYNO42AoFDjr0WUbLtebnCA')
	list.append('&youtube_pl=PLOPSPZSEWlCWpW6kId3LRDlKYrvsfZQsK') #Gameplay
	addDir(addonString(10767).encode('utf-8'),list,17,thumb,addonString(107670).encode('utf-8'),'1',"",fanart)
	
	CATEGORIES107F(General_LanguageL, background, background2) #קירוקי
	CATEGORIES107Q(General_LanguageL, background, background2) #רובו אוטו פולי
	CATEGORIES107R(General_LanguageL, background, background2) #מטוסי על

	'''רוי בוי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLR7DTcU2p0Qg8pxiEld0Fg3K2Bd8gTKw5')
	addDir(addonString(10772).encode('utf-8'),list,17,'http://amarganim.co.il/images_bo/%D7%A8%D7%95%D7%99%20%D7%91%D7%95%D7%99.jpg',addonString(107720).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/Uci_grLDJVo/maxresdefault.jpg", default=background2))
	
	'''רוני וקשיו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f8%e5%f0%e9%20%e5%f7%f9%e9%e5&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2691928')
		list.append('&youtube_pl=PLPWc8VdaIIsDPb04SHd5fzzqYt3FtmWs-')
		list.append('&youtube_pl=PLPWc8VdaIIsDCX6hU5b-ve2I_MRESc8FZ')
	addDir(addonString(10773).encode('utf-8'),list,17,'http://amarganim.co.il/images_bo/%D7%A8%D7%95%D7%A0%D7%99%20%D7%95%D7%A7%D7%A9%D7%99%D7%95.jpg',addonString(107730).encode('utf-8'),'1',"",fanart)
	
	'''רוץ דייגו רוץ!'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f8%e5%f5%20%e3%e9%e9%e2%e5%20%f8%e5%f5!&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f1688298')
		list.append('&youtube_ch=UCB6woLfnHOGUo2V4L1O_xUw')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLGlfDbXygO0aM7lIzlvQczZUIG7uWVAE_')
		list.append('&youtube_pl=PLGlfDbXygO0bFeMr9q7HHcjnegFvr52yQ')
		
	addDir(addonString(10770).encode('utf-8'),list,17,thumb,'','1',0,fanart)
	
	'''רורי - מכונית המירוץ'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLBD5CA381B360E697') #רורי - מכונית המירוץ
		list.append('&youtube_pl=PL2_l_4eIE1ayuv8Pu5RJq4__9cWJSz_q3') #S1
		list.append('&youtube_pl=PL2_l_4eIE1awTALqUwY74eAu9jJhrHxIx') #S2
		list.append('&youtube_pl=PL2_l_4eIE1axGrnR3bOyebdHbq4FxEa4X')
		list.append('&youtube_pl=PLCD5DC0818873F01B')
		list.append('&youtube_pl=PL6D2CFE1974DC147A')
		
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLYyLwF_4uU8C5uvETiiiFdeGiDrJZgHWQ') #רורי - מכונית המירוץ
			
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL4AB6764BB1A5D9BC') #רורי - מכונית המירוץ
	
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PL_8KHX6sbn_LmIgyCGpuYsG-kaL3qE6AJ') #רורי - מכונית המירוץ
		list.append('&youtube_pl=PLH1Aa9oodhpvE3_TjiudN9MmgrAc65HP4')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLNKCGwoKGNlk_mO53RtB8lY2xw_x4KCnW')
	
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL51C4EC12702A03E2') #רורי - מכונית המירוץ
	
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=PLimGLL8W7RsnaTo2rktkrhgzKYlgKWXG3') #רורי - מכונית המירוץ
	
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL3qHjxSSl7AFJdTot0Gntox_a9x9CCzEv') #רורי - מכונית המירוץ	
		
	addDir(addonString(10771).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/thumb/4/46/RoaryTheRacingCarFullCharacters.png/280px-RoaryTheRacingCarFullCharacters.png',addonString(107710).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.factorycreate.com/wp-content/uploads/2014/10/Factory_Roary_LargeImage_1350x760_02.jpg", default=background2))
	
	'''רינת ויויו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLVisQUXwii8qa6lRDe1OmCIup6ylcprfc')
	addDir(addonString(10774).encode('utf-8'),list,17,'http://media.israel-music.com/images/7290012163999.jpg',addonString(107740).encode('utf-8'),'1',"",fanart)
	
	'''רכבת הדינוזאורים'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F116291-4.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F116291-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDinosaur%20Train%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdinosaur-train')
		list.append('&youtube_ch=UCn_ancn0S-mkGyn3bn3f8XA')
	addDir(addonString(10780).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/116291-2.jpg',addonString(107800).encode('utf-8'),'1',"",getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/116291-4.jpg", default=background2))
	
	'''שטויות בחדשות'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f9%e8%e5%e9%e5%fa%20%e1%e7%e3%f9%e5%fa&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2691886')
		list.append('&youtube_pl=PLPWc8VdaIIsBzxaUfj3smv1tJ8sKQXwrW')
	addDir(addonString(10777).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer3/2013/02/04/4440787/shtuyot_01.jpg',addonString(107770).encode('utf-8'),'1',"",fanart)
	
	'''שלדון'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL_8KXLhQVQMLzs0EHUhG_9PwxVsFgDAo4')
	addDir(addonString(10778).encode('utf-8'),list,17,'https://i.ytimg.com/vi/6kSynpNXMBs/default.jpg',addonString(107780).encode('utf-8'),'1',0,fanart)
	
	'''שון כבשון*'''
	thumb = ''
	fanart = ''
	list = []
	list.append('&youtube_ch=UCgeyhZ9dcdOuNAy9MVa7W6w/playlists')
	list.append('&youtube_pl=PLYaaF6e9cMtG4fx0bxhS7lVNYYJ0toqqr')
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_id=KtIa3HsLxng') #S1
		list.append('&youtube_pl=PL75WpgEj_KA2a6-aSWRtjzwqLpth8afUj') #S2
		list.append('&youtube_pl=PL75WpgEj_KA0B8fal43tCjQfJwvQR8vKf') #S
	list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F79890-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F79890-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DShaun%20the%20Sheep%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fshaun-the-sheep')
		
	
	addDir(addonString(10730).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/79890-2.jpg',addonString(107300).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/79890-2.jpg", default=background2))
	
	'''שמרסקי'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLeVA7eICJ6d0zofGFGpd3t_RXBjbuQGdW')
		list.append('&youtube_pl=PLeVA7eICJ6d30xzPCWQm7198EUJgVdOjN')
		list.append('&youtube_pl=PLeVA7eICJ6d0Lywa2hyj513nrCmrgnHdj')
		list.append('&youtube_pl=PLK7zXb6tNkiYi1TZ8HoLUS7ppv3C_AxMb')
	
	addDir(addonString(10787).encode('utf-8'),list,17,'https://yt3.ggpht.com/-NaEYR_gMd_s/AAAAAAAAAAI/AAAAAAAAAAA/ev0E714j9mM/s100-c-k-no/photo.jpg',addonString(107870).encode('utf-8'),'1',0,fanart)
	
	'''שלוש ארבע לעבודה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f9%ec%e5%f9%20%e0%f8%e1%f2%20%ec%f2%e1%e5%e3%e4&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2693368')
		list.append('&youtube_pl=PLPWc8VdaIIsASIzs8TcS3FFYEL68jBPWO')
	addDir(addonString(10779).encode('utf-8'),list,17,'http://www.hll.co.il/web/8888/nsf/web/8017/%D7%A9%D7%9C%D7%95%D7%A9-%D7%90%D7%A8%D7%91%D7%A2-%D7%9C%D7%A2%D7%91%D7%95%D7%93%D7%94.jpg',addonString(107790).encode('utf-8'),'1',"",fanart)
	
	'''תגליות''' #לוגי
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=')
	addDir('תגליות',list,17,'','','1',0,fanart)
	
	'''תומס הקטר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLsDVVvjmKAxEeSD3K7wybKJ42BbZc5JlJ') #תומס הקטר
		
		list.append('&youtube_id=FrUVIyhhhkQ')
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78949-8.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78949-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThomas%20the%20Tank%20Engine%20%26%20Friends%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthomas-the-tank-engine-friends')
		list.append('&youtube_pl=PLI2i4PrLia3gAAYjMaVbAwdt1xrOsUaXS')
	
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLwGUVOoN_pI3QbBFmTHQ76uYtVS7c4yF9')
		
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=') #תומס הקטר
		
	addDir(addonString(10786).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/78949-3.jpg',addonString(107840).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/78949-8.jpg", default=background2))
	
	'''תותית'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2550328')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2710592')
		list.append('&youtube_pl=PLfcYs4SRZfuJgh8F-yrhcqKuQke6YbHLj') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fwww.thetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F74841-1.jpg&iconimage=http%3A%2F%2Fwww.thetvdb.com%2Fbanners%2F_cache%2Fposters%2F74841-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DStrawberry%20Shortcake%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fstrawberry-shortcake')
		list.append('&youtube_pl=PLGNVqRT1VxkJBlBVQFiF-FZuzPVRLhUXm') #English
		list.append('&youtube_pl=PLX4pO2h-uwKBRpV8SKQre69BJxdDY4J_i') #English
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL31D1F4E7E212F382') #French
		list.append('&youtube_pl=PLF7169918C82398BF') #French
	addDir(addonString(10784).encode('utf-8'),list,17,'https://i1.ytimg.com/sh/YO96TrSN7Do/showposter.jpg?v=508e4f85',addonString(107840).encode('utf-8'),'1',0,fanart)
	
	'''Baby Looney Tunes'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F51%2Fimage%2F555x418%2Fbaby-looney-toons.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBaby%20Looney%20Tunes%20(2001-2006)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fbaby-looney-tunes-tv-series')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10341).encode('utf-8'),list,6,'https://www.thetvdb.com/banners/posters/71301-3.jpg',addonString(103410).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://www.thetvdb.com/banners/fanart/original/71301-3.jpg", default=background2))
	
	'''Future-Worm!'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F296709-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F296709-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DFuture-Worm%20(2016)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ffuture-worm-2016')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10379).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/296709-2.jpg',addonString(103790).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/296709-1.jpg", default=background2))
	
	'''Kate and Mim-Mim'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F284464-1.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F284464-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DKate%20and%20Mim-Mim%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fkate-and-mim-mim')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10718).encode('utf-8'),list,6,'https://thetvdb.com/banners/_cache/posters/284464-1.jpg',addonString(107180).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://thetvdb.com/banners/fanart/original/284464-1.jpg", default=background2))
	
	'''The Octonauts'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F198851-7.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F198851-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Octonauts%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-octonauts')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10781).encode('utf-8'),list,6,'https://thetvdb.com/banners/_cache/posters/198851-2.jpg',addonString(107810).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://thetvdb.com/banners/fanart/original/198851-7.jpg", default=background2))
	
	'''My Friends Tigger and Pooh'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F80850-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F80850-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMy%20Friends%20Tigger%20and%20Pooh%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmy-friends-tigger-and-pooh')
		list.append('&youtube_pl=PLOfLarWANBSqRbaxnZ6aRET0ZV1SsqI63')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10700).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/80850-1.jpg',addonString(107000).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/80850-1.jpg", default=background2))
	
	'''Little Charley Bear'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F220631-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F220631-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DLittle%20Charley%20Bear%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Flittle-charley-bear')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10720).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/220631-1.jpg',addonString(107200).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/220631-1.jpg", default=background2))
	
	'''Go Jetters'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F302130-1.jpg&iconimage=https%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F302130-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGo%20Jetters%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fgo-jetters')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10701).encode('utf-8'),list,6,'https://thetvdb.com/banners/_cache/posters/302130-1.jpg',addonString(107010).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://thetvdb.com/banners/fanart/original/302130-1.jpg", default=background2))
	
	'''Sid the Science Kid'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F82931-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F82931-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSid%20the%20Science%20Kid%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fsid-the-science-kid')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10782).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/82931-1.jpg',addonString(107820).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/82931-3.jpg", default=background2))
	
	'''Talking Tom and Friends'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F310606-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F310606-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DTalking%20Tom%20and%20Friends%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ftalking-tom-and-friends')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10783).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/310606-1.jpg',addonString(107830).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/310606-1.jpg", default=background2))
	
	
	CATEGORIES107A(General_LanguageL, background, background2) #עמוד הבא קטנטנים
	
def CATEGORIES108(name, iconimage, desc, fanart):
	'ילדים ונוער'
	background = 108
	background2 = "" #http://30k0u22sosp4xzag03cfogt1.wpengine.netdna-cdn.com/wp-content/uploads/2015/03/strika-3.jpg
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES108Z(General_LanguageL, background, background2) #ערוצי טלוויזיה
	
	'''אגדת הנסיך וליאנט'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLITCTw1CgheMxcO_E0VMrd9LQSuWE49MW')
		
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
		
	addDir(addonString(10858).encode('utf-8'),list,17,'http://ecx.images-amazon.com/images/I/51leujDMgQL.jpg',addonString(108580).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://static.justwatch.com/backdrop/496670/s1440/the-legend-of-prince-valiant", default=background2))
	
	'''אוסטין ואלי'''
	thumb = 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/Austin_%26_ally_tv_series_logo.png/200px-Austin_%26_ally_tv_series_logo.png'
	fanart = 'http://img.lum.dolimg.com/v1/images/au_disneychannel_aaa_ross_aanda_superroom_albumcover_d16e7f65.jpeg'
	list = []
	if 'Hebrew' in General_LanguageL:
		thumb = 'https://upload.wikimedia.org/wikipedia/he/1/1b/A%26a.hebrew.png'
		list.append('&youtube_pl=')
	if 'English' in General_LanguageL:
		list.append('&dailymotion_pl=x46tyj') #S1-3
		list.append('&dailymotion_pl=x2fj350') #S1-3
		list.append('&dailymotion_pl=x2fiw3b') #S2
		list.append('&dailymotion_pl=x3irdaq') #S4
		
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLXXlWZEt9lW6W03mrW407QLmBZdRs7U4I')
		
	addDir(addonString(10859).encode('utf-8'),list,17,thumb,addonString(108590).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES108C(General_LanguageL, background, background2) #אחים וחיות אחרות
	
	'''איוון הצארביץ והזאב האפור'''
	thumb = ''
	fanart = ''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLOgjrDemRWxKAYykYCyyHjhLg-AnVL_WJ') #איוון הצארביץ והזאב האפור
		list.append('&youtube_pl=PLjnasSEuz-qROskHRihuIMhACIQQhrDZw')
		
	addDir(addonString(10803).encode('utf-8'),list,17,'http://www.fest.md/files/events/45/image_4571_1_large.jpg',addonString(108030).encode('utf-8'),'1',0,fanart)
	
	'''איוון מקסימוב'''
	thumb = ''
	fanart = ''
	list = []
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL1HIp83QRJHQOmroSI5hWLo0ma89aFtND')
		list.append('&youtube_pl=PLp1Znx4yjhEvp8XODti0-0Mgnuojr3rTV')
	addDir(addonString(10802).encode('utf-8'),list,17,'https://i.ytimg.com/vi/gJEBr4MJ0uI/mqdefault.jpg',addonString(108020).encode('utf-8'),'1',0,fanart)
	
	'''אייס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2015%2f07%2f23%2fhafranim_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fthe-diggers-S1')
		list.append('&youtube_pl=PLKMFPiSCwUk3QnO33fixyo8gCPIBN6pf0')
		
	if 'English' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PLwAAJ8zskC84ZvLI23zWD85SkfaytngH-')
	addDir(addonString(10851).encode('utf-8'),list,17,'http://vignette2.wikia.nocookie.net/voiceacting/images/4/48/Get_Ace_Web_Logo.jpg/revision/latest?cb=20140315004313',addonString(108510).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://images.tvnz.co.nz/tvnz_images/get_ace/2015/01/get_ace_e345_Master.jpg", default=background2))
	
	'''איטי ועצבני'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLKMFPiSCwUk08zM6SlJ3RrCu2_zdReijH')
	addDir('איטי ועצבני',list,17,'http://f.frogi.co.il/pic/VOD_zoom/itivazbani/itivazbni_gadol_vod.png?r=1436869042','','1',0,fanart)
	
	'''איפה אפי?'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72185-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72185-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DWhere%27s%20Wally%3F%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fwheres-wally')
		list.append('&youtube_pl=')
	if 'Russian' in General_LanguageL:	
		list.append('&youtube_pl=')
	addDir(addonString(10886).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/72185-1.jpg',addonString(108860).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/72185-1.jpg", default=background2))
	
	'''איק החתול'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyEvz6V-X7BPsRnJA7otQ3ds')
	if 'Russian' in General_LanguageL:	
		list.append('&youtube_pl=')
	addDir(addonString(10801).encode('utf-8'),list,17,'https://images.rapgenius.com/de1193471b5b2ab9ce7eaec9c896ec18.800x521x1.png',addonString(108010).encode('utf-8'),'1',0,fanart)
	
	'''איש משפחה'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F75978-23.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F75978-17.jpg&mode=1&name=%5BB%5D%5BCOLOR%20white%5DFamily%20Guy%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.kisspanda.net%2Ffamily-guy%2F')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F18%2Fimage%2F555x418%2Ffamily-guy.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DFamily%20Guy%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Ffamily-guy-tv-series')
		
	addDir(addonString(10873).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/75978-17.jpg',addonString(108730).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/75978-23.jpg", default=background2))
	
	'''אלוף הסופר סטרייקה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLKMFPiSCwUk27kVfF2uHBMqVZ9XaykEYN') #?
	addDir('אלוף הסופר סטרייקה',list,17,'http://images1.ynet.co.il/PicServer4/2015/10/07/6545370/aluf_super_strika_01.jpg','','1',0,getAddonFanart(background, custom="http://zoomtv.co.il/wp-content/uploads/2015/10/%D7%90%D7%9C%D7%95%D7%A3-%D7%94%D7%A1%D7%95%D7%A4%D7%A8-%D7%A1%D7%98%D7%A8%D7%99%D7%99%D7%A7%D7%94-%D7%9C%D7%95%D7%92%D7%95.png", default=background2))
	
	'''אליפים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLA707A24672EA3BFE')
		list.append('&youtube_pl=PLAr10z7QNUYHFgUFhvBAq1s8du1J8LIds')
		list.append('&youtube_pl=PLl93DUIXBk8T9TKjAYAisbnjgDkiIgaY4')
	addDir('אליפים',list,17,'http://images.mouse.co.il/storage/7/6/120125215_9936250_0..jpg','','1',0,fanart)
	
	'''אלישע'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2021.jpg&mode=3&name=%d7%90%d7%9c%d7%99%d7%a9%d7%a2-elisha%2fseason%2f1&series_id=2021&series_name=%d7%90%d7%9c%d7%99%d7%a9%d7%a2-elisha%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2021%2f%d7%90%d7%9c%d7%99%d7%a9%d7%a2-elisha%2fseason%2f1')
		
	addDir('אלישע',list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/0/02/%D7%90%D7%9C%D7%99%D7%A9%D7%A2_%D7%A1%D7%93%D7%A8%D7%94.jpg/250px-%D7%90%D7%9C%D7%99%D7%A9%D7%A2_%D7%A1%D7%93%D7%A8%D7%94.jpg','אלישע היא קומדיית מצבים ישראלית, בכיכובו של יובל סמו המתרחשת בבית הספר "הרצל" בפתח תקווה','1',0,fanart)
	
	'''בבית של פיסטוק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL9FD9492D8C95F00F') #בבית של פיסטוק
	addDir('בבית של פיסטוק',list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/6/6c/FistukLogo.jpg/250px-FistukLogo.jpg',addonString(108040).encode('utf-8'),'1',0,fanart)
	
	'''בורו גלאי החייזרים'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyG-Xfgy-9pxWeE6fWHIL7dh') #English
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir(addonString(10818).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/a/ab/Bureau_of_Alien_Detectors.png',addonString(108180).encode('utf-8'),'1',0,fanart)
	
	'''Bobobobs'''
	thumb = ''
	fanart = ''
	list = [] 
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLB461927E7B8CF3F1') #English
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL063973E8C7388E65') #French
	addDir(addonString(10811).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/6/6c/FistukLogo.jpg/250px-FistukLogo.jpg',addonString(108110).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES108D(General_LanguageL, background, background2) #ביוויס ובאטהד
	
	'''בובס בורגר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F194031-5.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F194031-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBobs%20Burgers%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbobs-burgers')
		
	addDir(addonString(10860).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/194031-3.jpg',addonString(108600).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/194031-5.jpg", default=background2))
	
	'''בית אנוביס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e1%e9%fa%20%e0%f0%e5%e1%e9%f1&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1810190')
	addDir(addonString(10816).encode('utf-8'),list,6,'https://upload.wikimedia.org/wikipedia/he/thumb/3/3c/House_of_Anubis.jpg/250px-House_of_Anubis.jpg',addonString(108160).encode('utf-8'),'1',0,fanart)
	
	'''בלה והבולדוגס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e1%ec%e4%20%e5%e4%e1%e5%ec%e3%e5%e2%f1&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2888985')
	if 'English' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=ELjuobdmKDkF2ilbSpE1D8fg')
	addDir(addonString(10815).encode('utf-8'),list,6,'https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Bellaandthebulldogslogo.png/200px-Bellaandthebulldogslogo.png',addonString(108150).encode('utf-8'),'1',0,fanart)
	
	'''בלי סודות''' #addonString(10804).encode('utf-8')
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL9FD9492D8C95F00F') #בלי סודות
		list.append('&youtube_pl=PL29CF6709AA760AB5')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1143.jpg&mode=3&name=%d7%91%d7%9c%d7%99-%d7%a1%d7%95%d7%93%d7%95%d7%aa-without-secrets%2fseason%2f1&series_id=1143&series_name=%d7%91%d7%9c%d7%99-%d7%a1%d7%95%d7%93%d7%95%d7%aa-without-secrets%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1143%2f%d7%91%d7%9c%d7%99-%d7%a1%d7%95%d7%93%d7%95%d7%aa-without-secrets%2fseason%2f1')
	addDir('בלי סודות',list,17,thumb,'בבית של פיסטוק היא ספין-אוף של סדרת הטלוויזיה הישראלית לילדים "רגע עם דודלי".[CR]הסדרה הופקה על ידי הטלוויזיה החינוכית במשך שתי עונות בין השנים 1981 - 1983 וכללה 29 פרקים שצולמו בעונה הראשונה בשחור-לבן (18 פרקים) ובעונה השנייה בצבע (11 פרקים). הסדרה שודרה בשידורים חוזרים לאורך כל שנות השמונים והתשעים וזכתה לפופולריות רבה בקרב ילדי ישראל.[CR]עלילת הסדרה מתמקדת בהרפתקאותיהם של פיסטוק (ספי ריבלין) וידידו רגע (ציפי מור). פיסטוק הוא אדם תמהוני חביב ומגושם המתגורר בבית קטן ומוזר על ראש גבעה ורגע הוא בובה שהפכה לילד. בנוסף, התוכנית הכילה גם פינה של בובה בשם "פלטיאל ממגדיאל" וסדרה נוספת עם בובות מהולנד ב סיפורימפו אשר דובבו לעברית.[CR]הסדרה הופקה בתקציב נמוך משמעותית מסדרת האם "רגע עם דודלי". למעט פרקים מיוחדים היא צולמה רובה ככולה באולפני הטלוויזיה החינוכית ברמת אביב. החל מעונתה השנייה, זו הייתה ההפקה הראשונה של הטלוויזיה החינוכית שצולמה בצבע.[CR]רבים מפרקי הסדרה שצולמו בשחור-לבן נחשבים כיום לאבודים, מאחר שהטלוויזיה החינוכית מעולם לא שימרה אותם ולא העבירה אותם מהסרטים המקוריים לפורמט דיגיטלי מודרני.[CR]שיר הפתיחה של התוכנית נכתב על ידי לאה נאור, הולחן על ידי נורית הירש, ובוצע על ידי אילנית.','1',0,fanart)
	
	'''גאליס'''
	thumb = ''
	fanart = 'http://niranbd.com/newcity/vcitypics/950593/976250_597922800238215_757208968_o.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UC1ZvZmYKkigob8Vg7MSgqjg') #?
		list.append('&dailymotion_pl=x3mu52') #S1
		list.append('&dailymotion_pl=x3my1z') #S2
		list.append('&dailymotion_pl=x3mzpe') #S3
		list.append('&dailymotion_pl=x3n07f') #S4
		#list.append('&dailymotion_pl=x3nt5q') #S5
		list.append('&dailymotion_pl=x48aar') #S6
		
		list.append('&youtube_pl=PL5NvWknQGq-IoWfSxfH71hyT0Ec4u7VgE')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?mode=6&name=%5bCOLOR%20red%5d%20%d7%97%d7%a4%d7%a9%20%20%5b%2fCOLOR%5d&summary&url=http%3a%2f%2fwww.sdarot.wf%2fsearch')
	addDir(addonString(10849).encode('utf-8'),list,17,thumb,addonString(108490).encode('utf-8'),'1',0,fanart)
	
	'''גיבורי האור הדור הבא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99%20%d7%94%d7%90%d7%95%d7%a8%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90&url=seasonId%3d2884528')
	addDir('גיבורי האור הדור הבא',list,6,'','','1',0,fanart)
	
	'''גארפילד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F77054-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F77054-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGarfield%20and%20Friends%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fgarfield-and-friends')

	addDir(addonString(10877).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/77054-1.jpg',addonString(108770).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/77054-1.jpg", default=background2))
	
	'''גור ואוח'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f521.jpg&mode=3&name=gur-ve-uch-%d7%92%d7%95%d7%a8-%d7%95%d7%90%d7%95%d7%97&series_id=521&series_name=gur-ve-uch-%d7%92%d7%95%d7%a8-%d7%95%d7%90%d7%95%d7%97&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f521%2fgur-ve-uch-%d7%92%d7%95%d7%a8-%d7%95%d7%90%d7%95%d7%97')
		list.append('&youtube_ch=spongebob0o8')
	addDir('גור ואוח',list,17,'https://upload.wikimedia.org/wikipedia/he/6/66/TVshow45GorAndOhooHtheme.PNG','','1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/QXbJOjYnkhw/maxresdefault.jpg", default=background2))
	
	'''גיבורי האור הדור הבא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99%20%d7%94%d7%90%d7%95%d7%a8%20%d7%94%d7%93%d7%95%d7%a8%20%d7%94%d7%91%d7%90&url=seasonId%3d2884528')
	addDir('גיבורי האור הדור הבא',list,6,'','','1',0,fanart)
	
	'''גלקטיק פוטבול'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLHGRa3D4Qeg3Vmg4oAkO-rfLoWA9Ybj0k') #גלקטיק פוטבול
		list.append('&youtube_pl=PLDOEpwVmWYUsqtvYg12JP_y51qoXpObEA') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL4FAE601401A6B3F3') #English #S1
		list.append('&youtube_pl=PLDAAEF5D78E11754B') #English #S2
		list.append('&youtube_pl=PL005SsHOGXPPjJDAemQjWvK7lvBL5iQnW') #English #S3
		list.append('&youtube_pl=PLOcNLH674qyFkgYT1powjI-XcBhAqUtA6') #English
	if 'Bulgarian' in General_LanguageL:	
		list.append('&youtube_pl=PLWMCwroYhJSo2sFT6InbR6kiQGovNvcsK') #Bulgarian
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLDexQIApun8-FuZkNLaoBe0JagWq9I-I-') #Italian #S2
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLi6qC0rHH6ZgZano90K1AC9umjDocRWVV') #Hungarian #S2
	
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PL4A983F74692C098F') #Turkish #S1
		list.append('&youtube_pl=PL4A37742103A8546E') #Turkish #S2
	addDir(addonString(10821).encode('utf-8'),list,17,'https://pbs.twimg.com/profile_images/541776376/Galactik_Reduced_Carr__400x400.jpg',addonString(108210).encode('utf-8'),'1',0,fanart)
	
	'''ג'ינג'י'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=') #
		list.append('&youtube_pl=') #
		list.append('&youtube_pl=') #
	addDir("ג'ינג'י",list,17,'http://msc.wcdn.co.il/w/w-635/1999686-18.jpg','','1',0,getAddonFanart(background, custom="https://www.yes.co.il/SiteCollectionImages/Pages/GINGI_landingP3.jpg", default=background2))
	
	'''גיבורי התנ"ך'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1083.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1083&series_name=greatest-heroes-and-legends-of-the-bible-%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99-%d7%94%d7%aa%d7%a0-%d7%9a-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary=%d7%90%d7%a0%d7%aa%d7%95%d7%9c%d7%95%d7%92%d7%99%d7%94%20%d7%a9%d7%9c%20%d7%90%d7%99%d7%a8%d7%95%d7%a2%d7%99%d7%9d%20%d7%9e%d7%a4%d7%95%d7%a8%d7%a1%d7%9e%d7%99%d7%9d%20%d7%91%d7%aa%d7%a0%22%d7%9a.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1083%2fgreatest-heroes-and-legends-of-the-bible-%d7%92%d7%99%d7%91%d7%95%d7%a8%d7%99-%d7%94%d7%aa%d7%a0-%d7%9a-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLx1dI0IFg6RqlKwV-RPhXx_YZfDbadc7h') #גיבורי התנ"ך
	
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL67F1DD7B9B45213A')
		list.append('&youtube_pl=PLE8E08292878C59A1')
		list.append('&youtube_pl=PLx1dI0IFg6RqlKwV-RPhXx_YZfDbadc7h')
		list.append('&youtube_pl=PL488DDE53D6E20EEE')
		list.append('&youtube_id=Q1nUIA2uGMI')
		
		
	addDir(addonString(10820).encode('utf-8'),list,17,thumb,addonString(108200).encode('utf-8'),'1',0,fanart)
	
	'''גים באטן'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyEigxNLxRyVKL-c1fL9Aw_o')
	if 'Russian' in General_LanguageL:	
		list.append('&youtube_pl=')
	addDir(addonString(10819).encode('utf-8'),list,17,'http://www.animenewsnetwork.com/thumbnails/fit200x200/encyc/A116-12.jpg',addonString(108190).encode('utf-8'),'1',0,fanart)
	
	'''גלילאו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLth1a195qHsjFGXCmLtU0WZDuLq4CiWz4') #גלילאו
		list.append('&youtube_pl=PL51YAgTlfPj6Ypxb-_Dh0eoCztCXiBYsN')
		list.append('&youtube_pl=PLth1a195qHsigShKnT9DsIyKxcTBQ70Tf')
		list.append('&youtube_pl=PL51YAgTlfPj5ERxljvk0cLQAjnLMj3son') #S4
		list.append('&youtube_pl=PLFw7KwIWHNB14v2w1rx_drmWtZPldqgtp') #S4-5
	addDir(addonString(10810).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Hila_Korach.jpg/250px-Hila_Korach.jpg',addonString(108100).encode('utf-8'),'1',0,fanart)
	
	'''גן חיות'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e2%ef%20%e7%e9%e5%fa&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2656314')
	addDir('גן חיות',list,6,'https://upload.wikimedia.org/wikipedia/he/thumb/2/28/%D7%9C%D7%95%D7%92%D7%95_%D7%92%D7%9F_%D7%97%D7%99%D7%95%D7%AA.jpeg/240px-%D7%9C%D7%95%D7%92%D7%95_%D7%92%D7%9F_%D7%97%D7%99%D7%95%D7%AA.jpeg','בפתיח של כל פרק מופיע מאפיין מצחיק של גן החיות גנחה שבצומת מנחה.[CR]כל פרק מתחיל כאשר מנהל גן החיות מר פיקולו מעלה רעיון חדש לשיפור גן החיות גנחה שבצומת מנחה. הוא נוהג לקרוא למזכירתו דורותי ולציין מה יש לעשות כדי לבצע רעיון זה, אך היא חשה שעלולות להיווצר תקלות בביצוע הרעיון. בכל פרק מתרחשות עלילות משנה של דמויות נוספות בקרב עובדי גן החיות ומבקריו.','1',0,fanart)
	
	'''גרוויטי פולס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
		
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F259972-6.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F259972-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DGravity%20Falls%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fgravity-falls')
		
	if 'French' in General_LanguageL:
		pass
		
	addDir(addonString(10887).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/259972-3.jpg',addonString(108870).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/259972-6.jpg", default=background2))
	
	'''האגדה של קורה''' #The Legend of Korra
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e4%e0%e2%e3%e4%20%f9%ec%20%f7%e5%f8%e4&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2579878')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F27%2Fimage%2F555x418%2Fthe-legend-of-korra.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Legend%20of%20Korra%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-legend-of-korra')
	addDir('האגדה של קורה',list,6,'','','1',0,fanart)
	
	CATEGORIES108B(General_LanguageL, background, background2) #הארווי ביקס
	
	'''הדב פדינגטון'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLWJa48pm3noa-CVm1nZMEZUHcQTH795Pm')
		list.append('&youtube_pl=PL5D179E8870E9F8F9')
		list.append('&youtube_pl=PLWJa48pm3noa-CVm1nZMEZUHcQTH795Pm')
		
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLE6B301EF25A1B959') #הדב פדינגטון
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir(addonString(10823).encode('utf-8'),list,17,'http://www.product-reviews.net/wp-content/userimages/2007/09/paddington.jpg',addonString(10823).encode('utf-8'),'1',0,fanart)
	
	'''הופה היי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL1236E31BAFB62B85') #הופה היי
	addDir('הופה היי',list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/e/ef/Hopa_Hey.jpg/250px-Hopa_Hey.jpg','הופה היי הייתה להקה ותוכנית טלוויזיה ישראלית מצליחה לילדים ולכל המשפחה אשר הופיעה וצולמה ברחבי ישראל במהלך שנות השמונים ושנות התשעים.[CR]סדרת הטלוויזיה של הופה היי הופקה לטלוויזיה מיוני 1986 עד מאי 1995 והכילה 63 פרקים. הסדרה שודרה בערוץ הראשון במסגרת מחלקת התוכניות לילדים ונוער.[CR]בעקבות הצלחת סדרת הטלוויזיה בקרב ילדי ישראל, במהלך שנות פעילותה הופיעה הלהקה ברחבי ישראל בשמונה מופעים מצליחים והוציאה שבעה אלבומים. מוצרים נלווים נוספים של הופה היי אשר נמכרו לאורך השנים כוללים ספרים, קלטות וידאו וחטיף שוקולד.','1',0,fanart)
	
	'''הזבלונים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL1236E31BAFB62B85')
	if 'English' in General_LanguageL:	
		list.append('&youtube_pl=PLBndX23tvlo8tNeHSxeWrBdjBDMTv6XlF') #S1
		list.append('&youtube_pl=PLM1bVm0b8Gm0VUSB9Qz7Z5JqVVmFWhj9a')
		list.append('&youtube_id=tihWbgMa-NQ')
		list.append('&youtube_id=1JoHFjtiLHE')
	if 'Greek' in General_LanguageL:	
		list.append('&youtube_id=Cszu-vXyg-A')
		
	addDir(addonString(10852).encode('utf-8'),list,17,'http://www.myfirsthomepage.co.il/mfhp/trend/image/ziblonim/banner.jpg',addonString(108520).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/3Vuj2hIfDtc/maxresdefault.jpg", default=background2))
	
	'''החיים עם לואי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyFE_bpQAmTft7NuZA7qBNBW')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLovF9Z5TJjw8d9PF_SmDtsdF6mTgtrL15')
		
	addDir(addonString(10817).encode('utf-8'),list,17,'http://ia.media-imdb.com/images/M/MV5BMTU1MzY1NjM3NF5BMl5BanBnXkFtZTcwNzY4NzEyMQ@@._V1_SX214_AL_.jpg',addonString(108170).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://thumbs01.myvideo.ge/screens/227/2265298.jpg", default=background2))
	
	'''החממה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%94%d7%97%d7%9e%d7%9e%d7%94&url=seriesId%3d2855906')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f349.jpg&mode=3&name=%d7%94%d7%97%d7%9e%d7%9e%d7%94-hahamama%2fseason%2f1&series_id=349&series_name=%d7%94%d7%97%d7%9e%d7%9e%d7%94-hahamama%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f349%2f%d7%94%d7%97%d7%9e%d7%9e%d7%94-hahamama%2fseason%2f1')
		
	addDir('החממה',list,6,'https://upload.wikimedia.org/wikipedia/he/thumb/5/5b/Hahamama.jpg/250px-Hahamama.jpg','החממה היא סדרת נוער ישראלית.[CR]הסדרה מתארת את עלילותיהם של בני נוער הלומדים בבית-ספר למנהיגים הנקרא "החממה" שעל שפת הכנרת.','1',0,getAddonFanart(background, custom="https://i.ytimg.com/vi/qhil5N9kWi8/maxresdefault.jpg", default=background2))
	
	
	
	'''החפרנים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2015%2f07%2f23%2fhafranim_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fthe-diggers-S1')
	addDir(addonString(10812).encode('utf-8'),list,6,'http://img.mako.co.il/2015/07/23/hafranim_f.jpg',addonString(108120).encode('utf-8'),'1',0,fanart)
	
	'''הטופוס'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL0975E268A42E4399')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL8229305931BB2E0B')
		
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLDyfEDDq7obVDwqQTJlwpNefhfb54eajN')
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLgrNRgZxdFPCodbntsO9Nep8hirCwF2wS')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyFuBlRvQYwlUdFEZgE4yUF4')
	addDir(addonString(10825).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/2/2d/Tofus.jpg',addonString(108250).encode('utf-8'),'1',0,fanart)
	
	'''הי-מן ושליטי היקום'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73014-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73014-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DHe-Man%20And%20The%20Masters%20Of%20The%20Universe%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fhe-man-and-the-masters-of-the-universe')

	addDir(addonString(10878).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/73014-3.jpg',addonString(108780).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73014-1.jpg", default=background2))
	
	'''היי ארנולד!'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F72005-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F72005-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DHey%20Arnold!%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fhey-arnold')

	addDir(addonString(10888).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/72005-1.jpg',addonString(108880).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/72005-1.jpg", default=background2))
	
	'''המופע של מר פיבודי ושרמן'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F301314-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F301314-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Mr.%20Peabody%20%26%20Sherman%20Show%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-new-mr.-peabody-and-sherman-show')
		
	addDir(addonString(10880).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/301314-1.jpg',addonString(108800).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/301314-3.jpg", default=background2))
	
	'''המופע של קליבלנד'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F93991-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F93991-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Cleveland%20Show%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-cleveland-show')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F22%2Fimage%2F555x418%2FThe_Cleveland_Show_.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Cleveland%20Show%20(2009%E2%80%932013)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fthe-cleveland-show-2009-2013-tv-series')
	addDir(addonString(10862).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/93991-1.jpg',addonString(108620).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/93991-2.jpg", default=background2))
	
	'''המלך היל'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73903-8.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73903-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DKing%20of%20the%20Hill%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fking-of-the-hill')
	addDir(addonString(10879).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/73903-2.jpg',addonString(108790).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73903-8.jpg", default=background2))
	
	'''The Tick'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLxqFxAMV_HrHDWuG0WdL4efHjEHXJ-ig0')
	if 'Russian' in General_LanguageL:	
		list.append('&youtube_pl=PLovF9Z5TJjw86v5oWnRwMjEIrwyuMc7Wu')
	addDir(addonString(10846).encode('utf-8'),list,6,'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/The_Tick_%28S%C3%A9rie_de_desenho_animado%29.jpg/250px-The_Tick_%28S%C3%A9rie_de_desenho_animado%29.jpg',addonString(108460).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES108F(General_LanguageL, background, background2) #הילדים מחדר 402

	'''הסוכן אנרי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e4%f1%e5%eb%ef%20%e4%f0%f8%e9&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2851924')
	addDir('הסוכן אנרי',list,6,'','','1',0,fanart)
	
	'''הצחוקייה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e5%e9%f7%e8%e5%f8%e9%e5%f1&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1744947')
	addDir('הצחוקייה',list,6,'','','1',0,fanart)
	
	
	'''הקבצים הסודיים של כלבי מרגלים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLyuJqPammrxl2ShakPFQH-4yMAdtCEXE9')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
		
		
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=PLIUOFDAQm0tdAJdzaD_GMX82UXR5DBR5w')
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLWMCwroYhJSoepoqlLT3za1PpmYpnjCR3')
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLuQquogfWXdssgPhLIBlHFftuUTB-kfUn')	
		
	addDir(addonString(10824).encode('utf-8'),list,17,'https://s-media-cache-ak0.pinimg.com/736x/bc/17/11/bc17115194d6d15c98673f790141849c.jpg',addonString(108240).encode('utf-8'),'1',0,fanart)
	
	'''הקומדי סטור'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLKMFPiSCwUk35KmF0lRIeW641IbkseuER')
		list.append('&youtube_id=OnTGfthIrSE')
		list.append('&youtube_id=xyo6FLeZ3Aw')
		list.append('&youtube_id=aSke8kN719Q')
		list.append('&youtube_id=Ui6doOZZdgg')
		list.append('&youtube_id=kQ-w5sdqOZ8')
		list.append('&youtube_id=eyUuh89Ivi0')
		list.append('&youtube_id=Tciexh7ZTio')
		list.append('&youtube_id=bCGekFm2_w4')
		list.append('&youtube_id=xlbcC9iQA0M')
	addDir(addonString(10807).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/5/58/Komedi.jpg',addonString(108070).encode('utf-8'),'1',0,fanart)
	
	'''הרפתקאות קראט'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLa8HWWMcQEGShWcQbipVlr3uEEnr0bLeh')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL75Ev9SzNPCbBph8ohUx7PztLgGIqqxkS')
	addDir(addonString(10813).encode('utf-8'),list,17,'http://pbskids.org/apps/media/apps/WK_World_PBS_Apps-1024X1024.png',addonString(108130).encode('utf-8'),'1',0,fanart)
	
	'''ויקטוריוס'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e5%e9%f7%e8%e5%f8%e9%e5%f1&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1744947')
	addDir('ויקטוריוס',list,6,'','','1',0,fanart)
	
	'''חבורת הספסל האחורי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e7%e1%e5%f8%fa%20%e4%f1%f4%f1%ec%20%e4%e0%e7%e5%f8%e9&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2825941')
	addDir('חבורת הספסל האחורי',list,6,'','','1',0,fanart)
	
	'''חידון התנך'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL51YAgTlfPj51ODBIMhtOF_lYxjS1cuQh')
	addDir(addonString(10809).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Peresohad1985hidon.jpg/350px-Peresohad1985hidon.jpg',addonString(108090).encode('utf-8'),'1',0,fanart)
	
	'''טופו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL0Z8ES1NjCOLmnEaxOl5fWHvKP62ky3Bt')
	addDir('טופו',list,17,'https://i.ytimg.com/vi/D0e3ltYvggw/hqdefault.jpg','','1',0,fanart)
	
	'''כמעט מלאכים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f25.jpg&mode=3&name=%d7%9b%d7%9e%d7%a2%d7%98-%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-casi-angeles%2fseason%2f1&series_id=25&series_name=%d7%9b%d7%9e%d7%a2%d7%98-%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-casi-angeles%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f25%2f%d7%9b%d7%9e%d7%a2%d7%98-%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-casi-angeles%2fseason%2f1')
	addDir('כמעט מלאכים',list,17,thumb,'','1',0,fanart)
	
	'''לואי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_id=In78b28tpeQ')
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	addDir(addonString(10826).encode('utf-8'),list,17,'https://i.ytimg.com/vi/MvItl_ca-J8/hqdefault.jpg',addonString(108260).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://s2.dmcdn.net/OGBIH/1280x720-gt2.jpg", default=background2))
	
	'''חי ב-LA LA לנד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%9e%d7%99%d7%9b%d7%9c%20%d7%94%d7%a7%d7%98%d7%a0%d7%94%20%d7%95%d7%94%d7%98%d7%95%d7%a0%d7%98%d7%95%d7%a0%d7%99%d7%9d&url=seasonId%3d2890384')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%97%d7%99%20%d7%91-%20LA%20LA%20%d7%9c%d7%a0%d7%93%202&url=seasonId%3d2855896')
	addDir('חי ב-LA LA לנד',list,6,'','','1',0,fanart)
	
	'''יומני החופש הגדול'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=5&module=wallavod&name=%d7%99%d7%95%d7%9e%d7%a0%d7%99%20%d7%94%d7%97%d7%95%d7%a4%d7%a9%20%d7%94%d7%92%d7%93%d7%95%d7%9c&url=seriesId%3d2855910')
	addDir('יומני החופש הגדול',list,6,'','','1',0,fanart)
	
	'''יפניק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%e9%f4%f0%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1878402')
		list.append('&youtube_pl=PLuQCYUv97StS-YtE8BYNUpLIxKrGOBAe6')
	addDir(addonString(10814).encode('utf-8'),list,17,'',addonString(108140).encode('utf-8'),'1',0,fanart)
	
	'''לא מדהימה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ec%e0%20%ee%e3%e4%e9%ee%e4&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1688289')
	addDir('לא מדהימה',list,6,'','','1',0,fanart)
	
	'''לתפוס את בלייק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ec%fa%f4%e5%f1%20%e0%fa%20%e1%ec%e9%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2853374')
	addDir('לתפוס את בלייק',list,6,'','','1',0,fanart)
	
	'''מבצע קיפוד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f428.jpg&mode=3&name=%d7%9e%d7%91%d7%a6%d7%a2-%d7%a7%d7%99%d7%a4%d7%95%d7%93-mivtza-kipod%2fseason%2f1&series_id=428&series_name=%d7%9e%d7%91%d7%a6%d7%a2-%d7%a7%d7%99%d7%a4%d7%95%d7%93-mivtza-kipod%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f428%2f%d7%9e%d7%91%d7%a6%d7%a2-%d7%a7%d7%99%d7%a4%d7%95%d7%93-mivtza-kipod%2fseason%2f1')
		list.append('&youtube_pl=PL-SBsAk8heRkmohaurMbQdGHXoF-W4sHJ') #S1
		list.append('&youtube_pl=PL-SBsAk8heRlmbAFxsqL20CD3KTM9_a6i') #S2
		list.append('&youtube_pl=PL-PL_gKiiTUgBvZVgma7WShCSNpAfUrYhyEb') #S3
		list.append('&youtube_pl=PL-PLuzkzb0C0aRLZTbIC4vNtQKbHUkq1nTWI') #S3
		
	addDir('מבצע קיפוד',list,6,thumb,'מבצע קיפוד היא סדרת הרפתקאות חינוכית לילדים, ששודרה בערוץ לוגי. הסדרה היא סדרת בת של הסדרה "נשרים".','1',0,fanart)
	
	'''מה פתאום'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2013%2f08%2f15%2fma_pitom_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fma-pitom-s1')
	addDir(addonString(10834).encode('utf-8'),list,6,'http://img.mako.co.il/2008/08/06/replacement-b.jpg',addonString(108340).encode('utf-8'),'1',0,fanart)
	
	'''מועדון החנונים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLBaGngHK8wj2Ejhha53BVxYYCyCm-Y2y0') #S1
		list.append('&youtube_pl=PLKMFPiSCwUk0myYc1Z8oPLGO6hXJdf5uv') #S2
		list.append('&youtube_pl=PLKMFPiSCwUk22xxgMwcNShgeBYNSfotbB')
		list.append('&youtube_id=8xwzlXqOzwM') #S2E1
		
	addDir(addonString(10827).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/5/5e/%D7%9E%D7%95%D7%A2%D7%93%D7%95%D7%9F_%D7%94%D7%97%D7%A0%D7%95%D7%A0%D7%99%D7%9D.jpg/250px-%D7%9E%D7%95%D7%A2%D7%93%D7%95%D7%9F_%D7%94%D7%97%D7%A0%D7%95%D7%A0%D7%99%D7%9D.jpg',addonString(108270).encode('utf-8'),'1',0,fanart)
	
	'''מיסטר בין'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78158-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78158-3.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMr.%20Bean%3A%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fmr-bean-animated-series')
		list.append('&custom8=plugin://plugin.video.cartoonson/?description&iconimage=http%3A%2F%2Fwww.cartoonson.com%2F_resources%2FCartoons%2Fshow%2F44%2Fimage%2F555x418%2FMr.-Bean1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DMr.%20Bean%20-%20The%20Animated%20Series%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.cartoonson.com%2Fcartoons%2Fview%2Fid%2Fmr-bean-the-animated-series')
	addDir(addonString(10889).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/78158-3.jpg',addonString(108890).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/78158-2.jpg", default=background2))
	
	'''מרטין על הבוקר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1056.jpg&mode=3&name=%d7%9e%d7%a8%d7%98%d7%99%d7%9f-%d7%a2%d7%9c-%d7%94%d7%91%d7%95%d7%a7%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martin-morning%2fseason%2f1&series_id=1056&series_name=%d7%9e%d7%a8%d7%98%d7%99%d7%9f-%d7%a2%d7%9c-%d7%94%d7%91%d7%95%d7%a7%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martin-morning%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1056%2f%d7%9e%d7%a8%d7%98%d7%99%d7%9f-%d7%a2%d7%9c-%d7%94%d7%91%d7%95%d7%a7%d7%a8-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martin-morning%2fseason%2f1')
		list.append('&youtube_pl=PL46680F40368D0F46')
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLRHlpEIdAaUJPRYLuwcZWv2yqJmZdOE3S') #French
	addDir(addonString(10829).encode('utf-8'),list,17,thumb,addonString(108290).encode('utf-8'),'1',0,fanart)
	
	'''מריו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2018.jpg&mode=3&name=%d7%9e%d7%a8%d7%99%d7%95-mario%2fseason%2f1&series_id=2018&series_name=%d7%9e%d7%a8%d7%99%d7%95-mario%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2018%2f%d7%9e%d7%a8%d7%99%d7%95-mario%2fseason%2f1')
		list.append('&dailymotion_pl=x45ton')
		list.append('&dailymotion_pl=x45p6g')
	addDir(addonString(10832).encode('utf-8'),list,17,thumb,addonString(108320).encode('utf-8'),'1',0,fanart)
	
	'''מר קו*'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f928.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=928&series_name=%d7%9e%d7%a8-%d7%a7%d7%95-la-linea%2fseason%2f1&summary=%d7%9e%d7%a8%20%d7%a7%d7%95%20%d7%94%d7%95%d7%90%20%d7%90%d7%99%d7%a9%20%d7%9e%d7%a6%d7%95%d7%99%d7%a8%20%d7%94%d7%94%d7%95%d7%9c%d7%9a%20%d7%9c%d7%90%d7%95%d7%a8%d7%9a%20%d7%a7%d7%95%20%d7%90%d7%95%d7%a4%d7%a7%d7%99%20%d7%95%d7%90%d7%99%d7%a0%d7%a1%d7%95%d7%a4%d7%99%2c%20%d7%9b%d7%90%d7%a9%d7%a8%20%d7%94%d7%95%d7%90%20%d7%9e%d7%94%d7%95%d7%95%d7%94%2c%20%d7%91%d7%90%d7%95%d7%aa%d7%95%20%d7%94%d7%96%d7%9e%d7%9f%2c%20%d7%97%d7%9c%d7%a7%20%d7%9e%d7%94%d7%a7%d7%95%20%d7%a2%d7%9c%d7%99%d7%95%20%d7%94%d7%95%d7%90%20%d7%94%d7%95%d7%9c%d7%9a.%20%d7%91%d7%9b%d7%9c%20%d7%a4%d7%a2%d7%9d%20%d7%a9%d7%9e%d7%a8%20%d7%a7%d7%95%20%d7%a0%d7%aa%d7%a7%d7%9c%20%d7%91%d7%93%d7%a8%d7%9b%d7%95%20%d7%91%d7%9e%d7%9b%d7%a9%d7%95%d7%9c%d7%99%d7%9d%20%d7%94%d7%95%d7%90%20%d7%a0%d7%95%d7%94%d7%92%20%d7%9c%d7%a4%d7%a0%d7%95%d7%aa%20%d7%9c%d7%a6%d7%99%d7%99%d7%a8%20%d7%a2%d7%9c%20%d7%9e%d7%a0%d7%aa%20%d7%a9%d7%96%d7%94%20%d7%99%d7%99%d7%a6%d7%a8%20%d7%a2%d7%91%d7%95%d7%a8%d7%95%20%d7%90%d7%aa%20%d7%94%d7%a4%d7%aa%d7%a8%d7%95%d7%9f.%20%d7%90%d7%9d%20%d7%9e%d7%a8%20%d7%a7%d7%95%20%d7%90%d7%99%d7%a0%d7%95%20%d7%9e%d7%a8%d7%95%d7%a6%d7%94%20%d7%9e%d7%94%d7%a4%d7%aa%d7%a8%d7%95%d7%a0%d7%95%d7%aa%20%d7%a9%d7%9c%20%d7%94%d7%9e%d7%a6%d7%99%d7%99%d7%a8%20%d7%95%d7%9e%d7%94%d7%97%d7%a4%d7%a6%d7%99%d7%9d%20%d7%95%d7%94%d7%9e%d7%9b%d7%a9%d7%95%d7%9c%d7%99%d7%9d%20%d7%a9%d7%96%d7%94%20%d7%9e%d7%a2%d7%9e%d7%99%d7%93%20%d7%9c%d7%a4%d7%a0%d7%99%d7%95%2c%20%d7%94%d7%95%d7%90%20%d7%a4%d7%95%d7%aa%d7%97%20%d7%90%d7%aa%20%d7%a4%d7%99%d7%95%20%d7%91%d7%9e%d7%99%d7%9c%d7%95%d7%aa%20%d7%96%d7%a2%d7%9d%20%d7%95%d7%a7%d7%9c%d7%9c%d7%95%d7%aa%20%d7%91%d7%a9%d7%a4%d7%aa%d7%95%20%d7%94%d7%9c%d7%90%20%d7%9e%d7%95%d7%91%d7%a0%d7%aa.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f928%2f%d7%9e%d7%a8-%d7%a7%d7%95-la-linea%2fseason%2f1')
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL69CA847A1767B3D5') #Italian
		list.append('&youtube_pl=PL2346AC7ACF71633B') #Italian
	addDir(addonString(10830).encode('utf-8'),list,17,thumb,addonString(108300).encode('utf-8'),'1',0,fanart)
	
	'''מר שיהוק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f2101.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=2101&series_name=%d7%9e%d7%a8-%d7%a9%d7%99%d7%94%d7%95%d7%a7-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-mr-hiccup%2fseason%2f1&summary=%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%9e%d7%aa%d7%9e%d7%a7%d7%93%d7%aa%20%d7%91%d7%97%d7%99%d7%99%d7%95%20%d7%a9%d7%9c%20%d7%9e%d7%a8%20%d7%a9%d7%99%d7%94%d7%95%d7%a7%20%d7%91%d7%a2%d7%9c%20%d7%94%d7%a9%d7%99%d7%94%d7%95%d7%a7%d7%99%d7%9d%20%d7%94%d7%9b%d7%a8%d7%95%d7%a0%d7%99%d7%99%d7%9d%20%d7%95%d7%9c%d7%93%d7%a8%d7%9a%20%d7%a9%d7%91%d7%94%20%d7%94%d7%95%d7%90%20%d7%9e%d7%95%d7%a6%d7%99%d7%90%20%d7%90%d7%aa%20%d7%a2%d7%a6%d7%9e%d7%95%20%d7%9e%d7%94%d7%9e%d7%a6%d7%91%d7%99%d7%9d%20%d7%94%d7%9e%d7%91%d7%99%d7%9b%d7%99%d7%9d%20%d7%95%d7%94%d7%9c%d7%90%20%d7%a7%d7%9c%d7%99%d7%9d%20%d7%90%d7%a9%d7%a8%20%d7%9e%d7%98%d7%a8%d7%93%20%d7%96%d7%94%20%d7%9e%d7%95%d7%91%d7%99%d7%9c%20%d7%90%d7%95%d7%aa%d7%95%20%d7%90%d7%9c%d7%99%d7%94%d7%9d.%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%94%d7%99%d7%92%d7%9e%d7%9c%20%d7%9e%d7%94%d7%a9%d7%99%d7%94%d7%95%d7%a7%d7%99%d7%9d%20%d7%94%d7%9b%d7%a8%d7%95%d7%a0%d7%99%d7%99%d7%9d%20%d7%9e%d7%94%d7%9d%20%d7%94%d7%95%d7%90%20%d7%a1%d7%95%d7%91%d7%9c%2c%20%d7%91%d7%9b%d7%9c%20%d7%a4%d7%a8%d7%a7%20%d7%9e%d7%a8%20%d7%a9%d7%99%d7%94%d7%95%d7%a7%20%d7%9e%d7%a0%d7%a1%d7%94%20%d7%93%d7%91%d7%a8%d7%99%d7%9d%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%a9%d7%99%d7%a2%d7%96%d7%a8%d7%95%20%d7%9c%d7%94%d7%a4%d7%a1%d7%99%d7%a7%20%d7%90%d7%aa%20%d7%94%d7%a9%d7%99%d7%94%d7%95%d7%a7%d7%99%d7%9d%2c%20%d7%9c%d7%9c%d7%90%20%d7%94%d7%a6%d7%9c%d7%97%d7%94%20%d7%a8%d7%91%d7%94.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f2101%2f%d7%9e%d7%a8-%d7%a9%d7%99%d7%94%d7%95%d7%a7-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-mr-hiccup%2fseason%2f1')
		list.append('&youtube_pl=PLxixvuzGJWPNpD1OdK5x4LoqYKjfNUTNy')
	addDir(addonString(10831).encode('utf-8'),list,17,thumb,addonString(108310).encode('utf-8'),'1',0,fanart)
	
	'''מרוין מרוין'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ee%f8%e5%e5%e9%ef%20%ee%f8%e5%e5%e9%ef&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2753755')
		list.append('&youtube_pl=') #?
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=') #
	
	addDir('מרוין מרוין',list,6,'','','1',0,fanart)
	
	'''מרתה מדברת'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1640.jpg&mode=3&name=%d7%9e%d7%a8%d7%aa%d7%94-%d7%9e%d7%93%d7%91%d7%a8%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martha-speaks%2fseason%2f1&series_id=1640&series_name=%d7%9e%d7%a8%d7%aa%d7%94-%d7%9e%d7%93%d7%91%d7%a8%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martha-speaks%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1640%2f%d7%9e%d7%a8%d7%aa%d7%94-%d7%9e%d7%93%d7%91%d7%a8%d7%aa-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-martha-speaks%2fseason%2f1')
		list.append('&youtube_pl=PL_8KXLhQVQMLtfN5bkh11lSA6Awg5rt9y')
	addDir(addonString(10833).encode('utf-8'),list,17,thumb,addonString(108330).encode('utf-8'),'1',0,fanart)
	
	'''משלים שועליים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f986.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=986&series_name=%d7%9e%d7%a9%d7%9c%d7%99%d7%9d-%d7%a9%d7%95%d7%a2%d7%9c%d7%99%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-meshalim-shualyim%2fseason%2f1&summary=%d7%a1%d7%93%d7%a8%d7%aa%20%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94%20%d7%91%d7%a4%d7%9c%d7%a1%d7%98%d7%99%d7%a0%d7%94%20%d7%a9%d7%a0%d7%95%d7%a6%d7%a8%d7%94%20%d7%a2%d7%9c%20%d7%99%d7%93%d7%99%20%d7%94%d7%90%d7%a0%d7%99%d7%9e%d7%98%d7%95%d7%a8%20%d7%a8%d7%95%d7%a0%d7%99%20%d7%90%d7%95%d7%a8%d7%9f%20%d7%a2%d7%91%d7%95%d7%a8%d7%94%d7%a2%d7%a8%d7%95%d7%a5%20%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%9f&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f986%2f%d7%9e%d7%a9%d7%9c%d7%99%d7%9d-%d7%a9%d7%95%d7%a2%d7%9c%d7%99%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-meshalim-shualyim%2fseason%2f1')
		list.append('&youtube_pl=PL1F479A5492E26B5C') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLROxl1XYA9feI1PPaaOtNmxMssCdacnNX') #English
		list.append('&youtube_pl=PL2tnhrkjPvkutDzPrOwhdiJWBNluZSVaM') #English
	addDir(addonString(10835).encode('utf-8'),list,17,thumb,addonString(108990).encode('utf-8'),'1',0,fanart)
	
	'''משפחת כספי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%ee%f9%f4%e7%fa%20%eb%f1%f4%e9&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2565349')
		list.append('&youtube_pl=') #?
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=') #
	
	addDir('משפחת כספי',list,6,'','','1',0,fanart)
	
	'''נביא החושך''' #Sdarot
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLwqmbDQfp96ieQhPFLZD2oaOTYMDLhwJ4') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLQH9_jN7uLguhvbpxnjMoruzg9xTY3rNi') #English
		list.append('&youtube_pl=PLuQ1zyXvUqEiZaTQQVwyj0JRjTqKktBXz') #English
	addDir(addonString(10839).encode('utf-8'),list,17,thumb,addonString(108390).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES107N(General_LanguageL, background, background2) #נווה עצלנות
	
	'''נוי והדר''' #WALLA VOD
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1454.jpg&mode=3&name=%d7%a0%d7%95%d7%99-%d7%95%d7%94%d7%93%d7%a8-noy-ve-hadar%2fseason%2f1&series_id=1454&series_name=%d7%a0%d7%95%d7%99-%d7%95%d7%94%d7%93%d7%a8-noy-ve-hadar%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1454%2f%d7%a0%d7%95%d7%99-%d7%95%d7%94%d7%93%d7%a8-noy-ve-hadar%2fseason%2f1')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a0%d7%95%d7%99%20%d7%95%d7%94%d7%93%d7%a8&url=seasonId%3d2855980')
		list.append('&youtube_id=Z51T2XotMoM')
		list.append('&youtube_id=tEkfczvaoZQ')
		list.append('&youtube_id=tEkfczvaoZQ')
	addDir(addonString(10842).encode('utf-8'),list,17,thumb,addonString(108420).encode('utf-8'),'1',0,fanart)

	''''נאנוק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL_8KXLhQVQMJJ4nHubadbykzbHhzzmUPu')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1315.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1315&series_name=%d7%a0%d7%90%d7%a0%d7%95%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91-nanook%2fseason%2f1&summary=%d7%91%d7%9e%d7%a8%d7%97%d7%91%d7%99%20%d7%94%d7%a9%d7%9c%d7%92%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%a7%d7%a0%d7%93%d7%94%20%d7%97%d7%99%20%d7%a9%d7%91%d7%98%20%d7%a9%d7%9c%20%d7%90%d7%a0%d7%a9%d7%99%d7%9d%20%d7%aa%d7%9e%d7%99%d7%9e%d7%99%d7%9d%20%d7%95%d7%a6%d7%99%d7%99%d7%93%d7%99%d7%9d%20%d7%a7%d7%a9%d7%95%d7%97%d7%99%d7%9d%20%d7%94%d7%9d%20%d7%92%d7%a8%d7%99%d7%9d%20%d7%91%d7%90%d7%99%d7%92%d7%9c%d7%95%20%d7%95%d7%9e%d7%a1%d7%aa%d7%a4%d7%a7%d7%99%d7%9d%20%d7%91%d7%9e%d7%95%d7%a2%d7%98.%20%d7%90%d7%9a%20%d7%94%d7%93%d7%91%20%d7%94%d7%92%d7%93%d7%95%d7%9c%20%d7%95%d7%95%d7%90%d7%a7%20%d7%93%d7%9e%d7%95%d7%9f%20%d7%9e%d7%97%d7%a1%d7%9c%20%d7%90%d7%aa%20%d7%9b%d7%9c%20%d7%91%d7%a2%d7%9c%d7%99%20%d7%94%d7%97%d7%99%d7%99%d7%9d%20%d7%91%d7%a1%d7%91%d7%99%d7%91%d7%94.%20%d7%a7%d7%90%d7%95%d7%a0%d7%94%20%d7%94%d7%9c%d7%95%d7%97%d7%9d%20%d7%91%d7%97%d7%a8%20%d7%9c%d7%a6%d7%90%d7%aa%20%d7%9c%d7%a6%d7%95%d7%93%20%d7%90%d7%95%d7%aa%d7%95.%20%d7%90%d7%9a%20%d7%92%d7%9d%20%d7%a0%d7%90%d7%a0%d7%95%d7%a7%20%d7%91%d7%9f%20%d7%94-12%20%d7%99%d7%95%d7%a6%d7%90%20%d7%9c%d7%a6%d7%95%d7%93%20%d7%95%d7%9e%d7%a7%d7%95%d7%94%20%d7%a9%d7%94%d7%95%d7%90%20%d7%96%d7%94%20%d7%a9%d7%99%d7%a6%d7%95%d7%93%20%d7%90%d7%aa%20%d7%94%d7%93%d7%91%20%d7%94%d7%90%d7%9b%d7%96%d7%a8.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1315%2f%d7%a0%d7%90%d7%a0%d7%95%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91-nanook%2fseason%2f1')
	addDir(addonString(10836).encode('utf-8'),list,17,thumb,addonString(107540).encode('utf-8'),'1',0,fanart)
	
	'''נאס"א : העולם שלנו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1910.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1910&series_name=%d7%a0%d7%90%d7%a1-%d7%90-%d7%94%d7%a2%d7%95%d7%9c%d7%9d-%d7%a9%d7%9c%d7%a0%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-nasa-our-world%2fseason%2f1&summary=%d7%97%d7%99%d7%a0%d7%95%d7%9b%d7%99%d7%aa%2c%20%d7%a0%d7%90%d7%a1%22%d7%90%20%d7%95%d7%a1%d7%95%d7%9b%d7%a0%d7%95%d7%aa%20%d7%94%d7%97%d7%9c%d7%9c%20%d7%94%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99%d7%aa%20%d7%9e%d7%a6%d7%99%d7%92%d7%95%d7%aa%3a%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d%20%d7%a9%d7%9c%d7%a0%d7%95.%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%a1%d7%a8%d7%98%d7%95%d7%a0%d7%99%d7%9d%20%d7%9c%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%94%d7%9e%d7%a1%d7%91%d7%99%d7%a8%d7%94%20%d7%aa%d7%95%d7%a4%d7%a2%d7%95%d7%aa%2c%20%d7%92%d7%95%d7%a8%d7%9e%d7%99%d7%9d%2c%20%d7%aa%d7%95%d7%a6%d7%90%d7%95%d7%aa%20%d7%95%d7%a9%d7%99%d7%9e%d7%95%d7%a9%d7%99%d7%9d%20%d7%9c%d7%a4%d7%99%d7%aa%d7%95%d7%97%d7%99%d7%9d%20%d7%94%d7%98%d7%9b%d7%a0%d7%95%d7%9c%d7%92%d7%99%d7%9d%20%d7%94%d7%9b%d7%99%20%d7%97%d7%93%d7%a9%d7%99%d7%9d%20%d7%95%d7%97%d7%93%d7%a9%d7%a0%d7%99%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1910%2f%d7%a0%d7%90%d7%a1-%d7%90-%d7%94%d7%a2%d7%95%d7%9c%d7%9d-%d7%a9%d7%9c%d7%a0%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-nasa-our-world%2fseason%2f1')
		list.append('&youtube_pl=PLTnbwiCw-mMTMyud7eaLkzfQBN5gMwTIE')
	addDir(addonString(10837).encode('utf-8'),list,17,thumb,addonString(108370).encode('utf-8'),'1',0,fanart)
	
	'''נסקר רייסר'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLZs0gQed9tMSLhHXasmy0gSjgs_vv9sU5') #English
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PLWMCwroYhJSqSut59L-Sxr0A5IR-0XWeE') #Serbian
	addDir(addonString(10843).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/7/7f/Nascar_racers_title.png',addonString(108430).encode('utf-8'),'1',0,fanart)
	
	'''סאם וקאט'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f1%e0%ed%20%e5%f7%e0%e8&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2741687')
		list.append('&youtube_pl=') #?
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=') #
	
	addDir('סאם וקאט',list,6,'','','1',0,fanart)
	
	'''סבבה בנט''' #MAKO
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f891.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=891&series_name=%d7%a1%d7%91%d7%91%d7%94-%d7%91%d7%a0%d7%98-sababa-benet%2fseason%2f1&summary=%d7%aa%d7%95%d7%9b%d7%a0%d7%99%d7%aa%20%d7%a7%d7%95%d7%9e%d7%99%d7%aa%20%d7%95%d7%9e%d7%a6%d7%97%d7%99%d7%a7%d7%94%20%d7%a2%d7%9d%20%d7%94%d7%9e%d7%a0%d7%97%d7%99%d7%9d%20%d7%90%d7%95%d7%93%d7%99%20%d7%95%d7%90%d7%91%d7%99%d7%a2%d7%93&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f891%2f%d7%a1%d7%91%d7%91%d7%94-%d7%91%d7%a0%d7%98-sababa-benet%2fseason%2f1')
		list.append('&youtube_id=IJ5pD7Jyzxw')
		list.append('&youtube_id=ZBnOdu3L3SI')
		list.append('&youtube_id=MM3ZkbrHJlo')
		list.append('&youtube_id=uIXc-jhmMTk')
	addDir(addonString(10844).encode('utf-8'),list,17,thumb,addonString(108440).encode('utf-8'),'1',0,fanart)
	
	
	'''סדריק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f563.jpg&mode=3&name=%d7%a1%d7%93%d7%a8%d7%99%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91-cedric%2fseason%2f1&series_id=563&series_name=%d7%a1%d7%93%d7%a8%d7%99%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91-cedric%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f563%2f%d7%a1%d7%93%d7%a8%d7%99%d7%a7-%d7%9e%d7%93%d7%95%d7%91%d7%91-cedric%2fseason%2f1')
		list.append('&youtube_pl=PLIR_swtdpOGlM5pCPxgrVF0PZEHo2ajHn') #Hebrew
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLiItfFtbus3DFOhVyy075yXjvAy9XJrG5') #French
		list.append('&youtube_pl=PLia0fh24w3OtjX-rI3OFpHNGGH65Zbdtz') #French
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLKGaRn_uvwDfCDN0VaGqpVi62m6ufUny6') #Turkish
		list.append('&youtube_pl=PLHDypsdYQJJDgKLp0DquYdZbbnc1YSNue') #Turkish
	addDir(addonString(10838).encode('utf-8'),list,17,thumb,addonString(108380).encode('utf-8'),'1',0,fanart)
	
	'''סול איטר'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f657.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=657&series_name=soul-eater-%d7%a1%d7%95%d7%9c-%d7%90%d7%99%d7%98%d7%a8-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary=%d7%94%d7%a2%d7%9c%d7%99%d7%9c%d7%94%20%d7%a2%d7%95%d7%a7%d7%91%d7%aa%20%d7%90%d7%97%d7%a8%20%d7%a1%d7%99%d7%a4%d7%95%d7%a8%d7%9d%20%d7%a9%d7%9c%20%d7%a9%d7%9c%d7%95%d7%a9%d7%94%20%d7%a6%d7%95%d7%95%d7%aa%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%aa%d7%9c%d7%9e%d7%99%d7%93%d7%99%d7%9d%20%d7%94%d7%9c%d7%95%d7%9e%d7%93%d7%99%d7%9d%20%d7%91%d7%9e%d7%9b%d7%9c%d7%9c%d7%aa%20%d7%90%d7%9c%20%d7%94%d7%9e%d7%95%d7%95%d7%aa%20%d7%9c%d7%a0%d7%a9%d7%a7%d7%99%d7%9d%20%d7%95%d7%90%d7%93%d7%95%d7%a0%d7%99%d7%9d.%20%d7%9e%d7%90%d7%a7%d7%94%20%d7%90%d7%9c%d7%91%d7%a8%d7%9f%20%d7%95%d7%90%d7%9b%d7%9c%d7%9f%20%d7%94%d7%a0%d7%a9%d7%9e%d7%95%d7%aa%2c%20%d7%a9%d7%97%d7%95%d7%a8%20%d7%94%d7%9b%d7%95%d7%9b%d7%91%20%d7%95%d7%a6%d7%95%d7%91%d7%90%d7%a7%d7%99%20%d7%95%d7%94%d7%99%d7%9c%d7%93%20%d7%9e%d7%95%d7%95%d7%aa%20%d7%95%d7%94%d7%90%d7%97%d7%99%d7%95%d7%aa%20%d7%aa%d7%95%d7%9e%d7%a4%d7%a1%d7%95%d7%9f%20%d7%a0%d7%9c%d7%97%d7%9e%d7%99%d7%9d%20%d7%99%d7%97%d7%93%20%d7%a2%d7%9c%20%d7%9e%d7%a0%d7%aa%20%d7%9c%d7%99%d7%a6%d7%95%d7%a8%20%d7%97%d7%a8%d7%9e%d7%a9%20%d7%9e%d7%95%d7%95%d7%aa%2c%20%d7%a0%d7%a9%d7%a7%20%d7%91%d7%a2%d7%9c%20%d7%a2%d7%95%d7%a6%d7%9e%d7%94%20%d7%92%d7%91%d7%95%d7%94%20%d7%a9%d7%99%d7%a9%d7%9e%d7%a9%20%d7%90%d7%aa%20%d7%90%d7%9c%20%d7%94%d7%9e%d7%95%d7%95%d7%aa%20%d7%91%d7%a2%d7%a6%d7%9e%d7%95.%20%d7%9b%d7%93%d7%99%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%96%d7%90%d7%aa%20%d7%a2%d7%9c%d7%99%d7%94%d7%9d%20%d7%9c%d7%90%d7%a1%d7%95%d7%a3%2099%20%d7%a0%d7%a9%d7%9e%d7%95%d7%aa%20%d7%90%d7%93%d7%9d%20%d7%a9%d7%94%d7%95%d7%a9%d7%97%d7%aa%d7%95%20%d7%95%d7%94%d7%a4%d7%9b%d7%95%20%d7%9c%d7%91%d7%99%d7%a6%d7%99%20%d7%a9%d7%93%2c%20%d7%95%d7%a0%d7%a9%d7%9e%d7%94%20%d7%90%d7%97%d7%aa%20%d7%a9%d7%9c%20%d7%9e%d7%9b%d7%a9%d7%a4%d7%94%2c%20%d7%90%d7%9a%20%d7%91%d7%93%d7%a8%d7%9b%d7%9d%20%d7%a2%d7%95%d7%9e%d7%93%d7%99%d7%9d%20%d7%a7%d7%a9%d7%99%d7%99%d7%9d%20%d7%a9%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%91%d7%9c%d7%aa%d7%99%20%d7%a6%d7%a4%d7%95%d7%99%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f657%2fsoul-eater-%d7%a1%d7%95%d7%9c-%d7%90%d7%99%d7%98%d7%a8-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PL438F23E3CAF45E30') #?
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLRncpcX6yCQIjAlkwY0jt4Ojb4hfVFio5') #English
		list.append('&youtube_pl=ELl52PjjPiC8I') #?
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=PLFYo6tyrrt1IiiOZrzmFTJYtIXwXRhUNi') #אוזבקית
	
	addDir(addonString(10854).encode('utf-8'),list,17,thumb,addonString(108540).encode('utf-8'),'1',0,fanart)
	
	'''סופר סטרייקה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1566.jpg&mode=3&name=%d7%a1%d7%95%d7%a4%d7%a8-%d7%a1%d7%98%d7%a8%d7%99%d7%99%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-supa-strikas%2fseason%2f1&series_id=1566&series_name=%d7%a1%d7%95%d7%a4%d7%a8-%d7%a1%d7%98%d7%a8%d7%99%d7%99%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-supa-strikas%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1566%2f%d7%a1%d7%95%d7%a4%d7%a8-%d7%a1%d7%98%d7%a8%d7%99%d7%99%d7%a7%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91-supa-strikas%2fseason%2f1')
		list.append('&youtube_pl=PLU6_PRY_7y1TQMr67fJ6WC2mzkqtVyU3B')
		list.append('&youtube_pl=PLKMFPiSCwUk3bjgDUSlTPskV9rA74nBiB')
		
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLJbBhDouIDY2moXY4n3F-px9zd-66RDP9') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLJbBhDouIDY1KBvLTtnqihGTP2uxoVTJB') #Spanish
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLJbBhDouIDY2b7rgjhkpgAJIWY5Vos-3j') #Portuguese
	if 'Polski' in General_LanguageL:
		list.append('&youtube_pl=PLJbBhDouIDY33fDF10-RtrFj9jivfiwH7') #Polski
	addDir(addonString(10840).encode('utf-8'),list,17,thumb,addonString(108400).encode('utf-8'),'1',0, fanart)
	
	'''סנג'אי וקרייג''' #NICK
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f1%f0%e2%27%e0%e9%20%e5%f7%f8%e9%e9%e2&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2741715')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1788.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1788&series_name=%d7%a1%d7%a0%d7%92-%d7%90%d7%99-%d7%95%d7%a7%d7%a8%d7%99%d7%99%d7%92-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-sanjay-and-craig%2fseason%2f1&summary=%d7%a1%d7%a0%d7%92%27%d7%90%d7%99%20(%d7%94%d7%94%d7%95%d7%93%d7%99%20%d7%94%d7%9b%d7%99%20%d7%a7%d7%95%d7%9c%20%d7%91%d7%a1%d7%91%d7%99%d7%91%d7%94)%20%d7%95%d7%a7%d7%a8%d7%99%d7%99%d7%92%20(%d7%a9%d7%94%d7%95%d7%90%20%d7%91%d7%9e%d7%a7%d7%a8%d7%94%20%d7%a0%d7%97%d7%a9%20%d7%9e%d7%93%d7%91%d7%a8)%20%d7%94%d7%9d%20%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%94%d7%9b%d7%99%20%d7%98%d7%95%d7%91%d7%99%d7%9d%20%d7%a9%d7%99%d7%a9!%d7%a1%d7%a0%d7%92%27%d7%90%d7%99%20%d7%95%d7%a7%d7%a8%d7%99%d7%99%d7%92%20%d7%aa%d7%9e%d7%99%d7%93%20%d7%9e%d7%a1%d7%aa%d7%95%d7%91%d7%91%d7%99%d7%9d%20%d7%99%d7%97%d7%93%20%d7%95%d7%a2%d7%95%d7%a9%d7%99%d7%9d%20%d7%93%d7%91%d7%a8%d7%99%d7%9d%20%d7%9e%d7%9e%d7%a9%20%d7%94%d7%96%d7%95%d7%99%d7%99%d7%9d!%d7%97%d7%99%d7%99%d7%91%d7%99%d7%9d%20%d7%93%d7%95%d7%92%d7%9e%d7%90%3f%20%d7%91%d7%91%d7%a7%d7%a9%d7%94!%20%d7%94%d7%9c%d7%9b%d7%aa%d7%9d%20%d7%a4%d7%a2%d7%9d%20%d7%a2%d7%9c%20%d7%97%d7%91%d7%9c%20%d7%93%d7%a7%20%d7%95%d7%9e%d7%aa%d7%95%d7%97%20%d7%91%d7%90%d7%95%d7%95%d7%99%d7%a8%3f!%20%d7%94%d7%9d%20%d7%9b%d7%9f!%d7%a8%d7%95%d7%a6%d7%99%d7%9d%20%d7%a2%d7%95%d7%93%20%d7%a7%d7%a6%d7%aa%20%d7%9e%d7%94%d7%a9%d7%98%d7%95%d7%99%d7%95%d7%aa%20%d7%a9%d7%9c%d7%94%d7%9d%3f%d7%a9%d7%95%d7%91%d7%a8%d7%99%d7%9d%20%d7%a9%d7%99%d7%90%d7%99%20%d7%a2%d7%95%d7%9c%d7%9d%20%d7%91%d7%9e%d7%a9%d7%97%d7%a7%d7%99%20%d7%95%d7%99%d7%93%d7%90%d7%95%2c%20%d7%9e%d7%aa%d7%97%d7%96%d7%99%d7%9d%20%d7%9c%d7%a8%d7%95%d7%a4%d7%90%d7%99%d7%9d%20%d7%9b%d7%9c%20%d7%99%d7%9b%d7%95%d7%9c%d7%99%d7%9d%2c%20%d7%95...%d7%91%d7%a2%d7%a6%d7%9d%20%d7%9b%d7%9c%20%d7%9e%d7%94%20%d7%a9%d7%91%d7%90%20%d7%9c%d7%94%d7%9d%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa!!!%d7%a1%d7%a0%d7%92%27%d7%90%d7%99%20%d7%95%d7%a7%d7%a8%d7%99%d7%99%d7%92%20%d7%91%d7%9c%d7%aa%d7%99%20%d7%a0%d7%99%d7%aa%d7%a0%d7%99%d7%9d%20%d7%9c%d7%a2%d7%a6%d7%99%d7%a8%d7%94%20...%20%d7%9b%d7%9c%20%d7%a2%d7%95%d7%93%20-%20%d7%90%d7%a3%20%d7%90%d7%97%d7%93%20%d7%9c%d7%90%20%d7%99%d7%92%d7%9c%d7%94%20%d7%a9%d7%a7%d7%a8%d7%99%d7%99%d7%92%20%d7%99%d7%9b%d7%95%d7%9c%20%d7%9c%d7%93%d7%91%d7%a8&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1788%2f%d7%a1%d7%a0%d7%92-%d7%90%d7%99-%d7%95%d7%a7%d7%a8%d7%99%d7%99%d7%92-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-sanjay-and-craig%2fseason%2f1')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLTjHc6tMisa8E1PS6NzXCldlpAAVAzpMW') #English
	
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLwLVa1RYGXSQp_AgMlXLLs_RmcTKtXMTS') #French
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLge1O0RQ5hhbQ8F6e5Xux8poqfLb7LnwN')	
		
		
	addDir(addonString(10841).encode('utf-8'),list,17,thumb,addonString(108410).encode('utf-8'),'1',0,fanart)
	
	'''ספיד רייסר'''
	thumb = ''
	fanart = ''
	list = []
	list.append('&youtube_pl=PLR7DTcU2p0QjzH9muKiw1eTbp0aU3hB63') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLZcWUVgQtnviQjBdcwStkS6y6PA3j2mUA') #English
		list.append('&youtube_pl=PLe0iK_w3CRsqlVFQechdeNh8Nlm0f0Gfn') #English
	addDir(addonString(10863).encode('utf-8'),list,17,thumb,addonString(108630).encode('utf-8'),'1',0,fanart)
	
	'''עמרי והפייה יעל'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL419YR22ubLBPUYYOTxv3y4J4jadrvBDM') #?
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=') #
	
	addDir('עמרי והפייה יעל',list,17,'','','1',0,fanart)
	
	'''עיר החזירים'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLOcNLH674qyHjdSXYpB6CPrkGOI-h7YSZ')
	if 'Russian' in General_LanguageL:	
		list.append('&youtube_pl=PLovF9Z5TJjw_T_-WPi7cr7dSptxqSXKHz')
	addDir(addonString(10864).encode('utf-8'),list,6,'http://s12.radikal.ru/i185/1103/28/6f6b8ba901b3.png',addonString(108640).encode('utf-8'),'1',0,fanart)
	
	'''עיר המלאכים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f554.jpg&mode=3&name=angel-s-friends-%d7%a2%d7%99%d7%a8-%d7%94%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=554&series_name=angel-s-friends-%d7%a2%d7%99%d7%a8-%d7%94%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f554%2fangel-s-friends-%d7%a2%d7%99%d7%a8-%d7%94%d7%9e%d7%9c%d7%90%d7%9b%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLBc-duIJ68eRIqdBV_R0jTHsIAd5aet-x') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL-IcKdcVyt_X68_zjNMqeI3IDyNr4LaE4') #English
		list.append('&youtube_pl=PL-PLYKWkz8U9vamZh7_xnY-kYKp5ZhP4y2oH') #English
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLA2784F98198B430D') #French
		list.append('&youtube_pl=PLGYC_8BSiiFudjhrlcRHQm9uw1sYR8Xwv') #French
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLeLNnWBsUgnLS4_wFT4cEf8sKsAyFqCxc') #Spanish
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLC7B66C12749CB929') #Italian
		list.append('&youtube_pl=PLDE08622C1114A775') #Italian
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=PL7a8BZvixhYvPr9jcgl1WBxQRjBZBjoV4') #Greek
		list.append('&youtube_pl=PL7F9941728DC2A2F4') #Greek
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PL8zbfEfQBH4fcLTQNNkOeTDbO_Kg7OcVj') #Turkish
	addDir(addonString(10861).encode('utf-8'),list,17,thumb,addonString(108610).encode('utf-8'),'1',0,fanart)
	
	'''על טבעי: סדרת האנימציה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f28.jpg&mode=3&name=supernatural-%d7%a2%d7%9c-%d7%98%d7%91%d7%a2%d7%99&series_id=28&series_name=supernatural-%d7%a2%d7%9c-%d7%98%d7%91%d7%a2%d7%99&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f28%2fsupernatural-%d7%a2%d7%9c-%d7%98%d7%91%d7%a2%d7%99')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL_AYqxzHii9ijePQIl8CEzizRkr5JYEjd') #English
		list.append('&youtube_pl=PLxbJ3NXwaPMXrXqmSM-zCy-AbO-f2BQME') #English
	addDir(addonString(10866).encode('utf-8'),list,17,thumb,addonString(108660).encode('utf-8'),'1',0,fanart)

	'''ערי הזהב הנסתרות'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1460.jpg&mode=3&name=the-mysterious-cities-of-gold-%d7%a2%d7%a8%d7%99-%d7%94%d7%96%d7%94%d7%91-%d7%94%d7%a0%d7%a1%d7%aa%d7%a8%d7%95%d7%aa-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&series_id=1460&series_name=the-mysterious-cities-of-gold-%d7%a2%d7%a8%d7%99-%d7%94%d7%96%d7%94%d7%91-%d7%94%d7%a0%d7%a1%d7%aa%d7%a8%d7%95%d7%aa-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1460%2fthe-mysterious-cities-of-gold-%d7%a2%d7%a8%d7%99-%d7%94%d7%96%d7%94%d7%91-%d7%94%d7%a0%d7%a1%d7%aa%d7%a8%d7%95%d7%aa-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&youtube_pl=PLwqmbDQfp96ichTyPjD-MMC5bZxYn01Mf') #Hebrew
		list.append('&youtube_pl=PLKMFPiSCwUk0g2xv447QfJlQHuMtNKegW') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=x2hPBpbfK2E&list=ELvLRRJftv4ZQ') #English
		list.append('&youtube_pl=PLKMFPiSCwUk0g2xv447QfJlQHuMtNKegW') #English
	addDir(addonString(10867).encode('utf-8'),list,17,thumb,addonString(108670).encode('utf-8'),'1',0,fanart)
	
	'''פופאי המלח*'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1469.jpg&mode=3&name=%d7%a4%d7%95%d7%a4%d7%90%d7%99-%d7%94%d7%9e%d7%9c%d7%97-popeye-the-sailor%2fseason%2f1&series_id=1469&series_name=%d7%a4%d7%95%d7%a4%d7%90%d7%99-%d7%94%d7%9e%d7%9c%d7%97-popeye-the-sailor%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1469%2f%d7%a4%d7%95%d7%a4%d7%90%d7%99-%d7%94%d7%9e%d7%9c%d7%97-popeye-the-sailor%2fseason%2f1')
	list.append('&youtube_pl=PLAD2B3930314C3FA5')
	list.append('&youtube_pl=PL9MZvRGPZkoEzhmpgT-wjPmljDeiRDOld')
	list.append('&youtube_pl=PL9MZvRGPZkoHV-2Cm2-DVpW3OdOaTnsGC')
	list.append('&youtube_pl=PLgHHcDslTatSQ-4O8jzEXsvHdfmcVA1lt')
	addDir(addonString(10868).encode('utf-8'),list,17,thumb,addonString(108680).encode('utf-8'),'1',0,fanart)
	
	'''פוקה''' #SDAROT
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLwqmbDQfp96g7F4hn-6yT2XRXi3w1oHPl') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLpKIU9Us2Mvpo6jpW64RXaMShLHosRNnY-wjPmljDeiRDOld') #English
		list.append('&youtube_pl=PL5DA5DBE69686729D') #English
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLpKIU9Us2Mvrl86maUz6a8NAoQcKgoMd-') #Spanish
		list.append('&youtube_pl=PLo4Z3qdePPNjc-eyvKXULuN1GuSBLlEzo') #Spanish
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLkt5Bvp27tD1kfd5-qh62gr9reMf8oRmJ') #French
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLkt5Bvp27tD3CMAIJqLeNJe3vTbhEzbvx') #Italian
	addDir(addonString(10870).encode('utf-8'),list,17,thumb,addonString(108700).encode('utf-8'),'1',0,fanart)
	
	'''פיוצ'רמה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73871-33.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73871-7.jpg&mode=1&name=%5BB%5D%5BCOLOR%20white%5DFuturama%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.kisspanda.net%2Ffuturama%2F')
	addDir(addonString(10876).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/73871-7.jpg',addonString(108760).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73871-33.jpg", default=background2))
	
	CATEGORIES108P(General_LanguageL, background, background2) #פינגו
	
	'''1 2 3 פינגווינים!''' #Sdarot
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL_8KXLhQVQMIkR9iafygY0ztBUPSAyUki') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL0D8BG0UKzYax5sl56VUWgFuZEWHXdu5J') #English
		list.append('&youtube_pl=PLuQ1zyXvUqEiZaTQQVwyj0JRjTqKktBXz') #English
	addDir(addonString(10869).encode('utf-8'),list,17,'https://i.ytimg.com/vi/vzVdiqGJZ7E/default.jpg',addonString(108690).encode('utf-8'),'1',0,fanart)
	
	'''פיניאס ופרב'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f532.jpg&mode=3&name=%d7%a4%d7%99%d7%a0%d7%99%d7%90%d7%a1-%d7%95%d7%a4%d7%a8%d7%91-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-phinnias-ferb%2fseason%2f1&series_id=532&series_name=%d7%a4%d7%99%d7%a0%d7%99%d7%90%d7%a1-%d7%95%d7%a4%d7%a8%d7%91-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-phinnias-ferb%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f532%2f%d7%a4%d7%99%d7%a0%d7%99%d7%90%d7%a1-%d7%95%d7%a4%d7%a8%d7%91-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94-phinnias-ferb%2fseason%2f1')
		#list.append('&youtube_pl=PLpm7RYAjgzoKDbffmhuNrxc_-lpTorM7G') #Hebrew
	if 'English' in General_LanguageL:
		list.append('&dailymotion_pl=x48bpr') #English #S1
		list.append('&dailymotion_pl=x48bps') #English #S2
		list.append('&dailymotion_pl=x48bpu') #English #S3
	addDir(addonString(10871).encode('utf-8'),list,17,thumb,addonString(108710).encode('utf-8'),'1',0,fanart)
	
	'''פליקס החתול''' #WALLA VOD
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f574.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=574&series_name=felix-the-cat-%d7%a4%d7%9c%d7%99%d7%a7%d7%a1-%d7%94%d7%97%d7%aa%d7%95%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary=%d7%90%d7%a1%d7%95%d7%a4%d7%94%20%d7%a9%d7%9c%20%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%99%d7%9d%20%d7%91%d7%9b%d7%99%d7%9b%d7%95%d7%91%d7%95%20%d7%a9%d7%9c%20%d7%a4%d7%9c%d7%99%d7%a7%d7%a1%20%d7%94%d7%97%d7%aa%d7%95%d7%9c.%20%d7%a4%d7%9c%d7%99%d7%a7%d7%a1%20%d7%94%d7%97%d7%aa%d7%95%d7%9c%20%d7%94%d7%95%d7%90%20%d7%93%d7%9e%d7%95%d7%aa%20%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%aa%20%d7%a9%d7%a0%d7%95%d7%9c%d7%93%d7%94%20%d7%91%d7%a1%d7%a8%d7%98%d7%95%d7%a0%d7%99%d7%9d%20%d7%a7%d7%a6%d7%a8%d7%99%d7%9d%20%d7%91-1919%2c%20%d7%91%d7%aa%d7%a7%d7%95%d7%a4%d7%aa%20%d7%94%d7%a1%d7%a8%d7%98%20%d7%94%d7%90%d7%99%d7%9c%d7%9d%20%d7%95%d7%91%d7%a9%d7%97%d7%95%d7%a8%20%d7%9c%d7%91%d7%9f.%20%d7%a4%d7%9c%d7%99%d7%a7%d7%a1%20%d7%94%d7%97%d7%aa%d7%95%d7%9c%20%d7%94%d7%a6%d7%9c%d7%99%d7%97%20%d7%9c%d7%a2%d7%a9%d7%95%d7%aa%20%d7%90%d7%aa%20%d7%94%d7%9e%d7%a2%d7%91%d7%a8%20%d7%9c%d7%a1%d7%a8%d7%98%d7%99%d7%9d%20%d7%9e%d7%93%d7%91%d7%a8%d7%99%d7%9d%20%d7%95%d7%91%d7%a6%d7%91%d7%a2%2c%20%d7%95%d7%9b%d7%99%d7%9b%d7%91%20%d7%91%d7%a1%d7%a8%d7%98%d7%95%d7%a0%d7%99%d7%9d%20%d7%a7%d7%a6%d7%a8%d7%99%d7%9d%20%d7%a8%d7%91%d7%99%d7%9d%2c%20%d7%a7%d7%99%d7%91%d7%9c%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%9e%d7%a9%d7%9c%d7%95%20%d7%95%d7%94%d7%95%d7%90%20%d7%90%d7%97%d7%aa%20%d7%9e%d7%94%d7%93%d7%9e%d7%95%d7%99%d7%95%d7%aa%20%d7%94%d7%9e%d7%a6%d7%95%d7%99%d7%a8%d7%95%d7%aa%20%d7%94%d7%95%d7%95%d7%aa%d7%99%d7%a7%d7%95%d7%aa%20%d7%91%d7%99%d7%95%d7%aa%d7%a8%20%d7%94%d7%9e%d7%95%d7%9b%d7%a8%d7%95%d7%aa%20%d7%92%d7%9d%20%d7%9b%d7%99%d7%95%d7%9d.%20%d7%91%d7%9e%d7%a7%d7%91%d7%a5%20%d7%96%d7%94%20%d7%a9%d7%9c%d7%95%d7%a9%d7%99%d7%9d%20%d7%95%d7%90%d7%97%d7%93%20%d7%a1%d7%a8%d7%98%d7%95%d7%a0%d7%99%d7%9d%20%d7%9e%d7%aa%d7%95%d7%9a%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%94%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%a9%d7%a9%d7%95%d7%93%d7%a8%d7%95%20%d7%91%d7%9e%d7%a7%d7%95%d7%a8%20%d7%91%d7%99%d7%9f%20&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f574%2ffelix-the-cat-%d7%a4%d7%9c%d7%99%d7%a7%d7%a1-%d7%94%d7%97%d7%aa%d7%95%d7%9c-%d7%9e%d7%93%d7%95%d7%91%d7%91')
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLDqISjt-2YGUqZpTEM-38BNZSshzcViNj') #English
		list.append('&youtube_pl=PL896C42A946504FB2') #English
		list.append('&youtube_pl=PLyUjzUUY7MEld66JKzwqpbBJiMrR3LyMi') #English
	addDir(addonString(10872).encode('utf-8'),list,17,thumb,addonString(108720).encode('utf-8'),'1',0,fanart)
	
	'''Rabbids Invasion / פלישת הרבידים'''
	thumb = 'https://www.thetvdb.com/banners/posters/271708-3.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/271708-3.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		#list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f4%ec%e9%f9%fa%20%e4%f8%e1%e9%e3%e9%ed&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2741602') #ריק
		list.append('&youtube_pl=') #S1
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLF_QeNkDVBPLvhU8p0olMp7hwEIjifFIj') #S1
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=lapincretinsinvasion/playlists')
		list.append('&youtube_id=kt_X0enZRLc') #S1
		list.append('&youtube_id=In78b28tpeQ')
		list.append('&youtube_pl=H_jIyw7cap4') #S2
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_id=mU5spS35oG4')
		list.append('&youtube_id=bbGRFrZV-XQ')
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_id=dGMC6-MJ03U')
		
	addDir(addonString(10845).encode('utf-8'),list,17,thumb,addonString(108450).encode('utf-8'),'1',0,fanart)
	
	'''פרפר נחמד'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2013%2f06%2f06%2fparpar_nice_f.jpg&mode=2&name=%d7%a2%d7%95%d7%a0%d7%94%201&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fparpar-s1')
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1092.jpg&mode=3&name=parpar-nehmad-%d7%a4%d7%a8%d7%a4%d7%a8-%d7%a0%d7%97%d7%9e%d7%93&series_id=1092&series_name=parpar-nehmad-%d7%a4%d7%a8%d7%a4%d7%a8-%d7%a0%d7%97%d7%9e%d7%93&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1092%2fparpar-nehmad-%d7%a4%d7%a8%d7%a4%d7%a8-%d7%a0%d7%97%d7%9e%d7%93')
		list.append('&youtube_pl=PL51YAgTlfPj7XTzORdSrWpgCfF1x7ZUeK')
		list.append('&youtube_pl=PL5B247BE19DDE24D5') #Hebrew
		list.append('&youtube_pl=PLE117810DAD8DB2AD') #Hebrew
		list.append('&youtube_pl=PL_mw-BY43H9zxMB_75CMCbEcidGU9-UQQ') #Hebrew
	addDir(addonString(10105).encode('utf-8'),list,17,thumb,addonString(101050).encode('utf-8'),'1',0,fanart)
	
	'''צור משלנו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1320.jpg&mode=3&name=%d7%a6%d7%95%d7%a8-%d7%9e%d7%a9%d7%9c%d7%a0%d7%95-tzur-meshelanu%2fseason%2f1&series_id=1320&series_name=%d7%a6%d7%95%d7%a8-%d7%9e%d7%a9%d7%9c%d7%a0%d7%95-tzur-meshelanu%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1320%2f%d7%a6%d7%95%d7%a8-%d7%9e%d7%a9%d7%9c%d7%a0%d7%95-tzur-meshelanu%2fseason%2f1')
		list.append('&youtube_pl=PLtz5gfkQ59bJw2o_B23A_Pb1ooaHq3-tj')
	addDir('צור משלנו',list,17,thumb,"צור משלנו זו תוכנית חינוכית וערכית לילדים. מדובר בבובה ועוד מס' שחקנים שכל פרק עוסק בנושא אחר חינוכי וערכי. כגון לכבד את האחר, לשפוט לכף זכות, לעזור לשני וכו' צור הוא ילד סקרן בעל הרבה חוש הומור, נוטה לשאול שאלות ואף ליישם את מה שהוא לומד.",'1',0,fanart)
	
	'''Code Lyoko / קוד ליוקו'''
	thumb = 'https://www.thetvdb.com/banners/posters/74280-2.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/74280-1.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1579.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1579&series_name=%d7%a7%d7%95%d7%93-%d7%9c%d7%99%d7%95%d7%a7%d7%95-%d7%90%d7%91%d7%95%d7%9c%d7%95%d7%a6%d7%99%d7%94-code-lyoko-evolution%2fseason%2f1&summary=%d7%a7%d7%91%d7%95%d7%a6%d7%94%20%d7%a9%d7%9c%20%d7%aa%d7%9c%d7%9e%d7%99%d7%93%d7%99%d7%9d%20%d7%9e%d7%92%d7%9c%d7%99%d7%9d%20%d7%99%d7%a7%d7%95%d7%9d%20%d7%9e%d7%a7%d7%91%d7%99%d7%9c%20%d7%9e%d7%a1%d7%aa%d7%95%d7%a8%d7%99%20%d7%91%d7%a9%d7%9d%20%d7%9c%d7%99%d7%95%d7%a7%d7%95%2c%20%d7%95%d7%9e%d7%aa%d7%a2%d7%9e%d7%aa%d7%99%d7%9d%20%d7%a2%d7%9d%20%d7%9e%d7%97%d7%a9%d7%91%20%d7%a2%d7%9c%20%d7%a9%d7%9e%d7%90%d7%99%d7%99%d7%9d%20%d7%9c%d7%94%d7%a9%d7%aa%d7%9c%d7%98%20%d7%a2%d7%9c%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1579%2f%d7%a7%d7%95%d7%93-%d7%9c%d7%99%d7%95%d7%a7%d7%95-%d7%90%d7%91%d7%95%d7%9c%d7%95%d7%a6%d7%99%d7%94-code-lyoko-evolution%2fseason%2f1')

	addDir(addonString(10890).encode('utf-8'),list,17,thumb,addonString(108900).encode('utf-8'),'1',0,fanart)
	
	'''Code Lyoko: Evolution / קוד ליוקו: אבולוציה'''
	thumb = 'https://www.thetvdb.com/banners/posters/265109-1.jpg'
	fanart = 'https://www.thetvdb.com/banners/fanart/original/265109-2.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1579.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1579&series_name=%d7%a7%d7%95%d7%93-%d7%9c%d7%99%d7%95%d7%a7%d7%95-%d7%90%d7%91%d7%95%d7%9c%d7%95%d7%a6%d7%99%d7%94-code-lyoko-evolution%2fseason%2f1&summary=%d7%a7%d7%91%d7%95%d7%a6%d7%94%20%d7%a9%d7%9c%20%d7%aa%d7%9c%d7%9e%d7%99%d7%93%d7%99%d7%9d%20%d7%9e%d7%92%d7%9c%d7%99%d7%9d%20%d7%99%d7%a7%d7%95%d7%9d%20%d7%9e%d7%a7%d7%91%d7%99%d7%9c%20%d7%9e%d7%a1%d7%aa%d7%95%d7%a8%d7%99%20%d7%91%d7%a9%d7%9d%20%d7%9c%d7%99%d7%95%d7%a7%d7%95%2c%20%d7%95%d7%9e%d7%aa%d7%a2%d7%9e%d7%aa%d7%99%d7%9d%20%d7%a2%d7%9d%20%d7%9e%d7%97%d7%a9%d7%91%20%d7%a2%d7%9c%20%d7%a9%d7%9e%d7%90%d7%99%d7%99%d7%9d%20%d7%9c%d7%94%d7%a9%d7%aa%d7%9c%d7%98%20%d7%a2%d7%9c%20%d7%94%d7%a2%d7%95%d7%9c%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1579%2f%d7%a7%d7%95%d7%93-%d7%9c%d7%99%d7%95%d7%a7%d7%95-%d7%90%d7%91%d7%95%d7%9c%d7%95%d7%a6%d7%99%d7%94-code-lyoko-evolution%2fseason%2f1')

	addDir(addonString(10891).encode('utf-8'),list,17,thumb,addonString(108910).encode('utf-8'),'1',0,fanart)
	
	'''קופיקו'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=UCCktKuBGZ1kHifzp9Mxu6Eg')
		list.append('&youtube_pl=PLN0EJVTzRDL_9qHYdDXgf6tslifiY_4zI')
		list.append('&youtube_pl=PLR7DTcU2p0QhDzYbbniDNwSbXUM_p6N3f')
		list.append('&youtube_pl=PLR7DTcU2p0QgEdLPHhrhKtxElvYVrseAQ') #Hebrew #S2
		list.append('&youtube_pl=PLR7DTcU2p0QhNGUffSgu8_5dP3lnOGZTx') #Hebrew #S3
	addDir(addonString(10855).encode('utf-8'),list,17,thumb,addonString(108550).encode('utf-8'),'1',0,fanart)
	
	'''קים פוסיבול'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78259-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78259-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DKim%20Possible%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fkim-possible')
		
	addDir(addonString(10800).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/78259-1.jpg',addonString(108000).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/78259-2.jpg", default=background2))
	
	'''קשת וענן'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1751.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1751&series_name=%d7%a7%d7%a9%d7%aa-%d7%95%d7%a2%d7%a0%d7%9f-keshet-veanan%2fseason%2f1&summary=%d7%a7%d7%a9%d7%aa%20%d7%95%d7%a2%d7%a0%d7%9f%20%d7%94%d7%99%d7%90%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99%d7%aa%20%d7%9c%d7%99%d7%9c%d7%93%d7%99%d7%9d%2c%20%d7%a9%d7%a9%d7%95%d7%93%d7%a8%d7%94%20%d7%91%d7%98%d7%9c%d7%95%d7%95%d7%99%d7%96%d7%99%d7%94%20%d7%94%d7%97%d7%99%d7%a0%d7%95%d7%9b%d7%99%d7%aa%20%d7%94%d7%99%d7%a9%d7%a8%d7%90%d7%9c%d7%99%d7%aa%20%d7%91%d7%99%d7%9f%20%d7%94%d7%a9%d7%a0%d7%99%d7%9d%201983-%201986%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%a9%d7%95%d7%93%d7%a8%d7%94%20%d7%91%d7%a9%d7%99%d7%93%d7%95%d7%a8%d7%99%d7%9d%20%d7%97%d7%95%d7%96%d7%a8%d7%99%d7%9d%20%d7%a2%d7%93%20%d7%a1%d7%95%d7%a3%20%d7%a9%d7%a0%d7%95%d7%aa%20%d7%94%d7%a9%d7%9e%d7%95%d7%a0%d7%99%d7%9d%20%d7%95%d7%aa%d7%97%d7%99%d7%9c%d7%aa%20%d7%a9%d7%a0%d7%95%d7%aa%20%d7%94%d7%aa%d7%a9%d7%a2%d7%99%d7%9d.%20%d7%94%d7%a1%d7%93%d7%a8%d7%94%20%d7%a2%d7%a1%d7%a7%d7%94%20%d7%91%d7%a0%d7%95%d7%a9%d7%90%d7%99%d7%9d%20%d7%91%d7%aa%d7%97%d7%95%d7%9d%20%d7%94%d7%99%d7%94%d7%93%d7%95%d7%aa%2c%20%d7%9b%d7%92%d7%95%d7%9f-%20%d7%9e%d7%95%d7%a2%d7%93%d7%99%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%2c%20%d7%a9%d7%91%d7%aa%d7%95%d7%aa%2c%20%d7%a2%d7%93%d7%95%d7%aa%2c%20%d7%90%d7%99%d7%a9%d7%99%d7%9d%20%d7%91%d7%aa%d7%95%d7%9c%d7%93%d7%95%d7%aa%20%d7%a2%d7%9d%20%d7%99%d7%a9%d7%a8%d7%90%d7%9c%20%d7%95%d7%9e%d7%a0%d7%94%d7%92%d7%99%d7%9d%20%d7%99%d7%94%d7%95%d7%93%d7%99%d7%99%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1751%2f%d7%a7%d7%a9%d7%aa-%d7%95%d7%a2%d7%a0%d7%9f-keshet-veanan%2fseason%2f1')
		list.append('&youtube_pl=PL51YAgTlfPj6qcpdP7e44dNj7xHuwd3oo') #Hebrew
	addDir(addonString(10805).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/5/56/Keshet_and_Anan_logo.jpg/250px-Keshet_and_Anan_logo.jpg',addonString(108050).encode('utf-8'),'1',0,fanart)
	
	'''ראגרטס'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F77038-7.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F77038-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DRugrats%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Frugrats')
		
	addDir(addonString(10881).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/77038-2.jpg',addonString(108810).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/77038-7.jpg", default=background2))
	
	'''ראש גדול'''
	thumb = ''
	fanart = 'http://30k0u22sosp4xzag03cfogt1.wpengine.netdna-cdn.com/wp-content/uploads/2015/04/rosh-gadol7.jpg'
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?mode=6&name=%5bCOLOR%20red%5d%20%d7%97%d7%a4%d7%a9%20%20%5b%2fCOLOR%5d&summary&url=http%3a%2f%2fwww.sdarot.wf%2fsearch')
		list.append('&youtube_pl=PLNMdxRa6e5t-8xyd3eFtXKIHbd6gcZPXG')
		list.append('&youtube_id=2cuxr5DLnwg')
		list.append('&youtube_id=TEuf9SojWug')
		list.append('&youtube_id=dspu_9neTsA')
		list.append('&youtube_id=syv0DjQqJQ0')
	addDir(addonString(10865).encode('utf-8'),list,17,thumb,addonString(108650).encode('utf-8'),'1',0,fanart)
	
	'''רגע עם דודלי'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL51YAgTlfPj5gUK-SIhbYyAMUQASzrZAw')
	addDir(addonString(10806).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/thumb/f/fe/Dodlee.jpg/250px-Dodlee.jpg',addonString(108060).encode('utf-8'),'1',0,fanart)
	
	CATEGORIES108Q(General_LanguageL, background, background2) #רחוב סומסום
	
	'''קסם של הורים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f7%f1%ed%20%f9%ec%20%e4%e5%f8%e9%ed&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2516297')
		list.append('&youtube_pl=PLaGWxxBsbL1D_bSy9Vuy_UCAONqidrlWB') #
	addDir('קסם של הורים',list,17,'','','1',0,fanart)
	
	'''שאמן קינג'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		pass
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL494DB3F3F5F5F6CB') #English
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLWMCwroYhJSqqXaG7kh8u6yk9O5gKvI29') #שאמן קינג
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL327HVtSHDnsYYKAsrudqZjaOX8brHVNO') #Italian
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=PLNTB1s2moCBc2G1WKhMPI_e0RPocTVpfK') #Bulgarian
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLBCBF4FA8CB8C4FE9') #Spanish
	addDir(addonString(10885).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/9/92/Shaman_King_25.png',addonString(108850).encode('utf-8'),'1',0,fanart)
	
	'''שבט צוללת'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a9%d7%91%d7%98%20%d7%a6%d7%95%d7%a6%d7%9c%d7%aa&url=seasonId%3d2855982')
		list.append('&youtube_pl=PLKMFPiSCwUk3QeQW6cq_GyoDKxZ5n0Uai') #
	addDir('שבט צוללת',list,17,'','','1',0,fanart)
	
	'''שוברי גלים'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=3&module=wallavod&name=%d7%a4%d7%a8%d7%a7%d7%99%d7%9d%20%d7%9e%d7%9c%d7%90%d7%99%d7%9d&url=seasonId%3d2884205')
	addDir('שוברי גלים',list,6,'','','1',0,fanart)
	
	'''שטותניק'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f9%e8%e5%fa%f0%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f1837648')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f1%e5%f4%f8%20%f9%e8%e5%fa%f0%e9%f7&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2662395')
		list.append('&youtube_pl=PLuQCYUv97StRk-DsmuAL0ptZPJ9ATkguV') #סופר שטותניק
		
	addDir('שטותניק',list,17,'','','1',0,fanart)
	
	CATEGORIES108E(General_LanguageL, background, background2) #שי-רה נסיכת הכוח
	
	'''שכונה'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		#list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%f9%eb%e5%f0%e4&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2796370') #Empty!
		list.append('&dailymotion_pl=x45tcn')
		list.append('&youtube_pl=PLuQCYUv97StR0o1N7zfbpobVVwev0sx91')
		
	addDir('שכונה',list,6,'https://upload.wikimedia.org/wikipedia/he/8/80/10628436_316742958505148_2646201463663204371_n.jpg','','1',0,fanart)
	
	'''שרגא בישגדא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2014%2f08%2f06%2fShraga_1920x1080_f.jpg&mode=1&name=%d7%a9%d7%a8%d7%92%d7%90%20%d7%91%d7%99%d7%a9%d7%92%d7%93%d7%90&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-23tv%2fshraga-bishgada')
		list.append('&youtube_pl=PL51YAgTlfPj5KPYOntZkqg2Nwyqj2M1Lf')
	addDir(addonString(10808).encode('utf-8'),list,17,'https://i.ytimg.com/vi/E5JQ2o84iSw/hqdefault.jpg',addonString(108080).encode('utf-8'),'1',0,fanart)
	
	'''תראו את אבא'''
	thumb = ''
	fanart = ''
	list = []
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nick&name=%fa%f8%e0%e5%20%e0%fa%20%e0%e1%e0&url=http%3a%2f%2fnick.walla.co.il%2f%3fw%3d%2f%2f2850878')
	addDir('תראו את אבא',list,17,'','','1',0,fanart)
	
	'''Thunderbirds Are Go'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F266631-5.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F266631-5.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThunderbirds%20Are%20Go!%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthunderbirds-are-go')
		
	addDir(addonString(10883).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/266631-5.jpg',addonString(108830).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/266631-5.jpg", default=background2))
	
	'''Sarah & Duck'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F267108-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F267108-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSarah%20%26%20Duck%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fsarah-and-duck')
		
	addDir(addonString(10882).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/267108-2.jpg',addonString(108820).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/267108-2.jpg", default=background2))
	
	'''The Furchester Hotel'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F286332-1.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F286332-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DThe%20Furchester%20Hotel%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fthe-furchester-hotel')
	addDir(addonString(10874).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/286332-1.jpg',addonString(108740).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/286332-1.jpg", default=background2))
	
	'''Wacky Races'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76261-7.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F76261-6.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DWacky%20Races%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fwacky-races')
	addDir(addonString(10884).encode('utf-8'),list,6,'http://thetvdb.com/banners/_cache/posters/76261-6.jpg',addonString(108840).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/76261-7.jpg", default=background2))
	
	'''Wacky Races (2017)'''
	thumb = ''
	fanart = ''
	list = []
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fwww.thetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F76261-7.jpg&iconimage=https%3A%2F%2Fwww.thetvdb.com%2Fbanners%2F_cache%2Fposters%2F76261-8.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DWacky%20Races%20(2017)%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fwacky-races-2017')
	addDir(addonString(10884).encode('utf-8') + space + '(2017)',list,6,'https://www.thetvdb.com/banners/_cache/posters/76261-8.jpg',addonString(108840).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://www.thetvdb.com/banners/fanart/original/76261-7.jpg", default=background2))
	
	CATEGORIES108A(General_LanguageL, background, background2) #עמוד הבא ילדים ונוער
	
def CATEGORIES109(name, iconimage, desc, fanart):
	'''לימוד שפה'''
	background = 109
	background2 = ""
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	CATEGORIES109B(General_LanguageL, background, background2) #לימוד שפה
	
	CATEGORIES109A(General_LanguageL, background, background2) #עמוד הבא לימוד שפה
	
def CATEGORIES200():
	background = 200
	background2 = ""
	
	'''עברית'''
	addDir(addonString_servicefeatherence(32900).encode('utf-8'),'Hebrew',90,"http://flaglane.com/download/israeli-flag/israeli-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32900).encode('utf-8')),'1',0,getAddonFanart(200, custom="http://pre15.deviantart.net/2dd4/th/pre/f/2015/166/3/2/israel_aph_by_wolf_kid1000-d8xdbyp.jpg"))
	
	'''אנגלית'''
	addDir(addonString_servicefeatherence(32901).encode('utf-8'),'English',90,"http://flaglane.com/download/british-flag/british-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32901).encode('utf-8')),'1',0,getAddonFanart(200,custom=""))
	
	'''אוזבקית'''
	addDir(addonString_servicefeatherence(32929).encode('utf-8'),'Uzbek',90,"http://flaglane.com/download/uzbekistani-flag/uzbekistani-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32929).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''אוקראינית'''
	addDir(addonString_servicefeatherence(32903).encode('utf-8'),'Ukrainian',90,"http://www.enchantedlearning.com/europe/ukraine/flag/Flagbig.GIF",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32903).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''איטלקית'''
	addDir(addonString_servicefeatherence(32909).encode('utf-8'),'Italian',90,"http://flaglane.com/download/italian-flag/italian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32909).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))	
	
	'''אינדונזית'''
	addDir(addonString_servicefeatherence(32927).encode('utf-8'),'Indonesian',90,"http://www.united-states-flag.com/media/catalog/product/cache/2/thumbnail/9df78eab33525d08d6e5fb8d27136e95/F/L/FLGDECL1000004754_-00_indonesia-flag-decal_3.jpg",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32927).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''אירית'''
	addDir(addonString_servicefeatherence(32912).encode('utf-8'),'Irish',90,"http://flaglane.com/download/irish-flag/irish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32912).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''בולגרית'''
	addDir(addonString_servicefeatherence(32928).encode('utf-8'),'Bulgarian',90,"http://flaglane.com/download/bulgarian-flag/bulgarian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32928).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''גאורגית'''
	addDir(addonString_servicefeatherence(32906).encode('utf-8'),'Georgian',90,"http://freestock.ca/georgia_grunge_flag_sjpg1133.jpg",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32906).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''גרמנית'''
	addDir(addonString_servicefeatherence(32920).encode('utf-8'),'German',90,"http://flaglane.com/download/german-flag/german-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32920).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''דנית'''
	addDir(addonString_servicefeatherence(32933).encode('utf-8'),'Dansk',90,"http://flaglane.com/download/dane-flag/dane-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32933).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''הודית'''
	addDir(addonString_servicefeatherence(32923).encode('utf-8'),'Hindi',90,"http://www.iloveindia.com/national-symbols/pics/indian-flag.jpg",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32923).encode('utf-8')),'1',0,getAddonFanart(200, custom="http://allpicts.in/download/5073/india_flag_fluttering_by_kids_for_Indian_Independence_day_Celebration.jpg/"))
	
	'''הולנדית'''
	addDir(addonString_servicefeatherence(32902).encode('utf-8'),'Dutch',90,"http://flaglane.com/download/dutch-flag/dutch-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32902).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''הונגרית'''
	addDir(addonString_servicefeatherence(32921).encode('utf-8'),'Hungarian',90,"http://flaglane.com/download/hungarian-flag/hungarian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32921).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''טורקית'''
	addDir(addonString_servicefeatherence(32916).encode('utf-8'),'Turkish',90,"http://flaglane.com/download/turkish-flag/turkish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32916).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''יוונית'''
	addDir(addonString_servicefeatherence(32931).encode('utf-8'),'Greek',90,"http://flaglane.com/download/greek-flag/greek-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32931).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''יפנית'''
	addDir(addonString_servicefeatherence(32911).encode('utf-8'),'Japanese',90,"http://flaglane.com/download/japanese-flag/japanese-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32911).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''סינית'''
	addDir(addonString_servicefeatherence(32907).encode('utf-8'),'Chinese',90,"http://flaglane.com/download/chinese-flag/chinese-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32907).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''סלובקית'''
	addDir(addonString_servicefeatherence(32917).encode('utf-8'),'Slovak',90,"http://flaglane.com/download/slovakian-flag/slovakian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32917).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''ספרדית'''
	addDir(addonString_servicefeatherence(32908).encode('utf-8'),'Spanish',90,"http://flaglane.com/download/spanish-flag/spanish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32908).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
		
	'''סרבית'''
	addDir(addonString_servicefeatherence(32915).encode('utf-8'),'Serbian',90,"http://www.flagsinformation.com/serbian-flag.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32915).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''פולנית'''
	addDir(addonString_servicefeatherence(32922).encode('utf-8'),'Polish',90,"http://flaglane.com/download/polish-flag/polish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32922).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''פורטוגזית'''
	addDir(addonString_servicefeatherence(32918).encode('utf-8'),'Portuguese',90,"http://flaglane.com/download/portuguese-flag/portuguese-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32918).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''פינית'''
	addDir(addonString_servicefeatherence(32925).encode('utf-8'),'Finnish',90,"http://flaglane.com/download/finnish-flag/finnish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32925).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''פרסית'''
	addDir(addonString_servicefeatherence(32935).encode('utf-8'),'Persian',90,"http://flaglane.com/download/iranian-flag/iranian-flag-graphic.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32935).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))

	'''ערבית'''
	addDir(addonString_servicefeatherence(32926).encode('utf-8'),'Arabic',90,"http://flaglane.com/download/emirian-flag/emirian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32926).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''צ'כית'''
	addDir(addonString_servicefeatherence(32934).encode('utf-8'),'Czech',90,"http://flaglane.com/download/czech-flag/czech-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32934).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''צרפתית'''
	addDir(addonString_servicefeatherence(32904).encode('utf-8'),'French',90,"http://flaglane.com/download/french-flag/french-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32904).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''קוריאנית'''
	addDir(addonString_servicefeatherence(32913).encode('utf-8'),'Korean',90,"http://flaglane.com/download/south-korean-flag/south-korean-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32913).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''קזחית'''
	addDir(addonString_servicefeatherence(32930).encode('utf-8'),'Kazakh',90,"http://flaglane.com/download/kazakh-flag/kazakh-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32930).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''קטלאנית'''
	addDir(addonString_servicefeatherence(32919).encode('utf-8'),'Catalan',90,"http://www.barcelonas.com/images/la-senyera.jpg",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32919).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''קריאולית האיטית'''
	addDir(addonString_servicefeatherence(32924).encode('utf-8'),'Haitian',90,"http://flaglane.com/download/haitian-flag/haitian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32924).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''רומנית'''
	addDir(addonString_servicefeatherence(32914).encode('utf-8'),'Romanian',90,"http://flaglane.com/download/romanian-flag/romanian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32914).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''רוסית'''
	addDir(addonString_servicefeatherence(32905).encode('utf-8'),'Russian',90,"http://flaglane.com/download/russian-flag/russian-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32905).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))

	'''שוודית'''
	addDir(addonString_servicefeatherence(32932).encode('utf-8'),'Swedish',90,"http://flaglane.com/download/swedish-flag/swedish-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32932).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))
	
	'''תאילנדית'''
	addDir(addonString_servicefeatherence(32910).encode('utf-8'),'Thai',90,"http://flaglane.com/download/thai-flag/thai-flag-medium.png",addonString(1).encode('utf-8') % (addonString_servicefeatherence(32910).encode('utf-8')),'1',0,getAddonFanart(200, custom=""))

	
	
def	CATEGORIES999():
	'''testing'''
	background = 999
	
	list = []
	list.append('&youtube_ch=vicenews') #vicenews
	list.append('&youtube_ch=UCMtFAi84ehTSYSE9XoHefig') #vicenews
	addDir('Vice News',list,17,'http://a5.mzstatic.com/us/r30/Purple69/v4/8e/96/c7/8e96c725-6b07-6d16-877e-351b4ebcd5b6/icon175x175.png',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []	
	list.append('&youtube_pl=PLZ_hwG6UuEJYkYPqoeiV1lYTAF0E8CS5Y') #ViceLand
	addDir('ViceLand',list,17,'https://pbs.twimg.com/profile_images/672122073465020416/Yr0DYmAB.jpg',"description",'1',0,getAddonFanart(background,custom="https://pbs.twimg.com/profile_images/672122073465020416/Yr0DYmAB.jpg"))
	list = []
	list.append('&youtube_pl=PLw613M86o5o5BNP8ls1TNDLLHVEi1Mopg') #ViceOnHBO S1
	list.append('&youtube_pl=PLDbSvEZka6GE6wL8MtEvaZzs1ghK4CGZC') #ViceOnHBO S2
	list.append('&youtube_pl=PLDbSvEZka6GEZPMAxNvcWMW8OvuzNaN8J') #ViceOnHBO S3
	addDir('Vice on HBO',list,17,'http://assets.vice.com/content-images/series/vice-on-hbo-outtakes/show_image/vice_on_HBO_extended_vice_220x220.jpg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_pl=PL5UsyVL1WN7hlV2wAdPzHWQY8QibeKA0L') #Xive History
	list.append('&youtube_pl=PL5UsyVL1WN7gOiampy3Ha-nNyncfNofSK') #Xive Global	
	addDir('Xive Documentaries',list,17,'https://superrepo.org/static/images/icons/original/xplugin.video.xivetv.png.pagespeed.ic.HsmZ7Ypju8.png',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_pl=UCUR7DG5xaHpo1GyIPEGISIw') #RANDOM DOCS
	addDir('Random Documentaries',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_pl=PLFMWEb-q8eH5uC7uTNtO4kJ9COGE8_qgt') #DarkWing Duck S1
	list.append('&youtube_pl=PLFMWEb-q8eH5bPJHF5T2zKd3Bhv7gtq8Q') #DarkWing Duck S2	
	addDir('Dark Wing Duck',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_pl=PLZxWJ6CTr63bL1Vc2qB6zyG_Gad4hpB9K') #
	list.append('&youtube_pl=PLZxWJ6CTr63byWWhy_YgJGcks3yiUtDbl') #Top Punishments
	list.append('&youtube_pl=PLZxWJ6CTr63bTvlXWaDgTyx2pZolLlGuy') #Funniest
	list.append('&youtube_pl=PLZxWJ6CTr63aF3u-S_zcz2J7tME6eBXKw') #Top Moments
	list.append('&youtube_pl=PLZxWJ6CTr63Z1imTZyROqVQnjFOPxso0D') #Deleted Scenes
	list.append('&youtube_pl=PLZxWJ6CTr63ZwCGZg8cMhqyDOyWv3Om0U') #Bonus
	list.append('&youtube_pl=PLZxWJ6CTr63a3W3sHmsYzQ3X6h02X7gzQ') #S1
	list.append('&youtube_pl=PLZxWJ6CTr63YRCu7RIysdPIKBXA0-TNAP') #S2
	addDir('Impractical Jokers',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_ch=teamcoco') #conan
	list.append('&youtube_ch=latenight') #fallon
	list.append('&youtube_ch=JimmyKimmelLive') #kimmel
	#list.append('&custom8=plugin://plugin.video.youtube/channel/UCMtFAi84ehTSYSE9XoHefig/') #colbert
	#list.append('&youtube_id=UCMtFAi84ehTSYSE9XoHefig') #colbert
	addDir('Late Night',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_pl=PL4166A6B67CF5C6AE') #RELAXHD
	addDir('Relax in HD',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	list = []
	list.append('&youtube_se=RelaxHD') #random search HD
	addDir('Random RelaxHD',list,17,'thumb.jpeg',"description",'1',0,getAddonFanart(background,custom="thumb.jpeg"))
	
	if 1 + 1 == 3:
		url2 = '0B4tub3thj86KRjhUWGJIMXhlQU0'
		url2 = '&googledrive=0Bxnz_CSSq5-xVFNIVFZNY24xcTA'
		url3 = '&googledrive2=http://dragonballz.co.il/%d7%93%d7%a8%d7%92%d7%95%d7%9f-%d7%91%d7%95%d7%9c-%d7%96%d7%99-%d7%9c%d7%a6%d7%a4%d7%99%d7%99%d7%94-%d7%99%d7%a9%d7%99%d7%a8%d7%94/'
		#url3 = '&googledrive2=http://stackoverflow.com/questions/32575617/using-unicode-hebrew-characters-with-regular-expression'
		#url2 = 'http://www.supercartoons.net/video/1208/jeepers-its-the-creeper.mp4'
		image2 = 'http://dragonballz.co.il/wp-content/uploads/2015/03/1058-214x300.jpg'
		title2 = 'דרגון בול זי פרק 1 – מדובב לעברית'
		addDir('googledrive',url2,4,image2,'testing','1',0,getAddonFanart(200, urlcheck_=False)) #Test
		
		url = os.path.join(templates2_path, '104', 'Dragon Ball Z.txt')
		addDir('googledrive mode=11 custom_se2',url,11,image2,'testing','1',50, image2) #Test
		
		
		addDir('moridim','http://www.moridim.tv/%D7%A1%D7%A8%D7%98%D7%99%D7%9D.html#types-4',40,'','testing','1',50, "") #Test
		
		list = []
		#list.append('&direct4='+url2)
		list.append('&googledrive2='+url3)
		list.append('&googledrive='+url2)
		
		addDir('dragonball',url3,40,'',addonString(104200).encode('utf-8'),'1',50,"")
		
		
		addDir('cartoons','http://www.supercartoons.net/cartoons/',40,image2,'testing','1',0,getAddonFanart(200, urlcheck_=False))
		
		
		'''הובוס ספר הקסמים הגדול'''
		list = []
		url = 'http://serethd.net/wp-json/oembed/1.0/embed?url=http%3A%2F%2Fserethd.net%2F%25d7%2590%25d7%25a0%25d7%2599%25d7%259e%25d7%25a6%25d7%2599%25d7%2594%2F%25d7%25a6%25d7%25a2%25d7%25a6%25d7%2595%25d7%25a2-%25d7%25a9%25d7%259c-%25d7%25a1%25d7%2599%25d7%25a4%25d7%2595%25d7%25a8-%25d7%259e%25d7%2593%25d7%2595%25d7%2591%25d7%2591-%25d7%259c%25d7%25a6%25d7%25a4%25d7%2599%25d7%2599%25d7%2594-%25d7%2599%25d7%25a9%25d7%2599%25d7%25a8%25d7%2594.html'
		addDir('direct8/44',url,44,'',addonString(104200).encode('utf-8'),'1',50,"")
