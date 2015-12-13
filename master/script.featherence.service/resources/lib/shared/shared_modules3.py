import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,random
import json

from variables import *
#from modules import *
from shared_modules import *

'''plugins'''
def addDir(name, url, mode, iconimage, desc, num, viewtype, fanart=""):
	url2 = url ; printpoint = "" ; returned = "" ; extra = ""
	if '$LOCALIZE' in name or '$ADDON' in name: name = xbmc.getInfoLabel(name)
	if '$LOCALIZE' in desc or '$ADDON' in desc: desc = xbmc.getInfoLabel(desc)
	

	if desc == None or desc == "" or desc == "None": desc = ""
	else:
		try: desc = str(desc).encode('utf-8')
		except:
			try: desc = str(desc)
			except Exception, TypeError:
				extra = extra + newline + "TypeError" + space2 + "desc Error" + space + "name" + space2 + str(name)
				desc = ""
	if iconimage == None or iconimage == "": iconimage = "" #iconimage = "None" #"None"
	if url == None or url == "": url = "None"
	else:
		url = str(url)
	
	
	if name == None or name == "": name = "" #name = "None" #"None"
	else:
		try: name = name.encode('utf-8')
		except: pass
	if fanart == None: fanart = ""
	
	if mode == 17: name = '[COLOR=Green]' + name + '[/COLOR]'
	elif mode == 5: name = '[COLOR=Yellow]' + name + '[/COLOR]'
	elif mode == 8: name = '[COLOR=White2]' + name + '[/COLOR]'
	
	
	if mode >= 100 and 1 + 1 == 2:
		#if url == "": url = "1"
		u=sys.argv[0]+"?url="+str(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
	else:
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
	
	
	
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc} )
	try:
		if Fanart_Enable != "" and Fanart_EnableCustom != "": pass
	except:
		Fanart_Enable = "true"
		Fanart_EnableCustom = "false"
		
	fanart2 = setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom)
	if fanart2 != "": liz.setProperty('Fanart_Image', fanart2)
		
	menu = []
	#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	
	text = "addonID" + space2 + str(addonID) + newline + "name" + space2 + str(name) + newline + "url " + space2 + str(url) + newline + "url2" + space2 + str(url2) + newline + "mode" + space2 + str(mode) + newline + "iconimage" + space2 + str(iconimage) + newline + "desc" + space2 + str(desc) + newline + "num" + space2 + str(num)
	printlog(title='addDir_test1', printpoint=printpoint, text=text, level=0, option="")
	
	if addonID == 'script.featherence.install':
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
	elif mode >= 100 and mode <= 139 or mode >= 10001:
		menu.append(('Set Custom Fanart', 'RunScript(script.featherence.service,,?mode=34&value='+str(addonID)+'&value2='+str(mode)+')'))
		if getsetting('Fanart_Custom'+str(mode)) != "": menu.append(('Remove Custom Fanart', 'RunScript(script.featherence.service,,?mode=35&value='+str(addonID)+'&value2='+str(mode)+')'))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
	elif mode == 2 or mode == 4 or mode == 3:
		'''------------------------------
		---play_video/2------------------
		------------------------------'''
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 5:
		'''------------------------------
		---PlayMultiVideos-(list)--------
		------------------------------'''
		if admin:
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.featherence.kids/?&mode=5&url=%s)"% (url)))
			#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://%s/?num&iconimage=''&mode=6&name=''&url=%s)"% (addonID, url)))
			#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://plugin.video.featherence.kids/?&mode=5&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?iconimage="+iconimage+"&mode=5&name="+name+"&num="+num+"&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.featherence.kids/?iconimage=http%3a%2f%2fmsc.wcdn.co.il%2fw-2-1%2fw-300%2f768225-54.jpg&mode=5&name=%d7%94%d7%9b%d7%91%d7%a9%d7%94%20%d7%a9%d7%95%d7%a9%d7%a0%d7%94&num=1&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d&viewtype=50)"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?&mode=5&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d)"))
			liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 6:
		'''------------------------------
		---ListMultiVideos-(play)--------
		------------------------------'''
		if admin:
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.featherence.kids/?&mode=5&url=%s)"% (url2)))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?iconimage="+iconimage+"&mode=5&name="+name+"&num="+num+"&url="+url+")"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://plugin.video.featherence.kids/?iconimage=http%3a%2f%2fmsc.wcdn.co.il%2fw-2-1%2fw-300%2f768225-54.jpg&mode=5&name=%d7%94%d7%9b%d7%91%d7%a9%d7%94%20%d7%a9%d7%95%d7%a9%d7%a0%d7%94&num=1&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d&viewtype=50)"))
			#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://"+addonID+"/?&mode=5&url=%5b%27shuffle%3dtrue%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819037%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%201%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819043%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%202%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2819050%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx99%5cxd7%5cx99%5cxd7%5cxa4%5cxd7%5cxaa%20%5cxd7%5cxa9%5cxd7%5cx9c%20%5cxd7%5cx93%5cxd7%5cxa5%20%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20-%20%5cxd7%5cx97%5cxd7%5cx9c%5cxd7%5cxa7%203%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817560%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx9c%5cxd7%5cx95%5cxd7%5cx9d%20%5cxd7%5cxa2%5cxd7%5cx9c%20%5cxd7%5cx99%5cxd7%5cxa9%5cxd7%5cxa8%5cxd7%5cx90%5cxd7%5cx9c%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817583%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx95%5cxd7%5cx97%5cxd7%5cx91%5cxd7%5cxa8%5cxd7%5cx99%5cxd7%5cx9d%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2817533%26mode%3d10%26name%3d%5cxd7%5cx94%5cxd7%5cx9b%5cxd7%5cx91%5cxd7%5cxa9%5cxd7%5cx94%20%5cxd7%5cxa9%5cxd7%5cx95%5cxd7%5cxa9%5cxd7%5cxa0%5cxd7%5cx94%20%5cxd7%5cx91%5cxd7%5cx92%5cxd7%5cx9f%20%5cxd7%5cx94%5cxd7%5cx90%5cxd7%5cx95%5cxd7%5cxaa%5cxd7%5cx99%5cxd7%5cx95%5cxd7%5cxaa%26module%3dwallavod%27%2c%20%27%26custom%3dplugin%3a%2f%2fplugin.video.wallaNew.video%2f%3furl%3ditem_id%253D2820067%26mode%3d10%26name%3d%5cxd7%5cx91%5cxd7%5cx90%20%5cxd7%5cx9c%5cxd7%5cx99%20%5cxd7%5cx9e%5cxd7%5cxa1%5cxd7%5cx99%5cxd7%5cx91%5cxd7%5cx94%20%5cxd7%5cx9c%5cxd7%5cx99%26module%3dwallavod%27%5d)"))
			liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 12:
		'''------------------------------
		---View-Playlist-----------------
		------------------------------'''
		#url=urllib.unquote(url)
		#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://plugin.video.featherence.kids/?num&iconimage=''&mode=13&name=''&url=%s)"% (url)))
		#menu.append(('[COLOR=Purple]' + str79522.encode('utf-8') + '[/COLOR]', "XBMC.Container.Update(plugin://%s/?num&iconimage=''&mode=13&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 9:
		'''------------------------------
		---TV-MODE-----------------------
		------------------------------'''
		#menu.append(('[COLOR=Green]' + str79525.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://%s/?num&iconimage=''&mode=15&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 8 or mode == 10:
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
		returned = ok
		'''---------------------------'''
	elif mode == 11 or mode == 15:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 13:
		#menu.append(('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]', "XBMC.RunPlugin(plugin://%s/?num&iconimage=''&mode=12&name=''&url=%s)"% (addonID, url)))
		liz.addContextMenuItems(items=menu, replaceItems=False)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 17:
		'''------------------------------
		---TV-MODE-2---------------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 18:
		'''------------------------------
		---TV-MODE-2+CUSTOM--------------
		------------------------------'''
		up, down = CheckMoveCustom(name, num)
		
		if up != "": menu.append(("Move Up", "XBMC.RunPlugin(plugin://%s/?url=%s&mode=23&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)" % (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num + "__" + up, viewtype, urllib.quote_plus(fanart)))) #Move Up
		if down != "": menu.append(("Move Down", "XBMC.RunPlugin(plugin://%s/?url=%s&mode=23&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)" % (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num + "__" + down, viewtype, fanart))) #Move Down
		#u=sys.argv[0]+"?url="+str(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&desc="+urllib.quote_plus(desc)+"&num="+urllib.quote_plus(num)+"&viewtype="+str(viewtype)
		
		#menu.append((localize(16106), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=21&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, url, name, iconimage, desc, num, viewtype, fanart))) #Manage....
		
		menu.append((localize(16106), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=21&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Manage....
		menu.append((localize(33063), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=22&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Options....
		liz.addContextMenuItems(items=menu, replaceItems=True)
		if url == "None": ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		else: ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 20:
		'''------------------------------
		---New-Custom-Playlist-----------
		------------------------------'''
		menu.append((localize(33063), "XBMC.RunPlugin(plugin://%s/?url=%s&mode=22&name=%s&iconimage=%s&desc=%s&num=%s&viewtype=%s&fanart=%s)"% (addonID, urllib.quote_plus(url), urllib.quote_plus(name), iconimage, urllib.quote_plus(desc), num, viewtype, fanart))) #Options....
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		returned = ok
		'''---------------------------'''
	elif mode == 21:
		'''------------------------------
		---Manage...---------------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	elif mode == 22:
		'''------------------------------
		---AdvancedCustom...-------------
		------------------------------'''
		liz.addContextMenuItems(items=menu, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
		'''---------------------------'''
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		returned = ok
	
	text = "name" + space2 + str(name) + newline + \
	"desc" + space2 + str(desc) + space + "addonID" + space2 + str(addonID) + newline + \
	"iconimage" + space2 + str(iconimage) + newline + \
	"num" + space2 + str(num) + newline + \
	"fanart" + space2 + str(fanart) + extra
	printlog(title='addDir', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return returned
	
def addVideoLink(name, url, mode, iconimage='DefaultFolder.png', desc=""):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + name 
	#u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + name + "&iconimage="+str(iconimage)+"&desc="+str(desc)+"&desc="+str(desc)+"&desc="+str(desc)
	#u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode="+ str(mode) #SPOTIFY/BESTOFYOUTUBE
	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": urllib.unquote(name), "Plot": urllib.unquote(desc)})    
	liz.setProperty('IsPlayable', 'true')
	ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
	text = "ok" + space2 + str(ok) + space + "u" + space2 + str(u)
	printlog(title='addVideoLink', printpoint="", text=text, level=0, option="")
	'''---------------------------'''
	return ok
		
def addLink(name, url, iconimage="", desc="", viewtype=""):
	printpoint = ""
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc})
	liz.setProperty("IsPlayable","true")
	
	if "plugin://plugin.video.youtube/playlist/" in url:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=True)
		printpoint = printpoint + "1"
	elif '&dailymotion_id' in url:
		url = url.replace("&dailymotion_id=","")
		url = 'http://www.dailymotion.com/video/x3bik3i'
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
		printpoint = printpoint + "2"
	text = "ok" + space2 + str(ok) + space + "name" + space2 + str(name) + space + "url" + space2 + str(url) + space
	printlog(title='addLink', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return ok, liz
	
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
				params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
					param[splitparams[0]]=splitparams[1]
							
	return param

def InstallAddon_(url, viewtype):
	addon = ""
	if '&addon=' in url:
		addon = find_string(url, '&addon=', '&') ; url = url.replace(addon,"") ; addon = addon.replace('&addon=',"") ; addon = addon.replace('&',"")
		installaddon(admin, addon, update=True)
	
	if addon == "" or (xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(os.path.join(addons_path, addon))):
		update_view(url, num, viewtype)
	else:
		notification_common("24")
	print 'InstallAddon_' + space + 'addon' + space2 + str(addon)
	
	return url
	
def ListLive(url):
	#addDir('[COLOR=Yellow]' + str79520.encode('utf-8') + '[/COLOR]',url,12,addonMediaPath + "190.png",str79526.encode('utf-8'),'1',"") #Quick-Play
	link = OPEN_URL(url)
	link=unescape(link)
	print printfirst + "link" + space2 + link
	matches1=re.compile('pe=(.*?)#',re.I+re.M+re.U+re.S).findall(link)
	#print str(matches1[0]) + '\n'
	for match in matches1 :
		#print "match=" + str(match)
		match=match+'#'
		if match.find('playlist') != 0 :
			'''------------------------------
			---url---------------------------
			------------------------------'''
			regex='name=(.*?)URL=(.*?)#'
			matches=re.compile(regex,re.I+re.M+re.U+re.S).findall(match)
			#print str(matches)
			for name,url in matches:
				thumb=''
				i=name.find('thumb')
				i2=name.find('description')
				if i>0:
					thumb=name[i+6:]
					name=name[0:i]
					description = name[i2+11:]
					print printfirst + "name" + space2 + name + space + "thumb" + space2 + thumb + space + "description" + space2 + description
		#print url
				addLink('[COLOR yellow]'+ name+'[/COLOR]',url,thumb,description,"")  
			
		else:
			'''------------------------------
			---.plx--------------------------
			------------------------------'''
			regex='name=(.*?)URL=(.*?).plx'
			matches=re.compile(regex,re.I+re.M+re.U+re.S).findall(match)
			for name,url in matches:
				thumb=''
				i=name.find('thumb')
				i2=name.find('description')
				if i>0:
					thumb=name[i+6:]
					name=name[0:i]
					description = name[i2+11:]
				url=url+'.plx'
				if name.find('Radio') < 0 :
					addDir('[COLOR blue]'+name+'[/COLOR]',url,7,thumb,description,'1',"")
					
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "matches1" + space2 + str(matches1)
	printlog(title='ListLive', printpoint="", text=text, level=0, option="")
	'''---------------------------'''

def clean_commonsearch(x):
	y = x
	if "commonsearch" in y:
		if addonID == 'plugin.video.featherence.music':
			y = y.replace("commonsearch101", space + commonsearch101)
			y = y.replace("commonsearch102", space + commonsearch102)
			y = y.replace("commonsearch104", space + commonsearch104)
			y = y.replace("commonsearch106", space + commonsearch106)
			y = y.replace("commonsearch107", space + commonsearch107)
			y = y.replace("commonsearch108", space + commonsearch109)
			
			y = y.replace("commonsearch111", space + commonsearch111)
			y = y.replace("commonsearch112", space + commonsearch112)
			y = y.replace("commonsearch114", space + commonsearch114)
	
	if "[COLOR" in y or "[/COLOR" in y:
		y = y.replace("[COLOR=Green]", "")
		y = y.replace("[COLOR=Yellow]", "")
		y = y.replace("[COLOR=White]", "")
		y = y.replace("[/COLOR]", "")
	
	y = y.replace(" ","%20")
	
	text = "x" + str(x) + space + "y" + space2 + str(y)
	printlog(title='clean_commonsearch', printpoint="", text=text, level=0, option="")
	return y

def LocalSearch(mode, name, url, iconimage, desc, num, viewtype):
	printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; value = "" ; url2 = ""
	url2 = read_from_file(url, silent=True, lines=True, retry=True, printpoint="", addlines='&custom_se=', createlist=False)
	text = 'url2' + space2 + str(url2)
	printlog(title='LocalSearch' + space + name, printpoint=printpoint, text=text, level=0, option="")
	TvMode2(mode, name, url2, iconimage, desc, num, viewtype)
		
def YoutubeSearch(name, url, desc, num, viewtype):
	printpoint = "" ; admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; value = "" ; url2 = ""

	name = clean_commonsearch(name)
	url = clean_commonsearch(url)
	
	try: url = str(url).encode('utf-8')
	except: pass
	try: name = str(name).encode('utf-8')
	except: pass
	if name == localize(137):
		'''search'''
		printpoint = printpoint + "1"
		url2 = url.replace("%20", "")
		#print url2
		x = desc
		#addonString_servicefeatherence(23).encode('utf-8') % (url2)
		returned = dialogkeyboard("", x, 0, '1', "", "")
		if returned != 'skip':
			value = returned + space + url2
		else:
			notification_common("8")
	else:
		'''commonsearch'''
		printpoint = printpoint + "2"
		value = name + space + url
	
	if value != "": update_view('plugin://plugin.video.youtube/search/?q=' + value, num, viewtype)
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "value" + space2 + str(value) + newline + \
	"url" + space2 + str(url) + newline + \
	"url2" + space2 + str(url2) + space 
	printlog(title='YoutubeSearch', printpoint="", text=text, level=0, option="")
	'''---------------------------'''
	
def ListPlaylist2(playlistid, num, viewtype):
	default = 'plugin://plugin.video.youtube/'
	update_view('plugin://plugin.video.youtube/playlist/' + playlistid + '/', num, viewtype)
	'''---------------------------'''
	
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    '''---------------------------'''
    return link

def play_video(url):
	#xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
	#match=re.compile("http\://www.youtube.com/watch\?v\=([^\&]+)\&.+?<media\:descriptio[^>]+>([^<]+)</media\:description>.+?<media\:thumbnail url='([^']+)'.+?<media:title type='plain'>(.+?)/media:title>").findall(link)
	url='https://gdata.youtube.com/feeds/api/videos/'+ url +''
	#url='https://gdata.youtube.com/feeds/api/videos/'+ url +'' + '?alt=json'
	#url='plugin://plugin.video.youtube/play/?video_id='+ url +''
	link = OPEN_URL(url)
	prms=json.loads(link)
	
	match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').url
	finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
	title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
	thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
	description = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
	addLink(title,finalurl,thumb,description,"")
	#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
	text = "link" + space2 + link + space + "url" + space2 + url
	printlog(title='play_video', printpoint="", text=text, level=0, option="")

def play_video2(url):
	
	if 'plugin.video.wallaNew.video' in url: xbmc.executebuiltin('PlayMedia('+ url +')')
	elif '&dailymotion_id' in url:
		addon = "plugin.video.dailymotion_com"
		if not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or not os.path.exists(os.path.join(addons_path, addon)):
			installaddonP(admin, addon) ; xbmc.sleep(1000)
			
		url = url.replace("&dailymotion_id=","")
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.dailymotion_com/?url='+url+'&mode=playVideo)')
		
		if 1 + 1 == 3:
			url = 'https://api.dailymotion.com/video/'+ url +''
			link = OPEN_URL(url)
			prms=json.loads(link)
			
			title = str(prms['title'].encode('utf-8'))#.decode('utf-8')
			id = str(prms['id'].encode('utf-8'))#.decode('utf-8')
			channel = str(prms['channel'].encode('utf-8'))#.decode('utf-8')
			#name = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
			finalurl='http://www.dailymotion.com/video/'+id+'_'+title+'_'+channel
			finalurl = finalurl.replace(space,"-")
			finalurl = 'http://www.dailymotion.com/video/x3bik3i_atlas-unfolded-new-york-city_music'
			print 'link :' + str(link) + newline + 'prms:' + str(prms) + newline + 'title:' + str(title) + newline + 'id' + space2 + str(id) + newline + 'finalurl' + space2 + str(finalurl)
	
	elif '&youtube_id' in url:
		url = url.replace("&youtube_id=","")
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
	else:
		xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id='+ url +')')
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "play_video2" + space + "url" + space2 + str(url)
	printlog(title='play_video2', printpoint="", text=text, level=0, option="")
	'''---------------------------'''

def YOULink(mname, url, thumb, desc):
	if not "UKY3scPIMd8" in url or admin:
		ok=True
		url = "plugin://plugin.video.youtube/play/?video_id="+url
		#url='https://gdata.youtube.com/feeds/api/videos/'+url+'?alt=json&max-results=50' #TEST
		liz=xbmcgui.ListItem(mname, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": mname, "Plot": desc } )
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
		text = "url" + space2 + str(url) + space + "mname" + space2 + mname
		printlog(title='YOULink', printpoint="", text=text, level=0, option="")
		return ok
		
def MultiVideos(mode, name, url, iconimage, desc, num, viewtype):
	printpoint = "" ; i = 0 ; i2 = 0 ; extra = "" ; desc = str(desc)
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	playlist = []
	
	url2 = url.replace("['","")
	url2 = url2.replace("']","")
	url2 = url2.replace("'","")
	url2 = url2.replace("' ","'")
	url2 = url2.replace("'',","")
	
	url2 = url2.replace("&amp;", "&")
	
	url2 = url2.replace(" &custom","&custom")
	url2 = url2.replace(" &custom_se","&custom_se")
	url2 = url2.replace(" &dailymotion_id=","&dailymotion_id=")
	url2 = url2.replace(" &hotVOD","&hotVOD")
	url2 = url2.replace(" &sdarot","&sdarot")
	url2 = url2.replace(" &seretil","&seretil")
	url2 = url2.replace(" &wallaNew2","&wallaNew2")
	url2 = url2.replace(" &wallaNew","&wallaNew")
	
	url2 = url2.replace(" &youtube_ch","&youtube_ch")
	url2 = url2.replace(" &youtube_pl","&youtube_pl")
	url2 = url2.replace(" &youtube_id","&youtube_id")
	url2 = url2.replace(" &youtube_se","&youtube_se")
	
	url2a = url2
	url2 = url2.split(',')
	if General_TVModeShuffle == "true" and mode == 5: random.shuffle(url2) ; printpoint = printpoint + "0"
		
		
	text = "url " + space2 + str(url) + newline + "url2a" + space2 + str(url2a) + newline + "url2" + space2 + str(url2)
	printlog(title='url_first_check', printpoint="", text=text, level=0, option="")
	#returned = get_types(url)
	counturl2 = 0
	for x in url2:
		x = str(x) ; finalurl = "" ; finalurlL = [] ; numOfItems2 = 0 ; name2 = ""
		x = url2[counturl2]
		counturl2 += 1
		text = "x" + space2 + str(x) + newline + "playlist" + space + str(playlist) + newline + "finalurl" + space2 + str(finalurl) + space + "finalurlL" + space2 + str(finalurlL)
		printlog(title='MultiVideos_test', printpoint=printpoint, text=text, level=0, option="")
		x = x.replace("[","")
		x = x.replace(",","")
		x = x.replace("'","")
		x = x.replace("]","")
		
		if '&name=' in x:
			name2 = find_string(x, '&name=', '&')
			x = x.replace(name2,"",1)
			name2 = name2.replace('&name=',"",1)
			name2 = name2.replace('&',"")
			name2 = space + '(' + name2 + ')'
			
		if x not in playlist and x != "":
			i += 1
			if mode == 5:
				if "&custom=" in x:
					x = x.replace("&custom=","")
					finalurl=x
					'''---------------------------'''
				elif "&dailymotion_id=" in x:
					x = x.replace("&dailymotion_id=","")
					finalurl='plugin://plugin.video.dailymotion_com/?url='+x+'&mode=playVideo'
				elif "&hotVOD=" in x:
					x = x.replace("&hotVOD=","")
					if "FCmmAppVideoApi_AjaxItems" in x:
						finalurl="plugin://plugin.video.hotVOD.video/?url="+x+"&mode=4"
						'''---------------------------'''
				elif "&sdarot=" in x:
					x = x.replace("&sdarot=","")
					#finalurl="plugin://plugin.video.sdarot.tv/?mode=4&"+x
					'''---------------------------'''
				elif "&seretil=" in x:
					x = x.replace("&seretil=","")
					#finalurl="plugin://plugin.video.sdarot.tv/?mode=4&"+x
					'''---------------------------'''
				elif "&wallaNew=" in x:
					x = x.replace("&wallaNew=","")
					if "item_id" in x: finalurl="plugin://plugin.video.wallaNew.video/?url="+x+"&mode=10&module=wallavod"
					'''---------------------------'''
				elif "&wallaNew2=" in x:
					x = x.replace("&wallaNew2=","")
					#z = '1'
					#addDir(name + space + str(i), "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=nickjr", 8, iconimage, desc, num, viewtype)
					'''---------------------------'''
				elif "&youtube_ch=" in x:
					#i2 += 1
					#x = x.replace("&youtube_ch=","")
					try: finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					#finalurl="plugin://plugin.video.youtube/play/?playlist_id="+x+""
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					#i2 += 1
					#x = x.replace("&youtube_pl=","")
					#finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					try: finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					#finalurl="plugin://plugin.video.youtube/play/?playlist_id="+x+""
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					finalurl="plugin://plugin.video.youtube/play/?video_id="+x+"&hd=1"
					'''---------------------------'''
				elif "&youtube_se=" in x or "&custom_se=" in x:
					#try: str(name).encode('utf-8')
					#except: str(name)
					#x = x.replace("&youtube_se=","")
					if '&youtube_se=' in x: x = x + space + str(name)
					#print 'xxx' + str(x)
					try: finalurlL, numOfItems2 = youtube_pl_to_youtube_id(x, playlist)
					except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "6"
					#finalurl="plugin://plugin.video.youtube/play/?video_id="+x+"&hd=1"
					'''---------------------------'''
					
				if admin: extra = extra + newline + str(i) + space2 + str(finalurl)
				'''---------------------------'''
				#title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
				#thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
				#description = str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
				
				if finalurl != "" or finalurlL != []:
					returned = get_types(finalurl)
					returned2 = get_types(finalurlL)
					count = 0
					if finalurlL != [] and 'list' in returned2:
						if General_TVModeShuffle == "true" and mode == 5: random.shuffle(finalurlL) ; printpoint = printpoint + "0"
						#finalurlL2 = str(finalurlL)
						#finalurlL2 = finalurlL2.split(',')
						if numOfItems2 > 0:
							for y in finalurlL:
								count += 1
								#if not y in playlist:
								pl.add(y)
								playlist.append(y)
								if not "3" in printpoint:
									printpoint = printpoint + "3"
									xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl) ; xbmc.sleep(2000)
									'''---------------------------'''
								#else:
								#print "aaa " + "y" + space2 + str(y) + space + "playist" + space2 + str(playlist)
								
								
								if count >= numOfItems2: break
								text = "i" + space2 + str(i) + space + "y" + space2 + str(y) + space + "count" + space2 + str(count) + newline + "finalurlL" + space2 + str(finalurlL) + newline + 'numOfItems2' + space2 + str(numOfItems2)
								printlog(title='MultiVideos_test2', printpoint=printpoint, text=text, level=0, option="")
							
					elif finalurl != "" and 'str' in returned:	
						#if not y in playlist:
						pl.add(finalurl)
						playlist.append(finalurl)
						if not "3" in printpoint:
							printpoint = printpoint + "3"
							xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
							'''---------------------------'''
					else: printpoint = printpoint + "9"
					
					text = "i" + space2 + str(i) + space + "count" + space2 + str(count) + space + "playlist" + space2 + str(playlist)
					printlog(title='MultiVideos_test3', printpoint=printpoint, text=text, level=0, option="")
				if '3' in printpoint:
					playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
					playlistlength = xbmc.getInfoLabel('Playlist.Length(video)')
					if not playerhasvideo or int(playlistlength) >= 40:
						'''Probably Cancel'''
						printpoint = printpoint + 'q'
						break
				
			elif mode == 6:
				#try:
				finalurl, id, name, iconimage, desc = getAPIdata(x, name, iconimage, desc)
							
				#except: pass
				
				if "&dailymotion_id=" in x:
					#x = x.replace("&dailymotion_id=","")
					addDir(str(i) + '.' + space + name + space + name2, x, 4, iconimage, desc, num, viewtype)
					'''---------------------------'''
				elif "&youtube_ch=" in x:
					x = x.replace("&youtube_ch=","")
					if "/playlists" in x: x = x.replace("/playlists","")
					addDir(str(i) + '.' + space + name + space + name2, x, 9, iconimage, desc, num, viewtype) #addonString(192).encode('utf-8')
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					i2 += 1
					x = x.replace("&youtube_pl=","")
					addDir(str(i) + '.' + space + name + space + name2, x, 13, iconimage, desc, num, viewtype) #addonString(192).encode('utf-8')
					'''---------------------------'''
				elif "&youtube_id=" in x:
					#x = x.replace("&youtube_id=","")
					addDir(str(i) + '.' + space + name + space + name2, x, 4, iconimage, desc, num, viewtype)
					'''---------------------------'''
				elif "&youtube_se=" in x or "&custom_se=" in x:
					#try: str(name).encode('utf-8')
					#except: str(name)
					x = x.replace("&youtube_se=","")
					x = x.replace("&custom_se=","")
					x = x + space + str(name)
					x = clean_commonsearch(x)
					addDir(str(i) + '.' + space + name + space + name2, x, 3, iconimage, desc, num, viewtype)
					'''---------------------------'''	
				else:
					if "&wallaNew=" in x:
						x = x.replace("&wallaNew=","")
						if "item_id" in x: z = '10'
						elif "seriesId" in x: z = '5'
						elif "seasonId" in x: z = '3'
						elif "genreId" in x: z = '2'
						else: z = '10'
						addDir(str(i) + '.' + space + name + space + name2, "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=wallavod", 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&wallaNew2=" in x:
						x = x.replace("&wallaNew2=","")
						z = '1'
						addDir(str(i) + '.' + space + name + space + name2, "plugin://plugin.video.wallaNew.video/?url="+x+"&mode="+z+"&module=nickjr", 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&sdarot=" in x:
						x = x.replace("&sdarot=","")
						if "episode_id=" in url: z = '4'
						elif "season_id" in url: z = '5'
						elif "series_id=" in url: z = '3'
						else: z = '2'
						
						if 1 + 1 == 2:
							if not "summary=" in x:
								if z == '3':
									if not "summary" in x: summary = "&summary"
									else: summary = ''
								else: summary = "&summary="
								#elif desc != "": summary = "&summary="+desc
							else: summary = ''
						else: summary = ''
						
						text = "Testing x" + space2 + newline + \
						"x" + space2 + str(x) + newline + \
						"z" + space2 + str(z) + newline + \
						"summary" + space2 + str(summary) + newline
						printlog(title='MultiVideos_test4', printpoint=printpoint, text=text, level=0, option="")
							
						
						if not "series_name=" in x: series_name = "&series_name="
						else: series_name = ''
						addDir(str(i) + '.' + space + name + space + name2, "plugin://plugin.video.sdarot.tv/?mode="+z+summary+series_name+"&image="+iconimage+"&name="+name+"&"+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&seretil=" in x:
						x = x.replace("&seretil=","")
						if "?mode=211&url=http%3a%2f%2fseretil.me" in x: name2 = '[COLOR=Red]' + name + space + str(i) + '[/COLOR]'
						else: name2 = name + space + str(i)
						addDir(name2, "plugin://plugin.video.seretil/"+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''
					elif "&hotVOD=" in x:
						x = x.replace("&hotVOD=","")
						if "TopSeriesPlayer" in x: z = '3&module=%2fCmn%2fApp%2fVideo%2fCmmAppVideoApi_AjaxItems%2f0%2c13776%2c'
						elif "FCmmAppVideoApi_AjaxItems" in x: z = '4'
						else: z = '3&module=%2fCmn%2fApp%2fVideo%2fCmmAppVideoApi_AjaxItems%2f0%2c13776%2c'
						addDir(str(i) + '.' + space + name + space + name2, "plugin://plugin.video.hotVOD.video/?mode="+z+"&url="+x, 8, iconimage, desc, num, viewtype)
						'''---------------------------'''	
						
					elif "&custom=" in x:
						x = x.replace("&custom=","")
						addLink(str(i) + '.' + space + name + space + name2, x, iconimage, desc, viewtype)
						'''---------------------------'''
					else: addLink(str(i) + '.' + space + name + space + name2, x, iconimage, desc, viewtype)
		
		
	if mode == 5:
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		if playlist == []: notification(addonString_servicefeatherence(1).encode('utf-8'), addonString_servicefeatherence(2).encode('utf-8'), "", 2000)
		#xbmc.executebuiltin('RunScript('+addonID+'/?mode=6&name='+name+'&url='+url+'&iconimage='+str(iconimage)+'&desc='+desc+'&num='+str(num)+'&viewtype='+str(viewtype)+')')
		#MultiVideos(6, name, url, iconimage, desc, num, viewtype)
		
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "mode" + space2 + str(mode) + space + "i" + space2 + str(i) + space + newline + \
	"url " + space2 + str(url) + newline + \
	"url2" + space2 + str(url2) + newline + \
	"pl" + space2 + str(pl) + space + "playlist" + space2 + str(playlist) + newline + \
	"finalurl" + space2 + str(finalurl) + space + "finalurlL" + space2 + str(finalurlL) + space + newline + extra
	printlog(title="MultiVideos", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''
		
def getAPIdata(x, name, iconimage, desc):
	printpoint = "" ; TypeError = "" ; extra = ""
	finalurl = "" ; url = "" ; prms = "" ; id = ""
	try:
		if '&youtube_pl=' in x:
			x2 = x.replace('&youtube_pl=',"")
			url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+x2+'&key='+featherenceapi+'&part=snippet&maxResults=40&pageToken='
			#url = 'https://www.googleapis.com/youtube/v3/playlists?id='+x2+'&key='+featherenceapi+'&part=snippet&maxResults=1&pageToken='
		elif '&youtube_ch=' in x:
			x2 = x.replace('&youtube_ch=',"")
			url = 'https://www.googleapis.com/youtube/v3/channels?forUsername='+x2+'&key='+featherenceapi+'&part=snippet&maxResults=1'
			link = OPEN_URL(url)
			#print 'link__' + space2 + str(link)
			if '"totalResults": 0' in link or '"items": []' in link:
				url = 'https://www.googleapis.com/youtube/v3/channels?id='+x2+'&key='+featherenceapi+'&part=snippet&maxResults=1'
			
		elif '&youtube_id=' in x:
			x2 = x.replace('&youtube_id=',"")
			url = 'https://www.googleapis.com/youtube/v3/videos?id='+x2+'&key='+featherenceapi+'&part=snippet'
		elif '&youtube_se' in x:
			x2 = x.replace('&youtube_se=',"")
			url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+featherenceapi+'&safeSearch=moderate&type=video&part=snippet&maxResults=40&pageToken='
		elif '&custom_se' in x:
			x2 = x.replace('&custom_se',"")
			url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+featherenceapi+'&safeSearch=moderate&type=video&part=snippet&maxResults=1&pageToken='
		
		if url != "":
			link = OPEN_URL(url)
			prms=json.loads(link)
			printlog(title='getAPIdata_test1', printpoint=printpoint, text=str(link), level=0, option="")
			i = 0
			if '&youtube_pl' in x:
				#id=str(prms['items'][i][u'id']) #Video ID (Playlist)
				id=str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
				#id=str(prms['items'][i][u'snippet'][u'playlistId']) #Video ID (Playlist)
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
			elif '&youtube_ch' in x:
				id=str(prms['items'][i][u'id']) #Video ID (Playlist)
				#id=str(prms['items'][i][u'snippet'][u'playlistId']) #Video ID (Playlist)
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
			elif '&youtube_id' in x:
				id=str(prms['items'][i][u'id']) #Video ID ()
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
					
			elif '&youtube_se' in x:
				id=str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
				
				
				
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	text = 'x' + space2 + str(x) + newline + \
	'prms' + space2 + str(prms) + newline + \
	'finalurl' + space2 + str(finalurl) + newline + \
	'name' + space2 + str(name) + newline + \
	'iconimage' + space2 + str(iconimage) + newline + \
	'desc' + space2 + str(desc) + extra
	
	printlog(title="getAPIdata", printpoint=printpoint, text=text, level=0, option="")
	return str(finalurl), str(id), str(name), str(iconimage), str(desc)
	
def PlayPlayList(playlistid):
	printpoint = ""
	url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=40'
	link = OPEN_URL(url)
	prms=json.loads(link)

	playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	playlist.clear()
	playlist1 = []
	numOfItems=int(prms['feed'][u'openSearch$totalResults'][u'$t']) #if bigger than 40 needs  to add more result
	
	j=1
	h=1
	pages = (numOfItems //50)+1
	while  j<= pages:
		link=OPEN_URL(url)
		prms=json.loads(link)
		i=0
		while i< 50  and  h<numOfItems :
			try:
				urlPlaylist= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$player'][0][u'url'])
				match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(urlPlaylist)
				#finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
				finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1"
				title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
				thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
				liz = xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage=thumb)
				liz.setInfo( type="Video", infoLabels={ "Title": title} )
				liz.setProperty("IsPlayable","true")
				playlist1.append((finalurl ,liz))
			except:
				pass
			if playlist1 != [] and not "3" in printpoint:
				for blob ,liz in playlist1:
					try:
						if blob:
							playlist.add(blob,liz)
							xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playlist)
							printpoint = printpoint + "3"
							xbmc.sleep(2000)
					except:
						printpoint = printpoint + "4"
				
				
			i=i+1
			h=h+1

		j=j+1
		url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=50&start-index='+str (j*50-49)
	random.shuffle(playlist1)
	for blob ,liz in playlist1:
		try:
			if blob:
				playlist.add(blob,liz)
		except:
			pass
	notification_common("15")
	playlist.shuffle()
	
	#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(playlist)

	#https://gdata.youtube.com/feeds/api/users/polosoft/playlists (gets playlist fro, user) https://gdata.youtube.com/feeds/api/users/polosoft/playlists?alt=json
	#https://gdata.youtube.com/feeds/api/playlists/PLN0EJVTzRDL_53Jz8bhZl4m3UtkY2btbV?max-results=50?alt=json  (gets items in playlist)
	#https://gdata.youtube.com/feeds/api/playlists/PLN0EJVTzRDL_53Jz8bhZl4m3UtkY2btbV?max-results=50&alt=json
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "playlistid" + space2 + playlistid + space + "numOfItems" + space2 + str(numOfItems) + space + "playlist1" + space2 + str(playlist1)
	printlog(title='PlayPlayList', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def PlayPlayList2(playlistid):
	default = 'plugin://plugin.video.youtube/'
	default2 = 'play/?playlist_id='

	xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?playlist_id='+ playlistid +')')
	#addLink("",'plugin://plugin.video.youtube/play/?playlist_id=' + playlistid,"","","")
	#xbmc.executebuiltin('RunPlugin(plugin://plugin.video.youtube/play/?playlist_id='+ playlistid +'&order=default)')
	#plugin://plugin.video.youtube/playlist/PL4RuBaWCIgHrFNTIP37qBS254y7-2r9e4/
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "playlistid" + space2 + str(playlistid)
	printlog(title="PlayPlayList2", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''

def PlayPlayList3(playlistid):
	default = 'plugin://plugin.video.youtube/'
	default2 = 'play/?playlist_id='
	update_view(default + default2 + playlistid + '/', num, viewtype)
	'''---------------------------'''
	
def getCustom_Playlist(admin):
	#from variables import Custom_Playlist1
	returned = "" ; printpoint = ""
	if Custom_Playlist1_ID  == "": returned = 'Custom_Playlist1_ID'
	elif Custom_Playlist2_ID  == "": returned = 'Custom_Playlist2_ID'
	elif Custom_Playlist3_ID  == "": returned = 'Custom_Playlist3_ID'
	elif Custom_Playlist4_ID  == "": returned = 'Custom_Playlist4_ID'
	elif Custom_Playlist5_ID  == "": returned = 'Custom_Playlist5_ID'
	elif Custom_Playlist6_ID  == "": returned = 'Custom_Playlist6_ID'
	elif Custom_Playlist7_ID  == "": returned = 'Custom_Playlist7_ID'
	elif Custom_Playlist8_ID  == "": returned = 'Custom_Playlist8_ID'
	elif Custom_Playlist9_ID  == "": returned = 'Custom_Playlist9_ID'
	elif Custom_Playlist10_ID  == "": returned = 'Custom_Playlist10_ID'
	'''---------------------------'''
	text = "returned" + space2 + str(returned) + space + "Custom_Playlist1_ID" + space2 + str(Custom_Playlist1_ID)
	printlog(title="getCustom_Playlist", printpoint=printpoint, text=text, level=2, option="")
	return returned

def setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, num, viewtype):
	printpoint = "" ; extra = "" ; New_Type = ""
	if "&list=PL" in New_ID:
		'''Playlist'''
		New_Type = localize(559) #Playlist
		extra = addonString_servicefeatherence(47).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(49).encode('utf-8') #New %s, Update Succesfully!
		New_ID = find_string(New_ID, "&list=PL", "")
		New_ID = New_ID.replace("&list=","&youtube_pl=")
		New_ID_ = New_ID.replace("&youtube_pl=","")
		'''---------------------------'''
	elif "/user/" in New_ID or "/channel/" in New_ID:
		'''Channel'''
		New_Type = localize(19029) #Channel
		extra = addonString_servicefeatherence(46).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(48).encode('utf-8') #New %s, Update Succesfully!
		if "/channel/" in New_ID:
			New_ID = find_string(New_ID, "/channel/", "")
			New_ID = New_ID.replace("/channel/", "&youtube_ch=")
		elif "/user/"    in New_ID:
			New_ID = find_string(New_ID, "/user/", "")
			New_ID = New_ID.replace("/user/", "&youtube_ch=")
			
		New_ID_ = New_ID.replace("&youtube_ch=","")
		'''---------------------------'''
	elif "watch?v=" in New_ID:
		'''Single Video'''
		New_Type = localize(157) #Video
		extra = addonString_servicefeatherence(46).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(48).encode('utf-8') #New %s, Update Succesfully!
		New_ID = find_string(New_ID, "watch?v=", "")
		New_ID = New_ID.replace("watch?v=", "&youtube_id=")
		New_ID_ = New_ID.replace("&youtube_id=","")
		'''---------------------------'''
	
	elif New_ID == "None":
		New_Type = localize(2080) #Empty list
		extra = addonString_servicefeatherence(47).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(49).encode('utf-8') #New %s, Update Succesfully!
		New_ID_ = ""
		
	if New_Type != "":
		if New_ID in url:
			check = dialogyesno(addonString_servicefeatherence(93).encode('utf-8'), localize(19194)) # Duplicated URL found!, Continue?
			if check == "ok": pass				
			else: notification_common("9") ; printpoint = printpoint + "8"
		
		if not "8" in printpoint:
			if mode == 20:
				setsetting(Custom_Playlist_ID, New_ID)
			elif mode == 21:
				setsetting(Custom_Playlist_ID, str(url) + "," + New_ID)
				#extra = "Previous ID: " + str(url)		
			#extra = addonString_servicefeatherence(46).encode('utf-8') % (New_Type) + space + addonString_servicefeatherence(48).encode('utf-8')
			dialogok(extra, "ID: " + str(New_ID_), str(name), "") ; xbmc.sleep(100)
			update_view(url, num, viewtype)
			'''---------------------------'''

	else: notification_common("17")
	
	text = "name" + space2 + str(name) + newline + "New_Type" + space2 + str(New_Type) + space + "New_ID" + space2 + str(New_ID) + space + "New_ID_" + space2 + str(New_ID_)
	printlog(title="setCustom_Playlist_ID", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''

def AdvancedCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	'''------------------------------
	---Save and Load your addon-design
	------------------------------'''
	printpoint = "" ; extra = "" ; formula = "" ; formula_ = "" ; path = "" ; file1 = "" ; file2 = "" ; file3 = "" ; returned = "" ; returned2 = ""; returned3 = "" ; y = "s"
	
	if name == addonString(6).encode('utf-8'):
		list = ['-> (Exit)']
		list.append(localize(190) + space + localize(593)) #Save All
		list.append(addonString_servicefeatherence(51).encode('utf-8') + space + localize(593) + space + "[LOCAL]") #Load All [LOCAL]
		list.append(addonString_servicefeatherence(51).encode('utf-8') + space + localize(593) + space + "[REMOTE]") #Load All [REMOTE] 
		list.append(localize(10035) + space + localize(593)) #Reset All
		y = "s"
		'''---------------------------'''
	else:
		list = ['-> (Exit)']
		list.append(localize(190) + space + addonString_servicefeatherence(57).encode('utf-8')) #Save One
		list.append(addonString_servicefeatherence(51).encode('utf-8') + space + addonString_servicefeatherence(57).encode('utf-8') + space + "[LOCAL]") #Load One [LOCAL]
		list.append(addonString_servicefeatherence(51).encode('utf-8') + space + addonString_servicefeatherence(57).encode('utf-8') + space + "[REMOTE]") #Load One [REMOTE]
		y = ""
		
		Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
		if Custom_Playlist_ID == "": notification("Error ID", "Use featherence Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
		'''---------------------------'''
	returned, value = dialogselect(addonString_servicefeatherence(31).encode('utf-8'),list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		
		if returned == 1 or returned == 2: path = os.path.join(addondata_path, addonID, '')
		elif returned == 3: path = os.path.join(addonPath, 'resources', 'templates', '')
		elif returned == 4: pass
		else: path = ""
		
		if path != "":

			if returned == 3:
				check = dialogyesno(addonString_servicefeatherence(96).encode('utf-8') % addonString(100).encode('utf-8'), addonString_servicefeatherence(99).encode('utf-8')) #Share My Music buttons, Choose YES to learn how to share Your Music button
				if check == 'ok':
					header = addonString_servicefeatherence(96).encode('utf-8') % addonString(100).encode('utf-8')
					msg1 = localize(190) + space + localize(592) ; msg1.decode('utf-8').encode('utf-8') #; msg1 = '[B]' + msg1 + '[/B]'
					msg2 = os.path.join(addondata_path, addonID) ; msg2 = msg2.decode('utf-8').encode('utf-8')
					message = "1. " + addonString_servicefeatherence(95).encode('utf-8') % (msg1) + ".[CR]" + "2. " + addonString_servicefeatherence(97).encode('utf-8') + "[CR]" + msg2 + ".[CR]" + "3. " + addonString_servicefeatherence(52).encode('utf-8') + "[CR]" + "4. " + addonString_servicefeatherence(53).encode('utf-8') % ("templates") + "[CR]" + "5. " + addonString_servicefeatherence(54).encode('utf-8') + ".[CR]" + "6. " + addonString_servicefeatherence(98).encode('utf-8') + ".[CR]" + "7. " + addonString_servicefeatherence(55).encode('utf-8') + ".[CR]" + "8. " + addonString_servicefeatherence(56).encode('utf-8') % ("Commit") + ".[CR][CR]" + "*You should now wait for the next addon update."
					diaogtextviewer(header,message)
					
			'''read existing files'''
			file1 = os.path.join(path, "Addon_SavedButton"+y+"1.txt")
			file2 = os.path.join(path, "Addon_SavedButton"+y+"2.txt")
			file3 = os.path.join(path, "Addon_SavedButton"+y+"3.txt")
			'''---------------------------'''
			
			if os.path.exists(file1):
				infile1 = read_from_file(file1, silent=True)
				filename1 = regex_from_to(infile1, "&name=", "&", excluding=True)
			else: filename1 = None
			if os.path.exists(file2):
				infile2 = read_from_file(file2, silent=True)
				filename2 = regex_from_to(infile2, "&name=", "&", excluding=True)
			else: filename2 = None
			if os.path.exists(file3):
				infile3 = read_from_file(file3, silent=True)
				filename3 = regex_from_to(infile3, "&name=", "&", excluding=True)
				#print 'infile3' + space2 + str(infile3) + newline + 'filename3' + space2 + str(filename3)
			else: filename3 = None
			
			value1 = 'NO.' + space + "1" + space + "(" + str(filename1) + ")"
			value2 = 'NO.' + space + "2" + space + "(" + str(filename2) + ")"
			value3 = 'NO.' + space + "3" + space + "(" + str(filename3) + ")"
			
			'''save/load'''
			if filename1 == None: value1 = '[COLOR=Red]' + value1 + '[/COLOR]'
			if filename2 == None: value2 = '[COLOR=Red]' + value2 + '[/COLOR]'
			if filename3 == None: value3 = '[COLOR=Red]' + value3 + '[/COLOR]'
		
			list = ['-> (Exit)', value1, value2, value3]
				
			returned2, value2 = dialogselect(addonString_servicefeatherence(31).encode('utf-8'),list,0)
			
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
			
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				
				if returned2 == 1: printpoint = printpoint + "1" #1
				elif returned2 == 2: printpoint = printpoint + "2" #2
				elif returned2 == 3: printpoint = printpoint + "3" #3
				
				if returned == 1: printpoint = printpoint + "A" #SAVE
				elif returned == 2: printpoint = printpoint + "B" #LOAD
				elif returned == 3: printpoint = printpoint + "C" #TEMPLATES
		
				if "A" in printpoint:
					if y == "s":
						'''------------------------------
						---Save-All-----------------------
						------------------------------'''
						formula = ""

						if Custom_Playlist1_ID != "":
							formula = "Custom_Playlist1_ID" + "=5" + Custom_Playlist1_ID
							formula = formula + newline + "Custom_Playlist1_Description" + "=5" + Custom_Playlist1_Description
							formula = formula + newline + "Custom_Playlist1_Fanart" + "=5" + Custom_Playlist1_Fanart
							formula = formula + newline + "Custom_Playlist1_Name" + "=5" + Custom_Playlist1_Name
							formula = formula + newline + "Custom_Playlist1_Thumb" + "=5" + Custom_Playlist1_Thumb
						if Custom_Playlist2_ID != "":
							formula = formula + newline + "Custom_Playlist2_ID" + "=5" + Custom_Playlist2_ID + "=5" + Custom_Playlist2_ID
							formula = formula + newline + "Custom_Playlist2_Description" + "=5" + Custom_Playlist2_Description
							formula = formula + newline + "Custom_Playlist2_Fanart" + "=5" + Custom_Playlist2_Fanart
							formula = formula + newline + "Custom_Playlist2_Name" + "=5" + Custom_Playlist2_Name
							formula = formula + newline + "Custom_Playlist2_Thumb" + "=5" + Custom_Playlist2_Thumb
						if Custom_Playlist3_ID != "":
							formula = formula + newline + "Custom_Playlist3_ID" + "=5" + Custom_Playlist3_ID + "=5" + Custom_Playlist3_ID
							formula = formula + newline + "Custom_Playlist3_Description" + "=5" + Custom_Playlist3_Description
							formula = formula + newline + "Custom_Playlist3_Fanart" + "=5" + Custom_Playlist3_Fanart
							formula = formula + newline + "Custom_Playlist3_Name" + "=5" + Custom_Playlist3_Name
							formula = formula + newline + "Custom_Playlist3_Thumb" + "=5" + Custom_Playlist3_Thumb
						if Custom_Playlist4_ID != "":
							formula = formula + newline + "Custom_Playlist4_ID" + "=5" + Custom_Playlist4_ID + "=5" + Custom_Playlist4_ID
							formula = formula + newline + "Custom_Playlist4_Description" + "=5" + Custom_Playlist4_Description
							formula = formula + newline + "Custom_Playlist4_Fanart" + "=5" + Custom_Playlist4_Fanart
							formula = formula + newline + "Custom_Playlist4_Name" + "=5" + Custom_Playlist4_Name
							formula = formula + newline + "Custom_Playlist4_Thumb" + "=5" + Custom_Playlist4_Thumb
						if Custom_Playlist5_ID != "":
							formula = formula + newline + "Custom_Playlist5_ID" + "=5" + Custom_Playlist5_ID + "=5" + Custom_Playlist5_ID
							formula = formula + newline + "Custom_Playlist5_Description" + "=5" + Custom_Playlist5_Description
							formula = formula + newline + "Custom_Playlist5_Fanart" + "=5" + Custom_Playlist5_Fanart
							formula = formula + newline + "Custom_Playlist5_Name" + "=5" + Custom_Playlist5_Name
							formula = formula + newline + "Custom_Playlist5_Thumb" + "=5" + Custom_Playlist5_Thumb
						if Custom_Playlist6_ID != "":
							formula = formula + newline + "Custom_Playlist6_ID" + "=5" + Custom_Playlist6_ID + "=5" + Custom_Playlist6_ID
							formula = formula + newline + "Custom_Playlist6_Description" + "=5" + Custom_Playlist6_Description
							formula = formula + newline + "Custom_Playlist6_Fanart" + "=5" + Custom_Playlist6_Fanart
							formula = formula + newline + "Custom_Playlist6_Name" + "=5" + Custom_Playlist6_Name
							formula = formula + newline + "Custom_Playlist6_Thumb" + "=5" + Custom_Playlist6_Thumb
						if Custom_Playlist7_ID != "":
							formula = formula + newline + "Custom_Playlist7_ID" + "=5" + Custom_Playlist7_ID + "=5" + Custom_Playlist7_ID
							formula = formula + newline + "Custom_Playlist7_Description" + "=5" + Custom_Playlist7_Description
							formula = formula + newline + "Custom_Playlist7_Fanart" + "=5" + Custom_Playlist7_Fanart
							formula = formula + newline + "Custom_Playlist7_Name" + "=5" + Custom_Playlist7_Name
							formula = formula + newline + "Custom_Playlist7_Thumb" + "=5" + Custom_Playlist7_Thumb
						if Custom_Playlist8_ID != "":
							formula = formula + newline + "Custom_Playlist8_ID" + "=5" + Custom_Playlist8_ID + "=5" + Custom_Playlist8_ID
							formula = formula + newline + "Custom_Playlist8_Description" + "=5" + Custom_Playlist8_Description
							formula = formula + newline + "Custom_Playlist8_Fanart" + "=5" + Custom_Playlist8_Fanart
							formula = formula + newline + "Custom_Playlist8_Name" + "=5" + Custom_Playlist8_Name
							formula = formula + newline + "Custom_Playlist8_Thumb" + "=5" + Custom_Playlist8_Thumb
						if Custom_Playlist9_ID != "":
							formula = formula + newline + "Custom_Playlist9_ID" + "=5" + Custom_Playlist9_ID + "=5" + Custom_Playlist9_ID
							formula = formula + newline + "Custom_Playlist9_Description" + "=5" + Custom_Playlist9_Description
							formula = formula + newline + "Custom_Playlist9_Fanart" + "=5" + Custom_Playlist9_Fanart
							formula = formula + newline + "Custom_Playlist9_Name" + "=5" + Custom_Playlist9_Name
							formula = formula + newline + "Custom_Playlist9_Thumb" + "=5" + Custom_Playlist9_Thumb
						if Custom_Playlist10_ID != "":
							formula = formula + newline + "Custom_Playlist10_ID" + "=5" + Custom_Playlist10_ID + "=5" + Custom_Playlist10_ID
							formula = formula + newline + "Custom_Playlist10_Description" + "=5" + Custom_Playlist10_Description
							formula = formula + newline + "Custom_Playlist10_Fanart" + "=5" + Custom_Playlist10_Fanart
							formula = formula + newline + "Custom_Playlist10_Name" + "=5" + Custom_Playlist10_Name
							formula = formula + newline + "Custom_Playlist10_Thumb" + "=5" + Custom_Playlist10_Thumb
					elif y == "":
						'''------------------------------
						---Save-One-----------------------
						------------------------------'''
						formula = ""

						if Custom_Playlist_ID != "":
							formula = Custom_Playlist_ID + "=5" + getsetting(Custom_Playlist_ID)
							formula = formula + newline + Custom_Playlist_Fanart + "=5" + getsetting(Custom_Playlist_Fanart)
							formula = formula + newline + Custom_Playlist_Name + "=5" + getsetting(Custom_Playlist_Name)
							formula = formula + newline + Custom_Playlist_Thumb + "=5" + getsetting(Custom_Playlist_Thumb)
							formula = formula + newline + Custom_Playlist_Description + "=5" + getsetting(Custom_Playlist_Description)
							'''---------------------------'''
							
					if "1" in printpoint:
						if filename1 == None: filename = ""
						else: filename = filename1
					elif "2" in printpoint:
						if filename2 == None: filename = ""
						else: filename = filename2
					elif "3" in printpoint:
						if filename3 == None: filename = ""
						else: filename = filename3
					
					filename = dialogkeyboard(filename, localize(21821), 0, "", "", "") #Description
					filename_ = "&name="+str(filename)+"&"
					formula = filename_ + newline + formula
					
					try: formula.encode('utf-8')
					except: pass
					
					if "1" in printpoint:
						write_to_file(file1, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'1', str(formula))
					elif "2" in printpoint:
						write_to_file(file2, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'2', str(formula))
					elif "3" in printpoint:
						write_to_file(file3, str(formula), append=False, silent=True, utf8=False)
						#setsetting('Addon_SavedButton'+y+'3', str(formula))
						'''---------------------------'''
					
					notification(addonString_servicefeatherence(58).encode('utf-8'), str(filename), "", 4000) #Saved Succesfully!, 
				
				elif "B" in printpoint or "C" in printpoint:
					'''------------------------------
					---Load/Templates----------------
					------------------------------'''

					if "1" in printpoint:
						if filename1 == None: printpoint = printpoint + "Q"
						else: file = file1
					elif "2" in printpoint:
						if filename2 == None: printpoint = printpoint + "Q"
						else: file = file2
					elif "3" in printpoint:
						if filename3 == None: printpoint = printpoint + "Q"
						else: file = file3
					
					if "Q" in printpoint or file == "":
						'''nothing to load'''
						if "C" in printpoint: notification(localize(19055), "Share Your Music button first.", "", 4000) #No information available
						else:
							if y == "": extra2 = localize(190) + space + localize(592)
							else: extra2 = localize(190) + space + localize(593)
							extra2 = extra2.decode('utf-8').encode('utf-8')
							notification(localize(19055), addonString_servicefeatherence(95).encode('utf-8') % (extra2), "", 4000) #No information available
					else:
						#formula_ = formula_.split(',')
						#formula_ = CleanString(formula_, filter=[])
						import fileinput
						for line in fileinput.input([file]):
							x = "" ; x1 = "" ; x2 = "" ; x3 = ""
							if "=5" in line:
								'''setsetting'''
								x = line.replace("=5","=")
								x1 = find_string(x, "", "=")
								x2 = find_string(x, "=", "")
								x1 = x1.replace("=","")
								x2 = x2.replace('=&', '&') #CLEAN STRINGS
								x2 = x2.replace('\n', '') #CLEAN STRINGS
								if not "_ID" in x:
									'''Clean values for none ID lines'''
									x2 = x2.replace("=","")
									#x2 = x2.replace("\n","")
								
								if y == "":
									count = 0
									while count <= 10 and not xbmc.abortRequested:
										if str(count) in x1:
											x1 = x1.replace(str(count), str(num))
											count = 40
										else: count += 1
								setsetting(str(x1), str(x2))
								
							if admin3 and admin and not admin2: extra = extra + newline + space + "line" + space2 + str(line) + space + "x" + space2 + str(x) + space + "x1" + space2 + str(x1) + space + "x2" + space2 + str(x2) + space + "x3" + space2 + str(x3)
							'''---------------------------'''	
		elif returned == 4:
			'''------------------------------
			---Reset-All---------------------
			------------------------------'''
			returned = dialogyesno(localize(10035) + space + localize(593) + space + "(" + localize(19291) + ")", "You may want to SAVE your settings just in case..") #Reset all (Delete permanently),
			if returned == 'ok':
				file = os.path.join(addondata_path, addonID, 'settings.xml')
				removefiles(file) ; xbmc.sleep(500)
				setsetting('General_AutoView', General_AutoView)
				setsetting('General_TVModeShuffle', General_TVModeShuffle)
				setsetting('General_TVModeDialog', General_TVModeDialog)
				setsetting('Addon_ShowLog', Addon_ShowLog)
				setsetting('Addon_ShowLog2', Addon_ShowLog2)
				setsetting('Addon_Update', Addon_Update)
				setsetting('Addon_UpdateDate', Addon_UpdateDate)
				setsetting('Addon_UpdateLog', Addon_UpdateLog)
				setsetting('Addon_Version', Addon_Version)
				setsetting('Fanart_Enable', Fanart_Enable)
				setsetting('Fanart_EnableCustom', Fanart_EnableCustom)
				setsetting('Fanart_Custom100', Fanart_Custom100)
				setsetting('Fanart_Custom101', Fanart_Custom101)
				setsetting('Fanart_Custom102', Fanart_Custom102)
				setsetting('Fanart_Custom103', Fanart_Custom103)
				setsetting('Fanart_Custom104', Fanart_Custom104)
				setsetting('Fanart_Custom105', Fanart_Custom105)
				setsetting('Fanart_Custom106', Fanart_Custom106)
				setsetting('Fanart_Custom107', Fanart_Custom107)
				setsetting('Fanart_Custom108', Fanart_Custom108)
				setsetting('Fanart_Custom109', Fanart_Custom109)
				setsetting('Fanart_Custom110', Fanart_Custom110)
				setsetting('Fanart_Custom111', Fanart_Custom111)
				setsetting('Fanart_Custom112', Fanart_Custom112)
				setsetting('Fanart_Custom113', Fanart_Custom113)
				setsetting('Fanart_Custom114', Fanart_Custom114)
				setsetting('Fanart_Custom115', Fanart_Custom115)
				setsetting('Fanart_Custom116', Fanart_Custom116)
				setsetting('Fanart_Custom117', Fanart_Custom117)
				setsetting('Fanart_Custom118', Fanart_Custom118)
				setsetting('Fanart_Custom119', Fanart_Custom119)
				setsetting('Fanart_Custom120', Fanart_Custom120)
				setsetting('Fanart_Custom121', Fanart_Custom121)
				setsetting('Fanart_Custom122', Fanart_Custom122)
				setsetting('Fanart_Custom123', Fanart_Custom123)
				setsetting('Fanart_Custom124', Fanart_Custom124)
				setsetting('Fanart_Custom125', Fanart_Custom125)
				setsetting('Fanart_Custom126', Fanart_Custom126)
				setsetting('Fanart_Custom127', Fanart_Custom127)
				setsetting('Fanart_Custom128', Fanart_Custom128)
				setsetting('Fanart_Custom129', Fanart_Custom129)
				setsetting('Fanart_Custom130', Fanart_Custom130)
				
				
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		if not "Q" in printpoint and not "A" in printpoint:
			notification(".","","",1000)
			xbmc.sleep(500)
			notification("..","","",1000)
			update_view(url, num, viewtype)
			'''---------------------------'''
	
	text = 'name_' + space2 + name + "_LV" + printpoint + space + newline + \
	"path" + space2 + str(path) + newline + \
	"file1" + space2 + str(file1) + newline + \
	"file2" + space2 + str(file2) + newline + \
	"file3" + space2 + str(file3) + newline + \
	"formula" + space2 + str(formula) + space + "formula_" + space2 + str(formula_) + newline + \
	"extra" + space2 + str(extra)
	printlog(title="AdvancedCustom", printpoint=printpoint, text=text, level=2, option="")
		
def AddCustom(mode, name, url, iconimage, desc, num, viewtype):
	'''------------------------------
	---New-Button--------------------
	------------------------------'''
	printpoint = ""
	Custom_Playlist_ID = getCustom_Playlist(admin) ; New_Type = "" ; New_ID = "" ; New_Name = ""
	Custom_Playlist_Name = Custom_Playlist_ID.replace("_ID","_Name")
	if Custom_Playlist_ID == "": notification("Playlist limit reached!", "You may delete some playlists and try again!", "", 4000)
	else:
		New_ID = dialogkeyboard("", "Enter YouTube URL", 0, "5", "" , "")
		if New_ID != "skip":
			New_Name = dialogkeyboard('My Button', "Button Name", 0, "",Custom_Playlist_Name, "0")
			if New_Name != "skip":
				setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, New_Name, num, viewtype)
				
	text = "name" + space2 + str(name)
	printlog(title="AddCustom", printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''
	
def CheckMoveCustom(name, num):
	extra = "" ; printpoint = "" ; down = "" ; up = ""
	
	'''---------------------------'''
	if num == "1":
		'''---------------------------'''
		if Custom_PlaylistL[1] != "": down = "2"
		elif Custom_PlaylistL[2] != "": down = "3"
		elif Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "2":
		if Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[2] != "": down = "3"
		elif Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "3":
		if Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[3] != "": down = "4"
		elif Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "4":
		if Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[4] != "": down = "5"
		elif Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "5":
		if Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[5] != "": down = "6"
		elif Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "6":
		if Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[6] != "": down = "7"
		elif Custom_PlaylistL[7] != "": down = "8"
		elif Custom_PlaylistL[8] != "": down = "9"
		elif Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "7":
		if Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[8] != "": up = "9"
		elif Custom_PlaylistL[9] != "": up = "10"
		'''---------------------------'''
	elif num == "8":
		if Custom_PlaylistL[7] != "": up = "8"
		elif Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
		if Custom_PlaylistL[9] != "": down = "10"
		'''---------------------------'''
	elif num == "10":
		if Custom_PlaylistL[8] != "": up = "9"
		elif Custom_PlaylistL[7] != "": up = "8"
		elif Custom_PlaylistL[6] != "": up = "7"
		elif Custom_PlaylistL[5] != "": up = "6"
		elif Custom_PlaylistL[4] != "": up = "5"
		elif Custom_PlaylistL[3] != "": up = "4"
		elif Custom_PlaylistL[2] != "": up = "3"
		elif Custom_PlaylistL[1] != "": up = "2"
		elif Custom_PlaylistL[0] != "": up = "1"
		'''---------------------------'''
	
	text = "name" + space2 + str(name) + space + "num" + space2 + str(num) + space + "down" + space2 + str(down) + space + "up" + space2 + str(up)
	printlog(title="CheckMoveCustom", printpoint=printpoint, text=text, level=2, option="")
		
	return up, down

def cleanfanartCustom(fanart):
	printpoint = ""
	fanart2 = fanart.replace("/","")
	fanart2 = fanart2.replace("\\","")
	addonFanart2 = addonFanart.replace("/","")
	addonFanart2 = addonFanart2.replace("\\","")
	if fanart2 == addonFanart2:
		printpoint = printpoint + "7"
		fanart = "" # or not os.path.exists(fanart)
	
	text = "fanart" + space2 + str(fanart) + newline + \
	"fanart2" + space2 + str(fanart2) + newline + \
	"addonFanart" + space2 + str(addonFanart) + newline + \
	"addonFanart2" + space2 + str(addonFanart2)
	printlog(title="cleanfanartCustom", printpoint=printpoint, text=text, level=2, option="")
	return fanart
	
def MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart):
	'''23'''
	printpoint = ""
	'''---------------------------'''
	if not "__" in num: printpoint = printpoint + "9"
	else:
		printpoint = printpoint + "1"
		num = num.split("__")
		num1 = num[0]
		num2 = num[1]
	try:
		test = int(num1) + 1
		test = int(num2) + 1
	except Exception, TypeError: printpoint = printpoint + "9"
	
	fanart = cleanfanartCustom(fanart)
	
	if not "9" in printpoint:
		printpoint = printpoint + "3"
		Custom_Playlist_ID = "Custom_Playlist" + num1 + "_ID"
		if Custom_Playlist_ID == "": notification("Error ID", "Use featherence Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name = "Custom_Playlist" + num1 + "_Name"
		Custom_Playlist_Thumb = "Custom_Playlist" + num1 + "_Thumb"
		Custom_Playlist_Description = "Custom_Playlist" + num1 + "_Description"
		Custom_Playlist_Fanart = "Custom_Playlist" + num1 + "_Fanart"
		'''---------------------------'''
		Custom_Playlist_ID2 = "Custom_Playlist" + str(num2) + "_ID"
		if Custom_Playlist_ID2 == "": notification("Error ID", "Use featherence Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
		Custom_Playlist_Name2 = "Custom_Playlist" + str(num2) + "_Name"
		Custom_Playlist_Thumb2 = "Custom_Playlist" + str(num2) + "_Thumb"
		Custom_Playlist_Description2 = "Custom_Playlist" + str(num2) + "_Description"
		Custom_Playlist_Fanart2 = "Custom_Playlist" + str(num2) + "_Fanart"
		'''---------------------------'''
	
	if not "9" in printpoint:
		printpoint = printpoint + "7"
		'''---------------------------'''
		setsetting(Custom_Playlist_ID, getsetting(Custom_Playlist_ID2))
		setsetting(Custom_Playlist_Name, getsetting(Custom_Playlist_Name2))
		setsetting(Custom_Playlist_Thumb, getsetting(Custom_Playlist_Thumb2))
		setsetting(Custom_Playlist_Description, getsetting(Custom_Playlist_Description2))
		setsetting(Custom_Playlist_Fanart, getsetting(Custom_Playlist_Fanart2))
		'''---------------------------'''
		setsetting(Custom_Playlist_ID2, url)
		setsetting(Custom_Playlist_Name2, name)
		setsetting(Custom_Playlist_Thumb2, iconimage)
		setsetting(Custom_Playlist_Description2, desc)
		setsetting(Custom_Playlist_Fanart2, fanart)
		'''---------------------------'''
		update_view(url, num, viewtype)
	
	text = "url" + space2 + str(url) + space + "num" + space2 + str(num)
	printlog(title="MoveCustom", printpoint=printpoint, text=text, level=2, option="")
		
def ManageCustom(mode, name, url, thumb, desc, num, viewtype, fanart):
	extra = "" ; printpoint = "" ; New_ID = ""
	
	Custom_Playlist_ID = "Custom_Playlist" + num + "_ID"
	if Custom_Playlist_ID == "": notification("Error ID", "Use featherence Debug addon for support", "", 2000) ; printpoint = printpoint + "9"
	Custom_Playlist_Name = "Custom_Playlist" + num + "_Name"
	Custom_Playlist_Thumb = "Custom_Playlist" + num + "_Thumb"
	Custom_Playlist_Description = "Custom_Playlist" + num + "_Description"
	Custom_Playlist_Fanart = "Custom_Playlist" + num + "_Fanart"
	
	if printpoint != "9":
		list = ['-> (Exit)']
		list.append(addonString_servicefeatherence(38).encode('utf-8')) #Edit URL
		list.append(addonString_servicefeatherence(41).encode('utf-8')) #Rename Button
		if thumb == "": list.append(addonString_servicefeatherence(36).encode('utf-8')) #Add Thumb
		else: list.append(addonString_servicefeatherence(37).encode('utf-8')) #Remove Thumb
		if desc == "": list.append(addonString_servicefeatherence(32).encode('utf-8')) #Add Description
		else: list.append(addonString_servicefeatherence(33).encode('utf-8')) #Edit Description
		fanart = cleanfanartCustom(getsetting(Custom_Playlist_Fanart))
		if fanart == "": list.append(addonString_servicefeatherence(34).encode('utf-8')) #Add Fanart
		else: list.append(addonString_servicefeatherence(35).encode('utf-8')) #Remove Fanart
		list.append(localize(13336)) #'Remove Button'

		returned, value = dialogselect(addonString_servicefeatherence(31).encode('utf-8'),list,0)
			
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
	
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		if returned == 1: printpoint = printpoint + "A" #Edit URL
		elif returned == 2: printpoint = printpoint + "B" #Rename
		elif returned == 3: printpoint = printpoint + "C" #Add/Remove Thumb
		elif returned == 4: printpoint = printpoint + "D" #Add/Edit Description
		elif returned == 5: printpoint = printpoint + "E" #Add/Remove Fanart
		elif returned == 6: printpoint = printpoint + "F" #Remove Button
		'''---------------------------'''
	if "A" in printpoint:
		'''------------------------------
		---Edit-URL----------------------
		------------------------------'''
		list = ['-> (Exit)']
		list.append(addonString_servicefeatherence(42).encode('utf-8')) #View URL
		list.append(addonString_servicefeatherence(40).encode('utf-8')) #Add URL
		list.append(addonString_servicefeatherence(39).encode('utf-8')) #Remove URL
		
		returned2, value = dialogselect(addonString_servicefeatherence(31).encode('utf-8'),list,0)
			
		if returned2 == -1: printpoint = printpoint + "9"
		elif returned2 == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
		if returned2 == 1: printpoint = printpoint + "1" #View URL
		elif returned2 == 2: printpoint = printpoint + "2" #Add URL
		elif returned2 == 3: printpoint = printpoint + "3" #Remove URL
		
		if "1" in printpoint:
			'''------------------------------
			---View-URL----------------------
			------------------------------'''
			message2 = "" ; i = 0
			url2 = url.split(",")
			for x in url2:
				i += 1
				x2 = ""
				if "&youtube_ch=" in x:
					x = x.replace("&youtube_ch=","")
					x2 = space + "[" + "YouTube Channel" + "]"
					'''---------------------------'''
				elif "&youtube_pl=" in x:
					x = x.replace("&youtube_pl=","")
					x2 = space + "[" + "YouTube Playlist" + "]"
					'''---------------------------'''
				elif "&youtube_id=" in x:
					x = x.replace("&youtube_id=","")
					x2 = space + "[" + "YouTube Video" + "]"
					'''---------------------------'''
				if x2 != "": message2 = message2 + '[CR]' + str(i) + space2 + str(x) + str(x2)
				'''---------------------------'''
			header = addonString_servicefeatherence(42).encode('utf-8') + space2 + str(name)
			if message2 != "": message = message2 + '[CR][CR]' + addonString_servicefeatherence(89).encode('utf-8')
			else: message = addonString_servicefeatherence(90).encode('utf-8') #URL Error occured.
			diaogtextviewer(header,message)
			'''---------------------------'''
			
		elif "2" in printpoint:
			'''------------------------------
			---Add-URL-----------------------
			------------------------------'''
			New_ID = dialogkeyboard("", addonString_servicefeatherence(40).encode('utf-8'), 0, "5", "" , "")
			setCustom_Playlist_ID(Custom_Playlist_ID, New_ID, mode, url, name, num, viewtype)
			
				
		elif "3" in printpoint:
			'''------------------------------
			---Remove-URL--------------------
			------------------------------'''
			list = ['-> (Exit)']
			url2 = url.split(',')
			i = 0
			for x in url2:
				i += 1
				list.append(x)

			returned2, value = dialogselect(addonString_servicefeatherence(31).encode('utf-8'),list,0)
				
			if returned2 == -1: printpoint = printpoint + "9"
			elif returned2 == 0: printpoint = printpoint + "8"
			else: printpoint = printpoint + "7"
			
			if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
				
				if i == 1:
					'''Warning 1 URL found!'''
					check = dialogyesno(localize(13336), addonString_servicefeatherence(92).encode('utf-8') + '[CR]' + addonString_servicefeatherence(91).encode('utf-8'))
					if check == "ok":
						'''Remove Button'''
						printpoint = printpoint + "F"
					else:
						'''Skip'''
				else:
					if value + "," in url:
						'''multi links'''
						value2 = url.replace(value + ",","",1)
					elif value in url:
						'''single link'''
						value2 = url.replace(value,"",1)
					else: value2 = ""
					if value2 == "": notification_common("17")
					else:
						setsetting(Custom_Playlist_ID, value2)
						notification(addonString_servicefeatherence(44).encode('utf-8') + space + addonString_servicefeatherence(43).encode('utf-8'),str(name), "", 4000) #URL Removed Succesfully!
						'''---------------------------'''
				
	elif "B" in printpoint:
		'''------------------------------
		---Rename-Button-----------------
		------------------------------'''
		New_Name = dialogkeyboard(name, addonString_servicefeatherence(41).encode('utf-8'), 0, "", Custom_Playlist_Name, "0")
		if New_Name != "skip" and New_Name != name:
			notification(addonString_servicefeatherence(45).encode('utf-8') + space + addonString_servicefeatherence(30).encode('utf-8'), str(name), "", 4000) #Button Name Update Succesfully!
			'''---------------------------'''
		
	elif "C" in printpoint:
		if thumb == "":
			'''------------------------------
			---Add-Thumb---------------------
			------------------------------'''
			New_Thumb = ""
			returned = dialogyesno(str(name), addonString_servicefeatherence(31).encode('utf-8'), nolabel=localize(20017), yeslabel=localize(20015))
			if returned == 'ok':
				'''remote'''
				x = localize(20015) #Remote thumb
				value = dialogkeyboard("", x + space + "URL", 0, "1", "", "")
				if value != "skip":
					returned = urlcheck(value, ping=False)
					if returned != "ok":
						notification("URL Error", "Try again..", "", 2000)
						header = "URL Error"
						message = "Examine your URL for errors:" + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Thumb = value
			else:
				'''local'''
				x = localize(20017) #Local thumb
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Thumb = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Thumb != "":
				setsetting(Custom_Playlist_Thumb, New_Thumb)
				notification(str(x) + space + addonString_servicefeatherence(30).encode('utf-8'), str(name), "", 4000) #Thumb* Update Succesfully!
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Thumb------------------
			------------------------------'''
			if os.path.exists(thumb): x = localize(20017) #Local thumb
			else: x = localize(20015)
			setsetting(Custom_Playlist_Thumb, "")
			notification(str(x) + space + addonString_servicefeatherence(43).encode('utf-8'), str(name), "", 2000) #Thumb* Removed Succesfully!
			'''---------------------------'''
			
	elif "D" in printpoint:
		'''------------------------------
		---Add-Description---------------
		------------------------------'''
		returned, value = getRandom("0", min=0, max=100, percent=50)
		if int(value) <= 10: notification("Tip New Line:", "[CR]", "", 4000)
		elif int(value) <= 20: notification("Tip Bold:", "[B]text[/B]", "", 4000)
		elif int(value) <= 30: notification("Tip Color:", "[COLOR=X]text[/COLOR]", "", 4000)
		elif int(value) <= 40: notification("Tip Italic:", "[I]text[/I]", "", 4000)
		
		if Custom_Playlist_Description == "": extra1 = addonString_servicefeatherence(32).encode('utf-8') #Add Description
		else: extra1 = addonString_servicefeatherence(33).encode('utf-8') #Edit Description
		
		returned = dialogkeyboard(desc, extra1, 0, "", Custom_Playlist_Description, "0")
		if returned != "skip":
			if returned == "": extra2 = addonString_servicefeatherence(43).encode('utf-8') #Removed Succesfully!
			else: extra2 = addonString_servicefeatherence(30).encode('utf-8') #Update Succesfully!
			if returned != desc: notification(localize(21821) + space + extra2, str(name), "", 4000) #Description Update/Removed Succesfully!
			'''---------------------------'''
	
	elif "E" in printpoint:
		
		if fanart == "":
			'''------------------------------
			---Add-Fanart----------------
			------------------------------'''
			New_Fanart = ""
			returned = dialogyesno(str(name), addonString_servicefeatherence(31).encode('utf-8'), nolabel=localize(20438), yeslabel=localize(20441))
			if returned == 'ok':
				'''remote'''
				x = localize(20441) #Remote fanart
				value = dialogkeyboard("", localize(20441), 0, "1", "", "")
				if value != "skip":
					returned2 = urlcheck(value, ping=False)
					if returned2 != "ok":
						notification("URL Error", "Try again..", "", 2000)
						header = "URL Error"
						message = "Examine your URL for errors:" + newline + '[B]' + str(value) + '[/B]'
						diaogtextviewer(header,message)
					else:
						New_Fanart = value
			else:
				'''local'''
				x = localize(20438) #Local fanart
				xbmc.executebuiltin('Skin.SetString('+addonID+'_Temp,)')
				xbmc.executebuiltin('Skin.SetImage('+addonID+'_Temp,)') ; xbmc.sleep(4000)
				dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
				while dialogfilebrowserW and not xbmc.abortRequested:
					xbmc.sleep(500)
					dialogfilebrowserW = xbmc.getCondVisibility('Window.IsVisible(FileBrowser.xml)')
					xbmc.sleep(500)
				xbmc.sleep(500)
				New_Fanart = xbmc.getInfoLabel('Skin.String('+addonID+'_Temp)')
			
			if New_Fanart != "":
				setsetting(Custom_Playlist_Fanart, New_Fanart)
				 
				notification(str(x) + space + addonString_servicefeatherence(30).encode('utf-8'), str(New_Fanart), "", 2000) #Fanart* Update Succesfully!
				xbmc.sleep(2000)
				if Fanart_Enable != "true": notification(addonString_servicefeatherence(28).encode('utf-8') + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Allow Backgrounds Disabled, ->Add-on settings
				elif Fanart_EnableCustom != "true": notification(localize(21389) + space + localize(24023) + "!", "->" + localize(1045), "", 4000) # Enable custom background Disabled, ->Add-on settings
				'''---------------------------'''
		else:
			'''------------------------------
			---Remove-Fanart------------
			------------------------------'''
			setsetting(Custom_Playlist_Fanart, "")
			notification(localize(33068) + space + localize(19179) + "!", str(name), "", 4000) #Background Deleted!
			'''---------------------------'''
			
	if "F" in printpoint:
		if Custom_Playlist_Description != "":
			'''------------------------------
			---Remove-Button-----------------
			------------------------------'''
			returned = dialogyesno(localize(13336) + '[CR]' + str(name),localize(19194)) #Remove Button, Continue?
			if returned == "ok":
				setsetting(Custom_Playlist_ID, "")
				setsetting(Custom_Playlist_Name, "")
				setsetting(Custom_Playlist_Thumb, "")
				setsetting(Custom_Playlist_Description, "")
				setsetting(Custom_Playlist_Fanart, "")
				'''---------------------------'''
				if desc != "": extra1 = localize(21821) + space2 + str(desc)
				else: extra1 = ""
				dialogok(localize(50) + space + addonString_servicefeatherence(43).encode('utf-8') + '[CR]' + str(name), "ID" + space2 + str(url), "", extra1)
				'''---------------------------'''
				
	if "7" in printpoint and not "8" in printpoint and not "9" in printpoint:
		update_view(url, num, viewtype)
		#xbmcplugin.endOfDirectory(int(sys.argv[1]))
		
	text = "name" + space2 + str(name) + newline + \
	"Custom_Playlist_ID" + space2 + str(Custom_Playlist_ID) + newline + \
	"Custom_Playlist_Name" + space2 + str(Custom_Playlist_Name) + newline + \
	"Custom_Playlist_Thumb" + space2 + str(Custom_Playlist_Thumb) + newline + \
	"thumb" + space2 + str(thumb) + newline + \
	"Custom_Playlist_Description" + space2 + str(Custom_Playlist_Description) + newline + \
	"Custom_Playlist_Fanart" + space2 + str(Custom_Playlist_Fanart) + newline + \
	"fanart" + space2 + str(fanart) + newline + \
	"New_ID" + space2 + str(New_ID) + newline + \
	"url" + space2 + str(url) + newline
	'''---------------------------'''
	printlog(title="ManageCustom", printpoint=printpoint, text=text, level=2, option="")
		
def youtube_pl_to_youtube_id(x, playlist=[]):
	'''Error may occured at anytime'''
	'''Make sure to use exception upon running this module'''
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)') ; playlist2 = []
	printpoint = "" ; TypeError = "" ; extra = "" ; page = 1 ; pagesize = 40
	valid_ = "" ; invalid_ = 0 ; invalid__ = "" ; duplicates_ = 0 ; duplicates__ = "" ; except_ = 0 ; except__ = ""
	
	returned = get_types(playlist)
	if not 'list' in returned: playlist = []
	
	if "&youtube_pl=" in x:
		printpoint = printpoint + "1"
		x = x.replace("&youtube_pl=","")
		url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+x+'&key='+featherenceapi+'&part=snippet&maxResults=40&pageToken='
	elif "&youtube_se=" in x:
		printpoint = printpoint + "2"
		x = x.replace("&youtube_se=","")
		x = clean_commonsearch(x)
		url = 'https://www.googleapis.com/youtube/v3/search?q='+x+'&key='+featherenceapi+'&safeSearch=moderate&type=video&part=snippet&maxResults=40&pageToken='
	elif "&custom_se=" in x:
		text = 'xxx' + space2 + str(x)
		printlog(title='youtube_pl_to_youtube_id_test1', printpoint=printpoint, text=text, level=0, option="")
		printpoint = printpoint + "3"
		x = x.replace("&custom_se=","")
		x = clean_commonsearch(x)
		#print "qwewqeqwe" + x
		pagesize = 1
		url = 'https://www.googleapis.com/youtube/v3/search?q='+x+'&key='+featherenceapi+'&safeSearch=moderate&type=video&part=snippet&maxResults=1&pageToken='
	elif "&youtube_ch=" in x:
		printpoint = printpoint + "4"
		finalurl, id, name, iconimage, desc = getAPIdata(x, "", "", "")
		x = x.replace("&youtube_ch=","")
		url = 'https://www.googleapis.com/youtube/v3/search?channelId='+id+'&key='+featherenceapi+'&part=snippet&maxResults=40'
	else: printpoint = printpoint + "8"
	
	link = OPEN_URL(url)
	prms=json.loads(link)
	text = "url" + space2 + str(url) + newline + \
	"link" + space2 + str(link) + newline + \
	"prms" + space2 + str(prms) + newline #+ \ + "totalResults" + space2 + str(totalResults)
	'''---------------------------'''
	printlog(title='youtube_pl_to_youtube_id_test2', printpoint=printpoint, text=text, level=0, option="")

	totalResults=int(prms['pageInfo'][u'totalResults']) #if bigger than pagesize needs to add more result
	totalpagesN = (totalResults / pagesize) + 1
	'''---------------------------'''

	i = 0 ; count = 0
	while i < pagesize and i < totalResults and not "8" in printpoint and count < (pagesize + 20) and not xbmc.abortRequested: #h<totalResults
		try:
			#if 1 + 1 == 2:
			#print "i" + space2 + str(i) + space + "duplicates__" + space2 + str(duplicates__) + "totalResults" + space2 + str(totalResults)
			id = "" ; finalurl = ""
			if "1" in printpoint: id=str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
			elif "2" in printpoint or "3" in printpoint or '4' in printpoint: id=str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)

			if id != "":
				finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
				title=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
				thumb=str(prms['items'][i][u'snippet'][u'thumbnails'][u'default'][u'url'])
				desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
				#id = "" ; finalurl = "" ; title = "" ; thumb = "" ; desc = ""
			
			if not finalurl in playlist and not "Deleted video" in title and not "Private video" in title and finalurl != "":
				#ok, liz = addLink(title,finalurl, thumb, desc)
				#name, url, mode, iconimage='DefaultFolder.png', desc="", num="", viewtype=""
				#playlist.append((finalurl ,liz))
				if addonID == 'plugin.video.featherence.music' and (commonsearch104 in x or commonsearch109 in x or commonsearch114 in x):
					for filterx in sefilter:
						if filterx in title:
							error

				playlist.append(finalurl)
				playlist2.append(finalurl)
				'''---------------------------'''
			else:
				if "Deleted video" in title or "Private video" in title:
					invalid_ += 1
					invalid__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)
				elif finalurl in playlist:
					duplicates_ += 1
					duplicates__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)

		except Exception, TypeError:
			except_ += 1
			except__ = "i" + space2 + str(i) + space + "id" + space2 + str(id)
			if not 'list index out of range' in TypeError: extra = extra + newline + "i" + space2 + str(i) + space + "TypeError" + space2 + str(TypeError)
			else: printpoint = printpoint + "8"
			'''---------------------------'''
		
		i += 1
		count += 1
		
	numOfItems2 = len(playlist2)
	#numOfItems2 = totalResults - invalid_ - duplicates_ - except_
	#if numOfItems2 > pagesize: numOfItems2 = 40
	totalpages = (numOfItems2 / pagesize) + 1
	nextpage = page + 1
	
	#if totalpages > page: addDir('[COLOR=Yellow]' + localize(33078) + '[/COLOR]',x,13,"special://skin/media/DefaultVideo2.png",str79528.encode('utf-8'),str(nextpage),50) #Next Page
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	if duplicates__ != "": extra = "duplicates__" + space2 + str(duplicates__) + "(" + str(duplicates_) + ")" + newline + extra
	if invalid__ != "": extra = "invalid__" + space2 + str(invalid__) + "(" + str(invalid_) + ")" + newline + extra
	if except__ != "": extra = "except__" + space2 + str(except__) + "(" + str(except_) + ")" + newline + extra
	if playlist != []: extra = "playlist" + space2 + str(playlist) + newline + extra
		
	text = "i" + space2 + str(i) + space + "totalResults" + space2 + str(totalResults) + space + "numOfItems2" + space2 + str(numOfItems2) + newline + \
	"x" + space2 + x + space + "page" + space2 + str(page) + " / " + str(totalpages) + space + "pagesize" + space2 + str(pagesize) + newline + \
	"extra" + space2 + str(extra)
	printlog(title='youtube_pl_to_youtube_id', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return playlist2, numOfItems2

	
def RanFromPlayList(playlistid):
	random.seed()
	url='https://gdata.youtube.com/feeds/api/playlists/'+playlistid+'?alt=json&max-results=50'
	link = OPEN_URL(url)
	prms=json.loads(link)
	numOfItems=int(prms['feed'][u'openSearch$totalResults'][u'$t']) #if bigger than 50 needs  to add more result
	if numOfItems >1 :
		link = OPEN_URL(url)
		prms=json.loads(link)
		if numOfItems>49:
			numOfItems=49
		i=random.randint(1, numOfItems-1)
		#print str (len(prms['feed'][u'entry']))  +"and i="+ str(i)
		try:
			urlPlaylist= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$player'][0][u'url'])
			match=re.compile('www.youtube.com/watch\?v\=(.*?)\&f').findall(urlPlaylist)
			finalurl="plugin://plugin.video.youtube/play/?video_id="+match[0]+"&hd=1" #finalurl="plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid="+match[0]+"&hd=1"
			title= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$title'][u'$t'].encode('utf-8')).decode('utf-8')
			thumb =str(prms['feed'][u'entry'][i][ u'media$group'][u'media$thumbnail'][2][u'url'])
			desc= str(prms['feed'][u'entry'][i][ u'media$group'][u'media$description'][u'$t'].encode('utf-8')).decode('utf-8')
		except :
			 return "","","",""  # private video from youtube
		'''liz = xbmcgui.ListItem(title, iconImage="DefaultVideo.png", thumbnailImage=thumb)
		liz.setInfo( type="Video", infoLabels={ "Title": title} )
		liz.setProperty("IsPlayable","true")
		pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
		pl.clear()
		pl.add(finalurl, liz)'''
		#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
		return finalurl,title,thumb,desc
	else:
		return "","","",""

def myView(type):
	name = 'myView' ; value = ""
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	if type == "A":
		if xbmc.getSkinDir() != "skin.featherence":
			try: value = int(General_AutoView_A)
			except: value = ""
		else: value = "50"
		
	elif type == "B":
		if xbmc.getSkinDir() != "skin.featherence":
			try: value = int(General_AutoView_B)
			except: value = ""
	elif type == "C":
		if xbmc.getSkinDir() != "skin.featherence":
			try: value = int(General_AutoView_C)
			except: value = ""

	text = "type" + space2 + str(type) + space + "value" + space2 + str(value)
	printlog(title=name, printpoint="", text=text, level=0, option="")
	return value

def setView(content, viewType, containerfolderpath2):
	'''set content type so library shows more views and info'''
	name = 'setView' ; printpoint = ""
	
	if content:
		printpoint = printpoint + "1"
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if viewType == None:
		printpoint = printpoint + "2"
		if containerfolderpath2 == 'plugin://' + addonID + "/": viewType = 50
		elif viewType == None: pass
		elif content == 'episodes': viewType = 50
		elif content == 'seasons': viewType = 50
		elif content == 'tvshows': viewType = 58
		elif content == 'movies': viewType = 58
		

	if General_AutoView == "true" and viewType != None:
		if xbmc.getSkinDir() == 'skin.featherence':
			xbmc.executebuiltin("Container.SetViewMode(%s)" % str(viewType) )
			printpoint = printpoint + "7"
			'''---------------------------'''
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "content" + space2 + str(content) + space + "viewType" + space2 + str(viewType) + newline + \
	"containerfolderpath2" + space2 + containerfolderpath2
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def ShowFromUser(user):
	'''reads  user names from my subscriptions'''
	murl='https://gdata.youtube.com/feeds/api/users/'+user+'/shows?alt=json&start-index=1&max-results=50&v=2'
	resultJSON = json.loads(OPEN_URL(murl))
	shows=resultJSON['feed']['entry']
	#print shows[1]
	hasNext= True
	while hasNext:
		shows=resultJSON['feed']['entry']
		for  i in range (0, len(shows)) :
			showApiUrl=shows[i]['link'][1]['href']
			showApiUrl=showApiUrl[:-4]+'/content?v=2&alt=json'
			showName=shows[i]['title']['$t'].encode('utf-8')
			image= shows[i]['media$group']['media$thumbnail'][-1]['url']
			addDir(showName,showApiUrl,14,image,'','1',"")
		hasNext= resultJSON['feed']['link'][-1]['rel'].lower()=='next'
		if hasNext:
			resultJSON = json.loads(OPEN_URL(resultJSON['feed']['link'][-1]['href']))
			
def TVMode_check(admin, url, playlists):
	printpoint = ""
	returned = ""
	if General_TVModeDialog == "true":
		printpoint = printpoint + "1"
		printpoint = printpoint + "3"
		countl = 0
		for space in playlists:
			countl += 1
		countlS = str(countl)
		if playlists==[] or countl > 1:  #no playlists on  youtube channel
			'''------------------------------
			---PLAYLIST->-1------------------
			------------------------------'''
			printpoint = printpoint + "5"
			returned = dialogyesno(addonString_servicefeatherence(7).encode('utf-8'), addonString_servicefeatherence(8).encode('utf-8'))
			if returned == "ok": returned = TvMode(url)
			'''---------------------------'''
		else: printpoint = printpoint + "8"
				
	printlog(title='TVMode_check', printpoint=printpoint, text="", level=0, option="")
	'''---------------------------'''
	return returned

def TvMode2(mode, name, url, iconimage, desc, num, viewtype):
	returned = ""
	if url == "None":
		'''Empty button'''
		notification("no valid URL founds!", "...", "", 2000)
	else:
		if General_TVModeDialog == "true" or mode == 2:
			if General_TVModeShuffle == "true": extra = addonString_servicefeatherence(8).encode('utf-8')
			else: extra = addonString_servicefeatherence(61).encode('utf-8') + '[CR]' + addonString_servicefeatherence(62).encode('utf-8')
			if mode == 2: returned = 'ok'
			else: returned = dialogyesno(addonString_servicefeatherence(7).encode('utf-8'), extra)
			
		if returned == 'ok': mode = 5
		else: mode = 6
		
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
		
		return mode

def getAddonInfo(addon):
	name = 'getAddonInfo' ; printpoint = ""
	thumb = "" ; fanart = "" ; summary = "" ; description = ""
	
	thumb = os.path.join(addons_path, addon, 'icon.png')
	fanart = os.path.join(addons_path, addon, 'fanart.jpg')
	addoninfo = os.path.join(addons_path, addon, 'addon.xml')
	addoninfo_ = read_from_file(addoninfo, silent=True, lines=False, retry=False, printpoint="", addlines="")
	systemlanguage = xbmc.getInfoLabel('System.Language')
	systemlanguage_ = systemlanguage[:2].lower()
	
	if addoninfo_ != "":
		i = 0
		for i in range(0,3):
			if i == 0: summary = regex_from_to(addoninfo_, '<summary lang="'+systemlanguage_+'">', '</summary>', excluding=True)
			elif i == 1: summary = regex_from_to(addoninfo_, '<summary>', '</summary>', excluding=True)
			elif i == 2: summary = regex_from_to(addoninfo_, '<summary lang="en">', '</summary>', excluding=True)
			if summary != "": break
		
		i = 0
		for i in range(0,3):
			if i == 0: description = regex_from_to(addoninfo_, '<description lang="'+systemlanguage_+'">', '</description>', excluding=True)
			elif i == 1: description = regex_from_to(addoninfo_, '<description>', '</description>', excluding=True)
			elif i == 2: description = regex_from_to(addoninfo_, '<description lang="en">', '</description>', excluding=True)
			if description != "": break
	
	text = 'systemlanguage' + space2 + str(systemlanguage) + space + 'systemlanguage[:2]' + space2 + str(systemlanguage_) + newline + \
	'thumb' + space2 + str(thumb) + newline + \
	'fanart' + space2 + str(fanart) + newline + \
	'summary' + space2 + str(summary) + newline + \
	'description' + space2 + str(description)
	
	try: summary = summary.encode('utf-8')
	except: pass
	try: description = description.encode('utf-8')
	except: pass
	plot = '[COLOR=Yellow]'+summary+'[/COLOR]'+'[CR][CR]'+description
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	return thumb, fanart, summary, description, plot
	
def update_view(url, num, viewtype):
	if 'plugin.' in num:
		if not xbmc.getCondVisibility('System.HasAddon('+ num +')') or not os.path.exists(os.path.join(addons_path, num)):
			notification_common("24")
			installaddon(admin, num, update=True)
			xbmc.sleep(2000)
	ok = True
	xbmc.executebuiltin('XBMC.Container.Update(%s)' % url )
	text = "url" + space2 + str(url) + space + 'viewtype' + space2 + str(viewtype)
	printlog(title='update_view', printpoint="", text=text, level=0, option="")
	return ok

def play_view(url, num, viewtype):
	if 'plugin.' in num:
		if not xbmc.getCondVisibility('System.HasAddon('+ num +')') or not os.path.exists(os.path.join(addons_path, num)):
			notification_common("24")
			installaddon(admin, num, update=True)
			xbmc.sleep(2000)
	ok = True
	xbmc.executebuiltin('PlayMedia(%s)' % url )
	text = "url" + space2 + str(url) + space + 'viewtype' + space2 + str(viewtype)
	printlog(title='update_view', printpoint="", text=text, level=0, option="")
	return ok	

def unescape(text):
	try:            
		rep = {"&nbsp;": " ",
			   "\n": "",
			   "\t": "",
			   "\r":"",
			   "&#39;":"",
			   "&quot;":"\""
			   }
		for s, r in rep.items():
			text = text.replace(s, r)
			
		# remove html comments
		text = re.sub(r"<!--.+?-->", "", text)    
			
	except TypeError:
		pass

	return text

def urlcheck(url, ping=False, timeout=7):
	import urllib2
	admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	name = "urlcheck" ; printpoint = "" ; returned = "" ; extra = "" ; TypeError = ""
	
	
	try:
		#urllib2.urlopen(url)
		request = urllib2.Request(url)
		response = urllib2.urlopen(request, timeout=timeout)
		#content = response.read()
		#f = urllib2.urlopen(url)
		#f.fp._sock.recv=None # hacky avoidance
		response.close()
		del response
		printpoint = printpoint + "7"
		
	except urllib2.HTTPError, e: 
		extra = extra + newline + str(e.code) + space + str(e)
		printpoint = printpoint + "8"
	except urllib2.URLError, e:
		extra = extra + newline + str(e.args) + space + str(e)
		printpoint = printpoint + "9"
	except Exception, TypeError:
		printpoint = printpoint + "9"
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		if 'The read operation timed out' in TypeError: returned = 'timeout'
		
	if not "7" in printpoint:
		if ping == True:
			if systemplatformwindows: output = terminal('ping '+url+' -n 1',"Connected2")
			else: output = terminal('ping -W 1 -w 1 -4 -q '+url+'',"Connected")
			if (not systemplatformwindows and ("1 packets received" in output or not "100% packet loss" in output)) or (systemplatformwindows and ("Received = 1" in output or not "100% loss" in output)): printpoint = printpoint + "7"
	
	if "UKY3scPIMd8" in url: printpoint = printpoint + "6"
	elif "7" in printpoint: returned = "ok" # or 'Forbidden' in extra
	else: returned = 'error'
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "url" + space2 + url + space + "ping" + space2 + str(ping) + space + 'returned' + space2 + str(returned) + space + extra
	printlog(title='urlcheck', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	return returned
	
def YOUList2(name, url, iconimage, desc, num, viewtype):
	returned = ""
	
	if General_TVModeDialog != "true" or returned != "ok":

		default = 'http://www.youtube.com/'
		url1 = 'channel/' + url + '/'
		url2 = 'user/' + url + '/'
		returned1 = urlcheck(default + url1)
		returned2 = urlcheck(default + url2)
		
		default2 = 'plugin://plugin.video.youtube/'

		if returned1 == 'ok': update_view(default2 + url1, num, viewtype)
		elif returned2 == 'ok': update_view(default2 + url2, num, viewtype)
		'''---------------------------'''

def setCustomFanart(addon, mode, admin, name, printpoint):
	x = "" ; printpoint = ""
	if not '.' in addon: addon = ""
	try: test = int(mode) + 1
	except: mode = ""
	
	if mode != "" and addon != "":
		'''Add-Fanart'''
		name = localize(20441)
		x = 'background'
		nolabel=localize(20438)
		yeslabel=localize(20441)
	
	if x != "":
		returned = dialogyesno(str(name), addonString_servicefeatherence(31).encode('utf-8'), nolabel=nolabel, yeslabel=yeslabel)
		if returned == 'ok':
			returned2, value = getRandom(0, min=0, max=100, percent=40)
			if returned2 == 'ok': notification('O_o???','Copy & Paste an image URL','',4000)
			'''remote'''
			value = dialogkeyboard("", yeslabel, 0, "1", "", "")
			if value != "skip":
				from shared_modules3 import urlcheck
				returned2 = urlcheck(value, ping=False)
				if returned2 != "ok":
					notification("URL Error", "Try again..", "", 2000)
					header = "URL Error"
					message = "Examine your URL for errors:" + newline + '[B]' + str(value) + '[/B]'
					diaogtextviewer(header,message)
				else:
					setsetting_custom1(addon, 'Fanart_Custom' + str(mode),str(value))
		else:
			'''local'''
			value = setPath(type=1,mask='pic', folderpath="")
			setsetting_custom1(addon, 'Fanart_Custom' + str(mode),str(value))
	
	text = 'addon' + space2 + str(addon) + space + 'mode' + space2 + str(mode) + space + 'x' + space2 + str(x) + newline
	printlog(title='setCustomFanart', printpoint=printpoint, text=text, level=0, option="")
	
def setaddonFanart(fanart, Fanart_Enable, Fanart_EnableCustom): #Fanart_EnableExtra
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	#admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	returned = "" ; printpoint = "" ; TypeError = "" ; extra = ""
	try:
		Fanart_Enable = getsetting('Fanart_Enable')
		Fanart_EnableCustom = getsetting('Fanart_EnableCustom')
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	if Fanart_Enable == "true" and extra == "":
		printpoint = printpoint + "1"
		if fanart != "":
			try:
				if os.path.exists(fanart):
					printpoint = printpoint + "4"
					returned = fanart
				elif "http://" in fanart or "www." in fanart:
					printpoint = printpoint + "5"
					returned = fanart
				else: pass
			except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
			
			printpoint = printpoint + "2"
			
		else: printpoint = printpoint + "8"
	else: printpoint = printpoint + "9"
	
	text =  "Fanart_Enable" + space2 + str(Fanart_Enable) + space + "Fanart_EnableCustom" + space2 + str(Fanart_EnableCustom) + newline + \
	"fanart" + space2 + str(fanart) + extra
	printlog(title='setaddonFanart', printpoint=printpoint, text=text, level=0, option="")
	return returned

def getAddonFanart(category, custom=""):
	#admin = xbmc.getInfoLabel('Skin.HasSetting(Admin)')
	#admin2 = xbmc.getInfoLabel('Skin.HasSetting(Admin2)')
	#admin3 = xbmc.getInfoLabel('Skin.HasSetting(Admin3)')
	returned = "" ; category_path = "" ; printpoint = "" ; extra = ""
	
	if custom != "":
		valid = urlcheck(custom, ping=False, timeout=1)
		
		if 'ok' in valid:
			printpoint = printpoint + "7"
			returned = custom
	if returned == "":
		if Fanart_EnableCustom != "true":
			returned = addonFanart
			printpoint = printpoint + "8"
		elif category == 100: category_path = Fanart_Custom100
		elif category == 101: category_path = Fanart_Custom101
		elif category == 102: category_path = Fanart_Custom102
		elif category == 103: category_path = Fanart_Custom103
		elif category == 104: category_path = Fanart_Custom104
		elif category == 105: category_path = Fanart_Custom105
		elif category == 106: category_path = Fanart_Custom106
		elif category == 107: category_path = Fanart_Custom107
		elif category == 108: category_path = Fanart_Custom108
		elif category == 109: category_path = Fanart_Custom109
		elif category == 110: category_path = Fanart_Custom110
		elif category == 111: category_path = Fanart_Custom111
		elif category == 112: category_path = Fanart_Custom112
		elif category == 113: category_path = Fanart_Custom113
		elif category == 114: category_path = Fanart_Custom114
		elif category == 115: category_path = Fanart_Custom115
		elif category == 116: category_path = Fanart_Custom116
		elif category == 117: category_path = Fanart_Custom117
		elif category == 118: category_path = Fanart_Custom118
		elif category == 119: category_path = Fanart_Custom119
		
		elif category == 10000: category_path = Fanart_Custom10000
		elif category == 10001: category_path = Fanart_Custom10001
		elif category == 10002: category_path = Fanart_Custom10002
		elif category == 10003: category_path = Fanart_Custom10003
		elif category == 10004: category_path = Fanart_Custom10004
		elif category == 10005: category_path = Fanart_Custom10005
		elif category == 10006: category_path = Fanart_Custom10006
		elif category == 10007: category_path = Fanart_Custom10007
		elif category == 10008: category_path = Fanart_Custom10008
		elif category == 10009: category_path = Fanart_Custom10009
		
		elif category == 10100: category_path = Fanart_Custom10100
		elif category == 10101: category_path = Fanart_Custom10101
		elif category == 10102: category_path = Fanart_Custom10102
		elif category == 10103: category_path = Fanart_Custom10103
		elif category == 10104: category_path = Fanart_Custom10104
		elif category == 10105: category_path = Fanart_Custom10105
		elif category == 10106: category_path = Fanart_Custom10106
		elif category == 10107: category_path = Fanart_Custom10107
		elif category == 10108: category_path = Fanart_Custom10108
		elif category == 10109: category_path = Fanart_Custom10109
		elif category == 10200: category_path = Fanart_Custom10200
		elif category == 10201: category_path = Fanart_Custom10201
		elif category == 10202: category_path = Fanart_Custom10202
		elif category == 10203: category_path = Fanart_Custom10203
		elif category == 10204: category_path = Fanart_Custom10204
		elif category == 10205: category_path = Fanart_Custom10205
		elif category == 10206: category_path = Fanart_Custom10206
		elif category == 10207: category_path = Fanart_Custom10207
		elif category == 10208: category_path = Fanart_Custom10208
		elif category == 10209: category_path = Fanart_Custom10209
		
		elif category == 11100: category_path = Fanart_Custom11100
		elif category == 11101: category_path = Fanart_Custom11101
		elif category == 11102: category_path = Fanart_Custom11102
		elif category == 11103: category_path = Fanart_Custom11103
		elif category == 11104: category_path = Fanart_Custom11104
		elif category == 11105: category_path = Fanart_Custom11105
		elif category == 11106: category_path = Fanart_Custom11106
		elif category == 11107: category_path = Fanart_Custom11107
		elif category == 11108: category_path = Fanart_Custom11108
		elif category == 11109: category_path = Fanart_Custom11109
		
		else:
			try:
				if "Custom_Playlist" in category:
					if category == "Custom_Playlist1": category_path = Custom_Playlist1_Fanart
					elif category == "Custom_Playlist2": category_path = Custom_Playlist2_Fanart
					elif category == "Custom_Playlist3": category_path = Custom_Playlist3_Fanart
					elif category == "Custom_Playlist4": category_path = Custom_Playlist4_Fanart
					elif category == "Custom_Playlist5": category_path = Custom_Playlist5_Fanart
					elif category == "Custom_Playlist6": category_path = Custom_Playlist6_Fanart
					elif category == "Custom_Playlist7": category_path = Custom_Playlist7_Fanart
					elif category == "Custom_Playlist8": category_path = Custom_Playlist8_Fanart
					elif category == "Custom_Playlist9": category_path = Custom_Playlist9_Fanart
					elif category == "Custom_Playlist10": category_path = Custom_Playlist10_Fanart
					else: printpoint = printpoint + "8"
			except Exception, TypeError:
				extra = extra + newline + "TypeError" + space2 + str(TypeError)
				printpoint = printpoint + "8"
	
	
		if category_path != "":
			if "http://" in category_path or "www." in category_path:
				printpoint = printpoint + "7a"
				returned = category_path
				#valid = urlcheck(value, ping=False)
			else:
				try:
					category_path = os.path.join(xbmc.translatePath(category_path).decode("utf-8"))
					category_path = category_path.encode('utf-8')
				except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError).encode('utf-8')
				if os.path.exists(category_path):
					printpoint = printpoint + "7b"
					
					if 1 + 1 == 3:
						category_path = os.path.join(xbmc.translatePath(category_path).decode("utf-8"))
						try: category_path = category_path.encode('utf-8')
						except: pass
					
				else:
					setsetting('Fanart_Custom'+str(category),"")
					printpoint = printpoint + "9d"
		else:
			printpoint = printpoint + "9"
			
	if "9" in printpoint or "8" in printpoint:
		try:
			if os.path.exists(addonFanart): returned = addonFanart
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			returned = ""
	
	elif "7" in printpoint and custom == "": returned = category_path
	
	text = "category" + space2 + str(category) + space + "custom" + space2 + str(custom) + newline + \
	"returned" + space2 + str(returned) + newline + \
	"category_path" + space2 + str(category_path) + extra
	printlog(title='getAddonFanart', printpoint=printpoint, text=text, level=0, option="")
	return returned
	
def pluginend(admin):
	try: from modules import *
	except: pass
	try: from modulesp import *
	except: pass
	printpoint = "" ; TypeError = "" ; extra = ""
	
	'''------------------------------
	---params------------------------
	------------------------------'''
	params=get_params()
	url=None
	name=None
	mode=None
	iconimage=None
	desc=None
	num=None
	viewtype=None
	fanart=None
	#value=None
	'''---------------------------'''
	try: url=urllib.unquote_plus(params["url"])
	except: pass
	try: name=urllib.unquote_plus(params["name"])
	except: pass
	try: iconimage=urllib.unquote_plus(params["iconimage"])
	except: pass
	try: mode=int(params["mode"])
	except: pass
	try: desc=urllib.unquote_plus(params["desc"])
	except: pass
	
	try: num=urllib.unquote_plus(params["num"])
	except: pass
	try: viewtype=int(params["viewtype"])
	except: pass
	try: fanart=urllib.unquote_plus(params["fanart"])
	except: pass
	#try: value=urllib.unquote_plus(params["value"])
	#except: pass
	'''---------------------------'''

	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	try: IconImageS = str(IconImage)
	except: IconImageS = "None"
	'''---------------------------'''
	text = "mode" + space2 + str(mode) + newline + \
	"url" + space2 + str(url) + newline + \
	"name" + space2 + str(name) + space + "IconImage" + space2 + IconImageS + space + "desc" + space2 + str(desc) + newline + \
	"viewtype" + space2 + str(viewtype) + space + "fanart" + space2 + str(fanart) + newline + \
	"params" + space2 + str(params)
	printlog(title='pluginend', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

	'''------------------------------
	---MODES-LIST--------------------
	------------------------------'''
	if mode == None or ((url == None or len(url)<1) and mode < 100): 
		CATEGORIES()
		systemlanguage = xbmc.getInfoLabel('System.Language')
		try:
			getsetting('Addon_Update')
			getsetting('Addon_Version')
			getsetting('Addon_UpdateDate')
			getsetting('Addon_UpdateLog')
			getsetting('Addon_ShowLog')
			getsetting('Addon_ShowLog2')
			
			VerReset = ""
			if addonID == 'plugin.video.featherence.music' and Addon_Version == '0.0.17': VerReset = "true"
			checkAddon_Update(admin, Addon_Update, Addon_Version, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2, VerReset)
			if Addon_UpdateLog == "true":
				if addonID == 'plugin.video.featherence.kids':
					if systemlanguage != "Hebrew" and systemlanguage != "English": notification("This addon does not support "+str(systemlanguage)+" yet","...","",2000)
					else: notification('featherence',addonString_servicefeatherence(63).encode('utf-8'),'',2000)
					installaddonP(admin, 'repository.xbmc-israel', version="", update=True, silent=False)
					'''---------------------------'''
				elif addonID == 'plugin.video.featherence.music':
					if systemlanguage != "Hebrew" and systemlanguage != "English": notification("This addon does not support "+str(systemlanguage)+" yet","...","",2000)
					else: notification('featherence',addonString_servicefeatherence(63).encode('utf-8'),'',2000)
					
					if Addon_Version == '0.0.17' or Addon_Version == '0.0.18': setsetting('General_OnlyPopular','true')

					
		except Exception, TypeError:
			extra = extra + newline + "TypeError" + space2 + str(TypeError)
			printpoint = printpoint + "2"
			'''---------------------------'''
	
	#1-99 = COMMANDS
	elif mode == 1:
		pass
	elif mode == 2:
		LocalSearch(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 3:
		YoutubeSearch(name, url, desc, num, viewtype)
	elif mode == 4:
		#play_video(url) #API V3 issues
		play_video2(url)
	elif mode == 5:
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 6:
		MultiVideos(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 7:
		ListLive(url)
	elif mode == 8:
		update_view(url, num, viewtype)
	elif mode == 9:
		YOUList2(name, url, iconimage, desc, num, viewtype)
	elif mode == 10:
		play_view(url, num, viewtype)
	elif mode == 11:
		pass #YOULinkAll(url)
	elif mode == 12:
		#PlayPlayList(url)
		PlayPlayList2(url)
	elif mode == 13:
		#ListPlaylist(url, num)
		ListPlaylist2(url, num, viewtype)
	elif mode == 14:       
		pass #SeasonsFromShow(url)
	elif mode == 15:
		pass
	elif mode == 16:       
		ShowFromUser(url)
	elif mode == 17:
		mode = TvMode2(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 18:
		'''Custom Playlist'''
		mode = TvMode2(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 20:
		AddCustom(mode, name, url, iconimage, desc, num, viewtype)
	elif mode == 21:
		ManageCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 22:
		AdvancedCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 23:
		MoveCustom(mode, name, url, iconimage, desc, num, viewtype, fanart)
	elif mode == 100:
		CATEGORIES100(admin)
	elif mode == 101:
		CATEGORIES101(admin)
	elif mode == 102: 
		CATEGORIES102(admin)
	elif mode == 103:       
		CATEGORIES103(admin)
	elif mode == 104:       
		CATEGORIES104(admin)
	elif mode == 105:    
		CATEGORIES105(admin)
	elif mode == 106:       
		CATEGORIES106(admin)
	elif mode == 107:       
		CATEGORIES107(admin)
	elif mode == 108:       
		CATEGORIES108(admin)
	elif mode == 109:       
		CATEGORIES109(admin)
	
	elif mode == 110:       
		CATEGORIES110(admin)
	elif mode == 111:
		CATEGORIES111(admin)
	elif mode == 112: 
		CATEGORIES112(admin)
	elif mode == 113:       
		CATEGORIES113(admin)
	elif mode == 114:       
		CATEGORIES114(admin)
	elif mode == 115:    
		CATEGORIES115(admin)
	elif mode == 116:       
		CATEGORIES116(admin)
	elif mode == 117:       
		CATEGORIES117(admin)
	elif mode == 118:       
		CATEGORIES118(admin)
	elif mode == 119:       
		CATEGORIES119(admin)
	
	elif mode == 120:       
		CATEGORIES120(admin)	
	elif mode == 121:
		CATEGORIES121(admin)
	elif mode == 122: 
		CATEGORIES122(admin)
	elif mode == 123:       
		CATEGORIES123(admin)
	elif mode == 124:       
		CATEGORIES124(admin)
	elif mode == 125:    
		CATEGORIES125(admin)
	elif mode == 126:       
		CATEGORIES126(admin)
	elif mode == 127:       
		CATEGORIES127(admin)
	elif mode == 128:       
		CATEGORIES128(admin)
	elif mode == 129:       
		CATEGORIES129(admin)
	
	elif mode == 130:
		CATEGORIES130(admin)
	elif mode == 131:
		CATEGORIES131(admin)
	elif mode == 132: 
		CATEGORIES132(admin)
	elif mode == 133:       
		CATEGORIES133(admin)
	elif mode == 134:       
		CATEGORIES134(admin)
	elif mode == 135:    
		CATEGORIES135(admin)
	elif mode == 136:       
		CATEGORIES136(admin)
	elif mode == 137:       
		CATEGORIES137(admin)
	elif mode == 138:       
		CATEGORIES138(admin)
	elif mode == 139:       
		CATEGORIES139(admin)
	
	#10101+ = SUB-CATEGORIES2
	elif mode == 10001:
		CATEGORIES10001(name, iconimage, desc, fanart)
	elif mode == 10002:
		CATEGORIES10002(name, iconimage, desc, fanart)
	elif mode == 10003:
		CATEGORIES10003(name, iconimage, desc, fanart)
	elif mode == 10004:
		CATEGORIES10004(name, iconimage, desc, fanart)
	elif mode == 10005:
		CATEGORIES10005(name, iconimage, desc, fanart)
	elif mode == 10006:
		CATEGORIES10006(name, iconimage, desc, fanart)
	elif mode == 10007:
		CATEGORIES10007(name, iconimage, desc, fanart)
	elif mode == 10008:
		CATEGORIES10008(name, iconimage, desc, fanart)
	elif mode == 10009:
		CATEGORIES10009(name, iconimage, desc, fanart)
		
	elif mode == 10101:
		CATEGORIES10101(name, iconimage, desc, fanart)
	elif mode == 10102:
		CATEGORIES10102(name, iconimage, desc, fanart)
	elif mode == 10103:
		CATEGORIES10103(name, iconimage, desc, fanart)
	elif mode == 10104:
		CATEGORIES10104(name, iconimage, desc, fanart)
	elif mode == 10105:
		CATEGORIES10105(name, iconimage, desc, fanart)
	elif mode == 10106:
		CATEGORIES10106(name, iconimage, desc, fanart)
	elif mode == 10107:
		CATEGORIES10107(name, iconimage, desc, fanart)
	elif mode == 10108:
		CATEGORIES10108(name, iconimage, desc, fanart)
	elif mode == 10109:
		CATEGORIES10109(name, iconimage, desc, fanart)
		
	elif mode == 10201:
		CATEGORIES10201(name, iconimage, desc, fanart)
	elif mode == 10202:
		CATEGORIES10202(name, iconimage, desc, fanart)
	elif mode == 10203:
		CATEGORIES10203(name, iconimage, desc, fanart)
	elif mode == 10204:
		CATEGORIES10204(name, iconimage, desc, fanart)
	elif mode == 10205:
		CATEGORIES10205(name, iconimage, desc, fanart)
	elif mode == 10206:
		CATEGORIES10206(name, iconimage, desc, fanart)
	elif mode == 10207:
		CATEGORIES10207(name, iconimage, desc, fanart)
	elif mode == 10208:
		CATEGORIES10208(name, iconimage, desc, fanart)
	elif mode == 10209:
		CATEGORIES10209(name, iconimage, desc, fanart)
	
	elif mode == 10301:
		CATEGORIES10301(name, iconimage, desc, fanart)
	elif mode == 10302:
		CATEGORIES10302(name, iconimage, desc, fanart)
	elif mode == 10303:
		CATEGORIES10303(name, iconimage, desc, fanart)
	elif mode == 10304:
		CATEGORIES10304(name, iconimage, desc, fanart)
	elif mode == 10305:
		CATEGORIES10305(name, iconimage, desc, fanart)
	elif mode == 10306:
		CATEGORIES10306(name, iconimage, desc, fanart)
	elif mode == 10307:
		CATEGORIES10307(name, iconimage, desc, fanart)
	elif mode == 10308:
		CATEGORIES10308(name, iconimage, desc, fanart)
	elif mode == 10309:
		CATEGORIES10309(name, iconimage, desc, fanart)
	
	elif mode == 10401:
		CATEGORIES10401(name, iconimage, desc, fanart)
	elif mode == 10402:
		CATEGORIES10402(name, iconimage, desc, fanart)
	elif mode == 10403:
		CATEGORIES10403(name, iconimage, desc, fanart)
	elif mode == 10404:
		CATEGORIES10405(name, iconimage, desc, fanart)
	elif mode == 10406:
		CATEGORIES10406(name, iconimage, desc, fanart)
	elif mode == 10407:
		CATEGORIES10407(name, iconimage, desc, fanart)
	elif mode == 10408:
		CATEGORIES10408(name, iconimage, desc, fanart)
	elif mode == 10409:
		CATEGORIES10409(name, iconimage, desc, fanart)
	elif mode == 10410:
		CATEGORIES10410(name, iconimage, desc, fanart)
	elif mode == 10411:
		CATEGORIES10411(name, iconimage, desc, fanart)
	elif mode == 10412:
		CATEGORIES10412(name, iconimage, desc, fanart)
	elif mode == 10413:
		CATEGORIES10413(name, iconimage, desc, fanart)
	elif mode == 10414:
		CATEGORIES10414(name, iconimage, desc, fanart)
	elif mode == 10415:
		CATEGORIES10415(name, iconimage, desc, fanart)
	elif mode == 10416:
		CATEGORIES10416(name, iconimage, desc, fanart)
	elif mode == 10417:
		CATEGORIES10417(name, iconimage, desc, fanart)
	elif mode == 10418:
		CATEGORIES10418(name, iconimage, desc, fanart)
	elif mode == 10419:
		CATEGORIES10419(name, iconimage, desc, fanart)
	elif mode == 10420:
		CATEGORIES10420(name, iconimage, desc, fanart)
	elif mode == 10421:
		CATEGORIES10421(name, iconimage, desc, fanart)
	elif mode == 10422:
		CATEGORIES10422(name, iconimage, desc, fanart)
	elif mode == 10423:
		CATEGORIES10423(name, iconimage, desc, fanart)
	elif mode == 10424:
		CATEGORIES10424(name, iconimage, desc, fanart)
	elif mode == 10425:
		CATEGORIES10425(name, iconimage, desc, fanart)
	elif mode == 10426:
		CATEGORIES10426(name, iconimage, desc, fanart)
	elif mode == 10427:
		CATEGORIES10427(name, iconimage, desc, fanart)
	elif mode == 10428:
		CATEGORIES10428(name, iconimage, desc, fanart)
	elif mode == 10429:
		CATEGORIES10429(name, iconimage, desc, fanart)
	elif mode == 10430:
		CATEGORIES10430(name, iconimage, desc, fanart)
	
	elif mode == 10501:
		CATEGORIES10501(name, iconimage, desc, fanart)
	elif mode == 10502:
		CATEGORIES10502(name, iconimage, desc, fanart)
	elif mode == 10503:
		CATEGORIES10503(name, iconimage, desc, fanart)
	elif mode == 10504:
		CATEGORIES10504(name, iconimage, desc, fanart)
	elif mode == 10505:
		CATEGORIES10505(name, iconimage, desc, fanart)
	elif mode == 10506:
		CATEGORIES10506(name, iconimage, desc, fanart)
	elif mode == 10507:
		CATEGORIES10507(name, iconimage, desc, fanart)
	elif mode == 10508:
		CATEGORIES10508(name, iconimage, desc, fanart)
	elif mode == 10509:
		CATEGORIES10509(name, iconimage, desc, fanart)
	
	elif mode == 10601:
		CATEGORIES10601(name, iconimage, desc, fanart)
	elif mode == 10602:
		CATEGORIES10602(name, iconimage, desc, fanart)
	elif mode == 10603:
		CATEGORIES10603(name, iconimage, desc, fanart)
	elif mode == 10604:
		CATEGORIES10604(name, iconimage, desc, fanart)
	elif mode == 10605:
		CATEGORIES10605(name, iconimage, desc, fanart)
	elif mode == 10606:
		CATEGORIES10606(name, iconimage, desc, fanart)
	elif mode == 10607:
		CATEGORIES10607(name, iconimage, desc, fanart)
	elif mode == 10608:
		CATEGORIES10608(name, iconimage, desc, fanart)
	elif mode == 10609:
		CATEGORIES10609(name, iconimage, desc, fanart)
	
	elif mode == 10701:
		CATEGORIES10701(name, iconimage, desc, fanart)
	elif mode == 10702:
		CATEGORIES10702(name, iconimage, desc, fanart)
	elif mode == 10703:
		CATEGORIES10703(name, iconimage, desc, fanart)
	elif mode == 10704:
		CATEGORIES10704(name, iconimage, desc, fanart)
	elif mode == 10705:
		CATEGORIES10705(name, iconimage, desc, fanart)
	elif mode == 10706:
		CATEGORIES10706(name, iconimage, desc, fanart)
	elif mode == 10707:
		CATEGORIES10707(name, iconimage, desc, fanart)
	elif mode == 10708:
		CATEGORIES10708(name, iconimage, desc, fanart)
	elif mode == 10709:
		CATEGORIES10709(name, iconimage, desc, fanart)
	
	elif mode == 10801:
		CATEGORIES10801(name, iconimage, desc, fanart)
	elif mode == 10802:
		CATEGORIES10802(name, iconimage, desc, fanart)
	elif mode == 10803:
		CATEGORIES10803(name, iconimage, desc, fanart)
	elif mode == 10804:
		CATEGORIES10804(name, iconimage, desc, fanart)
	elif mode == 10805:
		CATEGORIES10805(name, iconimage, desc, fanart)
	elif mode == 10806:
		CATEGORIES10806(name, iconimage, desc, fanart)
	elif mode == 10807:
		CATEGORIES10807(name, iconimage, desc, fanart)
	elif mode == 10808:
		CATEGORIES10808(name, iconimage, desc, fanart)
	elif mode == 10809:
		CATEGORIES10809(name, iconimage, desc, fanart)
		
	elif mode == 10901:
		CATEGORIES10901(name, iconimage, desc, fanart)
	elif mode == 10902:
		CATEGORIES10902(name, iconimage, desc, fanart)
	elif mode == 10903:
		CATEGORIES10903(name, iconimage, desc, fanart)
	elif mode == 10904:
		CATEGORIES10904(name, iconimage, desc, fanart)
	elif mode == 10905:
		CATEGORIES10905(name, iconimage, desc, fanart)
	elif mode == 1090504:
		CATEGORIES1090504(name, iconimage, desc, fanart)
	elif mode == 10906:
		CATEGORIES10906(name, iconimage, desc, fanart)
	elif mode == 10907:
		CATEGORIES10907(name, iconimage, desc, fanart)
	elif mode == 10908:
		CATEGORIES10908(name, iconimage, desc, fanart)
	elif mode == 10909:
		CATEGORIES10909(name, iconimage, desc, fanart)
	elif mode == 10910:
		CATEGORIES10910(name, iconimage, desc, fanart)
	elif mode == 10911:
		CATEGORIES10911(name, iconimage, desc, fanart)
	elif mode == 10912:
		CATEGORIES10912(name, iconimage, desc, fanart)
	elif mode == 10913:
		CATEGORIES10913(name, iconimage, desc, fanart)
	elif mode == 10914:
		CATEGORIES10914(name, iconimage, desc, fanart)
	elif mode == 10915:
		CATEGORIES10915(name, iconimage, desc, fanart)
	elif mode == 10916:
		CATEGORIES10916(name, iconimage, desc, fanart)
	elif mode == 10917:
		CATEGORIES10917(name, iconimage, desc, fanart)
	elif mode == 10918:
		CATEGORIES10918(name, iconimage, desc, fanart)
	elif mode == 10919:
		CATEGORIES10919(name, iconimage, desc, fanart)
	elif mode == 10920:
		CATEGORIES10920(name, iconimage, desc, fanart)
	elif mode == 10921:
		CATEGORIES10921(name, iconimage, desc, fanart)
	elif mode == 10922:
		CATEGORIES10922(name, iconimage, desc, fanart)
	elif mode == 10923:
		CATEGORIES10923(name, iconimage, desc, fanart)
	elif mode == 10924:
		CATEGORIES10924(name, iconimage, desc, fanart)
	elif mode == 10925:
		CATEGORIES10925(name, iconimage, desc, fanart)
	elif mode == 10926:
		CATEGORIES10926(name, iconimage, desc, fanart)
	elif mode == 10927:
		CATEGORIES10927(name, iconimage, desc, fanart)
	elif mode == 10928:
		CATEGORIES10928(name, iconimage, desc, fanart)
	elif mode == 10929:
		CATEGORIES10929(name, iconimage, desc, fanart)
	elif mode == 10930:
		CATEGORIES10930(name, iconimage, desc, fanart)
	
	elif mode == 11101:
		CATEGORIES11101(name, iconimage, desc, fanart)
	elif mode == 11102:
		CATEGORIES11102(name, iconimage, desc, fanart)
	elif mode == 11103:
		CATEGORIES11103(name, iconimage, desc, fanart)
	elif mode == 11104:
		CATEGORIES11104(name, iconimage, desc, fanart)
	elif mode == 11105:
		CATEGORIES11105(name, iconimage, desc, fanart)
	elif mode == 11106:
		CATEGORIES11106(name, iconimage, desc, fanart)
	elif mode == 11107:
		CATEGORIES11107(name, iconimage, desc, fanart)
	elif mode == 11108:
		CATEGORIES11108(name, iconimage, desc, fanart)
	elif mode == 11109:
		CATEGORIES11109(name, iconimage, desc, fanart)
		
	else: notification("?","","",1000)
	
	if mode != 17 and mode != 5 and mode != 21: # and mode != 20
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
		#xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL, name)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_NONE)
		if mode > 130:
			xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
			xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE, name)
		#xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE, name)
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
		printpoint = printpoint + "7"
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	printlog(title='pluginend', printpoint=printpoint, text=extra, level=0, option="")
	'''---------------------------'''
	return url, name, mode, iconimage, desc, num, viewtype, fanart
	
	
def pluginend2(admin, url, containerfolderpath, viewtype):
	printpoint = "" ; count = 0 ; countmax = 10 ; url = str(url) ; containerfolderpath2 = ""
	returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
	
	#xbmc.sleep(1000) #TIME FOR DIALOGBUSY
	'''------------------------------
	---countmax-ADJUST---------------
	------------------------------'''
	if "plugin.video.10qtv" in url: countmax = 40
	'''---------------------------'''
	
	while (count < countmax and (returned_Dialog == "dialogbusyW" or returned_Dialog == "dialogprogressW")) or (count < 2 and returned_Dialog == "") and not xbmc.abortRequested:
		count += 1
		if count == 1: printpoint = printpoint + "1"
		xbmc.sleep(500)
		returned_Dialog, returned_Header, returned_Message = checkDialog(admin)
		'''---------------------------'''
		
	if count < countmax:
		printpoint = printpoint + "2"
		if count == 0: xbmc.sleep(1000)
		else: xbmc.sleep(500)
		containerfolderpath2 = xbmc.getInfoLabel('Container.FolderPath')
		if viewtype == None:
			'''------------------------------
			---viewtype-ADJUST---------------
			------------------------------'''
			printpoint = printpoint + "3"
			if containerfolderpath2 == 'plugin://'+addonID+'/?&': printpoint = printpoint + "4" ; viewtype = 50
			elif "http://nickjr.walla.co.il/" in url: viewtype = 50
			elif ("plugin.video.gozlan.me" in url or "plugin.video.seretil" in url or "plugin.video.supercartoons" in url or "plugin.video.sdarot.tv" in url or "seretil.me" in url): viewtype = 58
			'''---------------------------'''
		if containerfolderpath != containerfolderpath2 or "4" in printpoint: #GAL CHECK THIS! #containerfolderpath2 == "plugin://"+addonID+"/"
			printpoint = printpoint + "5"
			setView('', viewtype, containerfolderpath2)
			'''---------------------------'''
	
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "count" + space2 + str(count) + space + "returned_Dialog" + space2 + returned_Dialog + space + "containerfolderpath/2" + newline + \
	str(containerfolderpath) + newline + \
	str(containerfolderpath2) + newline + \
	"url" + space2 + str(url)
	printlog(title='pluginend2', printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''