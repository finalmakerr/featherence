import xbmc, xbmcgui, xbmcaddon, sys, os

try:
	addonID2 = xbmcaddon.Addon().getAddonInfo("id")
	printfirst = xbmcaddon.Addon().getAddonInfo("name") + ": !@# "
except:
	addonID2 = ""
	printfirst = " "

'''------------------------------
---DEFAULT-----------------------
------------------------------'''
space = " "
space2 = ": "
space3 = "_"
space4 = " / "
space5 = " - "
newline = "\n"
TypeError = ""
dialog = xbmcgui.Dialog()
systemplatformwindows = xbmc.getCondVisibility('System.Platform.Windows')
systemplatformlinux = xbmc.getCondVisibility('System.Platform.Linux')
systemplatformlinuxraspberrypi = xbmc.getCondVisibility('System.Platform.Linux.RaspberryPi')
systemplatformandroid = xbmc.getCondVisibility('System.Platform.Android')
	
systemplatformosx = xbmc.getCondVisibility('System.Platform.OSX')
systemplatformios = xbmc.getCondVisibility('System.Platform.IOS')
'''---------------------------'''

addon = 'script.featherence.service'
if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	getsetting_servicefeatherence = xbmcaddon.Addon(addon).getSetting
	setsetting_servicefeatherence = xbmcaddon.Addon(addon).setSetting
	addonString_servicefeatherence = xbmcaddon.Addon(addon).getLocalizedString
	admin = getsetting_servicefeatherence('admin')
	admin2 = "a"
	if xbmc.getInfoLabel('Network.MacAddress') == '0C:8B:FD:9D:2F:CE': admin3 = 'true'
	elif xbmc.getInfoLabel('Network.MacAddress') != "": admin3 = 'false'
	else: admin3 = 'false'
	'''---------------------------'''
else:
	addonString_servicefeatherence = ""
	admin3 = 'false'
	'''---------------------------'''

'''paths'''
addons_path = os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"))
userdata_path = os.path.join(xbmc.translatePath("special://userdata/").decode("utf-8"))
addondata_path = os.path.join(userdata_path,'addon_data','')
database_path = os.path.join(xbmc.translatePath("special://database").decode("utf-8"))	
home_path = os.path.join(xbmc.translatePath("special://home/").decode("utf-8"))
packages_path = os.path.join(addons_path,'packages','')
skin_path = os.path.join(xbmc.translatePath("special://skin").decode("utf-8"))
temp_path = os.path.join(xbmc.translatePath("special://temp/").decode("utf-8"))
thumbnails_path = os.path.join(xbmc.translatePath("special://thumbnails").decode("utf-8"))

xbmc_path = os.path.join(xbmc.translatePath("special://xbmc/").decode("utf-8"))

featherenceservice_addondata_path = os.path.join(addondata_path,'script.featherence.service', '')
featherenceserviceaddondata_media_path = os.path.join(featherenceservice_addondata_path, 'media', '')
featherenceservice_path = os.path.join(addons_path,'script.featherence.service','')
featherenceserviceicons_path = os.path.join(featherenceservice_path, 'resources', 'icons', '')
featherenceservicebackgrounds_path = os.path.join(addons_path, 'resource.images.weatherfanart.single', 'resources', '')

systemlanguage = xbmc.getInfoLabel('System.Language')
containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
'''---------------------------'''
Featherence_auth2 = '0811'

'''------------------------------
---Window(Home).Property(key)----
------------------------------'''
scriptfeatherenceservice_random = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random)')
scriptfeatherenceservice_random1 = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random1)')
scriptfeatherenceservice_random2 = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random2)')
scriptfeatherenceservice_random3 = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random3)')
scriptfeatherenceservice_random4 = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random4)')
scriptfeatherenceservice_random5 = xbmc.getInfoLabel('Window(home).Property(script.featherence.service_random5)')
scriptfeatherenceservice_randomL = []
if scriptfeatherenceservice_random1 != "": scriptfeatherenceservice_randomL.append(scriptfeatherenceservice_random1)
if scriptfeatherenceservice_random2 != "": scriptfeatherenceservice_randomL.append(scriptfeatherenceservice_random2)
if scriptfeatherenceservice_random3 != "": scriptfeatherenceservice_randomL.append(scriptfeatherenceservice_random3)
if scriptfeatherenceservice_random4 != "": scriptfeatherenceservice_randomL.append(scriptfeatherenceservice_random4)
if scriptfeatherenceservice_random5 != "": scriptfeatherenceservice_randomL.append(scriptfeatherenceservice_random5)

'''---------------------------'''

if addonID2 == 'plugin.video.featherence.extreme': api_youtube_featherence = 'AIzaSyBde4TsUnb8RHSGh-4FSmuEgEhe_QBTYlU'
elif addonID2 == 'plugin.video.featherence.kids': api_youtube_featherence = 'AIzaSyDhADc1LWKBkrEWgViqoe4gjo6YmLKU9uY'
elif addonID2 == 'plugin.video.featherence.music': api_youtube_featherence = 'AIzaSyAs0RWqPz1wn7Sb6gZRjqAyim7oPnn35H0'
elif addonID2 == 'plugin.video.featherence.docu': api_youtube_featherence = 'AIzaSyA7wtnafo-M_PPHV7CmLaz3o3DBaN5s-5w'
elif addonID2 == 'plugin.video.featherence.rofl': api_youtube_featherence = 'AIzaSyAddU4mfo8ItvKdSYBqT2gB7X7qIdw-JYI'
elif systemplatformwindows: api_youtube_featherence = 'AIzaSyAV27UywO__WqRlKF_FKxoAyL4dwFDmvyE'
else: api_youtube_featherence = 'AIzaSyDkNxiwClyCildDbHdDKSWt5BkKQ6LeQqA'
print api_youtube_featherence
api_dailymotion_featherence = '3e563cafd4fbba5de0c1'
api_vimeo_featherence = '45584ad52d6951f441fd2f7c7ae690d2'
api_pastebin_featherence = '1040252c25203082ce6901fcf22e2756'
api_imagebin_featherence = 'c8LpkstmM3WBoukL+zaJdFRCJEMIWRwL'

'''------------------------------
---DATES-----------------------
------------------------------'''
import datetime as dt
import time

datenow = dt.date.today()
datenowS = str(datenow)