# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''
	
def CATEGORIES101A(General_LanguageL, background): #אקראי שירים וסיפורים
	'''אקראי'''
	list = []
		
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCfm5IpcgGCooON4Mm2vq40A/playlists')
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=wallavod&name=%d7%a9%d7%99%d7%a8%d7%99%d7%9d%20(19)&url=genre%3dkids%26genreId%3d7450')
		list.append('&youtube_id=6LNpGsYpWJw') #שירי ילדים
		list.append('&youtube_id=YtuVAZyWoG4') #שירי ילדים ופעוטות ברצף
		list.append('&youtube_pl=PLFw7KwIWHNB1_mXvYXwqFOw6S026LL3tj')
		list.append('&youtube_pl=PLF11AD94724D37E02')
		list.append('&youtube_pl=PL0495C8F5A2024FA4')
		list.append('&youtube_pl=PLCA955BD31C5CA512') #שירי דיסני
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLDt4VQajKv8w3VEaYG7Imqtgwmt1y2aJ8') #English
		list.append('&youtube_pl=PLOJVlm6BAdVuneDJhqmF4Q7a1WVeZO96v') #English
		list.append('&youtube_ch=UC-qWJlvaPME3MWvrY-yjXeA')
		list.append('&youtube_ch=UCLsooMJoIpl_7ux2jvdPB-Q')
		list.append('&youtube_ch=UCtgpDqkeOToveUgh8igrvXQ')
		list.append('&youtube_ch=UC3djj8jS0370cu_ghKs_Ong')
		list.append('&youtube_ch=ch=UCBnZ16ahKA2DZ_T5W0FPUXg')
		list.append('&youtube_pl=PLA1896AD5E9625B8C')
		list.append('&youtube_pl=PLtUvIcNPXN59c-ZJMt0Z6PkcKmseSGMAg')
		list.append('&youtube_pl=PLDB6FE8E3E0778DC8')
		list.append('&youtube_id=HP-MbfHFUqs')
		list.append('&youtube_pl=PLNNSc1ZGQKJ2OLMnyGGHiNU31Un30BCte')
		list.append('&youtube_pl=PLFF5E78C1F6DD249A') #שירי דיסני
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
		list.append('&youtube_pl=PL-s48adn-YXjSIXrWs5sMxHdlS1Kw0qym') #שירי דיסני
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLB6E1CC078D067452') #שירי דיסני
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=RDD2VTOlVVIoo')
		list.append('&youtube_pl=PLc6OoqL0xc0ayk2bl5VY_3p-_x3M2E4w-') #שירי דיסני
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLCE36BC8BB4712703') #שירי דיסני
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLSYmbyGEyJRBiQJ_i0BStz0OrY8ygNsbT') #שירי דיסני
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=RDLKDNzdjp4Lc#t=29')
		list.append('&youtube_pl=PLbBfnSpdVgaYlm9iC0LJLmOznnfAxkjUR')
		list.append('&youtube_pl=PLYfN6ttNNcbTxkGBr_PBAMDeap9QRb35G')
		list.append('&youtube_pl=PLfH7vjpTQ7to85hnvrOauTehE73pZ5-D1') #שירי דיסני
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLcHYNoAhXTuRepaK1hkUNF9OVsxv3osUO') #שירי דיסני
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PL7SSS8oSHfGZg2U76Nq8J7iFokm6MHfcC')
		list.append('&youtube_pl=PLlOn3l2a68aMZgCd8PKEr7-ru3rDSlAIa')
		list.append('&youtube_pl=PLk0aMP5sfRqWdrpAIuy-OYs7JThcpP9Fx')
		list.append('&youtube_pl=PLiXEtCvi0UHMVTirHnhs3e1UyT3-EfnNF') #שירי דיסני
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL1EE26AB0AC072016') #שירי דיסני
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLCC17D921DFB7B60D') #שירי דיסני
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLqDclpzVrDJMJnF-oSA6u2I3dXpez42lE') #Stories
		list.append('&youtube_pl=PLAB5131587C712D86') #Songs
		list.append('&youtube_pl=PL3l5QRRFt2i3DTN9O8uDffJswsf_P97eP') #Songs
		list.append('&youtube_pl=PLqDclpzVrDJMe1tIITMxuAnULvUqGhCME') #Songs
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
	
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=RDWjhQvv9kexk#t=47')
	
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
		list.append('&youtube_pl=PLEoWurB6PfTPuA-G6W0GRF1pj-9g_6dKS') #שירי דיסני
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLJgmMSdWwadtTK4JzHhl5N5YR49ZVcGTK') #Songs
		list.append('&youtube_pl=PLt6kNtUbjfc9YuNnmmzcFWL-UfW38egUx') #Songs
		list.append('&youtube_pl=PLJgmMSdWwadtTK4JzHhl5N5YR49ZVcGTK') #Songs
		list.append('&youtube_pl=PLA87EDCE79FC3FD10') #Songs
		list.append('&youtube_pl=PL8aozOmtKmVrkAr70kP2t6j0EPz-I2SSm') #שירי דיסני
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL0B74C49EA4578EF9') #שירי דיסני
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLZzjuZRUVoG-25qMwSlGO3EdtJs8L63nd') #שירי דיסני
	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES102A(General_LanguageL, background): #אקראי הצגות ילדים
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=0FaBsetswDA')
		list.append('&youtube_id=PUL2C9mEAKQ')
		list.append('&youtube_id=o20-0VygrsE')
		list.append('&youtube_id=-ihwgBW3sVs')
		list.append('&youtube_id=_ixMuVcAGhA')
		list.append('&youtube_id=YOs5zhvXUf8')
		list.append('&youtube_id=63mlzFfxDxI')
		list.append('&youtube_id=kbzPyZV3cck')
		list.append('&youtube_id=i5yQxLraENk')
		list.append('&youtube_id=yfEzE5V409k')
		list.append('&youtube_id=f9s_aunAElY')
		list.append('&youtube_pl=PLuDrdycU7c6gcx20C2zPrM87gMfaaoCov') #עוץ לי גוץ לי
		list.append('&wallaNew=item_id%3D2833366')
		list.append('&wallaNew=item_id%3D2817611')
		list.append('&custom4=plugin://plugin.video.MakoTV/?url=http%3A%2F%2Fwww.mako.co.il%2Fmako-vod-kids%2FVOD-b231728b7e02e41006.htm%3FsCh%3D131102642cecc310%26pId%3D540607453&mode=4&name=%D7%9E%D7%95%D7%A8%D7%A0%D7%99+%D7%94%D7%90%D7%9C%D7%95%D7%A4%D7%94&iconimage=http://img.mako.co.il/2015/07/05/morani+tabi_f.jpg')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
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

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES104A(General_LanguageL, background): #אקראי סדרות
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&sdarot=plugin://plugin.video.sdarot.tv/?mode=2&module=http%3a%2f%2fwww.sdarot.wf%2fseries%2fgenre%2f7%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&name=%d7%90%d7%a0%d7%99%d7%9e%d7%a6%d7%99%d7%94&url=all-heb&name_=SDAROT-TV&')
		list.append('&sdarot=series_id=1784&series_name=%d7%98%d7%95%d7%9d%20-%20%2a%d7%9e%d7%93%d7%95%d7%91%d7%91%2b%d7%aa%d7%a8%d7%92%d7%95%d7%9d%20%d7%9e%d7%95%d7%91%d7%a0%d7%94%2a&url=http%3a%2f%2fwww.sdarot.pm%2fwatch%2f1784%2ftom-%d7%98%d7%95%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91-%d7%aa%d7%a8%d7%92%d7%95%d7%9d-%d7%9e%d7%95%d7%91%d7%a0%d7%94')
		list.append('&wallaNew=genre%3dkids%26genreId%3d7447&name_=WallaVOD&')
		list.append('&youtube_ch=UCDfoEu-jaKsjNL6Fl0h5PUQ')
		list.append('&youtube_ch=UC9DU2y9iXnrI0Y5NFoBQ4RQ/playlists')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL618DEA0E28636BC2') #English
		list.append('&youtube_pl=PLL7dcgwYKsm0vTqux1z7SDbuuO3PwEmDC') #English
		list.append('&youtube_pl=PL1SAyTUFBb767lthA5ZrIux5ierTsdY8X') #בנימין הפיל
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
		list.append('&youtube_pl=PL8xBm2jGFeURg8zePCAvOmz0HKF0Buxx9') #בנימין הפיל
	
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
		list.append('&youtube_pl=PL1SAyTUFBb76vI6mmDVJW-idZzy5w3O95') #בנימין הפיל
		
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
		list.append('&youtube_pl=PL1SAyTUFBb76lUw0NZmBs5wivH7C2rDjH') #בנימין הפיל
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PLWMCwroYhJSqSut59L-Sxr0A5IR-0XWeE')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL1SAyTUFBb74M_o7qtwLX507S1U11DFdq') #בנימין הפיל
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL1SAyTUFBb76FQRP8IUUdRWdyvejE7KHg') #בנימין הפיל
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
		list.append('&youtube_id=6M2Ll1ckj-o')
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
		list.append('&youtube_pl=PL1SAyTUFBb77CVJW1egme_gOlYTcPsy1X') #בנימין הפיל
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES105A(General_LanguageL, background): #אקראי סרטים
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_id=RwY6ZNmV1OU')
		list.append('&youtube_pl=PLZOPiMtEyky3WOXdj-PUdbTsGpsm-zS8m')
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
		list.append('&youtube_pl=PLIf4rYL_srdU4GHrrC2SY6FpPWV05dr-i')
		list.append('&youtube_ch=getmovies/playlists') #getmovies
		list.append('&youtube_id=jEQvhO3QCDg') #Three heroes and Shamahanskaya queen (cartoon)
		list.append('&youtube_id=8vPQKM5UOJU')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES106A(General_LanguageL, background): #אקראי פעוטות
	'''אקראי'''
	list = []
	
	list.append('&youtube_pl=PLwxbE7ppBW4l1nxhAxPS7ZNkQQN3Z4_jr') #בייבי איינשטיין
	list.append('&youtube_pl=PLvIdvaV3orE-FmApmbSoDRXPVnlNW5TAS') #פים ופימבה
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_id=dby1qndJnGs')
		list.append('&youtube_id=Ood3teygwh8')
		list.append('&youtube_id=KEDLj-c5zZg')
		list.append('&youtube_id=y24MAvLMHdE')
		list.append('youtube_pl=PLnraPnhPHcc4EJiGhB2lh3cq0xo3gD0gp') #צופי
		list.append('youtube_pl=PLnraPnhPHcc7gx1zReO0qmXQ5nGV_6wtJ') #צופי
		list.append('youtube_pl=PLnraPnhPHcc7O4BysIZ9_9nBOuakjrvUJ') #צופי
		list.append('youtube_pl=PLnraPnhPHcc7ZM0lb57BnB2QK9syspUuF') #צופי
		list.append('youtube_id=dpIySQOXpvg') #צופי
		list.append('&youtube_pl=PLbHXbhgZi5cL97NlobjLHNtBwIA9VHcmw') #קטני
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLydGVtigmLv3dH5928n81xDim_3YrVHZ7')
		list.append('&youtube_pl=PLF06QSQtcR4cqGAXuilkIJmKOvmF1EQo7') #פויוקו
		list.append('&youtube_pl=PLFdlLLQanAPDDSueGBJBwdSLnQCwdog9H') #קטני

	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLOY9guFx55F1HjVkrHpgWX0yrBcI2exnX') #פויוקו
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=PLkEXJmKDVso5cQjSUez3x8oLsI7VloRPE')
	
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
		list.append('&youtube_pl=PLhzFGhjBvFmPa2xvYZJuaP3AjMvUbi9BU') #פויוקו
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=PLWge4sjPIE4hg55zSnVf1wIUpTX1g-LX1') #פויוקו
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLporszkvR1VfMzI9-XGFpgB0Nk_d5FcUj') #קטני
		
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLGtYWSxNvzCiX0LiGqNCZOYi943_okMpP') #פויוקו
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PLDc2NTYsDK4kHzbwYUOWjQkt30d0h89xy') #פויוקו
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PLjCu5PKs0QNylhl4MLYSL3-ijX1lVzFnd') #פויוקו
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLF06QSQtcR4eeHVVZ0ML1kX92_m-rMTxl') #פויוקו
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLD03iNFvg_Iu6zly-qEhAu6UVEGkDxC6X') #קטני
		
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=PLI3FCm0aa3nlLHvUTEYs0RGL-xbpq_hKK') #פויוקו
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLMjx0ykYrUymHrKQpuGpMLzAlGFBxecOX') #פויוקו
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=PL6RR5mzxETPEIpEObk06RvI76dYko5W5W') #פויוקו

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLBFFF9A937DCF1B0F') #פויוקו
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=PL_mwrALU8Bo_Wy8FnR7SeLsGo2hjLepsZ') #פויוקו
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
		list.append('&youtube_pl=PLCsBweb0jQ6Ryvv3inUpGXnZXAwCIFEbm') #Shapes for kids children
		list.append('&youtube_pl=PL1SAyTUFBb77CVJW1egme_gOlYTcPsy1X') #Benjamin the Elephant
		list.append('&youtube_pl=PLA8O63dq_Dpf7YuaGE1LZr8HIqtrldyZi') #?
		list.append('&youtube_pl=PLYjQr8vff1Jy95LtWqFNCeNL8w-NCFFgg') #פויוקו
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=PLyMip9LDuF-pLB0u1xoMVYvvIPMOxNtdR') #פויוקו
		list.append('&youtube_pl=')
	
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES107A(General_LanguageL, background): #אקראי קטנטנים
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_ch=UCDfoEu-jaKsjNL6Fl0h5PUQ')
		list.append('&wallaNew2=http://nickjr.walla.co.il/')
		list.append('&wallaNew=genre%3dkids%26genreId%3d7623')
		list.append('&youtube_ch=UCQWDQwBdFVOPjvBy6mgqUQQ')
		list.append('&wallaNew=genre%3dkids%26genreId%3d7452')
		list.append('&wallaNew=genre%3dkids%26genreId%3d7453')
		list.append('&youtube_ch=UC9DU2y9iXnrI0Y5NFoBQ4RQ/playlists')
		list.append('&youtube_pl=PL_8KXLhQVQMK80XCn7g3qVj7RwhrwiGHG') #בוב הבנאי
		list.append('&youtube_pl=PLsDVVvjmKAxEeSD3K7wybKJ42BbZc5JlJ') #תומס הקטר
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_id=Twm_igTeias') #תומס הקטר #S1
		list.append('&youtube_id=xhap8ezkfCE')
		list.append('&youtube_pl=PL0sYiBnLzquZiY3lUx4gtdQjkYHEbls-4') #בוב הבנאי
		list.append('&youtube_id=u9zAJz2wyG8') #פפה החזיר
		list.append('&youtube_pl=PLG7lOHF8VEv8gIhF5E3iy1ueiwViDSrq7') #English #קירוקי
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL61W_aqonWD9cRbZnicuZ-7Z2YgI3pXb3') #בוב הבנאי
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
		list.append('&youtube_pl=PL6E6EC6BECB940729') #בוב הבנאי
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=89A-ElVAsRs') #בוב הבנאי
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_ch=UCKxUuFz2-m-sMSOdMzN-jDA') #Dutch	
		list.append('&youtube_pl=PLiYnki7YcURvX8um3QXUYBflo7nPajnG3') #טלטאביז
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
		list.append('&youtube_id=mhwasuXjMKg') #תומס הקטר
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL718qI31wRq9nDjjDvBvLzFo3SxpKve-p') #טלטאביז
		list.append('&youtube_pl=PLF493BCB7A2B5EF42') #בוב הבנאי
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLS6A4SYN00LYYloR80D1aubcjcEO0o376') #טלטאביז
		list.append('&youtube_pl=PL8BA2003016C19A9C') #בוב הבנאי
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL6CFD617813187A4E') #בוב הבנאי
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
		list.append('&youtube_pl=PLrpvkUYQuRUFKClj669y7JFEgr2AkwEPI')
		list.append('&youtube_pl=PL58leaokT4HSFmnwtRrjvXQg9SZqnjsaG') #טלטאביז
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLdDOXpS6MzV9DkSRE3ubF53QEOFe18mzc') #בוב הבנאי
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL5p0NjRxSV8Dw8nK2rm-mr9ykr7OA5dQ_')
		list.append('&youtube_pl=PL465ZjxENzxGCYVR3zCKWdNzpT_S6L26Q')
		list.append('&youtube_pl=PLHfTivZrNVwwehlbkuaUeWQmQidWoA-Gi')
		list.append('&youtube_pl=PLOgjrDemRWxKAYykYCyyHjhLg-AnVL_WJ')
		list.append('&youtube_id=5hQEwTINIE8') #סם הכבאי
		list.append('&youtube_pl=PLXnIohISHNIuH97pzQYV5O96-Q7-VwhRV') #מאשה והדוב
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES108A(General_LanguageL, background): #אקראי ילדים ונוער
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLa8HWWMcQEGShWcQbipVlr3uEEnr0bLeh') #הרפתקאות קראט

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
		list.append('&youtube_pl=PL75Ev9SzNPCbBph8ohUx7PztLgGIqqxkS') #הרפתקאות קראט
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_id=tHdRnmWMrXc') #RUCA AND YOUR FRIENDS
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
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
		list.append('&youtube_pl=PL1HIp83QRJHQOmroSI5hWLo0ma89aFtND') #Ivan Maximov
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES109A(General_LanguageL, background): #אקראי לימוד שפה
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
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
		list.append('&youtube_pl=PLPLJUpFxaEzbm3COhJ9vNDvWPmcvcZdfj') #Learning Russian language
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES110A(General_LanguageL, background): #אקראי ?
	'''אקראי'''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
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

	addDir('-' + localize(590),list,17,featherenceserviceicons_path + 'random.png',"",'1',"", getAddonFanart(background, custom=""))
	
	
