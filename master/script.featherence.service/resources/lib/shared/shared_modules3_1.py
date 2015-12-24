import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,random
import json
from random import shuffle

from variables import *
#from modules import *
from shared_modules import *

def getAPIdata(x, name, iconimage, desc, fanart):
	printpoint = "" ; TypeError = "" ; extra = ""
	finalurl = "" ; url = "" ; prms = "" ; id = "" ; iconimage_ = "" ; desc_ = ""
	#print 'x[:1]' + space2 + str(x[:1]) + newline + 'x[:-1]' + space2 + str(x[:-1]) + newline + 'x[1:]' + space2 + str(x[1:]) + newline + 'x[-1:]' + space2 + str(x[-1:])
	if 'getAPIdata=' in x:
		if x[:1] == '[': x = x.replace('[',"",1)
		if x[-1:] == ']': x = x.replace(']',"")
		if x[:1] == "'": x = x.replace("'","",1)
		if x[-1:] == "'": x = x.replace("'","")
		#x = find_string(name, "getAPIdata=", "")
		x = x.replace('getAPIdata=',"")
		#print 'blabla' + space2 + str(x)
	try:
		#if 1 + 1 == 2:
		if '&youtube_ch=' in x:
			printpoint = printpoint + '1'
			if '/playlists' in x: x.replace('/playlists',"")
			x2 = x.replace('&youtube_ch=',"")
			url = 'https://www.googleapis.com/youtube/v3/channels?forUsername='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults=1'
			link = OPEN_URL(url)
			#print 'link__' + space2 + str(link)
			if '"totalResults": 0' in link or '"items": []' in link:
				printpoint = printpoint + '2'
				url = 'https://www.googleapis.com/youtube/v3/channels?id='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults=1'
		elif '&youtube_se=' in x:
			x2 = x.replace('&youtube_se=',"")
			x2 = clean_commonsearch(x2)
			url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&safeSearch=moderate&type=video&part=snippet&maxResults=1&pageToken='
		elif "&youtube_se2=" in x:
			'''WIP'''
			printpoint = printpoint + "4"
			x2 = x.replace("&youtube_se2=","")
			x2 = clean_commonsearch(x2)
			url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&safeSearch=moderate&type=channel&part=snippet&maxResults=1&pageToken='
			print 'blabla2' + space2 + str(url)
		elif '&youtube_pl=' in x:
			x2 = x.replace('&youtube_pl=',"")
			#url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults=40&pageToken='
			url = 'https://www.googleapis.com/youtube/v3/playlists?id='+x2+'&key='+api_youtube_featherence+'&part=snippet&maxResults=1&pageToken='
			
		elif '&youtube_id=' in x:
			x2 = x.replace('&youtube_id=',"")
			url = 'https://www.googleapis.com/youtube/v3/videos?id='+x2+'&key='+api_youtube_featherence+'&part=snippet'
		elif '&custom_se' in x:
			x2 = x.replace('&custom_se',"")
			x2 = clean_commonsearch(x2)
			url = 'https://www.googleapis.com/youtube/v3/search?q='+x2+'&key='+api_youtube_featherence+'&safeSearch=moderate&type=video&part=snippet&maxResults=1&pageToken='
		elif '&dailymotion_pl=' in x:
			x2 = x.replace('&dailymotion_pl=',"")
			#url = 'https://api.dailymotion.com/playlist/'+x2+'/videos?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&sort=recent&limit=40&family_filter=1&localization=en&page=1'
			url = 'https://api.dailymotion.com/playlist/'+x2
		if url != "":
			printpoint = printpoint + '5'
			link = OPEN_URL(url)
			prms=json.loads(link)
			printlog(title='getAPIdata_test1', printpoint=printpoint, text='url' + space2 + str(url) + newline + 'link' + space2 + str(link) + newline + 'prms' + space2 + str(prms), level=0, option="")
			i = 0
			if '&youtube_pl=' in x:
				id=str(prms['items'][i][u'id']) #Video ID (Playlist)
				#id=str(prms['items'][i][u'snippet'][u'resourceId'][u'videoId']) #Video ID (Playlist)
				#id=str(prms['items'][i][u'snippet'][u'playlistId']) #Video ID (Playlist)
				if id != "":
					#print 'testing' + space2 + str(x2)
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc_ = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					fanart_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					if name_ != "" and not 'Deleted video' in name_: name = name_ # and name == ""
					if iconimage_ != "": iconimage = iconimage_ # and iconimage == ""
					if fanart_ != "": fanart = fanart_ # and fanart == ""
					if desc_ != "": desc = desc_ # and desc == ""
					name = name + space + '[Playlist]'
					
			elif '&youtube_ch=' in x:
				id=str(prms['items'][i][u'id']) #Video ID (Playlist)
				#id=str(prms['items'][i][u'snippet'][u'playlistId']) #Video ID (Playlist)
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc_ = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					fanart_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					if name_ != "" and not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
					if fanart_ != "": fanart = fanart_
					if desc_ != "": desc = desc_
					#name = name + space + '[Channel]'
					
			elif '&youtube_id=' in x:
				id=str(prms['items'][i][u'id']) #Video ID ()
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					fanart_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
					if fanart_ != "": fanart = fanart_
					name = name + space + '[Video]'
					
			elif '&youtube_se=' in x:
				id=str(prms['items'][i][u'id'][u'videoId']) #Video ID (Search)
				if id != "":
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc_ = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					fanart_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					if name_ != "" and not 'Deleted video' in name_ and name == "": name = name_
					if iconimage_ != "" and iconimage == "": iconimage = iconimage_
					if fanart_ != "" and fanart == "": fanart = fanart_
					if desc_ != "" and desc == "": desc = desc_
					name = name + space + '[Search]'
					
			elif '&youtube_se2=' in x:
				id=str(prms['items'][i][u'snippet'][u'channelId']) #Video ID (Search)
				if id != "":
					finalurl=""
					name_=str(prms['items'][i][u'snippet'][u'title'].encode('utf-8'))
					iconimage_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'medium'][u'url'])
					desc = str(prms['items'][i][u'snippet'][u'description'].encode('utf-8')) #.decode('utf-8')
					fanart_=str(prms['items'][i][u'snippet'][u'thumbnails'][u'high'][u'url'])
					if not 'Deleted video' in name_: name = name_
					if iconimage_ != "": iconimage = iconimage_
					if fanart_ != "": fanart = fanart_
		
			elif '&dailymotion_pl=' in x:
				#id=str(prms['items'][i][u'id']) #Video ID (Playlist)
				id = str(prms[u'id'])
				#id=str(prms['items'][i][u'snippet'][u'playlistId']) #Video ID (Playlist)
				if id != "":
					#print 'testing' + space2 + str(x2)
					finalurl="plugin://plugin.video.youtube/play/?video_id="+id+"&hd=1"
					#name_ = str(prms[u'title'])
					name_ = str(prms[u'name'])
					try: iconimage_ = str(prms[u'thumbnail_large_url'])
					except Exception, TypeError: pass
					try: desc_ = str(prms[u'description']).encode('utf-8')
					except Exception, TypeError: pass
					fanart_ = ""
					if name_ != "" and not 'Deleted video' in name_ and name == "": name = name_
					if iconimage_ != "" and iconimage == "": iconimage = iconimage_
					if fanart_ != "" and fanart == "": fanart = fanart_
					if desc_ != "" and desc == "": desc = desc_
					name = name + space + '[Playlist]'
					

		else:
			printpoint = printpoint + '9'	
			if 'getAPIdata' in x and not '&' in x: notification('Missing "&" in getAPIdata','','',1000)
			elif not '&' in x: extra = extra + newline + 'Missing "&" in getAPIdata'
				
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	
	text = 'x' + space2 + str(x) + newline + \
	'id' + space2 + str(id) + newline + \
	'url' + space2 + str(url) + newline + \
	'prms' + space2 + str(prms) + newline + \
	'finalurl' + space2 + str(finalurl) + newline + \
	'name' + space2 + str(name) + newline + \
	'iconimage' + space2 + str(iconimage) + newline + \
	'desc' + space2 + str(desc) + extra
	
	printlog(title="getAPIdata", printpoint=printpoint, text=text, level=0, option="")
	return str(finalurl), str(id), str(name), str(iconimage), str(desc), str(fanart)