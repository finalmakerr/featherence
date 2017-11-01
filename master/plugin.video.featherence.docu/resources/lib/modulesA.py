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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES104A(name, iconimage, desc, fanart):
	'''מדע'''
	background = 104
	
	list = []

	list.append('&youtube_ch=UCWYeiNSo18bhZvI1pz39U6g')
	list.append('&youtube_ch=UCWkOjdpqIcKZrnjefwWMKAQ')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10401A(name, iconimage, desc, fanart):
	'''מדע - חברתי'''
	background = 10401
	
	list = []

	list.append('&youtube_pl=PLNLnlLmMBcgT9fhs_lpKRRrLasi2ggqT5')
	list.append('&youtube_pl=PLeDkGnO-NieF4Otwc4K2RA-ZagUdAIVwZ')
	list.append('&youtube_pl=PL0z0Pscrs45B0POHdpKhikbhjKU491-gL')
	list.append('&youtube_pl=PLU8cnQEDNLyWeKlWxwj4aY8wDuAkxa06W')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10402A(name, iconimage, desc, fanart):
	'''מדע - טבע'''
	background = 10402
	
	list = []
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10403A(name, iconimage, desc, fanart):
	'''מדע - טכנולוגיה'''
	background = 10403
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES107A(name, iconimage, desc, fanart):
	'''ילדים'''
	background = 107
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES11105A(name, iconimage, desc, fanart):
	''''''
	background = 115
	
	list = []

	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
	list.append('&youtube_pl=')
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

	
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
		
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))
	
def CATEGORIES108A(name, iconimage, desc, fanart):
	'''בעברית'''
	background = 108
	
	list = []
	
	list.append('&youtube_pl=PL51YAgTlfPj6s0QtcgOpIwKewkEeSN77e')
	list.append('&youtube_pl=PL51YAgTlfPj7TAvhkV8c9UnnMHUpQy-Bx')
	list.append('&youtube_pl=PL51YAgTlfPj474gCGLEUa7_Zo5Bxgy9fG')
	list.append('&youtube_pl=PL51YAgTlfPj4v3ww2jfBb21LiJFh3XSIe')
	list.append('&youtube_pl=PL51YAgTlfPj6zllZWhjkRCv95Q9LPhRZ2')
	list.append('&youtube_pl=PL51YAgTlfPj4NGa6HC87lQQL5KfqQTqW3')
	list.append('&youtube_id=eIOvF0MlMe0')
	list.append('&youtube_id=TOeT5DQSRDc')
	list.append('&youtube_id=J1JIHh1ZEf0')
	list.append('&youtube_pl=PLEDEE611B09BB3800')
	list.append('&youtube_pl=PLth1a195qHsj20lXv4QqTQ7kb2RLoGxY8')
	list.append('&youtube_pl=PL51YAgTlfPj59VvVLjLaAiGbFjbqv7sh3')
	list.append('&youtube_pl=PL51YAgTlfPj4F8EkY07BfV1KhdjmtjX0P')
	list.append('&youtube_pl=PL51YAgTlfPj4oR5aIC0Ru5JZA1a1TT-RN')
	list.append('&youtube_pl=PL51YAgTlfPj6PWe7kECdyz6ToCjcmSd6z')
	list.append('&youtube_pl=PLth1a195qHsi9fsrgjDzYTzqKSOF-Ky-N')
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))

def CATEGORIES10801A(name, iconimage, desc, fanart):
	'''בעברית - ילדים'''
	background = 10801
	
	list = []
	list.append('&youtube_ch=The23Kidz')
	list.append('&youtube_ch=23language')
	list.append('&youtube_pl=VGVK6cqjoj6Aeyi2x7yQqo0S9Pq8CkZ')
	list.append('&youtube_id=l3fXEyLWCzI')
	list.append('&youtube_pl=PL43AC3544C5E17BEF')
	list.append('&youtube_id=QcANPfq5V7g')
	list.append('&youtube_id=gO9hyX4s1ko')
	list.append('&youtube_pl=PLTleo-h9TFqI2CFuWeFA-Q2Bu3BBHdXqv')
	list.append('&youtube_id=jMIELC0KFs4')
	
	addDir('-' + localize(33078),list,6,featherenceserviceicons_path + 'nextpage.png',"",'1',0,getAddonFanart(background, custom=""))
	