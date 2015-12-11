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
	addDir(addonString(100).encode('utf-8'),'MyDocu',100,"",addonString(1000).encode('utf-8'),'1',50, getAddonFanart(100, custom="")) #My Docu
	addDir(addonString(101).encode('utf-8'),'',101,'',addonString(1010).encode('utf-8'),'1',50, getAddonFanart(101, custom="")) #Nature
	addDir(addonString(102).encode('utf-8'),'',102,'',addonString(1020).encode('utf-8'),'1',50, getAddonFanart(102, custom="")) #Space
	addDir(addonString(103).encode('utf-8'),'',103,'',addonString(1030).encode('utf-8'),'1',50, getAddonFanart(103, custom="")) #History
	addDir(addonString(104).encode('utf-8'),'',104,'',addonString(1040).encode('utf-8'),'1',50, getAddonFanart(104, custom="")) #Science
	addDir(addonString(107).encode('utf-8'),'',107,'',addonString(1070).encode('utf-8'),'1',50, getAddonFanart(107, custom="")) #Kids
	addDir(addonString(108).encode('utf-8'),'',108,'',addonString(1080).encode('utf-8'),'1',50, getAddonFanart(108, custom="")) #Hebrew Subtitle
	addDir(addonString(109).encode('utf-8'),'',109,'',addonString(1090).encode('utf-8'),'1',50, getAddonFanart(109, custom="")) #TV channels
			
	addon = 'plugin.video.smithsonian'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('HD 1080','plugin://'+addon,8,thumb,plot,addon,58, getAddonFanart(110, custom=""))
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
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
	'''בעלי חיים'''
	addDir(addonString(10101),'',10101,'',addonString(101010),'1',"", getAddonFanart(10101))
		
	'''Animal's'''
	list = []
	list.append('&youtube_id=eH1s9GCqPKo')
	list.append('&youtube_pl=PLNxd9fYeqXeba2Nz4ocWac4hyhJnEACFw')
	list.append('&youtube_pl=PLNxd9fYeqXeYQpcE7LfadSFjUU4E6inZC')
	list.append('&youtube_pl=PL_jFbqOSEqaLIYGS0Oz8jTlrB8PaHiwdp')
	list.append('&youtube_pl=PL66rc6rMkuadKawGwt9pYSq_yVJ1dnsyp')
	list.append('&youtube_pl=PLpHQQspuhgG7qhHOD1HrWklZg458-LQYj')
	list.append('&youtube_pl=PL7GQU9nivpYJpnzAhTH1OB3N6BeQipls_')
	list.append('&youtube_pl=PLd2jr44gFMvBMxFlT0tFxeJqrAYGmpjO1')
	list.append('&youtube_pl=PLsa65XLFLA2-mxUpttawU8AN1TX0VwKpH')
	list.append('&youtube_pl=PLvTrLxXekhJrlt2IY3-Paobg5skAXFIMB')
	list.append('&youtube_pl=PLcOr-eBi9or-I7knKXhhdihMqswzWJ7yo')
	list.append('&youtube_pl=PL3Ea6NwLKoMSArPBNWh-gMgKCX2cmJzCq')
	list.append('&youtube_pl=PL0GL1wmKQPGgOBIHtvwcP3g51_rWqnwBx')
	list.append('&youtube_pl=PL0GL1wmKQPGhnl30h5A2OmyR94N1UkDmB')
	list.append('&youtube_pl=PL0GL1wmKQPGi_eAvRbaBVlae24tVsrGuK')
	list.append('&youtube_pl=PLpYgp0wW8mmZyLCqY415YbjefiazLBHzJ')
	list.append('&youtube_ch=UC3c8nDp-i60gB2wTmUeyQAA')
	list.append('&youtube_pl=PL38WzeWx41gayCgnx5EsqsFAS4lH3XhV5')
	list.append('&youtube_ch=UCvfH62D48X5Bahu-oroIreQ')
	list.append('&youtube_pl=PLvTrLxXekhJrUx5QHSfP6hJuIseU2FY2F')
	list.append('&youtube_pl=PL3Ea6NwLKoMSArPBNWh-gMgKCX2cmJzCq')
	list.append('&youtube_pl=PLoUUkpYUScvJb2li_PY6c9fu_A3IlJKiT')
	list.append('&youtube_pl=PLWWOl-2iqjMb2UljVPPhQQy6SJJ3E-7gK')
	list.append('&youtube_pl=PLezpCwYgD_yvNYNXZlDM6z3mpuTQYgjUs')
	list.append('&youtube_ch=PLHtNpWbpKrdgTnYZDyTKpZNyBStsVyNK-')
	list.append('&youtube_pl=PLfAToAFYpTfuHlcsmO-hiYcpp1yrrP10y')
	list.append('&youtube_ch=UCaL6Fn_Exyfe2tzBMI4cHVw')
	addDir("Animal's",list,17,'','','1',"", getAddonFanart(background, custom=""))
 
	'''Dogtv'''
	list = []
	list.append('&youtube_ch=DOGTVWORLD')
	list.append('&youtube_id=BTKo1M-QzSc')
	list.append('&youtube_pl=PLjXkouFJLKB2fBgsHcpOMTqt-cExph4RK')
	list.append('&youtube_pl=PLjXkouFJLKB3jeq_W_wBZnyZe4q-rLDKL')
	addDir('Dogtv',list,17,'','','1',"", getAddonFanart(background, custom=""))
 
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
	addDir('DOG WHISPERER',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''צומח'''
	addDir(addonString(10102),'',10102,'',addonString(101020),'1',"", getAddonFanart(10102))
	
		
	'''Plant's'''
	list = []
	list.append('&youtube_ch=DOGTVWORLD')
	list.append('&youtube_id=eH1s9GCqPKo')
	list.append('&youtube_pl=PLgKYsEYF9_QCxM_29RC6euEJLvaHFOdrJ')
	list.append('&youtube_pl=PLs7Y2nGwfz4FL4ZJgONHsl1qp-AZPr3tJ')
	list.append('&youtube_pl=PLh8cmtKf7uVnEKm-YiByTebR3bdyOV_XV')
	list.append('&youtube_pl=PL7fxIatI1SNjeZZ8yzoyKX2b3LihqLJzs')
	list.append('&youtube_pl=PLolk0MpPk5HYNPHfb3tnSh6gSDjuGIPIv')
	list.append('&youtube_pl=PLFSXLuczIM61o8GJ_kA9UoXbbIsLXD5hS')
	list.append('&youtube_pl=PLYpOT73IUzMkKNkgQS-uGOISuOS207BL-')
	addDir("Plant's",list,17,'','','1',"", getAddonFanart(background, custom=""))
 
	'''מקומות'''
	addDir(addonString(10103),'',10103,'',addonString(101030),'1',"", getAddonFanart(10103))
	'''natural places'''
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
	
	'''ocean's'''
	list = []
	list.append('&youtube_ch=DOGTVWORLD')
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
	addDir("ocean's",list,17,'','','1',"", getAddonFanart(background, custom=""))
 
 
	addDir('natural places',list,17,'','','1',"", getAddonFanart(background, custom=""))

	'''BBC Earth channel'''
	addDir('BBC Earth','BBCEarth',9,'','','1',"", getAddonFanart(background, custom=""))

	 
	'''Nat Geo WILD channel'''
	addDir('Nat Geo WILD','NatGeoWild',9,'','','1',"", getAddonFanart(background, custom=""))

	
	'''Animal Planet Channel'''
	addDir('Animal Planet Channel','AnimalPlanetTV',9,'','','1',"", getAddonFanart(background, custom=""))
	

	
	
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
	addDir('natural phenomena and disasters',list,17,'','','1',"", getAddonFanart(background, custom=""))
 

	

	
	
 

def CATEGORIES10101(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-ANIMALS----------------
	------------------------------'''
	
def CATEGORIES10102(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-PLANTS-----------------
	------------------------------'''
	
def CATEGORIES10103(name, iconimage, desc, fanart):
	'''------------------------------
	---NATURE-PLACES-----------------
	------------------------------'''
		
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
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))


	'''youtube space channels'''
	list = []
	list.append('&youtube_ch=NASAtelevision')
	list.append('&youtube_ch=spacelab')
	list.append('&youtube_ch=VideoFromSpace')
	list.append('&youtube_ch=UC7_gcs09iThXybpVgjHZ_7g')
	list.append('&youtube_ch=scishowspace')
	addDir("youtube space channel's",list,17,'','','1',"", getAddonFanart(background, custom=""))
 
	'''Space and Universe'''
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
	addDir("Space and Universe",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''------------------------------
	---art&visual arts----------------
	------------------------------'''


	'''markcrilley Channel'''
	addDir('markcrilley','markcrilley',9,'','','1',"", getAddonFanart(background, custom=""))

	'''PESfilm Channel'''
	addDir('Crash Course Kids Channel','crashcoursekids',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''WilliamsShamir Channel'''
	addDir('WilliamsShamir Channel','WilliamsShamir',9,'','','1',"", getAddonFanart(background, custom=""))

	'''ChrisSamba22 Channel'''
	addDir('ChrisSamba22 Channel','ChrisSamba22',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''EclecticAsylumArt Channel'''
	addDir('EclecticAsylumArt Channel','EclecticAsylumArt',9,'','','1',"", getAddonFanart(background, custom=""))

	'''idrawgirls Channel'''
	addDir('idrawgirls  Channel','idrawgirls/',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''daarken Channel'''
	addDir('daarken Channel','daarken',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Crash Course Kids Channel'''
	addDir('Crash Course Kids Channel','crashcoursekids',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''3dsMaxHowTos Channel'''
	addDir('3dsMaxHowTos Channel','3dsMaxHowTos',9,'','','1',"", getAddonFanart(background, custom=""))

	'''revolutions34 Channel'''
	addDir('revolutions34 Channel','crashcoursekids',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''CGArtSuccess Channel'''
	addDir('CGArtSuccess Channel','CGArtSuccess',9,'','','1',"", getAddonFanart(background, custom=""))

	'''bluefley00 Channel'''
	addDir('bluefley00  Channel','bluefley00 ',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''bedavelli Channel'''
	addDir('bedavelli Channel','bedavellis',9,'','','1',"", getAddonFanart(background, custom=""))

	'''arieldiaz3d Channel'''
	addDir('arieldiaz3d Channel','arieldiaz3d',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Arenovalis Channel'''
	addDir('Arenovalis Channel','Arenovalis',9,'','','1',"", getAddonFanart(background, custom=""))

	
	
	'''iceblazer17 Channel'''
	addDir('iceblazer17 Channel','iceblazer17',9,'','','1',"", getAddonFanart(background, custom=""))

	'''AlexanderKoshelkov Channel'''
	addDir('AlexanderKoshelkov Channel','AlexanderKoshelkov',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''tate Channel'''
	addDir('tate Channel','tate',9,'','','1',"", getAddonFanart(background, custom=""))
	
		
	'''smarthistoryvideos Channel'''
	addDir('smarthistoryvideos Channel','smarthistoryvideos',9,'','','1',"", getAddonFanart(background, custom=""))

	'''guggenheim Channel'''
	addDir('guggenheim Channel','guggenheim',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''MoMAvideos Channel'''
	addDir('SciShow Kids Channel','scishowkids',9,'','','1',"", getAddonFanart(background, custom=""))

	'''TheArtistsPlace Channel'''
	addDir('TheArtistsPlace Channel','UCLCHcL4M0xSwPeEuKGrsGkg',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''TattooWoo Channel'''
	addDir('SciShow Kids Channel','scishowkids',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Sycra Channel'''
	addDir('Sycra Kids Channel','Sycra',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	
	
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
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))

	
	'''youtube history channel's'''
	list = []
	list.append('&youtube_ch=UCQGjxZRfQ8Bt6rnudw2kgUQ')
	list.append('&youtube_ch=UCErKUCncCyBgEdxWAtrj5hg')
	list.append('&youtube_ch=AlternateHistoryHub')
	list.append('&youtube_ch=UC5xIAFuCs4m2S4uPY9dp_Ww')
	list.append('&youtube_ch=BlastfromthePast')
	list.append('&youtube_ch=TheGreatWar')
	addDir("youtube history channel's",list,17,'','','1',"", getAddonFanart(background, custom=""))


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
	addDir("History Channel",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
        '''History '''
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
	addDir("History Channel",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	
	
	
	
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
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
	addon = 'plugin.video.ted.talks'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir('TED','plugin://'+addon,8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	


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
	addDir("youtube science channel's",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''מתמטיקה'''
	list = []
	list.append('&youtube_pl=-PL_7F0HR2FSAqlAmhi3HAASthdwFaPT1mf')
	list.append('&youtube_pl=PLUl4u3cNGP63ctJIEC1UnZ0btsphnnoHR')
	list.append('&youtube_pl=PL204B0C2C2F48DF2A')
	list.append('&youtube_pl=-PL55C7C83781CF4316')
	list.append('&youtube_pl=PL3o9D4Dl2FJ8zkoLxaO4aKlq2JsKsz365')
	list.append('&youtube_pl=geW-geF5fa4')
	addDir('מתמטיקה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
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
	addDir('ניסויים מדעיים',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''רובוטיקה'''
	list = []
	list.append('&youtube_id=-nOolOVw118')
	list.append('&youtube_id=Bm6LzaxTX44')
	list.append('&youtube_id=geW-geF5fa4')
	addDir('רובוטיקה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''100 Greatest Discoveries'''
	list = []
	list.append('&youtube_pl=PLDeln0BXcz6qr7wn_s7vtCedOE67eN-e7')
	addDir('100 Greatest Discoveries',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	
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

	'''SciShow Kids Channel'''
	addDir('SciShow Kids Channel','scishowkids',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Crash Course Kids Channel'''
	addDir('Crash Course Kids Channel','crashcoursekids',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Kids Animal Channel'''
	addDir('Kids Animal Channel','KidsAnimalChannel',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Crash Course Kids Channel'''
	addDir('Crash Course Kids Channel','crashcoursekids',9,'','','1',"", getAddonFanart(background, custom=""))

	'''makemegenius Channel'''
	addDir('makemegenius Channel','makemegenius',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Smart Learning for All Channel'''
	addDir('Smart Learning for All Channel','Smartlearningforall',9,'','','1',"", getAddonFanart(background, custom=""))

	'''space and planet for kids'''
	list = []
	list.append('&youtube_id=-xKKzIoJgMSQ')
	list.append('&youtube_pl=PLRkXn_ayyCS8kOR-EKAbWx5hS_YUBEo5')
	list.append('&youtube_pl=PLwmqN2cDkUGtn_gPHUpPfLwWF3Sp9BS3R')
	addDir('space and planet for kids',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''planets for kids'''
	list = []
	list.append('&youtube_pl=PLy0B6ncmGtqd-wb1Iqh036p3l9ZN4OCZ0')
	list.append('&youtube_pl=PLlKRPDYgEh4xRq0AYTCwWduDmhq1yFPHY')
	list.append('&youtube_pl=PL2Zef9KQGytUntJegeTmJxAFlIkaTRo-P')
	list.append('&youtube_pl=PLfo1kYEnYLcJ-UhenL0Yf3afIR3zw7fr2')
	list.append('&youtube_pl=PLeUPs98mdCOLKpvPU8tr1-1rgJ1h_xgxA')
	list.append('&youtube_pl=PLwmqN2cDkUGtn_gPHUpPfLwWF3Sp9BS3R')
	addDir('planets for kids',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	

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
	addDir(localize(590),list,17,'https://cdn3.iconfinder.com/data/icons/flat-icons-web/40/Random-512.png',"",'1',"", getAddonFanart(background, custom=""))
	
	'''אפריקה - הסרנגטי'''
	list = []
	list.append('&youtube_id=Md3BQG4oWDU')
	addDir('אפריקה - הסרנגטי',list,17,'','','1',"", getAddonFanart(background, custom=""))
					
	'''הסוד הכמוס של אפריקה'''
	list = []
	list.append('&youtube_id=jC5iaonGRCg')
	addDir('הסוד הכמוס של אפריקה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''סיפורים מהסוואנה'''
	list = []
	list.append('&youtube_id=4pBLynGT5ZA')
	addDir('סיפורים מהסוואנה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	

	'''בית -home'''
	list = []
	list.append('&youtube_id=NEnRsTlSsxM')
	addDir('בית -home',list,17,'','','1',"", getAddonFanart(background, custom=""))
		
	'''ההסטוריה של העולם בשעתיים'''
	list = []
	list.append('&youtube_id=HZzSLaqk2dA')
	addDir('ההסטוריה של העולם בשעתיים',list,17,'','','1',"", getAddonFanart(background, custom=""))
		
	'''טבע ישראלי'''
	list = []
	list.append('&youtube_pl=PL1PXZ56eQG-SGcBGlBXuokGz8O0Iogpzs')
	list.append('&youtube_pl=PL762D7FD5B70D28C0')
	addDir('טבע ישראלי',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''דוקו קירשנבאום -קוסטה ריקה'''
	list = []
	list.append('&youtube_id=YMfg06-1zec')
	addDir('דוקו קירשנבאום -קוסטה ריקה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
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
	addDir('הסטוריה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''אילוף כלבים'''
	addDir('אילוף כלבים','Orenadika73',9,'','','1',"", getAddonFanart(background, custom=""))

	'''ערוץ הגיון ומדע'''
	addDir('ערוץ הגיון ומדע','ScienceReasonIsrael',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''חיות בספארי'''
	list = []
	list.append('&youtube_pl=PL43AC3544C5E17BEF')
	addDir('חיות בספארי',list,17,'','','1',"", getAddonFanart(background, custom=""))

	
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
	addDir('חיות פראיות ',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''קטנטנים בטבע'''
	list = []
	list.append('&youtube_id=J1JIHh1ZEf0')
	addDir('קטנטנים בטבע',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''בעלי חיים לילדים ופעוטות'''
	list = []
	list.append('&youtube_id=QcANPfq5V7g')
	addDir('בעלי חיים לילדים ופעוטות',list,17,'','','1',"", getAddonFanart(background, custom=""))
		
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
	addDir('גלילאו',list,17,'','','1',"", getAddonFanart(background, custom=""))
		
	'''היה היה'''
	list = []
	list.append('&youtube_pl=PLF487E714444A3272')
	list.append('&youtube_pl=PL2E6FC61CB0B4C510')
	list.append('&youtube_pl=PLEB6F71190B2A83D1')
	list.append('&youtube_pl=PL19F750D7137E32A2')
	list.append('youtube_id=TLT7tM6ZxLc')
	addDir('היה היה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''עולם החיות של הופ'''
	list = []
	list.append('&youtube_id=l3fXEyLWCzI')
	addDir('עולם החיות של הופ',list,17,'','','1',"", getAddonFanart(background, custom=""))
			
	
	'''החפרנים'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj6PWe7kECdyz6ToCjcmSd6z')
	list.append('&youtube_pl=PLth1a195qHsi9fsrgjDzYTzqKSOF-Ky-N')
	addDir('החפרנים',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''להיות מדען עם פרופסור דן'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4oR5aIC0Ru5JZA1a1TT-RN')
	addDir('להיות מדען עם פרופסור דן',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''מה זה מוזה'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj4F8EkY07BfV1KhdjmtjX0P')
	addDir('מה זה מוזה',list,17,'','','1',"", getAddonFanart(background, custom=""))

	'''מה זה מוזה במעבדה'''
	list = []
	list.append('&youtube_pl=PL51YAgTlfPj59VvVLjLaAiGbFjbqv7sh3')
	addDir('דוקו קירשנבאום -קוסטה ריקה',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''2מה זה מוזה במעבדה'''
	list = []
	list.append('&youtube_pl=PLth1a195qHsj20lXv4QqTQ7kb2RLoGxY8')
	addDir( '2מה זה מוזה במעבדה ',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''שירים לילדים בנושא חיות'''
	list = []
	list.append('&youtube_id=jMIELC0KFs4')
	addDir('שירים לילדים בנושא חיות',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''חיות בערוץ לולי'''
	list = []
	list.append('&youtube_pl=PLTleo-h9TFqI2CFuWeFA-Q2Bu3BBHdXqv')
	addDir('חיות בערוץ לולי',list,17,'','','1',"", getAddonFanart(background, custom=""))

	'''לולי אוהב חיות'''
	list = []
	list.append('&youtube_id=gO9hyX4s1ko')
	addDir('לולי אוהב חיות',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	addon = 'plugin.video.seretil'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(342) + space + '1','plugin://'+addon+'/?iconimage=http%3a%2f%2fimages.nationalgeographic.com%2fwpf%2fsites%2fcommon%2fi%2fpresentation%2fNGLogo560x430-cb1343821768.png&mode=4&name=%d7%a0%d7%a9%d7%99%d7%95%d7%a0%d7%9c%20%d7%92%d7%90%d7%95%d7%92%d7%a8%d7%a4%d7%99%d7%a7&url=http%3a%2f%2fseretil.me%2fcategory%2f%25D7%25A0%25D7%25A9%25D7%2599%25D7%2595%25D7%25A0%25D7%259C-%25D7%2592%25D7%2599%25D7%2590%25D7%2595%25D7%2592%25D7%25A8%25D7%25A4%25D7%2599%25D7%25A7%2fpage1%2f',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.movixws'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(342) + space + '2','plugin://'+addon+'/?description&iconimage=http%3a%2f%2ficons.iconarchive.com%2ficons%2faaron-sinuhe%2ftv-movie-folder%2f512%2fDocumentaries-National-Geographic-icon.png&mode=2&name=Documentary%20-%20%d7%93%d7%95%d7%a7%d7%95%d7%9e%d7%a0%d7%98%d7%a8%d7%99&url=http%3a%2f%2fwww.movix.me%2fgenres%2fDocumentary',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
	addon = 'plugin.video.sdarot.tv'
	thumb, fanart, summary, description, plot = getAddonInfo(addon)
	addDir(localize(20343) + space + '1','plugin://'+addon+'/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f11%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&name=%d7%94%d7%99%d7%a1%d7%98%d7%95%d7%a8%d7%99%d7%94&summary&url=all-heb',8,thumb,plot,addon,50, getAddonFanart(110, custom=""))
	
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
