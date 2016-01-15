# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
"""-----------------------------"""

def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	addDir(addonString(100).encode('utf-8'),'MyMusic',100,featherenceserviceicons_path + 'star.png',addonString(1000).encode('utf-8'),'1',50, getAddonFanart(100)) #My Music
	addDir(addonString(101).encode('utf-8'),'',101,featherenceserviceicons_path + 'sod.png',addonString(1010).encode('utf-8'),'1',50, getAddonFanart(101)) #Israeli Music
	addDir(addonString(111).encode('utf-8'),'',111,featherenceserviceicons_path + 'us.png',addonString(1010).encode('utf-8'),'1',50, getAddonFanart(101)) #Foreign Music
	'''---------------------------'''
	
	'''---------------------------'''
	#addDir(addonString(118).encode('utf-8'),'',118,featherenceserviceicons_path + 'classical.png',addonString(1180).encode('utf-8'),'1',50, getAddonFanart(118)) #Classical Music
	addDir(addonString(119).encode('utf-8'),'',119,featherenceserviceicons_path + 'radio.png',addonString(1190).encode('utf-8'),'1',50, getAddonFanart(119)) #Radio
	
def CATEGORIES100(admin):
	'''------------------------------
	---My-Music----------------------
	------------------------------'''
	background = 100
	
	'''כפתור מוזיקה חדש..'''
	addDir(addonString_servicefeatherence(86).encode('utf-8') % (addonString(100).encode('utf-8')),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(87).encode('utf-8') + addonString_servicefeatherence(88).encode('utf-8') + addonString_servicefeatherence(89).encode('utf-8'),'1',50, getAddonFanart(background))
	
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',50, getAddonFanart("Custom_Playlist1"))
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',50, getAddonFanart("Custom_Playlist2"))
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',50, getAddonFanart("Custom_Playlist3"))
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',50, getAddonFanart("Custom_Playlist4"))
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',50, getAddonFanart("Custom_Playlist5"))
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',50, getAddonFanart("Custom_Playlist6"))
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',50, getAddonFanart("Custom_Playlist7"))
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',50, getAddonFanart("Custom_Playlist8"))
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',50, getAddonFanart("Custom_Playlist9"))
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',50, getAddonFanart("Custom_Playlist10"))
	
	if Custom_10001 == "true": addDir(addonString(10001).encode('utf-8'),'',10001,featherenceserviceicons_path + 'star.png',addonString(100010).encode('utf-8'),'1',50, '') #AMIR ELGAZAR PLAYLISTS

	
def CATEGORIES10001(name, iconimage, desc, fanart):
	if name == None: name = ""
	else: name = name + newline
	'''Easy Listening, Love songs & Bellads'''
	thumb = 'https://d85wutc1n854v.cloudfront.net/live/products/600x375/WB0PGGM81.png?v=1.0'
	fanart = 'http://www.pavellevchenko.com/hard-rock-music-guitar.jpg'
	addDir('Easy Listening, Love songs & Bellads',templates2_path + 'Easy Listening, Love songs & Bellads Personal Collection.txt',2,thumb,name + '','1',50, fanart)
	
	'''The Greatest Hits of All Times'''
	thumb = 'https://d85wutc1n854v.cloudfront.net/live/products/600x375/WB0PGGM81.png?v=1.0'
	fanart = 'http://www.pavellevchenko.com/hard-rock-music-guitar.jpg'
	addDir('The Greatest Hits of All Times',templates2_path + 'The Greatest Hits of All Times.txt',2,thumb,name + 'Personal Collection','1',50, fanart)
	
	'''billboard top 100 All The Time'''
	thumb = 'https://d85wutc1n854v.cloudfront.net/live/products/600x375/WB0PGGM81.png?v=1.0'
	fanart = 'http://www.pavellevchenko.com/hard-rock-music-guitar.jpg'
	addDir('billboard top 100 All The Time',templates2_path + 'billboard top 100 All The Time.txt',2,thumb,name + '','1',50, fanart)
	
	'''Elton John Personal Collection'''
	thumb = 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/GreatestHits19761986EltonJohn.jpg/220px-GreatestHits19761986EltonJohn.jpg'
	fanart = 'http://www.kwiknews.my/sites/default/files/styles/kwik_inner_cover/public/elton.john_.jpg?itok=eUB3cG36'
	addDir('Elton John Personal Collection',templates2_path + 'Elton John Personal Collection.txt',2,thumb,name + 'אלטון גון - אוסף אישי','1',50, fanart)
	
	'''Rain songs in a playlist'''
	thumb = 'http://laughingsquid.com/wp-content/uploads/Rain.jpg'
	fanart = 'http://www.artifacting.com/blog/wp-content/uploads/2012/10/Rain-Room.jpg'
	addDir('Rain songs in a playlist',templates2_path + 'Rain songs in a playlist.txt',2,thumb,name + '','1',50, fanart) 
	
	'''George Michael & wham'''
	thumb = 'http://i234.photobucket.com/albums/ee136/suwarnaadi/hair/GeorgeMichaelshortsideshair.jpg'
	fanart = 'http://www.golden80s.com/wp-content/uploads/2014/05/Wham-head.jpg'
	addDir('George Michael & wham',templates2_path + 'George Michael & wham.txt',2,thumb,name + 'Personal Collection','1',50, fanart)
	
	'''Great French Collection'''
	thumb = 'http://images.travelpod.com/tripwow/photos/ta-00b7-d4d4-11a6/arc-de-triomphe-paris-france+1152_12905284514-tpfil02aw-11867.jpg'
	fanart = 'http://www.wallpapersbyte.com/wp-content/uploads/2015/06/Downolad-HD-Wallpaper-France-Paris-City-Eiffel-Tower-Sunset-WallpapersByte-com-1920x1080.jpg'
	addDir('Great French Collection',templates2_path + 'Great French Collection.txt',2,thumb,name + '','1',50, fanart)
	
	'''Twilight Time'''
	thumb = 'http://cps-static.rovicorp.com/3/JPG_400/MI0003/649/MI0003649662.jpg?partner=allrovi.com'
	fanart = 'http://a2.mzstatic.com/us/r1000/096/purple/v4/cc/8c/0f/cc8c0ff5-6e27-d9fa-62f1-791ffc4c7432/mzl.lcqgfyzc.1024x1024-65.jpg'
	addDir('Twilight Time - Oldies',templates2_path + 'Twilight Time.txt',2,thumb,name + '','1',50, fanart)
	
	'''The Beatles'''
	thumb = 'http://img2-ak.lst.fm/i/u/ar0/6a122bb0665d4d8ca0cc4c31e245ff55'
	fanart = 'http://topwalls.net/wallpapers/2012/02/The-Beatles-1080x1920.jpg'
	addDir('The Beatles',templates2_path + 'The Beatles.txt',2,thumb,name + '','1',50, fanart)
	
	'''love songs vol 1'''
	thumb = 'http://fullhdpictures.com/wp-content/uploads/2015/04/Beauty-Love-Wallpapers.jpg'
	fanart = 'http://www.hd-wallpapersdownload.com/upload/bulk-upload/hd-wallpaper-romantic-love.jpg'
	addDir('love songs vol 1',templates2_path + 'love songs vol 1.txt',2,thumb,name + 'love songs vol 1 - Personal Collection','1',50, fanart)
	
	'''אוסף ישראלי'''
	thumb = 'http://www.artishuk.co.il/UserFiles/Store/Products/Products/230x634453006475603750_M.png'
	fanart = 'http://www.pupic.co.il/UploadedImages/Original/%D7%9E%D7%95%D7%96%D7%99%D7%A7%D7%94%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99%D7%AA.jpg'
	addDir('ישראלי אוסף אישי',templates2_path + 'Israeli Collection.txt',2,thumb,name + addonString(30).encode('utf-8'),'1',50, fanart)
	
	'''ארבע אחר הצהריים'''
	thumb = 'http://th-pro.co.il/SiteImages/SiteImage_c98e320c-2103-4fb8-9c91-b2e8e4aa416a.jpg'
	fanart = 'http://www.women-zone.com/wp-content/uploads/2015/08/israel.jpg' 
	addDir('ארבע אחר הצהריים',templates2_path + 'Four in the afternoon.txt',2,thumb,name + 'מוקדש ל Oren Hagay חברינו לקבוצה Kodisrael.net','1',50, fanart)
	
	'''שלמה ארצי אוסף אישי'''
	thumb = 'http://www.nrg.co.il/images/archive/465x349/1/077/947.jpg'
	fanart = 'http://www.megapixel.co.il/mega/wp-content/uploads/2012/02/Shlomo-Artzi_so.jpg'
	addDir('שלמה ארצי אוסף אישי',templates2_path + 'Shlomo Artzi Personal Collection.txt',2,thumb,name + '','1',50, fanart)
	
	'''פלייליסט מזרחי שקט ורגוע''' 
	thumb = 'http://www.vehiclehi.com/thumbnails/detail/20121101/headphones%20women%20music%20headphones%20girl%201920x1080%20wallpaper_www.vehiclehi.com_28.jpg'
	fanart = 'http://i.ytimg.com/vi/vaQiwOi8Afk/maxresdefault.jpg'
	addDir('פלייליסט מזרחי שקט ורגוע',templates2_path + 'Eastern playlist sedate.txt',2,thumb,name + 'על פי בקשה של חברי הקבוצה (KODISRAEL.NET)','1',50, fanart) 
	
	'''פלייליסט מזרחי קיצבי דאנס'''
	thumb = 'http://www.commentsyard.com/cy/01/9086_original.gif'
	fanart = 'http://3.bp.blogspot.com/-_90x10bD8Xs/VIn8kUH4rwI/AAAAAAAAABo/Yif1L9eLyuE/s1600/music.jpg'
	addDir('פלייליסט מזרחי קיצבי דאנס',templates2_path + 'mizrahi playlist rhythmic dance.txt',2,thumb,name + 'על פי בקשה של חברי הקבוצה (KODISRAEL.NET)','1',50, fanart) 
	
	'''אריק איינשטיין אוסף אישי'''
	thumb = 'http://www.maariv.co.il/download/pictures/%D7%90%D7%A8%D7%99%D7%A7%20%D7%90%D7%99%D7%99%D7%A0%D7%A9%D7%98%D7%99%D7%9F%203%20-%20%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A9%D7%94%20%D7%A9%D7%99%20%D7%A4%D7%9C%D7%90%D7%A9%2090%20480_2.jpg'
	fanart = 'http://www.haaretz.co.il/polopoly_fs/1.2490157.1416401072!/image/2643586370.jpg_gen/derivatives/size_936xAuto/2643586370.jpg'
	addDir('אריק איינשטיין אוסף אישי',templates2_path + 'Arik Einstein.txt',2,thumb,name + '','1',50, fanart)
	
def CATEGORIES101(admin):
	'''Israeli Music'''
	addDir(addonString(101).encode('utf-8'),'',10101,featherenceserviceicons_path + "music.png",addonString(1010).encode('utf-8'),'1',58, getAddonFanart(10101)) #Israeli Music
	addDir(addonString(102).encode('utf-8'),'',10102,featherenceserviceicons_path + "karaoke.png",addonString(1020).encode('utf-8'),'1',58, getAddonFanart(10102)) #Israeli Karaoke
	addDir(addonString(104).encode('utf-8'),'',10104,featherenceserviceicons_path + "guitar.png",addonString(1040).encode('utf-8'),'1',58, getAddonFanart(10104)) #Israeli Liveshows
	
	addDir(addonString(106).encode('utf-8'),'',10106,featherenceserviceicons_path + "music.png",addonString(1060).encode('utf-8'),'1',58, getAddonFanart(10106)) #Mizrahit Music
	addDir(addonString(107).encode('utf-8'),'',10107,featherenceserviceicons_path + "karaoke.png",addonString(1070).encode('utf-8'),'1',58, getAddonFanart(10107)) #Mizrahit Karaoke
	addDir(addonString(109).encode('utf-8'),'',10109,featherenceserviceicons_path + "guitar.png",addonString(1090).encode('utf-8'),'1',58, getAddonFanart(10108)) #Mizrahit Liveshows
	#addDir(addonString(105).encode('utf-8'),'',10105,featherenceserviceicons_path + "microphone.png",addonString(1050).encode('utf-8'),'1',58, getAddonFanart(10105)) #Israeli Djs

def CATEGORIES111(admin):
	'''Foreign Music'''
	addDir(addonString(111).encode('utf-8'),'',11101,featherenceserviceicons_path + "music.png",addonString(1110).encode('utf-8'),'1',58, getAddonFanart(11101)) #Foreign Music
	addDir(addonString(112).encode('utf-8'),'',11102,featherenceserviceicons_path + "karaoke.png",addonString(1120).encode('utf-8'),'1',58, getAddonFanart(11102)) #Foreign Karaoke
	addDir(addonString(114).encode('utf-8'),'',11104,featherenceserviceicons_path + "guitar.png",addonString(1140).encode('utf-8'),'1',58, getAddonFanart(11104)) #Foreign Liveshows
	#addDir(addonString(115).encode('utf-8'),'',11105,featherenceserviceicons_path + "microphone.png",addonString(1150).encode('utf-8'),'1',58, getAddonFanart(11105)) #Foreign Djs

def CATEGORIES10101(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Music-----------------
	------------------------------'''
	background = 101
	commonsearch = 'commonsearch101'
	'''חיפוש'''
	addDir(localize(137),'שיר',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(2).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''קליפים ישראליים אקראי'''
	list = []
	list.append('&youtube_pl=PLjUpwHk7giaiaSeSzZ4Alqj8cGQB6rPEk')
	list.append('&youtube_pl=PLjUpwHk7giaj910tIRA-XTqx6HJA7tPUi') 
	#list.append('&youtube_pl=PL46129841F86EDCCB4')
	list.append('&youtube_pl=FLw_JTl5vBNd_ILZsGOecXmQ')
	list.append('&youtube_pl=PLB97405B96D068FC6')
	list.append('&youtube_pl=PL8B8D8008EC2AEC94')
	list.append('&youtube_pl=PL87E8D450A93CD471')
	list.append('&youtube_pl=PLC5599CB5B12761ED')
	list.append('&youtube_pl=PL8E141F3BEC23F14D')
	list.append('&youtube_pl=PL99BA4ED06D054C29')	
	list.append('&youtube_pl=PLB1AAF2963CBAEF82')
	list.append('&youtube_pl=PLB262A552C2351091')
	list.append('&youtube_pl=PLjf7D2X0WebGDn5SI4OZls5u0iiXdEKPg')
	list.append('&youtube_pl=PLjUpwHk7giaj910tIRA-XTqx6HJA7tPUi') 
	list.append('&youtube_pl=PLWvtqTEJL_PecfYvYdEhXvijvSas9ocp5')
	list.append('&youtube_pl=PLD_zAoRa9UcA4U7jHXTx3hDF3om7zM5jd')
	list.append('&youtube_pl=PLzzwAvFoE3KfG0eR0kCdUjEiEbOIUpvZb')
	list.append('&youtube_pl=PL533AC0BFD30DA202')
	list.append('&youtube_pl=PLFcBFujWU-tB6op3uAj-eJiymuwsUt51T')
	list.append('&youtube_pl=PLFcBFujWU-tDTP_OahLQ6CVvew_TElbHr')
	list.append('&youtube_pl=PLLaB91oVoE-Cq3aJa7MElaf5i3JBILpit')
	list.append('&youtube_pl=PLDMFOZKyoCX0EMCapcK2qW7X3mxjs52Xw')	
	list.append('&youtube_pl=PL1sns8HoY1uKuGp9ze9f5W410VleGhAZ-')
	list.append('&youtube_pl=PL6CcUVzFqqcVNcscz560ZsaxhWrQOrWXH')
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''אביתר בנאי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL6026A7CFC38F5707')
	addDir(addonString(10101).encode('utf-8'),list,17,'http://images.mouse.co.il/storage/7/f/eviatar-ggg.jpg',addonString(101010).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''אברהם טל'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1FSBd3ZP7tlmaOzuqxY1rqG')
	list.append('&youtube_pl=PLk4zDFbgeRTEZtlsrFSpE0yrZsZPpS7p_')
	addDir(addonString(10102).encode('utf-8'),list,17,'http://images.mouse.co.il/storage/a/d/Avraham_Tal_490.jpg',addonString(101020).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	  
	'''אתניקס'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLF755889E22A52FBE')
	list.append('&youtube_pl=PLWkfrFkdyL1H6PXpPbiyjiQ0VgNSGYYoW')
	addDir(addonString(10105).encode('utf-8'),list,17,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פורטיסחרוף'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL0654550EA8A46CDD')
	list.append('&youtube_pl=PLBA8B32965A604B21')
	addDir(addonString(10106).encode('utf-8'),list,17,'http://www.yosmusic.com/images/articles/big/fortis1284-b.jpg',addonString(101060).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
		
	'''גיא ויהל'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL1PXZ56eQG-SGcBGlBXuokGz8O0Iogpzs')
	list.append('&youtube_pl=PL-kn95T5-Cf6ufTD1-IeN06Iz6IHtJtr-')
	list.append('&youtube_pl=PLPL1PXZ56eQG-SGcBGlBXuokGz8O0Iogpzs')
	addDir(addonString(10108).encode('utf-8'),list,17,'http://i.ytimg.com/vi/9fkcGdgj-iI/hqdefault.jpg',addonString(101080).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''דני סנדרסון'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLFA58AD1DB0A251B8')
	list.append('&youtube_pl=PLWs5r3WqRUR0kiPs-hou6gtDbj9qlUBK_')
	addDir(addonString(10111).encode('utf-8'),list,17,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''הראל סקעת'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL1BB87411225FE4D1')
	list.append('&youtube_pl=PLWkfrFkdyL1EPnjO4BYQvKvJ42x4bYd0c')
	addDir(addonString(10113).encode('utf-8'),list,17,'https://i.ytimg.com/i/BbOw6LiHmj6L9o_HlMvKKg/mq1.jpg?v=51c9be2d',addonString(101130).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	
	'''ישראל גוריון והדודאים''' 
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLn28hVQTxgSI1jm2SVdULN64ZK5wORn6m&index=3')
	list.append('&youtube_pl=PL0EB1277ADADAFFAC')
	list.append('&youtube_pl=PLP_Ayo58xDDA96ToPMQtfdMx_rcT3a6Ec')
	addDir(addonString(10148).encode('utf-8'),list,17,'https://i.ytimg.com/vi/vxA1AlH9o-0/hqdefault.jpg',addonString(101480).encode('utf-8'),'1',"", getAddonFanart(background, custom="")) 

	'''כוורת גזוז דודה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLFB7C6CBF00B7FF79')
	list.append('&youtube_pl=PLOu5DKBAMX7Bx5MUnOD-SSPCaybo59XFF')
	list.append('&youtube_pl=PLWkfrFkdyL1H1-Onq0RU2ZwFzrQYh2h7a')
	list.append('&youtube_pl=PLWkfrFkdyL1HzlTe77o1R0RoLTY54rB9n')
	list.append('&youtube_pl=PL5_QhTYCfpJif504ZuJrs7dX-blAGuQ1g')
	addDir(addonString(10115).encode('utf-8'),list,17,'http://3.bp.blogspot.com/-MQNn8bDIkIU/TcN-z5QEkkI/AAAAAAAABCM/xYuRV3ht--I/s1600/%25D7%2593%25D7%2595%25D7%2593%25D7%2594+%25D7%25A6%25D7%2599%25D7%259C%25D7%2595%25D7%259D+%25D7%2590%25D7%2591%25D7%2599+%25D7%2592%25D7%25A0%25D7%2595%25D7%25A8.jpg',addonString(101150).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוש בן ארי ולהקת שבע'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLF3D98239566183BC')
	list.append('&youtube_pl=PLsVqs3jf6nhRbOT_QZpO-Yz2RUYxX8RcF')
	list.append('&youtube_pl=PLF3IvinLSGJgLHeVreYiIqbpwlPpPwCQ8')
	list.append('&youtube_pl=PL245FA03F73653824')
	list.append('&youtube_pl=PL9AE3DACFCF4C7F92')
	list.append('&youtube_pl=PLa_C8kv5anqYTbTX-DIHVa1x8q1iQ_1D2')
	addDir(addonString(10121).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''מזי כהן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLBDIuIv7lLh8rmjkHMsDgGGsr9HWTdGeE')
	addDir(addonString(10120).encode('utf-8'),list,17,'https://i.ytimg.com/vi/3JAAD8Ptq00/maxresdefault.jpg',addonString(101200).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מירי מסיקה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLEFCE4407F6FA1904')
	list.append('&youtube_pl=PL45629848ABCF7094')
	addDir(addonString(10123).encode('utf-8'),list,17,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משינה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL69520B827662EA0D')
	list.append('&youtube_pl=PL84FA93F5887F1751')
	addDir(addonString(10126).encode('utf-8'),list,17,'http://msc.wcdn.co.il/w/w-700/253820-5.jpg',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''נתן גושן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLEgDwaW-dRjrbcf8HWbaOR7E3c-087y5M')
	addDir(addonString(10127).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/2/27/%D7%A0%D7%AA%D7%9F_%D7%92%D7%95%D7%A9%D7%9F.jpg',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	 
	'''עברי לידר'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL4731BCED6938743B')
	addDir(addonString(10130).encode('utf-8'),list,17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עידן רייכל'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL249D7F2BCFAE0105')
	list.append('&youtube_pl=PLxGrSvGsaqfVN9wq8U4UNRWqoFm2tsvCD')
	addDir(addonString(10132).encode('utf-8'),list,17,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
  
	'''קרן פלס'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1EL7x_uQAjucsf5fwcZTr43')
	list.append('&youtube_pl=PLNilsFQExAqJsp71r_BAih7V-Ujfa3SCo')
	addDir(addonString(10138).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ריטה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLf7LrXQb_2uFQ4QVEj4t05pLgW_Fmuopo')
	addDir(addonString(10139).encode('utf-8'),list,17,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''רמי קליינשטיין'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLtH1TqrerKR1oLff98mr-svFZWIq2fjvO&index=3')
	addDir(addonString(10140).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שירי מימון'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLtH1TqrerKR0V6jazm82SHiObpILrObcY')
	addDir(addonString(10141).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sm_album3.jpg/250px-Sm_album3.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלום חנוך'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL017773C5147C4EFB')
	list.append('&youtube_pl=PLC8F10926912E6EBD')
	addDir(addonString(10142).encode('utf-8'),list,17,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''שלמה ארצי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLTojoXqu-e3l-d7nqjHRGjxsF8W77L50f')
	addDir(addonString(10144).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלישית גשר הירקון''' 
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWb1bV-0WydPLmTK9orqNOigyeSGi0KW7')
	addDir(addonString(10149).encode('utf-8'),list,17,'https://www.kedem-auctions.com/sites/default/files/sale/1300/19724.jpg',addonString(101490).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10102(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Karaoke---------------
	------------------------------'''
	background = 102
	commonsearch = 'commonsearch102'
	'''חיפוש'''
	addDir(localize(137),'קריוקי',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (localize(13327)),'1',"", getAddonFanart(background, custom=""))
	
	'''ישראלי קריוקי אקראי'''
	list = []
	list.append('&youtube_ch=sharimkaraokeltd')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PLpx0ojEH2giXH8GUUIcvsBmc5adv_96FW')
	list.append('&youtube_pl=PL6WvGFcuPjESeFQY0YyCzTy7qTofzMlaQ')
	list.append('&youtube_pl=PL7302191F8A43E01C')
	list.append('&youtube_pl=PLgEY_FhZUaoolhDNTkPX40f6cqxIISjp_')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PLjHwF6MA1nycO4TXyQ0Di7ADrg9wTJ8XW')
	list.append('&youtube_pl=PL96E48EDE517CA6D3')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PL9LIAIL0iLiqjA78v9ZYxQELTUsDSvttM')
	list.append('&youtube_pl=PLpUURqa-V9sg8RHi8M-sn3x9Kn6UB9aQs')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''אביתר בנאי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=A87C22Yz2N4')
	list.append('&youtube_id=dd7j6S7s0LM')
	list.append('&youtube_id=uIeS4UJgK2M')
	list.append('&youtube_id=vroIq_IhqzE')
	addDir(addonString(10101).encode('utf-8'),list,17,'http://images.mouse.co.il/storage/7/f/eviatar-ggg.jpg',addonString(101010).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''אברהם טל'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=cu_QUPEsrBc')
	list.append('&youtube_id=rznOQRMUia4_')
	addDir(addonString(10102).encode('utf-8'),list,17,'http://images.mouse.co.il/storage/a/d/Avraham_Tal_490.jpg',addonString(101020).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	  
	'''אתניקס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLz-nEGHyTLyFntxIao6FUopx-XSRfOnb2')
	list.append('&youtube_id=YhzmJbzDk4k')
	addDir(addonString(10105).encode('utf-8'),list,17,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פורטיסחרוף'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=72t4WAmwSaQ')
	addDir(addonString(10106).encode('utf-8'),list,17,'http://www.yosmusic.com/images/articles/big/fortis1284-b.jpg',addonString(101060).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
		
	'''דני סנדרסון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=t7iuwGHzfUA')
	list.append('&youtube_id=RuGEwBvPQSI')
	list.append('&youtube_id=meOrHECoQ2I')
	addDir(addonString(10111).encode('utf-8'),list,17,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''הראל סקעת'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=SMVmC8Y3uQs')
	list.append('&youtube_id=dnLoqwXVozE')
	list.append('&youtube_id=zXq1aKBF4HE')
	list.append('&youtube_id=XmdXDz8ptrs')
	list.append('&youtube_id=BcJTwqezdWc')
	list.append('&youtube_id=wB_B6_5vLUo')
	addDir(addonString(10113).encode('utf-8'),list,17,'https://i.ytimg.com/i/BbOw6LiHmj6L9o_HlMvKKg/mq1.jpg?v=51c9be2d',addonString(101130).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	
	'''ישראל גוריון והדודאים''' 
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=x7IgaPYUpqg')
	list.append('&youtube_id=z9oiKMzsVf8')
	addDir(addonString(10148).encode('utf-8'),list,17,'https://i.ytimg.com/vi/vxA1AlH9o-0/hqdefault.jpg',addonString(101480).encode('utf-8'),'1',"", getAddonFanart(background, custom="")) 

	'''כוורת גזוז דודה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=wtDwhMcaA80')
	list.append('&youtube_pl=WSoDhohI16I')
	list.append('&youtube_id=vYUgUF1Szrs')
	list.append('&youtube_id=fTNne4BQDuk')
	list.append('&youtube_id=NGLQTQHOCXU')
	list.append('&youtube_id=P4Z39LFeDI')
	list.append('&youtube_id=G1ct4loZEEM')
	addDir(addonString(10115).encode('utf-8'),list,17,'http://3.bp.blogspot.com/-MQNn8bDIkIU/TcN-z5QEkkI/AAAAAAAABCM/xYuRV3ht--I/s1600/%25D7%2593%25D7%2595%25D7%2593%25D7%2594+%25D7%25A6%25D7%2599%25D7%259C%25D7%2595%25D7%259D+%25D7%2590%25D7%2591%25D7%2599+%25D7%2592%25D7%25A0%25D7%2595%25D7%25A8.jpg',addonString(101150).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוש בן ארי ולהקת שבע'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLF3D98239566183BC')
	list.append('&youtube_pl=PLsVqs3jf6nhRbOT_QZpO-Yz2RUYxX8RcF')
	list.append('&youtube_pl=PLF3IvinLSGJgLHeVreYiIqbpwlPpPwCQ8')
	list.append('&youtube_pl=PL245FA03F73653824')
	list.append('&youtube_pl=PL9AE3DACFCF4C7F92')
	list.append('&youtube_pl=PLa_C8kv5anqYTbTX-DIHVa1x8q1iQ_1D2')
	addDir(addonString(10121).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''מזי כהן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLBDIuIv7lLh8rmjkHMsDgGGsr9HWTdGeE')
	addDir(addonString(10120).encode('utf-8'),list,17,'https://i.ytimg.com/vi/3JAAD8Ptq00/maxresdefault.jpg',addonString(101200).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מירי מסיקה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEFCE4407F6FA1904')
	list.append('&youtube_pl=PL45629848ABCF7094')
	addDir(addonString(10123).encode('utf-8'),list,17,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משינה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL69520B827662EA0D')
	list.append('&youtube_pl=PL84FA93F5887F1751')
	addDir(addonString(10126).encode('utf-8'),list,17,'http://msc.wcdn.co.il/w/w-700/253820-5.jpg',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''נתן גושן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEgDwaW-dRjrbcf8HWbaOR7E3c-087y5M')
	addDir(addonString(10127).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/2/27/%D7%A0%D7%AA%D7%9F_%D7%92%D7%95%D7%A9%D7%9F.jpg',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	 
	'''עברי לידר'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL4731BCED6938743B')
	addDir(addonString(10130).encode('utf-8'),list,17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עידן רייכל'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL249D7F2BCFAE0105')
	list.append('&youtube_pl=PLxGrSvGsaqfVN9wq8U4UNRWqoFm2tsvCD')
	addDir(addonString(10132).encode('utf-8'),list,17,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
  
	'''קרן פלס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLWkfrFkdyL1EL7x_uQAjucsf5fwcZTr43')
	list.append('&youtube_pl=PLNilsFQExAqJsp71r_BAih7V-Ujfa3SCo')
	addDir(addonString(10138).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ריטה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLf7LrXQb_2uFQ4QVEj4t05pLgW_Fmuopo')
	addDir(addonString(10139).encode('utf-8'),list,17,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''רמי קליינשטיין'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLtH1TqrerKR1oLff98mr-svFZWIq2fjvO&index=3')
	addDir(addonString(10140).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שירי מימון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLtH1TqrerKR0V6jazm82SHiObpILrObcY')
	addDir(addonString(10141).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sm_album3.jpg/250px-Sm_album3.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלום חנוך'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL017773C5147C4EFB')
	list.append('&youtube_pl=PLC8F10926912E6EBD')
	addDir(addonString(10142).encode('utf-8'),list,17,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''שלמה ארצי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLTojoXqu-e3l-d7nqjHRGjxsF8W77L50f')
	addDir(addonString(10144).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלישית גשר הירקון''' 
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLWb1bV-0WydPLmTK9orqNOigyeSGi0KW7')
	addDir(addonString(10149).encode('utf-8'),list,17,'https://www.kedem-auctions.com/sites/default/files/sale/1300/19724.jpg',addonString(101490).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10104(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Liveshows-------------
	------------------------------'''
	background = 104
	commonsearch = 'commonsearch104'
	'''חיפוש'''
	addDir(localize(137),'הופעה חיה',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(1).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''אייל גולן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=9GdWNAXvd0g')
	list.append('&youtube_id=uhDjEYmF-oo')
	list.append('&youtube_id=RqLn1vCQVMo')
	list.append('&youtube_id=fTTsZ1OGZV8')
	list.append('&youtube_id=hqnv8qVOqLY')
	list.append('&youtube_pl=PL2l4T5NjtOsrGnFacKHUc1m7F1Kojuisq')
	addDir(addonString(10103).encode('utf-8'),list,17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''אתניקס'''
	list = []
	list.append('&youtube_se='+commonsearch)
	#list.append('&youtube_pl=PL7M1X2KObyxpFPtF2x33tdJVXKlpOE0wm')
	#list.append('&youtube_id=dzbN8WG33Sg')
	#list.append('&youtube_id=0_n5BLIk6D4')
	#list.append('&youtube_id=sRjlF4Z262w')
	#list.append('&youtube_id=q13ohAH_I-I')
	addDir(addonString(10105).encode('utf-8'),list,17,'http://img.mako.co.il/2013/05/21/etnix_prn_c.jpg',addonString(101050).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פורטיסחרוף'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL01DA343E8BB95D12')
	list.append('&youtube_pl=PLeZqOp-eE-FpvoWCBK-G5Wr1y_VA5Y4ih')
	list.append('&youtube_pl=PLeZqOp-eE-FqJOAKrN7YN6aE8IsKxPqSZ&index=2')
	list.append('&youtube_pl=PL104313B485ECC1DB')
	list.append('&youtube_id=9Oyiis9B6pU')
	list.append('&youtube_id=sVXFm5lOqy8')
	list.append('&youtube_id=ku8mNNCrEys')
	list.append('&youtube_id=P5KW_r2Uu1c')
	addDir(addonString(10106).encode('utf-8'),list,17,'http://img.mako.co.il/2010/10/22/dan_toren_15c.jpg',addonString(101060).encode('utf-8'),'1', 50)
		
	'''דודו אהרון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir(addonString(10107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''דני סנדרסון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10111).encode('utf-8'),['&youtube_pl=PLF867884C8D46A864', 'youtube_id=S2UWI6LooeM', 'youtube_id=eyimcCRqY4w', 'youtube_id=VNGXb8N5mrw', 'youtube_id=jnev_7SipPk', 'youtube_id=MWMvdkWlAis', 'youtube_id=7-UxjnOJkc0', 'youtube_id=goA2RNz1GXo', 'youtube_id=HDXDpyowM-w', 'youtube_id=FVe96EROE6k', 'youtube_id=634o-c7nsM8', 'youtube_id=U3ZonngA4E8', 'youtube_id=wwbYQOGTpYA'],17,'http://images1.calcalist.co.il/PicServer2/20122005/158200/YE0415562_l.jpg',addonString(101110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
			
	'''הפרויקט של רביבו'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10112).encode('utf-8'),['&youtube_pl=PLtQpQHKTXRlM7lPI_5rD4bpyPZRu0IkvB', '&youtube_id=kRzM7QxPk4I', '&youtube_id=GiOtZf7sV9c', '&youtube_id=at4HQssvFCY', '&youtube_id=khp0ONQKcS4', '&youtube_id=UJMB-wfkNqY', '&youtube_id=OqUuH03p1J4', '&youtube_id=iBaaYqMMCtI', '&youtube_id=n8b5YIXCEJ0'],17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''חיים משה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10114).encode('utf-8'),['&youtube_id=tp5jBsO1aKs', '&youtube_id=vxQkLouq2FA', '&youtube_id=v08pmMFcjzQ', '&youtube_id=ysMtHK3DufU', '&youtube_id=tNXkBUJh_0E', '&youtube_id=2GwVBzAp-j4', '&youtube_id=XksMJCIn8Xg', '&youtube_id=5wsETIhNIWo', '&youtube_id=ukik1um6_iU', '&youtube_id=-ICVE31U4lg', '&youtube_id=ccplk-lEIiQ', '&youtube_id=mqMcjRSZAhU', '&youtube_id=ZD5TKctpmS4'],17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''יעקב חתן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10116).encode('utf-8'),'MrBeitarj',9,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ישי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10117).encode('utf-8'),['&youtube_pl=PLv1v9m-FDMVqBylOgmLDDjxQucuVyKW12', '&youtube_pl=PL04D961E06FE727F7'],17,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''כוורת גזוז דודה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=iOPcJZDiumA')
	list.append('&youtube_pl=PLWs5r3WqRUR1ePw0dCrn5pCI5NHUThiTK')
	list.append('&youtube_id=lHRgfC2oifc')
	addDir(addonString(10104).encode('utf-8'),list,17,'http://3.bp.blogspot.com/-MQNn8bDIkIU/TcN-z5QEkkI/AAAAAAAABCM/xYuRV3ht--I/s1600/%25D7%2593%25D7%2595%25D7%2593%25D7%2594+%25D7%25A6%25D7%2599%25D7%259C%25D7%2595%25D7%259D+%25D7%2590%25D7%2591%25D7%2599+%25D7%2592%25D7%25A0%25D7%2595%25D7%25A8.jpg',addonString(101040).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	
	'''ליאור נרקיס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10118).encode('utf-8'),['&youtube_pl=PLAA0970991BC5D286', '&youtube_id=hjpyGlciA74', '&youtube_id=qR5outGV3WE'],17,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוש בן ארי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10121).encode('utf-8'),['&youtube_id=kNv3UW_9WxM', 'youtube_id=YeN12hSYDEQ', 'youtube_id=I0kHj1lz-7w', 'youtube_id=v67d3R96cS8', 'youtube_id=tI2ON_FCu0E', 'youtube_id=6V39QRTjxJA', 'youtube_id=pJaIMPEd6c8', 'youtube_id=VSW9-20xkt4', 'youtube_id=bWJgDQeXZc8', 'youtube_id=RcdlJ0Z5MEw'],17,'http://www.nrg.co.il/images/archive/408x322/692/069.jpg',addonString(101210).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''מושיק עפיה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10122).encode('utf-8'),['&youtube_id=CeeA4BICM4M', '&youtube_id=PTmlzquqb0k', '&youtube_id=uxMPllmgV6c', '&youtube_id=AM2OQvGMqMA', '&youtube_id=PUQZp2_gTyg', '&youtube_id=5aFFOl4-SRY', '&youtube_id=1qalCKhglOE'],17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מירי מסיקה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10123).encode('utf-8'),['&youtube_pl=PLfjHoXmP14hnvOwUzYY8A6YxM-YpZdLiK', '&youtube_id=hxktgo0Df_g', '&youtube_id=R2qT506LRpk', '&youtube_id=rbBvP5Z4lBs', '&youtube_id=rogROHXxFjM', '&youtube_id=lBAp2OWCcu4'],17,'https://i.ytimg.com/i/7cwmZGtlWPDkkEWsxkZd-Q/mq1.jpg?v=54998b82',addonString(101230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
		
	'''מאור אדרי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10124).encode('utf-8'),['&youtube_pl=PLmUWHf2-pPZEsNbXMoJYoA1O-2zGJEtHv', '&youtube_id=w3boSL65UZ4', '&youtube_id=IDVzo-FOE4k', '&youtube_id=3MOyFCkeViU', '&youtube_id=VpcqDALi97w', '&youtube_id=Pc1h1IcO5_o'],17,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משה פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL_8KXLhQVQMKGzYt_5Wvdk7d_ve9Dc-AE')
	list.append('&youtube_id=xptpHXTrrv0')
	list.append('&youtube_id=dhW8XEkyzdU')
	list.append('&youtube_id=SdoFI2eqbQs')
	list.append('&youtube_id=SraFCGtrTtM')
	list.append('&youtube_id=vIyUoiA7R-c')
	list.append('&youtube_id=IUzhr-BkIcA')
	list.append('&youtube_id=mPSNlhZP-BM')
	list.append('&youtube_id=5M0rdjVBO4E')
	addDir(addonString(10125).encode('utf-8'),list,17,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משינה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_id=hxkVbXt8G0')
	list.append('&youtube_id=ySgfjP4L1yY')
	list.append('&youtube_id=vjLpAaPX_FY')
	list.append('&youtube_id=IlUDZvGc-fE')
	addDir(addonString(10126).encode('utf-8'),list,17,'http://msc.wcdn.co.il/w/w-700/253820-5.jpg',addonString(101260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''נתן גושן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10127).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/he/2/27/%D7%A0%D7%AA%D7%9F_%D7%92%D7%95%D7%A9%D7%9F.jpg',addonString(101270).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	 
	'''עברי לידר'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10130).encode('utf-8'),list,17,'http://media.shironet.mako.co.il/media/performers/heb/0/764/profile/764_t275.jpg?rnd=58',addonString(101300).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עידן רייכל'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10132).encode('utf-8'),list,17,'https://yt3.ggpht.com/-vsBWN1RBQuk/AAAAAAAAAAI/AAAAAAAAAAA/SWZEbbG5oUY/s100-c-k-no/photo.jpg',addonString(101320).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עומר אדם'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10133).encode('utf-8'),list,17,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''פאר טסי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10135).encode('utf-8'),list,17,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קובי אפללו'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10136).encode('utf-8'),list,17,'https://yt3.ggpht.com/-W5wjK70SQ1U/AAAAAAAAAAI/AAAAAAAAAAA/Ibov9BPmodU/s100-c-k-no/photo.jpg',addonString(101360).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קובי פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10137).encode('utf-8'),list,17,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קרן פלס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10138).encode('utf-8'),list,17,'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/KerenPelesNew.jpg/375px-KerenPelesNew.jpg',addonString(101380).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ריטה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10139).encode('utf-8'),list,17,'http://img.mako.co.il/2013/02/07/rita_promo_bww_c.jpg',addonString(101390).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''רמי קליינשטיין'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10140).encode('utf-8'),list,17,'http://images1.ynet.co.il/PicServer2/28102008/1770103/2_wh.jpg',addonString(101400).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שירי מימון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10141).encode('utf-8'),list,17,'https://yt3.ggpht.com/-33p31sJqT88/AAAAAAAAAAI/AAAAAAAAAAA/taeHwLul6Io/s100-c-k-no/photo.jpg',addonString(101410).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלום חנוך'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10142).encode('utf-8'),list,17,'https://yt3.ggpht.com/-6DiGw2l8Nrk/AAAAAAAAAAI/AAAAAAAAAAA/3qnrk75SjaA/s100-c-k-no/photo.jpg',addonString(101420).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''שלומי שבת'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10143).encode('utf-8'),list,17,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלמה ארצי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10144).encode('utf-8'),list,17,'http://www.nrg.co.il/images/archive/465x349/1/403/734.jpg',addonString(101440).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שרית חדד'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10145).encode('utf-8'),list,17,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(11450).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10105(name, iconimage, desc, fanart):
	'''------------------------------
	---Israeli-Djs-------------------
	------------------------------'''
	background = 105
	
def CATEGORIES10106(name, iconimage, desc, fanart):
	'''------------------------------
	---Mizrahit-Music----------------
	------------------------------'''
	background = 106
	commonsearch = 'commonsearch106'
	'''חיפוש'''
	addDir(localize(137),'שיר',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(2).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''מיזרחי אקראי'''
	list = []
	list.append('&youtube_pl=PLTc0JNRljDnDGP78_AArd92uOID5cgXQ-')
	list.append('&youtube_pl=PL76tprfc11flz1_awCcqXMU54HAKmU9hQ')
	list.append('&youtube_pl=PL76C25ECA2C0A42D8')
	list.append('&youtube_pl=PLHJ3aAavAyXPvWoAZDAbSjF7_rtxcj_GV')
	list.append('&youtube_pl=PL244F4D7779BDB785')
	list.append('&youtube_pl=PL4Y9oM_hCEX-ufbpFC1PFGNDgW0cs0VjC')
	list.append('&youtube_pl=PL0-1r69ebVlq4lyF3IG2RCDv9K-7Cx4kb')
	list.append('&youtube_pl=PL2ED2F272AAD77564')
	list.append('&youtube_pl=PL6T48PIw2WV0lA-0CGnJkyBN9kHpZrMsN')
	list.append('&youtube_pl=PLcTtnwINjBVetkyrXdlslnaB18-FGrIeB')
	list.append('&youtube_pl=PLwc22f_a0ALr7yxtJfyMBL4UvghuPCyaW')
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	
	'''אייל גולן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL534B67045452C8B6')
	list.append('&youtube_pl=PL2l4T5NjtOsrGnFacKHUc1m7F1Kojuisq')
	list.append('&youtube_pl=PLIgqP62BgBJZEvZpThiNG1WKBv5bVqXcI')
	list.append('&youtube_pl=PLCZzzkQsZVch4XvMQ4epdHVsPVd3hPT5u')
	list.append('&youtube_pl=PLF233F5B848BC0F60')
	list.append('&youtube_pl=PLahQrL3v7AmcylYih7Cr9goUZabCX2X-B')
	addDir(addonString(10103).encode('utf-8'),list,17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''דודו אהרון'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLtNXvU296rEZljDLRMlJ0u1l3IOl7vf0O')
	list.append('&youtube_pl=PLtH1TqrerKR2_z2U7b2Y_m6IKV8D1Ux0p')
	list.append('&youtube_pl=PL30631109E935AB19')
	list.append('&youtube_pl=PL9Wd_4uyU1_6Jhti2HEpo6iUM6P1upNXI')
	list.append('&youtube_pl=PLvf4j8HMmxVoibz7lyv9ozSaklUO442tf')
	list.append('&youtube_pl=PLAD1EAEE365AA736F')
	addDir(addonString(10107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''הפרויקט של רביבו'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLiKPpxNRa3vIZZ4F9OMTeMFKqfJ6GaBal')
	list.append('&youtube_pl=PLiKPpxNRa3vK7rlUimO50nG-kXvyrdxQG')
	addDir(addonString(10112).encode('utf-8'),list,17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''חיים משה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL015121DF81A43072')
	addDir(addonString(10114).encode('utf-8'),list,17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''יעקב חתן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_ch=MrBeitarj')
	addDir(addonString(10116).encode('utf-8'),list,17,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ישי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLTU1sbF1ZeZY4ir25Txd44OPuwrYPKB_s&spfreload=1')
	addDir(addonString(10117).encode('utf-8'),list,17,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''ליאור נרקיס'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL0VvKv2KkveTEz-pUqSdkFrmeQz99EYza')
	addDir(addonString(10118).encode('utf-8'),list,17,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	 	
	'''מושיק עפיה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLtH1TqrerKR062w68GunrKtCIUkjZ8L4H')
	addDir(addonString(10122).encode('utf-8'),list,17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	 
	'''מאור אדרי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLmUWHf2-pPZEsNbXMoJYoA1O-2zGJEtHv')
	addDir(addonString(10124).encode('utf-8'),list,17,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משה פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1EWVjqup2p3wZmQQfBs_pZB')
	list.append('&youtube_pl=PL4ChqhtdbVmIhKD0GZdrThnWroCbrdHNc')
	list.append('&youtube_pl=PLKZQiSVr7xyWlAis9erWVW_C5I07-fpoH')
	addDir(addonString(10125).encode('utf-8'),list,17,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עדן בן זקן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL7xgp7CnQHVV0wx4TumlDId__ao64-Ikp')
	addDir(addonString(10146).encode('utf-8'),list,17,'http://img.mako.co.il/2015/05/28/EDENBENZAKEN_c.jpg',addonString(101460).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מושיק עפיה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLtH1TqrerKR062w68GunrKtCIUkjZ8L4H')
	addDir(addonString(10122).encode('utf-8'),list,17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''עומר אדם'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1G2mEpImYt9H7PCeDpRcFb0')
	addDir(addonString(10133).encode('utf-8'),list,17,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פאר טסי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLnMrQZ_HbXQS8nxlNOV99UxKB64R-Xtr-')
	addDir(addonString(10135).encode('utf-8'),list,17,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קובי פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1G1PHZkatBOWEaxrQtDf0bX&index=60')
	addDir(addonString(10137).encode('utf-8'),list,17,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''שרית חדד'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL3A53E013065CF1EF')
	addDir(addonString(10145).encode('utf-8'),list,17,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(101450).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שני יצהרי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLWkfrFkdyL1FdoAA90Dr2amc3Fgh-bEkE')
	list.append('&youtube_pl=PL015121DF81A43072')
	addDir(addonString(10147).encode('utf-8'),list,17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101470).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10107(name, iconimage, desc, fanart):
	'''------------------------------
	---Mizrahit-Karaoke--------------
	------------------------------'''
	background = 107
	commonsearch = 'commonsearch102'
	'''חיפוש'''
	addDir(localize(137),'קריוקי',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (localize(13327)),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	list.append('&youtube_ch=sharimkaraokeltd')
	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PLjHwF6MA1nycO4TXyQ0Di7ADrg9wTJ8XW')
	list.append('&youtube_pl=PL6WvGFcuPjESeFQY0YyCzTy7qTofzMlaQ')
	list.append('&youtube_pl=PL7302191F8A43E01C')
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''אייל גולן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLfqnCw11fqG3yXYqAOIBV4Fw8PARsJsmK')
	list.append('&youtube_pl=PLz-nEGHyTLyGdbL3DZGL32dSC9G-NPxTo')
	list.append('&youtube_pl=PLMnLzbWQQ8Il3YwCm_NIS-6rlhvtKFr78')             
	addDir(addonString(10103).encode('utf-8'),list,17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''דודו אהרון'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''הפרויקט של רביבו'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10112).encode('utf-8'),list,17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''חיים משה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10114).encode('utf-8'),list,17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''יעקב חתן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10116).encode('utf-8'),list,17,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ישי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10117).encode('utf-8'),list,17,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''ליאור נרקיס'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10118).encode('utf-8'),list,17,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''מושיק עפיה'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10122).encode('utf-8'),list,17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מאור אדרי'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10124).encode('utf-8'),list,17,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משה פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10125).encode('utf-8'),list,17,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''סטלוס ואורן חן'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10129).encode('utf-8'),list,17,'https://yt3.ggpht.com/-2gpbz_o3W7I/AAAAAAAAAAI/AAAAAAAAAAA/PfzwwLycsmo/s100-c-k-no/photo.jpg',addonString(101290).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עומר אדם'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10133).encode('utf-8'),list,17,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פאר טסי'''
	addDir(addonString(10135).encode('utf-8'),list,17,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קובי פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10137).encode('utf-8'),list,17,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלומי שבת'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10143).encode('utf-8'),list,17,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שרית חדד'''
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(10145).encode('utf-8'),list,17,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(11450).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10109(name, iconimage, desc, fanart):
	'''------------------------------
	---Mizrahit-Liveshows------------
	------------------------------'''
	background = 109
	commonsearch = "commonsearch104"
	
	'''חיפוש'''
	addDir(localize(137),'הופעה חיה',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(1).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	#addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''אייל גולן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=81Vh9FriKfc')
	list.append('&youtube_pl=PLB781B8A94339CC67')
	list.append('&youtube_id=RqLn1vCQVMo')
	list.append('&youtube_id=fTTsZ1OGZV8')
	list.append('&youtube_id=hqnv8qVOqLY')
	list.append('&youtube_id=9GdWNAXvd0g')
	list.append('&youtube_id=uhDjEYmF-oo')
	list.append('&youtube_pl=PL2l4T5NjtOsrGnFacKHUc1m7F1Kojuisq')
	list.append('&youtube_id=bI85XpkVTHg')
	addDir(addonString(10103).encode('utf-8'),list,17,'http://www.atzuma.co.il/uploaded/13112175e8e2be3e53e7dc74153479b3a0c726.jpg',addonString(101030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''דודו אהרון'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir(addonString(10107).encode('utf-8'),list,17,'http://www.klr-lior.com/wp-content/gallery/omanim/dudu_aharon-hero_c.jpg',addonString(101070).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''הפרויקט של רביבו'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10112).encode('utf-8'),['&youtube_pl=PLtQpQHKTXRlM7lPI_5rD4bpyPZRu0IkvB', '&youtube_id=kRzM7QxPk4I', '&youtube_id=GiOtZf7sV9c', '&youtube_id=at4HQssvFCY', '&youtube_id=khp0ONQKcS4', '&youtube_id=UJMB-wfkNqY', '&youtube_id=OqUuH03p1J4', '&youtube_id=iBaaYqMMCtI', '&youtube_id=n8b5YIXCEJ0'],17,'http://img.mako.co.il/2012/08/23/revivo_project_purple_c.jpg',addonString(101120).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''חיים משה'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10114).encode('utf-8'),['&youtube_id=tp5jBsO1aKs', '&youtube_id=vxQkLouq2FA', '&youtube_id=v08pmMFcjzQ', '&youtube_id=ysMtHK3DufU', '&youtube_id=tNXkBUJh_0E', '&youtube_id=2GwVBzAp-j4', '&youtube_id=XksMJCIn8Xg', '&youtube_id=5wsETIhNIWo', '&youtube_id=ukik1um6_iU', '&youtube_id=-ICVE31U4lg', '&youtube_id=ccplk-lEIiQ', '&youtube_id=mqMcjRSZAhU', '&youtube_id=ZD5TKctpmS4'],17,'http://images.one.co.il/images/mag/450_250/gg789176.jpg',addonString(101140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''יעקב חתן'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10116).encode('utf-8'),'MrBeitarj',9,'https://yt3.ggpht.com/-_rt6N50COLw/AAAAAAAAAAI/AAAAAAAAAAA/F_g5RBGIXfo/s100-c-k-no/photo.jpg',addonString(101160).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''ישי לוי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10117).encode('utf-8'),['&youtube_pl=PLv1v9m-FDMVqBylOgmLDDjxQucuVyKW12', '&youtube_pl=PL04D961E06FE727F7'],17,'http://harif.co.il/wp-content/uploads/2010/07/%D7%99%D7%A9%D7%99-%D7%9C%D7%95%D7%99-%D7%9E%D7%A8%D7%92%D7%A9-%D7%91%D7%A6%D7%99%D7%9C%D7%95%D7%9E%D7%99-%D7%94%D7%A7%D7%9C%D7%99%D7%A4-%D7%AA%D7%95%D7%93%D7%94.jpg',addonString(101170).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''ליאור נרקיס'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10118).encode('utf-8'),['&youtube_pl=PLAA0970991BC5D286', '&youtube_id=hjpyGlciA74', '&youtube_id=qR5outGV3WE'],17,'http://bsn.co.il/sites/default/files/styles/home_page_main_story_image_480x269/public/%D7%9C%D7%99%D7%90%D7%95%D7%A8%20%D7%A0%D7%A8%D7%A7%D7%99%D7%A1.jpg?itok=nVnP8pg-',addonString(101180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מושיק עפיה'''
	addDir(addonString(10122).encode('utf-8'),['&youtube_id=CeeA4BICM4M', '&youtube_id=PTmlzquqb0k', '&youtube_id=uxMPllmgV6c', '&youtube_id=AM2OQvGMqMA', '&youtube_id=PUQZp2_gTyg', '&youtube_id=5aFFOl4-SRY', '&youtube_id=1qalCKhglOE'],17,'https://yt3.ggpht.com/-4IayEL0C0Rs/AAAAAAAAAAI/AAAAAAAAAAA/kEV66on9DOM/s100-c-k-no/photo.jpg',addonString(101220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מאור אדרי'''
	addDir(addonString(10124).encode('utf-8'),['&youtube_pl=PLmUWHf2-pPZEsNbXMoJYoA1O-2zGJEtHv', '&youtube_id=w3boSL65UZ4', '&youtube_id=IDVzo-FOE4k', '&youtube_id=3MOyFCkeViU', '&youtube_id=VpcqDALi97w', '&youtube_id=Pc1h1IcO5_o'],17,'http://img.mako.co.il/2012/09/12/maor_edri_suit_c.jpg',addonString(101240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''משה פרץ'''
	list = []
	list.append('&youtube_pl=PL_8KXLhQVQMKGzYt_5Wvdk7d_ve9Dc-AE')
	list.append('&youtube_id=xptpHXTrrv0')
	list.append('&youtube_id=dhW8XEkyzdU')
	list.append('&youtube_id=SdoFI2eqbQs')
	list.append('&youtube_id=SraFCGtrTtM')
	list.append('&youtube_id=vIyUoiA7R-c')
	list.append('&youtube_id=IUzhr-BkIcA')
	list.append('&youtube_id=mPSNlhZP-BM')
	list.append('&youtube_id=5M0rdjVBO4E')
	addDir(addonString(10125).encode('utf-8'),list,17,'https://i.ytimg.com/i/0ebT4a-IyuY61X8py3nzsg/mq1.jpg?v=52124db3',addonString(101250).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''עומר אדם'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10133).encode('utf-8'),list,17,'https://i.ytimg.com/i/o4y7A6EF2tZ1Q2Oxx64HNQ/mq1.jpg?v=520b5fde',addonString(101330).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''פאר טסי'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	#addDir(addonString(10135).encode('utf-8'),list,17,'https://yt3.ggpht.com/-XdArdL_W374/AAAAAAAAAAI/AAAAAAAAAAA/phGLZNk8iwU/s100-c-k-no/photo.jpg',addonString(101350).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''קובי פרץ'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10137).encode('utf-8'),list,17,'https://i.ytimg.com/i/GYqX6zfso91VDawbH_Nukw/mq1.jpg?v=4f5f486f',addonString(101370).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שלומי שבת'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10143).encode('utf-8'),list,17,'https://i.ytimg.com/i/GaHPMv8YIv_0HfRDQQ44cA/mq1.jpg?v=af5444',addonString(101430).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''שרית חדד'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(10145).encode('utf-8'),list,17,'https://i.ytimg.com/i/0m-czKbg-tL7J61RDdU1rg/mq1.jpg?v=54ac3da1',addonString(11450).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11101(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Music-----------------
	------------------------------'''
	background = 111
	commonsearch = 'commonsearch111'
	'''חיפוש'''
	addDir(localize(137),'song',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(2).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''להיטים לועזיים מכל הזמנים'''
	list = []
	list.append('&youtube_pl=PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk')
	list.append('&youtube_pl=PLsiyfJZak8Pc7AA6EqEIXBgU4u-qypRLe')
	list.append('&youtube_pl=PLuK6flVU_Aj5EJ9Pp-C9N7XA0YJr_GrJI')
	list.append('&youtube_pl=PLqYXv_L7NiEyYnfZhVHR7ixOTANxjes89')
	list.append('&youtube_pl=PL6D06B33066D077FF')
	list.append('&youtube_pl=PL2E373ABBD360C09F')
	list.append('&youtube_pl=PLP6Mnyo0OTQtnZtDpxceawHIFW5dx38y8')
	list.append('&youtube_pl=PL422A945E3D37BF49')
	list.append('&youtube_pl=PL230B1AFAC3F149D0')
	list.append('&youtube_pl=PLQw-AwSCH8G3Dhw4vAu0R7OfxDWdUbhaR')
	list.append('&youtube_pl=PL7BA598CBAF2745D9')
	list.append('&youtube_pl=PL05E1623111A9A860')
	list.append('&youtube_pl=PLpuDUpB0osJmZQ0a3n6imXirSu0QAZIqF')
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	
	'''Adele'''
	list = []
	list.append('&youtube_pl=PL2jZGLrfnPrwKpGWByChK2ujJsh8XGT1u')
	list.append('&youtube_pl=PL9319650950E41B78')
	list.append('&youtube_pl=PL1C76D5F2FB130533')             
	list.append('&youtube_pl=PLEEyQEShYtdXMVAiHjpbSAIXRmuaxkiac') 
	addDir(addonString(11127).encode('utf-8'),list,17,'http://cdn.cultofmac.com/wp-content/uploads/2015/11/adele-third-album-25.jpg',addonString(111270).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=-aVCoKV6XpVJ8U1wNNOkbo6BzgCdf83m')
	addDir(addonString(11126).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(111260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=arPDo5YMm5RA7XMeJtn5HFDdXPed4A-X')
	addDir(addonString(11102).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(111020).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLF76A601FD261FE55') 
	addDir(addonString(11122).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(111220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL7B7E250ABE8B4E64&index=2&spfreload=1')
	addDir(addonString(11123).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(111230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL595EC905D80443EB')
	addDir(addonString(11150).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(111500).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLD88DB02A8CA3EBC2')
	addDir(addonString(11129).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(111290).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL4FA0D24F56BD0191')
	addDir(addonString(11151).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(111510).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Elton John'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLA910D381CD5AF74E')
	addDir(addonString(11152).encode('utf-8'),list,17,"http://i.huffpost.com/gen/2722330/images/o-ELTON-JOHN-facebook.jpg",addonString(111520).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLVsyHu2yDLkzdYcDjz8yqw84CmcYZGCIt')
	addDir(addonString(11120).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(111200).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLnTKYzbTaPq4yjmTe5CwzpRUvHlJspIO7')
	addDir(addonString(11124).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(111240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLC9944199588E8EE8')
	addDir(addonString(11118).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(111180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Jean Michel Jarre'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL0X6k9ILt02rs8SYwNfNxgGHTDzTA-eWI')
	addDir(addonString(11131).encode('utf-8'),list,17,"http://www.whale.to/c/zs107kz4jarre.jpg",addonString(111310).encode('utf-8'),'1',"electronic music", getAddonFanart(background, custom=""))
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(11101).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(111010).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	addDir(addonString(11111).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(111110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLEB34410B67CCA932')
	addDir(addonString(11113).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(111130).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PLvPrczMM8gz3y1Iboy6CsZ432HjCWUQgR&index=15')
	addDir(addonString(11110).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(111100).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL2DC5A0B189256D7D&index=4')
	addDir(addonString(11103).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(111030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_ch=TaylorSwiftVEVO')
	addDir(addonString(11104).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(111040).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_ch=UsherVEVO')
	addDir(addonString(11115).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(111150).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Whitney Houston'''
	list = []
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(11114).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(111140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11102(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Karaoke---------------
	------------------------------'''
	background = 112
	commonsearch = 'commonsearch112'
	
	'''חיפוש'''
	addDir(localize(137),'karaoke',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (localize(13327)),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	#addDir(localize(590),'UC-9-kyTW8ZkZNDHQJ6FgpwQ',9,featherenceserviceicons_path + "singers.png","",'1',"", getAddonFanart(background, custom=""))
		
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11126).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(111260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11102).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(111020).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11122).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(111220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11123).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(111230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11150).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(111500).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11129).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(111290).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11151).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(111510).encode('utf-8'),'1',"", getAddonFanart(background, custom="https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg"))
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11120).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(111200).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11124).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(111240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11118).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(111180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Justin Bieber'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11130).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(111300).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(11101).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(111010).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	addDir(addonString(11111).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(111110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEB34410B67CCA932')
	addDir(addonString(11113).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(111130).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11110).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(111100).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11103).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(111030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Sam Smith'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11133).encode('utf-8'),list,17,"https://yt3.ggpht.com/-9z_bFRPDMYQ/AAAAAAAAAAI/AAAAAAAAAAA/czjhAF4k4aw/s100-c-k-no/photo.jpg",addonString(111330).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11104).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(111040).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11115).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(111150).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Whitney Houston'''
	list = []
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(11114).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(111140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11104(name, iconimage, desc, fanart):
	'''------------------------------
	---Foreign-Liveshows-------------
	------------------------------'''
	background = 114
	commonsearch = 'commonsearch114'
	'''חיפוש'''
	addDir(localize(137),'liveshow',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(23).encode('utf-8') % (addonString(1).encode('utf-8')),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי הופעות חיות לועזי'''
	list = []
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))
	
	'''Aretha Franklin'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=a3raW4rt2fE')
	list.append('&youtube_id=y0xZsepl4Is')
	list.append('&youtube_id=CbmB2nXJRDM')
	addDir(addonString(11126).encode('utf-8'),list,17,"http://sandiegofreepress.org/wp-content/uploads/2013/01/ARETHA-FRANKLIN-QUEEN-OF-SOUL.jpg",addonString(111260).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Beyonce'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11102).encode('utf-8'),list,17,"http://factmag-images.s3.amazonaws.com/wp-content/uploads/2013/05/beyonce-5.13.20132.jpg",addonString(111020).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Marley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11122).encode('utf-8'),list,17,"http://imgc.allpostersimages.com/images/P-473-488-90/65/6544/ATK4100Z/posters/bob-marley-colors.jpg/300px-Bob-Marley-in-Concert_Zurich_05-30-80.jpg",addonString(111220).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Bob Dylan'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11123).encode('utf-8'),list,17,"http://www.rockbandaide.com/wp-content/uploads/2014/02/Bob-Dylan-Times-are-Changing-C10113356.jpg",addonString(111230).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''Britney Spears'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11150).encode('utf-8'),list,17,"http://guardianlv.com/wp-content/uploads/2013/12/Britney-Spears-Hits-Vegas-With-Piece-of-Me-Concert-Series-e1388228163153.jpg",addonString(111500).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Coldplay'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=vMAyzVr_fZI')
	addDir(addonString(11129).encode('utf-8'),list,17,"http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2011/10/12/1318414177419/Coldplay-007.jpg",addonString(111290).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''David Bowie'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11151).encode('utf-8'),list,17,"https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg",addonString(111510).encode('utf-8'),'1',"", getAddonFanart(background, custom="https://wallpaperscraft.com/image/david_bowie_face_fist_sweater_look_3332_1920x1080.jpg"))
	
	'''Elton John'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_id=9_5UFmJ7YhM')
	list.append('&youtube_id=9_3WKNlZg-qr8')
	addDir(addonString(11152).encode('utf-8'),list,17,"http://i.huffpost.com/gen/2722330/images/o-ELTON-JOHN-facebook.jpg",addonString(111520).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Elvis Presley'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11120).encode('utf-8'),list,17,"http://static.europosters.cz/image/750/plakatok/elvis-presley-portrait-i9038.jpg/375px-Elvis_Presley_promoting_Jailhouse_Rock.jpg",addonString(111200).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''Eric Clapton'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11124).encode('utf-8'),list,17,"http://rock.amazingradios.com/wp-content/uploads/2014/10/eric-clapton-9.jpg",addonString(111240).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Jennifer Lopez'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11118).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Jennifer_Lopez_GLAAD_2014.jpg/375px-Jennifer_Lopez_GLAAD_2014.jpg",addonString(111180).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Justin Bieber'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11130).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Believe_Tour_7%2C_2012.jpg/375px-Believe_Tour_7%2C_2012.jpg",addonString(111300).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Michael Jackson'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL3CF35F99B7B4A227')
	addDir(addonString(11101).encode('utf-8'),list,17,"https://michaeljacksonisrael.files.wordpress.com/2013/05/69235_majkl-dzhekson_or_michael-jack21.jpg",addonString(111010).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Maddona'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLOOBElWP-gj6hl7PQVcZak9FGri0ppeWG')
	addDir(addonString(11111).encode('utf-8'),list,17,"http://g04.a.alicdn.com/kf/HTB1jqmjIVXXXXbSapXXq6xXFXXX4/%D7%AA%D7%90%D7%A8%D7%99%D7%9A-%D7%94%D7%9E%D7%A1%D7%AA%D7%95%D7%A8%D7%99%D7%9F-%D7%A9%D7%97%D7%A7%D7%A0%D7%99%D7%AA-%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2-%D7%9E%D7%93%D7%95%D7%A0%D7%94-ciccone-%D7%A4%D7%95%D7%A1%D7%98%D7%A8-%D7%A6%D7%99%D7%95%D7%A8-%D7%93%D7%A7%D7%95%D7%A8%D7%98%D7%99%D7%91%D7%99-%D7%9C%D7%91%D7%99%D7%AA-%D7%91%D7%93-%D7%9E%D7%A9%D7%99-%D7%94%D7%93%D7%A4%D7%A1%D7%94.jpg",addonString(111110).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Mariah Carey'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PLEB34410B67CCA932')
	addDir(addonString(11113).encode('utf-8'),list,17,"http://www.studentsoftheworld.info/sites/musique/img/2827_Maria_Carey_1.jpg",addonString(111130).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Roy Orbison'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11110).encode('utf-8'),list,17,"http://www.billboard.com/files/styles/promo_650/public/stylus/1077939-roy-orbison-617-409.jpg",addonString(111100).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Rihanna'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11103).encode('utf-8'),list,17,"http://static1.1.sqspcdn.com/static/f/610086/15180915/1321583897117/Rihanna.jpg?token=kZt1lYEul%2FfTahdORTKehFd28NI%3D/site1/20091127/0023ae9885da0c7990e10d.jpg&pw=200",addonString(111030).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Taylor Swift'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11104).encode('utf-8'),list,17,"http://upload.wikimedia.org/wikipedia/he/5/58/Taylor_Swift_-_Taylor_Swift_Album_Cover.png",addonString(111040).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''Usher'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	addDir(addonString(11115).encode('utf-8'),list,17,"http://www.usherdaily.com/wp-content/uploads/2015/02/usher-2014-cover-bb36-01-650.jpg",addonString(111150).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

	'''Whitney Houston'''
	list = []
	list.append('&youtube_se='+commonsearch+'')
	list.append('&youtube_pl=PL201BB89398FE5675')
	addDir(addonString(11114).encode('utf-8'),list,17,"http://img2.timeinc.net/people/i/2012/specials/yearend/obits/whitney-houston-1435.jpg",addonString(111140).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
		
def CATEGORIES11105(name, iconimage, desc, fanart):
	'''------------------------------
	---Foregin-Djs-------------------
	------------------------------'''
	background = 115

	'''אקראי Djs'''
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))

	
def CATEGORIES119(admin):
	'''------------------------------
	---Radio-------------------------
	------------------------------'''
	background = 119
	addon = 'plugin.audio.jango'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Jango','plugin://'+addon,8,thumb,plot,addon,"", getAddonFanart(background, custom=fanart))
	
	addon = 'plugin.audio.99fm-playlists'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('99 FM','plugin://'+addon,8,thumb,plot,addon,"", getAddonFanart(background, custom=fanart))
	
	
def CATEGORIES121(admin):
	'''------------------------------
	---Classical-Music---------------
	------------------------------'''
	
	'''אקראי מוזיקה קלאסית'''
	addDir(localize(590),list,17,'http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33',addonString(590).encode('utf-8'),'1',"http://reallifeglobal.com/wp-content/uploads/2012/06/music.jpg?467a33", getAddonFanart(background, custom=""))

	
	background = 121
	'''מוזיקה קלאסית 1'''
	addDir(addonString(121).encode('utf-8') + space + "1",'ClassicalMusicOnly',9,'https://yt3.ggpht.com/-ECuTE_OO3EU/AAAAAAAAAAI/AAAAAAAAAAA/2j-Kiyky9JU/s100-c-k-no/photo.jpg',addonString(2050).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוזיקה קלאסית 2'''
	addDir(addonString(121).encode('utf-8') + space + "2",'TopClassicalMusic',9,'https://yt3.ggpht.com/-RcrsdLR_BvI/AAAAAAAAAAI/AAAAAAAAAAA/2kIbfIgVXi4/s100-c-k-no/photo.jpg',addonString(2051).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוזיקה קלאסית 3'''
	addDir(addonString(121).encode('utf-8') + space + "3",'ClassicalMusicOn',9,'https://yt3.ggpht.com/-LuYmD_n6gFo/AAAAAAAAAAI/AAAAAAAAAAA/nNUB6_ECXJc/s100-c-k-no/photo.jpg',addonString(2052).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))
	
	'''מוזיקה קלאסית 4'''
	addDir(addonString(121).encode('utf-8') + space + "4",'PLcGkkXtask_fpbK9YXSzlJC4f0nGms1mI',13,'https://yt3.ggpht.com/-LFti8mQBHdE/AAAAAAAAAAI/AAAAAAAAAAA/F8sYy19ISBc/s88-c-k-no/photo.jpg',addonString(2053).encode('utf-8'),'1',"", getAddonFanart(background, custom=""))

