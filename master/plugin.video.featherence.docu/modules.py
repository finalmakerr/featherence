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
	addDir(addonString(100).encode('utf-8'),'MyDocu',100,"http://www.2gzr.com/uploads/2014/07/documentary-2.jpg",addonString(1000).encode('utf-8'),'1',50, getAddonFanart(100, custom="")) #My Docu
	addDir(addonString(101).encode('utf-8'),'',101,'https://i.ytimg.com/vi/q4AQDDKglEE/maxresdefault.jpg',addonString(1010).encode('utf-8'),'1',50, getAddonFanart(101, custom="")) #Nature
	addDir(addonString(102).encode('utf-8'),'',102,'http://www.esa.int/var/esa/storage/images/esa_multimedia/images/2014/02/searching_for_exoplanetary_systems/14282306-1-eng-GB/Searching_for_exoplanetary_systems.jpg',addonString(1020).encode('utf-8'),'1',50, getAddonFanart(102, custom="")) #Space
	addDir(addonString(103).encode('utf-8'),'',103,'http://wsap.academy/wp-content/uploads/2015/03/1123676.jpg',addonString(1030).encode('utf-8'),'1',50, getAddonFanart(103, custom="")) #History
	addDir(addonString(104).encode('utf-8'),'',104,'http://orig07.deviantart.net/ff1a/f/2009/033/1/3/science_wallpaper_by_hamdanzinha.jpg',addonString(1040).encode('utf-8'),'1',50, getAddonFanart(104, custom="")) #Science
	addDir(addonString(107).encode('utf-8'),'',107,'http://www.muralswallpaper.co.uk/sites/default/files/styles/full_lightbox/public/product_images/Cute-Animals-Kids-Wallpaper-Mural.jpg?itok=F5n249_x',addonString(1070).encode('utf-8'),'1',50, getAddonFanart(107, custom="")) #Kids
	addDir(addonString(108).encode('utf-8'),'',108,'http://in.bgu.ac.il/welcome/EventGalleries/%D7%9C%D7%A9%D7%95%D7%9F%20%D7%A2%D7%91%D7%A8%D7%99%D7%AA.jpg',addonString(1080).encode('utf-8'),'1',50, getAddonFanart(108, custom="")) #Hebrew Subtitle
	addDir(addonString(109).encode('utf-8'),'',109,'http://www.globallistings.info/repository/image/6/445.jpg',addonString(1090).encode('utf-8'),'1',50, getAddonFanart(109, custom="")) #TV channels
	addDir(addonString(110).encode('utf-8'),'',110,'http://crownheights.org/wp-content/uploads/2015/07/art.jpg',addonString(1100).encode('utf-8'),'1',50, getAddonFanart(110, custom="")) #Art
	addDir(addonString(111).encode('utf-8'),'',111,'https://i.ytimg.com/vi/ZnBg4MCg7Mg/maxresdefault.jpg',addonString(1110).encode('utf-8'),'1',50, getAddonFanart(111, custom="")) #National Geographic
	addDir(addonString(112).encode('utf-8'),'',112,'http://vignette1.wikia.nocookie.net/logopedia/images/3/34/Discovery_Channel_2000.png/revision/latest?cb=20100728112637',addonString(1120).encode('utf-8'),'1',50, getAddonFanart(112, custom="")) #Discovery
	addDir(addonString(113).encode('utf-8'),'',113,'http://media.shawmedia.ca/uploadedimages/shawmedia/content/brands/header_natgeowild.jpg?n=4234',addonString(1130).encode('utf-8'),'1',50, getAddonFanart(113, custom="")) #Nat Geo Wild
	addDir(addonString(114).encode('utf-8'),'',114,'https://upload.wikimedia.org/wikipedia/en/3/3a/Animal_Planet_Canada_Logo.PNG',addonString(1140).encode('utf-8'),'1',50, getAddonFanart(114, custom="")) #Animal Planet
	addon = 'plugin.video.smithsonian'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Smithsonian HD 1080','plugin://'+addon,8,thumb,plot,addon,58, getAddonFanart(110, custom=""))
	'''---------------------------'''
	

def CATEGORIES100(admin):
	'''------------------------------
	---My-Docu-----------------------
	------------------------------'''
	fanart = 100
	
	'''כפתור דוקו חדש..'''
	addDir(addonString_servicefeatherence(86).encode('utf-8') % (addonString(100).encode('utf-8')),"New",20,'https://cdn3.iconfinder.com/data/icons/logistics-delivery-set-1/512/8-512.png',addonString_servicefeatherence(87).encode('utf-8') + addonString_servicefeatherence(88).encode('utf-8') + addonString_servicefeatherence(89).encode('utf-8'),'1',50, getAddonFanart(fanart))
	
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
	
def CATEGORIES101(admin):
	'''------------------------------
	---Nature------------------------
	------------------------------'''
	background = 101
	name = addonString(101).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Nature Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	list.append('&youtube_pl=PLNxd9fYeqXeba2Nz4ocWac4hyhJnEACFw')
	list.append('&youtube_pl=PLNxd9fYeqXeYQpcE7LfadSFjUU4E6inZC')
	list.append('&youtube_pl=PL_jFbqOSEqaLIYGS0Oz8jTlrB8PaHiwdp')
	list.append('&youtube_pl=PL66rc6rMkuadKawGwt9pYSq_yVJ1dnsyp')
	list.append('&youtube_pl=PLpHQQspuhgG7qhHOD1HrWklZg458-LQYj')
	list.append('&youtube_pl=PL7GQU9nivpYJpnzAhTH1OB3N6BeQipls_')
	list.append('&youtube_pl=PLd2jr44gFMvBMxFlT0tFxeJqrAYGmpjO1')
	list.append('&youtube_pl=PLsa65XLFLA2-mxUpttawU8AN1TX0VwKpH')
	list.append('&youtube_pl=PLcOr-eBi9or-I7knKXhhdihMqswzWJ7yo')
	list.append('&youtube_pl=PL3Ea6NwLKoMSArPBNWh-gMgKCX2cmJzCq')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))

	'''Nature Ultra HD'''
	list = []
	list.append('&youtube_pl=PL_VFlQR7BSNQTvSG8Ua6rFtS-tyxVenA2')
	list.append('&youtube_pl=PL_T9MO520krq5QsT1sIHdmBUNodksi8v2')
	list.append('&youtube_pl=PLdhB2hC90YEsbPuupoVTms5PYM1iDCdDw')
	list.append('&youtube_pl=PLe9OS0jiMKcK9Nr3msXChWTxFneaNAUAE')
	list.append('&youtube_pl=PLdhB2hC90YEsLDfMVMyYCzfPm6adWdSE_')
	list.append('&youtube_pl=PLdZiffjjeKRAQD9WOL8M3fDQUnfPEC2rp')
	list.append('&youtube_pl=PLTk0fHKIvaBb8GwPtHJ5CgW5m6IyF4UDv')
	list.append('&youtube_pl=PLViQOmmwfTG-A03mKp-cehLvW9uii8xL3')
	addDir("Nature Ultra HD",list,17,'http://www.lyfaces.com/wallpaper/download/download-wallpaper-3840x2160-water-lilies-leaves-pond-4k-ultra-hd-nature-wallpaper-.jpg','','1',"", getAddonFanart(background, custom=""))	
 

	'''youtube nature channels'''
	list = []
	list.append('&youtube_ch=BBCEarth')
	list.append('&youtube_ch=AnimalPlanetTV')
	list.append('&youtube_ch=UC1BOeEP9-jiSmvME99fneQA')
	addDir("youtube nature channel's",list,17,'http://www.planwallpaper.com/static/images/121.jpg','','1',"", getAddonFanart(background, custom=""))
 
 
 
	'''בעלי חיים'''
	addDir(addonString(10101),'',10101,'http://3.bp.blogspot.com/-GmdLk2R6ahA/T55Ud9aXCcI/AAAAAAAABY4/4Z9aMnM0Ukc/s1600/Blue-Butterfuly-Latest-Animal-Wallpaper-2012.jpg',addonString(101010),'1',"", getAddonFanart(10101))
	
	'''צומח'''
	addDir(addonString(10102),'',10102,'https://lh5.ggpht.com/rJg02fFypSfx2mL6BMWEN__3Je-E-sy2ZDgZs2PNnnFLawi2b1QtL9S_GtY5sPLXPw=h900',addonString(101020),'1',"", getAddonFanart(10102))
	

	'''מקומות'''
	addDir(addonString(10103),'',10103,'https://s-media-cache-ak0.pinimg.com/originals/f6/7c/e8/f67ce86161d17cbde49bac13be0ea023.jpg',addonString(101030),'1',"", getAddonFanart(10103))

	
 

def CATEGORIES10101(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-ANIMALS----------------
	------------------------------'''
	background = 10101
	

	'''Animal's'''
	list = []
	list.append('&youtube_ch=UCFYJCBaHRzLJrnhRglM3GdA')
	addDir("Animal's",list,17,'http://hdwallpaper.camera/download/2461/2015/03/black_panther_animals_wallpaper_1920x1080-800x600.jpg/','','1',"", getAddonFanart(background, custom=""))

	'''Lions'''
	list = []
	list.append('&youtube_se=#lions')
	list.append('&youtube_pl=PLpYgp0wW8mmZyLCqY415YbjefiazLBHzJ')
	list.append('&youtube_pl=PL3Ea6NwLKoMSArPBNWh-gMgKCX2cmJzCq')
	addDir('Lions',list,17,'http://3.bp.blogspot.com/-Iff7IaN3DKI/UeUqIwYg3ZI/AAAAAAAAAZ4/1qJiCmolK7M/s1600/lion-photo.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Giraffe'''
	list = []
	list.append('&youtube_ch=UCDJLpRSvaPy8vWn8hZVguSg') 
	addDir('Giraffe',list,17,'http://ww2.valdosta.edu/~sybashlor/giraffe.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Elephant'''
	list = []
	list.append('&youtube_ch=UCXhjuyNdDSbe5L0yiFoCoxQ') 
	addDir('Elephant',list,17,'http://www.turtlehurtled.com/wp-content/uploads/2013/06/Elephant.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Tiger'''
	list = []
	list.append('&youtube_ch=UCEYScfGuWVU9gxdrqf0XArQ') 
	addDir('Tiger',list,17,'http://www.the-south-asian.com/april2001/bengal_tiger.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Monkey'''
	list = []
	list.append('&youtube_ch=channel/UC265iYDGY4YHbEqLPrhvJKQ') 
	addDir('Monkey',list,17,'http://www.happytrailsindonesia.com/uploads/img/8/Monkey%20Indonesia.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Cats'''
	list = []
	list.append('&youtube_ch=UC9egiwuJsQZ0Cy2to5fvSIQ') 
	addDir('Cats',list,17,'https://www.colourbox.com/preview/3100637-grey-scottish-cat-on-the-white-background.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Birds'''
	list = []
	list.append('&youtube_ch=UC7uJ7jdwfPcmqKu7V2nI9rA') 
	list.append('&youtube_pl=PLvTrLxXekhJrlt2IY3-Paobg5skAXFIMB')
	addDir('Birds',list,17,'http://nice-animals.com/wp-content/uploads/2013/02/colorful-birds-02.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Fish'''
	list = []
	list.append('&youtube_ch=UCZGIp0c6Dv6o6GOR7XCuZTA')
	list.append('&youtube_pl=PLfAToAFYpTfuHlcsmO-hiYcpp1yrrP10y')
	list.append('&youtube_pl=PLezpCwYgD_yvNYNXZlDM6z3mpuTQYgjUs')
	addDir('Fish',list,17,'http://corural.com/wp-content/uploads/2014/10/great-barrier-reef-fish.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''Shark'''
	list = []
	list.append('&youtube_ch=UCHThGYhvhgyvTgUkv3n5R_A') 
	addDir('Shark',list,17,'http://marinesciencetoday.com/wp-content/uploads/2009/10/Blacktip-Reef-Shark-Carcharhinus-melanopterus-Bora-Bora-Photo-by-Duncan-Rawlinson.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Snakes'''
	list = []
	list.append('&youtube_ch=UC26F6BLFDlCufiZnXsbWMwQ')
	list.append('&youtube_pl=PLWWOl-2iqjMb2UljVPPhQQy6SJJ3E-7gK')
	list.append('&youtube_pl=PLoUUkpYUScvJb2li_PY6c9fu_A3IlJKiT')
	addDir('Snakes',list,17,'http://www.888reptiles.co.uk/user/products/large/amberstripe.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Reptile'''
	list = []
	list.append('&youtube_ch=UCvfH62D48X5Bahu-oroIreQ')
	addDir('Reptile',list,17,'http://coldbloodedexpos.com/wp-content/uploads/2012/03/PatchanSambavaFired.jpg','','1',"", getAddonFanart(background, custom=""))
	

	
	'''dogs'''
	list = []
	list.append('&youtube_ch=UCcqLkZqBfBOKmi4vrgkQ6yw')
	addDir('Dogs',list,17,'http://images4.fanpop.com/image/photos/15300000/Basset-Hound-hound-dogs-15363087-800-600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Dogtv'''
	list = []
	list.append('&youtube_ch=DOGTVWORLD')
	list.append('&youtube_id=BTKo1M-QzSc')
	list.append('&youtube_pl=PLjXkouFJLKB2fBgsHcpOMTqt-cExph4RK')
	list.append('&youtube_pl=PLjXkouFJLKB3jeq_W_wBZnyZe4q-rLDKL')
	addDir('Dogtv',list,17,'http://www.telestar.fr/var/telestar/storage/images/2015/articles/dog-tv-quels-sont-les-programmes-proposes-par-cette-chaine-reservee-aux-chiens-96685/825982-1-fre-FR/Dog-TV-quels-sont-les-programmes-proposes-par-cette-chaine-reservee-aux-chiens.jpg','','1',"", getAddonFanart(background, custom=""))
 
def CATEGORIES10102(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-PLANTS-----------------
	------------------------------'''
	background = 10102
	'''Plant's'''
	list = []
	list.append('&youtube_ch=UCNVi9QvilfDjDZ8MPzSl8Xg')
	list.append('&youtube_id=eH1s9GCqPKo')
	list.append('&youtube_pl=PLgKYsEYF9_QCxM_29RC6euEJLvaHFOdrJ')
	list.append('&youtube_pl=PLs7Y2nGwfz4FL4ZJgONHsl1qp-AZPr3tJ')
	list.append('&youtube_pl=PLh8cmtKf7uVnEKm-YiByTebR3bdyOV_XV')
	list.append('&youtube_pl=PL7fxIatI1SNjeZZ8yzoyKX2b3LihqLJzs')
	list.append('&youtube_pl=PLolk0MpPk5HYNPHfb3tnSh6gSDjuGIPIv')
	list.append('&youtube_pl=PLFSXLuczIM61o8GJ_kA9UoXbbIsLXD5hS')
	list.append('&youtube_pl=PLYpOT73IUzMkKNkgQS-uGOISuOS207BL-')
	addDir("Plant's",list,17,'http://www.laspilitas.com/images/grid24_24/10506/images/native-plants/bouquet.jpg','','1',"", getAddonFanart(background, custom=""))

	'''Tree's'''
	list = []
	list.append('&youtube_ch=UCTdBhnGG8i5bNLSGBR4PJGQ')
	addDir("Tree's",list,17,'http://memolition.com/wp-content/uploads/2015/07/collection-of-beautiful-pictures-from-around-the-world-23781.jpg','','1',"", getAddonFanart(background, custom=""))

	'''Vegetable'''
	list = []
	list.append('&youtube_ch=UCsSTiRba-BUnOk0PALOhsug')
	addDir("vegetable",list,17,'http://earthdivasblog.com/wp-content/uploads/2010/07/Colorful-vegetables-755879.jpg','','1',"", getAddonFanart(background, custom=""))

	'''Botany'''
	list = []
	list.append('&youtube_ch=UCSq58WM2_CZGlps_oZeAyOQ')
	addDir("Botany",list,17,'http://chabad4israel.org/tznius4israel/pictures/brooklyn-botanic-garden-new-yor.jpg','','1',"", getAddonFanart(background, custom=""))

	'''stracture,growth & Physiology'''
	list = []
	list.append('&youtube_pl=PLamCflZiuToOGHFxb3PmgJsTW9mZQWYY1')
	list.append('&youtube_pl=PLiMEFMGielcPQRckSoNzLxxKC2LmnkIQc')
	list.append('&youtube_pl=PLamCflZiuToPflePAQQrn-vhvFbhE8JeC')
	list.append('&youtube_pl=PLDfSq7WkJcZVA58kjn0jztzjoqrJTfcaJ')
	list.append('&youtube_pl=PLamCflZiuToNa6pIevRMZec0V1-7DOmmj')
	list.append('&youtube_pl=PLamCflZiuToPohg1CYK3KAx-nOcdHOWLq')
	list.append('&youtube_pl=PLamCflZiuToNa6pIevRMZec0V1-7DOmmj')
	list.append('&youtube_pl=PLamCflZiuToOZH2SmvSdj7Z6Oy_48zOMr')
	addDir("stracture growth & Physiology",list,17,'http://lghttp.32183.nexcesscdn.net/80E716/magento/media/catalog/product/cache/1/image/b460c937cc66d1ece654b0d9d3e637af/e/d/editable-keynote-presentation-timeline-plant-growing.jpg','','1',"", getAddonFanart(background, custom=""))

	
	

def CATEGORIES10103(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-PLACES-----------------
	------------------------------'''
	background = 10103
	list = []
	list.append('&youtube_id=gWOeZ54JoO0')
	list.append('&youtube_id=w7AFRg7-hrA')
	list.append('&youtube_id=1DaFRA28C9o')
	list.append('&youtube_id=-qzIUbI_SME')
	list.append('&youtube_id=wX7ehYPWBtk')
	list.append('&youtube_id=3aY9Se-J2ww')
	list.append('&youtube_id=QfmRf8iOBkI')
	list.append('&youtube_pl=PL84lwJwmw23BiBnJwzzX1uuuHg5LM8F4A')
	list.append('&youtube_pl=3KRTfKZfIp0&list=PLmoUtGEFm50dTvd_VwML9_sEVJAQ7t2xj')
	list.append('&youtube_pl=PL5P2pncIQpzCuoGHCF_PCudmHZ4wdUIEo')
	list.append('&youtube_pl=PLdr2r9KsuBiteyDIaV_I8sb6kZCscO4kM')
	list.append('&youtube_pl=PL9HOq0cGCaCQKoh6dWz1N3s9_H7HjxA5o')
	list.append('&youtube_pl=PLxD46bIwUSnGBok3QJzd1PY6WkSiYfgKB')
	list.append('&youtube_pl=PL0pF26S5a5KD1NcL1zbMrlV7qqj4ro6iw')
	list.append('&youtube_pl=PL8rWKwqFW1l0opYCffj6A4EPi0kgobTuz')
	list.append('&youtube_pl=PLR1CNcQmgvMlowMRAo2SjCLBKzibJq0Y5')
	list.append('&youtube_pl=PLql7ZywaMwm2ugmP5-rIjUOvly5kqBV7J')
	addDir('natural places',list,17,'http://naturerandom.com/wp-content/uploads/2014/06/the-17-nature-places-to-see-before-they-disappear-forever-6.jpg','','1',"", getAddonFanart(background, custom=""))

	'''ocean's'''
	list = []
	list.append('&youtube_ch=UCpytjV41TM0RiSuZx0dS-7Q')
	list.append('&youtube_id=eH1s9GCqPKo')
	list.append('&youtube_pl=PLHva7axGsKGp38eqVqqdxD5d4IOB9KOWL')
	list.append('&youtube_pl=PL7ddU90jpZDsJAhKNsVyuMcWELCLQsrfV')
	list.append('&youtube_pl=PLrzTIP2lsW_ioMVg-nOA9no5PNg6PEfp_')
	list.append('&youtube_pl=PLufSG52JVObYXb1-aZl9e7hFkXkKe92Hj')
	list.append('&youtube_pl=PL3kcQ0lk32Iq3LDcQ8OUd6Zv6PTULCa3J')
	list.append('&youtube_pl=PL1mDQRn6BW7Q-utly7N5DyrKWZeVrrRU2')
	list.append('&youtube_pl=PLzEB0af6uUKY-C4hfcWqDI5o6P_Gbrycl')
	list.append('&youtube_pl=PLD0rNDBsRxFOxysUhikCbhsGawiU50PMX')
	list.append('&youtube_pl=PLG5mK0MTE_3GoOFcf7xKPXmcKTUnSvXW2')
	addDir("ocean's",list,17,'http://pix1.agoda.net/hotelimages/972/97258/97258_14012319470018139576.jpg?s=800x600','','1',"", getAddonFanart(background, custom=""))
 
	
	'''Earth'''
	list = []
	list.append('&youtube_ch=UC8OvMbWkaW5rWhOGsGNHD5Q')
	addDir("Earth",list,17,'http://orig14.deviantart.net/3632/f/2008/151/4/a/the_planet_earth_by_technoking.jpg','','1',"", getAddonFanart(background, custom=""))


	'''natural phenomena and disasters'''
	list = []
	list.append('&youtube_id=x-rIe1sCJU4')
	list.append('&youtube_id=x-d78aT0rbsDQ')
	list.append('&youtube_id=x-YZzvu_fnDww')
	list.append('&youtube_id=x-zb77L6v9vxM')
	list.append('&youtube_id=x-yz0QYFq8bc')
	list.append('&youtube_id=zQYe3ngG6qs')
	list.append('&youtube_id=QfmRf8iOBkI')
	list.append('&youtube_pl=PL_jFbqOSEqaJs4l1clBJ2w8dRWArUcQH3')
	list.append('&youtube_pl=PLIhyKgmJSkqK50xd2ZC3eYMPZQBGNgcmq')
	list.append('&youtube_pl=PLA42E3C7F214452E7')
	list.append('&youtube_pl=PL95E291BF550DFD9C')
	list.append('&youtube_pl=PLaKnDNcDS7loTcHzKgUJXkkCfAtYFfJd7')
	list.append('&youtube_pl=PLxD46bIwUSnGBok3QJzd1PY6WkSiYfgKB')
	list.append('&youtube_pl=PL0pF26S5a5KD1NcL1zbMrlV7qqj4ro6iw')
	list.append('&youtube_pl=PL8rWKwqFW1l0opYCffj6A4EPi0kgobTuz')
	addDir('natural phenomena and disasters',list,17,'https://wallpaperscraft.com/image/northern_lights_aurora_borealis_uk_2015_100946_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
 
    
 
	
def CATEGORIES102(admin):
	'''------------------------------
	---Space-------------------------
	------------------------------'''
	background = 102
	name = addonString(102).encode('utf-8')
	'''חיפוש'''
	addDir(localize(137),'Space Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	list.append('&youtube_pl=PLplagMMHBe3VDYwsYiz8sDwcfPdtlP3Kk')
	list.append('&youtube_pl=PLd9AuSNtqr2Um8hx3aIh4K8h9cmfW5Exi')
	list.append('&youtube_pl=PLdmZDuZvWhSWvBl4r7u2gohE9TFEybp9')
	list.append('&youtube_pl=PLw4OJKHSzqfIn7EzUUWMfMiz_Ietf33bz')
	list.append('&youtube_pl=PL1I0u8UePoJZcT6A-hkQttpoyc1DkLLjh')
	list.append('&youtube_pl=PLnm2aXiptCvgn6P6SZOPmFsfJruywU8Se')
	list.append('&youtube_pl=PLht3ColwII5rNwVkc7vJdCYkAUVr-1-uG')
	list.append('&youtube_pl=PL6oforB7ir5Iq9DHVczSeQKYfmwl-zgY3')
	list.append('&youtube_pl=PLw4zAzjwBP1d5annau67miUKlxoEERFKi')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))


	'''youtube space channels'''
	list = []
	list.append('&youtube_ch=NASAtelevision')
	list.append('&youtube_ch=spacelab')
	list.append('&youtube_ch=VideoFromSpace')
	list.append('&youtube_ch=UC7_gcs09iThXybpVgjHZ_7g')
	list.append('&youtube_ch=scishowspace')
	addDir("youtube space channel's",list,17,'http://www.fabuloussavers.com/wallpapers/wspace5.jpg','','1',"", getAddonFanart(background, custom=""))
 
	'''Universe'''
	list = []
	list.append('&youtube_ch=UCAP0Ypni5eG56SJT0A0Kwaw')
	addDir("Universe",list,17,'https://wallpaperscraft.com/image/nebula_universe_space_stars_105874_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Space'''
	list = []
	list.append('&youtube_ch=UCRqAn0M59wxBYyHHuwOXfGA')
	addDir("Space",list,17,'http://2.bp.blogspot.com/-epZUsCIzQuY/T18MYajib8I/AAAAAAAAAb4/9Z6xk2nj8Vk/s1600/Space-Wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Astronomy'''
	list = []
	list.append('&youtube_ch=UCSIJHiTGlBRsdpRf5-fEZaA')
	addDir("Astronomy",list,17,'http://www.wall321.com/thumbnails/detail/20120615/outer%20space%20stars%20nebulae%201920x1200%20wallpaper_www.wall321.com_24.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	
	
	

	
	
	
def CATEGORIES103(admin):
	'''------------------------------
	---History-----------------------
	------------------------------'''
	background = 103
	name = addonString(103).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'History Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	list.append('&youtube_pl=PLZctZ0yYTg4W4dvyFca9Yu6RK9inYHLtp')
	list.append('&youtube_pl=PLx5B22t2Ksu2jerdLdWvZ1JuYizKsnnzr')
	list.append('&youtube_pl=PL_jFbqOSEqaKU4fClblf8aI4e1Dc4hWgD')
	list.append('&youtube_pl=PLFpHQFR1whr9tedK5KP_igREFo8gwiE_6')
	list.append('&youtube_pl=PLu1rATTEb5flTauK4qgdZ64mTGFBJiJqf')
	list.append('&youtube_pl=PLqLhZXiMn3PWWIkxQCPMPD-TbzsMCOh-L')
	list.append('&youtube_pl=PLUCeR-HMWgNH4RkhcqTBDURIV8jHhBEXG')
	list.append('&youtube_pl=PL8dPuuaLjXtNjasccl-WajpONGX3zoY4M')
	list.append('&youtube_pl=PLp-cIkvQ88-1_nvZZ2-i5j90J3llXJl1o')
	list.append('&youtube_pl=PL47F868B521713645')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))

	
	'''youtube history channel's'''
	list = []
	list.append('&youtube_ch=UCQGjxZRfQ8Bt6rnudw2kgUQ')
	list.append('&youtube_ch=UCErKUCncCyBgEdxWAtrj5hg')
	list.append('&youtube_ch=AlternateHistoryHub')
	list.append('&youtube_ch=UC5xIAFuCs4m2S4uPY9dp_Ww')
	list.append('&youtube_ch=BlastfromthePast')
	list.append('&youtube_ch=TheGreatWar')
	list.append('&youtube_ch=UCBcIe5EBAxqK267uyEVibFw')
	addDir("youtube history channel's",list,17,'http://images6.fanpop.com/image/photos/36300000/Women-in-History-image-women-in-history-36309535-800-600.jpg','','1',"", getAddonFanart(background, custom=""))


	'''History Channel'''
	list = []
	list.append('&youtube_ch=historychannel')
	list.append('&youtube_pl=PLRdJd67Hep8vhFvhGNyfnglC1N9urBdDy')
	list.append('&youtube_pl=PLx5B22t2Ksu2jerdLdWvZ1JuYizKsnnzr')
	list.append('&youtube_pl=PLonoXswioCfuGeOm4jbD_P6dF3BbMbsti')
	list.append('&youtube_pl=PLMZhrNNj_z5tnKucoERFbWHB1zPoCHvYG')
	list.append('&youtube_pl=PLdKcwrFSzUrQQN9iPssQ_0JDOEE2K1c_D')
	list.append('&youtube_pl=PLNgZMT5s0l7F6Hr3wWjX6haqDNbjWzIIa')
	list.append('&youtube_pl=PLACB85DD0818A69A8')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	list.append('&youtube_pl=PLJQnz1qx0QxZNT7KQKC9L95-Wt1ZQ-gaT')
	list.append('&youtube_pl=PL5CFDF24A6CB53CD6')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	addDir("History Channel",list,17,'http://download.1wallpaper.net/20150329/the-history-channel-logo-design-black-background-800x600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''History'''
	list.append('&youtube_ch=UCBcIe5EBAxqK267uyEVibFw')
	addDir("History",list,17,'https://wallpaperscraft.com/image/colosseum_rome_italy_architecture_monument_history_25482_800x600.jpg','','1',"", getAddonFanart(background, custom=""))

    
	
	
	
	
	
def CATEGORIES104(admin):
	'''------------------------------
	---Science-----------------------
	------------------------------'''
	background = 104
	name = addonString(104).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Science Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = [] 
	list.append('&youtube_ch=UCWYeiNSo18bhZvI1pz39U6g')
	list.append('&youtube_ch=UCWkOjdpqIcKZrnjefwWMKAQ')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
	
	'''youtube science channel's'''
	list = []
	list.append('&youtube_ch=1veritasium')
	list.append('&youtube_ch=CGPGrey')
	list.append('&youtube_ch=UC6107grRI4m0o2-emgoDnAA')
	list.append('&youtube_ch=vsauce')
	list.append('&youtube_ch=AsapSCIENCE')
	list.append('&youtube_ch=scishow')
	list.append('&youtube_ch=crashcourse')
	list.append('&youtube_ch=numberphile')
	list.append('&youtube_ch=education')
	list.append('&youtube_ch=grossscienceshow')
	list.append('&youtube_ch=periodicvideos')
	addDir("youtube science channel's",list,17,'http://www.wall321.com/thumbnails/detail/20120901/science%20drugs%20molecule%20chemistry%201024x768%20wallpaper_www.wall321.com_41.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	addon = 'plugin.video.ted.talks'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('TED','plugin://'+addon,8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	
	'''מדעי החברה והרוח'''
	addDir(addonString(10401),'',10401,'http://2.bp.blogspot.com/-NvLKmKXYxIo/UTfqXTdoYTI/AAAAAAAAGSY/f3q1fXoIxHE/s1600/Social+influence.jpg',addonString(104010),'1',"", getAddonFanart(10401))
	
	'''מדעי הטבע'''
	addDir(addonString(10402),'',10402,'http://www.memrise.com/s3_proxy/?f=uploads/mems/2495464000130417092533.jpeg',addonString(104020),'1',"", getAddonFanart(10402))

	'''טכנולוגיה'''
	addDir(addonString(10403),'',10403,'http://kommercialize.com/wp-content/uploads/2013/02/iStock_000020426012Small.jpg',addonString(104030),'1',"", getAddonFanart(10403))	

	'''מחקר מדעי'''
	list.append('&youtube_ch=UCWFRiMtUDXj6N-hNe0An-VQ')
	addDir('מחקר',list,17,'https://www.colourbox.com/preview/4178295-scientific-research.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''ניסויים מדעיים'''
	list = []
	list.append('&youtube_ch=SteveSpanglerScience')
	list.append('&youtube_ch=CrazyRussianHacker')
	list.append('&youtube_ch=01032010814')
	list.append('&youtube_pl=PLGprL0LvYdRKBgndE2Se0ggtoWlcKffQb')
	list.append('&youtube_pl=PLPrxsxOjNmzjdGSrRA7IVGb1tCc9Asszp')
	list.append('&youtube_id=Ih6ApEBmHic')
	list.append('&youtube_id=8xHXx5HARC8')
	list.append('&youtube_id=HQx5Be9g16')
	list.append('&youtube_id=2n9ZZVHx_iI')
	list.append('&youtube_id=QnptSX1kPkU')
	addDir('ניסויים מדעיים',list,17,'http://1.bp.blogspot.com/-CqEGzAVgHsM/T3cAXa6qyxI/AAAAAAAAAnU/RJiWpn8rM0k/s1600/light_double_slit_experiment.png','','1',"", getAddonFanart(background, custom=""))
	
	
	
	
	
def CATEGORIES10401(name, iconimage, desc, fanart):
	'''------------------------------
	---social science-----------------
	------------------------------'''
	background = 10401
	
	
	'''ניסויים חברתיים'''
	list = []
	list.append('&youtube_pl=PLNLnlLmMBcgT9fhs_lpKRRrLasi2ggqT5')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PL0z0Pscrs45B0POHdpKhikbhjKU491-gL')
	list.append('&youtube_pl=PLU8cnQEDNLyWeKlWxwj4aY8wDuAkxa06W')
	addDir('ניסויים חברתיים',list,17,'http://www.entrepreneurs-journey.com/wp-content/uploads/2011/02/network.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''social science lectures'''
	list = []
	list.append('&youtube_pl=PLrb5XV0d1JsJAR-kAmDuyFyn6AUyDTKNH')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PLrb5XV0d1JsJnrEjivD-G1UbxB4q0hcNq')
	list.append('&youtube_pl=PLrb5XV0d1JsLyXjrm5meM3mnSI0PopLdv')
	addDir('ניסויים חברתיים',list,17,'http://www.slidecage.com/wp-content/uploads/2007/08/sliders_800x600_arturo-lecture.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Sociology'''
	list = []
	list.append('&youtube_ch=UCltQS7ZuOoJSHaPW53t0sig')
	addDir('Sociology',list,17,'http://cdn.yourarticlelibrary.com/wp-content/uploads/2013/09/241.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Politics'''
	list = []
	list.append('&youtube_ch=UCMQtDXgovMX9yMfHAEsdjVw')
	addDir('Politics',list,17,'http://wallpoper.com/images/00/28/25/35/flags-politics_00282535.png','','1',"", getAddonFanart(background, custom=""))
	
	'''Geography'''
	list = []
	list.append('&youtube_ch=UCl-12y1Zht8eSiOGBiMV7wQ')
	addDir('Geography',list,17,'http://wallpaperbeta.com/wallpaper_800x600/map_of_the_world_geographical_geography_800x600_hd-wallpaper-330201.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Law'''
	list = []
	list.append('&youtube_ch=UC_LsaJB2t-LJy2cxw_QYWyQ')
	addDir('Law',list,17,'http://oddstuffmagazine.com/wp-content/uploads/2012/06/Law.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Architecture'''
	list = []
	list.append('&youtube_ch=UCMT9aOQSpFzjorzrVpv9Dig')
	addDir('Architecture',list,17,'http://www.datavisualizationtools.biz/wp-content/uploads/2015/09/architecture-modern-atlanta-modern-architecture-architecture-atlanta-architecture.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Philosophy'''
	list = []
	list.append('&youtube_ch=UC_LsaJB2t-LJy2cxw_QYWyQ')
	addDir('Philosophy',list,17,'http://www.thegreatcourses.com/media/catalog/product/cache/1/image/800x600/0f396e8a55728e79b48334e699243c07/4/4/4477---base_image_4.1424272096.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Economy'''
	list = []
	list.append('&youtube_ch=UC15VWxug_nLMMWVbj5zgxCQ')
	list.append('&youtube_ch=UC4V_BtzAiDgh_XcNRZ70jaw')
	addDir('Economy',list,17,'http://gazettereview.com/wp-content/uploads/2015/04/march-jobs-report-economic-news.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Psychology'''
	list = []
	list.append('&youtube_ch=UCYlpMl8sk46MKU9P7XgJpGw')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PLrb5XV0d1JsJnrEjivD-G1UbxB4q0hcNq')
	list.append('&youtube_pl=PLrb5XV0d1JsLyXjrm5meM3mnSI0PopLdv')
	addDir('Psychology',list,17,'http://cdn.patch.com/users/22843411/stock/T800x600/20150254e5602e6ff13.jpg','','1',"", getAddonFanart(background, custom=""))
	
	

def CATEGORIES10402(name, iconimage, desc, fanart):
	'''------------------------------
	---natural sciences-----------------
	------------------------------'''
	background = 10402
	
	'''מתמטיקה'''
	list = []
	list.append('&youtube_ch=UCT4-UAcRfvBtO76gX2vexpA')	
	list.append('&youtube_pl=-PL_7F0HR2FSAqlAmhi3HAASthdwFaPT1mf')
	list.append('&youtube_pl=PLUl4u3cNGP63ctJIEC1UnZ0btsphnnoHR')
	list.append('&youtube_pl=PL204B0C2C2F48DF2A')
	list.append('&youtube_pl=PL3o9D4Dl2FJ8zkoLxaO4aKlq2JsKsz365')
	addDir('מתמטיקה',list,17,'https://lh4.googleusercontent.com/-Glq_hJMk9C8/T3QvhUuGdgI/AAAAAAAAAdQ/iVeLm88VrHY/w800-h800/Magic%2BMath.png','','1',"", getAddonFanart(background, custom=""))

	
	'''ביולוגיה'''
	list = []
	list.append('&youtube_ch=UCaPqwD6at0tcpG7lEUbIiPw')
	list.append('&youtube_pl=PL3EED4C1D684D3ADF')
	list.append('&youtube_pl=PL-XXv-cvA_iDuZ4BUn54ujg2kZttNk27L')
	list.append('&youtube_pl=PL-XXv-cvA_iBklnV4A6ucBpazJQ88yW-Z')
	list.append('&youtube_pl=PLFCE4D99C4124A27A')
	list.append('&youtube_pl=PL0B4CED0AB112B993')
	addDir('ביולוגיה',list,17,'http://cdn.allwallpaper.in/wallpapers/800x600/4746/biology-microscopic-cells-neurons-background-800x600-wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''פיסיקה'''
	list = []
	list.append('&youtube_ch=UCB9Sac4pdeZ7gcwhcS-q01g')	
	list.append('&youtube_pl=PL8F3D8958EFBFF76E')
	addDir('פיסיקה',list,17,'http://www.wall321.com/thumbnails/detail/20120913/mathematics%20chalkboards%20equation%20mind%201024x768%20wallpaper_www.wall321.com_79.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''כימיה'''
	list = []
	list.append('&youtube_ch=UChyplgK6jTl_XySEv0znTJw')	
	addDir('כימיה',list,17,'http://www.wallpaperhi.com/thumbnails/detail/20111217/26.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''מח'''
	list = []
	list.append('&youtube_ch=UCNJIGYmJX206jSl1tpqF1Tg')
	list.append('&youtube_ch=UCIw-oqRTWIWMV0RrF-bVtGQ')
	addDir('מח',list,17,'https://c1.staticflickr.com/9/8230/8384110298_da510e0347_b.jpg','','1',"", getAddonFanart(background, custom=""))
    
	
	'''רפואה'''
	list = []
	list.append('&youtube_ch=UCVlOYl7YDZhYvzzwOp1urtA')	
	addDir('רפואה',list,17,'http://wallpaperbeta.com/wallpaper_800x600/tablets_capsule_medicine_macro_800x600_hd-wallpaper-239312.jpg','','1',"", getAddonFanart(background, custom=""))
    
    


	

def CATEGORIES10403(name, iconimage, desc, fanart):
	'''------------------------------
	---Technology-----------------
	------------------------------'''
	background = 10403
	
	'''אקראי'''
	list = []
	list.append('&youtube_ch=UCiDF_uaU1V00dAc8ddKvNxA')
	addDir('אקראי',list,17,'http://imgur.com/kcLrrGH.jpg','','1',"", getAddonFanart(background, custom=""))

	'''קודי'''
	list = []
	list.append('&youtube_ch=hmemar22')	
	list.append('&youtube_ch=UCuSdObYHdjize3ziP951org')	
	list.append('&youtube_ch=TARGETin1080p')	
	list.append('&youtube_ch=UCoMOQDEEBECQ81CdojuEqfg')	
	list.append('&youtube_ch=UCKRic5GN63gWXc2MsWaRUHA')
	list.append('&youtube_ch=newtechevolution')
	list.append('&youtube_ch=dimitrology')	
	list.append('&youtube_ch=Charba')	
	list.append('&youtube_ch=UCrzGIViKiIGPX0BHqsTCWrQ')
	list.append('&youtube_ch=RobertoJorgeC')
	addDir('קודי',list,17,'http://i.imgur.com/bkWkbHH.png','','1',"", getAddonFanart(background, custom=""))
    
	
	'''טלפון סלולרי'''
	list = []
	list.append('&youtube_ch=UCQeVqx-WI_NrBfiOAizVgRg')	
	addDir('טלפון סלולרי',list,17,'http://wallpapers.windowsace.com/pics/f/r/free-electronics-and-gadgets-iphone-wallpaper-voyager-cell-phone--a-e-ibackgroundz.com.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''מחשבים'''
	list = []
	list.append('&youtube_ch=UCC7sJlTVc6vuxY6r5k5vuPQ')
	addDir('מחשבים',list,17,'http://www.bestfullhdwallpapers.com/download/6183/Computers/hd_wallpaper_computer_hd-800x600.jpg/','','1',"", getAddonFanart(background, custom=""))
    
	'''כלי רכב'''
	list = []
	list.append('&youtube_ch=UCHiJaXgDo_JnsfOmSe-HgzA')	
	addDir('כלי רכב',list,17,'http://wallpaperbeta.com/wallpaper_800x600/porsche_plane_sun_airfield_machine_car_800x600_hd-wallpaper-342079.jpg','','1',"", getAddonFanart(background, custom=""))
   
	'''מטוסים'''
	list = []
	list.append('&youtube_ch=UCYY7yBrHt9BDlvQWKfu0-uw')	
	addDir('מטוסים',list,17,'http://www.fabuloussavers.com/wallpapers/5_f22_raptor_fighter_plane_sunset_usairforce_aviation_wallpaper_s.jpg','','1',"", getAddonFanart(background, custom=""))
  
	'''אופנועים'''
	list = []
	list.append('&youtube_ch=UCOanIHchig1FZ2kmN1BYZLg')	
	addDir('אופנועים',list,17,'http://newestmotorcycle.com/wp-content/uploads/2015/10/awesome-cruiser-motorcycle-wallpaper-hd-800x600.jpg','','1',"", getAddonFanart(background, custom=""))
  
	'''רובוטיקה'''
	list = []
	list.append('&youtube_pl=-PLr2I5IvtDVkZGpQ-YnrsEge2ersHuhhHw')
	list.append('&youtube_pl=PLMTaZKpkWF7JF_bsmPOrb-DGiha_k82x9')
	list.append('&youtube_pl=PLV5Y1URLAmfQoCvOLtqtNSAwBeHHtP1QI')
	list.append('&youtube_pl=PLr2I5IvtDVkZmflvZn9Mvny3WBDMaGnBJ')
	list.append('&youtube_pl=PL6C6E43A700A08949')
	list.append('&youtube_pl=PL2A735F42FA18D5DD')
	list.append('&youtube_id=-nOolOVw118')
	list.append('&youtube_id=Bm6LzaxTX44')
	list.append('&youtube_id=geW-geF5fa4')
	addDir('רובוטיקה',list,17,'https://gyulchev.files.wordpress.com/2014/05/robot_blue.jpg','','1',"", getAddonFanart(background, custom=""))

	
def CATEGORIES107(admin):
	'''------------------------------
	---Kids--------------------------
	------------------------------'''
	background = 107
	name = addonString(107).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Kids Documentary',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))

	
	'''youtube kids channel's'''
	list = []
	list.append('&youtube_ch=scishowkids')
	list.append('&youtube_ch=crashcoursekids')
	list.append('&youtube_ch=KidsAnimalChannel')
	list.append('&youtube_ch=makemegenius')
	list.append('&youtube_ch=Smartlearningforall')
	list.append('&youtube_ch=hooplakidzlab')
	list.append('&youtube_ch=cUCXVCgDuD_QCkI7gTKU7-tpg')
	list.append('&youtube_ch=UCB_2_OiPFh6FdUvp50_maug')
	addDir("youtube kids channel's",list,17,'http://www.iddigital.net/images/2015/11/1447854910a3647g-800X600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''National Geographic Kids'''
	list = []
	list.append('&youtube_ch=UCav9nv7-is8vF7vrH16KPZg')	
	addDir('National Geographic Kids',list,17,'http://espana.paninimagazine.com/store/media/catalog/product/cache/5/image/800x600/9df78eab33525d08d6e5fb8d27136e95/s/n/snage018_0.jpg','','1',"", getAddonFanart(background, custom=""))
  
	
	'''animal for kids'''
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
	addDir('animal for kids',list,17,'https://d3373c9sxdao7y.cloudfront.net/content/product/large/05328RAV.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''space and planet's for kids'''
	list = []
	list.append('&youtube_id=-xKKzIoJgMSQ')
	list.append('&youtube_pl=PLRkXn_ayyCS8kOR-EKAbWx5hS_YUBEo5')
	list.append('&youtube_pl=PLwmqN2cDkUGtn_gPHUpPfLwWF3Sp9BS3R')
	list.append('&youtube_pl=PLRkXn_ayyCS8kOR-PLudXYjXPY1I6JnkHTWUiHJEvZd6f5_C26')
	list.append('&youtube_pl=PLDO7YrQpg54RumJmx39xie-QGa9NUCyFd')
	addDir('space and planet for kids',list,17,'http://4.bp.blogspot.com/-EB8N_Kjqiws/T4KSeG48w4I/AAAAAAAAA5Q/3hs2tGC3e38/s1600/Display-Cool-Space-Wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''plant's for kids'''
	list = []
	list.append('&youtube_pl=PLy0B6ncmGtqd-wb1Iqh036p3l9ZN4OCZ0')
	list.append('&youtube_pl=PLlKRPDYgEh4xRq0AYTCwWduDmhq1yFPHY')
	list.append('&youtube_pl=PL2Zef9KQGytUntJegeTmJxAFlIkaTRo-P')
	list.append('&youtube_pl=PLfo1kYEnYLcJ-UhenL0Yf3afIR3zw7fr2')
	list.append('&youtube_pl=PLeUPs98mdCOLKpvPU8tr1-1rgJ1h_xgxA')
	list.append('&youtube_pl=	PLamCflZiuToNeoHktZvD07ti-g-F1SFki')
	addDir('planets for kids',list,17,'https://cdn-jr.brainpop.com/topics/plantadaptations/motw_graphic.png','','1',"", getAddonFanart(background, custom=""))
	

def CATEGORIES110(admin):
	'''------------------------------
	---Art-------------------
	------------------------------'''
	background = 110
	name = addonString(110).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	list.append('&youtube_pl=PLLUaXSRnKa3i3nijItUi0ifqGSS908qzA')
	list.append('&youtube_pl=PL8844506E7313A565')
	list.append('&youtube_pl=PLII6iBh1SmmXbUh-O-c7crIRuFzUd1ZhR')
	list.append('&youtube_pl=PLMZJXymFn-onnjN1simnU0ci7HctVK5wx')
	list.append('&youtube_pl=PLKHtWF0sQl2MVYjQek9uYH6IJZXgNtXZP')
	list.append('&youtube_pl=PLL0D1-W61pZpMfkX0d_ylMb3iBLbdfxwv')
	list.append('&youtube_pl=PLgxrD7KGdqICE3Y5bMLxpQ0H4yXnMLAuS')
	list.append('&youtube_pl=PLlAZ-3Bm6pmYbX2q3yCO53aZ16ewlUmNI')
	list.append('&youtube_pl=PLE8Rno1I66X84UJNGbpHEUkD5FR58xxMy')
	list.append('&youtube_pl=PLwVO1qTdvxW2B7tvClvBoo_XwIY1FEhZw')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))

	
	'''youtube art channels'''
	list = []
	list.append('&youtube_ch=markcrilley')
	list.append('&youtube_ch=PESfilm')
	list.append('&youtube_ch=ChrisSamba22')
	list.append('&youtube_ch=EclecticAsylumArt')
	list.append('&youtube_ch=idrawgirls/')
	list.append('&youtube_ch=daarken')
	list.append('&youtube_ch=3dsMaxHowTos')
	list.append('&youtube_ch=CGArtSuccess')
	list.append('&youtube_ch=bluefley00')
	list.append('&youtube_ch=bedavellis')
	list.append('&youtube_ch=AlexanderKoshelkov')
	list.append('&youtube_ch=arieldiaz3d')
	list.append('&youtube_ch=iceblazer17')
	list.append('&youtube_ch=tate')
	list.append('&youtube_ch=smarthistoryvideos')
	list.append('&youtube_ch=guggenheim')
	list.append('&youtube_ch=MoMAvideos')
	list.append('&youtube_ch=UCLCHcL4M0xSwPeEuKGrsGkg')
	list.append('&youtube_ch=Sycra')
	list.append('&youtube_ch=WilliamsShamir')
	addDir("youtube art channel's",list,17,'http://www.abm-enterprises.net/fractal-art/color-16-wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
 
	'''אומנות'''
	list = []
	list.append('&youtube_ch=UCIZxVeC2kyPJIzfwaXqjhmg')
	addDir("אומנות",list,17,'http://pengcognito.com/wallpaper/nightpenguins/800x600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''צילום'''
	list = []
	list.append('&youtube_ch=UCqqMppXUKf_dBaKoF-6cXHg')	
	addDir('צילום',list,17,'https://wallpaperscraft.com/image/canon_clip_art_camera_photography_beach_42535_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''אומנים'''
	list = []
	list.append('&youtube_ch=UCAAi-y3PfAZuMJWR-2nA6Uw')
	addDir('אומנים',list,17,'http://www.davidpaulkirkpatrick.com/wp-content/uploads/2013/03/van-Gogh-Self-Potrait_1889_1890.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''עבודות אומנות'''
	list = []
	list.append('&youtube_ch=UC6SMopdiqCarcS6IUGZu2xg')
	addDir('עבודות אומנות',list,17,'https://wallpaperscraft.com/image/plate_paper_candy_pink_background_crafts_80738_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''שרטוט'''
	list = []
	list.append('&youtube_ch=UCmg3B6F4Av4vmvhM6Lyndeg')
	addDir('שרטוט',list,17,'http://orig00.deviantart.net/3a19/f/2013/230/1/8/drawing_michael_ealy_part_two_by_xjorieke-d6io2s8.jpg','','1',"", getAddonFanart(background, custom=""))
   
	'''ציור'''
	list = []
	list.append('&youtube_ch=UCVuJxpqgQ9ZexOOhCIfh6jg')	
	addDir('ציור',list,17,'http://www.florenceartacademy.it/blog/wp-content/uploads/2013/07/Gioconda.jpg','','1',"", getAddonFanart(background, custom=""))
  
	'''עיצוב פנים'''
	list = []
	list.append('&youtube_ch=UCGHWrdMukDc-uUzLYHx4r5g')
	addDir('עיצוב פנים',list,17,'http://magnificentonline.com/wp-content/uploads/2013/01/BLACK-home-design-interior-japan-livingroom.jpg','','1',"", getAddonFanart(background, custom=""))
   
	'''עיצוב גרפי'''
	list = []
	list.append('&youtube_ch=UCxRDqCzR5moFFjBNsb8lmMQ')	
	addDir('עיצוב גרפי',list,17,'http://cdn.allwallpaper.in/wallpapers/800x600/13756/graphic-design-text-typography-800x600-wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
  
	
	

def CATEGORIES108(admin):
	'''------------------------------
	---Hebrew Subtitle---------------
	------------------------------'''
	background = 108
	name = addonString(108).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'מתורגם',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	
	'''אקראי'''
	list = []
	list.append('&youtube_id=eIOvF0MlMe0')
	list.append('&youtube_id=TOeT5DQSRDc')
	list.append('&youtube_pl=VGVK6cqjoj6Aeyi2x7yQqo0S9Pq8CkZ')
	list.append('&youtube_pl=PL51YAgTlfPj6s0QtcgOpIwKewkEeSN77e')
	list.append('&youtube_id=PLEDEE611B09BB3800')
	list.append('&youtube_pl=PL51YAgTlfPj7TAvhkV8c9UnnMHUpQy-Bx')
	list.append('&youtube_pl=PL51YAgTlfPj474gCGLEUa7_Zo5Bxgy9fG')
	list.append('&youtube_pl=PL51YAgTlfPj4v3ww2jfBb21LiJFh3XSIe')
	list.append('&youtube_pl=PL51YAgTlfPj6zllZWhjkRCv95Q9LPhRZ2')
	list.append('&youtube_pl=PL51YAgTlfPj4NGa6HC87lQQL5KfqQTqW3')
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
	
	
	'''אפריקה - הסרנגטי'''
	list = []
	list.append('&youtube_id=Md3BQG4oWDU')
	addDir('אפריקה - הסרנגטי',list,17,'http://www.wallpapergeeks.com/wp-content/uploads/2014/12/african-safari-zebras-wallpaper-800x600.jpg','','1',"", getAddonFanart(background, custom=""))
					
	'''הסוד הכמוס של אפריקה'''
	list = []
	list.append('&youtube_id=jC5iaonGRCg')
	addDir('הסוד הכמוס של אפריקה',list,17,'http://photography.nationalgeographic.com/staticfiles/NGS/Shared/StaticFiles/Photography/Images/POD/s/san-bushmen-504958-sw.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''סיפורים מהסוואנה'''
	list = []
	list.append('&youtube_id=4pBLynGT5ZA')
	addDir('סיפורים מהסוואנה',list,17,'https://pbs.twimg.com/media/CJsdloWUkAE0g38.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''בית -home'''
	list = []
	list.append('&youtube_id=NEnRsTlSsxM')
	addDir('בית -home',list,17,'https://upload.wikimedia.org/wikipedia/en/a/a7/HOME-SHOT.jpg','','1',"", getAddonFanart(background, custom=""))
		
	'''ההסטוריה של העולם בשעתיים'''
	list = []
	list.append('&youtube_id=HZzSLaqk2dA')
	addDir('ההסטוריה של העולם בשעתיים',list,17,'https://i.ytimg.com/vi/HZzSLaqk2dA/hqdefault.jpg','','1',"", getAddonFanart(background, custom=""))
		
	'''טבע ישראלי'''
	list = []
	list.append('&youtube_pl=PL1PXZ56eQG-SGcBGlBXuokGz8O0Iogpzs')
	list.append('&youtube_pl=PL762D7FD5B70D28C0')
	addDir('טבע ישראלי',list,17,'http://www.israel-travel-secrets.com/images/Meshushim-pool3.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''דוקו קירשנבאום -קוסטה ריקה'''
	list = []
	list.append('&youtube_id=YMfg06-1zec')
	addDir('דוקו קירשנבאום -קוסטה ריקה',list,17,'http://images.nana10.co.il/upload/mediastock/img/8/0/192/192476.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''מים - המסתורין הגדול'''
	list = []
	list.append('&youtube_id=watch?v=JsPuREOKvPc')
	addDir('מים - המסתורין הגדול',list,17,'http://evolution-diet.com/wp-content/uploads/2013/01/water.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''חיי היונקים'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f032%2f469%2ffanarts%2fmedium%2f3e05ae14af.jpg&mode=seasons&trakt_id=32469'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('חיי היונקים','plugin://'+addon + addon2,8,'http://www.articlesweb.org/blog/wp-content/uploads/2012/04/mammals-definition-for-kids-12.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''הכוכב האנושי'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f031%2f922%2ffanarts%2fmedium%2f3d9a08eb9f.jpg&mode=seasons&trakt_id=31922'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('הכוכב האנושי','plugin://'+addon + addon2,8,'http://www.2all.co.il/web/Sites4//12123322portal/199369_(186).jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''עולם מופלא'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f001%2f039%2ffanarts%2fmedium%2f29cc38ac56.jpg&mode=seasons&trakt_id=1039'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('עולם מופלא','plugin://'+addon + addon2,8,'http://www.kinbooks.co.il/media/uploads/olam%20mufla_med.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''סיפור החיים'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f081%2f151%2ffanarts%2fmedium%2f64c7db9e96.jpg&mode=seasons&trakt_id=81151'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('סיפור החיים','plugin://'+addon + addon2,8,'http://www.bbcshop.com/content/ebiz/bbc/invt/bbcbd0281/life_story_bd_f_600.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
		
	'''אל תוך היקום עם סטיבן הוקינג'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f032%2f469%2ffanarts%2fmedium%2f3e05ae14af.jpg&mode=seasons&trakt_id=32469'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('אל תוך היקום עם סטיבן הוקינג','plugin://'+addon + addon2,8,'http://www.theupportunity.com/wp-content/uploads/2015/02/69429.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
		
	'''קוסמוס: מסע לחלל'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f071%2f041%2ffanarts%2fmedium%2fd9e784c61b.jpg&mode=seasons&trakt_id=71041'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('קוסמוס: מסע לחלל','plugin://'+addon + addon2,8,'http://contraversao.com/wp-content/uploads/2014/01/cosmos-a-spacetime-odyssey-fox-poster-800x600.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
		
	'''מבעד לחור התולעת'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f032%2f758%2ffanarts%2fmedium%2ff3e91f4d2c.jpg&mode=seasons&trakt_id=32758'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('מבעד לחור התולעת','plugin://'+addon + addon2,8,'http://cdn.indiewire.psdops.com/dims4/INDIEWIRE/6e0a535/2147483647/resize/1024x633%3E/quality/90/?url=http%3A%2F%2Fdl9fvu4r30qs1.cloudfront.net%2F66%2F36%2Fb4540b7945a295e3fb8cde27604f%2Fmorgan-freeman-through-the-wormhole.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''הכוכב הכחול'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f013%2f520%2ffanarts%2fmedium%2f7486926229.jpg&mode=seasons&trakt_id=13520'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('הכוכב הכחול','plugin://'+addon + addon2,8,'http://media.israel-music.com/images/7290372215994.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''חוצה ישראל'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4zFxXNjp8UC6nE9ePEQ9Ai')
	list.append('&youtube_pl=PL127E7734AE7476DD')
	list.append('&youtube_pl=PL3n39NB10sYkxOj0jlAWVtxGJBkMosU1K')
	addDir('חוצה ישראל',list,17,'https://i.ytimg.com/vi/i9GSeDTY5BE/maxresdefault.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''מקבלים שבת'''
	list = []
	list.append('&youtube_pl=PLLttfoK87AdVbyvsH-HGmT2on83Y9UzMo')
	list.append('&youtube_pl=PLLttfoK87AdVbyvsH-HGmT2on83Y9UzMo')
	list.append('&youtube_pl=PLE1B47D7CC412DC7B')
	addDir('מקבלים שבת',list,17,'http://www.iba.org.il/pictures/p452860.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''הסטוריה'''
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
	addDir('הסטוריה',list,17,'https://upload.wikimedia.org/wikipedia/he/d/d8/%D7%9C%D7%95%D7%92%D7%95_%D7%A2%D7%A8%D7%95%D7%A5_%D7%94%D7%94%D7%99%D7%A1%D7%98%D7%95%D7%A8%D7%99%D7%94.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''דוקו ישראלי'''
	list = []
	list.append('&youtube_pl=PLv8p71sW2GjxrF8oXQeDlqDCtELS9dVg5')		
	list.append('&youtube_pl=PLqwNAHu38eWXT7BdjK28TC1PmL1kzzEwB')
	list.append('&youtube_pl=PLT_oMlvxWt_09lgcujCrv10eOWvR-is6o')
	list.append('&youtube_id=PL-p_vqDAgZc7A')
	list.append('&youtube_pl=g6RU5xVaywc')
	list.append('&youtube_id=Sn8M283kGj0')
	list.append('&youtube_id=DOEisLFmPrs')	
	list.append('&youtube_id=PLhAvByb6CVNucuFXKM17ZNTO7RgqZ06jW')
	list.append('&youtube_id=PLeCnWyfgXGWQHx6Enc80Q70foHGq5qrIz')
	list.append('&youtube_id=PL6ADAC23F75CCB91F')
	list.append('&youtube_id=PLhAvByb6CVNtiMfk1VQhdycNyOWxYhNUT')
	addDir('דוקו ישראלי',list,17,'http://images.photolight.co.il/photo/2006-06-24/15120.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''תרבות-חינוכית'''
	list = []
	list.append('&youtube_ch=23Culture')
	addDir('תרבות-חינוכית',list,17,'https://yt3.ggpht.com/-PVEs_ee6CxU/AAAAAAAAAAI/AAAAAAAAAAA/NNkej9cD-YA/s100-c-k-no/photo.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''ערוץ הגיון ומדע'''
	list = []
	list.append('&youtube_ch=ScienceReasonIsrael')
	addDir('ערוץ הגיון ומדע',list,17,'http://www.iba.org.il/zap/pictures/P670944.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''אילוף כלבים'''
	list = []
	list.append('&youtube_ch=Orenadika73')
	addDir('אילוף כלבים',list,17,'https://lh6.googleusercontent.com/-04dBifp4BQc/VE9pqg-8-WI/AAAAAAAAACQ/FqqIgmOz0vY/w800-h800/best%2Bdog%2Btrainer.JPG','','1',"", getAddonFanart(background, custom=""))
	
	addon = 'plugin.video.seretil'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(342) + space + '1','plugin://'+addon+'/?iconimage=http%3a%2f%2fimages.nationalgeographic.com%2fwpf%2fsites%2fcommon%2fi%2fpresentation%2fNGLogo560x430-cb1343821768.png&mode=4&name=%d7%a0%d7%a9%d7%99%d7%95%d7%a0%d7%9c%20%d7%92%d7%90%d7%95%d7%92%d7%a8%d7%a4%d7%99%d7%a7&url=http%3a%2f%2fseretil.me%2fcategory%2f%25D7%25A0%25D7%25A9%25D7%2599%25D7%2595%25D7%25A0%25D7%259C-%25D7%2592%25D7%2599%25D7%2590%25D7%2595%25D7%2592%25D7%25A8%25D7%25A4%25D7%2599%25D7%25A7%2fpage1%2f',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.movixws'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(342) + space + '2','plugin://'+addon+'/?description&iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2faaron-sinuhe%2ftv-movie-folder%2f512%2fDocumentaries-National-Geographic-icon.png&mode=2&name=Documentary%20-%20%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99&url=http%3a%2f%2fwww.movix.me%2fgenres%2fDocumentary',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.sdarot.tv'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(20343) + space + '1','plugin://'+addon+'/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f11%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&name=%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&summary&url=all-heb',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	'''ילדים'''
	addDir(addonString(10801),'',10801,'http://www.disneywallpaper.net/data/media/7/Winnie_the_Pooh_kids.jpg',addonString(108010),'1',"", getAddonFanart(10801))
	

def CATEGORIES10801(name, iconimage, desc, fanart):
	'''------------------------------
	---ילדים-----------------
	------------------------------'''
	background = 10801
	
	'''חיות בספארי'''
	list = []
	list.append('&youtube_pl=PL43AC3544C5E17BEF')
	addDir('חיות בספארי',list,17,'https://d3373c9sxdao7y.cloudfront.net/content/product/large/05328RAV.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''חיות פראיות '''
	list = []
	list.append('&youtube_id=81Vh9FriKfc')
	list.append('&youtube_pl=PLB781B8A94339CC67')
	list.append('&youtube_id=RqLn1vCQVMo')
	list.append('&youtube_id=fTTsZ1OGZV8')
	list.append('&youtube_id=hqnv8qVOqLY')
	list.append('&youtube_id=9GdWNAXvd0g')
	list.append('&youtube_id=uhDjEYmF-oo')
	list.append('&youtube_pl=PL2l4T5NjtOsrGnFacKHUc1m7F1Kojuisq')
	list.append('&youtube_id=bI85XpkVTHg')
	addDir('חיות פראיות ',list,17,'http://onmilwaukee.com/images/articles/ri/rio2review/rio2review_fullsize_story1.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''קטנטנים בטבע'''
	list = []
	list.append('&youtube_id=J1JIHh1ZEf0')
	addDir('קטנטנים בטבע',list,17,'http://4.bp.blogspot.com/-i5yjcp0Hsek/VL3-_9tBpRI/AAAAAAAAjgk/3P6kPNQZDbc/s1600/%D7%A7%D7%99%D7%95%D7%98%D7%99.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''בעלי חיים לילדים ופעוטות'''
	list = []
	list.append('&youtube_id=QcANPfq5V7g')
	addDir('בעלי חיים לילדים ופעוטות',list,17,'https://i.ytimg.com/vi/jMIELC0KFs4/hqdefault.jpg','','1',"", getAddonFanart(background, custom=""))
		
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
	addDir('גלילאו',list,17,'https://i.ytimg.com/vi/HZ7UHZcIuh0/maxresdefault.jpg','','1',"", getAddonFanart(background, custom=""))
		
	'''היה היה'''
	list = []
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir('היה היה',list,17,'http://www.asksheilta.com/wp-content/uploads/2009/06/fond04_8001.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''עולם החיות של הופ'''
	list = []
	list.append('&youtube_id=l3fXEyLWCzI')
	addDir('עולם החיות של הופ',list,17,'https://i.ytimg.com/vi/l3fXEyLWCzI/hqdefault.jpg','','1',"", getAddonFanart(background, custom=""))
			
	
	'''החפרנים'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj6PWe7kECdyz6ToCjcmSd6z')
	list.append('&youtube_pl=PLth1a195qHsi9fsrgjDzYTzqKSOF-Ky-N')
	addDir('החפרנים',list,17,'http://www.maariv.co.il/HttpHandlers/ShowImage.ashx?id=274624','','1',"", getAddonFanart(background, custom=""))
	
	
	'''להיות מדען עם פרופסור דן'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4oR5aIC0Ru5JZA1a1TT-RN')
	addDir('להיות מדען עם פרופסור דן',list,17,'https://static2.timeout.co.il/media/2014/04/2%D7%90%D7%99%D7%94-%D7%90%D7%A4%D7%A8%D7%99%D7%9D_P.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''מה זה מוזה'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4F8EkY07BfV1KhdjmtjX0P')
	addDir('מה זה מוזה',list,17,'http://www.nrg.co.il/images/archive/465x349/1/536/495.jpg','','1',"", getAddonFanart(background, custom=""))

	'''מה זה מוזה במעבדה'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj59VvVLjLaAiGbFjbqv7sh3')
	addDir('מה זה מוזה במעבדה',list,17,'https://i.ytimg.com/vi/iUyRkPDPr8s/maxresdefault.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''2 2מה זה מוזה במעבדה'''
	list = []
	list.append('&youtube_pl=PLth1a195qHsj20lXv4QqTQ7kb2RLoGxY8')
	addDir( 'מה זה מוזה במעבדה 2',list,17,'https://i.ytimg.com/vi/25zKDuO98IY/sddefault.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''שירים לילדים בנושא חיות'''
	list = []
	list.append('&youtube_id=jMIELC0KFs4')
	addDir('שירים לילדים בנושא חיות',list,17,'https://i.ytimg.com/vi/jMIELC0KFs4/hqdefault.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''חיות בערוץ לולי'''
	list = []
	list.append('&youtube_pl=PLTleo-h9TFqI2CFuWeFA-Q2Bu3BBHdXqv')
	addDir('חיות בערוץ לולי',list,17,'https://i.ytimg.com/vi/6PBHhtBSpsI/maxresdefault.jpg','','1',"", getAddonFanart(background, custom=""))

	'''לולי אוהב חיות'''
	list = []
	list.append('&youtube_id=gO9hyX4s1ko')
	addDir('לולי אוהב חיות',list,17,'http://i.ytimg.com/vi/gO9hyX4s1ko/0.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''חינוכית לילדים'''
	list = []
	list.append('&youtube_ch=The23Kidz')
	addDir('חינוכית לילדים',list,17,'https://yt3.ggpht.com/-ChQs3ZvwjBI/AAAAAAAAAAI/AAAAAAAAAAA/jiyTOAdmqgo/s100-c-k-no/photo.jpg','','1',"", getAddonFanart(background, custom=""))

	
	'''חינוכית בית ספר לשפות'''
	list = []
	list.append('&youtube_ch=23language')
	addDir('חינוכית בית ספר לשפות',list,17,'https://yt3.ggpht.com/-lBNXia5dmco/AAAAAAAAAAI/AAAAAAAAAAA/WdkzNf3TbHE/s100-c-k-no/photo.jpg','','1',"", getAddonFanart(background, custom=""))

	

def CATEGORIES109(admin):
	'''------------------------------
	---TV-channels-------------------
	------------------------------'''
	background = 109
	name = addonString(109).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))
	
	'''אקראי'''
	list = []
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES109(admin):
	'''------------------------------
	---LIVE TV Channels-------------------
	------------------------------'''
	background = 109
	name = addonString(109).encode('utf-8')
	
	
	
	
	
	'''BBTS'''
	addon = 'plugin.video.bbts'
	addon2 = '/?folder=%2fDOCUMENTARIES'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('BBTS Ducomentaries','plugin://'+addon + addon2,8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''ZEUS'''
	addon = 'plugin.video.zeus'
	addon2 = '/?description&iconimage=http%3a%2f%2fs6.postimg.org%2fiiswv9g9t%2fdocumentories.png&mode=20&name=%5bCOLOR%20white%5dDOCUMENTARIES%5b%2fCOLOR%5d&url=niRwEAbN'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('ZEUS Ducomentaries','plugin://'+addon + addon2,8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''

	
	'''DogTv'''
	addon = 'plugin.video.israelive'
	addon2 = '/?url=plugin%3A%2F%2Fplugin.video.israelive%2F%3Furl%3D3226%26mode%3D1%26ignorefilmonguide%3D1%26filmonmethod%3D1&mode=10&name=%5BCOLOR+yellow%5D%5BB%5DDog+TV%5B%2FB%5D%5B%2FCOLOR%5D&iconimage=http%3A%2F%2Fstatic.filmon.com%2Fcouch%2Fchannels%2F3226%2Fextra_big_logo.png&description=&displayname=Dog+TV&categoryid=10451'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Dog Tv','plugin://'+addon + addon2,10,'http://3.bp.blogspot.com/-LRjcfd85n5o/UlNRltQt_7I/AAAAAAAAAtE/i3vgCKqbfD4/s1600/dogtv+icon+2.png',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	  
	'''Travel Channel +1'''
	addon = 'plugin.video.israelive'
	addon2 ='/?url=plugin%3A%2F%2Fplugin.video.israelive%2F%3Furl%3D842%26mode%3D1%26ignorefilmonguide%3D1&mode=10&name=%5BCOLOR+yellow%5D%5BB%5DTravel+Channel%2B1%5B%2FB%5D%5B%2FCOLOR%5D+-+%5BCOLOR+orange%5D%5BB%5DShed+and+Buried%5B%2FB%5D%5B%2FCOLOR%5D+%5BCOLOR+burlywood%5D%5B19%3A30-20%3A00%5D%5B%2FCOLOR%5D+-+%5BCOLOR+white%5DNext%3A+%5BB%5DBuilding+Alaska%5B%2FB%5D%5B%2FCOLOR%5D+%5BCOLOR+burlywood%5D%5B20%3A00-21%3A00%5D%5B%2FCOLOR%5D&iconimage=http%3A%2F%2Fstatic.filmon.com%2Fcouch%2Fchannels%2F842%2Fextra_big_logo.png&description=Henry+and+Sam+continue+their+search+through+Britain%3Fs+sheds+in+search+of+vintage+treasure+to+restore+and+sell+for+a+tidy+profit.+In+Surrey%2C+they+find+Pontiac+ambulances%2C+mysterious+automotive+sculptures+and+strangely+well-preserved+motorbikes.+reserved.&displayname=Travel+Channel%2B1&categoryid=10451'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Travel Channel+1','plugin://'+addon + addon2,10,'http://www.travelchannel.com/content/dam/images/travel/fullset/2012/08/15/bc/travel-channel_web-logo.rend.tccom.616.462.jpeg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
		
		
def CATEGORIES111(admin):
	'''------------------------------
	---National Geographic-------------------
	------------------------------'''
	background = 111
	name = addonString(111).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))

		
	
	'''National Geographic'''
	list = []
	list.append('&youtube_ch=NationalGeographic')
	list.append('&youtube_ch=UC1KCUsWsce0B6kXMv10bFsg')
	addDir("National Geographic",list,17,'https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-prn2/981552_347810472007719_83908702_o.jpg','','1',"", getAddonFanart(background, custom=""))	
 	
	
	
	
	
	'''Air Crash Investigation (Mayday)'''
	addon = 'plugin.video.salts'
	addon2 ='/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f000%2f089%2ffanarts%2fmedium%2fe16b304873.jpg&mode=seasons&trakt_id=89'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('mayday','plugin://'+addon + addon2,8,'http://cosmolearning.org/images_dir/education/documentaries/1157/profile.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''

	
	'''Brain Games'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f053%2f972%2ffanarts%2fmedium%2fa91e82b592.jpg&mode=seasons&trakt_id=53972'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Brain Games','plugin://'+addon + addon2,8,'http://static1.squarespace.com/static/52c6e2f9e4b0fbf19ff9e2c6/52d5b7b9e4b0722eef0bd3e7/52d5b7b9e4b0722eef0bd3ee/1388950219619/brain-games(1).jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
	'''DOG WHISPERER'''
	list = []
	list.append('&youtube_pl=PLdN3gbvLGO69ux2taRPiVADgwfTrPor2C')
	list.append('&youtube_pl=PLdN3gbvLGO6-MbV_l-ThMzUsWX9-XVdP6')
	list.append('&youtube_pl=PLvt1492Vj-RbJx64fEZkS5ygKZWCVOkZm')
	list.append('&youtube_pl=PLdN3gbvLGO6-OHbniVjAUMfV5Z7K_dRzz')
	list.append('&youtube_pl=PLdN3gbvLGO6_zXj9K0fwSTrqAG01MA__q')
	list.append('&youtube_pl=PL4GlJCvaiJkTath_Qafqp_K0zfyxzXTUr')
	list.append('&youtube_pl=PL4GlJCvaiJkThBI4xT-1VIHc4ZLSB0H97')
	list.append('&youtube_pl=PL4GlJCvaiJkQjm8rnXXJhkuHrfu7rM3pV')
	list.append('&youtube_pl=PL4GlJCvaiJkS5S4M2QU5AJhTRhka_SzUC')
	addDir('DOG WHISPERER',list,17,'http://cdn-img.people.com/emstag/styles/800x600/s3/i/2009/pets/migration/001074442.jpg?itok=tMQvsEP0','','1',"", getAddonFanart(background, custom=""))

	
	
	

	'''World's Most Extreme'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f080%2f202%2ffanarts%2fmedium%2fb4e2a93a35.jpg&mode=seasons&trakt_id=80202'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir("World's Most Extreme",'plugin://'+addon + addon2,8,'https://i.ytimg.com/vi/afbwKsNZ35k/maxresdefault.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
	'''Megafactories'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f005%2f320%2ffanarts%2fmedium%2f537f9c2cb3.jpg&mode=seasons&trakt_id=5320'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Megafactories','plugin://'+addon + addon2,8,'https://d3fa68hw0m2vcc.cloudfront.net/ba1/47613017.jpeg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Drugs, Inc.'''
	addon = ''
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f035%2f949%2ffanarts%2fmedium%2f1ba9dde305.jpg&mode=seasons&trakt_id=35949'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Drugs, Inc.','plugin://'+addon + addon2,8,'http://images.bwwstatic.com/columnpic6/B4F20FA4-A4D4-C308-9D0A8C30FB6655D9.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Border Wars'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f033%2f767%2ffanarts%2fmedium%2ff726488acf.jpg&mode=seasons&trakt_id=33767'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Border Wars','plugin://'+addon + addon2,8,'http://ecx.images-amazon.com/images/I/814vtg37U%2BL._SY445_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Dirty Jobs'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f002%2f568%2ffanarts%2fmedium%2fe48554af99.jpg&mode=seasons&trakt_id=2568'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Dirty Jobs','plugin://'+addon + addon2,8,'http://ecx.images-amazon.com/images/I/91OeiYvZbbL._SL1500_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
def CATEGORIES114(admin):
	'''------------------------------
	---Animal Planet-------------------
	------------------------------'''
	background = 114
	name = addonString(114).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))

	'''Animal Planet'''
	list = []
	list.append('&youtube_ch=AnimalPlanetTV')
	list.append('&youtube_ch=UC7mx4Zz-zgUeYrIxsRpPeNw')
	addDir("Animal Plane",list,17,'http://www.gasta.org/wordpress/wp-content/uploads/2013/10/Dirty-Dancing-strapline-v2.jpeg','','1',"", getAddonFanart(background, custom=""))	
 	
	
	'''river monsters'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f018%2f069%2ffanarts%2fmedium%2fda556f2c4e.jpg&mode=seasons&trakt_id=18069'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('river monsters','plugin://'+addon + addon2,8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
	
	'''Meerkat Manor'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f001%2f921%2ffanarts%2fmedium%2fd7'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Meerkat Manor','plugin://'+addon + addon2,8,'http://ecx.images-amazon.com/images/I/91JOCgTCDFL._SL1500_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	

	'''Pit Bulls & Parolees'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f031%2f400%2ffanarts%2fmedium%2f86208eb62f.jpg&mode=seasons&trakt_id=3140'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Pit Bulls & Parolees','plugin://'+addon + addon2,8,'http://cdn.renewcanceltv.com/wp-content/uploads/2015/03/PITBULLS.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
	

def CATEGORIES112(admin):
	'''------------------------------
	---Discovery-------------------
	------------------------------'''
	background = 112
	name = addonString(112).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))


	
	'''Discovery'''
	list = []
	list.append('&youtube_ch=DiscoveryNetworks')
	list.append('&youtube_ch=UCah1A9yF6I0geya0xNPHQfw')
	addDir("Discovery",list,17,'http://www.podcasts.com/uploads/50759096c7f97.jpg','','1',"", getAddonFanart(background, custom=""))
 
	
	'''Big Giant Swords'''
	addon = 'plugin.video.salts'
	addon2 = '	/?fanart=C%3a%5cUsers%5cyoel%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.salts%5cfanart.jpg&mode=seasons&trakt_id=94652'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Big Giant Swords','plugin://'+addon + addon2,8,'http://when-will.net/images/artikel/2015/february/Big-Giant-Swords.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Gold Rush'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f034%2f485%2ffanarts%2fmedium%2f88b1d5bf79.jpg&mode=seasons&tra'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Gold Rush','plugin://'+addon + addon2,8,'https://upload.wikimedia.org/wikipedia/en/e/ec/Gold_Rush_Title.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''MythBusters'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f001%2f419%2ffanarts%2fmedium%2f2f227cdbb9.jpg&mode=seasons&trakt_id=1419'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('MythBusters','plugin://'+addon + addon2,8,'http://media.boingboing.net/wp-content/uploads/2015/10/MythBusters-Unleashed.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Deadliest Catch'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f002%2f596%2ffanarts%2fmedium%2f1d4e9ac6c4.jpg&mode=seasons&trakt_id=2596'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Deadliest Catch','plugin://'+addon + addon2,8,'http://toucharcade.com/wp-content/uploads/2015/05/deadliest-catch.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Dual Survival'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f032%2f852%2ffanarts%2fmedium%2f533c12f58f.jpg&mode=seasons&trakt_id=32852'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Dual Survival','plugin://'+addon + addon2,8,'http://ecx.images-amazon.com/images/I/610wX702quL._SX940_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Fast N Loud'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f046%2f598%2ffanarts%2fmedium%2f79b727980e.jpg&mode=seasons&trakt_id=46598'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Fast N Loud','plugin://'+addon + addon2,8,'https://i.ytimg.com/vi/gnZUpBvGlWU/maxresdefault.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Naked And Afraid'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f058%2f445%2ffanarts%2fmedium%2fcfeccc090a.jpg&mode=seasons&trakt_id=58445'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Naked And Afraid','plugin://'+addon + addon2,8,'http://r.ddmcdn.com/s_f/DSC/uploads/2014/07/naked-afraid-110-notunein-01.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Man vs. Wild'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f004%2f685%2ffanarts%2fmedium%2f119d5858c3.jpg&mode=seasons&trakt_id=4685'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Man vs. Wild','plugin://'+addon + addon2,8,'http://ecx.images-amazon.com/images/I/A10AfUwm1wL._SL1500_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''how it's made'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f001%2f737%2ffanarts%2fmedium%2f9c7e7e31ac.jpg&mode=seasons&trakt_id=1737'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir("how it's made",'plugin://'+addon + addon2,8,'https://techofcomm.files.wordpress.com/2015/09/512abxavpyl-_sx940_.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''how do they do it'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f001%2f737%2ffanarts%2fmedium%2f9c7e7e31ac.jpg&mode=seasons&trakt_id=1737'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('how do they do it','plugin://'+addon + addon2,8,'http://images.zap2it.com/assets/p404110_l_h6_aa/how-do-they-do-it.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Amish Mafia'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f046%2f010%2ffanarts%2fmedium%2f2e'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Amish Mafia','plugin://'+addon + addon2,8,'https://upload.wikimedia.org/wikipedia/en/e/ee/Amish_Mafia.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
	'''ultimate survival alaska'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f070%2f702%2ffanarts%2fmedium%2f95'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('ultimate survival alaska','plugin://'+addon + addon2,8,'https://i1.ytimg.com/sh/zXSHyiqhP84/showposter.jpg?v=529ca2d6',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	

def CATEGORIES113(admin):
	'''------------------------------
	---Nat Geo Wild-------------------
	------------------------------'''
	background = 113
	name = addonString(113).encode('utf-8')
	
	'''חיפוש'''
	addDir(localize(137),'Live Docu',3,'http://files.softicons.com/download/system-icons/web0.2ama-icons-by-chrfb/png/128x128/Search.png',addonString_servicefeatherence(23).encode('utf-8') % (name),'1',"", getAddonFanart(background, custom=""))


	
	'''Nat Geo Wild'''
	list = []
	list.append('&youtube_ch=NatGeoWild')
	list.append('&youtube_ch=UCWiqP_4evlj80g_HzzvToaw')
	addDir("Nat Geo Wild",list,17,'http://www.givingbacksmiles.com/wp-content/uploads/2012/06/NAT-GEO-Ad-Snake-and-Bird.jpg','','1',"", getAddonFanart(background, custom=""))
 
	
	'''built for the kill'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=https%3a%2f%2fwalter.trakt.us%2fimages%2fshows%2f000%2f031%2f075%2ffanarts%2fmedium%2fe2259e2703.jpg&mode=seasons&trakt_id=31075'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('built for the kill','plugin://'+addon + addon2,8,'https://upload.wikimedia.org/wikipedia/en/4/41/Built_for_the_kill_collection_1_dvd_cover.jpg',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''


	'''Islands HD'''
	list = []
	list.append('&youtube_pl=PLR1CNcQmgvMlowMRAo2SjCLBKzibJq0Y5')		
	addDir('Islands HD',list,17,'http://weknowyourdreams.com/images/island/island-02.jpg','','1',"", getAddonFanart(background, custom=""))

	
	'''Wild Russia HD'''
	list = []
	list.append('&youtube_pl=PLR1CNcQmgvMlowMRAo2SjCLBKzibJq0Y5')		
	addDir('Wild Russia HD',list,17,'https://fanart.tv/fanart/tv/125511/tvthumb/W_125511.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''The Incredible Dr. Pol'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=C%3a%5cUsers%5cyoel%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.salts%5cfanart.jpg&mode=seasons&trakt_id=67584'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('The Incredible Dr. Pol','plugin://'+addon + addon2,8,'https://lh5.ggpht.com/qg2YaGNf0D-ZgZkvfni-07gXn5srBdIhxSAXbXytjd7QsxkhQnp2LC58N_ywZ52SwGtt=w1264',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	'''Fish Tank Kings'''
	addon = 'plugin.video.salts'
	addon2 = '/?fanart=C%3a%5cUsers%5cyoel%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.salts%5cfanart.jpg&mode=seasons&trakt_id=66535'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('Fish Tank Kings','plugin://'+addon + addon2,8,'https://i1.ytimg.com/sh/lgiz1rGSPZ4/showposter.jpg?v=4f9acd8b',plot,addon,50, getAddonFanart(110, custom=""))
	'''---------------------------'''
	
	
