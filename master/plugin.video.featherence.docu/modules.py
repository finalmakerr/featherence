﻿# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
from modulesA import *
from modulesZ import *
"""-----------------------------"""

def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	CATEGORIES_SEARCH(mode=30, url="")
	addDir(addonString(30000).encode('utf-8'),'MyDocu',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0, getAddonFanart(100, default="https://i.ytimg.com/vi/esMX5NIsHdk/maxresdefault.jpg")) #My Docu
	addDir(addonString(30001).encode('utf-8'),'',101,'https://i.ytimg.com/vi/q4AQDDKglEE/maxresdefault.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30001).encode('utf-8')),'1',0, getAddonFanart(101, default="http://www.freedomwallpaper.com/wp-content/uploads/2015/02/Wild-animal-wallpaper-2.jpg")) #Nature
	addDir(addonString(30002).encode('utf-8'),'',102,'http://www.esa.int/var/esa/storage/images/esa_multimedia/images/2014/02/searching_for_exoplanetary_systems/14282306-1-eng-GB/Searching_for_exoplanetary_systems.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30002).encode('utf-8')),'1',0, getAddonFanart(102, default="http://infossible.com/infosdata/wp-content/uploads/2015/08/Earth-From-Space-Space-1080x1920.jpg")) #Space
	addDir(addonString(30003).encode('utf-8'),'',103,'http://wsap.academy/wp-content/uploads/2015/03/1123676.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30003).encode('utf-8')),'1',0, getAddonFanart(103, default="https://d1ox703z8b11rg.cloudfront.net/uploads_image/3caff507-7d11-49ef-973a-c38a5fefe0e6/d01263ae1ef2e674b4920fecc6ddb625.png")) #History
	addDir(addonString(30004).encode('utf-8'),'',104,'http://orig07.deviantart.net/ff1a/f/2009/033/1/3/science_wallpaper_by_hamdanzinha.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30004).encode('utf-8')),'1',0, getAddonFanart(104, default="http://wallpapercave.com/wp/582gycq.jpg")) #Science
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
	
def CATEGORIES101(name, iconimage, desc, fanart):
	'''טבע'''
	background = 101
	
	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'Nature Docu',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES101Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
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
	addDir(addonString(30101).encode('utf-8'),list,17,'http://bocadolobo.com/blog/wp-content/uploads/2013/11/10-of-the-Most-Inspiring-Places-On-Earth-Boca-do-Lobo-blog-Fairy-Pools-Scotland.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30101).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="https://i.ytimg.com/vi/gvWRDhd7QXM/maxresdefault.jpg"))		
	
	'''Earth Touch'''
	list = []
	list.append('&custom8=plugin://plugin.video.earthtouch/')
	addDir(addonString(30102).encode('utf-8'),list,8,"http://www.earthtouchnews.com/media/1074524/earth-touch-insider_series-poster_2_GalleryLarge.jpg",addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30102).encode('utf-8')),'',0, getAddonFanart(background, default=fanart, custom=""))
	
	'''בעלי חיים'''
	addDir(addonString(30103).encode('utf-8'),'',10101,'http://3.bp.blogspot.com/-GmdLk2R6ahA/T55Ud9aXCcI/AAAAAAAABY4/4Z9aMnM0Ukc/s1600/Blue-Butterfuly-Latest-Animal-Wallpaper-2012.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30103).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''צומח'''
	addDir(addonString(30104).encode('utf-8'),'',10102,'https://lh5.ggpht.com/rJg02fFypSfx2mL6BMWEN__3Je-E-sy2ZDgZs2PNnnFLawi2b1QtL9S_GtY5sPLXPw=h900',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30104).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''כדור הארץ'''
	addDir(addonString(30105).encode('utf-8'),'',10103,'https://s-media-cache-ak0.pinimg.com/originals/f6/7c/e8/f67ce86161d17cbde49bac13be0ea023.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30105).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://copthornekuwait.com/wp-content/uploads/2016/01/most-beautiful-places-in-the-world-wallpapers.jpg"))

	CATEGORIES101A(name, iconimage, desc, getAddonFanart(background, default=fanart, custom="")) # עמוד הבא
 
def CATEGORIES10101(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-ANIMALS----------------
	------------------------------'''
	background = 10101
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10101Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''אריות'''
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
	addDir(addonString(30110).encode('utf-8'),list,17,'http://3.bp.blogspot.com/-Iff7IaN3DKI/UeUqIwYg3ZI/AAAAAAAAAZ4/1qJiCmolK7M/s1600/lion-photo.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30110).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://4997-presscdn-0-37.pagely.netdna-cdn.com/wp-content/uploads/2014/12/Lion-Cubs.jpg"))
	
	'''גירפות'''
	list = []
	list.append('&youtube_id=VhMU_F3arSA')
	list.append('&youtube_id=zBUgaQrUBWQ')
	list.append('&youtube_id=DRQmVSyvcKA')
	list.append('&youtube_id=7HcYJKMxpcg')
	list.append('&youtube_id=vh3Rcl-2wDE')
	list.append('&youtube_id=pg9bUkS87-Y') 
	addDir(addonString(30111).encode('utf-8'),list,17,'http://ww2.valdosta.edu/~sybashlor/giraffe.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30111).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://3.bp.blogspot.com/-BQNfb36zZmM/ULekrJYr-UI/AAAAAAAAAM4/548nRni_LTo/s1600/Giraffe-HD-Wallpapers.jpg"))
	
	'''דגים'''
	list = []
	list.append('&youtube_id=Z-BbpaNXbxg')
	list.append('&youtube_id=5G_6YZrNNy0')
	list.append('&youtube_id=Slp8G7bAWeA')
	list.append('&youtube_id=Yx1a5swwqXc')
	list.append('&youtube_pl=PLfAToAFYpTfuHlcsmO-hiYcpp1yrrP10y')
	list.append('&youtube_pl=PLezpCwYgD_yvNYNXZlDM6z3mpuTQYgjUs')
	list.append('&youtube_pl=PL3L2HQeYSn6ff_0gyAJ8T_Hcsq9uyxxx1')
	list.append('&youtube_pl=PLSMO2bjU_7i9A7SbNN4PB_cosoXsmrBWN')
	addDir(addonString(30116).encode('utf-8'),list,17,'http://corural.com/wp-content/uploads/2014/10/great-barrier-reef-fish.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30116).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''פילים'''
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
	addDir(addonString(30112).encode('utf-8'),list,17,'http://he.bcdn.biz/Images/2010/12/14/a66c6d7a-2379-41b9-bd7f-a4a9ffa66ec3.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30112).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://img.hrhwalls.com/images219/omdzhyapbs0.jpg"))
	
	'''טיגריסים'''
	list = []
	list.append('&youtube_id=1b7oy0jo5tU')
	list.append('&youtube_id=_fc3m96wtQo')
	list.append('&youtube_id=7HcYJKMxpcg')
	list.append('&youtube_pl=PLpE7aFRb1sOUEWGAyTiqzA8jx5IncqwIr')
	list.append('&youtube_pl=PL5o3ll3G4acw3YumPFuqmJWgjgJmOVQX-')
	list.append('&youtube_pl=PLpE7aFRb1sOXrYG24pHaeqFmApxdtn5Iz') 
	list.append('&youtube_pl=PL5iIO4k3YjsRK7j4HZGNiJINQUC29wamE') 
	list.append('&youtube_pl=PLJAiNrGWNZmbZOcdxnMI5zG-bD83NYP8E')  
	addDir(addonString(30113).encode('utf-8'),list,17,'http://www.the-south-asian.com/april2001/bengal_tiger.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30113).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''כלבים'''
	list = []
	list.append('&youtube_ch=DOGTVWORLD')
	list.append('&youtube_pl=PLuVVnmxF_tkSSxMWZZYOCopZ-h5YiBW48')
	list.append('&youtube_pl=PLMssKIjsDxXmMGypWsr8u-yGOUSoPoozb')
	list.append('&youtube_pl=PLIAkKPWGh_rbUV3uPDUXCOcoMEv3VJnsP')
	list.append('&youtube_pl=PLIAkKPWGh_rawwECMC2UCD0zSq-QUz2_Z')
	list.append('&youtube_pl=PLjXkouFJLKB2fBgsHcpOMTqt-cExph4RK')
	list.append('&youtube_pl=PLjXkouFJLKB3jeq_W_wBZnyZe4q-rLDKL')
	list.append('&youtube_id=BTKo1M-QzSc')
	list.append('&youtube_id=mwm0OwqWvF4')
	list.append('&youtube_id=ilMzs1UHEmw')
	list.append('&youtube_id=B8ISzf2pryI')
	list.append('&youtube_id=rp03AorAWLY')
	list.append('&youtube_id=zOiWYQIrqyE')
	list.append('&youtube_id=b0nG0kuwcSg')
	addDir(addonString(30119).encode('utf-8'),list,17,'http://images4.fanpop.com/image/photos/15300000/Basset-Hound-hound-dogs-15363087-800-600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30119).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''כרישים'''
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
	addDir(addonString(30117).encode('utf-8'),list,17,'http://marinesciencetoday.com/wp-content/uploads/2009/10/Blacktip-Reef-Shark-Carcharhinus-melanopterus-Bora-Bora-Photo-by-Duncan-Rawlinson.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30117).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''נחשים'''
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
	addDir(addonString(30118).encode('utf-8'),list,17,'http://www.888reptiles.co.uk/user/products/large/amberstripe.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30118).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''ציפורים'''
	list = []
	list.append('&youtube_id=0Yjdf3woXl8')
	list.append('&youtube_id=YTR21os8gTA')
	list.append('&youtube_id=Xb0P5t5NQWM')
	list.append('&youtube_id=pd5BMP_41bI')
	list.append('&youtube_pl=PLvTrLxXekhJrlt2IY3-Paobg5skAXFIMB') 
	list.append('&youtube_pl=PLvTrLxXekhJosswcJtwUAyZmD1Kn0ePrN')
	list.append('&youtube_pl=PLADghIKXCKMd39gUXdb2m3mOJF25-ighv')
	list.append('&youtube_pl=PLvTrLxXekhJoJM4NroZILrYVOCot7Gw0i')
	addDir(addonString(30115).encode('utf-8'),list,17,'http://nice-animals.com/wp-content/uploads/2013/02/colorful-birds-02.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30115).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
		
	'''קופים'''
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
	addDir(addonString(30114).encode('utf-8'),list,17,'http://www.happytrailsindonesia.com/uploads/img/8/Monkey%20Indonesia.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30114).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES10101A(name, iconimage, desc, fanart)
	
def CATEGORIES10102(name, iconimage, desc, fanart):
	'''טבע - חוקי טבע'''
	background = 10102
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10102Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
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
	addDir(addonString(30170).encode('utf-8'),list,17,'http://www.laspilitas.com/images/grid24_24/10506/images/native-plants/bouquet.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30170).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

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
	addDir(addonString(30171).encode('utf-8'),list,17,'http://memolition.com/wp-content/uploads/2015/07/collection-of-beautiful-pictures-from-around-the-world-23781.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30171).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
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
	addDir(addonString(30172).encode('utf-8'),list,17,'http://1.bp.blogspot.com/-ysKfjEIIlvA/U4mlY_TLzHI/AAAAAAAAAGU/Hu6j3XFa3Jg/s1600/Orchid-flower-HD-stock-photos-editable-for-greetings.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30172).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

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
	addDir(addonString(30173).encode('utf-8'),list,17,'http://chabad4israel.org/tznius4israel/pictures/brooklyn-botanic-garden-new-yor.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30173).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''Plant physiology'''
	list = []
	list.append('&youtube_pl=PLamCflZiuToOGHFxb3PmgJsTW9mZQWYY1')
	list.append('&youtube_pl=PLiMEFMGielcPQRckSoNzLxxKC2LmnkIQc')
	list.append('&youtube_pl=PLamCflZiuToPflePAQQrn-vhvFbhE8JeC')
	list.append('&youtube_pl=PLDfSq7WkJcZVA58kjn0jztzjoqrJTfcaJ')
	list.append('&youtube_pl=PLamCflZiuToNa6pIevRMZec0V1-7DOmmj')
	list.append('&youtube_pl=PLamCflZiuToPohg1CYK3KAx-nOcdHOWLq')
	list.append('&youtube_pl=PLamCflZiuToNa6pIevRMZec0V1-7DOmmj')
	list.append('&youtube_pl=PLamCflZiuToOZH2SmvSdj7Z6Oy_48zOMr')
	addDir(addonString(30174).encode('utf-8'),list,17,'http://lghttp.32183.nexcesscdn.net/80E716/magento/media/catalog/product/cache/1/image/b460c937cc66d1ece654b0d9d3e637af/e/d/editable-keynote-presentation-timeline-plant-growing.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30174).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	CATEGORIES10102A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES10103(name, iconimage, desc, fanart):
	'''כדור הארץ'''
	background = 10103
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10103Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''מקומות'''
	list = []
	list.append('&youtube_id=gWOeZ54JoO0')
	list.append('&youtube_id=1DaFRA28C9o')
	list.append('&youtube_id=-qzIUbI_SME')
	list.append('&youtube_id=wX7ehYPWBtk')
	list.append('&youtube_id=3aY9Se-J2ww')
	list.append('&youtube_id=QfmRf8iOBkI')
	list.append('&youtube_pl=PL84lwJwmw23BiBnJwzzX1uuuHg5LM8F4A')
	list.append('&youtube_pl=PLmoUtGEFm50dTvd_VwML9_sEVJAQ7t2xj')
	list.append('&youtube_pl=PL5P2pncIQpzCuoGHCF_PCudmHZ4wdUIEo')
	list.append('&youtube_pl=PL9HOq0cGCaCQKoh6dWz1N3s9_H7HjxA5o')
	list.append('&youtube_pl=PLxD46bIwUSnGBok3QJzd1PY6WkSiYfgKB')
	list.append('&youtube_pl=PL0pF26S5a5KD1NcL1zbMrlV7qqj4ro6iw')
	list.append('&youtube_pl=PL8rWKwqFW1l0opYCffj6A4EPi0kgobTuz')
	addDir(addonString(30180).encode('utf-8'),list,17,'http://naturerandom.com/wp-content/uploads/2014/06/the-17-nature-places-to-see-before-they-disappear-forever-6.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30180).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''אוקינוסים'''
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
	addDir(addonString(30181).encode('utf-8'),list,17,'http://www.startau.co.il/uploads/Articles/Article_68_280420131143_1529886926.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30181).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://awesomeocean.com/wp-content/uploads/2014/09/Flat-Ocean.jpeg"))
 
	'''כדור הארץ'''
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
	addDir(addonString(30105).encode('utf-8'),list,17,'http://orig14.deviantart.net/3632/f/2008/151/4/a/the_planet_earth_by_technoking.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30182).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''תופעות ואסונות טבע'''
	list = []
	list.append('&youtube_id=x-rIe1sCJU4')
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
	addDir(addonString(30183).encode('utf-8'),list,17,'https://wallpaperscraft.com/image/northern_lights_aurora_borealis_uk_2015_100946_800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30183).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
 
	CATEGORIES10103A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES102(name, iconimage, desc, fanart):
	'''חלל'''
	background = 102
	
	CATEGORIES_RANDOM(background,fanart)
	
	'''חיפוש'''
	addDir('-' + localize(137),'Space Docu',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES102Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''אסטרונאוטים'''
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
	addDir(addonString(30204).encode('utf-8'),list,17,'http://www.blt.co.uk/wp-content/uploads/2015/12/Astronauts_Nigeria_.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30204).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''אסטרונומיה'''
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
	addDir(addonString(30203).encode('utf-8'),list,17,'http://www.wall321.com/thumbnails/detail/20120615/outer%20space%20stars%20nebulae%201920x1200%20wallpaper_www.wall321.com_24.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30203).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''חקר החלל'''
	list = []
	list.append('&youtube_ch=UC7DeQ1bhSunszQ3JQ-25WiA/playlists')
	list.append('&youtube_id=tMVDWvHlrRc')
	list.append('&youtube_id=htOtW0pD92Y')
	list.append('&youtube_id=_P57CbtAVE0')
	list.append('&youtube_id=KyKvr_7fNWc')
	list.append('&youtube_id=ZtaKWt26dNs')
	list.append('&youtube_id=GVTm0loi9OY')
	list.append('&youtube_id=dyyOcL5tn7k')
	addDir(addonString(30201).encode('utf-8'),list,17,'https://wallpaperscraft.com/image/nebula_universe_space_stars_105874_800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30201).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''טלסקופ החלל האבל'''
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
	addDir(addonString(30202).encode('utf-8'),list,17,'http://2.bp.blogspot.com/-epZUsCIzQuY/T18MYajib8I/AAAAAAAAAb4/9Z6xk2nj8Vk/s1600/Space-Wallpaper.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30202).encode('utf-8')),'1',0,getAddonFanart(background, custom="http://infossible.com/infosdata/wp-content/uploads/2015/08/Earth-From-Space-Space-1080x1920.jpg"))
		
	'''eso'''
	addon = 'plugin.video.eso'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30205).encode('utf-8'),'plugin://'+addon,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''ESA'''
	addon = 'plugin.video.esa'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30206).encode('utf-8'),'plugin://'+addon,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))

	CATEGORIES102A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES103(name, iconimage, desc, fanart):
	'''------------------------------
	---History-----------------------
	------------------------------'''
	background = 103
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir('-' + localize(137),'History Docu',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES103Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

	'''History Channel'''
	list = []
	list.append('&youtube_ch=historychannel')
	list.append('&youtube_pl=PLx5B22t2Ksu2jerdLdWvZ1JuYizKsnnzr')
	list.append('&youtube_pl=PLonoXswioCfuGeOm4jbD_P6dF3BbMbsti')
	list.append('&youtube_pl=PLMZhrNNj_z5tnKucoERFbWHB1zPoCHvYG')
	list.append('&youtube_pl=PLdKcwrFSzUrQQN9iPssQ_0JDOEE2K1c_D')
	list.append('&youtube_pl=PLNgZMT5s0l7F6Hr3wWjX6haqDNbjWzIIa')
	list.append('&youtube_pl=PLACB85DD0818A69A8')
	list.append('&youtube_pl=PLAHSKcwF7IuoAlecwFFfOkyJvQZvFTEh5')
	list.append('&youtube_pl=PLJQnz1qx0QxZNT7KQKC9L95-Wt1ZQ-gaT')
	list.append('&youtube_pl=PL5CFDF24A6CB53CD6')
	addDir(addonString(30300).encode('utf-8'),list,17,'http://download.1wallpaper.net/20150329/the-history-channel-logo-design-black-background-800x600.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30300).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	
	'''World Wars'''
	list = []
	list.append('&youtube_ch=TheGreatWar')
	list.append('&youtube_pl=PLC-0e1pjuxF9bc8e0cDsmj0tqGJ0Ss8tT')
	list.append('&youtube_pl=PL-b6BqXQgEFo88XFZ2r-DQmN-c5W5W9u-')
	list.append('&youtube_pl=PL7eLCXTvueOvs67EDHnuKr7aXguRyuJ0S')
	list.append('&youtube_pl=PLu7g1OfsO2vcKnzSXQiCHisyUIQcclbxr')
	list.append('&youtube_pl=PL95DD3A12BDB77AF0')
	list.append('&youtube_pl=PLACB85DD0818A69A8')
	list.append('&youtube_pl=PLCA467ED9C59E9D8D')
	list.append('&youtube_pl=PLkJloWOsgyNlKNx-LhoAp50o5gqn5d8rp')
	list.append('&youtube_pl=PLHbgAq4l2Bj7AwVk7R1SIuhqtki7fPLUL')
	list.append('&youtube_pl=PL8dPuuaLjXtNjasccl-WajpONGX3zoY4M')
	list.append('&youtube_pl=PL6oforB7ir5JDZaxy6017UJM-cvC-CpKy&index=1')
	addDir(addonString(30301).encode('utf-8'),list,17,'http://cdn.usborne.com/catalogue/covers/eng/width_223px/87886.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30301).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	

	'''Historical armies'''
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
	addDir(addonString(30302).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/d/d0/History_channel_military.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30302).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''Exodus Movies'''
	addon = 'plugin.video.exodus'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	url = '&activatewindow=plugin://plugin.video.exodus/?action=movies&url=http%3a%2f%2fwww.imdb.com%2fsearch%2ftitle%3ftitle_type%3dfeature%2ctv_movie%26languages%3den%26num_votes%3d100%2c%26release_date%3ddate%5b730%5d%2cdate%5b30%5d%26genres%3dhistory%26sort%3dmoviemeter%2casc%26count%3d40%26start%3d1'
	addDir('Exodus Movies',url,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))

	'''Exodus TV shows'''
	addon = 'plugin.video.exodus'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	url = '&activatewindow=plugin://plugin.video.exodus/?action=tvshows&url=http%3a%2f%2fwww.imdb.com%2fsearch%2ftitle%3ftitle_type%3dtv_series%2cmini_series%26release_date%3d%2cdate%5b0%5d%26genres%3dhistory%26sort%3dmoviemeter%2casc%26count%3d40%26start%3d1'
	addDir('Exodus TV shows',url,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))

	CATEGORIES103A(name, iconimage, desc, fanart) #עמוד הבא
		
def CATEGORIES104(name, iconimage, desc, fanart):
	'''------------------------------
	---Science-----------------------
	------------------------------'''
	background = 104
	
	CATEGORIES_RANDOM(background,fanart)
	'''חיפוש'''
	addDir('-' + localize(137),'Science Docu',3,featherenceserviceicons_path + 'se.png',addonString_servicefeatherence(32416).encode('utf-8') % (name),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES104Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה

	addon = 'plugin.video.ted.talks'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(addonString(30400).encode('utf-8'),'plugin://'+addon,8,thumb,plot,addon,0, getAddonFanart(background, default=fanart, custom=""))
	
	'''טכנולוגיה'''
	addDir(addonString(30403).encode('utf-8'),'',10403,'http://kommercialize.com/wp-content/uploads/2013/02/iStock_000020426012Small.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30403).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''מדעי החברה והרוח'''
	addDir(addonString(30401).encode('utf-8'),'',10401,'http://2.bp.blogspot.com/-NvLKmKXYxIo/UTfqXTdoYTI/AAAAAAAAGSY/f3q1fXoIxHE/s1600/Social+influence.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30401).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''מדעי הטבע'''
	addDir(addonString(30402).encode('utf-8'),'',10402,'http://www.memrise.com/s3_proxy/?f=uploads/mems/2495464000130417092533.jpeg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30402).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''מחקרים'''
	list = []
	list.append('&youtube_pl=PLtSuKq2ke_sm8yCeOhOs-yaYgEyVIKXxt')
	list.append('&youtube_pl=PLtSuKq2ke_snSo4WimGOrlquJc8r7Tq7u')                        
	list.append('&youtube_pl=PLtSuKq2ke_skIPkapVG8PLBUmIOSgPlkS')
	list.append('&youtube_pl=PLtSuKq2ke_slVxQS0sqeYVoLkmP74Y4gW')
	list.append('&youtube_pl=PLtSuKq2ke_sn4qo5px_i1jZNVDzz47PVJ')
	list.append('&youtube_pl=PLtSuKq2ke_smyz5y_v6N36MfT5dgA4ORB')
	list.append('&youtube_pl=PLtSuKq2ke_sn4qo5px_i1jZNVDzz47PVJ')
	list.append('&youtube_pl=PLtSuKq2ke_smyz5y_v6N36MfT5dgA4ORB')
	addDir(addonString(30404).encode('utf-8'),list,17,'https://www.colourbox.com/preview/4178295-scientific-research.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30404).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
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
	addDir(addonString(30405).encode('utf-8'),list,17,'http://1.bp.blogspot.com/-CqEGzAVgHsM/T3cAXa6qyxI/AAAAAAAAAnU/RJiWpn8rM0k/s1600/light_double_slit_experiment.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30405).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES104A(name, iconimage, desc, fanart) #עמוד הבא
	
def CATEGORIES10401(name, iconimage, desc, fanart):
	'''------------------------------
	---social science-----------------
	------------------------------'''
	background = 10401
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10401Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''ארכיטקטורה'''
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
	addDir(addonString(30424).encode('utf-8'),list,17,'http://www.datavisualizationtools.biz/wp-content/uploads/2015/09/architecture-modern-atlanta-modern-architecture-architecture-atlanta-architecture.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30424).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''גאוגרפיה'''
	list = []
	list.append('&youtube_pl=PL67F390EB9FE9F4F0')
	list.append('&youtube_pl=PLR7XO54Pktt8_jNjAVaunw1EqqcEAdcow')
	list.append('&youtube_pl=R719mLoDLaQ&list=PLD985DC24042D71ED')
	list.append('&youtube_pl=PL3RbLxbjtXdmyirZPUqrKKWrSjGlfwqRc')
	list.append('&youtube_pl=PLzW2SWgVnP9t9VP7q65cy7Zg3o9DudTUx')
	list.append('&youtube_pl=PL71HsN_LrZoA-Suz9mznJktPqwHVMQRX0')
	list.append('&youtube_pl=PLdAwJqwLRJOHCEeJwJipe24G1-6YYwSLd')
	list.append('&youtube_pl=PLVeXbgaZS8ge9SQwQK47meZbUGA0I-RwX')
	addDir(addonString(30423).encode('utf-8'),list,17,'http://wallpaperbeta.com/wallpaper_800x600/map_of_the_world_geographical_geography_800x600_hd-wallpaper-330201.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30423).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''ניסויים חברתיים'''
	list = []
	list.append('&youtube_pl=PLrb5XV0d1JsJAR-kAmDuyFyn6AUyDTKNH')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PLrb5XV0d1JsJnrEjivD-G1UbxB4q0hcNq')
	list.append('&youtube_pl=PLrb5XV0d1JsLyXjrm5meM3mnSI0PopLdv')
	addDir(addonString(30420).encode('utf-8'),list,17,'http://www.slidecage.com/wp-content/uploads/2007/08/sliders_800x600_arturo-lecture.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30420).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''סוציולוגיה'''
	list = []
	list.append('&youtube_pl=PLiyEC8E9r_ymK3Ps3DbXtzn9NDt9b47PY')
	list.append('&youtube_pl=PLiyEC8E9r_yltRbrb3lKnf-wuvsxUq1w6')
	list.append('&youtube_pl=PLiyEC8E9r_ymDhossOXG2t-XXE_G9j_1-')
	list.append('&youtube_pl=PLiyEC8E9r_ymUoLrKtCmVDJyxFyYFl5z2')
	list.append('&youtube_pl=PLP8Ma8K8YxnwiAYGiCMba5yu8swa6a7-V')
	list.append('&youtube_pl=PLT35IWG8lUbYwramdIPMAR5wPbDFjDU0H')
	addDir(addonString(30421).encode('utf-8'),list,17,'http://cdn.yourarticlelibrary.com/wp-content/uploads/2013/09/241.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30421).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''פוליטיקה'''
	list = []
	list.append('&youtube_pl=PL3Ikn3SKdJHgC14x0oUEMJ7pxG_Yj8UNa')
	list.append('&youtube_pl=PLlTLHnxSVuIyeEZPBIQF_krewJkY2JSwi')
	list.append('&youtube_pl=PLeyJPHbRnGaaKyuj1467jFo7gzXqYSPKx')
	list.append('&youtube_pl=PLt-M8o1W_GdQrVQpvLQMJZlprs5MD0imr')
	list.append('&youtube_pl=PLrb5XV0d1JsJQIgr3l1iJtkRjzr1Cgbu8')
	addDir(addonString(30422).encode('utf-8'),list,17,'http://wallpoper.com/images/00/28/25/35/flags-politics_00282535.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30422).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

	'''פילוסופיה'''
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
	addDir(addonString(30425).encode('utf-8'),list,17,'http://www.thegreatcourses.com/media/catalog/product/cache/1/image/800x600/0f396e8a55728e79b48334e699243c07/4/4/4477---base_image_4.1424272096.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30425).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''כלכלה'''
	list = []
	list.append('&youtube_pl=PL6FA614EF0CB2AD82')
	list.append('&youtube_pl=PL8dPuuaLjXtPNZwz5_o_5uirJ8gQXnhEO')
	list.append('&youtube_pl=PLA46DB4506062B62B')
	list.append('&youtube_pl=PL11ADD17785C9C9A4')
	list.append('&youtube_pl=PLE70CA726102FB294')
	list.append('&youtube_pl=PL50F9C4FD0BE8FE28')
	list.append('&youtube_pl=5IDhKM&list=PL54ADCC41A7E439B7')
	list.append('&youtube_pl=5IDhKM&list=PL-9JQaDLOcT5MLi4NdWH7arCY3dEhozFS')
	addDir(addonString(30426).encode('utf-8'),list,17,'http://gazettereview.com/wp-content/uploads/2015/04/march-jobs-report-economic-news.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30426).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''פסיכולוגיה'''
	list = []
	list.append('&youtube_ch=UCYlpMl8sk46MKU9P7XgJpGw/playlists')
	list.append('&youtube_pl=PL8dPuuaLjXtOPRKzVLY0jJY-uHOH9KVU6')
	list.append('&youtube_pl=P3FKHH2RzjI&list=PL6A08EB4EEFF3E91F')
	list.append('&youtube_pl=PL6uC-XGZC7X6xObklmWEk8MbRVm87g0Uu')
	list.append('&youtube_pl=XgRlrBl-7Yg&list=PLFDE868BCF58A3950')
	list.append('&youtube_pl=2fbrl6WoIyo&list=PL44ABC9278E2EE706')
	list.append('&youtube_pl=PLg0JqCtcY-SxZt4kKj0b0OgIZESF46TDP')
	addDir(addonString(30427).encode('utf-8'),list,17,'http://cdn.patch.com/users/22843411/stock/T800x600/20150254e5602e6ff13.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30427).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES10401A(name, iconimage, desc, fanart) #עמוד הבא

def CATEGORIES10402(name, iconimage, desc, fanart):
	'''------------------------------
	---natural sciences-----------------
	------------------------------'''
	background = 10402
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10402Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
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
	addDir(addonString(30431).encode('utf-8'),list,17,'http://cdn.allwallpaper.in/wallpapers/800x600/4746/biology-microscopic-cells-neurons-background-800x600-wallpaper.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30431).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
		
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
	addDir(addonString(30433).encode('utf-8'),list,17,'http://www.wallpaperhi.com/thumbnails/detail/20111217/26.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30433).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
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
	addDir(addonString(30434).encode('utf-8'),list,17,'https://c1.staticflickr.com/9/8230/8384110298_da510e0347_b.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30434).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
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
	addDir(addonString(30430).encode('utf-8'),list,17,'https://lh4.googleusercontent.com/-Glq_hJMk9C8/T3QvhUuGdgI/AAAAAAAAAdQ/iVeLm88VrHY/w800-h800/Magic%2BMath.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30430).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

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
	addDir(addonString(30432).encode('utf-8'),list,17,'http://www.wall321.com/thumbnails/detail/20120913/mathematics%20chalkboards%20equation%20mind%201024x768%20wallpaper_www.wall321.com_79.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30432).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))

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
	addDir(addonString(30435).encode('utf-8'),list,17,'http://wallpaperbeta.com/wallpaper_800x600/tablets_capsule_medicine_macro_800x600_hd-wallpaper-239312.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30435).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
	CATEGORIES10402A(name, iconimage, desc, fanart) #עמוד הבא

def CATEGORIES10403(name, iconimage, desc, fanart):
	'''------------------------------
	---Technology-----------------
	------------------------------'''
	background = 10403
	
	CATEGORIES_RANDOM(background,fanart)
	CATEGORIES10403Z(name, iconimage, desc, background, fanart) #ערוצי טלוויזיה
	
	'''אקראי'''
	list = []
	list.append('&youtube_ch=PLB76E9DFE905DDAC0')
	addDir(addonString(30405).encode('utf-8'),list,17,'http://imgur.com/kcLrrGH.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30008).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	'''אלקטרוניקה'''
	list = []
	list.append('&youtube_pl=PL3C5D963B695411B6')
	list.append('&youtube_pl=PLC8A1AD995AB64055')
	list.append('&youtube_pl=PLFF553CED56CDE25D')
	list.append('&youtube_pl=PL9CDF91EC3585AAD9')
	list.append('&youtube_pl=PLLilrKdbjXDH-ztjsBHZLEpRvKHHP6bgO')
	list.append('&youtube_pl=PL774BE597B77BF3C5')
	addDir(addonString(30453).encode('utf-8'),list,17,'http://www.alsglobal.com/~/media/Images/Divisions/Life%20Sciences/Electronics%20Testing/Electronics%204.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30453).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
    
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
	addDir(addonString(30454).encode('utf-8'),list,17,'http://www.trdparts.jp/english/assets/img/rc-concept.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30454).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://wallpaper.zone/img/1929799.jpg"))
   
	'''מחשבים'''
	list = []
	list.append('&youtube_pl=PL57quI9usf_skTMa14vP58RZxlSjCIJ1P')
	list.append('&youtube_pl=PL57quI9usf_uI8ZxI58Gc5ACnmbL7rxP-')
	list.append('&youtube_pl=PL57quI9usf_so2Apomw8ap8jMm8e2-xTs')
	list.append('&youtube_pl=PL57quI9usf_saUGUzSvs4909pfSaloLHS')
	addDir(addonString(30452).encode('utf-8'),list,17,'http://kaplancomputers.com/wp-content/uploads/2014/04/Happy-Computer.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30452).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://www.hutui6.com/data/out/41/68116264-computers-wallpapers.jpg"))
    
	'''סלולר'''
	list = []
	list.append('&youtube_pl=PL57quI9usf_sKq-un-sKiH28GufDbfXud')
	list.append('&youtube_pl=PL57quI9usf_us0KVzB8aZFPVmdvp1_sIh')
	list.append('&youtube_pl=PLPBN-Ln1bNtxpgyoI2uVTAoD3VqHfe83c')
	list.append('&youtube_pl=PL57quI9usf_ujAfHHeCUHuJDL9rMo2_kr')
	addDir(addonString(30451).encode('utf-8'),list,17,'https://pixabay.com/static/uploads/photo/2012/04/26/12/57/cell-42409_960_720.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30451).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="http://colecellulartyler.com/files/2013/06/157734-1920x10801.jpg"))
    
	'''צבא'''
	list = []
	list.append('&youtube_ch=Mparovios3000')
	list.append('&youtube_ch=epsil2')
	list.append('&youtube_ch=vsbdefense')
	list.append('&youtube_ch=UCXw6jajdMu7tBrpvZqVUAaQ')
	list.append('&youtube_ch=UCzqZWekrxPTL2s8J_UMtS_A')
	addDir(addonString(30456).encode('utf-8'),list,17,'http://www.yadlashiryon.com/VF/ib_items/2025/1.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30456).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom="https://i.ytimg.com/vi/BR3x-MV4neY/maxresdefault.jpg"))

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
	addDir(addonString(30450).encode('utf-8'),list,17,'http://i.imgur.com/bkWkbHH.png',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30450).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
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
	addDir(addonString(30455).encode('utf-8'),list,17,'https://gyulchev.files.wordpress.com/2014/05/robot_blue.jpg',addonString_servicefeatherence(32099).encode('utf-8') % (addonString(30455).encode('utf-8')),'1',0,getAddonFanart(background, default=fanart, custom=""))
	
	CATEGORIES10403A(name, iconimage, desc, fanart) #עמוד הבא
	
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