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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10104A(name, iconimage, desc, fanart):
	'''הופעות חיות ישראליות'''
	background = 104
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10105A(name, iconimage, desc, fanart):
	'''די ג'י ישראליים'''
	background = 105
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10106A(name, iconimage, desc, fanart):
	'''מוזיקה מזרחית'''
	background = 106
	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10107A(name, iconimage, desc, fanart):
	'''קריוקי מזרחי'''
	background = 107
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10108A(name, iconimage, desc, fanart):
	'''הופעות חיות מזרחיות'''
	background = 108
	
	list = []

	list.append('&youtube_pl=PL5MV8_qxHC5ufNt9OV-lyMTm_WU-xUFWV')
	list.append('&youtube_pl=PLjHwF6MA1nycO4TXyQ0Di7ADrg9wTJ8XW')
	list.append('&youtube_pl=PL6WvGFcuPjESeFQY0YyCzTy7qTofzMlaQ')
	list.append('&youtube_pl=PL7302191F8A43E01C')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11101A(name, iconimage, desc, fanart):
	'''מוזיקה לועזית'''
	background = 111
	
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
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11102A(name, iconimage, desc, fanart):
	'''קריוקי לועזי'''
	background = 112
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11104A(name, iconimage, desc, fanart):
	'''הופעות חיות לועזיות'''
	background = 114
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11105A(name, iconimage, desc, fanart):
	'''די ג'י לועזיים'''
	background = 115
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

	
def CATEGORIES118A(name, iconimage, desc, fanart):
	'''מוזיקה קלאסית'''
	background = 118
	
	list = []

	list.append('&youtube_pl=PLcGkkXtask_fpbK9YXSzlJC4f0nGms1mI')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))