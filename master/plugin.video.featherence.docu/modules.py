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
	
	'''BBC Earth channel'''
	addDir('BBC Earth','BBCEarth',9,'','','1',"", getAddonFanart(background, custom=""))

	 
	'''Nat Geo WILD channel'''
	addDir('Nat Geo WILD','NatGeoWild',9,'','','1',"", getAddonFanart(background, custom=""))

	
	'''Animal Planet Channel'''
	addDir('Animal Planet Channel','AnimalPlanetTV',9,'','','1',"", getAddonFanart(background, custom=""))
	
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
	
	
	'''אריות'''
	list = []
	list.append('&youtube_id=r0RCYUa3Kbg')
	list.append('&youtube_id=fjNjEREV8j0')
	addDir('אריות',list,17,'http://www.gocool.co.il/home/safari/marapic/120.jpg','אריה הוא מין של טורף גדול מהסוג פנתר שבמשפחת החתוליים, והוא השני בגודלו במשפחה זו אחרי תת-המין הסיבירי של הטיגריס.','1',"", getAddonFanart(background, custom="http://blogs-images.forbes.com/jimdobson/files/2015/07/tt-editors-picks-2273-man-pays-55-000-to-shoot-kill-cecil-the-lion-large.thumb_.jpg"))
	
	'''World's Deadliest-החיות הקטלניות בעולם'''
	list = []
	list.append('&youtube_pl=PLNxd9fYeqXeba2Nz4ocWac4hyhJnEACFw')
	addDir("World's Deadliest-החיות הקטלניות בעולם",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''World's Weirdest-החיות המוזרות בעולם'''
	list = []
	list.append('&youtube_pl=PLNxd9fYeqXeYQpcE7LfadSFjUU4E6inZC')
	addDir("World's Weirdest-החיות המוזרות בעולם",list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''Wild Russia HD'''
	list = []
	list.append('&youtube_pl=PLR1CNcQmgvMlowMRAo2SjCLBKzibJq0Y5')
	addDir('Wild Russia HD',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''Islands HD'''
	list = []
	list.append('&youtube_pl=PLql7ZywaMwm2ugmP5-rIjUOvly5kqBV7J')
	addDir('Nat Geo Wild HD Islands',list,17,'','','1',"", getAddonFanart(background, custom=""))

	
		
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

	'''NASA channel'''
	addDir('NASA','NASAtelevision',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''Scientific American Space Lab channel'''
	addDir('Scientific American Space Lab','spacelab',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Space.com channel'''
	addDir('AlternateHistoryHub channel','VideoFromSpace',9,'','','1',"", getAddonFanart(background, custom=""))
	
   	'''PBS Space Time channel'''
	addDir('PBS Space Time channel','UC7_gcs09iThXybpVgjHZ_7g',9,'','','1',"", getAddonFanart(background, custom=""))

	
   	'''SciShow Space channel'''
	addDir('SciShow Space channel','scishowspace',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Space and Universe'''
	list = []
	list.append('&youtube_pl=PLplagMMHBe3VDYwsYiz8sDwcfPdtlP3Kk')
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
	
	cgoodswen
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

	'''History TV channel'''
	addDir('History TV','UCQGjxZRfQ8Bt6rnudw2kgUQ',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''HipHughes History channel'''
	addDir('HipHughes History channel','UCErKUCncCyBgEdxWAtrj5hg',9,'','','1',"", getAddonFanart(background, custom=""))

	'''AlternateHistoryHub channel'''
	addDir('AlternateHistoryHub channel','AlternateHistoryHub',9,'','','1',"", getAddonFanart(background, custom=""))

	
	'''History Channel Documentary'''
	addDir('History Channel Documentary','UC5xIAFuCs4m2S4uPY9dp_Ww',9,'','','1',"", getAddonFanart(background, custom=""))


	'''IT'S HISTORY channel'''
	addDir("IT'S HISTORY channel",'BlastfromthePast',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''The GREAT WAR channel'''
	addDir('The GREAT WAR','TheGreatWar',9,'','','1',"", getAddonFanart(background, custom=""))


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
	

	'''veritasium'''
	list = []
	list.append('&youtube_id=NddZ5ftQb0Q')
	addDir('veritasium',list,17,'','','1',"", getAddonFanart(background, custom=""))
	
	'''veritasium channel'''
	addDir('veritasium Channel','1veritasium',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''Smarter Every Day channel'''
	addDir('Smarter Every Day Channel','UC6107grRI4m0o2-emgoDnAA',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''vsauce channel'''
	addDir('vsauce Channel','vsauce',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''C.G.P.Grey Channel'''
	addDir('C.G.P.Grey Channel','CGPGrey',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''Asap SCIENCE Channel'''
	addDir('Asap SCIENCE Channel','AsapSCIENCE',9,'','','1',"", getAddonFanart(background, custom=""))

	'''SciShow Channel'''
	addDir('SciShow Channel','scishow',9,'','','1',"", getAddonFanart(background, custom=""))
	

	'''CrashCourse Channel'''
	addDir('CrashCourse Channel','crashcourse',9,'','','1',"", getAddonFanart(background, custom=""))

	'''numberphile Channel'''
	addDir('numberphile Channel','numberphile',9,'','','1',"", getAddonFanart(background, custom=""))
	
	'''YouTube EDU Channel'''
	addDir('numberphile Channel','education',9,'','','1',"", getAddonFanart(background, custom=""))

	'''Gross Science Channel'''
	addDir('Gross Science Channel','grossscienceshow',9,'','','1',"", getAddonFanart(background, custom=""))
	
	
	'''Periodic Videos Channel'''
	addDir('Periodic Videos Channel','periodicvideos',9,'','','1',"", getAddonFanart(background, custom=""))
	
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
