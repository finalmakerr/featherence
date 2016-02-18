# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,random
import json
from random import shuffle

from variables import *

from shared_modules import *
from shared_modules3 import *

'''
shared_modules5 is used for Kodi's plugins.
Import the module and input the addDir in your addon module.py file.
'''

def checkMode11(mode, name, url, iconimage, desc, num, viewtype, fanart):
	printpoint = "" ; id_L = [] ; title_L = [] ; thumb_L = [] ; desc_L = [] ; fanart_L = []
					   
					   #<url="&googledrive=0B02H6jdF_-acQkNYUFYxNkZYZzQ"/>
									 #<title="דרגון בול זי פרק 69
												  #"/><thumb="
																  #"/><desc=""/>
	match = re.compile('<url="(.+?)"/><title="(.+?)"/><thumb="(.+?)"/><desc="(.+?)"/>').findall(url)
	blankL = ["",None]
	url2 = regex_from_to(url, '<url="', '"/>', excluding=True)
	name2 = regex_from_to(url, '<title="', '"/>', excluding=True)
	iconimage2 = regex_from_to(url, '<thumb="', '"/>', excluding=True)
	desc2 = regex_from_to(url, '<desc="', '"/>', excluding=True)
	
	if url2 in blankL or name2 in blankL: printpoint = printpoint + '6'
	else:
		id_L.append(url2)
		title_L.append(name2)
		if iconimage2 in blankL: thumb_L.append(iconimage)
		else: thumb_L.append(iconimage2)
		if desc2 in blankL: desc_L.append(desc)
		else: desc_L.append(desc2)
		fanart_L.append(desc)
	
	text = 'url' + space2 + str(url) + newline + \
	'id_L' + space2 + str(id_L) + newline + \
	'name' + space2 + str(name) + newline + \
	'iconimage' + space2 + str(iconimage) + newline + \
	'desc' + space2 + str(desc) + newline + \
	'match' + space2 + str(match)
	printlog(title="checkMode11", printpoint=printpoint, text=text, level=0, option="")
	return id_L, title_L, thumb_L, desc_L, fanart_L
	
def GetHTML(url, agent = 'Apple-iPhone/'):
    html = geturllib.GetURL(url, 86400, agent)
    html = html.replace('\n',            '')
    html = html.replace('\r',            '')
    html = html.replace('\t',            '')
    html = html.replace('&quot;',        '"')
    html = html.replace('title="Search', '')
    return html

	
def getUserAgent():
    agents = []
    agents.append('Mozilla/5.0 (Android; Mobile; rv:%d.0) Gecko/%d.0 Firefox/%d.0')
    agents.append('Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.%d (KHTML, like Gecko) Chrome/%d.0.1847.114 Mobile Safari/537.%d')
    agents.append('Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/5%d.51.1 (KHTML, like Gecko) CriOS/%d.0.1847.%d Mobile/11B554a')
    agents.append('Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/5%d.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B5%da Safari/9537.%d')
    agents.append('Mozilla/5.0 (iPhone; CPU OS 7_0_4 like Mac OS X) AppleWebKit/5%d.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B%d4a Safari/9537.%d')
    agents.append('Mozilla/5.0 (Android; Mobile; rv:%d.0) Gecko/%d.0 Firefox/%d.0')

    agent = random.choice(agents) % (random.randint(10, 40), random.randint(10, 40), random.randint(10, 40))

    return '?|User-Agent=%s' % agent

def playURL(mode, name, url, iconimage, desc, num, viewtype, fanart):
	printpoint = ""
	url += getUserAgent()
	iconimage += getUserAgent()
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc} )
	liz.setProperty('IsPlayable', 'true')
	liz.setPath(url)
	#xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
	if mode == 44:
		xbmc.executebuiltin('PlayMedia('+url+')')
	
def listURL(mode, name, url, iconimage, desc, num, viewtype, fanart):
	from shared_modules3 import addDir
	printpoint = "" ; TypeError = "" ; extra = ""
	if mode == 41 or mode == 42:
		url += getUserAgent()
		iconimage += getUserAgent()

	addDir(name, url, mode, iconimage, desc, str(num), viewtype, fanart)
	
	if mode == 42:
		return url
		
def listURLS(id_L, title_L, thumb_L, desc_L, url2, desc2, iconimage2, name2):
	url2 += getUserAgent()
	iconimage2 += getUserAgent()
	
	id_L.append(url2)
	title_L.append(name2)
	thumb_L.append(iconimage2)
	desc_L.append(desc2)
	return id_L, title_L, thumb_L, desc_L
	
def listURLS_(mode, name, url, iconimage, desc, page, viewtype, fanart):
	printpoint = "" ; TypeError = "" ; extra = ""
	url_ = url ; total = 0 ; pageL = [] ; html = "" ; match = "" ; match_page = ""
	id_L = [] ; title_L = [] ; thumb_L = [] ; desc_L = []
	
	try: test = page + 1
	except: page = 1
	if 'http://www.supercartoons.net/' in url: id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL = listURLS_1(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart)
	elif 'www.moridim.tv' in url: id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL = listURLS_3(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart)
	elif '&googledrive2=' in url:
		url = url.replace('&googledrive2=',"")
		if 'http://dragonballz.co.il' in url:
			id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL = listURLS_2(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart)
	else: printpoint = '9'
	
	if match != "": match = 'ok'
	#if match_page != "": match_page = 'ok'
	text = 'url_' + space2 + str(url_) + newline + \
	'url' + space2 + str(url) + newline + \
	'total' + space2 + str(total) + newline + \
	'name' + space2 + str(name) + newline + \
	'html' + space2 + str(html) + newline + \
	'pageL' + space2 + str(pageL) + newline + \
	'match' + space2 + str(match) + newline + \
	'match_page' + space2 + str(match_page) + extra
	printlog(title="listURLS_", printpoint=printpoint, text=text, level=0, option="")
	
	return id_L, title_L, thumb_L, desc_L
	
def listURLS_1(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart):
	extra = "" ; TypeError = "" ; pageL = []
	pageP = int(page) - 1
	pageN = int(page) + 1
	html_ = GetHTML(url + str(page))
	
	match_page = regex_from_to(html_, '<div class="pages">', '</div>', excluding=False)
	match_page2 = re.compile('<a href="(.+?)">(.+?)</a>').findall(match_page)
	for page_url, page_num in match_page2:
		try: pageL.append(int(page_num))
		except Exception, TypeError: extra = extra + newline + 'TypeError' + space2 + str(TypeError) + space + 'page_num' + space2 + str(page_num)
	
	if mode == 42:
		page = random.choice(pageL)
		
	html = '<div class="cartoon">' + html_.split('<div class="cartoon">', 1)[-1]
	
	match = re.compile('<div class="cartoon"><a class="img" href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+?<span class="title"><a href=".+?" title=".+?">(.+?)</a></span></div>').findall(html)

	if pageP in pageL:
		from shared_modules3 import addDir
		listURL(40, 'Previous Page', url, iconimage, desc, str(pageP), viewtype, fanart)
		addDir('Home','plugin://' + addonID,8,featherenceserviceicons_path + 'home.png',desc,'1',50,fanart)
	i = 0
	for url2, desc2, iconimage2, name2 in match:
		url2 = url2.replace('/cartoon/', '/video/')
		url2 = url2.replace('.html', '.mp4')
		if mode == 42:
			id_L, title_L, thumb_L, desc_L = listURLS(id_L, title_L, thumb_L, desc_L, url2, desc2, iconimage2, name2)
		else:
			listURL(41, name2, url2, iconimage2, desc2, str(page), viewtype, fanart)
		i += 1
	if pageN in pageL:
		listURL(40, 'Next Page', url, iconimage, desc, str(pageN), viewtype, fanart)
	
	total = i
	return id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL
	
def listURLS_2(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart):
	extra = "" ; TypeError = "" ; pageL = [] ; match_page = "" ; match_page2 = ""
	pageP = int(page) - 1
	pageN = int(page) + 1
	html_ = GetHTML(url)

	print 'bla ' + html_
	if 1 + 1 == 3:
		match_page = regex_from_to(html_, '<article class', '</article>', excluding=False)
		match_page2 = re.compile('<a href="(.+?)">(.+?)</a>').findall(match_page)
		for page_url, page_num in match_page2:
			try: pageL.append(int(page_num))
			except Exception, TypeError: extra = extra + newline + 'TypeError' + space2 + str(TypeError) + space + 'page_num' + space2 + str(page_num)
	
	if mode == 42:
		page = random.choice(pageL)
		
	html = '<article class' + html_.split('<article class', 1)[-1]
	
	match = re.compile('<a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+?<span class="title"><a href=".+?" title=".+?">(.+?)</a></span></div>').findall(html)

	if pageP in pageL:
		from shared_modules3 import addDir
		listURL(40, 'Previous Page', url, iconimage, desc, str(pageP), viewtype, fanart)
		addDir('Home','plugin://' + addonID,8,featherenceserviceicons_path + 'home.png',desc,'1',50,fanart)
	i = 0
	for url2, desc2, iconimage2, name2 in match:
		url2 = url2.replace('/cartoon/', '/video/')
		url2 = url2.replace('.html', '.mp4')
		if mode == 42:
			id_L, title_L, thumb_L, desc_L = listURLS(id_L, title_L, thumb_L, desc_L, url2, desc2, iconimage2, name2)
		else:
			listURL(41, name2, url2, iconimage2, desc2, str(page), viewtype, fanart)
		i += 1
	if pageN in pageL:
		listURL(40, 'Next Page', url, iconimage, desc, str(pageN), viewtype, fanart)
	
	total = i
	return id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL

def listURLS_3(id_L, title_L, thumb_L, desc_L, mode, name, url, iconimage, desc, page, viewtype, fanart):
	extra = "" ; TypeError = "" ; pageL = []
	pageP = int(page) - 1
	pageN = int(page) + 1
	html_ = GetHTML(url + str(page))
	
	match_page = regex_from_to(html_, '<div class="pages">', '</div>', excluding=False)
	match_page2 = re.compile('<a href="(.+?)">(.+?)</a>').findall(match_page)
	for page_url, page_num in match_page2:
		try: pageL.append(int(page_num))
		except Exception, TypeError: extra = extra + newline + 'TypeError' + space2 + str(TypeError) + space + 'page_num' + space2 + str(page_num)
	
	if mode == 42:
		page = random.choice(pageL)
		
	html = '<div class="cartoon">' + html_.split('<div class="cartoon">', 1)[-1]
	
	match = re.compile('<div class="cartoon"><a class="img" href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+?<span class="title"><a href=".+?" title=".+?">(.+?)</a></span></div>').findall(html)

	if pageP in pageL:
		from shared_modules3 import addDir
		listURL(40, 'Previous Page', url, iconimage, desc, str(pageP), viewtype, fanart)
		addDir('Home','plugin://' + addonID,8,featherenceserviceicons_path + 'home.png',desc,'1',50,fanart)
	i = 0
	for url2, desc2, iconimage2, name2 in match:
		url2 = url2.replace('/cartoon/', '/video/')
		url2 = url2.replace('.html', '.mp4')
		if mode == 42:
			id_L, title_L, thumb_L, desc_L = listURLS(id_L, title_L, thumb_L, desc_L, url2, desc2, iconimage2, name2)
		else:
			listURL(41, name2, url2, iconimage2, desc2, str(page), viewtype, fanart)
		i += 1
	if pageN in pageL:
		listURL(40, 'Next Page', url, iconimage, desc, str(pageN), viewtype, fanart)
	
	total = i
	return id_L, title_L, thumb_L, desc_L, extra, url, html, match, match_page, total, pageL
	
