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
		''''''
		thumb = ''
		fanart = ''
		#se = 'Nature Ultra HD' ; list.append('&name_=' + 'addonString(30001)' + ' Ultra HD' + '&&youtube_se='+se)

	elif num == 102:
		'''Space / חלל'''
		thumb = 'http://www.esa.int/var/esa/storage/images/esa_multimedia/images/2014/02/searching_for_exoplanetary_systems/14282306-1-eng-GB/Searching_for_exoplanetary_systems.jpg'
		se = 'Alien space DOCU' ; list.append('&name_=' + 'addonString(30207)' + '&&youtube_se='+se)
		se = 'Space Astronauts DOCU' ; list.append('&name_=' + 'addonString(30204)' + '&&youtube_se='+se)
		se = 'Space Astronomy DOCU' ; list.append('&name_=' + 'addonString(30203)' + '&&youtube_se='+se)
		se = 'BLACK HOLE space DOCU' ; list.append('&name_=' + 'addonString(30212)' + '&&youtube_se='+se)
		se = 'Space Exploration DOCU' ; list.append('&name_=' + 'addonString(30201)' + '&&youtube_se='+se)
		se = 'Hubble Space Telescope DOCU' ; list.append('&name_=' + 'addonString(30202)' + '&&youtube_se='+se)
		se = 'MARS space DOCU' ; list.append('&name_=' + 'addonString(30208)' + '&&youtube_se='+se)
		se = 'METEORS space DOCU' ; list.append('&name_=' + 'addonString(30213)' + '&&youtube_se='+se)
		se = 'MOON space DOCU' ; list.append('&name_=' + 'addonString(30211)' + '&&youtube_se='+se)
		se = 'Space DOCU' ; list.append('&name_=' + 'addonString(30002)' + '&&youtube_se='+se)
		se = 'SPACESHIP space DOCU' ; list.append('&name_=' + 'addonString(30209)' + '&&youtube_se='+se)
		se = 'SPEED OF LIGHT space DOCU' ; list.append('&name_=' + 'addonString(30210)' + '&&youtube_se='+se)
		c8 = 'plugin://plugin.video.eso/' ; list.append('&name_=' + 'ESO' + '&&custom8='+c8)
		c8 = 'plugin://plugin.video.esa/' ; list.append('&name_=' + 'ESA' + '&&custom8='+c8)
	
	elif num == 103:
		thumb = 'http://wsap.academy/wp-content/uploads/2015/03/1123676.jpg'
		fanart = 'http://www.anratechnologies.com/home/wp-content/uploads/2016/11/history.jpg'
		se = 'BABYLON DOCU' ; list.append('&name_=' + 'addonString(30312)' + '&&youtube_se='+se)
		se = 'BIBLE DOCU' ; list.append('&name_=' + 'addonString(30306)' + '&&youtube_se='+se)
		se = 'FREE MASONS DOCU' ; list.append('&name_=' + 'addonString(30310)' + '&&youtube_se='+se)
		se = 'Historical armies DOCU' ; list.append('&name_=' + 'addonString(30302)' + '&&youtube_se='+se)
		se = 'History Channel DOCU' ; list.append('&name_=' + 'addonString(30300)' + '&&youtube_se='+se)
		se = 'ISRAEL DOCU' ; list.append('&name_=' + 'addonString(30304)' + '&&youtube_se='+se)
		se = 'JERUSALEM DOCU' ; list.append('&name_=' + 'addonString(30308)' + '&&youtube_se='+se)
		se = 'JESUS DOCU' ; list.append('&name_=' + 'addonString(30305)' + '&&youtube_se='+se)
		se = 'KING SOLOMON DOCU' ; list.append('&name_=' + 'addonString(30313)' + '&&youtube_se='+se)
		se = 'NOMADS DOCU' ; list.append('&name_=' + 'addonString(30309)' + '&&youtube_se='+se)
		se = 'ROMANS DOCU' ; list.append('&name_=' + 'addonString(30303)' + '&&youtube_se='+se)
		se = 'STONE, BRONZE, IRON, NEW AGE DOCU' ; list.append('&name_=' + 'addonString(30311)' + '&&youtube_se='+se)
		se = 'VIKINGS DOCU' ; list.append('&name_=' + 'addonString(30307)' + '&&youtube_se='+se)
		se = 'World War 1 DOCU' ; list.append('&name_=' + 'addonString(30301)' + ' 1' + '&&youtube_se='+se)
		se = 'World War 2 DOCU' ; list.append('&name_=' + 'addonString(30301)' + ' 2' +  '&&youtube_se='+se)
		se = 'World War 3 DOCU' ; list.append('&name_=' + 'addonString(30301)' + ' 3' +  '&&youtube_se='+se)
		
		c8 = 'plugin://plugin.video.exodus/?action=movies&url=http%3A%2F%2Fwww.imdb.com%2Fsearch%2Ftitle%3Ftitle_type%3Dfeature%2Ctv_movie%2Cdocumentary%26num_votes%3D100%2C%26release_date%3D%2Cdate%5B0%5D%26genres%3Dhistory%26sort%3Dmoviemeter%2Casc%26count%3D40%26start%3D1' ; list.append('&name_=' + 'Movies' + '&&custom8='+c8)
		c8 = 'plugin://plugin.video.exodus/?action=tvshows&url=http%3A%2F%2Fwww.imdb.com%2Fsearch%2Ftitle%3Ftitle_type%3Dtv_series%2Cmini_series%26release_date%3D%2Cdate%5B0%5D%26genres%3Dhistory%26sort%3Dmoviemeter%2Casc%26count%3D40%26start%3D1' ; list.append('&name_=' + 'TVShows' + '&&custom8='+c8)
	
	elif num == 104:
		thumb = 'http://orig07.deviantart.net/ff1a/f/2009/033/1/3/science_wallpaper_by_hamdanzinha.jpg'
		fanart = 'http://wallpapercave.com/wp/582gycq.jpg'

		se = 'Biology DOCU' ; list.append('&name_=' + 'addonString(30431)' + '&&youtube_se='+se)
		se = 'Chemistry DOCU' ; list.append('&name_=' + 'addonString(30433)' + '&&youtube_se='+se)
		se = 'Computers DOCU' ; list.append('&name_=' + 'addonString(30452)' + '&&youtube_se='+se)
		se = 'Economics DOCU' ; list.append('&name_=' + 'addonString(30426)' + '&&youtube_se='+se)
		se = 'Electronics DOCU' ; list.append('&name_=' + 'addonString(30453)' + '&&youtube_se='+se)
		se = 'Humanities and Social Sciences DOCU' ; list.append('&name_=' + 'addonString(30401)' + '&&youtube_se='+se)
		se = 'Math DOCU' ; list.append('&name_=' + 'addonString(30430)' + '&&youtube_se='+se)
		se = 'Medicine DOCU' ; list.append('&name_=' + 'addonString(30435)' + '&&youtube_se='+se)
		se = 'Philosophy DOCU' ; list.append('&name_=' + 'addonString(30425)' + '&&youtube_se='+se)
		se = 'Physics DOCU' ; list.append('&name_=' + 'addonString(30432)' + '&&youtube_se='+se)
		se = 'Politics DOCU' ; list.append('&name_=' + 'addonString(30422)' + '&&youtube_se='+se)
		se = 'Psychology DOCU' ; list.append('&name_=' + 'addonString(30427)' + '&&youtube_se='+se)
		se = 'Researches DOCU' ; list.append('&name_=' + 'addonString(30404)' + '&&youtube_se='+se)
		se = 'Scientific experiments DOCU' ; list.append('&name_=' + 'addonString(30405)' + '&&youtube_se='+se)
		se = 'Technology DOCU' ; list.append('&name_=' + 'addonString(30403)' + '&&youtube_se='+se)
		se = 'The science of nature DOCU' ; list.append('&name_=' + 'addonString(30402)' + '&&youtube_se='+se)
		
		c8 = 'plugin://plugin.video.ted.talks/' ; list.append('&name_=' + 'Ted Talks' + '&&custom8='+c8)
		
	elif num == 105:
		'''Animals / בעלי-חיים'''
		thumb = 'http://3.bp.blogspot.com/-GmdLk2R6ahA/T55Ud9aXCcI/AAAAAAAABY4/4Z9aMnM0Ukc/s1600/Blue-Butterfuly-Latest-Animal-Wallpaper-2012.jpg'
		fanart = ''
		se = 'ANIMALS DOCU' ; list.append('&name_=' + 'addonString(30005)' + '&&youtube_se='+se)
		se = 'ANIMALS 4K' ; list.append('&name_=' + 'addonString(30005)' + ' 4K' + '&&youtube_se='+se)
		se = 'BAT DOCU' ; list.append('&name_=' + 'addonString(30127)' + '&&youtube_se='+se)
		se = 'BEAR DOCU' ; list.append('&name_=' + 'addonString(30131)' + '&&youtube_se='+se)
		se = 'BEE DOCU' ; list.append('&name_=' + 'addonString(30121)' + '&&youtube_se='+se)
		se = 'BIRD DOCU' ; list.append('&name_=' + 'addonString(30115)' + '&&youtube_se='+se)
		se = 'BUGS DOCU' ; list.append('&name_=' + 'addonString(30124)' + '&&youtube_se='+se)
		se = 'BUTTERFLY DOCU' ; list.append('&name_=' + 'addonString(30134)' + '&&youtube_se='+se)
		se = 'CAT DOCU' ; list.append('&name_=' + 'addonString(30125)' + '&&youtube_se='+se)
		se = 'CROCODILE DOCU' ; list.append('&name_=' + 'addonString(30120)' + '&&youtube_se='+se)
		se = 'DINOSAUR DOCU' ; list.append('&name_=' + 'addonString(30126)' + '&&youtube_se='+se)
		se = 'DOG DOCU' ; list.append('&name_=' + 'addonString(30119)' + '&&youtube_se='+se)
		se = 'DRAGON DOCU' ; list.append('&name_=' + 'addonString(30122)' + '&&youtube_se='+se)
		se = 'ELEFHANT DOCU' ; list.append('&name_=' + 'addonString(30112)' + '&&youtube_se='+se)
		se = 'FISH DOCU' ; list.append('&name_=' + 'addonString(30116)' + '&&youtube_se='+se)
		se = 'GIRAFFE DOCU' ; list.append('&name_=' + 'addonString(30111)' + '&&youtube_se='+se)
		se = 'LION DOCU' ; list.append('&name_=' + 'addonString(30110)' + '&&youtube_se='+se)
		se = 'LIZARDS DOCU' ; list.append('&name_=' + 'addonString(30123)' + '&&youtube_se='+se)
		se = 'Mamuth DOCU' ; list.append('&name_=' + 'addonString(30129)' + '&&youtube_se='+se)
		se = 'MONKEY DOCU' ; list.append('&name_=' + 'addonString(30114)' + '&&youtube_se='+se)
		se = 'OCTOPUS DOCU' ; list.append('&name_=' + 'addonString(30132)' + '&&youtube_se='+se)
		se = 'PANTHER animal DOCU' ; list.append('&name_=' + 'addonString(30128)' + '&&youtube_se='+se)
		se = 'SHARK DOCU' ; list.append('&name_=' + 'addonString(30117)' + '&&youtube_se='+se)
		se = 'SNAKE DOCU' ; list.append('&name_=' + 'addonString(30118)' + '&&youtube_se='+se)
		se = 'SPIDER DOCU' ; list.append('&name_=' + 'addonString(30130)' + '&&youtube_se='+se)
		se = 'TIGRIS DOCU' ; list.append('&name_=' + 'addonString(30113)' + '&&youtube_se='+se)
		se = 'WOLFS DOCU' ; list.append('&name_=' + 'addonString(30133)' + '&&youtube_se='+se)
	
	elif num == 106:
		'''Planet Earth / כדור הארץ'''
		thumb = 'https://s-media-cache-ak0.pinimg.com/originals/f6/7c/e8/f67ce86161d17cbde49bac13be0ea023.jpg'
		fanart = 'https://s-media-cache-ak0.pinimg.com/originals/99/db/19/99db19557aec73a897f07992cbc4d0c8.jpg'
		se = 'CLIMATE EARTH DOCU' ; list.append('&name_=' + 'addonString(30182)' + '&&youtube_se='+se)
		se = 'Natural phenomena and disasters DOCU' ; list.append('&name_=' + 'addonString(30183)' + '&&youtube_se='+se)
		se = 'Nature Ultra HD' ; list.append('&name_=' + 'addonString(30001)' + ' Ultra HD' + '&&youtube_se='+se)
		se = 'OCEANS EARTH DOCU' ; list.append('&name_=' + 'addonString(30181)' + '&&youtube_se='+se)
		se = 'PLANET EARTH DOCU' ; list.append('&name_=' + 'addonString(30006)' + '&&youtube_se='+se)
		se = 'TREES DOCU' ; list.append('&name_=' + 'addonString(30171)' + '&&youtube_se='+se)
		se = 'WORLD WONDER EARTH  DOCU' ; list.append('&name_=' + 'addonString(30180)' + '&&youtube_se='+se)
	
	elif num == 107:
		'''Milatry / צבאי'''
		thumb = 'https://www.armyrecognition.com/images/stories/customer/rafael/land/Spyder_missile_system_Rafael_IsraeL_Israeli_defence_industry_001.jpg'
		fanart = 'https://i.ytimg.com/vi/VgukAu2Lvrg/maxresdefault.jpg'
		se = 'AIRCRAFT CARRIER DOCU' ; list.append('&name_=' + 'addonString(30709)' + '&&youtube_se='+se)
		se = 'Artillery DOCU' ; list.append('&name_=' + 'addonString(30712)' + '&&youtube_se='+se)
		se = 'COMBAT DRONES DOCU' ; list.append('&name_=' + 'addonString(30710)' + '&&youtube_se='+se)
		se = 'Combat helicopters DOCU' ; list.append('&name_=' + 'addonString(30702)' + '&&youtube_se='+se)
		se = 'COMBAT ROBOTS DOCU' ; list.append('&name_=' + 'addonString(30718)' + '&&youtube_se='+se)
		se = 'CYBER WAR MILITARY DOCU' ; list.append('&name_=' + 'addonString(30717)' + '&&youtube_se='+se)
		se = 'DEFENSE SYSTEM MILITARY DOCU' ; list.append('&name_=' + 'addonString(30715)' + '&&youtube_se='+se)
		se = 'DESTROYER MILITARY NAVY DOCU' ; list.append('&name_=' + 'addonString(30707)' + '&&youtube_se='+se)
		se = 'fighter jets bombers DOCU' ; list.append('&name_=' + 'addonString(30701)' + '&&youtube_se='+se)
		se = 'GENERALS MILITARY DOCU' ; list.append('&name_=' + 'addonString(30716)' + '&&youtube_se='+se)
		se = 'MISSILES DOCU' ; list.append('&name_=' + 'addonString(30703)' + '&&youtube_se='+se)
		se = 'MILITARY TECH DOCU' ; list.append('&name_=' + 'addonString(30007)' + '&&youtube_se='+se)
		se = 'Modern Infantry DOCU' ; list.append('&name_=' + 'addonString(30714)' + '&&youtube_se='+se)
		se = 'MOSSAD DOCU' ; list.append('&name_=' + 'addonString(30708)' + '&&youtube_se='+se)
		se = 'NUCLEAR WEAPON DOCU' ; list.append('&name_=' + 'addonString(30705)' + '&&youtube_se='+se)
		se = 'Paratroopers military DOCU' ; list.append('&name_=' + 'addonString(30711)' + '&&youtube_se='+se)
		se = 'SAM ANTI AIR MILITARY DOCU' ; list.append('&name_=' + 'addonString(30713)' + '&&youtube_se='+se)
		se = 'SNIPERS MILITARY DOCU' ; list.append('&name_=' + 'addonString(30719)' + '&&youtube_se='+se)
		se = 'Special Forces / COMMANDOS DOCU' ; list.append('&name_=' + 'addonString(30704)' + '&&youtube_se='+se)
		se = 'SUBMARINE MILITARY DOCU' ; list.append('&name_=' + 'addonString(30706)' + '&&youtube_se='+se)
		se = 'TANK DOCU' ; list.append('&name_=' + 'addonString(30700)' + '&&youtube_se='+se)

		ch = 'IAFmagazine' ; list.append('&name_=' + 'Israeli Air Force' + '&&youtube_ch='+ch)
		ch = 'idfnadesk' ; list.append('&name_=' + 'Israel Defense Forces' + '&&youtube_ch='+ch)
		ch = 'UCkU5SOTkVS6rFcx90XXsLAQ' ; list.append('&name_=' + 'Israeli Navy' + '&&youtube_ch='+ch)
		ch = 'RAFAELsystemLTD' ; list.append('&name_=' + 'Rafael Advanced Defense Systems' + '&&youtube_ch='+ch)
		
	elif num == 108:
		'''Documentaries in Hebrew / דוקומנטרי בעברית'''
		x = '&relevanceLanguage=he&'
		thumb = 'http://in.bgu.ac.il/welcome/EventGalleries/%D7%9C%D7%A9%D7%95%D7%9F%20%D7%A2%D7%91%D7%A8%D7%99%D7%AA.jpg'
		fanart = 'https://i.ytimg.com/vi/JiRWesm6e04/maxresdefault.jpg'
		#se = 'רומא' + x ; list.append('&name_=' + 'METEORS' + '&&youtube_se='+to_utf8(se))
		#se = 'דוקו ישראלי' + x ; list.append('&name_=' + 'addonString(30008)' + '&&youtube_se='+se)
		#se = 'טבע ישראלי' + x ; list.append('&name_=' + 'addonString(30801)' + '&&youtube_se='+se)
		#se = 'היסטוריה ישראלית' + x ; list.append('&name_=' + 'addonString(30804)' + '&&youtube_se='+se)
	
	elif num == 109:
		'''Arts / אומנות'''
		thumb = 'http://crownheights.org/wp-content/uploads/2015/07/art.jpg'
		fanart = 'http://hdwallpapersd.com/wp-content/uploads/2015/08/amazing-street-art-best-3d-graffiti-hd-wallpaper-desktop.jpg'
		se = 'ARTIST DOCU' ; list.append('&name_=' + 'addonString(30851)' + '&&youtube_se='+se)
		se = 'Photographer DOCU' ; list.append('&name_=' + 'addonString(30850)' + '&&youtube_se='+se)
		se = 'PAINTER ARTIST DOCU' ; list.append('&name_=' + 'addonString(30854)' + '&&youtube_se='+se)
		se = 'Sculpture ARTIST DOCU' ; list.append('&name_=' + 'addonString(30855)' + '&&youtube_se='+se)
		
		
	elif num == 110:
		'''Auto / Vehicles / מכוניות'''
		thumb = 'https://1bgnvt3q09toyb96v2ecsygm-wpengine.netdna-ssl.com/wp-content/uploads/2015/11/Local-Motors-3D-printed-car.jpg'
		fanart = 'http://images.car.bauercdn.com/pagefiles/69752/1752x1168/0000_00_0_genevamotorshow.jpg'
		se = '4x4 car DOCO ' ; list.append('&name_=' + '4x4' + '&&youtube_se='+se)
		se = 'Alfa Romeo car DOCO ' ; list.append('&name_=' + 'Alfa Romeo' + '&&youtube_se='+se)
		se = 'Audi car DOCO ' ; list.append('&name_=' + 'Audi' + '&&youtube_se='+se)
		se = 'Auto Vehicles DOCU' ; list.append('&name_=' + 'Auto Vehicles' + '&&youtube_se='+se)
		se = 'BMW car DOCO ' ; list.append('&name_=' + 'BMW' + '&&youtube_se='+se)
		se = 'Bugatti car DOCO ' ; list.append('&name_=' + 'Bugatti' + '&&youtube_se='+se)
		se = 'Cadillac car DOCO ' ; list.append('&name_=' + 'Cadillac' + '&&youtube_se='+se)
		se = 'Ferrari car DOCO ' ; list.append('&name_=' + 'Ferrari' + '&&youtube_se='+se)
		se = 'Ford car DOCO ' ; list.append('&name_=' + 'Ford' + '&&youtube_se='+se)
		se = 'Honda car DOCO ' ; list.append('&name_=' + 'Honda' + '&&youtube_se='+se)
		se = 'Lamborghini car DOCO ' ; list.append('&name_=' + 'Lamborghini' + '&&youtube_se='+se)
		se = 'Mazda car DOCO ' ; list.append('&name_=' + 'Mazda' + '&&youtube_se='+se)
		se = 'Mclaren car DOCO ' ; list.append('&name_=' + 'Mclaren' + '&&youtube_se='+se)
		se = 'Mercedes car DOCO ' ; list.append('&name_=' + 'Mercedes' + '&&youtube_se='+se)
		se = 'Nissan car DOCO ' ; list.append('&name_=' + 'Nissan' + '&&youtube_se='+se)
		se = 'Porsche car DOCO ' ; list.append('&name_=' + 'Porsche' + '&&youtube_se='+se)
		se = 'street racing car DOCO ' ; list.append('&name_=' + 'Street Racing' + '&&youtube_se='+se)
		
	return list, thumb, fanart
	
def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	CATEGORIES_SEARCH(mode=30, url="")
	addDir(addonString(30000).encode('utf-8'),'MyDocu',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0, getAddonFanart()) #My Docu
	list, thumb, fanart = getList(101) ; addDir(addonString(30001).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30001).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(102) ; addDir(addonString(30002).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30002).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(103) ; addDir(addonString(30003).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30003).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(104) ; addDir(addonString(30004).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30004).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(105) ; addDir(addonString(30005).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30005).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(106) ; addDir(addonString(30006).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30006).encode('utf-8')),'1',0, fanart)
	list, thumb, fanart = getList(107) ; addDir(addonString(30007).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30007).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(108) ; addDir(addonString(30008).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30008).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(109) ; addDir(addonString(30009).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30009).encode('utf-8')),'1',0,fanart)
	list, thumb, fanart = getList(110) ; addDir(addonString(30010).encode('utf-8'),list,17,thumb,addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30010).encode('utf-8')),'1',0,fanart)
	
	addon = 'plugin.video.smithsonian'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('smithsonian','plugin://'+addon,8,thumb,plot,addon,58, getAddonFanart(110, custom=""))
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

def CATEGORIES108(name, iconimage, desc, fanart):
	'''בעברית'''
	background = 108
	
	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'דוקו',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES108Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

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
