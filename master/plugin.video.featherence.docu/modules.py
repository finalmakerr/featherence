# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
from modulesA import *
from modulesZ import *
"""-----------------------------"""

def getList(num=0):
	list = [] ; thumb="" ; fanart=""
	if num == 101:
		'''Nature / טבע'''
		thumb = 'https://i.ytimg.com/vi/q4AQDDKglEE/maxresdefault.jpg'
		fanart = 'http://www.freedomwallpaper.com/wp-content/uploads/2015/02/Wild-animal-wallpaper-2.jpg'
		se = 'Nature Ultra HD' ; list.append('&name_=' + addonString(30001).encode('utf-8') + ' Ultra HD' + '&&youtube_se='+se)
		se = 'Nature 4K' ; list.append('&name_=' + addonString(30001).encode('utf-8') + ' 4K' + '&&youtube_se='+se)
		se = 'Plants DOCU' ; list.append('&name_=' + addonString(30104).encode('utf-8') + '&&youtube_se='+se)
		se = 'TREES DOCU' ; list.append('&name_=' + addonString(30171).encode('utf-8') + '&&youtube_se='+se)
		se = 'orchid plant DOCU' ; list.append('&name_=' + addonString(30172).encode('utf-8') + '&&youtube_se='+se)
		se = 'Botany plant DOCU' ; list.append('&name_=' + addonString(30173).encode('utf-8') + '&&youtube_se='+se)
		se = 'plants physiology DOCU' ; list.append('&name_=' + addonString(30174).encode('utf-8') + '&&youtube_se='+se)
		c8 = 'plugin://plugin.video.earthtouch/' ; list.append('&name_=' + 'Earth Touch' + '&&custom8='+c8)
	elif num == 102:
		'''Space / חלל'''
		thumb = 'http://www.esa.int/var/esa/storage/images/esa_multimedia/images/2014/02/searching_for_exoplanetary_systems/14282306-1-eng-GB/Searching_for_exoplanetary_systems.jpg'
		se = 'Space DOCU' ; list.append('&name_=' + addonString(30002).encode('utf-8') + '&&youtube_se='+se)
		se = 'Space Astronauts DOCU' ; list.append('&name_=' + addonString(30204).encode('utf-8') + '&&youtube_se='+se)
		se = 'Space Astronomy DOCU' ; list.append('&name_=' + addonString(30203).encode('utf-8') + '&&youtube_se='+se)
		se = 'Space Exploration DOCU' ; list.append('&name_=' + addonString(30201).encode('utf-8') + '&&youtube_se='+se)
		se = 'Hubble Space Telescope DOCU' ; list.append('&name_=' + addonString(30202).encode('utf-8') + '&&youtube_se='+se)
		se = 'Alien space DOCU' ; list.append('&name_=' + addonString(30207).encode('utf-8') + '&&youtube_se='+se)
		se = 'MARS space DOCU' ; list.append('&name_=' + addonString(30208).encode('utf-8') + '&&youtube_se='+se)
		se = 'SPACESHIP space DOCU' ; list.append('&name_=' + addonString(30209).encode('utf-8') + '&&youtube_se='+se)
		se = 'SPEED OF LIGHT space DOCU' ; list.append('&name_=' + addonString(30210).encode('utf-8') + '&&youtube_se='+se)
		se = 'MOON space DOCU' ; list.append('&name_=' + addonString(30211).encode('utf-8') + '&&youtube_se='+se)
		se = 'BLACK HOLE space DOCU' ; list.append('&name_=' + addonString(30212).encode('utf-8') + '&&youtube_se='+se)
		c8 = 'plugin://plugin.video.eso/' ; list.append('&name_=' + 'ESO' + '&&custom8='+c8)
		c8 = 'plugin://plugin.video.esa/' ; list.append('&name_=' + 'ESA' + '&&custom8='+c8)
	
	elif num == 103:
		thumb = 'http://wsap.academy/wp-content/uploads/2015/03/1123676.jpg'
		fanart = 'http://wsap.academy/wp-content/uploads/2015/03/1123676.jpg'
		se = 'History Channel DOCU' ; list.append('&name_=' + addonString(30300).encode('utf-8') + '&&youtube_se='+se)
		se = 'World War 1 DOCU' ; list.append('&name_=' + addonString(30301).encode('utf-8') + ' 1' + '&&youtube_se='+se)
		se = 'World War 2 DOCU' ; list.append('&name_=' + addonString(30301).encode('utf-8') + ' 2' + '&&youtube_se='+se)
		se = 'World War 3 DOCU' ; list.append('&name_=' + addonString(30301).encode('utf-8') + ' 3' + '&&youtube_se='+se)
		se = 'Historical armies DOCU' ; list.append('&name_=' + addonString(30302).encode('utf-8') + '&&youtube_se='+se)
		se = 'ROMANS DOCU' ; list.append('&name_=' + addonString(30303).encode('utf-8') + '&&youtube_se='+se)
		se = 'ISRAEL DOCU' ; list.append('&name_=' + addonString(30304).encode('utf-8') + '&&youtube_se='+se)
		se = 'KING SOLOMON DOCU' ; list.append('&name_=' + addonString(30313).encode('utf-8') + '&&youtube_se='+se)
		se = 'JERUSALEM DOCU' ; list.append('&name_=' + addonString(30308).encode('utf-8') + '&&youtube_se='+se)
		se = 'JESUS DOCU' ; list.append('&name_=' + addonString(30305).encode('utf-8') + '&&youtube_se='+se)
		se = 'BIBLE DOCU' ; list.append('&name_=' + addonString(30306).encode('utf-8') + '&&youtube_se='+se)
		se = 'VIKINGS DOCU' ; list.append('&name_=' + addonString(30307).encode('utf-8') + '&&youtube_se='+se)
		se = 'STONE, BRONZE, IRON, NEW AGE DOCU' ; list.append('&name_=' + addonString(30311).encode('utf-8') + '&&youtube_se='+se)
		se = 'FREE MASONS DOCU' ; list.append('&name_=' + addonString(30310).encode('utf-8') + '&&youtube_se='+se)
		se = 'NOMADS DOCU' ; list.append('&name_=' + addonString(30309).encode('utf-8') + '&&youtube_se='+se)
		se = 'BABYLON DOCU' ; list.append('&name_=' + addonString(30312).encode('utf-8') + '&&youtube_se='+se)
		
		c8 = 'plugin://plugin.video.exodus/?action=movies&url=http%3A%2F%2Fwww.imdb.com%2Fsearch%2Ftitle%3Ftitle_type%3Dfeature%2Ctv_movie%2Cdocumentary%26num_votes%3D100%2C%26release_date%3D%2Cdate%5B0%5D%26genres%3Dhistory%26sort%3Dmoviemeter%2Casc%26count%3D40%26start%3D1' ; list.append('&name_=' + 'Exodus Movies' + '&&custom8='+c8)
		c8 = 'plugin://plugin.video.exodus/?action=tvshows&url=http%3A%2F%2Fwww.imdb.com%2Fsearch%2Ftitle%3Ftitle_type%3Dtv_series%2Cmini_series%26release_date%3D%2Cdate%5B0%5D%26genres%3Dhistory%26sort%3Dmoviemeter%2Casc%26count%3D40%26start%3D1' ; list.append('&name_=' + 'Exodus Movies' + '&&custom8='+c8)
	
	elif num == 104:
		thumb = 'http://orig07.deviantart.net/ff1a/f/2009/033/1/3/science_wallpaper_by_hamdanzinha.jpg'
		fanart = 'http://wallpapercave.com/wp/582gycq.jpg'
		se = 'Technology DOCU' ; list.append('&name_=' + addonString(30403).encode('utf-8') + '&&youtube_se='+se)
		se = 'Humanities and Social Sciences DOCU' ; list.append('&name_=' + addonString(30401).encode('utf-8') + '&&youtube_se='+se)
		se = 'The science of nature DOCU' ; list.append('&name_=' + addonString(30402).encode('utf-8') + '&&youtube_se='+se)
		se = 'Researches DOCU' ; list.append('&name_=' + addonString(30404).encode('utf-8') + '&&youtube_se='+se)
		se = 'Scientific experiments DOCU' ; list.append('&name_=' + addonString(30405).encode('utf-8') + '&&youtube_se='+se)
		se = 'Politics DOCU' ; list.append('&name_=' + addonString(30422).encode('utf-8') + '&&youtube_se='+se)
		se = 'Philosophy DOCU' ; list.append('&name_=' + addonString(30425).encode('utf-8') + '&&youtube_se='+se)
		se = 'Economics DOCU' ; list.append('&name_=' + addonString(30426).encode('utf-8') + '&&youtube_se='+se)
		se = 'Psychology DOCU' ; list.append('&name_=' + addonString(30427).encode('utf-8') + '&&youtube_se='+se)
		se = 'Math DOCU' ; list.append('&name_=' + addonString(30430).encode('utf-8') + '&&youtube_se='+se)
		se = 'Biology DOCU' ; list.append('&name_=' + addonString(30431).encode('utf-8') + '&&youtube_se='+se)
		se = 'Physics DOCU' ; list.append('&name_=' + addonString(30432).encode('utf-8') + '&&youtube_se='+se)
		se = 'Chemistry DOCU' ; list.append('&name_=' + addonString(30433).encode('utf-8') + '&&youtube_se='+se)
		se = 'Medicine DOCU' ; list.append('&name_=' + addonString(30435).encode('utf-8') + '&&youtube_se='+se)
		se = 'Electronics DOCU' ; list.append('&name_=' + addonString(30453).encode('utf-8') + '&&youtube_se='+se)
		se = 'Computers DOCU' ; list.append('&name_=' + addonString(30452).encode('utf-8') + '&&youtube_se='+se)
		c8 = 'plugin://plugin.video.ted.talks/' ; list.append('&name_=' + 'Ted Talks' + '&&custom8='+c8)
		
	elif num == 105:
		'''Animals / בעלי-חיים'''
		thumb = 'http://3.bp.blogspot.com/-GmdLk2R6ahA/T55Ud9aXCcI/AAAAAAAABY4/4Z9aMnM0Ukc/s1600/Blue-Butterfuly-Latest-Animal-Wallpaper-2012.jpg'
		fanart = ''
		se = 'ANIMALS DOCU' ; list.append('&name_=' + addonString(30103).encode('utf-8') + '&&youtube_se='+se)
		se = 'ANIMALS 4K' ; list.append('&name_=' + addonString(30103).encode('utf-8') + ' 4K' + '&&youtube_se='+se)
		se = 'LION DOCU' ; list.append('&name_=' + addonString(30110).encode('utf-8') + '&&youtube_se='+se)
		se = 'GIRAFFE DOCU' ; list.append('&name_=' + addonString(30111).encode('utf-8') + '&&youtube_se='+se)
		se = 'BEE DOCU' ; list.append('&name_=' + addonString(30121).encode('utf-8') + '&&youtube_se='+se)
		se = 'FISH DOCU' ; list.append('&name_=' + addonString(30116).encode('utf-8') + '&&youtube_se='+se)
		se = 'ELEFHANT DOCU' ; list.append('&name_=' + addonString(30112).encode('utf-8') + '&&youtube_se='+se)
		se = 'TIGRIS DOCU' ; list.append('&name_=' + addonString(30113).encode('utf-8') + '&&youtube_se='+se)
		se = 'DOG DOCU' ; list.append('&name_=' + addonString(30119).encode('utf-8') + '&&youtube_se='+se)
		se = 'SHARK DOCU' ; list.append('&name_=' + addonString(30117).encode('utf-8') + '&&youtube_se='+se)
		se = 'SNAKE DOCU' ; list.append('&name_=' + addonString(30118).encode('utf-8') + '&&youtube_se='+se)
		se = 'BIRD DOCU' ; list.append('&name_=' + addonString(30115).encode('utf-8') + '&&youtube_se='+se)
		se = 'MONKEY DOCU' ; list.append('&name_=' + addonString(30114).encode('utf-8') + '&&youtube_se='+se)
		se = 'CROCODILE DOCU' ; list.append('&name_=' + addonString(30120).encode('utf-8') + '&&youtube_se='+se)
		se = 'DRAGON DOCU' ; list.append('&name_=' + addonString(30122).encode('utf-8') + '&&youtube_se='+se)
		se = 'LIZARDS DOCU' ; list.append('&name_=' + addonString(30123).encode('utf-8') + '&&youtube_se='+se)
		se = 'BUGS DOCU' ; list.append('&name_=' + addonString(30124).encode('utf-8') + '&&youtube_se='+se)
		se = 'CAT DOCU' ; list.append('&name_=' + addonString(30125).encode('utf-8') + '&&youtube_se='+se)
		se = 'DINOSAUR DOCU' ; list.append('&name_=' + addonString(30126).encode('utf-8') + '&&youtube_se='+se)
		se = 'BAT DOCU' ; list.append('&name_=' + addonString(30127).encode('utf-8') + '&&youtube_se='+se)
		se = 'PANTHER animal DOCU' ; list.append('&name_=' + addonString(30128).encode('utf-8') + '&&youtube_se='+se)
		se = 'Mamuth DOCU' ; list.append('&name_=' + addonString(30129).encode('utf-8') + '&&youtube_se='+se)
		se = 'SPIDER DOCU' ; list.append('&name_=' + addonString(30130).encode('utf-8') + '&&youtube_se='+se)
		se = 'BEAR DOCU' ; list.append('&name_=' + addonString(30131).encode('utf-8') + '&&youtube_se='+se)
		se = 'OCTOPUS DOCU' ; list.append('&name_=' + addonString(30132).encode('utf-8') + '&&youtube_se='+se)
		se = 'WOLFS DOCU' ; list.append('&name_=' + addonString(30133).encode('utf-8') + '&&youtube_se='+se)
	
	elif num == 106:
		'''Planet Earth / כדור הארץ'''
		thumb = 'https://s-media-cache-ak0.pinimg.com/originals/f6/7c/e8/f67ce86161d17cbde49bac13be0ea023.jpg'
		fanart = 'https://s-media-cache-ak0.pinimg.com/originals/99/db/19/99db19557aec73a897f07992cbc4d0c8.jpg'
		se = 'PLANET EARTH DOCU' ; list.append('&name_=' + addonString(30105).encode('utf-8') + '&&youtube_se='+se)
		se = 'WORLD PLACES DOCU' ; list.append('&name_=' + addonString(30180).encode('utf-8') + '&&youtube_se='+se)
		se = 'OCEANS DOCU' ; list.append('&name_=' + addonString(30181).encode('utf-8') + '&&youtube_se='+se)
		se = 'EARTH CLIMATE DOCU' ; list.append('&name_=' + addonString(30182).encode('utf-8') + '&&youtube_se='+se)
		se = 'Natural phenomena and disasters DOCU' ; list.append('&name_=' + addonString(30183).encode('utf-8') + '&&youtube_se='+se)
		
	return list, thumb, fanart
	
def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	CATEGORIES_SEARCH(mode=30, url="")
	addDir(addonString(30000).encode('utf-8'),'MyDocu',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0, getAddonFanart(100, default="https://i.ytimg.com/vi/esMX5NIsHdk/maxresdefault.jpg")) #My Docu
	list, thumb, fanart = getList(101) ; addDir(addonString(30001).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30001).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(102) ; addDir(addonString(30002).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30002).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(103) ; addDir(addonString(30003).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30003).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(105) ; addDir(addonString(30005).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30005).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(104) ; addDir(addonString(30004).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30004).encode('utf-8')),'1',0,fanart)
	
	addDir(addonString(30007).encode('utf-8'),'',107,'http://www.muralswallpaper.co.uk/sites/default/files/styles/full_lightbox/public/product_images/Cute-Animals-Kids-Wallpaper-Mural.jpg?itok=F5n249_x',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30007).encode('utf-8')),'1',0, getAddonFanart(107, default="")) #Kids
	addDir(addonString(30008).encode('utf-8'),'',108,'http://in.bgu.ac.il/welcome/EventGalleries/%D7%9C%D7%A9%D7%95%D7%9F%20%D7%A2%D7%91%D7%A8%D7%99%D7%AA.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30008).encode('utf-8')),'1',0, getAddonFanart(108, default="https://i.ytimg.com/vi/JiRWesm6e04/maxresdefault.jpg")) #דוקומנטרי ישראלי
	addDir(addonString(30009).encode('utf-8'),'',110,'http://crownheights.org/wp-content/uploads/2015/07/art.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30009).encode('utf-8')),'1',0, getAddonFanart(110, default="http://hdwallpapersd.com/wp-content/uploads/2015/08/amazing-street-art-best-3d-graffiti-hd-wallpaper-desktop.jpg")) #Art
	
	addon = 'plugin.video.smithsonian'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30010).encode('utf-8'),'plugin://'+addon,8,thumb,plot,addon,58, getAddonFanart(110, custom=""))
	'''---------------------------'''

def CATEGORIES100(name, iconimage, desc, fanart):
	'''------------------------------
	---My-Docu-----------------------
	------------------------------'''
	fanart = 100
	
	'''כפתור דוקו חדש..'''
	addDir(addonString_servicefeatherence(32450).encode('utf-8') % (addonString(100).encode('utf-8')),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(32451).encode('utf-8') + addonString_servicefeatherence(32452).encode('utf-8') + addonString_servicefeatherence(32453).encode('utf-8'),'s',0, getAddonFanart(fanart))
	
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',0, getAddonFanart("Custom_Playlist1"))
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',0, getAddonFanart("Custom_Playlist2"))
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',0, getAddonFanart("Custom_Playlist3"))
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',0, getAddonFanart("Custom_Playlist4"))
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',0, getAddonFanart("Custom_Playlist5"))
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',0, getAddonFanart("Custom_Playlist6"))
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',0, getAddonFanart("Custom_Playlist7"))
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',0, getAddonFanart("Custom_Playlist8"))
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',0, getAddonFanart("Custom_Playlist9"))
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',0, getAddonFanart("Custom_Playlist10"))

def CATEGORIES107(name, iconimage, desc, fanart):
	'''ילדים'''
	background = 107
	
	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'Kids Documentary',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES107Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

	'''בעלי חיים לילדים'''
	list = []
	list.append('&youtube_pl=PL7BFAF7CBEF48B98D')
	list.append('&youtube_pl=PLnoO3k54vcBTWDArEYxKGDBZXkVv7GM1F')
	list.append('&youtube_pl=PL2Zef9KQGytUntJegeTmJxAFlIkaTRo-P')
	list.append('&youtube_pl=PLakLrQJOovvlpJzAuQuWN8yOszoycRTzz')
	list.append('&youtube_pl=PLbELaiA4QD9owZGT2vRmvbnvBBfQIlg9q')
	list.append('&youtube_pl=uTvsWsnygMq7BLVmRxI7rokS')
	list.append('&youtube_id=Ood3teygwh8')
	list.append('&youtube_id=qnaXJf_yaj8')
	list.append('&youtube_id=p5qwOxlvyhk')
	list.append('&youtube_id=w5N2TN520U8')
	addDir(addonString(30103).encode('utf-8') + space + addonString(30100).encode('utf-8'),list,17,'https://d3373c9sxdao7y.cloudfront.net/content/product/large/05328RAV.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30103).encode('utf-8') + space + addonString(30100).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''חלל לילדים'''
	list = []
	list.append('&youtube_id=-xKKzIoJgMSQ')
	list.append('&youtube_pl=PLRkXn_ayyCS8kOR-EKAbWx5hS_YUBEo5')
	list.append('&youtube_pl=PLwmqN2cDkUGtn_gPHUpPfLwWF3Sp9BS3R')
	list.append('&youtube_pl=PLRkXn_ayyCS8kOR-PLudXYjXPY1I6JnkHTWUiHJEvZd6f5_C26')
	list.append('&youtube_pl=PLDO7YrQpg54RumJmx39xie-QGa9NUCyFd')
	addDir(addonString(30002).encode('utf-8') + space + addonString(30100).encode('utf-8'),list,17,'http://4.bp.blogspot.com/-EB8N_Kjqiws/T4KSeG48w4I/AAAAAAAAA5Q/3hs2tGC3e38/s1600/Display-Cool-Space-Wallpaper.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30002).encode('utf-8') + space + addonString(30100).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''נשיונל ג'יאוגרפיק לילדים'''
	list = []
	list.append('&youtube_ch=UCav9nv7-is8vF7vrH16KPZg')	
	addDir(addonString(30999).encode('utf-8') + space + addonString(30100).encode('utf-8'),list,17,'http://espana.paninimagazine.com/store/media/catalog/product/cache/5/image/800x600/9df78eab33525d08d6e5fb8d27136e95/s/n/snage018_0.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30999).encode('utf-8') + space + addonString(30100).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
  
	'''צמחים לילדים'''
	list = []
	list.append('&youtube_pl=PLy0B6ncmGtqd-wb1Iqh036p3l9ZN4OCZ0')
	list.append('&youtube_pl=PLlKRPDYgEh4xRq0AYTCwWduDmhq1yFPHY')
	list.append('&youtube_pl=PL2Zef9KQGytUntJegeTmJxAFlIkaTRo-P')
	list.append('&youtube_pl=PLfo1kYEnYLcJ-UhenL0Yf3afIR3zw7fr2')
	list.append('&youtube_pl=PLeUPs98mdCOLKpvPU8tr1-1rgJ1h_xgxA')
	list.append('&youtube_pl=PLamCflZiuToNeoHktZvD07ti-g-F1SFki')
	addDir(addonString(30104).encode('utf-8') + space + addonString(30100).encode('utf-8'),list,17,'https://cdn-jr.brainpop.com/topics/plantadaptations/motw_graphic.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30104).encode('utf-8') + space + addonString(30100).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES107A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES108(name, iconimage, desc, fanart):
	'''בעברית'''
	background = 108
	
	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'דוקו',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES108Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''דוקו סרטים'''
	list = []
	list.append('&youtube_id=jC5iaonGRCg')
	list.append('&youtube_id=4pBLynGT5ZA')
	list.append('&youtube_id=NEnRsTlSsxM')
	list.append('&youtube_id=JsPuREOKvPc')
	list.append('&youtube_id=Qw3lObBE8WE')
	list.append('&youtube_id=vYzxryWHVZs')
	list.append('&youtube_id=uIotx1aGtKg')
	addDir(addonString(30800).encode('utf-8'),list,17,'http://www.wallpapergeeks.com/wp-content/uploads/2014/12/african-safari-zebras-wallpaper-800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30800).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''חוצה ישראל'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4zFxXNjp8UC6nE9ePEQ9Ai')
	list.append('&youtube_pl=PL127E7734AE7476DD')
	list.append('&youtube_pl=PL3n39NB10sYkxOj0jlAWVtxGJBkMosU1K')
	addDir(addonString(30802).encode('utf-8'),list,17,'https://i.ytimg.com/vi/i9GSeDTY5BE/maxresdefault.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30802).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''טבע ישראלי'''
	list = []
	list.append('&youtube_id=AoizSL-TEJQ')
	list.append('&youtube_id=cn6RKXod9zk')
	list.append('&youtube_id=RjLTWrxhJG0')
	list.append('&youtube_id=cCb2r8stBuM')
	list.append('&youtube_id=xPWtMZ-mGCM')
	list.append('&youtube_pl=PLq714Bj5JxO4x_MMlDQpC-FTPV64mfhGP')
	list.append('&youtube_pl=PLHv0VZq_Hje7b_ZUanXVHHLtzoFe8zUsn')
	list.append('&youtube_pl=PLZxxWjeQgN4s1cXnvkS6rWDGKCI1YYW8g')
	list.append('&youtube_pl=PLTa6eP38rKWV9jW-XdavVcQtM72hIGPVF')
	list.append('&youtube_pl=PL6A2CaEev7b4vrILtDfeCszrTq1rsXl_c')
	list.append('&youtube_pl=PL762D7FD5B70D28C0')
	addDir(addonString(30801).encode('utf-8'),list,17,'http://www.israel-travel-secrets.com/images/Meshushim-pool3.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30801).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''מקבלים שבת'''
	list = []
	list.append('&youtube_pl=PLLttfoK87AdVbyvsH-HGmT2on83Y9UzMo')
	list.append('&youtube_pl=PLLttfoK87AdVbyvsH-HGmT2on83Y9UzMo')
	list.append('&youtube_pl=PLE1B47D7CC412DC7B')
	addDir(addonString(30803).encode('utf-8'),list,17,'http://www.iba.org.il/pictures/p452860.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30803).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''היסטוריה ישראלית'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4IjHf-ISoprm2r9FO0szaD')		
	list.append('&youtube_pl=PLT-roSWIpp1GjJ0pa8PMmOs__wfTT-VMw')
	list.append('&youtube_pl=PLfHmQCZe1ktg9G7Too6IjmJfVPEeHfXCq')
	list.append('&youtube_pl=PL-gwOOmKp2HGIUUERL61UO9kHSKI5F7dY')
	list.append('&youtube_pl=PLvLpu_onn8GsfbR34yRoIOOVhJr8Bo0fJ')
	list.append('&youtube_pl=PLth1a195qHsgMfvA86lvv98Jt6mI5Jq17')
	list.append('&youtube_pl=PL51YAgTlfPj4IjHf-ISoprm2r9FO0szaD')	
	list.append('&youtube_pl=PL1OR9gJeDv2a8Tdfe0YTXzojKK8rSm36c')
	list.append('&youtube_pl=PLBB3ncGmqWJFNfcnBO-TEdTqs8ovCBiqm')
	list.append('&youtube_pl=PL7AqoEETVtK66cFOkIjGVTmXd_C7Q0r90')
	list.append('&youtube_pl=PLjURn7HFksDKqxsERATYFlzmBVpp1vNGY')
	list.append('&youtube_pl=PLLttfoK87AdV7Q8Eu8a_J3pVv28nC2lMv')
	list.append('&youtube_pl=PLLttfoK87AdV7Q8Eu8a_J3pVv28nC2lMv')
	list.append('&youtube_id=EFD_o0-1QbQ')
	list.append('&youtube_id=L5Wq-ma70tY')
	addDir(addonString(30804).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/d/d8/%D7%9C%D7%95%D7%92%D7%95_%D7%A2%D7%A8%D7%95%D7%A5_%D7%94%D7%94%D7%99%D7%A1%D7%98%D7%95%D7%A8%D7%99%D7%94.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30804).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''דוקו ישראלי'''
	list = []
	list.append('&youtube_pl=PLv8p71sW2GjxrF8oXQeDlqDCtELS9dVg5')		
	list.append('&youtube_pl=PLqwNAHu38eWXT7BdjK28TC1PmL1kzzEwB')
	list.append('&youtube_pl=PLT_oMlvxWt_09lgcujCrv10eOWvR-is6o')
	list.append('&youtube_pl=PL-p_vqDAgZc7A')
	list.append('&youtube_id=g6RU5xVaywc')
	list.append('&youtube_id=Sn8M283kGj0')
	list.append('&youtube_id=DOEisLFmPrs')	
	list.append('&youtube_pl=PLhAvByb6CVNucuFXKM17ZNTO7RgqZ06jW')
	list.append('&youtube_pl=PLeCnWyfgXGWQHx6Enc80Q70foHGq5qrIz')
	list.append('&youtube_pl=PL6ADAC23F75CCB91F')
	list.append('&youtube_pl=PLhAvByb6CVNtiMfk1VQhdycNyOWxYhNUT')
	addDir(addonString(30805).encode('utf-8'),list,17,'http://images.photolight.co.il/photo/2006-06-24/15120.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30805).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''תרבות-חינוכית'''
	list = []
	list.append('&youtube_ch=23Culture')
	addDir(addonString(30806).encode('utf-8'),list,17,'https://yt3.ggpht.com/-PVEs_ee6CxU/AAAAAAAAAAI/AAAAAAAAAAA/NNkej9cD-YA/s100-c-k-no/photo.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30806).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''ערוץ הגיון ומדע'''
	list = []
	list.append('&youtube_ch=ScienceReasonIsrael')
	list.append('&youtube_ch=UCLpn_QJwfehfKuTt0orfYDw')
	addDir(addonString(30807).encode('utf-8'),list,17,'http://www.iba.org.il/zap/pictures/P670944.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30807).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''מאקו הרצאות'''
	addon = 'plugin.video.MakoTV'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fstatic1.squarespace.com%2fstatic%2f545c3cefe4b0263200cf8bb7%2ft%2f5474d191e4b0dda9e3ce84e7%2f1416941970318%2flecture.jpg%3fformat%3d1500w&mode=0&name=%d7%94%d7%a8%d7%a6%d7%90%d7%95%d7%aa&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-more%2flectures')
	addDir(addonString(30808).encode('utf-8'),list,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''מאקו דוקו'''
	addon = 'plugin.video.MakoTV'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV//?iconimage=http%3a%2f%2fopendoclab.mit.edu%2fwp%2fwp-content%2fuploads%2f2011%2f09%2fcamera.jpg&mode=0&name=%d7%93%d7%95%d7%a7%d7%95&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-more%2fdocu_tv')
	addDir(addonString(30809).encode('utf-8'),list,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))

	'''וואלה דוקו'''
	addon = 'plugin.video.wallaNew.video'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	list = []
	list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=wallavod&name=%d7%93%d7%95%d7%a7%d7%95%20(56)&url=genre%3dmovies%26genreId%3d6263')
	addDir(addonString(30810).encode('utf-8'),list,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))

	'''ערוץ 8'''
	addon = 'plugin.video.seretil'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	list = []
	list.append('&custom8=plugin://plugin.video.hotVOD.video/?mode=5&name=%d7%a2%d7%a8%d7%95%d7%a5%208&url=http%3a%2f%2fhot.ynet.co.il%2fhome%2f0%2c7340%2cL-7461%2c00.html')
	addDir(addonString(30811).encode('utf-8'),list,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''דוקו 10'''
	addon = 'plugin.video.ilten'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30812).encode('utf-8'),'plugin://'+addon+'/?category=2118',8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''sertil דוקו'''
	addon = 'plugin.video.seretil'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30813).encode('utf-8'),'plugin://'+addon+'/?iconimage=http%3a%2f%2fimages.nationalgeographic.com%2fwpf%2fsites%2fcommon%2fi%2fpresentation%2fNGLogo560x430-cb1343821768.png&mode=4&name=%d7%a0%d7%a9%d7%99%d7%95%d7%a0%d7%9c%20%d7%92%d7%90%d7%95%d7%92%d7%a8%d7%a4%d7%99%d7%a7&url=http%3a%2f%2fseretil.me%2fcategory%2f%25D7%25A0%25D7%25A9%25D7%2599%25D7%2595%25D7%25A0%25D7%259C-%25D7%2592%25D7%2599%25D7%2590%25D7%2595%25D7%2592%25D7%25A8%25D7%25A4%25D7%2599%25D7%25A7%2fpage1%2f',8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''movix דוקו'''
	addon = 'plugin.video.movixws'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30814).encode('utf-8'),'plugin://'+addon+'/?description&iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2faaron-sinuhe%2ftv-movie-folder%2f512%2fDocumentaries-National-Geographic-icon.png&mode=2&name=Documentary%20-%20%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99&url=http%3a%2f%2fwww.movix.me%2fgenres%2fDocumentary',8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''דוקו sdarot'''
	addon = 'plugin.video.sdarot.tv'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30815).encode('utf-8'),'plugin://'+addon+'/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f11%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&name=%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&summary&url=all-heb',8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''ילדים'''
	addDir(addonString(30007).encode('utf-8'),'',10801,'http://www.disneywallpaper.net/data/media/7/Winnie_the_Pooh_kids.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30007).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES108A(name, iconimage, desc, fanart) #עמוד הבא

def CATEGORIES10801(name, iconimage, desc, fanart):
	'''בעברית - ילדים'''
	background = 10801
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10801Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
		
	'''גלילאו '''
	list = []
	list.append('&youtube_pl=PL01DA343E8BB95D12')
	list.append('&youtube_pl=PLeZqOp-eE-FpvoWCBK-G5Wr1y_VA5Y4ih')
	list.append('&youtube_pl=PLeZqOp-eE-FqJOAKrN7YN6aE8IsKxPqSZ&index=2')
	list.append('&youtube_pl=PL104313B485ECC1DB')
	list.append('&youtube_id=9Oyiis9B6pU')
	list.append('&youtube_id=sVXFm5lOqy8')
	list.append('&youtube_id=ku8mNNCrEys')
	list.append('&youtube_id=P5KW_r2Uu1c')
	addDir(addonString(30816).encode('utf-8'),list,17,'https://i.ytimg.com/vi/HZ7UHZcIuh0/maxresdefault.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30816).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
		
	'''היה היה'''
	list = []
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir(addonString(30817).encode('utf-8'),list,17,'http://www.asksheilta.com/wp-content/uploads/2009/06/fond04_8001.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30817).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES10801A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES110(name, iconimage, desc, fanart):
	'''------------------------------
	---Art-------------------
	------------------------------'''
	background = 110

	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'Art Docu',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))

	CATEGORIES110Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''צילום'''
	list = []
	list.append('&youtube_ch=DigitalRevCom')
	list.append('&youtube_ch=PhlearnLLC')
	list.append('&youtube_ch=thatnikonguy')
	list.append('&youtube_ch=theartofphotography')
	list.append('&youtube_pl=PLBE338967F8DB7F2A')
	list.append('&youtube_pl=PLJ6FIlZVNbQOYg4WXQN7ZpYK3FEH1GVco')
	list.append('&youtube_pl=PLBC5A73FEA8B7D7D2')
	list.append('&youtube_pl=PL0ajMRlXs96oTkC-ic_CrzJbM-y3p0F8s')
	list.append('&youtube_pl=PLCEE9B921EA84A6BF')
	list.append('&youtube_pl=PLBBCCB798B85DA47B')
	list.append('&youtube_pl=PLAD38BBF9053DE8DD')
	list.append('&youtube_pl=PL904CB241ED4AEE06')
	list.append('&youtube_pl=PL4F6CB4E3874F8483')
	list.append('&youtube_pl=PLF8Y1CD3PV0I2EYgQ6-DM3_UgZNnjDjeP')
	addDir(addonString(30850).encode('utf-8'),list,17,'https://wallpaperscraft.com/image/canon_clip_art_camera_photography_beach_42535_800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30850).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
	'''אומנים'''
	list = []
	list.append('&youtube_pl=PLgxrD7KGdqIAjKrX7044XQCCYyygH_Iip')
	list.append('&youtube_pl=PLgxrD7KGdqIBZ8L3mbbDWhtKVJx4P6VSY')
	list.append('&youtube_pl=PLYIapPsysmjCw77uxfyxW7HmdoMEooZzZ')
	list.append('&youtube_pl=PL3A50F86AE9A35934')
	list.append('&youtube_pl=PLgxrD7KGdqIAJLfcDPQHgj_mA6yMYFP0S')
	list.append('&youtube_pl=PLgxrD7KGdqICXqET81hxUjnbvRbQyw5bi')
	list.append('&youtube_pl=PLLUaXSRnKa3i3nijItUi0ifqGSS908qzA')
	addDir(addonString(30851).encode('utf-8'),list,17,'http://www.davidpaulkirkpatrick.com/wp-content/uploads/2013/03/van-Gogh-Self-Potrait_1889_1890.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30851).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
	'''עבודות אומנות'''
	list = []
	list.append('&youtube_pl=PLpKVHhjWeQ6_b9dCLPDTXNNLLrdSuwvQ')
	list.append('&youtube_pl=PLSVoinOQWRwRIzhWxuK2KWoHH454deajP')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	addDir(addonString(30852).encode('utf-8'),list,17,'https://wallpaperscraft.com/image/plate_paper_candy_pink_background_crafts_80738_800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30852).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
	'''שרטוט'''
	list = []
	list.append('&youtube_pl=PLhBKkQX9XSgeVEGuevcUrnxWYhyB31rZG')
	list.append('&youtube_pl=PLhBKkQX9XSgeALUlhjOdRwMaq7ucc6t6c')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	addDir(addonString(30853).encode('utf-8'),list,17,'http://orig00.deviantart.net/3a19/f/2013/230/1/8/drawing_michael_ealy_part_two_by_xjorieke-d6io2s8.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30853).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
   
	'''ציור'''
	list = []
	list.append('&youtube_pl=PLAEQD0ULngi67rwmhrkNjMZKvyCReqDV4')
	list.append('&youtube_pl=PL-OQ2u8XlJLuACG2jfzt_XxK8pDVsdIhm')
	list.append('&youtube_pl=PLCgkDVJst-Zhh6lqVu0UVUQPe68hgdEUo')
	list.append('&youtube_pl=PL2010F0BDC411BDC9')
	list.append('&youtube_pl=PL95664E97F3D868D7')
	addDir(addonString(30854).encode('utf-8'),list,17,'http://www.florenceartacademy.it/blog/wp-content/uploads/2013/07/Gioconda.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30854).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
  
	'''פיסול'''
	list = []
	list.append('&youtube_pl=PLdtE9aIU4iHlmdkhv2_oJg27s49CODbVC')
	list.append('&youtube_pl=PLB33559E547A1892B')
	list.append('&youtube_pl=PLcAAX2LjtsB6Eczr5HaHGxlAboQLgPv6I')
	list.append('&youtube_pl=PL0BF8F437080FBFB3')
	list.append('&youtube_pl=PLCD685A75D9C854E1')
	list.append('&youtube_pl=PLaOZQCQIBfZQ3EKqPb3w-Y-lK7InP63K6')
	list.append('&youtube_pl=PLaOZQCQIBfZSVI0_DYZmJr21RtURiVmI9')
	list.append('&youtube_pl=PLaOZQCQIBfZR26CsNo5xy1ezj68uF2Fue')
	list.append('&youtube_pl=PLaOZQCQIBfZTTXxj9cV6lTBDviu86Bwp8')
	list.append('&youtube_pl=PLaOZQCQIBfZTlvg0j2Hn-xr0M8ZGUzZZT')
	list.append('&youtube_pl=PLaOZQCQIBfZSqT2fIRR8P_thmLvawqSOQ')
	addDir(addonString(30855).encode('utf-8'),list,17,'https://s-media-cache-ak0.pinimg.com/736x/ef/06/95/ef0695c68517e3baaf58313d82573984.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30855).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
  
	CATEGORIES110A(name, iconimage, desc, fanart) #עמוד הבא