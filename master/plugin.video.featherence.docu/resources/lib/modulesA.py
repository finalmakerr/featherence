# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''

'''עמוד הבא'''

def CATEGORIES101A(name, iconimage, desc, fanart):
	'''טבע'''
	background = 101
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
	#list.append('&youtube_pl=PL3Ea6NwLKoMSArPBNWh-gMgKCX2cmJzCq') #Not working!
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10101A(name, iconimage, desc, fanart):
	'''טבע - חיות'''
	background = 10101
	
	list = []

		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10102A(name, iconimage, desc, fanart):
	'''טבע - חוקי טבע'''
	background = 10102
	
	list = []

		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES10103A(name, iconimage, desc, fanart):
	'''טבע - מקומות'''
	background = 10103
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES102A(name, iconimage, desc, fanart):
	'''חלל'''
	background = 102
	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES103A(name, iconimage, desc, fanart):
	'''היסטוריה'''
	background = 103
	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES104A(name, iconimage, desc, fanart):
	'''מדע'''
	background = 104
	
	list = []

	list.append('&youtube_ch=UCWYeiNSo18bhZvI1pz39U6g')
	list.append('&youtube_ch=UCWkOjdpqIcKZrnjefwWMKAQ')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10401A(name, iconimage, desc, fanart):
	'''מדע - חברתי'''
	background = 10401
	
	list = []

	list.append('&youtube_pl=PLNLnlLmMBcgT9fhs_lpKRRrLasi2ggqT5')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PL0z0Pscrs45B0POHdpKhikbhjKU491-gL')
	list.append('&youtube_pl=PLU8cnQEDNLyWeKlWxwj4aY8wDuAkxa06W')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10402A(name, iconimage, desc, fanart):
	'''מדע - טבע'''
	background = 10402
	
	list = []
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10403A(name, iconimage, desc, fanart):
	'''מדע - טכנולוגיה'''
	background = 10403
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES107A(name, iconimage, desc, fanart):
	'''ילדים'''
	background = 107
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES11105A(name, iconimage, desc, fanart):
	''''''
	background = 115
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

	
def CATEGORIES110A(name, iconimage, desc, fanart):
	'''אומנות'''
	background = 110
	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))
	
def CATEGORIES108A(name, iconimage, desc, fanart):
	'''בעברית'''
	background = 108
	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))

def CATEGORIES10801A(name, iconimage, desc, fanart):
	'''בעברית - ילדים'''
	background = 10801
	
	list = []
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',"", getAddonFanart(background, custom=""))
	