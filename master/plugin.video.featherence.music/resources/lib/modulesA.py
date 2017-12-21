# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''עמוד הבא'''

def CATEGORIES10101A(name, iconimage, desc, fanart):
	'''מוזיקה ישראלית'''
	background = 101
	
	list = []

	list.append('&youtube_pl=PLjUpwHk7giaiaSeSzZ4Alqj8cGQB6rPEk')
	list.append('&youtube_pl=PLjUpwHk7giaj910tIRA-XTqx6HJA7tPUi') 
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
	list.append('&youtube_pl=PLWvtqTEJL_PecfYvYdEhXvijvSas9ocp5')
	list.append('&youtube_pl=PLFcBFujWU-tB6op3uAj-eJiymuwsUt51T')
	list.append('&youtube_pl=PLFcBFujWU-tDTP_OahLQ6CVvew_TElbHr')
	list.append('&youtube_pl=PLLaB91oVoE-Cq3aJa7MElaf5i3JBILpit')
	list.append('&youtube_pl=PLDMFOZKyoCX0EMCapcK2qW7X3mxjs52Xw')	
	list.append('&youtube_pl=PL1sns8HoY1uKuGp9ze9f5W410VleGhAZ-')
	list.append('&youtube_pl=PL6CcUVzFqqcVNcscz560ZsaxhWrQOrWXH')
	list.append('&youtube_pl=PLB42AF7617D0814D2')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10102A(name, iconimage, desc, fanart):
	'''קריוקי ישראלי'''
	background = 102
	
	list = []

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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10104A(name, iconimage, desc, fanart):
	'''הופעות חיות ישראליות'''
	background = 104
	
	list = []

	list.append('&youtube_pl=PLKIqRYpY39ifwx1ri1V7M7VTAblAF8CsE')
	list.append('&youtube_pl=PLFA89WMFMcB1K9hxwOepQRJVhW-lrMPjM')
	list.append('&youtube_pl=PLMwPZme_veqWQINmATvObYwPKS3cb5_Nm')
	list.append('&youtube_pl=PLEB6243D778C2569F')
	list.append('&youtube_pl=PL50697249A4878FDD')
	list.append('&youtube_pl=PLmMwYXuNQYCj2-UJzQzDgvaRYSDkWTZtN')
	list.append('&youtube_pl=PLQGx0XOoq2fvv1Sqhtk3mcYhYVkKhPC2p')
	list.append('&youtube_pl=PLq3kSq7XTmPMysdOzY-9-lWzUxVLUacij')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10105A(name, iconimage, desc, fanart):
	'''די ג'י ישראליים'''
	background = 105
	
	list = []

	list.append('&youtube_pl=PLFA89WMFMcB0rEAl97cPtYtaBXbi_17jI')
	list.append('&youtube_pl=PLu0oMBI6tzUu_0EtzZ7XhBZijKPy_276g')
	list.append('&youtube_pl=PLNL6cVMJqkHFuHeeOQ5lCzPvb3Rrw8wg8')
	list.append('&youtube_pl=PLLgkjg98m5INnhyZDV-vLGMzMXbQdYrA6')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10107A(name, iconimage, desc, fanart):
	'''קריוקי מזרחי'''
	background = 107
	
	list = []

	list.append('&youtube_pl=PLHfj2MFrGpzct3Rym9_U3jG1n4H4xmJPe') #2015
	list.append('&youtube_pl=PLv6KOe-zMNbK4Nuceb39mdQlFXgdmXiSH')
	list.append('&youtube_pl=PLu57xoZ3keBcEEeFlr8NGgBCKIh-nzXNE')
	list.append('&youtube_pl=PLjMlZAOscH-v8ZG7OhCmI8PepJtw8OM3x')
	list.append('&youtube_pl=PLtm8IRX6612ofHw4vVeVg0XDSanSeLaEZ')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10109A(name, iconimage, desc, fanart):
	'''הופעות חיות מזרחיות'''
	background = 108
	
	list = []

	list.append('&youtube_pl=PLE4DED532FECA9BC4')
	list.append('&youtube_pl=PLB2FEE0AC0BD2819C')
	list.append('&youtube_pl=PLshzwVrSQVkjOFejcw0fQXKhQA3IcQOLV')
	list.append('&youtube_pl=PL6RyS6EH1Xnx9vF1no4Ris_JM6TO7EHsn')
	list.append('&youtube_pl=PLD088399863915B82')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11101A(name, iconimage, desc, fanart):
	'''מוזיקה לועזית'''
	background = 111
	
	list = []

	list.append('&youtube_pl=PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk')
	list.append('&youtube_pl=PLsiyfJZak8Pc7AA6EqEIXBgU4u-qypRLe')
	list.append('&youtube_pl=PLuK6flVU_Aj5EJ9Pp-C9N7XA0YJr_GrJI')
	list.append('&youtube_pl=PLqYXv_L7NiEyYnfZhVHR7ixOTANxjes89')
	list.append('&youtube_pl=PL2E373ABBD360C09F')
	list.append('&youtube_pl=PLP6Mnyo0OTQtnZtDpxceawHIFW5dx38y8')
	list.append('&youtube_pl=PL422A945E3D37BF49')
	list.append('&youtube_pl=PL230B1AFAC3F149D0')
	list.append('&youtube_pl=PLQw-AwSCH8G3Dhw4vAu0R7OfxDWdUbhaR')
	list.append('&youtube_pl=PL7BA598CBAF2745D9')
	list.append('&youtube_pl=PL05E1623111A9A860')
	list.append('&youtube_pl=PLpuDUpB0osJmZQ0a3n6imXirSu0QAZIqF')
	list.append('&youtube_pl=PLiDpE5JOXvy15BAQk5-xpAY8cgOJZDKlD')
	list.append('&youtube_pl=PLz1ThN-w-t_zGtVNm9xtNXyPfwUJ1EfyZ')
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11102A(name, iconimage, desc, fanart):
	'''קריוקי לועזי'''
	background = 112
	
	list = []

	list.append('&youtube_pl=PL7_nPoVWZlQ2OS8cBagc072Mzdx0V9uDR')
	list.append('&youtube_pl=PLzhHScp_FPuvuOijzOQjFiTajZMQCFhKi')
	list.append('&youtube_pl=PL1AC85D057F6825A9')
	list.append('&youtube_pl=PL0562084654703201')
	list.append('&youtube_pl=PL8D4Iby0Bmm-uQIcbRfHeUMd_YDSZDA39')
	list.append('&youtube_pl=PL2dHcK1nJqU8zCIhqC6gFIIIEikLi3AvB')
	list.append('&youtube_pl=PLqGkpApxFsX_jRp4sDFz9_gwztqqpDZ2U')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11104A(name, iconimage, desc, fanart):
	'''הופעות חיות לועזיות'''
	background = 114
	
	list = []

	list.append('&youtube_pl=PLJFSFauO5sHZbgRwOFlgk5a2PbniNQR7v')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11105A(name, iconimage, desc, fanart):
	'''די ג'י לועזיים'''
	background = 115
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11109A(name, iconimage, desc, fanart):
	''''''
	background = 119
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))
	
def CATEGORIES118A(name, iconimage, desc, fanart):
	'''מוזיקה קלאסית'''
	background = 118
	
	list = []

	list.append('&youtube_pl=PLcGkkXtask_fpbK9YXSzlJC4f0nGms1mI')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))
	

def CATEGORIES114A(name, iconimage, desc, fanart):
	'''תצוגות אופנה'''
	background = 114
	
	list = []

	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))