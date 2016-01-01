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
	addDir(addonString(110).encode('utf-8'),'',110,'http://crownheights.org/wp-content/uploads/2015/07/art.jpg',addonString(1100).encode('utf-8'),'1',50, getAddonFanart(110, custom="")) #Art
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
	list.append('&youtube_ch=UC1BOeEP9-jiSmvME99fneQA/playlists')
	addDir("youtube nature channel's",list,17,'http://www.planwallpaper.com/static/images/121.jpg','','1',"", getAddonFanart(background, custom=""))
 
    
	
	
	'''Earth Touch'''
	list = []
	list.append('&custom8=plugin://plugin.video.earthtouch/')
	addDir('Earth Touch',list,8,"http://www.earthtouchnews.com/media/1074524/earth-touch-insider_series-poster_2_GalleryLarge.jpg","",'',50, getAddonFanart(110, custom=""))

	

 
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
	


	'''Lions'''
	list = []
	list.append('&youtube_id=8KaqVQP7oMk')
	list.append('&youtube_id=LU8DDYz68kM')
	list.append('&youtube_id=JRSYMfC2PFU')
	list.append('&youtube_id=EpnERlsfBFc')
	list.append('&youtube_id=Z7inua2QVdM')
	list.append('&youtube_id=2kYWXQ2N45c')
	list.append('&youtube_pl=PL5o3ll3G4aczWH4OD47Jp4xTMH5hE3kUa&index=2')
	list.append('&youtube_pl=PLkie5Q84Noe2IgDYmkMaXHZ743_T4vYcP')
	list.append('&youtube_pl=PLkie5Q84Noe2IgDYmkMaXHZ743_T4vYcP')
	list.append('&youtube_pl=PLpYgp0wW8mmZyLCqY415YbjefiazLBHzJ')
	list.append('&youtube_pl=PLpYgp0wW8mmbd_brFAIB31QSerTwHOv7j')
	addDir('Lions',list,17,'http://3.bp.blogspot.com/-Iff7IaN3DKI/UeUqIwYg3ZI/AAAAAAAAAZ4/1qJiCmolK7M/s1600/lion-photo.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Giraffe'''
	list = []
	list.append('&youtube_id=VhMU_F3arSA')
	list.append('&youtube_id=zBUgaQrUBWQ')
	list.append('&youtube_id=DRQmVSyvcKA')
	list.append('&youtube_id=7HcYJKMxpcg')
	list.append('&youtube_pl=PLVxXlr3XU-_VZwC1SOiaPBFaujWEFiTPh')
	list.append('&youtube_pl=PLVxXlr3XU-_W_YnYr9wn_6ueFPH-O3Ltb') 
	list.append('&youtube_pl=PLVxXlr3XU-_X9GwrrVOCDuTbJujU0r8_4') 
	list.append('&youtube_pl=PLVxXlr3XU-_VGu-vKA7xMs_QlrBRHThS2') 
	addDir('Giraffe',list,17,'http://ww2.valdosta.edu/~sybashlor/giraffe.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Elephant'''
	list = []
	list.append('&youtube_id=ZVAMnirC72c')
	list.append('&youtube_id=FJBtujXM5cQ')
	list.append('&youtube_id=d-GdNAnVweE')
	list.append('&youtube_id=0NVBNC37V90')
	list.append('&youtube_pl=PLAiO6kEglH8xLaBkxV7MObuAa9QqCA10b')
	list.append('&youtube_pl=PLAiO6kEglH8x7Rv1DaI1hIhpk4MGPIG8I')
	list.append('&youtube_pl=PLAiO6kEglH8w5OVIBqcl7ZlIzjIkHMXeW') 
	list.append('&youtube_pl=PLAiO6kEglH8zS--XRJUQke_MxDoCEsF3u') 
	list.append('&youtube_pl=PLAiO6kEglH8xydCtHcO2pYPlVdssYH9l4')  
	addDir('Elephant',list,17,'http://www.turtlehurtled.com/wp-content/uploads/2013/06/Elephant.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Tiger'''
	list = []
	list.append('&youtube_id=1b7oy0jo5tU')
	list.append('&youtube_id=_fc3m96wtQo')
	list.append('&youtube_id=7HcYJKMxpcg')
	list.append('&youtube_pl=PLpE7aFRb1sOUEWGAyTiqzA8jx5IncqwIr')
	list.append('&youtube_pl=PL5o3ll3G4acw3YumPFuqmJWgjgJmOVQX-')
	list.append('&youtube_pl=PLpE7aFRb1sOXrYG24pHaeqFmApxdtn5Iz') 
	list.append('&youtube_pl=PL5iIO4k3YjsRK7j4HZGNiJINQUC29wamE') 
	list.append('&youtube_pl=PLJAiNrGWNZmbZOcdxnMI5zG-bD83NYP8E')  
	addDir('Tiger',list,17,'http://www.the-south-asian.com/april2001/bengal_tiger.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Monkey'''
	list = []
	list.append('&youtube_id=lPmOcJ9YdYw')
	list.append('&youtube_id=z3pGxE4SjUI')
	list.append('&youtube_id=ITvBkHxVszg')
	list.append('&youtube_id=Rqq2rqQA3FQ')
	list.append('&youtube_pl=PLvYtTDz1O1ZSbmQpbOzz05ao4c7Ziqlzb')
	list.append('&youtube_pl=PLvYtTDz1O1ZToKTjnexNwLDFYY6oaSNGx')
	list.append('&youtube_pl=PLvYtTDz1O1ZSUQVSwotzFtQh0LHwmm_6v') 
	list.append('&youtube_pl=PLzcIUDUth-LrlrwlP04LIkPMhjgq-cSPO') 
	list.append('&youtube_pl=PLb7h-pNxlzo-YAGePRFli68k7cOHxIWHI')
	list.append('&youtube_pl=PLZKAUcf1exr2OxfbQaqcuCOxAEi-NklJt')	
	addDir('Monkey',list,17,'http://www.happytrailsindonesia.com/uploads/img/8/Monkey%20Indonesia.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Birds'''
	list = []
	list.append('&youtube_id=0Yjdf3woXl8')
	list.append('&youtube_id=YTR21os8gTA')
	list.append('&youtube_id=Xb0P5t5NQWM')
	list.append('&youtube_id=pd5BMP_41bI')
	list.append('&youtube_pl=PLvTrLxXekhJrlt2IY3-Paobg5skAXFIMB') 
	list.append('&youtube_pl=PLvTrLxXekhJosswcJtwUAyZmD1Kn0ePrN')
	list.append('&youtube_pl=PLADghIKXCKMd39gUXdb2m3mOJF25-ighv')
	list.append('&youtube_pl=PLvTrLxXekhJoJM4NroZILrYVOCot7Gw0i')
	addDir('Birds',list,17,'http://nice-animals.com/wp-content/uploads/2013/02/colorful-birds-02.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Fish'''
	list = []
	list.append('&youtube_id=Z-BbpaNXbxg')
	list.append('&youtube_id=5G_6YZrNNy0')
	list.append('&youtube_id=Slp8G7bAWeA')
	list.append('&youtube_id=Yx1a5swwqXc')
	list.append('&youtube_pl=PLfAToAFYpTfuHlcsmO-hiYcpp1yrrP10y')
	list.append('&youtube_pl=PLezpCwYgD_yvNYNXZlDM6z3mpuTQYgjUs')
	list.append('&youtube_pl=PL3L2HQeYSn6ff_0gyAJ8T_Hcsq9uyxxx1')
	list.append('&youtube_pl=PLSMO2bjU_7i9A7SbNN4PB_cosoXsmrBWN')
	addDir('Fish',list,17,'http://corural.com/wp-content/uploads/2014/10/great-barrier-reef-fish.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''Shark'''
	list = []
	list.append('&youtube_id=zQV_WcltnsA')
	list.append('&youtube_id=zeQMqUMvIeY')
	list.append('&youtube_id=6aKcazsEWPk')
	list.append('&youtube_id=xrt27dZ7DOA')
	list.append('&youtube_id=aBzW95qi9gs')
	list.append('&youtube_id=RKyn6dEMHKA')
	list.append('&youtube_pl=PLB3B2BB679EA6723E')
	list.append('&youtube_pl=PLCE93DFB3E4FFA625')
	list.append('&youtube_pl=PL9BFF5E829E9F4C0A')
	list.append('&youtube_pl=PL2B-PWFn-iOZPvf3javy1DaGvy9nCl0pk')
	addDir('Shark',list,17,'http://marinesciencetoday.com/wp-content/uploads/2009/10/Blacktip-Reef-Shark-Carcharhinus-melanopterus-Bora-Bora-Photo-by-Duncan-Rawlinson.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Snakes'''
	list = []
	list.append('&youtube_id=l56K8eAtCig')
	list.append('&youtube_id=C17LC5M_v1k')
	list.append('&youtube_id=MiHPMpXqX20')
	list.append('&youtube_id=AJ2l4owxC7s')
	list.append('&youtube_id=lkdFDKk8YWk')
	list.append('&youtube_pl=PLWWOl-2iqjMb2UljVPPhQQy6SJJ3E-7gK')
	list.append('&youtube_pl=PLoUUkpYUScvJb2li_PY6c9fu_A3IlJKiT')
	list.append('&youtube_pl=PL5o3ll3G4acyS0FuMUmUct17qnGIMT9L-')
	list.append('&youtube_pl=PLLxGCgUG6c44p9fsTX5SJKxmooliiou8X')
	addDir('Snakes',list,17,'http://www.888reptiles.co.uk/user/products/large/amberstripe.jpg','','1',"", getAddonFanart(background, custom=""))
	


	
	'''dogs'''
	list = []
	list.append('&youtube_id=mwm0OwqWvF4')
	list.append('&youtube_id=ilMzs1UHEmw')
	list.append('&youtube_id=B8ISzf2pryI')
	list.append('&youtube_id=rp03AorAWLY')
	list.append('&youtube_id=zOiWYQIrqyE')
	list.append('&youtube_id=b0nG0kuwcSg')
	list.append('&youtube_pl=PLuVVnmxF_tkSSxMWZZYOCopZ-h5YiBW48')
	list.append('&youtube_pl=PLMssKIjsDxXmMGypWsr8u-yGOUSoPoozb')
	list.append('&youtube_pl=PLIAkKPWGh_rbUV3uPDUXCOcoMEv3VJnsP')
	list.append('&youtube_pl=PLIAkKPWGh_rawwECMC2UCD0zSq-QUz2_Z')
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
	list.append('&youtube_id=SvUJHX0EG4c')
	list.append('&youtube_id=wcmKT5uHgL0')
	list.append('&youtube_id=OTfB7FWipWk')
	list.append('&youtube_id=BsL5nsEf56s')
	list.append('&youtube_id=NsIojj4PzAo')
	list.append('&youtube_id=3qNlk3FAb5c')
	list.append('&youtube_id=MgDZBqTuUuE')
	list.append('&youtube_id=metLFxsnLDc')
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
	list.append('&youtube_id=8pJPSxYGp1Y')
	list.append('&youtube_id=cNlqSCN9V-4')
	list.append('&youtube_id=FpeCOyxWEsc')
	list.append('&youtube_id=qdlJUnfDTus')
	list.append('&youtube_id=TI7sJnMADHk')
	list.append('&youtube_id=DY1jz3SQXJ')
	list.append('&youtube_id=m5Mmq2vxkB0')
	list.append('&youtube_id=QJvtJeB2Iq0')
	list.append('&youtube_id=9aq_ssT-vfs')
	list.append('&youtube_id=BickMFHAZR0')
	list.append('&youtube_pl=PL21A27CBAD0255C88')
	list.append('&youtube_pl=PLS2vMpIq_JAklZyf-gI3MAtotuBZGs3b8')
	list.append('&youtube_pl=PLbuqSmk1tafN-_LltPvJ9T5DRmP8bVO_a')
	list.append('&youtube_pl=PLAA38DC71D32D4FAB')
	list.append('&youtube_pl=PL5C118AE173F37A41')
	list.append('&youtube_pl=PLQlgR0H02jQtTCuwdO5PFGYw1-pz4Q33')
	addDir("Tree's",list,17,'http://memolition.com/wp-content/uploads/2015/07/collection-of-beautiful-pictures-from-around-the-world-23781.jpg','','1',"", getAddonFanart(background, custom=""))

	
	'''orchid'''
	list = []
	list.append('&youtube_id=tzgdCaBNUPI')
	list.append('&youtube_id=tLj62iMs-TY')
	list.append('&youtube_id=J1FZNjASyKg')
	list.append('&youtube_id=QdfGCscTMak')
	list.append('&youtube_id=wbXQIsNKysk')
	list.append('&youtube_id=rI4YMycBfFk')
	list.append('&youtube_pl=PLAACBEB202A901918')
	list.append('&youtube_pl=PLPODINV_NFvrHTLuY_5t24zksa_a6nFX_')
	list.append('&youtube_pl=PLxo6tXzj__mYMG6SleHkd2-w4s5r15BYB')
	list.append('&youtube_pl=PLtWeWo5hGEkXgeSFumvRs2UPnM4uzvSyT')
	list.append('&youtube_pl=PLC1AEDCB8419E20E0')
	list.append('&youtube_pl=PLxo6tXzj__maD-wYTfK7_HZ-LSQRc9Xxm')
	list.append('&youtube_pl=PLdmAnVS3TYh3EWSHsQUxRMIwebHyi8OQb')
	list.append('&youtube_pl=PL-dcm20p996rQpoffnFBIlAZefgSpO55j')
	list.append('&youtube_pl=PL-dcm20p996o5X9LdTspLmO8QY24Ah_vE')
	list.append('&youtube_pl=PLek3G4uZlLYa7oipoSuvu2PmrxZPsBRN3')
	list.append('&youtube_pl=PL-dcm20p996r3ocrVFos7Shx6UvYwGhet')
	list.append('&youtube_pl=PL-dcm20p996peINJHgMOLskxDTGMlShDG')
	addDir("Orchid",list,17,'http://1.bp.blogspot.com/-ysKfjEIIlvA/U4mlY_TLzHI/AAAAAAAAAGU/Hu6j3XFa3Jg/s1600/Orchid-flower-HD-stock-photos-editable-for-greetings.jpg','','1',"", getAddonFanart(background, custom=""))

	
	'''Botany'''
	list = []
	list.append('&youtube_pl=PL7D120055C712F646')
	list.append('&youtube_pl=PLFDF144E5C691634E')
	list.append('&youtube_pl=PLJAzFg3PHTb3HVw18aKBsL82UGSdHGo-F')
	list.append('&youtube_pl=PLamCflZiuToPflePAQQrn-vhvFbhE8JeC')
	list.append('&youtube_pl=PLDfSq7WkJcZVA58kjn0jztzjoqrJTfcaJ')
	list.append('&youtube_pl=PLamCflZiuToNa6pIevRMZec0V1-7DOmmj')
	list.append('&youtube_pl=PLamCflZiuToPohg1CYK3KAx-nOcdHOWLq')
	list.append('&youtube_pl=PLsBvTYtPA-42WyF1BDOfp96wNQoNkajE9')
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
	list.append('&youtube_id=VNqNnUJVcVs')
	list.append('&youtube_id=GOAEIMx39-w')
	list.append('&youtube_id=x1QTc5YeO6w')
	list.append('&youtube_id=COWE6sMzdqI')
	list.append('&youtube_id=6v2L2UGZJAM')
	list.append('&youtube_pl=PL9CE54703E2B8E92F')
	list.append('&youtube_pl=PL746FAD2B2C91D906')
	list.append('&youtube_pl=PLki90Aw2GjddE7j9gsNyZ2BLOS9onitwN')
	list.append('&youtube_pl=PLZa5JgpDRphafqlAxL_j9eOGQkRsrQ1a6')
	list.append('&youtube_pl=PLzW2SWgVnP9sr5xy1qUxfkmnZAf47J9Wu')
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
	list.append('&youtube_ch=canadianspaceagency')
	addDir("youtube space channel's",list,17,'http://www.fabuloussavers.com/wallpapers/wspace5.jpg','','1',"", getAddonFanart(background, custom=""))
 
	'''Space Exploration'''
	list = []
	list.append('&youtube_id=tMVDWvHlrRc')
	list.append('&youtube_id=htOtW0pD92Y')
	list.append('&youtube_id=_P57CbtAVE0')
	list.append('&youtube_id=KyKvr_7fNWc')
	list.append('&youtube_id=ZtaKWt26dNs')
	list.append('&youtube_id=GVTm0loi9OY')
	list.append('&youtube_id=dyyOcL5tn7k')
	list.append('&youtube_ch=UC7DeQ1bhSunszQ3JQ-25WiA/playlists')
	addDir("Space Exploration",list,17,'https://wallpaperscraft.com/image/nebula_universe_space_stars_105874_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Hubble Space Telescope'''
	list = []
	list.append('&youtube_id=udAL48P5NJU')
	list.append('&youtube_id=3afEX8a2jPg')
	list.append('&youtube_id=SnnJg0jqr8A')
	list.append('&youtube_id=ZQKW76d2xrw')
	list.append('&youtube_ch=HubbleSiteChannel')
	list.append('&youtube_pl=PLowYwBwSCQXWnznaU5d0KXA2rz4vkHgsY')
	list.append('&youtube_pl=PLYTAjChqCnmE8QkMiaEilnBX20gxmbXG2')
	list.append('&youtube_pl=PLDA7830389EE0BA94')
	list.append('&youtube_pl=PLowYwBwSCQXW4OkSW1Oh0UbIe-w_h5crt')
	addDir("Space",list,17,'http://2.bp.blogspot.com/-epZUsCIzQuY/T18MYajib8I/AAAAAAAAAb4/9Z6xk2nj8Vk/s1600/Space-Wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Astronomy'''
	list = []
	list.append('&youtube_id=L3op3B907hM')
	list.append('&youtube_id=rCqZQdqd6Cw')
	list.append('&youtube_id=uabNtlLfYyU')
	list.append('&youtube_id=Xp4OIzvqE9k')
	list.append('&youtube_pl=PLsNB4peY6C6KgGVbYmTp0N5zPIXYE3ebY')
	list.append('&youtube_pl=PLw4zAzjwBP1d5annau67miUKlxoEERFKi')
	list.append('&youtube_pl=PL8dPuuaLjXtPAJr1ysd5yGIyiSFuh0mIL')
	list.append('&youtube_pl=PL39CB50AA10C74547')
	list.append('&youtube_pl=PLB47070730D7DA3F2')
	list.append('&youtube_pl=PL2yn_e5rlIW0bsNIOc3dEadJ6YwTOoj-Z')
	addDir("Astronomy",list,17,'http://www.wall321.com/thumbnails/detail/20120615/outer%20space%20stars%20nebulae%201920x1200%20wallpaper_www.wall321.com_24.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Astronaut'''
	list = []
	list.append('&youtube_id=7DWzmq9e0Lw')
	list.append('&youtube_id=uVLfkSrzBPk')
	list.append('&youtube_id=uabNtlLfYyU')
	list.append('&youtube_id=9ZEdApyi9Vw')
	list.append('&youtube_pl=PLN4k6F5s6hnkfkZ5py9pvdW4PMJ4pUqLG')
	list.append('&youtube_pl=PLN4k6F5s6hnm0GZ8tNJDNVP4osOiFwdLw')
	list.append('&youtube_pl=PLOXyXTU9MRIknE5ZVSWkEQ--HBLivYcM3')
	list.append('&youtube_pl=PLN4k6F5s6hnntHXavTTQ_T43eRlyZKjea')
	list.append('&youtube_pl=PLOXyXTU9MRIl4BGXzh8RAwHIdacWVAVpD')
	addDir("Astronaut",list,17,'http://www.blt.co.uk/wp-content/uploads/2015/12/Astronauts_Nigeria_.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''eso'''
	list = []
	list.append('&custom8=plugin://plugin.video.eso/')
	addDir('ESO-European Organisation for Astronomical Research',list,8,"https://lh6.googleusercontent.com/-UUnCTamsMNo/TXRGOOvxvnI/AAAAAAAAArY/psesZKPG8so/s1600/Nova_Fires_jpg.jpg","",'',50, getAddonFanart(110, custom=""))

	
	
	'''ESA'''
	list = []
	list.append('&custom8=plugin://plugin.video.esa/')
	addDir('ESA- European Space Agency',list,8,"http://www.esa.int/var/esa/storage/images/esa_multimedia/images/2006/05/artist_s_impression_of_the_gaia_satellite/9272925-5-eng-GB/Artist_s_impression_of_the_Gaia_satellite.jpg","",'',50, getAddonFanart(110, custom=""))

	
	
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
	addDir("History Channel",list,17,'http://download.1wallpaper.net/20150329/the-history-channel-logo-design-black-background-800x600.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''World Wars'''
	list = []
	list.append('&youtube_ch=TheGreatWar')
	list.append('&youtube_pl=PLC-0e1pjuxF9bc8e0cDsmj0tqGJ0Ss8tT')
	list.append('&youtube_pl=PL-b6BqXQgEFo88XFZ2r-DQmN-c5W5W9u-')
	list.append('&youtube_pl=PLtvqDUuIy5Ee5p_YVMoOfhCmkaLie32KB')
	list.append('&youtube_pl=PL7eLCXTvueOvs67EDHnuKr7aXguRyuJ0S')
	list.append('&youtube_pl=PLu7g1OfsO2vcKnzSXQiCHisyUIQcclbxr')
	list.append('&youtube_pl=PL95DD3A12BDB77AF0')
	list.append('&youtube_pl=PLACB85DD0818A69A8')
	list.append('&youtube_pl=PLCA467ED9C59E9D8D')
	list.append('&youtube_pl=PLkJloWOsgyNlKNx-LhoAp50o5gqn5d8rp')
	list.append('&youtube_pl=PLHbgAq4l2Bj7AwVk7R1SIuhqtki7fPLUL')
	list.append('&youtube_pl=PL8dPuuaLjXtNjasccl-WajpONGX3zoY4M')
	list.append('&youtube_pl=PLLvOGyTQQoqziO-Uobw49bDRT2Lel0t3R')
	list.append('&youtube_pl=PL6oforB7ir5JDZaxy6017UJM-cvC-CpKy&index=1')
	addDir("World Wars",list,17,'http://cdn.usborne.com/catalogue/covers/eng/width_223px/87886.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''Military history'''
	list.append('&youtube_id=m7pT4T0dixQ')
	list.append('&youtube_id=JldZnx3msTY')
	list.append('&youtube_id=PRA2zXjX-Xk')
	list.append('&youtube_id=emDz5qghrzY')
	list.append('&youtube_pl=PLi4lYGGXHIkMwfUrvRCTGZgbiBSjanvKw')
	list.append('&youtube_pl=PLaXWjn2EfstzVU9xb0HQRiPUOzAt6D1Z0')
	list.append('&youtube_pl=PLfFUSMjNfugL-kJQdkQS6B2_x_0cSDpnd')
	list.append('&youtube_ch=UClh0ObJvSmUAJU9K9mefMKg/playlists')
	list.append('&youtube_pl=PLi4lYGGXHIkMwfUrvRCTGZgbiBSjanvKw')
	list.append('&youtube_pl=PLdVZrg_VhTFEchYC_NfvZQLHBzbh08PZ4')
	list.append('&youtube_pl=PL6CCB81AAEACD6D17')
	addDir("Military history",list,17,'https://upload.wikimedia.org/wikipedia/en/d/d0/History_channel_military.png','','1',"", getAddonFanart(background, custom=""))

    

	
	
	
	
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
	list = []
	list.append('&youtube_pl=PLtSuKq2ke_sm8yCeOhOs-yaYgEyVIKXxt')
	list.append('&youtube_pl=PLtSuKq2ke_snSo4WimGOrlquJc8r7Tq7u')                        
	list.append('&youtube_pl=PLtSuKq2ke_skIPkapVG8PLBUmIOSgPlkS')
	list.append('&youtube_pl=PLtSuKq2ke_slVxQS0sqeYVoLkmP74Y4gW')
	list.append('&youtube_pl=PLtSuKq2ke_sn4qo5px_i1jZNVDzz47PVJ')
	list.append('&youtube_pl=PLtSuKq2ke_smyz5y_v6N36MfT5dgA4ORB')
	list.append('&youtube_pl=PLtSuKq2ke_sn4qo5px_i1jZNVDzz47PVJ')
	list.append('&youtube_pl=PLtSuKq2ke_smyz5y_v6N36MfT5dgA4ORB')
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
	list.append('&youtube_pl=PLiyEC8E9r_ymK3Ps3DbXtzn9NDt9b47PY')
	list.append('&youtube_pl=PLiyEC8E9r_yltRbrb3lKnf-wuvsxUq1w6')
	list.append('&youtube_pl=PLiyEC8E9r_ymDhossOXG2t-XXE_G9j_1-')
	list.append('&youtube_pl=PLiyEC8E9r_ymUoLrKtCmVDJyxFyYFl5z2')
	list.append('&youtube_pl=PLP8Ma8K8YxnwiAYGiCMba5yu8swa6a7-V')
	list.append('&youtube_pl=PLT35IWG8lUbYwramdIPMAR5wPbDFjDU0H')
	addDir('Sociology',list,17,'http://cdn.yourarticlelibrary.com/wp-content/uploads/2013/09/241.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Politics'''
	list = []
	list.append('&youtube_pl=PL3Ikn3SKdJHgC14x0oUEMJ7pxG_Yj8UNa')
	list.append('&youtube_pl=PLlTLHnxSVuIyeEZPBIQF_krewJkY2JSwi')
	list.append('&youtube_pl=PLeyJPHbRnGaaKyuj1467jFo7gzXqYSPKx')
	list.append('&youtube_pl=PLt-M8o1W_GdQrVQpvLQMJZlprs5MD0imr')
	list.append('&youtube_pl=PLrb5XV0d1JsJQIgr3l1iJtkRjzr1Cgbu8')
	addDir('Politics',list,17,'http://wallpoper.com/images/00/28/25/35/flags-politics_00282535.png','','1',"", getAddonFanart(background, custom=""))
	
	'''Geography'''
	list = []
	list.append('&youtube_pl=PL67F390EB9FE9F4F0')
	list.append('&youtube_pl=PLR7XO54Pktt8_jNjAVaunw1EqqcEAdcow')
	list.append('&youtube_pl=R719mLoDLaQ&list=PLD985DC24042D71ED')
	list.append('&youtube_pl=PL3RbLxbjtXdmyirZPUqrKKWrSjGlfwqRc')
	list.append('&youtube_pl=PLzW2SWgVnP9t9VP7q65cy7Zg3o9DudTUx')
	list.append('&youtube_pl=PL71HsN_LrZoA-Suz9mznJktPqwHVMQRX0')
	list.append('&youtube_pl=PLdAwJqwLRJOHCEeJwJipe24G1-6YYwSLd')
	list.append('&youtube_pl=PLVeXbgaZS8ge9SQwQK47meZbUGA0I-RwX')
	addDir('Geography',list,17,'http://wallpaperbeta.com/wallpaper_800x600/map_of_the_world_geographical_geography_800x600_hd-wallpaper-330201.jpg','','1',"", getAddonFanart(background, custom=""))
	

	'''Architecture'''
	list = []
	list.append('&youtube_id=sHL_F9g9scY')
	list.append('&youtube_id=gi9u6VgGn3k')
	list.append('&youtube_id=iY0Uuyf8Xhw')
	list.append('&youtube_id=Gb8k7pkGKKA')
	list.append('&youtube_id=KCB1_paPy-c')
	list.append('&youtube_pl=PLB3DC6A8DE288C013')
	list.append('&youtube_pl=PLPXsMt57rLthe1kihStAdRgGdj3IZ7WHe')
	list.append('&youtube_pl=PLABA0239EA68C47B6')
	list.append('&youtube_pl=PLnEy4CjpTzIUsjNPw1T62KDnYl_hBUU7X')
	list.append('&youtube_pl=PLs6rfCOqpsQgt_Ycctt-oRLhKiolwHbUZ')
	addDir('Architecture',list,17,'http://www.datavisualizationtools.biz/wp-content/uploads/2015/09/architecture-modern-atlanta-modern-architecture-architecture-atlanta-architecture.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Philosophy'''
	list = []
	list.append('&youtube_ch=thephilosophytube')
	list.append('&youtube_pl=PLwxNMb28XmpfEr2zNKQfU97eyEs70krSb')
	list.append('&youtube_pl=hdCBGWcd4qw&list=PL914258A2DAF5D393')
	list.append('&youtube_pl=PLtKNX4SfKpzUURFV6ucpn2TGaZYqXyrai')
	list.append('&youtube_pl=XXBQRuMfs2E&list=PLFF9E7ADD88FBA144')
	list.append('&youtube_id=Tm0Uq08xXhY')
	list.append('&youtube_id=j3BKnmtlMco')
	list.append('&youtube_id=UVA8jX9KQcE')
	list.append('&youtube_id=Mz_iGGGMddw')
	addDir('Philosophy',list,17,'http://www.thegreatcourses.com/media/catalog/product/cache/1/image/800x600/0f396e8a55728e79b48334e699243c07/4/4/4477---base_image_4.1424272096.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Economics'''
	list = []
	list.append('&youtube_pl=PL6FA614EF0CB2AD82')
	list.append('&youtube_pl=PL8dPuuaLjXtPNZwz5_o_5uirJ8gQXnhEO')
	list.append('&youtube_pl=PLA46DB4506062B62B')
	list.append('&youtube_pl=PL11ADD17785C9C9A4')
	list.append('&youtube_pl=PLE70CA726102FB294')
	list.append('&youtube_pl=PL50F9C4FD0BE8FE28')
	list.append('&youtube_pl=5IDhKM&list=PL54ADCC41A7E439B7')
	list.append('&youtube_pl=5IDhKM&list=PL-9JQaDLOcT5MLi4NdWH7arCY3dEhozFS')
	addDir('Economics',list,17,'http://gazettereview.com/wp-content/uploads/2015/04/march-jobs-report-economic-news.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''Psychology'''
	list = []
	list.append('&youtube_ch=UCYlpMl8sk46MKU9P7XgJpGw/playlists')
	list.append('&youtube_pl=PL8dPuuaLjXtOPRKzVLY0jJY-uHOH9KVU6')
	list.append('&youtube_pl=P3FKHH2RzjI&list=PL6A08EB4EEFF3E91F')
	list.append('&youtube_pl=PL6uC-XGZC7X6xObklmWEk8MbRVm87g0Uu')
	list.append('&youtube_pl=XgRlrBl-7Yg&list=PLFDE868BCF58A3950')
	list.append('&youtube_pl=2fbrl6WoIyo&list=PL44ABC9278E2EE706')
	list.append('&youtube_pl=PLg0JqCtcY-SxZt4kKj0b0OgIZESF46TDP')
	addDir('Psychology',list,17,'http://cdn.patch.com/users/22843411/stock/T800x600/20150254e5602e6ff13.jpg','','1',"", getAddonFanart(background, custom=""))
	
	

def CATEGORIES10402(name, iconimage, desc, fanart):
	'''------------------------------
	---natural sciences-----------------
	------------------------------'''
	background = 10402
	
	'''מתמטיקה'''
	list = []
	list.append('&youtube_id=HzeTPM3yEbI')
	list.append('&youtube_id=VJf8XAhC550')
	list.append('&youtube_id=YWHx0RsRNzI')
	list.append('&youtube_id=oiIW69RU')
	list.append('&youtube_pl=PLE3376FF44087B17B')	
	list.append('&youtube_pl=-PL_7F0HR2FSAqlAmhi3HAASthdwFaPT1mf')
	list.append('&youtube_pl=PLUl4u3cNGP63ctJIEC1UnZ0btsphnnoHR')
	list.append('&youtube_pl=PL204B0C2C2F48DF2A')
	list.append('&youtube_pl=PL3o9D4Dl2FJ8zkoLxaO4aKlq2JsKsz365')
	list.append('&youtube_pl=PLc0BtI8B0p-F8SHQ95LUIpBS0zozJIVc3')
	addDir('מתמטיקה',list,17,'https://lh4.googleusercontent.com/-Glq_hJMk9C8/T3QvhUuGdgI/AAAAAAAAAdQ/iVeLm88VrHY/w800-h800/Magic%2BMath.png','','1',"", getAddonFanart(background, custom=""))

	
	'''ביולוגיה'''
	list = []
	list.append('&youtube_id=juM2ROSLWfw')
	list.append('&youtube_id=MsHEAnPX59Y')
	list.append('&youtube_id=Y2f7YwCtHcgk')
	list.append('&youtube_id=gFuEo2ccTPA')
	list.append('&youtube_ch=UCaPqwD6at0tcpG7lEUbIiPw')
	list.append('&youtube_pl=PL3EED4C1D684D3ADF')
	list.append('&youtube_pl=PL-XXv-cvA_iDuZ4BUn54ujg2kZttNk27L')
	list.append('&youtube_pl=PL-XXv-cvA_iBklnV4A6ucBpazJQ88yW-Z')
	list.append('&youtube_pl=PLFCE4D99C4124A27A')
	list.append('&youtube_pl=PL0B4CED0AB112B993')
	list.append('&youtube_pl=PL7A9646BC5110CF64')
	list.append('&youtube_pl=PLC0CC234D0C5278A9')
	list.append('&youtube_pl=PLwL0Myd7Dk1F0iQPGrjehze3eDpco1eVz')
	list.append('&youtube_pl=PLB3FCEEAC84884760')
	addDir('ביולוגיה',list,17,'http://cdn.allwallpaper.in/wallpapers/800x600/4746/biology-microscopic-cells-neurons-background-800x600-wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''פיסיקה'''
	list = []
	list.append('&youtube_ch=UCUK0HBIBWgM2c4vsPhkYY4w')
	list.append('&youtube_ch=physicsgalaxy74')
	list.append('&youtube_ch=bestdamntutoring')
	list.append('&youtube_ch=minutephysics')
	list.append('&youtube_ch=Fysikshow')
	list.append('&youtube_ch=ilectureonline')
	list.append('&youtube_id=Ws6AAhTw7RA')
	list.append('&youtube_id=RtWbpyjJqrU')
	list.append('&youtube_id=0NbBjNiw4tk')
	list.append('&youtube_id=pnbJEg9r1o8')
	list.append('&youtube_id=IOYyCHGWJq4')
	list.append('&youtube_id=gzkB574jivA')
	list.append('&youtube_id=YAfmZKX24Zs')
	list.append('&youtube_id=1Xp_imnO6WE')
	list.append('&youtube_ch=UCB9Sac4pdeZ7gcwhcS-q01g')	
	list.append('&youtube_pl=PL8F3D8958EFBFF76E')
	list.append('&youtube_pl=PLaMjJl9Tuw7GnWs5upbXwmXdoJDaeIK_E')
	list.append('&youtube_pl=PLaMjJl9Tuw7HoCo8wzZNwMC7jjo3nrEvx')
	list.append('&youtube_pl=PLPxO-_IM9m7ixs5EASdix4veUUHET8oRz')
	list.append('&youtube_pl=PLQkrOakXQ_vGfcN29-KmVKYENsUwNLyPK')
	addDir('פיסיקה',list,17,'http://www.wall321.com/thumbnails/detail/20120913/mathematics%20chalkboards%20equation%20mind%201024x768%20wallpaper_www.wall321.com_79.jpg','','1',"", getAddonFanart(background, custom=""))
	
	'''כימיה'''
	list = []
	list.append('&youtube_id=C5tOEBmBAHg')
	list.append('&youtube_id=_g_ml8tAnWE')
	list.append('&youtube_id=IFKnq9QM6_A')
	list.append('&youtube_id=u6MfZbCvPCw')
	list.append('&youtube_ch=periodicvideos')
	list.append('&youtube_ch=tdewitt451')
	list.append('&youtube_pl=PLPxO-_IM9m7jpLSepNkezbLVNq19DztUK')
	list.append('&youtube_pl=PLk-gRvbk-NRT01UkWrLjIFIhFsu4A_0RD')
	list.append('&youtube_pl=PLPxO-_IM9m7hyNbuBZMDYkJUf_V8SdSIF')
	list.append('&youtube_pl=PLk-gRvbk-NRQ8Tdx3bZjYNsuNPWqJZR_7')
	list.append('&youtube_pl=PLk-gRvbk-NRQnOvOr-eiEXlIjenN5c1ai')
	list.append('&youtube_pl=PLk-gRvbk-NRQxVEoGmK75H9QQ9qIJTuaZ')
	list.append('&youtube_pl=PL7A1F4CF36C085DE1')
	list.append('&youtube_pl=PL166048DD75B05C0D')
	addDir('כימיה',list,17,'http://www.wallpaperhi.com/thumbnails/detail/20111217/26.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''מח'''
	list = []
	list.append('&youtube_ch=UCNJIGYmJX206jSl1tpqF1Tg')
	list.append('&youtube_id=JiTz2i4VHFw')
	list.append('&youtube_id=9bx7Vl6klmw')
	list.append('&youtube_id=K2MrzXPlt8o')
	list.append('&youtube_id=uAbUtrwYETg')
	list.append('&youtube_id=DfgkAJmp9-A')
	list.append('&youtube_id=3P8q_dCU3RI')
	list.append('&youtube_pl=PLMWnwPCA972tbj1p_FJJl8_scEuvIFEfD')
	list.append('&youtube_pl=PLMWnwPCA972sL53mDP7nCj2h95wMBtia0')
	list.append('&youtube_pl=PLMWnwPCA972tDM1djs-nmfN4Uvjer36Kn')
	list.append('&youtube_pl=PLk-gRvbk-NRQ8Tdx3bZjYNsuNPWqJZR_7')
	list.append('&youtube_pl=PLk-gRvbk-NRQnOvOr-eiEXlIjenN5c1ai')
	list.append('&youtube_pl=PLk-gRvbk-NRQxVEoGmK75H9QQ9qIJTuaZ')
	addDir(' מדעי ומשחקי מח',list,17,'https://c1.staticflickr.com/9/8230/8384110298_da510e0347_b.jpg','','1',"", getAddonFanart(background, custom=""))
    
	
	'''רפואה'''
	list = []	
	list.append('&youtube_pl=PLfJpbOpZBUQa34cJ2TRKpz3oA_3BywCs-')
	list.append('&youtube_pl=PL01AEFFF7C4C3C881')
	list.append('&youtube_pl=PL04349AC9C197EC93')
	list.append('&youtube_pl=PLpRE0Zu_k-BxWZoSNhjTxYLE3t14XUljV')
	list.append('&youtube_pl=PL831FBCA74153165E')
	list.append('&youtube_pl=PL4E2A5CA2AC52F71F')
	list.append('&youtube_id=mNvm0OWQOgA')
	list.append('&youtube_id=Qxx14RCxblg')
	list.append('&youtube_id=OBm1c_7tnCk')
	list.append('&youtube_id=9V-Ts9rFX2Q')
	addDir('רפואה',list,17,'http://wallpaperbeta.com/wallpaper_800x600/tablets_capsule_medicine_macro_800x600_hd-wallpaper-239312.jpg','','1',"", getAddonFanart(background, custom=""))
    
    


	

def CATEGORIES10403(name, iconimage, desc, fanart):
	'''------------------------------
	---Technology-----------------
	------------------------------'''
	background = 10403
	
	'''אקראי'''
	list = []
	list.append('&youtube_ch=PLB76E9DFE905DDAC0')
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
	list.append('&youtube_ch=UCrzGIViKiIGPX0BHqsTCWrQ')
	list.append('&youtube_ch=RobertoJorgeC')
	addDir('קודי',list,17,'http://i.imgur.com/bkWkbHH.png','','1',"", getAddonFanart(background, custom=""))
    
	
	'''טלפון סלולרי'''
	list = []
	list.append('&youtube_pl=PL57quI9usf_sKq-un-sKiH28GufDbfXud')
	list.append('&youtube_pl=PL57quI9usf_us0KVzB8aZFPVmdvp1_sIh')
	list.append('&youtube_pl=PLPBN-Ln1bNtxpgyoI2uVTAoD3VqHfe83c')
	list.append('&youtube_pl=PL57quI9usf_ujAfHHeCUHuJDL9rMo2_kr')
	addDir('טלפון סלולרי',list,17,'https://creationapplication.com/wp-content/uploads/2013/01/iStock_000019696025_Large1.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''מחשבים'''
	list = []
	list.append('&youtube_pl=PL57quI9usf_skTMa14vP58RZxlSjCIJ1P')
	list.append('&youtube_pl=PL57quI9usf_uI8ZxI58Gc5ACnmbL7rxP-')
	list.append('&youtube_pl=PL57quI9usf_so2Apomw8ap8jMm8e2-xTs')
	list.append('&youtube_pl=PL57quI9usf_saUGUzSvs4909pfSaloLHS')
	addDir('מחשבים',list,17,'http://7-themes.com/data_images/out/73/7022381-computer-keyboard-wallpaper.jpg','','1',"", getAddonFanart(background, custom=""))
    
	
	'''אלקטרוניקה'''
	list = []
	list.append('&youtube_pl=PL3C5D963B695411B6')
	list.append('&youtube_pl=PLC8A1AD995AB64055')
	list.append('&youtube_pl=PLFF553CED56CDE25D')
	list.append('&youtube_pl=PL9CDF91EC3585AAD9')
	list.append('&youtube_pl=PLLilrKdbjXDH-ztjsBHZLEpRvKHHP6bgO')
	list.append('&youtube_pl=PL774BE597B77BF3C5')
	addDir('אלקטרוניקה',list,17,'http://www.alsglobal.com/~/media/Images/Divisions/Life%20Sciences/Electronics%20Testing/Electronics%204.jpg','','1',"", getAddonFanart(background, custom=""))
   
	
	
	'''כלי רכב'''
	list = []
	list.append('&youtube_pl=PLE5A7A868916EA37C')
	list.append('&youtube_pl=PLN6Q52i0YBycJHc1nZ8BQrymggkDXQWoi')
	list.append('&youtube_pl=PLLilrKdbjXDH-ztjsBHZLEpRvKHHP6bgO')
	list.append('&youtube_pl=PL0_qQzejvS2m9t_PtPp1NMA6RqMeN0RVi')
	list.append('&youtube_pl=PLTu8nanTJo7ENISO0CPDoTesFUCk7uDXt')
	list.append('&youtube_pl=PLwC75JJGC4SUavw0jxNw66mTHsaPyLMqY')
	list.append('&youtube_pl=0TGJWxOYdemHRZCcGHCK')
	list.append('&youtube_pl=PLyFDjajffaUAxX0JIB2bVlJL-r-Og3GhW')
	list.append('&youtube_pl=PLwC75JJGC4SUavw0jxNw66mTHsaPyLMqY')
	list.append('&youtube_pl=PLlxvC7vPiNHBfbJJGMdAi-8njhYGQHgGt')
	addDir('כלי רכב',list,17,'http://wallpaperbeta.com/wallpaper_800x600/porsche_plane_sun_airfield_machine_car_800x600_hd-wallpaper-342079.jpg','','1',"", getAddonFanart(background, custom=""))
   

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
	list.append('&youtube_pl=PLamCflZiuToNeoHktZvD07ti-g-F1SFki')
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
	addDir('צילום',list,17,'https://wallpaperscraft.com/image/canon_clip_art_camera_photography_beach_42535_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''אומנים'''
	list = []
	list.append('&youtube_pl=PLgxrD7KGdqIAjKrX7044XQCCYyygH_Iip')
	list.append('&youtube_pl=PLgxrD7KGdqIBZ8L3mbbDWhtKVJx4P6VSY')
	list.append('&youtube_pl=PLYIapPsysmjCw77uxfyxW7HmdoMEooZzZ')
	list.append('&youtube_pl=PL3A50F86AE9A35934')
	list.append('&youtube_pl=PLgxrD7KGdqIAJLfcDPQHgj_mA6yMYFP0S')
	list.append('&youtube_pl=PLgxrD7KGdqICXqET81hxUjnbvRbQyw5bi')
	list.append('&youtube_pl=PLLUaXSRnKa3i3nijItUi0ifqGSS908qzA')
	addDir('אומנים',list,17,'http://www.davidpaulkirkpatrick.com/wp-content/uploads/2013/03/van-Gogh-Self-Potrait_1889_1890.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''עבודות אומנות'''
	list = []
	list.append('&youtube_pl=PLpKVHhjWeQ6_b9dCLPDTXNNLLrdSuwvQ')
	list.append('&youtube_pl=PLSVoinOQWRwRIzhWxuK2KWoHH454deajP')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	addDir('עבודות אומנות',list,17,'https://wallpaperscraft.com/image/plate_paper_candy_pink_background_crafts_80738_800x600.jpg','','1',"", getAddonFanart(background, custom=""))
    
	'''שרטוט'''
	list = []
	list.append('&youtube_pl=iXTDv4BewvLgrgttAC6OgX')
	list.append('&youtube_pl=PLhBKkQX9XSgeVEGuevcUrnxWYhyB31rZG')
	list.append('&youtube_pl=PLhBKkQX9XSgeALUlhjOdRwMaq7ucc6t6c')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	list.append('&youtube_pl=PLvwqC5cvT9A56w--qpeul2oiV0vz95CSm')
	addDir('שרטוט',list,17,'http://orig00.deviantart.net/3a19/f/2013/230/1/8/drawing_michael_ealy_part_two_by_xjorieke-d6io2s8.jpg','','1',"", getAddonFanart(background, custom=""))
   
	'''ציור'''
	list = []
	list.append('&youtube_pl=PLAEQD0ULngi67rwmhrkNjMZKvyCReqDV4')
	list.append('&youtube_pl=PL-OQ2u8XlJLuACG2jfzt_XxK8pDVsdIhm')
	list.append('&youtube_pl=PLCgkDVJst-Zhh6lqVu0UVUQPe68hgdEUo')
	list.append('&youtube_pl=PL2010F0BDC411BDC9')
	list.append('&youtube_pl=PL95664E97F3D868D7')
	addDir('ציור',list,17,'http://www.florenceartacademy.it/blog/wp-content/uploads/2013/07/Gioconda.jpg','','1',"", getAddonFanart(background, custom=""))
  
	
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
	addDir('פיסול',list,17,'https://s-media-cache-ak0.pinimg.com/736x/ef/06/95/ef0695c68517e3baaf58313d82573984.jpg','','1',"", getAddonFanart(background, custom=""))
  
	

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
	
	
	'''דוקו סרטים'''
	list = []
	list.append('&youtube_id=Md3BQG4oWDU')
	list.append('&youtube_id=jC5iaonGRCg')
	list.append('&youtube_id=4pBLynGT5ZA')
	list.append('&youtube_id=NEnRsTlSsxM')
	list.append('&youtube_id=watch?v=JsPuREOKvPc')
	list.append('&youtube_id=watch?v=Qw3lObBE8WE')
	list.append('&youtube_id=watch?v=vYzxryWHVZs')
	list.append('&youtube_id=uIotx1aGtKg')
	addDir('דוקו סרטים',list,17,'http://www.wallpapergeeks.com/wp-content/uploads/2014/12/african-safari-zebras-wallpaper-800x600.jpg','','1',"", getAddonFanart(background, custom=""))
					
		
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
	list.append('&youtube_pl=PLMOOIFFitzstfZJRTXIeirKr8V-UoUpsA')
	list.append('&youtube_pl=PL6A2CaEev7b4vrILtDfeCszrTq1rsXl_c')
	list.append('&youtube_pl=PL1PXZ56eQG-SGcBGlBXuokGz8O0Iogpzs')
	list.append('&youtube_pl=PL762D7FD5B70D28C0')
	addDir('טבע ישראלי',list,17,'http://www.israel-travel-secrets.com/images/Meshushim-pool3.jpg','','1',"", getAddonFanart(background, custom=""))
	
	
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
	list.append('&youtube_pl=PLLttfoK87AdV7Q8Eu8a_J3pVv28nC2lMv')
	list.append('&youtube_id=EFD_o0-1QbQ')
	list.append('&youtube_id=L5Wq-ma70tY')
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
	list.append('&youtube_ch=UCLpn_QJwfehfKuTt0orfYDw')
	addDir('ערוצי הגיון ומדע',list,17,'http://www.iba.org.il/zap/pictures/P670944.jpg','','1',"", getAddonFanart(background, custom=""))

	
	#'''אילוף כלבים'''
	#list = []
	#list.append('&youtube_ch=Orenadika73')
	#addDir('אילוף כלבים',list,17,'https://lh6.googleusercontent.com/-04dBifp4BQc/VE9pqg-8-WI/AAAAAAAAACQ/FqqIgmOz0vY/w800-h800/best%2Bdog%2Btrainer.JPG','','1',"", getAddonFanart(background, custom=""))
	
	'''מאקו הרצאות'''
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fstatic1.squarespace.com%2fstatic%2f545c3cefe4b0263200cf8bb7%2ft%2f5474d191e4b0dda9e3ce84e7%2f1416941970318%2flecture.jpg%3fformat%3d1500w&mode=0&name=%d7%94%d7%a8%d7%a6%d7%90%d7%95%d7%aa&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-more%2flectures')
	addDir('מאקו הרצאות',list,8,"","",'plugin.video.MakoTV',50, getAddonFanart(110, custom=""))
	
	'''מאקו דוקו'''
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV//?iconimage=http%3a%2f%2fopendoclab.mit.edu%2fwp%2fwp-content%2fuploads%2f2011%2f09%2fcamera.jpg&mode=0&name=%d7%93%d7%95%d7%a7%d7%95&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-more%2fdocu_tv')
	addDir('דוקו מאקו',list,8,"","",'plugin.video.MakoTV',50, getAddonFanart(110, custom=""))

	
	'''וואלה דוקו'''
	list = []
	list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=wallavod&name=%d7%93%d7%95%d7%a7%d7%95%20(56)&url=genre%3dmovies%26genreId%3d6263')
	addDir('דוקו וואלה',list,8,"","",'',50, getAddonFanart(110, custom=""))

	'''ערוץ 8'''
	list = []
	list.append('&custom8=plugin://plugin.video.hotVOD.video/?mode=5&name=%d7%a2%d7%a8%d7%95%d7%a5%208&url=http%3a%2f%2fhot.ynet.co.il%2fhome%2f0%2c7340%2cL-7461%2c00.html')
	addDir('ערוץ 8',list,8,"","",'',50, getAddonFanart(110, custom=""))

	
	addon = 'plugin.video.ilten'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('דוקו 10','plugin://'+addon+'/?category=2118',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	
	addon = 'plugin.video.seretil'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('sertil דוקו','plugin://'+addon+'/?iconimage=http%3a%2f%2fimages.nationalgeographic.com%2fwpf%2fsites%2fcommon%2fi%2fpresentation%2fNGLogo560x430-cb1343821768.png&mode=4&name=%d7%a0%d7%a9%d7%99%d7%95%d7%a0%d7%9c%20%d7%92%d7%90%d7%95%d7%92%d7%a8%d7%a4%d7%99%d7%a7&url=http%3a%2f%2fseretil.me%2fcategory%2f%25D7%25A0%25D7%25A9%25D7%2599%25D7%2595%25D7%25A0%25D7%259C-%25D7%2592%25D7%2599%25D7%2590%25D7%2595%25D7%2592%25D7%25A8%25D7%25A4%25D7%2599%25D7%25A7%2fpage1%2f',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.movixws'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('movix דוקו','plugin://'+addon+'/?description&iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2faaron-sinuhe%2ftv-movie-folder%2f512%2fDocumentaries-National-Geographic-icon.png&mode=2&name=Documentary%20-%20%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99&url=http%3a%2f%2fwww.movix.me%2fgenres%2fDocumentary',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.sdarot.tv'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('sdarot.tv דוקו','plugin://'+addon+'/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f11%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&name=%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&summary&url=all-heb',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
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

