# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, os, sys, subprocess, random

from variables import *
from shared_modules import *

def mode0(admin, name, printpoint):
	'''test'''
	for i in range(90,120):
		i_ = xbmc.getInfoLabel('Skin.String(label'+str(i)+')')
		if i_ != "" and i_ != None:
			setSkinSetting('0','id'+str(i),"")
			setSkinSetting('0','label'+str(i),"")
			setSkinSetting('0','action'+str(i),"")
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','icon'+str(i),"")
			setSkinSetting('0','background'+str(i),"")
			setSkinSetting('1','off'+str(i),"")
			setSkinSetting('1','pwd'+str(i),"")
			setSkinSetting('1','sub'+str(i),"")
			setSkinSetting('0','sw'+str(i),"")
			setSkinSetting('0','sw'+str(i)+'_name',"")
	#xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/play/?video_id=WFwHq6cY040)')
	if 1 + 1 == 3:
		finalurl = 'plugin://plugin.video.youtube/play/?video_id=WFwHq6cY040'
		pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO) ; pl.add(finalurl)
		playlist = [] ; playlist.append(finalurl)
		xbmc.Player().play(pl)

def mode4(value, value2, value3, name, printpoint):
	'''Action'''
	xbmc.executebuiltin('ActivateWindow(1170)')
		
def mode5(value, admin, name, printpoint):
	'''startup'''
	setProperty('TEMP', 'startup', type="home")
	
	addon = 'plugin.video.featherence.docu'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'): setsetting_custom1(addon, 'Addon_UpdateLog', "true")
		
	addon = 'plugin.video.featherence.kids'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'): setsetting_custom1(addon, 'Addon_UpdateLog', "true")

	addon = 'plugin.video.featherence.gopro'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'): setsetting_custom1(addon, 'Addon_UpdateLog', "true")

	addon = 'plugin.video.featherence.music'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'): setsetting_custom1(addon, 'Addon_UpdateLog', "true")
	
	addon = 'plugin.program.featherence.emu'
	if xbmc.getCondVisibility('System.HasAddon('+addon+')'): setsetting_custom1(addon, 'Addon_UpdateLog', "true")
	
	skin = 'skin.featherence'
	if xbmc.getSkinDir() == skin and xbmc.getCondVisibility('System.HasAddon('+skin+')'):
		try:
			VolumeLevel = int(xbmc.getInfoLabel('Skin.String(VolumeLevel)'))
			xbmc.executebuiltin('SetVolume('+str(VolumeLevel)+')')
		except: pass
		mode11(name, printpoint) #StartUp-Music/Video
		#mode12()
		mode215('_','','','')
		setsetting_custom1('script.featherence.service','Skin_UpdateLog',"true")
		Skin_UpdateLog = 'true'
		xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=23&value=)') #Widget
		if systembuildversion < 17:
			installaddonP('resource.images.weathericons.outline', update=False)
			installaddonP('resource.images.weatherfanart.single', update=False)
			installaddonP('resource.uisounds.featherence')
			installaddonP('script.module.unidecode', update=False)
			installaddonP('script.skinshortcuts')
		xbmc.sleep(2000) ; setSkin_Update(admin, datenowS, Skin_Version, Skin_UpdateDate, Skin_UpdateLog)
	
	setProperty('TEMP', '', type="home")
	
def mode6(value):
	name = 'mode6 (pwd)' ; printpoint = ""
	passprotect = xbmc.getInfoLabel('Skin.String(PassProtect)')
	passprotectduration = xbmc.getInfoLabel('Skin.String(PassProtectDuration)')
	passprotect_property = xbmc.getInfoLabel('Window(home).Property(PassProtect)')
	currentpwd = xbmc.getCondVisibility('Skin.HasSetting('+value+')')
	containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
	customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
	set1v = ""
	#label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
	
	if currentpwd or value == 'PassProtectAddon':
		printpoint = printpoint + '1'
		if passprotect_property != "":
			printpoint = printpoint + '2'
			
		elif not passprotect:
			'''This button is locked but you haven't set a password!'''
			printpoint = printpoint + '3'
			notification(addonString(32147).encode('utf-8'),"","",4000)
			setProperty('PassProtect','','home')
			xbmc.executebuiltin('ReplaceWindow(Home.xml)')
		else:
			if value == 'PassProtectAddon':
				printpoint = printpoint + 'z'
				passprotectaddon1 = xbmc.getInfoLabel('Skin.String(PassProtectAddon1)')
				passprotectaddon2 = xbmc.getInfoLabel('Skin.String(PassProtectAddon2)')
				passprotectaddon3 = xbmc.getInfoLabel('Skin.String(PassProtectAddon3)')
				passprotectaddon4 = xbmc.getInfoLabel('Skin.String(PassProtectAddon4)')
				passprotectaddon5 = xbmc.getInfoLabel('Skin.String(PassProtectAddon5)')
				passprotectaddon6 = xbmc.getInfoLabel('Skin.String(PassProtectAddon6)')
				passprotectaddon7 = xbmc.getInfoLabel('Skin.String(PassProtectAddon7)')
				passprotectaddon8 = xbmc.getInfoLabel('Skin.String(PassProtectAddon8)')
				passprotectaddon9 = xbmc.getInfoLabel('Skin.String(PassProtectAddon9)')
				passprotectaddon10 = xbmc.getInfoLabel('Skin.String(PassProtectAddon10)')
				passprotectaddonL = [passprotectaddon1, passprotectaddon2, passprotectaddon3, passprotectaddon4, passprotectaddon5, passprotectaddon6, passprotectaddon7, passprotectaddon8, passprotectaddon9, passprotectaddon10]
				containerfolderpath = xbmc.getInfoLabel('Container.FolderPath') ; containerfolderpath2 = containerfolderpath
				while 'addons://' in containerfolderpath and containerfolderpath2 == containerfolderpath and not xbmc.abortRequested:
					xbmc.sleep(2000) ; containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
				
				for z in passprotectaddonL:
					if z in containerfolderpath and z != "" and '.' in z and containerfolderpath != "":
						printpoint = printpoint + 'y'
						break
			if 'z' in printpoint and not 'y' in printpoint: pass
			else:
				printpoint = printpoint + '4'
				returned, set1v = dialognumeric(0,localize(12326),"",'1','','') ; xbmc.sleep(500)
				if set1v != passprotect:
					printpoint = printpoint + '5'
					notification(localize(12342),"","",1000)
					setProperty('PassProtect','','home')
					xbmc.executebuiltin('ReplaceWindow(Home.xml)')
				else:
					x = ""
					try:
						passprotectduration = int(passprotectduration)
						passprotectduration = str(passprotectduration)
					except:
						passprotectduration = '15'
						
					if passprotectduration == '0': pass
					else:
						printpoint = printpoint + 'B'
						xbmc.executebuiltin('AlarmClock(PassProtect,ClearProperty(PassProtect,home),'+passprotectduration+',silent)')
						x = addonString(32155).encode('utf-8') % (str(passprotectduration)) #Relocking is schedule in %s minutes
					
					notification(addonString(32154).encode('utf-8'),x,"",4000) #That's the right password :)
					setProperty('PassProtect','true', 'home')
					if value == 'PassProtect':
						printpoint = printpoint + 'A'
					
	else:
		printpoint = printpoint + '9'
	
	passprotect_property_ = xbmc.getInfoLabel('Window(home).Property(PassProtect)')
	text = 'value' + space2 + str(value) + newline + \
	'set1v' + space2 + str(set1v) + newline + \
	'passprotect' + space2 + str(passprotect) + newline + \
	'passprotect_property' + space2 + str(passprotect_property) + newline + \
	'passprotect_property_' + space2 + str(passprotect_property_) + newline + \
	'containerfolderpath' + space2 + str(containerfolderpath) + newline + \
	'currentpwd' + space2 + str(currentpwd) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def mode8(admin, name, printpoint):
	'''------------------------------
	---SMART-SUBTITLE-SEARCH---------
	------------------------------'''
	setPlayerInfo()
	input = xbmc.getInfoLabel('Window(home).Property(VideoPlayer.Title)')
	if input == "":
		input = xbmc.getInfoLabel('VideoPlayer.Title')
	if input != "":
		xbmc.executebuiltin('SendClick(160)')
		dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		count = 0
		while count < 20 and not dialogkeyboard and not xbmc.abortRequested:
			count += 1
			xbmc.sleep(100)
			dialogkeyboard = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
			
		if count < 20: xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.SendText","id":976575931,"params":{"text":"'+ input +'","done":false}}')
	else: notification('...','','',1000)

def mode9(admin, name):
	'''------------------------------
	---SEMI-AUTO-SUBTITLE-FIND-------
	------------------------------'''
	admin = xbmc.getCondVisibility('Skin.HasSetting(Admin)') ; timeout = False
	property_subtitleservice = xbmc.getInfoLabel('Window(home).Property(Subtitle_Service)')
	property_dialogsubtitles = xbmc.getInfoLabel('Window(home).Property(DialogSubtitles)')
	property_dialogsubtitles2 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitles2)')
	property_dialogsubtitlesna1 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA1)')
	property_dialogsubtitlesna2 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA2)')
	property_dialogsubtitlesna3 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA3)')
	property_dialogsubtitlesna4 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA4)')
	property_dialogsubtitlesna5 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA5)')
	property_dialogsubtitlesna6 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA6)')
	property_dialogsubtitlesna7 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA7)')
	property_dialogsubtitlesna8 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA8)')
	property_dialogsubtitlesna9 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA9)')
	property_dialogsubtitlesna10 = xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA10)')
	subL = [property_dialogsubtitles2, property_dialogsubtitlesna1, property_dialogsubtitlesna2, property_dialogsubtitlesna3, property_dialogsubtitlesna4, property_dialogsubtitlesna5, property_dialogsubtitlesna6, property_dialogsubtitlesna7, property_dialogsubtitlesna8, property_dialogsubtitlesna9, property_dialogsubtitlesna10]
	listL = []
	for i in range(0,10):
		x = xbmc.getInfoLabel('Container(150).ListItemAbsolute('+str(i)+').label')
		if x == "": break
		else: listL.append(x)
	#dialogok(str(listL),'','','')
	#listL = ['Subscenter.org', 'Ktuvit.com', 'OpenSubtitles.org', 'Torec', 'Quasar']
	dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
	controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)')
	controlhasfocus120 = xbmc.getCondVisibility('Control.HasFocus(120)') #MAIN
	controlhasfocus150 = xbmc.getCondVisibility('Control.HasFocus(150)') #SIDE
	controlhasfocus151 = xbmc.getCondVisibility('Control.HasFocus(151)') #SIDE
	controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
	controlgroup70hasfocus = xbmc.getCondVisibility('ControlGroup(70).HasFocus()') #OSD BUTTONS
	controlgroup70hasfocus0 = xbmc.getCondVisibility('ControlGroup(70).HasFocus(0)') #OSD BUTTONS
	container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
	container120numitems = 0
	container120numitems2 = container120numitems
	systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
	playerpaused = xbmc.getCondVisibility('Player.Paused')
	subject = ""
	refresh = 'true'
	tip = "true"
	count = 0
	count2 = 0 #container120numitems
	countidle = 0
	
	REFRESH_TIME = 15
	SWITCH_TIME = 30
	END_TIME = 100
	
	if xbmc.getSkinDir() != 'skin.featherence': listL = []
	'''---------------------------'''
	while countidle < END_TIME and dialogsubtitlesW and listL != [] and not xbmc.abortRequested:
		'''------------------------------
		---VARIABLES---------------------
		------------------------------'''
		dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
		if dialogsubtitlesW:
			container120numitems = xbmc.getInfoLabel('Container(120).NumItems') #DialogSubtitles
			try: container120numitems = int(container120numitems)
			except: container120numitems = ""
			'''---------------------------'''
			controlhasfocus120 = xbmc.getCondVisibility('Control.HasFocus(120)') #MAIN
			controlhasfocus150 = xbmc.getCondVisibility('Control.HasFocus(150)') #SIDE
			controlhasfocus151 = xbmc.getCondVisibility('Control.HasFocus(151)') #SIDE
			controlgetlabel100 = xbmc.getInfoLabel('Control.GetLabel(100)') #DialogSubtitles Service Name
			controlgroup70hasfocus = xbmc.getCondVisibility('ControlGroup(70).HasFocus()') #OSD BUTTONS
			controlgroup70hasfocus0 = xbmc.getCondVisibility('ControlGroup(70).HasFocus(0)') #OSD BUTTONS
			'''---------------------------'''
			systemcurrentcontrol = xbmc.getInfoLabel('System.CurrentControl')
			container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
			'''---------------------------'''
			
		property_dialogsubtitles = xbmc.getInfoLabel('Window(home).Property(DialogSubtitles)')
		dialogkeyboardW = xbmc.getCondVisibility('Window.IsVisible(DialogKeyboard.xml)')
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		'''---------------------------'''
		systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
		systemidle3 = xbmc.getCondVisibility('System.IdleTime(3)')
		systemidle7 = xbmc.getCondVisibility('System.IdleTime(7)')
		systemidle40 = xbmc.getCondVisibility('System.IdleTime(40)')
		'''---------------------------'''
		
		if controlhasfocus120 and container120numitems > 0 and count2 != 0:
			count2 = 0
			subject = ""
			#setProperty('TEMP','', 'home')
		
		if not dialogkeyboardW and container120numitems != "" and controlgetlabel100 != "":
			if count == 0 and property_subtitleservice != "" and property_subtitleservice != controlgetlabel100 and controlgetlabel100 != "":
				'''------------------------------
				---Last_SubService---------------
				------------------------------'''
				subject = 'Choosing Last Subtitle Service'
				#setProperty('TEMP',to_utf8(subject), 'home')
				if controlhasfocus120: xbmc.executebuiltin('Action(Left)')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",property_subtitleservice,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",property_subtitleservice,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",property_subtitleservice,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",property_subtitleservice,40,'Action(Down)','')
				systemcurrentcontrol = findin_systemcurrentcontrol("0",property_subtitleservice,100,'Action(Down)','Action(Select)')
				'''---------------------------'''
					
			elif controlhasfocus120 and container120numitems > 0:
				if (container120listitemlabel2 in subL or container120listitemlabel2 == property_dialogsubtitles2):
					if container120numitems2 != container120numitems and count < 3:
						'''------------------------------
						---Last_SubService---------------
						------------------------------'''
						count3 = 0
						while count3 < 5 and systemidle1 and not xbmc.abortRequested:
							count3 += 1
							container120listitemlabel2 = xbmc.getInfoLabel('Container(120).ListItem.Label2')
							systemidle1 = xbmc.getCondVisibility('System.IdleTime(1)')
							if (container120listitemlabel2 in subL or container120listitemlabel2 == property_dialogsubtitles2): xbmc.executebuiltin('Action(Down)')
							xbmc.sleep(100)
							'''---------------------------'''
							
					elif tip == "true" and countidle == 3:
						if container120listitemlabel2 == property_dialogsubtitles2:
							notification('$LOCALIZE[31858]',property_dialogsubtitles2,"",3000)
						elif container120listitemlabel2 in subL:
							notification('$LOCALIZE[31859]',property_dialogsubtitles2,"",3000)
						
						tip = "false"
						'''---------------------------'''
				elif xbmc.getInfoLabel('Window(home).Property(DialogSubtitles2)') == "":
					subject = 'Choose subtitle'
				
			elif (controlhasfocus150) and container120numitems == 0:
				
				if systemidle1: count2 += 1
				if admin: notification('1',str(countidle) + '/' + str(count) + '/' + str(count2),'',4000)
				
				if ((countidle >= 1 or count <= 3) and count2 == 1) or subject == 'User interrupting...' and countidle >= 3 or subject == "":
					'''------------------------------
					---LOOKING-FOR-SUBTITLE----------
					------------------------------'''
					#notification('$LOCALIZE[31862]',"","",4000)
					subject = localize(31862)
					#setProperty('TEMP',to_utf8(subject), 'home')
					'''---------------------------'''
				
				elif not countidle >= 3 and count2 > REFRESH_TIME and refresh == 'true':
					subject = 'User interrupting...'
					count2 -= 1
					
				elif countidle > 3 and count2 >= REFRESH_TIME and refresh == 'true':
					'''------------------------------
					---REFRESH-----------------------
					------------------------------'''
					refresh = 'false'
					#notification('$LOCALIZE[31861]',"","",2000)
					subject = localize(31861)
					#setProperty('TEMP',to_utf8(subject), 'home')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,40,'Action(Down)','')
					systemcurrentcontrol = findin_systemcurrentcontrol("0",controlgetlabel100,100,'Action(Down)','Action(Select)')
					'''---------------------------'''
					
				elif (countidle > 5 or refresh != 'true') and count2 >= SWITCH_TIME and controlgetlabel100 != "":
					if controlgetlabel100 in listL: listL.remove(controlgetlabel100)
					if listL != []:
						'''------------------------------
						---CHANGE-SUBTITLE-SERVICE-------
						------------------------------'''
						refresh = 'true'
						#notification('$LOCALIZE[31860]',"","",2000)
						subject = localize(31860)
						#setProperty('TEMP',to_utf8(subject), 'home')
						
						systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,40,'Action(Down)','')
						systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,100,'Action(Down)','')
						systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,200,'Action(Down)','')
						systemcurrentcontrol = findin_systemcurrentcontrol("2",listL,300,'Action(Down)','Action(Select)')
						
						count2 = 0
						'''---------------------------'''
					else:
						'''------------------------------
						---NO-SUBTITLES-FOUND!-----------
						------------------------------'''
						subject = 'No subtitles found..'
						#setProperty('TEMP',to_utf8(subject), 'home')
						'''---------------------------'''
			elif (controlgroup70hasfocus) and container120numitems == 0:
				subject = 'Searching paused..'
				#setProperty('TEMP',to_utf8(subject), 'home')
			elif (controlhasfocus151) and container120numitems == 0:
				subject = 'Searching paused..'
				count2 = 0
			else:
				pass
				
		dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
		if dialogsubtitlesW:
			if subject == 'User interrupting...': setProperty('TEMP',to_utf8(subject) + space + str(countidle) + '/3', 'home', force=False)
			elif container120numitems > 0: setProperty('TEMP',to_utf8(subject), 'home', force=False)
			elif count2 > REFRESH_TIME: setProperty('TEMP',to_utf8(subject) + space + str(count2) + '/' + str(SWITCH_TIME), 'home', force=False)
			else: setProperty('TEMP',to_utf8(subject) + space + str(count2) + '/' + str(REFRESH_TIME), 'home', force=False)
			xbmc.sleep(1000)
			'''---------------------------'''
			count += 1
			if systemidle1: countidle += 1
			else:
				countidle = 0
			'''---------------------------'''
	
	if countidle >= 70 or listL == []: timeout = True
	if xbmc.getCondVisibility('System.IdleTime(1)') and not xbmc.getCondVisibility('System.IdleTime(7)') and container120numitems != 0 and not timeout:
		'''------------------------------
		---SET-NEW-SUBTITLE--------------
		------------------------------'''
		setProperty('TEMP', localize(24110), type="home")
		property_dialogsubtitles = xbmc.getInfoLabel('Window(home).Property(DialogSubtitles)')
		if property_dialogsubtitles != "": setSubHisotry(admin, property_dialogsubtitles, property_dialogsubtitles2, property_dialogsubtitlesna1, property_dialogsubtitlesna2, property_dialogsubtitlesna3, property_dialogsubtitlesna4, property_dialogsubtitlesna5, property_dialogsubtitlesna6, property_dialogsubtitlesna7, property_dialogsubtitlesna8, property_dialogsubtitlesna9, property_dialogsubtitlesna10, subL)
		if property_subtitleservice != controlgetlabel100 and controlgetlabel100 != "": setProperty('Subtitle_Service', controlgetlabel100, type="home")
		'''---------------------------'''
		
	#if dialogsubtitlesW: xbmc.executebuiltin('Dialog.Close(subtitlesearch)')
	setProperty('DialogSubtitles', "", type="home")
	if listL != []: setProperty('TEMP', "", type="home")
	
	if xbmc.getCondVisibility('Player.Paused') and not timeout: xbmc.executebuiltin('Action(Play)')
	'''---------------------------'''
	
	setProperty('DialogSubtitles',"",type="home")
	'''------------------------------
	---PRINT-END---------------------
	------------------------------'''
	text = "count/2" + space2 + str(count) + space4 + str(count2) + space + "countidle" + space2 + str(countidle) + space + "controlgetlabel100" + space2 + str(controlgetlabel100) + space + "controlhasfocus120" + space2 + str(controlhasfocus120) + space + "controlhasfocus150" + space2 + str(controlhasfocus150) + space + "container120numitems/2" + space2 + str(container120numitems) + space4 + str(container120numitems2) + newline + "listL" + space2 + str(listL) + space + "systemcurrentcontrol" + space2 + str(systemcurrentcontrol) + space + space + "container120listitemlabel2" + space2 + str(container120listitemlabel2) + space + "subL" + space2 + str(subL) + space + "playerpaused" + space2 + str(playerpaused)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def setSubHisotry(admin, property_dialogsubtitles, property_dialogsubtitles2, property_dialogsubtitlesna1, property_dialogsubtitlesna2, property_dialogsubtitlesna3, property_dialogsubtitlesna4, property_dialogsubtitlesna5, property_dialogsubtitlesna6, property_dialogsubtitlesna7, property_dialogsubtitlesna8, property_dialogsubtitlesna9, property_dialogsubtitlesna10, subL):
	if property_dialogsubtitles != "" and not property_dialogsubtitles in subL:
		for i in range(1,11):
			if xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA'+str(i)+')') == "":
				setProperty('DialogSubtitlesNA' +str(i), property_dialogsubtitles, type="home")
				break
	
	xbmc.sleep(1000)
	setCurrent_Subtitle(admin, property_dialogsubtitles, property_dialogsubtitles2, property_dialogsubtitlesna1, property_dialogsubtitlesna2, property_dialogsubtitlesna3, property_dialogsubtitlesna4, property_dialogsubtitlesna5, property_dialogsubtitlesna6, property_dialogsubtitlesna7, property_dialogsubtitlesna8, property_dialogsubtitlesna9, property_dialogsubtitlesna10, subL)
	'''---------------------------'''
	
def setCurrent_Subtitle(admin, property_dialogsubtitles, property_dialogsubtitles2, property_dialogsubtitlesna1, property_dialogsubtitlesna2, property_dialogsubtitlesna3, property_dialogsubtitlesna4, property_dialogsubtitlesna5, property_dialogsubtitlesna6, property_dialogsubtitlesna7, property_dialogsubtitlesna8, property_dialogsubtitlesna9, property_dialogsubtitlesna10, subL):
	setProperty('DialogSubtitles2', property_dialogsubtitles, type="home")
	'''---------------------------'''

def ClearSubHisotry():
	setProperty('DialogSubtitles',"",type="home")
	setProperty('DialogSubtitles2',"",type="home")
	for i in range(1,11):
		setProperty('DialogSubtitlesNA'+str(i),"",type="home")
			
def setPlayerInfo():
	name = 'setPlayerInfo' ; printpoint = ""
	
	type = None
	playertitle = xbmc.getInfoLabel('Player.Title')
	videoplayercontentEPISODE = xbmc.getCondVisibility('VideoPlayer.Content(episodes)')
	videoplayercontentMOVIE = xbmc.getCondVisibility('VideoPlayer.Content(movies)')
	videoplayercountry = xbmc.getInfoLabel('VideoPlayer.Country')
	videoplayerseason = xbmc.getInfoLabel('VideoPlayer.Season')
	videoplayerepisode = xbmc.getInfoLabel('VideoPlayer.Episode')
	videoplayertagline = xbmc.getInfoLabel('VideoPlayer.Tagline')
	videoplayertitle = xbmc.getInfoLabel('VideoPlayer.Title')
	videoplayertvshowtitle = xbmc.getInfoLabel('VideoPlayer.TVShowTitle')
	playertitle = xbmc.getInfoLabel('Player.Title')
	playerfilename = xbmc.getInfoLabel('Player.Filename')
	videoplayeryear = xbmc.getInfoLabel('VideoPlayer.Year')
	
	if (videoplayertvshowtitle != "" and videoplayerseason != "" and videoplayerepisode != "" and videoplayertagline == ""): type = 1
	elif (videoplayertitle != "" and (videoplayeryear != "" or videoplayercountry != "" or videoplayertagline != "")): type = 0
	elif videoplayercontentEPISODE: type = 1
	elif videoplayercontentMOVIE: type = 0
	else: type = 2 ; printpoint = printpoint + '2'
	
	if type != "":
		printpoint = printpoint + '3'
		if type == 0:
			printpoint = printpoint + '4'
			input = str(videoplayertitle) + space + str(videoplayeryear)
		elif type == 1:
			printpoint = printpoint + '5'
			try: seasonN = int(videoplayerseason)
			except: seasonN = ""
			try: episodeN = int(videoplayerepisode)
			except: episodeN = ""
			if seasonN == "" or episodeN == "" or videoplayertvshowtitle == "": input = videoplayertitle
			elif seasonN < 10 and episodeN < 10: input = videoplayertvshowtitle + " " + 'S0' + videoplayerseason + 'E0' + videoplayerepisode
			elif seasonN > 10 and episodeN > 10: input = videoplayertvshowtitle + " " + 'S' + videoplayerseason + 'E' + videoplayerepisode
			elif seasonN > 10 and episodeN < 10: input = videoplayertvshowtitle + " " + 'S' + videoplayerseason + 'E0' + videoplayerepisode
			elif seasonN < 10 and episodeN > 10: input = videoplayertvshowtitle + " " + 'S0' + videoplayerseason + 'E' + videoplayerepisode
			else: input = playertitle
			'''---------------------------'''
		else: input = playertitle
		
		printpoint = printpoint + '7'
		setProperty('VideoPlayer.Title', str(input), type="home")
	
	
	text = 'input' + space2 + str(to_utf8(input)) + space + 'type' + space2 + str(type) + newline + \
	'playertitle' + space2 + str(to_utf8(playertitle)) + newline + \
	'videoplayercontentEPISODE' + space2 + str(to_utf8(videoplayercontentEPISODE)) + newline + \
	'videoplayercontentMOVIE' + space2 + str(to_utf8(videoplayercontentMOVIE)) + newline + \
	'videoplayercountry' + space2 + str(to_utf8(videoplayercountry)) + newline + \
	'videoplayerseason' + space2 + str(to_utf8(videoplayerseason)) + newline + \
	'videoplayerepisode' + space2 + str(to_utf8(videoplayerepisode)) + newline + \
	'videoplayertagline' + space2 + str(to_utf8(videoplayertagline)) + newline + \
	'videoplayertitle' + space2 + str(to_utf8(videoplayertitle)) + newline + \
	'videoplayertvshowtitle' + space2 + str(to_utf8(videoplayertvshowtitle)) + newline + \
	'playertitle' + space2 + str(to_utf8(playertitle)) + newline + \
	'videoplayeryear' + space2 + str(to_utf8(videoplayeryear)) + newline + \
	'playerfilename' + space2 + str(to_utf8(playerfilename))
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def videostarttweak(admin):
	playercache = xbmc.getInfoLabel('Player.CacheLevel')
	playerpaused = xbmc.getCondVisibility('Player.Paused')
	count = 0
	try:
		while count < 10 and int(playercache) < 90 and not xbmc.abortRequested:
			if count == 0 and not playerpaused:
				xbmc.executebuiltin('Action(Pause)')
				notification('Cache Tweak','...','',2000)
			count += 1
			playercache = xbmc.getInfoLabel('Player.CacheLevel')
			playerpaused = xbmc.getCondVisibility('Player.Paused')
			xbmc.sleep(500)

		if count > 0 and count < 10:
			playerpaused = xbmc.getCondVisibility('Player.Paused')
			if playerpaused: xbmc.executebuiltin('Action(Play)')
	except: pass
	
def mode10(admin, name, printpoint):
	'''------------------------------
	---VideoPlayer demon-------------
	------------------------------'''
	xbmc.sleep(3000)
	if property_mode10 == "":
		setProperty('mode10', 'true', type="home")
		playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
		playerhasaudio = xbmc.getCondVisibility('Player.HasAudio')
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy)')
		dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress)')
		setPlayerInfo()
		videostarttweak(admin)
		ii = 0
		if playerhasvideo and xbmc.getCondVisibility('Window.IsVisible(DialogFullScreenInfo.xml)'): xbmc.executebuiltin('Action(Info)')
		while (playerhasvideo or playerhasaudio or dialogbusyW or dialogprogressW or ii < 2) and not xbmc.abortRequested:
			xbmc.sleep(5000)
			videoplayertweak(admin, playerhasvideo)
			playerhasvideo = xbmc.getCondVisibility('Player.HasVideo')
			playerhasaudio = xbmc.getCondVisibility('Player.HasAudio')
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy)')
			dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress)')
			if xbmc.abortRequested:
				ii = 9
			elif not (playerhasvideo and not playerhasaudio and not dialogbusyW and not dialogprogressW):
				ii += 1
			elif ii > 0: ii -= 1
			'''---------------------------'''
		
		ClearSubHisotry()
		setProperty('mode10', "", type="home")
		setProperty('VideoPlayer.Title', "", type="home")
		if '5' in printpoint:
			'''refresh widget'''
			xbmc.sleep(3000)
			xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=23)')
		
		text = 'ii' + space2 + str(ii) + newline
		printlog(title=name, printpoint=printpoint, text=text, level=2, option="")


def mode11(name, printpoint):
	'''StartUp-Music/Video'''
	startupmusic1 = xbmc.getCondVisibility('Skin.HasSetting(StartUpMusic)')
	startupvideofullscreen1 = xbmc.getCondVisibility('Skin.HasSetting(StartUpVideoFullScreen)')
	startupvideo0 = xbmc.getInfoLabel('Skin.String(StartUpVideo)')
	startupmusic0 = xbmc.getInfoLabel('Skin.String(StartUpMusic)')
	IntroDelay = xbmc.getInfoLabel('Skin.String(IntroDelay)')
	
	if IntroDelay == "" or IntroDelay == '-':
		IntroDelay = 1
	else:
		try:
			IntroDelay = int(IntroDelay)
		except:
			IntroDelay = 1
	
	xsleep = int(IntroDelay) * 1000
	xbmc.sleep(xsleep)
	if startupvideo0 == "": pass
	else:
		startupvideo0_, startupvideo0__ = TranslatePath(startupvideo0, filename=True)
		if not os.path.exists(startupvideo0_):
			printpoint = printpoint + '1'
			notification('Startup Video failed','File is not available!','',2000)
		else: 
			xbmc.executebuiltin('CancelAlarm(startup,silent)')
			printpoint = printpoint + '2'
			if not startupvideofullscreen1: xbmc.executebuiltin('PlayMedia('+startupvideo0_+')')
			else: xbmc.executebuiltin('PlayMedia('+to_utf8(startupvideo0_)+'),1)')
			xbmc.sleep(1000)
	if not startupmusic1:
		printpoint = printpoint + '3'
		count = 0
		if xbmc.getCondVisibility('Player.HasVideo'):
			printpoint = printpoint + '4'
			while xbmc.getCondVisibility('Player.HasVideo') and count < 20 and not xbmc.abortRequested:
				xbmc.sleep(1000)
				count += 1
		
		if count >= 20: printpoint = printpoint + '5'
		else:
			printpoint = printpoint + '6'
			if not startupmusic0: xbmc.executebuiltin('PlayMedia(special://skin/sounds/featherence.mp3)') ; printpoint = printpoint + '7'
			else:
				printpoint = printpoint + '8'
				startupmusic0_, startupmusic0__ = TranslatePath(startupmusic0, filename=True)
				if not os.path.exists(startupmusic0_): notification('Startup Music failed','File is not available!','',2000)
				elif os.path.isfile(startupmusic0_): xbmc.executebuiltin('PlayMedia('+to_utf8(startupmusic0_)+')')
				elif os.path.isdir(startupmusic0_):	CreatePL(startupmusic0_, 'music')
				else: printpoint = printpoint + '9'
				#xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=21&amp;value='+ to_utf8(startupmusic0_) +'&amp;value2=music)')
	
	text = 'startupmusic1' + space2 + str(to_utf8(startupmusic1)) + newline + \
	'startupmusic1' + space2 + str(to_utf8(startupmusic1)) + newline + \
	'startupvideofullscreen1' + space2 + str(to_utf8(startupvideofullscreen1)) + newline + \
	'startupvideo0' + space2 + str(to_utf8(startupvideo0)) + newline + \
	'startupmusic0' + space2 + str(to_utf8(startupmusic0)) + newline + \
	'IntroDelay' + space2 + str(IntroDelay)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def mode12():
	name = 'mode12' ; printpoint = ''
	path = 'special://skin/extras/featherence_.mp4'
	x_, x__ = TranslatePath(path, filename=True)
	videoplayertitle = ""
	count = 0
	if os.path.exists(x_):
		printpoint = printpoint + '1'
		xbmc.executebuiltin('PlayMedia('+ x_ +')')
		while not xbmc.getCondVisibility('Player.HasVideo') and count < 20 and not xbmc.abortRequested:
			xbmc.sleep(100)
			if count == 0: printpoint = printpoint + '2'
			count += 1
		if xbmc.getCondVisibility('Player.HasVideo'):
			printpoint = printpoint + '3'
			videoplayertitle = xbmc.getInfoLabel('VideoPlayer.Title')
			setProperty('script.featherence.service_Info', 'true', type="home")
			xbmc.sleep(5000)
			#ReloadSkin(admin,force=False)
			
	text = 'path' + space2 + str(to_utf8(path)) + newline + \
	'count' + space2 + str(count) + newline + \
	'videoplayertitle' + space2 + str(videoplayertitle)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def mode13(value, name, printpoint):
	'''skinsettings 20-100'''
	Custom1000(title="Please Wait", progress="90", comment=str(value), autoclose="3")
	if value != "":
		skinsetting = value
		skinsetting_ = xbmc.getInfoLabel('Skin.String('+ skinsetting +')')
		if skinsetting != "":
			if skinsetting_ == "": setSkinSetting('0', skinsetting, '100')
			elif skinsetting_ == "100": setSkinSetting('0', skinsetting, '95')
			elif skinsetting_ == "95": setSkinSetting('0', skinsetting, '90')
			elif skinsetting_ == "90": setSkinSetting('0', skinsetting, '85')
			elif skinsetting_ == "85": setSkinSetting('0', skinsetting, '80')
			elif skinsetting_ == "80": setSkinSetting('0', skinsetting, '70')
			elif skinsetting_ == "70": setSkinSetting('0', skinsetting, '60')
			elif skinsetting_ == "60": setSkinSetting('0', skinsetting, '50')
			elif skinsetting_ == "50": setSkinSetting('0', skinsetting, '40')
			elif skinsetting_ == "40": setSkinSetting('0', skinsetting, '30')
			elif skinsetting_ == "30": setSkinSetting('0', skinsetting, '20')
			elif skinsetting_ == "20": setSkinSetting('0', skinsetting, )
			else: setSkinSetting('0', skinsetting, )
	
	xbmc.sleep(1000)
	mode32(value='6')
			
def mode22(header, message, nolabel, yeslabel, skinstring, type='video'):
	skinstring_ = xbmc.getInfoLabel('Skin.String('+skinstring+')')
	returned = dialogyesno(header, message, nolabel=nolabel, yeslabel=yeslabel)
	if returned == 'ok': z = 0
	else: z = 1
	returned = setPath(z,type) ; xbmc.sleep(200)
	notification(returned,skinstring,'',4000)
	if returned != "":
		if returned != skinstring_: setSkinSetting('0',skinstring,returned)
		else:
			returned2 = dialogyesno('Remove Current Path?',skinstring)
			if returned2 == 'ok': setSkinSetting('0',skinstring,"")
			'''---------------------------'''
			
def CheckExtensions(x, mask='video'):
	name = 'CheckExtensions' ; printpoint = "" ; returned = ""
	if mask =='video': list = ['mp4', 'mov', 'avi']
	elif mask =='picture': list = []
	elif mask =='music': list = ['mp3', 'flac', 'wav', 'm3u']
	else: list = []
	
	extension = os.path.splitext(x)[1][1:].strip().lower()
	if extension in list:
		returned = 'ok'
	
	text = 'mask' + space2 + str(to_utf8(mask)) + newline + \
	'x' + space2 + str(to_utf8(x)) + newline + \
	'list' + space2 + str(to_utf8(list)) + newline + \
	'extension' + space2 + str(to_utf8(extension)) + newline + \
	'returned' + space2 + str(to_utf8(returned))
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
	return returned

def CreatePL2(x, type, playlist, level, levelmax):
	name = 'CreatePL2' ; printpoint = "" ; x2 = ""
	if os.path.isdir(x):
		for x2 in os.listdir(x):
			x2 = to_utf8(x2)
			x2 = os.path.join(x, x2)
			if os.path.isdir(x2) and level <= levelmax:
				playlist = CreatePL2(x + x2, type, playlist, level + 1, levelmax)
			else:
				returned = CheckExtensions(x2, type)
				if returned == 'ok': playlist.append(x2)
	else:
		returned = CheckExtensions(x, type)
		if returned == 'ok': playlist.append(x)
	
	text = 'level' + space2 + str(to_utf8(level)) + space + 'levelmax' + space2 + str(to_utf8(levelmax)) + newline + \
	'x' + space2 + str(to_utf8(x)) + newline + \
	'x2' + space2 + str(to_utf8(x2)) + newline + \
	'playlist' + space2 + str(to_utf8(playlist))
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
	return playlist
	
def CreatePL(path, type='video', levelmax=10):
	name = 'CreatePL' ; printpoint = "" ; extra = "" ; notexistsL= []
	if type == 'music': pl = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
	else: pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	playlist = []
	if path == "": printpoint = printpoint + '9'
	if not '9' in printpoint:
		for x in os.listdir(path):
			x = os.path.join(path, x)
			x_, x__ = TranslatePath(x, filename=True)
			#x = to_utf8(x)
			if os.path.exists(x_):
				playlist = CreatePL2(x_, type, playlist, 0, levelmax)
			else: notexistsL.append(x_)
		
	if playlist != []:
		random.shuffle(playlist)
		for x in playlist:
			pl.add(x)
			extra = extra + newline + 'x' + space2 + str(to_utf8(x))
		#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)
		xbmc.Player().play(pl)
	
	text = 'type' + space2 + str(to_utf8(type)) + newline + \
	'path' + space2 + str(to_utf8(path)) + newline + \
	'pl' + space2 + str(to_utf8(pl)) + newline + \
	'playlist' + space2 + str(to_utf8(playlist)) + newline + \
	'notexistsL' + space2 + str(to_utf8(notexistsL)) + extra
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
		
def mode25(value, admin, name, printpoint):
	'''------------------------------
	---Play-Random-Trailers----------
	------------------------------'''
	
	pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	pl.clear()
	playlist = []
	for i in range(1,11):
		value_trailer = xbmc.getInfoLabel('Window(home).Property(RecentMovie.'+str(i)+'.Trailer)')
		value_trailer2 = xbmc.getInfoLabel('Window(home).Property(RandomMovie.'+str(i)+'.Trailer)')
		if value_trailer != "": playlist.append(value_trailer)
		if value_trailer2 != "": playlist.append(value_trailer2)
		'''---------------------------'''
	if playlist != []:
		random.shuffle(playlist)
		for x in playlist:
			pl.add(x)
		xbmc.Player().play(pl)
		#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(pl)

def mode28(value, value2, value3, name, printpoint):
	'''------------------------------
	---AutoView----------------------
	------------------------------'''
	extra = "" ; TypeError = "" ; value2 = "" ; returned = ""
	list = ['-> (Exit)', 'None', 'Default', localize(31010), localize(31011)] #Center List, Side List
	if (value == 'AutoView.episodes' or value == 'AutoView.seasons') and value != 'Force_all': list.append(localize(31012)) #Small List
	list.append(localize(31013)) #Wall
	list.append(localize(31014)) #Poster
	list.append(localize(31015)) #List
	list.append(localize(31016)) #Small Wall

	returned, value2 = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)

	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		if value2 == 'None': setSkinSetting('0', str(value), "None")
		elif value2 == 'Default': setSkinSetting('0', str(value), "")
		elif value2 != "": setSkinSetting('0', str(value), value2)
		else: printpoint = printpoint + "8"
		'''---------------------------'''

def mode29(value, command, header, exit, name, printpoint):
	'''------------------------------
	---Dialog-Select-Skin------------
	------------------------------
	value = list ; output = Skin.String/Setting ; header='''
	extra = "" ; TypeError = "" ; returned2 = "" ; returned = "" ; commandL = [] ; list = [] ; list2 = []
	
	if command == "":
		printpoint = printpoint + '9'
		notification_common('3')
		
	commandL = command.split('|')
	
	if header == "":
		header = 'Choose an option from the list'
	
	if exit != '0':
		list.append('-> (Exit)')
		list2.append('-> (Exit)')
	
	valueL = value.split('|')
	for x in valueL:
		#x = to_utf8(x)
		y = find_string(x, '-[', ']-')
		extra = extra + newline + 'y' + space2 + str(y)
		if y != "":
			y_ = x.replace(y, "")
			list.append(y_)
			y__ = y.replace('-[',"",1)
			y__ = y__.replace(']-',"",1)
			list2.append(y__)
		else:	
			list.append(x)
			list2.append(x)

	returned, returned2 = dialogselect(header,list,0)

	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0 and exit != '0': printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		for x in commandL:
			if x[:2] == '0.':
				x_ = x.replace(x[:2],"",1)
				if '_name' in x:
					setSkinSetting('0', x_, list[returned], force=True)
				else:
					setSkinSetting('0', x_, list2[returned], force=True)
			elif x[:2] == '1.':
				setSkinSetting('1', str(returned2), list2[returned], force=True)
			
			elif x[:2] == 's.':
				#mode = find_string(x, '.', '_')
				if 's.32_6' in x:
					xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=32&value=6)')
				
			else:
				#if '#' in x: x.replace('#','&')
				xbmc.executebuiltin(x) ; xbmc.sleep(10)
	
	text2 = newline + 'value' + space2 + str(value) + newline + \
	'list ' + space2 + str(list) + newline + \
	'list2 ' + space2 + str(list2) + newline + \
	'returned' + space2 + str(returned) + space + 'returned2' + space2 + str(returned2) + newline + \
	'command  ' + space2 + str(command) + newline + \
	'commandL ' + space2 + str(commandL) + newline + extra
	printlog(title=name, printpoint=printpoint, text=text2, level=0, option="")
	
def mode30(input, header, option, action, set1, addon, name, printpoint):
	'''------------------------------
	---Dialog-Keyboard-Skin----------
	------------------------------'''
	if action != "":
		'''same time action (pre)'''
		xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=4&amp;value=1&amp;value2='+action+'')
		
		#xbmc.executebuiltin('AlarmClock(mode30,'+action+',00:01,silent)')
	try: option += 1
	except: option = 0
	dialogkeyboard(input, header, option, "", set1=set1, addon=addon, force=True)
	
def mode31(value, value2, value3, value4, admin, name, printpoint):
	'''------------------------------
	---diaogtextviewer---------------
	------------------------------'''
	name = 'diaogtextviewer-mode31' ; printpoint = "" ; TypeError = "" ; extra = ""
	header = "" ; message = ""
	try: header = str(value).encode('utf-8')
	except Exception, TypeError: extra = extra + newline + 'TypeError-header' + space2 + str(TypeError)
	try: message = str(value2).encode('utf-8')
	except Exception, TypeError: extra = extra + newline + 'TypeError-message' + space2 + str(TypeError)

	if value == 'Custom':
		printpoint = printpoint + '1'
		value3 = setPath(type=1,mask="", folderpath="")
		if value3 != "":
			printpoint = printpoint + '2'
			'''get file name only'''
			header = os.path.basename(value3)
	
	if value3 != "" and value3 != None:
		printpoint = printpoint + '3'
		if not os.path.exists(value3) and '.' in value3:
			printpoint = printpoint + '4'
			x = os.path.join(addons_path, value3, 'changelog.txt')
			if os.path.exists(x):
				printpoint = printpoint + '5'
				value3 = x
		value3 = read_from_file(value3, silent=True, lines=False, retry=True, createlist=True, printpoint="", addlines="")
		message = message + newline + str(value3)
	message = message + newline + str(value4).encode('utf-8')
	diaogtextviewer(header, message)

	text = 'value' + space2 + str(value) + newline + \
	'value2' + space2 + str(value2) + newline + \
	'value3' + space2 + str(value3) + newline + \
	'value4' + space2 + str(value4) + newline + extra
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''
	
def mode32(value, value2="", value3="", name="", printpoint=""):
	'''------------------------------
	---MISCS-------------------------
	------------------------------'''
	if value == '0':
		if admin == 'false':
			setsetting('admin','true')
			#setsetting_custom1('script.featherence.service','admin',"true")
			#notification(admin,'','',1000)
			setSkinSetting('1','Admin','true')
		else:
			setsetting('admin','false')
			setSkinSetting('1','Admin','false')
	elif value == '1':
		text = "" ; extra = ""
		listitemfolderpath = xbmc.getInfoLabel('ListItem.FolderPath')
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		listitemlabel = xbmc.getInfoLabel('ListItem.Label')
		listitemplot = xbmc.getInfoLabel('ListItem.Plot')
		listitemthumb = xbmc.getInfoLabel('ListItem.Thumb')
		listitemisfolder = xbmc.getCondVisibility('ListItem.IsFolder')
		
		nolabel = 'Container.FolderPath'
		yeslabel = 'ListItem.Path'
		if containerfolderpath == "": nolabel = nolabel + space + '[Empty]'
		if listitemfolderpath == "": yeslabel = yeslabel + space + '[Empty]'
		
		returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=nolabel, yeslabel=yeslabel)
		
		if returned != 'skip': text = listitemfolderpath ; printpoint = printpoint + '1'
		else: text = containerfolderpath ; printpoint = printpoint + '2'
		
		if text != "":
			printpoint = printpoint + '3'
			text = text.replace('&amp;','&')
			text = text.replace('&quot;',"")
			
			if '1' in printpoint:
				if listitemisfolder: text = "list.append('&custom8=" + text + "')"
				else: text = "list.append('&custom4=" + text + "')"
			elif '2' in printpoint: text = "list.append('&custom8=" + text + "')"
		
		if listitemlabel != "" and listitemlabel != "..":
			text = text + newline + str(listitemlabel)
			
		if listitemthumb != "":
			text = text + newline + str(listitemthumb)
		
		if listitemplot != "":
			text = text + newline + str(listitemplot)
			
		if 'plugin.video.cartoons8' in text:
			if 'description=' in text:
				#y = find_string(text, 'description=', '&')
				#text = text.replace(y,'description=&',1)
				pass
			
		dest = featherenceservice_addondata_path + "Container.FolderPath" + ".txt"
		write_to_file(dest, str(text), append=False, silent=True, utf8=False)
		notification(addonString(32130).encode('utf-8'),dest,'',2000)
		'''---------------------------'''
		
		text2 = newline + 'text' + space2 + str(text) + newline + \
		'containerfolderpath ' + space2 + str(xbmc.getInfoLabel('Container.FolderPath')) + newline + \
		'containerfolderpath2' + space2 + containerfolderpath + newline + \
		'listitemisfolder' + space2 + str(listitemisfolder) + newline + \
		'listitemfolderpath  ' + space2 + str(xbmc.getInfoLabel('ListItem.FolderPath')) + newline + \
		'listitemfolderpath2 ' + space2 + listitemfolderpath + newline + extra
		printlog(title='MISCS (mode32) value: ' + str(value), printpoint=printpoint, text=text2, level=0, option="")
		
	elif value == '2':
		returned, value = getRandom(0, min=0, max=3, percent=50)
		if value == 0:
			returned = dialogyesno('F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e')
		elif value == 1:
			dialogok('F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e')
		else:
			dp = xbmcgui.DialogProgress()
			dp.create('F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e')
			count = 0
			while count < 10 and not dp.iscanceled() and not xbmc.abortRequested:
				count += 1
				xbmc.sleep(500)
				dp.update(count * 10,'F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e','F--e--a--t--h--e--r--e--n--c--e[CR]F--e--a--t--h--e--r--e--n--c--e')
			xbmc.sleep(500)
			dp.close
	
	elif value == '3':
		'''Featherence YouTube channel'''
		xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.youtube/user/finalmakerr/),returned')			
		setSkin_UpdateLog(admin, Skin_Version, Skin_UpdateDate, datenowS, force=True)
	elif value == '4':
		command = '<p mod="ctrl,shift" description="containerfolderpath">RunScript(script.featherence.service,,?mode=32&amp;value=1)</p>'
		command_ = '<p mod="ctrl,shift"'
		command__ = '</p>'
		content = '<keymap>' + newline + '	' + '<global>' + newline + '		' + '<keyboard>' + newline + '			' + command + newline + \
			'		</keyboard>' + newline + \
			'	</global>' + newline + \
			'</keymap>'
		keymaps_path = os.path.join(userdata_path,'keymaps','')
		keyboard_file = os.path.join(keymaps_path,'keyboard.xml')
		
		keyboard_file_ = read_from_file(keyboard_file, silent=True, lines=False, retry=True, createlist=False, printpoint="", addlines="")
		keyboard_file__ = keyboard_file_
		x = regex_from_to(keyboard_file_, '<global>', '</global>', excluding=False)
		y = regex_from_to(x, '<keyboard>', '</keyboard>', excluding=False)
		y_ = regex_from_to(x, '<keyboard>', '</keyboard>', excluding=True)
		z = regex_from_to(x, command_, command__, excluding=False)
		
		if not os.path.exists(keyboard_file):
			printpoint = printpoint + '0'
			write_to_file(keyboard_file, content, append=False, silent=True , utf8=False, eol=True)
			
		elif not command in y:
			printpoint = printpoint + '1'
			if z != "" and z != command_ + command__:
				printpoint = printpoint + '2'
				keyboard_file__ = keyboard_file__.replace(z, command, 1)
			
			elif y_ != "":
				printpoint = printpoint + '3'
				keyboard_file__ = keyboard_file__.replace(y_, y_ + '	' + command + newline + '		', 1)
			
			else:
				printpoint = printpoint + '4'
				dialogok('keyboard.xml exist!', 'Click OK to view the current file','','')
				diaogtextviewer('keyboard.xml', keyboard_file_)
				returned = dialogyesno('Would you like to overwrite your current file?','Click YES to proceed')
				if returned == 'ok':
					printpoint = printpoint + '7'
					write_to_file(keyboard_file, content, append=False, silent=True , utf8=False, eol=True)
				else: printpoint = printpoint + '9'
		
		if '9' in printpoint:
			notification_common("9")
		elif ('0' in printpoint or '1' in printpoint):
			xbmc.executebuiltin('Action(reloadkeymaps)')
			notification('Keymap modified!','Use Ctrl+Shift+P','',4000)
		else:
			notification('Keymap already setup!','Use Ctrl+Shift+P','',4000)
		
		text = 'x' + space2 + str(x) + newline + \
		'y' + space2 + str(y) + newline + \
		'y_' + space2 + str(y_) + newline + \
		'z' + space2 + str(z) + newline
		printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
		
	elif value == '5':
		ReloadSkin(admin,force=False)
		#ReloadSkin(admin)
	elif value == '6':
		custom1170W_ = xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)')
		custom1173W_ = xbmc.getCondVisibility('Window.IsVisible(Custom1173.xml)')
		if custom1170W_: xbmc.executebuiltin('Dialog.Close(1170)')
		elif custom1173W_: xbmc.executebuiltin('Dialog.Close(1173)')
		TEMP = xbmc.getInfoLabel('Window(home).Property(TEMP)')
		
		xbmc.executebuiltin('Action(Close)') ; xbmc.executebuiltin('ActivateWindow(1000)') ; xbmc.sleep(400) ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(200)
		xbmc.executebuiltin('ActivateWindow(1117)') ; xbmc.sleep(300)
		
		
		count = 0
		property_buttonid = xbmc.getInfoLabel('Window(home).Property(Button.ID)') #DYNAMIC
		property_buttonid_ = xbmc.getInfoLabel('Window(home).Property(Button.ID_)') #BASE
		while count < 10 and property_buttonid == "" and property_buttonid_ == "" and not xbmc.abortRequested:
			xbmc.sleep(50)
			property_buttonid = xbmc.getInfoLabel('Window(home).Property(Button.ID)') #DYNAMIC
			property_buttonid_ = xbmc.getInfoLabel('Window(home).Property(Button.ID_)') #BASE
			count += 1
		if 'WindowsBusy' in TEMP:
			xbmc.sleep(500)
			setProperty('TEMP', 'WindowsBusyClose', type="home")
			xbmc.sleep(100)
			setProperty('TEMP', '', type="home")
		if count < 10 or 1 + 1 == 2:
			xbmc.executebuiltin('ActivateWindow(1173)')
			custom1173W = xbmc.getCondVisibility('Window.IsVisible(Custom1173.xml)')
			while count < 20 and not custom1173W and not xbmc.abortRequested:
				xbmc.sleep(50)
				custom1173W = xbmc.getCondVisibility('Window.IsVisible(Custom1173.xml)')
				count += 1
			if custom1173W:
				xbmc.executebuiltin('Action(Down)')
		
		setProperty('TEMP', '', type="home")
	
	elif value == '7':
		xbmc.sleep(500)
		setProperty('DoubleClick', '', type="home")
	
	elif value == '8':
		xbmc.sleep(500)
		xbmc.executebuiltin('ActivateWindow(1170)')
	
	elif value == '9':
		if value2 != "" and value2 != None:
			try:
				xbmc.sleep(int(value3))
			except: xbmc.sleep(500)
			xbmc.executebuiltin('ActivateWindow('+value2+')')
	
	elif value == '10':
		containerfolderpath = xbmc.getInfoLabel('Container.FolderPath')
		addon = find_string(containerfolderpath, 'plugin://', '/')
		addon = addon.replace('plugin://',"",1)
		addon = addon.replace('/',"")
		notification(addon,'','',2000)
		xbmc.executebuiltin('Addon.OpenSettings('+addon+')')
	
	elif value == '11':
		xbmc.executebuiltin('ActivateWindow(1000)') ; xbmc.sleep(200)
		xbmc.executebuiltin('ReplaceWindow(Home.xml)') ; xbmc.sleep(300)
		count = 0 ; homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
		while count < 10 and not homeW and not xbmc.abortRequested():
			count += 1
			homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
			xbmc.sleep(200)
		xbmc.executebuiltin('Control.SetFocus(9000)')
		xbmc.executebuiltin('Control.SetFocus(9090)')
		
	elif value == '40':
		addon = 'plugin.video.featherence.kids'
		if xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
			dialogok(addonString_servicefeatherence(32085).encode('utf-8'),addonString_servicefeatherence(32081).encode('utf-8'),"",addonString_servicefeatherence(32108).encode('utf-8'),line1c="yellow")
			General_Language2 = xbmcaddon.Addon(addon).getSetting('General_Language2') ; General_Language2 = str(General_Language2)
			dialogok(addonString_servicefeatherence(32086).encode('utf-8') % (General_Language2),addonString_servicefeatherence(32087).encode('utf-8'),"",addonString_servicefeatherence(32088).encode('utf-8'),line1c="yellow")
		
def mode33(value, value2, name, printpoint):
	'''------------------------------
	---ADDONS-LOCK-------------------
	------------------------------'''
	extra = "" ; TypeError = "" ; value2 = "" ; returned = ""
	passprotectaddon1 = xbmc.getInfoLabel('Skin.String(PassProtectAddon1)')
	passprotectaddon2 = xbmc.getInfoLabel('Skin.String(PassProtectAddon2)')
	passprotectaddon3 = xbmc.getInfoLabel('Skin.String(PassProtectAddon3)')
	passprotectaddon4 = xbmc.getInfoLabel('Skin.String(PassProtectAddon4)')
	passprotectaddon5 = xbmc.getInfoLabel('Skin.String(PassProtectAddon5)')
	passprotectaddon6 = xbmc.getInfoLabel('Skin.String(PassProtectAddon6)')
	passprotectaddon7 = xbmc.getInfoLabel('Skin.String(PassProtectAddon7)')
	passprotectaddon8 = xbmc.getInfoLabel('Skin.String(PassProtectAddon8)')
	passprotectaddon9 = xbmc.getInfoLabel('Skin.String(PassProtectAddon9)')
	passprotectaddon10 = xbmc.getInfoLabel('Skin.String(PassProtectAddon10)')
	list = ['-> (Exit)']
	
	list.append(to_utf8(passprotectaddon1) + '(1)')
	list.append(to_utf8(passprotectaddon2) + '(2)')
	list.append(to_utf8(passprotectaddon3) + '(3)')
	list.append(to_utf8(passprotectaddon4) + '(4)')
	list.append(to_utf8(passprotectaddon5) + '(5)')
	list.append(to_utf8(passprotectaddon6) + '(6)')
	list.append(to_utf8(passprotectaddon7) + '(7)')
	list.append(to_utf8(passprotectaddon8) + '(8)')
	list.append(to_utf8(passprotectaddon9) + '(9)')
	list.append(to_utf8(passprotectaddon10) + '(10)')

	returned, value2 = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)

	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		if not xbmc.getInfoLabel('Skin.String(PassProtectAddon'+str(returned)+')'):
			heading = localize(24000) + space + 'ID'
			dialogkeyboard("", heading, 0, '1', 'PassProtectAddon'+str(returned), "", force=False)
		else: xbmc.executebuiltin('Skin.SetString(PassProtectAddon'+str(returned)+',)')
		
def mode39(value, name, printpoint):
	'''------------------------------
	---Reset-default-buttons---------
	------------------------------'''
	extra = "" ; TypeError = "" ; value2 = "" ; returned = ""
	list = ['-> (Exit)', 'Labels', 'Icons','Labels&Icons']

	returned, value2 = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)

	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		if returned == 1: mode215('_', 'RESET-LABEL', name, printpoint)
		elif returned == 2: mode215('_', 'RESET-ICON', name, printpoint)
		elif returned == 3: mode215('_', 'RESET', name, printpoint)
		else: printpoint = printpoint + "8"
		'''---------------------------'''
		
def mode40(value, name, printpoint):
	'''------------------------------
	---Reset-Skin-Settings-----------
	------------------------------'''
	extra2 = "" ; TypeError = ""
	if value == '0': printpoint = printpoint + '1'
	elif value == '1':
		returned = dialogyesno(localize(31821) , localize(31822))
		if returned == 'ok': printpoint = printpoint + '1' ; xbmc.executebuiltin('Dialog.Close(1173)')
	
	if printpoint == '1':
		'''------------------------------
		---DELETE-USER-FILES-------------
		------------------------------'''
	
	if printpoint == '1':
		xbmc.executebuiltin('Skin.ResetSettings') ; xbmc.sleep(500)
		Custom1000(name,1,addonString_servicefeatherence(32131).encode('utf-8'),30) #This action may take a while.. be patient!
		playerhasmedia = xbmc.getCondVisibility('Player.HasMedia')
		if playerhasmedia: xbmc.executebuiltin('Action(Stop)')
		
		count = 0

	if printpoint == '1':
		xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=215&value=_&value2=RESET)') ; xbmc.sleep(7000)
		xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(500) ; customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
		if not customhomecustomizerW: xbmc.executebuiltin('ActivateWindow(1171)')
	
	text = ''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
			
def mode41(admin, name, printpoint):
	'''------------------------------
	---Network-Settings--------------
	------------------------------'''
	if systemplatformandroid: pass
	elif systemplatformwindows: pass
	elif systemplatformlinux and xbmc.getCondVisibility('System.HasAddon(service.openelec.settings)'): xbmc.executebuiltin('RunScript(service.openelec.settings)')
	'''---------------------------'''

def mode69(value, admin, name, printpoint):
	'''------------------------------
	---TIPS--------------------------
	------------------------------'''
	if value == 'SubMenu2Tip': SubMenu2Tip(admin)
	else: pass
	'''---------------------------'''

def mode70(value, admin, name, printpoint, property_temp):
	'''------------------------------
	---ExtendedInfo------------------
	------------------------------'''
	listitemlabel = xbmc.getInfoLabel('ListItem.Label')
	listitemdbid = xbmc.getInfoLabel('ListItem.DBID')
	listitemtitle = xbmc.getInfoLabel('ListItem.Title')
	listitemseason = xbmc.getInfoLabel('ListItem.Season')
	listitemdirector = xbmc.getInfoLabel('ListItem.Director')
	listitemyear = xbmc.getInfoLabel('ListItem.Year')
	listitemwriter = xbmc.getInfoLabel('ListItem.Writer')
	listitemtvshowtitle = xbmc.getInfoLabel('ListItem.TVShowTitle')
	
	addon = 'script.extendedinfo' ; input0 = "" ; input = "" ; input2 = "" ; container50listitemlabel2 = "" ; property_temp_ = ""
	if xbmc.getCondVisibility('System.HasAddon('+ addon +')') and os.path.exists(addons_path + addon):
		if value == '0':
			'''movie info'''
			if listitemtitle != "":
				input = 'info=extendedinfo,name=%s' % (listitemtitle)
		elif value == '1':
			if listitemtvshowtitle == "" and listitemlabel != "": listitemtvshowtitle = listitemlabel
			if localize(20373) in listitemlabel and listitemseason != "":
				'''seasoninfo'''
				printpoint = printpoint + "1"
				input = 'info=seasoninfo,tvshow=%s,season=%s' % (listitemtvshowtitle,listitemseason)
			elif listitemtvshowtitle != "":
				'''extendedtvinfo'''
				printpoint = printpoint + "2"
				input = 'info=extendedtvinfo,name=%s' % (listitemtvshowtitle)
				
		elif value == '3':
			if '&actor=' in property_temp:
				'''Actor info'''
				printpoint = printpoint + "1"
				property_temp = property_temp.replace('&actor=',"")
				if localize(20347) in property_temp:
					printpoint = printpoint + "2"
					property_temp_ = find_string(property_temp, property_temp[:1], xbmc.getInfoLabel('$LOCALIZE[20347]'))
					str20347_len = len(localize(20347))
					property_temp_ = property_temp_[:-str20347_len]
					property_temp = property_temp_
				else: pass
				input = 'info=extendedactorinfo,name=%s' % (property_temp)
			elif '&director=' in property_temp:
				printpoint = printpoint + "3"
				property_temp = property_temp.replace('&director=',"")
				input = 'info=extendedactorinfo,name=%s' % (property_temp)
				#input = 'info=directormovies,director=%s' % (property_temp)
				#input = 'info=extendedinfo,director=%s' % (property_temp)
				

		elif value == '5':
			'''Write info'''
			input0 = 'writermovies'
			input2 = 'writer'
			#input = 'info=extendedinfo,writer=%s,writer=%s' % (listitemwriter)
			#input = 'info=writermovies,writer=%s' % (listitemwriter)
			input = 'info=extendedactorinfo,name=%s' % (listitemwriter)
			if listitemwriter != "" and 1 + 1 == 3:
				if ' / ' in listitemwriter and 1 + 1 == 3:
					listitemwriter_ = listitemwriter.split(' / ')
					list = []
					for x in listitemwriter_:
						list.append(x)
					
					if len(list) > 1:
						returned, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
						if returned == -1: printpoint = printpoint + "9"
						else:
							printpoint = printpoint + "7"
							input = 'info=writermovies,writer=%s' % (value)
							input = 'info=extendedinfo,writer=%s' % (value)
							'''---------------------------'''
				else:
					pass
					#input = 'info=writermovies,writer=%s' % (listitemwriter)
					#input = 'info=extendedinfo,writer=%s,writer=%s' % (listitemwriter)
					'''---------------------------'''
		elif value == '10':
			'''Rate Movie/TVshow'''
			input = 'info=ratedialog,name=%s' % (str(listitemlabel))
		elif value == '20':
			#xbmc.executebuiltin('RunScript(script.extendedinfo,info=seasoninfo,tvshow='+listitemtvshowtitle+',season='+listitemseason+')')
			xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedinfo,director='+listitemdirector+')')
			#input0 = 'similartvshowstrakt'
			#input2 = 'id'
			#input = listitemdbid
		
		elif value == '40':
			input0 = 'comingsoon'
			
		else: printpoint = printpoint + '9'
		
		if input != "" and not '9' in printpoint:
			dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
			if dialogselectW:
				xbmc.executebuiltin('dialog.close(selectdialog)') ; xbmc.sleep(500)
			
			xbmc.executebuiltin('RunScript('+addon+','+input+')')
			count = 0 ; dialogvideonfoEW = xbmc.getCondVisibility('Window.IsVisible(script-ExtendedInfo Script-DialogVideoInfo.xml)')
			while count < 10 and not dialogvideonfoEW and not xbmc.abortRequested:
				count += 1
				xbmc.sleep(500)
				dialogvideonfoEW = xbmc.getCondVisibility('Window.IsVisible(script-ExtendedInfo Script-DialogVideoInfo.xml)')
			if count < 10: printpoint = printpoint + "7"
			else: printpoint = printpoint + "Q"
		else:
			printpoint = printpoint + "8"
			notification_common("17")
			'''---------------------------'''
	else:
		printpoint = printpoint + "9"
		installaddon(addon, update=True)
		#installaddonP(addon, update=True)
	
	text = "input" + space2 + input + space + 'value' + space2 + str(value) + newline + \
	"INFO" + space2 + "listitemlabel" + space2 + listitemlabel + newline + "listitemtvshowtitle" + space2 + listitemtvshowtitle + newline + \
	"listitemtitle" + space2 + listitemtitle + newline + "listitemdbid" + space2 + listitemdbid + newline + \
	'listitemseason' + space2 + str(listitemseason) + newline + \
	"containerfolderpath" + space2 + containerfolderpath + newline + "property_temp" + space2 + property_temp + space + "property_temp_" + space2 + str(property_temp_) + newline + \
	"listitemdirector" + space2 + listitemdirector + newline + \
	"listitemwriter" + space2 + listitemwriter
	printlog(title=name, printpoint=printpoint, text=text, level=2, option="")
	'''---------------------------'''
	
def mode200(value, admin, name, printpoint):
	'''------------------------------
	---DIALOG-SELECT-(10-100)--------
	------------------------------'''
	extra = "" ; TypeError = "" ; value2 = "" ; returned = ""
	list = ['-> (Exit)', 'default', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
	
	if value != "":
		try:
			test = xbmc.getInfoLabel('Skin.String('+value+')')
			if test != None: printpoint = printpoint + "1"
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError)
	else: pass
	
	if "1" in printpoint:
		returned, value2 = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
	
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
		if "7" in printpoint:
			if value2 == 'default': setSkinSetting('0', str(value), "")
			elif value2 != "": setSkinSetting('0', str(value), value2)
			else: printpoint = printpoint + "8"
			
			if not "8" in printpoint:
				notification(".","","",1000)
				xbmc.sleep(200)
				xbmc.executebuiltin('Action(Back)')
				xbmc.sleep(200)
				ReloadSkin(admin)
	
	text = "list" + space2 + str(list) + space + "returned" + space2 + str(returned) + space + "value" + space2 + str(value) + space + "value2" + space2 + str(value2) + extra
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def Custom1000(title="", progress="", comment="", autoclose=""):
	libraryisscanningvideo = xbmc.getCondVisibility('Library.IsScanningVideo')
	if libraryisscanningvideo: xbmc.executebuiltin('UpdateLibrary(video)')
	xbmc.executebuiltin('SetProperty(1000title,'+title+',home)')
	xbmc.executebuiltin('SetProperty(1000progress,'+str(progress)+',home)')
	xbmc.executebuiltin('SetProperty(1000comment,'+comment+',home)')
	custom1000W = xbmc.getCondVisibility('Window.IsVisible(Custom1000.xml)')
	xbmc.executebuiltin('Dialog.Close(all,true)')
	if not custom1000W:
		notification_common("2")
		xbmc.executebuiltin('ActivateWindow(1000)') ; xbmc.sleep(100)
	
	if autoclose != "": xbmc.executebuiltin('AlarmClock(timeout,Action(Back),'+str(autoclose)+',silent)')
	
	
	text = 'title' + space2 + str(title)
	printlog(title='Custom1000', printpoint=printpoint, text=text, level=0, option="")
	
def getRandomColors(admin):	
	returned, value1 = getRandom("0", min=0, max=70, percent=50)
	returned, value2 = getRandom("0", min=0, max=70, percent=50)
	returned, value3 = getRandom("0", min=0, max=70, percent=50)
	returned, value4 = getRandom("0", min=0, max=70, percent=50)
	returned, value5 = getRandom("0", min=0, max=70, percent=50)
	listL = [value1, value2, value3, value4, value5]
	count = 0
	for value in listL:
		count += 1
		if value > 0 and value <= 5: value = '' ; value_ = ""
		elif value > 5 and value <= 10: value = 'ff000000' ; value_ = 'black'
		elif value > 10 and value <= 15: value = 'ff00a693' ; value_ = 'persian green'
		elif value > 15 and value <= 20: value = 'ff00cccc' ; value_ = 'robin egg blue'
		elif value > 20 and value <= 25: value = 'ffffc40c' ; value_ = 'mikado yellow'
		elif value > 25 and value <= 30: value = 'ff00ffff' ; value_ = 'aqua'
		elif value > 30 and value <= 35: value = 'ff1e4d2b' ; value_ = 'cal poly pomona green'
		elif value > 35 and value <= 40: value = 'ff2f4f4f' ; value_ = 'dark slate gray'
		elif value > 40 and value <= 45: value = 'ff4cbb17' ; value_ = 'kelly green'
		elif value > 45 and value <= 50: value = 'ff5d8aa8' ; value_ = 'air force blue'
		elif value > 50 and value <= 55: value = 'ff8b4513' ; value_ = 'saddle brown'
		elif value > 55 and value <= 60: value = 'ff89cff0' ; value_ = 'baby blue'
		elif value > 60 and value <= 65: value = 'fff5f5f5' ; value_ = 'white smoke'
		elif value > 65 and value <= 70: value = 'ffffd1dc' ; value_ = 'pastel pink'
		
		if count == 1: value1 = value ; value1_ = value_
		elif count == 2: value2 = value ; value2_ = value_
		elif count == 3: value3 = value ; value3_ = value_
		elif count == 4: value4 = value ; value4_ = value_
		elif count == 5: value5 = value ; value5_ = value_
	
	return value1, value1_, value2, value2_, value3, value3_, value4, value4_, value5, value5_
			
def mode201(value, admin, name, printpoint):
	'''------------------------------
	---RESET-TO-DEFAULT--------------
	------------------------------'''
	#from variables2 import *
	returned = "" ; extra = ""
	container50hasfocus390 = xbmc.getCondVisibility('Container(50).HasFocus(390)') #BUTTONS

	list = ['-> (Exit)', \
	localize(10035) + "-" + localize(593), \
	localize(590) + "-" + localize(593), \
	localize(31827) + "-" + localize(31420), \
	localize(31531) + "-" + localize(31420), \
	localize(31827) + "-" + localize(593), \
	localize(590) + "-" + localize(593), \
	localize(31827) + space + localize(31849) + "-" + localize(593), \
	localize(590) + space + localize(31849) + "-" + localize(593), \
	localize(10035) + space + localize(31825)]
	
	if value == "" or container50hasfocus390:
		returned, value_ = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
		
		if returned == -1: printpoint = printpoint + "9"
		elif returned == 0: printpoint = printpoint + "8"
		else: printpoint = printpoint + "7"
		
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		if (returned == 1 or value == "1"): printpoint = printpoint + "ACEG" #RESET-ALL
		elif returned == 2: printpoint = printpoint + "BDFH" #RANDOM-ALL
		elif returned == 3: printpoint = printpoint + "C" #RESET-BUTTONS-COLORS
		elif returned == 4: printpoint = printpoint + "D" #RANDOM-BUTTONS-COLORS
		elif returned == 5: printpoint = printpoint + "CE" #RESET COLORS-ALL
		elif returned == 6: printpoint = printpoint + "DF" #RANDOM COLORS-ALL
		elif returned == 7: printpoint = printpoint + "G" #RESET-TRANSPERANCY-ALL
		elif returned == 8: printpoint = printpoint + "H" #RANDOM TRANSPERANCY-ALL
		elif (returned == 9 or value == "9"): returned = 9 ; printpoint = printpoint + "I" #RESET BUTTONS PROPERTIES
		
		from variables2 import labelT, list1, list0, list0c, list0c2, list0o, list0l, list1l
		Custom1000(name,0,str(list[returned]),20)
		'''---------------------------'''
	if "A" in printpoint:
		Custom1000(name,20,str(list[returned]),20)
		xbmc.executebuiltin('SetProperty(1000title,'+name+',home)')
		xbmc.executebuiltin('SetProperty(1000comment,'+addonString_servicefeatherence(32131).encode('utf-8')+',home)')
		for x in list0: setSkinSetting('0',x,"")
		for x in list1: setSkinSetting('1',x,"false")
		'''---------------------------'''
	
	if "B" in printpoint:
		Custom1000(name,30,str(list[returned]),20)
		for x in list1:
			returned1, value1 = getRandom("0", min=0, max=100, percent=50)
			if returned1 == 'ok': value1 = "true"
			else: value1 = "false"
			setSkinSetting('1',x,value1)
		
	if "C" in printpoint:
		Custom1000(name,40,str(list[returned]),20)
		'''RESET-BUTTONS-COLORS'''
		for i in range(17,22):
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','color'+str(i)+'.name',"")
			'''---------------------------'''
		for i in range(90,120):
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','color'+str(i)+'.name',"")
			'''---------------------------'''
	
	if "D" in printpoint:
		Custom1000(name,50,str(list[returned]),20)
		value1, value1_, value2, value2_, value3, value3_, value4, value4_, value5, value5_ = getRandomColors(admin)
		for i in range(17,22):
			x = labelT.get('label'+str(i))
			if x != "":
				returnedx, count = getRandom("0", min=1, max=5, percent=50)
				if count == 1: value = value1 ; value_ = value1_
				elif count == 2: value = value2 ; value_ = value2_
				elif count == 3: value = value3 ; value_ = value3_
				elif count == 4: value = value4 ; value_ = value4_
				elif count == 5: value = value5 ; value_ = value5_
				setSkinSetting('0','color'+str(i),value)
				setSkinSetting('0','color'+str(i)+'.name',value_)
				'''---------------------------'''
		for i in range(90,120):
			x = labelT.get('label'+str(i))
			if x != "":
				returnedx, count = getRandom("0", min=1, max=5, percent=50)
				if count == 1: value = value1 ; value_ = value1_
				elif count == 2: value = value2 ; value_ = value2_
				elif count == 3: value = value3 ; value_ = value3_
				elif count == 4: value = value4 ; value_ = value4_
				elif count == 5: value = value5 ; value_ = value5_
				setSkinSetting('0','color'+str(i),value)
				setSkinSetting('0','color'+str(i)+'.name',value_)
				'''---------------------------'''
	
	if "E" in printpoint:
		Custom1000(name,60,str(list[returned]),15)
		'''RESET-ALL-COLORS'''
		for x in list0c: setSkinSetting('0',x,"")
		for x in list0c: setSkinSetting('0',x,"")
		'''---------------------------'''
		
	if "F" in printpoint:
		Custom1000(name,70,str(list[returned]),15)
		value1, value1_, value2, value2_, value3, value3_, value4, value4_, value5, value5_ = getRandomColors(admin)
		'''RANDOM-ALL-COLORS'''
		returnedx, count = getRandom("0", min=1, max=5, percent=50)
		for x in list0c:
			if count == 1: value = value1 ; value_ = value1_
			elif count == 2: value = value2 ; value_ = value2_
			elif count == 3: value = value3 ; value_ = value3_
			elif count == 4: value = value4 ; value_ = value4_
			elif count == 5: value = value5 ; value_ = value5_
			setSkinSetting('0',x,value)
			setSkinSetting('0',x+'.name',value_)
			'''---------------------------'''
		
	if "G" in printpoint:
		Custom1000(name,90,str(list[returned]),10)
		'''RESET-ALL-TRANSPERANCY'''
		for x in list0o: setSkinSetting('0',x,"")
		'''---------------------------'''
		
	if "H" in printpoint:
		Custom1000(name,90,str(list[returned]),10)
		'''RANDOM-ALL-TRANSPERANCY'''
		returnedx, value1 = getRandom("0", min=0, max=55, percent=50)
		returnedx, value2 = getRandom("0", min=0, max=55, percent=50)
		returnedx, value3 = getRandom("0", min=0, max=55, percent=50)
		returnedx, value4 = getRandom("0", min=0, max=55, percent=50)
		returnedx, value5 = getRandom("0", min=0, max=55, percent=50)
		listL = [value1, value2, value3, value4, value5]
		count = 0
		for value in listL:
			count += 1
			if value > 0 and value <= 5: value = ''
			elif value > 5 and value <= 10: value = ''
			elif value > 10 and value <= 15: value = '20'
			elif value > 15 and value <= 20: value = '30'
			elif value > 20 and value <= 25: value = '40'
			elif value > 25 and value <= 30: value = '50'
			elif value > 30 and value <= 35: value = '60'
			elif value > 35 and value <= 40: value = '70'
			elif value > 40 and value <= 45: value = '80'
			elif value > 45 and value <= 50: value = '90'
			elif value > 50 and value <= 55: value = '100'
			
			if count == 1: value1 = str(value)
			elif count == 2: value2 = str(value)
			elif count == 3: value3 = str(value)
			elif count == 4: value4 = str(value)
			elif count == 5: value5 = str(value)
			'''---------------------------'''
		
		for x in list0o:
			returnedx, count = getRandom("0", min=1, max=5, percent=50)
			if count == 1: y = str(value1)
			elif count == 2: y = str(value2)
			elif count == 3: y = str(value3)
			elif count == 4: y = str(value4)
			elif count == 5: y = str(value5)
			setSkinSetting('0',x,y)
			'''---------------------------'''
	
	if "I" in printpoint:
		Custom1000(name,20,str(list[returned]),10)
		'''RESET BUTTONS PROPERTIES'''
		count = 0
		for i in range(17,22):
			setSkinSetting('0','label'+str(i),"")
			setSkinSetting('0','color'+str(i),"")
			setSkinSetting('0','icon'+str(i),"")
			setSkinSetting('0','background'+str(i),"")
			setSkinSetting('1','off'+str(i),"")
			setSkinSetting('1','pwd'+str(i),"")
			setSkinSetting('1','sub'+str(i),"")
			setSkinSetting('0','sw'+str(i),"")
			setSkinSetting('0','sw'+str(i)+'_name',"")
			
			for i2 in range(100,110):
				'''subs'''
				i2_ = xbmc.getInfoLabel('Skin.String(label'+str(i)+'_'+str(i2)+')')
				if i2_ != "" and i != None:
					#setSkinSetting('0','id'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','label'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','action'+str(i)+'_'+str(i2),"")
					setSkinSetting('1','off'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','icon'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','background'+str(i)+'_'+str(i2),"")
					'''---------------------------'''
			for i2 in range(100,110):
				'''widgets'''
				i2_ = xbmc.getInfoLabel('Skin.String(labelw'+str(i)+'_'+str(i2)+')')
				if i2_ != "" and i != None:
					#setSkinSetting('0','id'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','labelw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','actionw'+str(i)+'_'+str(i2),"")
					setSkinSetting('1','offw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','iconw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','backgroundw'+str(i)+'_'+str(i2),"")
					'''---------------------------'''
		for i in range(90,120):
			count += 2
			i_ = xbmc.getInfoLabel('Skin.String(label'+str(i)+')')
			if i_ != "" and i_ != None:
				setSkinSetting('0','id'+str(i),"")
				setSkinSetting('0','label'+str(i),"")
				setSkinSetting('0','action'+str(i),"")
				setSkinSetting('0','color'+str(i),"")
				setSkinSetting('0','icon'+str(i),"")
				setSkinSetting('0','background'+str(i),"")
				setSkinSetting('1','off'+str(i),"")
				setSkinSetting('1','pwd'+str(i),"")
				setSkinSetting('1','sub'+str(i),"")
				setSkinSetting('0','sw'+str(i),"")
				setSkinSetting('0','sw'+str(i)+'_name',"")
				extra = extra + str(i) + '|'
				'''---------------------------'''
			for i2 in range(100,110):
				'''subs'''
				i2_ = xbmc.getInfoLabel('Skin.String(label'+str(i)+'_'+str(i2)+')')
				if i2_ != "" and i_ != None:
					#setSkinSetting('0','id'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','label'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','action'+str(i)+'_'+str(i2),"")
					setSkinSetting('1','off'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','icon'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','background'+str(i)+'_'+str(i2),"")
					'''---------------------------'''
			for i2 in range(100,110):
				'''widgets'''
				i2_ = xbmc.getInfoLabel('Skin.String(labelw'+str(i)+'_'+str(i2)+')')
				if i2_ != "" and i_ != None:
					#setSkinSetting('0','id'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','labelw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','actionw'+str(i)+'_'+str(i2),"")
					setSkinSetting('1','offw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','iconw'+str(i)+'_'+str(i2),"")
					setSkinSetting('0','backgroundw'+str(i)+'_'+str(i2),"")
					'''---------------------------'''
		
		for y in list1l:
			setSkinSetting('1',y,"")
			'''---------------------------'''
		
		for y in list0l:
			setSkinSetting('0',y,"")
			'''---------------------------'''
			
	if ("7" in printpoint or value != "") and not "8" in printpoint and not "9" in printpoint:
		if value != "9":
			Custom1000(name,90,str(list[returned]),3)
			notification(".","","",1000)
			ReloadSkin(admin)
			Custom1000(name,100,str(list[returned]),1) ; xbmc.sleep(1500)
			xbmc.executebuiltin('ActivateWindow(1117)') ; xbmc.sleep(2000) ; xbmc.executebuiltin('ActivateWindow(1173)')
		
	text = "list" + space2 + str(list) + newline + \
	"returned" + space2 + str(returned) + newline + 'extra: ' + str(extra)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def mode202(value, admin, name, printpoint):
	'''------------------------------
	---CHOOSE-COLORS-2---------------
	------------------------------'''
		
	#x = xbmc.getInfoLabel('Container(9003).ListItem(0).Label')
	#x2 = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(colorID)')
	#y = xbmc.getInfoLabel('Container(9003).ListItemNoWrap(0).Property(color)')
	#listitempropertycolor = xbmc.getInfoLabel('ListItem.Property(color)')
	
	if property_temp != "":
		if value == "30110":
			'''DEFAULT COLOR'''
			printpoint = printpoint + "2"
			setSkinSetting('0', property_temp, "")
			setSkinSetting('0', property_temp + '.name', "")
			notification("...","","",1000)
			xbmc.executebuiltin('Dialog.Close(1175)')
			if custom1173W: xbmc.executebuiltin('Dialog.Close(1173)')
			xbmc.executebuiltin('Dialog.Close(1117)')
			xbmc.executebuiltin('Action(Close)')
			xbmc.executebuiltin('ActivateWindow(1117)')
			if custom1173W: xbmc.executebuiltin('ActivateWindow(1173)')
			'''---------------------------'''
		else: printpoint = printpoint + "9"
		
	else: printpoint = printpoint + "9"
	xbmc.executebuiltin('ClearProperty(TEMP,home)')
	text = "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + newline + \
	'property_temp' + space2 + str(property_temp)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	'''---------------------------'''

def mode210(value, admin, name, printpoint):
	'''------------------------------
	---MOVE-ITEM---------------------
	------------------------------'''
	extra = "" ; extra2 = "" ; TypeError = "" ; x = "" ; y = "" ; y2 = ""
	
	xbmc.executebuiltin('Action(Close)')
	'''---------------------------'''
	if not int(property_buttonid) > 0 or not int(property_buttonid_) > 0: printpoint = printpoint + "9A"
	if '0' in value:
		printpoint = printpoint + "0"
		if property_temp == property_buttonid or property_temp2 == property_buttonid_: printpoint = printpoint + "9B"
		if property_temp2 == "": printpoint = printpoint + "9C"
		if property_temp == 'None' or property_temp2 == 'None': printpoint = printpoint + "9F"
		else:
			try:
				if not int(property_temp2) > 0: printpoint = printpoint + "9D"
			except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9E"

	if not '9' in printpoint:
		notification_common("2")
		from variables2 import *
		if '0' in value:
			for i in range(0,2):
				x = "" ; y = "" ; y2 = ""
				extra = extra + "i" + space2 + str(i)
				if i == 0:
					'''property_buttonid -> property_temp'''
					x = property_temp2
					x2 = property_temp
					y = property_buttonid_
					y2 = property_buttonid
					'''---------------------------'''
				elif i == 1:
					'''property_temp -> property_buttonid'''
					x = property_buttonid_
					x2 = property_buttonid_
					y = property_temp2
					y2 = property_temp
					'''---------------------------'''
				else: pass	
				if x != "" and y != "":
					'''continue'''
					notification("...", str(labelT.get('label'+x)) + ' -> ' + str(labelT.get('label'+y)), "", 1000)
					setSkinSetting('0','id'+x,str(idT.get('id'+y)))
					setSkinSetting('0','label'+x,str(labelT.get('label'+y)))
					setSkinSetting('0','action'+x,str(actionT.get('action'+y)))
					setSkinSetting('1','off'+x,str(offT.get('off'+y)))
					setSkinSetting('1','pwd'+x,str(pwdT.get('pwd'+y)))
					setSkinSetting('0','color'+x,str(colorT.get('color'+y)))
					setSkinSetting('0','icon'+x,str(iconT.get('icon'+y)))
					#setSkinSetting('0','background'+y,str(backgroundT.get('background'+x)))
					setSkinSetting('1','sub'+x,str(subT.get('sub'+y)))
					'''---------------------------'''
				else: notification("Error","","",2000) ; printpoint = printpoint + "8"
		elif '1' in value or '2' in value:
			for i in range(0,2):
				x = "" ; y = ""
				if i == 0:
					if '1' in value:
						'''property_subbuttonid_ -> property_previoussubbuttonid_'''
						x = property_previoussubbuttonid_
						y = property_subbuttonid_
						'''---------------------------'''
					elif '2' in value:
						'''property_subbuttonid_ -> property_nextsubbuttonid_'''
						x = property_nextsubbuttonid_
						y = property_subbuttonid_
						'''---------------------------'''
					
				elif i == 1:
					'''property_previoussubbuttonid_ -> property_subbuttonid_'''
					if '1' in value:
						'''property_previoussubbuttonid_ -> property_subbuttonid_'''
						x = property_subbuttonid_
						y = property_previoussubbuttonid_
						'''---------------------------'''
					elif '2' in value:
						'''property_nextsubbuttonid_ -> property_subbuttonid_'''
						x = property_subbuttonid_
						y = property_nextsubbuttonid_
						'''---------------------------'''
					
				else: pass
				
				if x != "" and y != "":
					'''continue'''
					label_ = xbmc.getInfoLabel('$VAR['+label_T.get('label'+y)+']')
					notification("...", "", "", 1000)
					setSkinSetting('1','off'+x,str(off_T.get('off'+y)))
					setSkinSetting('1','pwd'+x,str(pwdT.get('pwd'+y)))
					setSkinSetting('0','label'+x,label_T.get('label'+y))
					setSkinSetting('0','action'+x,str(action_T.get('action'+y)))
					setSkinSetting('0','icon'+x,str(icon_T.get('icon'+y)))
					setSkinSetting('0','background'+x,str(backgroundT.get('background'+y)))
					
					#extra = extra + newline + label_T.get('label'+y)	
					#extra = extra + newline + 'label_' + space2 + label_
					#extra = extra + newline + action_T.get('action'+y)
					#extra = extra + newline + icon_T.get('icon'+y)
				else: printpoint = printpoint + "9" ; break
				
				extra2 = extra2 + newline + "i" + space2 + str(i) + space + "x" + space2 + str(x) + space + "y" + space2 + str(y) + space + "y2" + space2 + str(y2) + space
		elif '3' in value:
			for i in range(0,2):
				x = "" ; y = "" ; y2 = ""
				extra = extra + "i" + space2 + str(i)
				if i == 0:
					'''property_buttonid -> property_temp'''
					x = property_temp2
					x2 = property_temp
					y = property_widgetbuttonid_
					y2 = property_widgetbuttonid_
					'''---------------------------'''
				elif i == 1:
					'''property_temp -> property_buttonid'''
					x = property_widgetbuttonid_
					x2 = property_widgetbuttonid_
					y = property_temp2
					y2 = property_temp
					'''---------------------------'''
				else: pass	
				if x != "" and y != "":
					'''continue'''
					notification("...", str(labelw_T.get('label'+x)) + ' -> ' + str(labelw_T.get('label'+y)), "", 1000)
					#setSkinSetting('0','id'+x,str(idT.get('id'+y)))
					setSkinSetting('0','label'+x,str(labelw_T.get('label'+y)))
					setSkinSetting('0','action'+x,str(actionw_T.get('action'+y)))
					setSkinSetting('1','off'+x,str(offw_T.get('off'+y)))
					setSkinSetting('0','icon'+x,str(iconw_T.get('icon'+y)))
					#setSkinSetting('0','background'+y,str(backgroundT.get('background'+x)))
					'''---------------------------'''
				else: notification("Error","","",2000) ; printpoint = printpoint + "8"

	#dp.close
	if "9" in printpoint: notification(localize(257) + space2 + '209', '', '', 2000)
	else:
		pass
		#ReloadSkin(admin)
		xbmc.sleep(500) ; xbmc.executebuiltin('Action(Down)') ; xbmc.sleep(500) ; xbmc.executebuiltin('Action(Up)')
	
	text = "value" + space2 + str(value) + newline + \
	"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + newline + \
	"property_temp" + space2 + str(property_temp) + space + "property_temp2" + space2 + str(property_temp2) + newline + \
	"property_subbuttonid_" + space2 + str(property_subbuttonid_) + newline + \
	"property_previoussubbuttonid_" + space2 + str(property_previoussubbuttonid_) + newline + \
	"property_nextsubbuttonid_" + space2 + str(property_nextsubbuttonid_) + newline + \
	"property_widgetbuttonid_" + space2 + str(property_widgetbuttonid_) + newline + \
	"property_widgetbuttonid" + space2 + str(property_widgetbuttonid) + newline + \
	extra + extra2
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def mode211(value, admin, name, printpoint):
	'''------------------------------
	---Create-New-Item---------------
	------------------------------'''
	extra = "" ; TypeError = "" ; x = "" ; y = "" ; max = 109
	
	if not xbmc.getCondVisibility('Skin.HasSetting(Performance)'): max = 119
	try:
		if not int(property_buttonid_) > 0: printpoint = printpoint + "1" ; notification(localize(257) + space2 + '211', "", "", 1000)
	except: printpoint = printpoint + 'q'
	
	if not '1' in printpoint and not 'q' in printpoint:
		'''Get new control ID'''
		if '0' in value:
			'''main menu item'''
			#from variables2 import *
			#label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			xbmc.executebuiltin('Dialog.Close(1175)')
			for i in range(100,max):
				x = xbmc.getInfoLabel('Skin.String(label'+str(i)+')')
				if x == "":
					y = str(i)
					setSkinSetting('0','label'+y,"...")
					setSkinSetting('1','off'+y,"false")
					setSkinSetting('1','pwd'+y,"false")
					break
				else: pass
		
		elif '1' in value:
			'''sub menu item'''
			#xbmc.executebuiltin('Dialog.Close(1138)')
			for i in range(100,109):
				x = xbmc.getInfoLabel('Skin.String(label'+property_buttonid+'_'+str(i)+')')
				if x == "":
					y = property_buttonid+'_'+str(i)
					#setSkinSetting('0','id'+y,y)
					setSkinSetting('0','label'+y,"...")
					setSkinSetting('1','off'+y,"false")
					setSkinSetting('1','pwd'+y,"false")
					break
				else: pass

					
		if y == "": printpoint = printpoint + "9" ; notification(addonString_servicefeatherence(32132).encode('utf-8'),addonString_servicefeatherence(32133).encode('utf-8'),"",2000) #Cannot create new buttons, Delete some first!
		else:
			notification("...", "", "", 1000)
			mode232(y, admin, 'ACTION-BUTTON', printpoint)
			'''---------------------------'''
				
	text = "value" + space2 + str(value) + newline + \
	"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + newline + \
	"property_temp" + space2 + str(property_temp) + space + "property_temp2" + space2 + str(property_temp2) + newline + \
	"x" + space2 + str(x) + newline + \
	"y" + space2 + str(y) + newline + \
	extra
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def mode212(value, admin, name, printpoint):
	'''------------------------------
	---REMOVE-ITEM-------------------
	------------------------------'''
	extra = "" ; extra2 = "" ; TypeError = "" ; x = "" ; two = 1 ; property_buttonname2 = ""

	try:
		if property_buttonid == "": printpoint = printpoint + "9A"
		else: test = int(property_buttonid_) + 1
		if '0' in value:
			if int(property_buttonid) < 100 and not 'B' in value: printpoint = printpoint + "9B"
		if '1' in value:
			if not "_" in property_subbuttonid_: printpoint = printpoint + "9C"
			if not "_" in property_subbuttonid_: printpoint = printpoint + "9D"
			if not property_buttonid in property_subbuttonid_: printpoint = printpoint + "9E"
		if 'B' in value and property_buttonid != property_buttonid_:
			from variables2 import idT, labelT
			two = 2
			y = 'Reset item'
			x = property_buttonid_
			property_buttonname2 = labelT.get('label'+property_buttonid)
			extra2 = extra2 + newline + addonString_servicefeatherence(32134).encode('utf-8') + space2 + str(property_buttonname2) + space + "(" + str(property_buttonid) + ")" #This action will also reset
		elif int(property_buttonid_) < 100:
			y = 'Reset item'
			x = property_buttonid_
			two = 1
		else:
			y = 'Remove item'
			x = property_buttonid_
			two = 1
			
	except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9F"
	
	if not '9' in printpoint:
		if '0' in value:
			'''main menu item'''
			printpoint = printpoint + "0"
			xbmc.sleep(100) ; returned = dialogyesno(y + space2 + str(property_buttonname), localize(19194) + extra2)
			if returned == 'skip': printpoint = printpoint + "8"
			else:
				for i in range(0,two):
					if i == 1: x = str(property_buttonid) ; y = str(property_buttonid_)

					if int(property_buttonid) > 99 and not 'B' in value:
						setSkinSetting('0','label' + x,"")
					else:
						setSkinSetting('0','label' + x,"...")
							
					setSkinSetting('1','off' + x,"false")
					setSkinSetting('1','pwd' + x,"false")
					setSkinSetting('1','sub' + x,"false")
					setSkinSetting('0','id' + x,"")
					setSkinSetting('0','color' + x,"")
					setSkinSetting('0','icon' + x,"")
					setSkinSetting('0','action' + x,"")
					#if i == 1: mode215(y, "RESET", name, printpoint)
					
					

					if '2' in value:
						'''sub menu items'''
						printpoint = printpoint + "2"
						if x == "": printpoint = printpoint + "9L"
						else:
							for i in range(90,109):
								if i > 99 : setSkinSetting('0','label'+x+'_'+str(i),"")
								else: setSkinSetting('0','label'+x+'_'+str(i),"")
								setSkinSetting('1','off'+x+'_'+str(i),"false")
								setSkinSetting('1','pwd'+x+'_'+str(i),"false")
								#setSkinSetting('0','id'+x+'_'+str(i),"")
								setSkinSetting('0','action'+x+'_'+str(i),"")
								setSkinSetting('0','icon'+x+'_'+str(i),"")
								'''---------------------------'''		
				printpoint = printpoint + "7"
					
		if '1' in value:
			'''sub menu item'''
			printpoint = printpoint + "1"
			if 'B' in value:
				y = 'Reset item'
				x = property_subbuttonid_
			else:
				y = 'Remove item'
				x = property_subbuttonid_
				
			xbmc.sleep(100) ; returned = dialogyesno(y + space2 + str(property_subbuttonname), localize(19194))
			if returned == 'skip': printpoint = printpoint + "8"
			else:
				setSkinSetting('1','off' + x,"false")
				setSkinSetting('1','pwd' + x,"false")
				if not '_90' in property_subbuttonid_ and not 'B' in value: setSkinSetting('0','label' + x,"")
				else: setSkinSetting('0','label' + x,"...")
				#setSkinSetting('0','id' + x,"")
				setSkinSetting('0','icon' + x,"")
				setSkinSetting('0','action' + x,"")
				setSkinSetting('0','background' + x,"")
				printpoint = printpoint + "7"
		
	
	if '8' in printpoint:
		notification_common('9')
	elif not "7" in printpoint and not "8" in printpoint:
		'''Error'''
		notification("Error...","","",1000)
	else:
		xbmc.executebuiltin('Action(Close)') ; xbmc.sleep(500)
		xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=215&value='+property_buttonid_+')')
		if two == 2: xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=215&value='+property_buttonid+')')
	
	
	
	text = "value" + space2 + str(value) + newline + \
	"property_buttonid" + space2 + str(property_buttonid) + space + "property_buttonid_" + space2 + str(property_buttonid_) + space + "property_buttonname" + space2 + str(property_buttonname) + newline + \
	"property_buttonname2" + space2 + str(property_buttonname2) + newline + \
	"two" + space2 + str(two) + newline + \
	"property_subbuttonid_" + space2 + str(property_subbuttonid_) + space + "property_subbuttonname" + space2 + str(property_subbuttonname) + newline + \
	extra
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def mode214(value, admin, name, printpoint):
	text = "value" + space2 + str(value)
	
	if value == '0':
		returned = dialogkeyboard(property_buttonname,addonString_servicefeatherence(32110).encode('utf-8'),0,"",'label'+property_buttonid_,"")
		if returned != 'skip':
			if returned == "": setSkinSetting('0','label'+property_buttonid_, '...')
	
	if value == '1':
		returned = dialogkeyboard(property_subbuttonname,addonString_servicefeatherence(32109).encode('utf-8'),0,"",'label'+property_subbuttonid_,"")
		if returned != 'skip':
			if returned == "": setSkinSetting('0','label'+property_subbuttonid_, '...')
	
	if value == '2':
		returned = dialogkeyboard(property_widgetbuttonname,addonString_servicefeatherence(32149).encode('utf-8'),0,"",'label'+property_widgetbuttonid_,"")
		if returned != 'skip':
			if returned == "": setSkinSetting('0','label'+widgetproperty_buttonid_, '...')
	
	if value == '5':
		'''SelectedColor'''
		returned_len = "" ; returned1 = "" ; path = ""
		property_selectedcolor = xbmc.getInfoLabel('Window(home).Property(SelectedColor)')
		currentbuttoncolor = xbmc.getInfoLabel('Skin.String(color'+property_buttonid_+')')
		notification(currentbuttoncolor,'Skin.String(color'+property_buttonid_+')','',2000)
		if property_selectedcolor == "" and property_buttonid_ != "": value2 = currentbuttoncolor
		else: value2 = property_selectedcolor
		
		returned = dialogkeyboard(value2,addonString_servicefeatherence(32111).encode('utf-8'),0,"","","")
		if returned != 'skip':
			if returned != "":
				returned_len = len(returned) ; returned1 = returned[:2]
				if returned1 != "ff":
					if returned_len == 8: returned = returned.replace(returned1,"ff",1)
					elif returned_len == 7: returned = 'f' + returned
					elif returned_len == 6: returned = 'ff' + returned
				
				setProperty('SelectedColor', str(returned), type="home")
				notification(addonString_servicefeatherence(32135).encode('utf-8'), str(returned), '', 1000) #New color selected!
	
		text = text + newline + 'returned' + space2 + str(returned) + space + 'returned_len' + space2 + str(returned_len) + space + 'returned1' + space2 + str(returned1) + newline + \
		'path' + space2 + str(path) + newline + \
		'property_selectedcolor' + space2 + str(property_selectedcolor) + newline + \
		'currentbuttoncolor' + space2 + str(currentbuttoncolor) + newline + \
		'value2' + space2 + str(value2)

	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def mode215(value, value2, name, printpoint):
	from variables2 import *
	extra2 = "" ; id = ""
	exe = printlog(title="test", printpoint="", text="", level=0, option="")
	
	if value != "" and value != '_' or xbmc.getInfoLabel('Skin.HasSetting(Admin)'): notification_common("2")
	
	'''מעודפים'''
	x = '17' ; id = x
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(1036))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(134)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'')		
			'''---------------------------'''
			
	'''הגדרות'''
	x = '18' ; id = x
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(5))
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'')		
			'''---------------------------'''
	
	'''כיבוי'''
	x = '19' ; id = x
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(13005))
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'')		
			'''---------------------------'''
			
	'''סרטים'''
	x = '90' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(342))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(Videos,MovieTitles,return)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/movies.png')		
			'''---------------------------'''
	
	'''סדרות'''
	x = '91' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(20343))
			
			if not defaultactionbuttons or value2 == 'RESET' or action == "":
				#if systembuildversion < 17: setSkinSetting('0','action'+id,'ActivateWindow(10025,TVShowTitles,return)')
				setSkinSetting('0','action'+id,'ActivateWindow(10025,TVShowTitles,return)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/tvshows.png')
			'''---------------------------'''

	'''ערוצי טלוויזיה'''
	x = '92' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(19023))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(TVChannels)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/LiveTV.png')
			'''---------------------------'''
	
	'''ילדים'''
	x = '93' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		background = backgroundT.get('icon'+x)
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(31814))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(10025,plugin://plugin.video.featherence.kids,return)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/kids.png')
			'''---------------------------'''	
			
	'''מוזיקה'''
	x = '94' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(2))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(10025,plugin://plugin.video.featherence.music,return)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/music.png')
			'''---------------------------'''
	
	'''ריק'''
	x = '95' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 3:
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,"")
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	
	
	'''תמונות'''
	x = '96' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(1))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(Pictures)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/pictures.png')
			'''---------------------------'''
	
	'''מזג אוויר'''
	x = '97' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,localize(8))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(MyWeather.xml)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/weather.png')
			'''---------------------------'''
			
	''''''
	x = '98' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and ( systemplatformwindows or systemplatformlinux and xbmc.getCondVisibility('System.HasAddon(service.openelec.settings)') ):
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			setSkinSetting('0','label'+id,"")
			setSkinSetting('0','action'+id,'')
			setSkinSetting('0','icon'+id,'')
			'''---------------------------'''	

	'''דוקו'''
	x = '99' ; id = idT2.get(x)
	if value == "_" or value == x:
		'''ראשי'''
		if id != "" and id != None and 1 + 1 == 2:	
			label = labelT.get('label'+str(id)) ; icon = iconT.get('icon'+str(id)) ; action = actionT.get('action'+str(id))
			if label == "" or label == "..." or value2 == 'RESET' or value2 == 'RESET-LABEL': setSkinSetting('0','label'+id,addonString(32803).encode('utf-8'))
			if not defaultactionbuttons or value2 == 'RESET' or action == "": setSkinSetting('0','action'+id,'ActivateWindow(10025,plugin://plugin.video.featherence.docu,return)')
			if icon == "" or value2 == 'RESET' or value2 == 'RESET-ICON': setSkinSetting('0','icon'+id,'special://home/addons/script.featherence.service/resources/icons/animals.png')
			'''---------------------------'''
	
	for i in range(90,119):
		x = idT.get('id'+str(i))
		#x = xbmc.getInfoLabel('Skin.String(id'+str(i)+')')
		if x != "" or x == 'None':
			try:
				int(x) + 1
				#extra2 = extra2 + newline + 'i' + space2 + str(i) + space + 'x' + space2 + str(x) + space
			except Exception, TypeError:
				setSkinSetting('0','id'+str(i),"",force=True)
				extra2 = extra2 + newline + 'i' + space2 + str(i) + space + 'x' + space2 + str(x) + space
				
	text = "value" + space2 + str(value) + space + "id" + space2 + str(id) + newline + \
	"value2" + space2 + str(value2) + newline + \
	"idT" + space2 + str(idT) + newline + \
	extra2
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def mode217(value, value2, name, printpoint):
	'''------------------------------
	---setWidgetButton---------------
	------------------------------'''
	from variables2 import labelT, idT, idT2
	extra = "" ; TypeError = "" ; returned = "" ; x = ""
	widget311 = xbmc.getInfoLabel('Skin.String(Widget311)')
	widget311_name = xbmc.getInfoLabel('Skin.String(Widget311_name)')
	if not widget311: widget311 = 90
	try: widget311 = int(widget311)
	except: pass
	if not widget311_name: widget311_name = labelT.get('label90')
	
	widget312 = xbmc.getInfoLabel('Skin.String(Widget312)')
	widget312_name = xbmc.getInfoLabel('Skin.String(Widget312_name)')
	if not widget312: widget312 = 91
	try: widget312 = int(widget312)
	except: pass
	if not widget312_name: widget312_name = labelT.get('label91')
	
	widget317 = xbmc.getInfoLabel('Skin.String(widget317)')
	widget317_name = xbmc.getInfoLabel('Skin.String(widget317_name)')
	if not widget317: widget317 = 97
	try: widget317 = int(widget317)
	except: pass
	if not widget317_name: widget317_name = labelT.get('label97')
	
	list = ['-> (Exit)',''] #ID
	list2 = ['-> (Exit)','Reset'] #NAME
	
	list.append('None')
	if value == '1' and widget311_name == 'None': list2.append('[COLOR=yellow]' + 'None' + '[/COLOR]')
	elif value == '2' and widget312_name == 'None': list2.append('[COLOR=yellow]' + 'None' + '[/COLOR]')
	elif value == '7' and widget317_name == 'None': list2.append('[COLOR=yellow]' + 'None' + '[/COLOR]')
	else: list2.append('None')
	
	for i in range(90,120):
		x = idT.get('id'+str(i)) ; x2 = idT2.get('id'+str(x))
		if x != "" and x != None:
			x = int(x)
			if value == '1' and (x == widget312 or x == widget317): continue
			elif value == '2' and (x == widget311 or x == widget317): continue
			elif value == '7' and (x == widget311 or x == widget312): continue
			
			y = labelT.get('label'+str(i))
			if y != "" and y != None:
				list.append(x)
				if value == '1' and (widget311 == x or widget311_name == y): list2.append('[COLOR=yellow]' + to_utf8(y) + '[/COLOR]')
				elif value == '2' and (widget312 == x2 or widget312_name == y): list2.append('[COLOR=yellow]' + to_utf8(y) + '[/COLOR]')
				elif value == '7' and (widget317 == x2 or widget317_name == y): list2.append('[COLOR=yellow]' + to_utf8(y) + '[/COLOR]')
				else: list2.append(to_utf8(y))
		
		
	returned, dvalue = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list2,0)
	dvalue2 = list[returned]
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		if value == '1': z = 'Widget311'
		elif value == '2': z = 'Widget312'
		elif value == '7': z = 'widget317'
		else:
			printpoint = printpoint + '9'
			notification_common("17")
		
		if not '9' in printpoint:
			setSkinSetting('0', z, str(dvalue2))
			setSkinSetting('0', z + '_name', str(dvalue))
			notification_common("13")
	
	text = 'value' + space2 + str(to_utf8(value)) + newline + \
	'value2' + space2 + str(to_utf8(value2)) + newline + \
	'widget311' + space2 + str(to_utf8(widget311)) + newline + \
	'widget312' + space2 + str(to_utf8(widget312)) + newline + \
	'list' + space2 + str(to_utf8(list)) + newline + \
	'list2' + space2 + str(to_utf8(list2)) + newline + \
	'returned' + space2 + str(to_utf8(returned)) + newline + \
	'dvalue' + space2 + str(to_utf8(dvalue)) + newline + \
	'dvalue2' + space2 + str(to_utf8(dvalue2)) + newline + \
	'x' + space2 + str(to_utf8(x)) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def mode218(value, admin, name, printpoint):
	'''------------------------------
	---editButtonProprties-----------
	------------------------------'''	
	message = ""
	if "view" in value:
		customhomecustomizerW = xbmc.getCondVisibility('Window.IsVisible(CustomHomeCustomizer.xml)')
		dialogfullscreeninfoW = xbmc.getCondVisibility('Window.IsVisible(DialogFullScreenInfo.xml)')
		dialogvideoinfoW = xbmc.getCondVisibility('Window.IsVisible(DialogVideoInfo.xml)')
		dialogsubtitlesW = xbmc.getCondVisibility('Window.IsVisible(DialogSubtitles.xml)')
		homeW = xbmc.getCondVisibility('Window.IsVisible(Home.xml)')
		myweatherW = xbmc.getCondVisibility('Window.IsVisible(MyWeather.xml)')
		playerpaused = xbmc.getCondVisibility('Player.Paused')
		message = message + newline + "script.featherence.service_downloading" + space2 + xbmc.getInfoLabel('Window(home).Property(script.featherence.service_downloading)')
		
		message = message + newline + "Current XML" + space2 + xbmc.getInfoLabel('Window.Property(xmlfile)')
		message = message + newline + "Current Control" + space2 + xbmc.getInfoLabel('System.CurrentControl')
		message = message + newline + "Container(9000).ListItem(0).Label" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Label')
		message = message + newline + "Container(9000).ListItem(0).Label2" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Label2')
		message = message + newline + "TEMP" + space2 + property_temp
		message = message + newline + "TEMP2" + space2 + property_temp2
		
		if dialogfullscreeninfoW and playerpaused:
			message = message + newline + "VideoPlayer.Duration" + space2 + xbmc.getInfoLabel('VideoPlayer.Duration')
			message = message + newline + "VideoPlayer.Year" + space2 + xbmc.getInfoLabel('VideoPlayer.Year')
			message = message + newline + "VideoPlayer.Rating" + space2 + xbmc.getInfoLabel('VideoPlayer.Rating')
			message = message + newline + "VideoPlayer.Plot" + space2 + xbmc.getInfoLabel('VideoPlayer.Plot')
			
			message = message + newline + "VideoPlayer.Genre" + space2 + xbmc.getInfoLabel('VideoPlayer.Genre')
			message = message + newline + "VideoPlayer.Tagline" + space2 + xbmc.getInfoLabel('VideoPlayer.Tagline')
			message = message + newline + "VideoPlayer.Title" + space2 + xbmc.getInfoLabel('VideoPlayer.Title')
			message = message + newline + "custom" + space2 + xbmc.getInfoLabel('VideoPlayer.VideoCodec') #CUSTOM TEST
			
		elif myweatherW:
			message = message + newline + "Day0 Title" + space2 + xbmc.getInfoLabel('Window.Property(Day0.Title)')
			message = message + newline + "Day1 Title" + space2 + xbmc.getInfoLabel('Window.Property(Day1.Title)')
			message = message + newline + "Day2 Title" + space2 + xbmc.getInfoLabel('Window.Property(Day2.Title)')
			message = message + newline + "Day3 Title" + space2 + xbmc.getInfoLabel('Window.Property(Day3.Title)')
			message = message + newline + "Day4 Title" + space2 + xbmc.getInfoLabel('Window.Property(Day4.Title)')
			
			message = message + newline + "Current day label (31)" + space2 + xbmc.getInfoLabel('Control.GetLabel(31)')
		
		elif dialogvideoinfoW:
			message = message + newline + "Window.Property(actor.Age)" + space2 + xbmc.getInfoLabel('$INFO[Window.Property(actor.Age)]')
			message = message + newline + "Window(home).Property(Age)" + space2 + xbmc.getInfoLabel('$INFO[Window(home).Property(Age)]')
			
			message = message + newline + "Window.Property(current.actor.name)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.name)')
			message = message + newline + "Window.Property(current.actor.biography)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.biography)')
			message = message + newline + "Window.Property(current.actor.icon)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.icon)')
			message = message + newline + "Window.Property(current.actor.fanart_image)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.fanart_image)')
			message = message + newline + "Window.Property(current.actor.extrafanart)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.extrafanart)')
			message = message + newline + "Window.Property(current.actor.extrathumb)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.extrathumb)')
			message = message + newline + "Window.Property(current.actor.name)" + space2 + xbmc.getInfoLabel('Window.Property(current.actor.name)')
			
		elif dialogsubtitlesW:
			message = message + newline + "Container(120).NumItems" + space2 + xbmc.getInfoLabel('Container(120).NumItems')
			message = message + newline + "Container(150).ListItemNoWrap(0).label" + space2 + xbmc.getInfoLabel('Container(150).ListItemAbsolute(0).label')
			message = message + newline + "Container(150).ListItemNoWrap(1).label" + space2 + xbmc.getInfoLabel('Container(150).ListItemAbsolute(1).label')
			message = message + newline + "Container(150).ListItemNoWrap(2).label" + space2 + xbmc.getInfoLabel('Container(150).ListItemAbsolute(2).label')
			message = message + newline + "Container(150).ListItemNoWrap(3).label" + space2 + xbmc.getInfoLabel('Container(150).ListItemAbsolute(3).label')
			message = message + newline + "Container(150).ListItemNoWrap(4).label" + space2 + xbmc.getInfoLabel('Container(150).ListItemAbsolute(4).label')
			message = message + newline + "Subtitle_Service" + space2 + xbmc.getInfoLabel('Window(home).Property(Subtitle_Service)')
			message = message + newline + "DialogSubtitles" + space2 + xbmc.getInfoLabel('Window(home).Property(DialogSubtitles)')
			message = message + newline + "DialogSubtitles2" + space2 + xbmc.getInfoLabel('Window(home).Property(DialogSubtitles2)')
			for i in range(1,11):
				message = message + newline + 'DialogSubtitlesNA'+str(i) + space2 + xbmc.getInfoLabel('Window(home).Property(DialogSubtitlesNA'+str(i)+')')
		elif xbmc.getCondVisibility('Window.IsVisible(Custom1170.xml)'):
			message = message + newline + "SelectedColor" + space2 + xbmc.getInfoLabel('Window(home).Property(SelectedColor)')
		else:
			message = message + newline + "scriptfeatherenceservice_random" + space2 + scriptfeatherenceservice_random
			message = message + newline + "scriptfeatherenceservice_random1" + space2 + scriptfeatherenceservice_random1
			message = message + newline + "scriptfeatherenceservice_random2" + space2 + scriptfeatherenceservice_random2
			message = message + newline + "scriptfeatherenceservice_random3" + space2 + scriptfeatherenceservice_random3
			message = message + newline + "scriptfeatherenceservice_random4" + space2 + scriptfeatherenceservice_random4
			message = message + newline + "scriptfeatherenceservice_random5" + space2 + scriptfeatherenceservice_random5
			message = message + newline + "scriptfeatherenceservice_randomL" + space2 + str(scriptfeatherenceservice_randomL)
			message = message + newline + '---------------------------'
			#message = message + newline + "ListItem.Property(id)" + space2 + xbmc.getInfoLabel('Container(9000).ListItemNoWrap(0).Property(id)')
			#message = message + newline + "ListItem.Property(id)" + space2 + xbmc.getInfoLabel('ListItem.Property(id)')
			message = message + newline + "Button.ID" + space2 + property_buttonid
			message = message + newline + "Button.ID_" + space2 + property_buttonid_
			message = message + newline + "Button.Name" + space2 + property_buttonname
			message = message + newline + '---------------------------'
			message = message + newline + "SubButton.ID_" + space2 + property_subbuttonid_
			message = message + newline + "SubButton.Name" + space2 + property_subbuttonname
			message = message + newline + '---------------------------'
			message = message + newline + "Previous_SubButton.ID_" + space2 + property_previoussubbuttonid_
			message = message + newline + "Next_SubButton.ID_" + space2 + property_nextsubbuttonid_
			message = message + newline + '---------------------------'
			message = message + newline + "WidgetButton.ID_" + space2 + property_widgetbuttonid_
			message = message + newline + "WidgetButton.Name" + space2 + property_widgetbuttonname
			message = message + newline + '---------------------------'
			message = message + newline + "sw" + space2 + 'sw' + property_buttonid
			message = message + newline + "sw_" + space2 + xbmc.getInfoLabel('Skin.String(sw'+property_buttonid+'')
			message = message + newline + '---------------------------'
			message = message + newline + "widget311" + space2 + xbmc.getInfoLabel('Skin.String(Widget311)')
			message = message + newline + "widget312" + space2 + xbmc.getInfoLabel('Skin.String(Widget312)')
			message = message + newline + "ReloadSkin" + space2 + property_reloadskin
			message = message + newline + '---------------------------'
			message = message + newline + "1000progress" + space2 + property_1000progress
			message = message + newline + "1000title" + space2 + property_1000title
			message = message + newline + "1000comment" + space2 + property_1000comment
			message = message + newline + '---------------------------'
			message = message + newline + "property_mode10" + space2 + property_mode10
			message = message + newline + "ViewsSettings" + space2 + xbmc.getInfoLabel('Window(home).Property(ViewsSettings)')
			message = message + newline + "HomeLastPos" + space2 + xbmc.getInfoLabel('Window(home).Property(HomeLastPos)')
			message = message + newline + "HomeLastPos2" + space2 + xbmc.getInfoLabel('Window(home).Property(HomeLastPos2)')
			message = message + newline + '---------------------------'
			message = message + newline + "SelectedColor" + space2 + xbmc.getInfoLabel('Window(home).Property(SelectedColor)')
			message = message + newline + '---------------------------'
			message = message + newline + "tips" + space2 + xbmc.getInfoLabel('Window(home).Property(tips)')
			message = message + newline + "ListItem.Path" + space2 + xbmc.getInfoLabel('ListItem.Path')
			message = message + newline + "Container.FolderPath" + space2 + xbmc.getInfoLabel('Container.FolderPath')
			message = message + newline + "Container.FolderName" + space2 + xbmc.getInfoLabel('Container.FolderName')
			message = message + newline + "ListItem.Overlay" + space2 + xbmc.getInfoLabel('ListItem.Overlay')
			message = message + newline + "VAR-11156label" + space2 + xbmc.getInfoLabel('$VAR[11156label]')
			message = message + newline + "ListItem.Duration" + space2 + xbmc.getInfoLabel('ListItem.Duration')
			message = message + newline + "Container.Viewmode" + space2 + xbmc.getInfoLabel('Container.Viewmode')
			message = message + newline + "ListItem.SetId" + space2 + xbmc.getInfoLabel('ListItem.SetId')
			message = message + newline + "ListItem.Set" + space2 + xbmc.getInfoLabel('ListItem.Set')
			message = message + newline + '---------------------------'
			if xbmc.getCondVisibility('System.HasAddon(script.tv.show.next.aired)'):
				message = message + newline + "NextAired.NextDate" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.NextDate)'))
				message = message + newline + "NextAired.NextTitle" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.NextTitle)'))
				message = message + newline + "NextAired.0.Label" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.0.Label)'))
				message = message + newline + "NextAired.0.AirTime" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.0.AirTime)'))
				message = message + newline + "NextAired.0.NextDate" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.0.NextDate)'))
				message = message + newline + "NextAired.0.NextTitle" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.0.NextTitle)'))
				message = message + newline + "NextAired.1.Label" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.1.Label)'))
				message = message + newline + "NextAired.1.AirTime" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.1.AirTime)'))
				message = message + newline + "NextAired.1.NextDate" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.1.NextDate)'))
				message = message + newline + "NextAired.1.NextTitle" + space2 + str(xbmc.getInfoLabel('Window(Home).Property(NextAired.1.NextTitle)'))
				message = message + newline + '---------------------------'
			message = message + newline + "ListItem.Label" + space2 + str(xbmc.getInfoLabel('$INFO[ListItem.Label]'))
			message = message + newline + "ListItem.Title" + space2 + str(xbmc.getInfoLabel('$INFO[ListItem.Title]'))
			message = message + newline + "ListItem.TVShowTitle" + space2 + str(xbmc.getInfoLabel('$INFO[ListItem.TVShowTitle]'))
			message = message + newline + "custom" + space2 + str(xbmc.getInfoLabel('$INFO[ListItem.Trailer]')) #CUSTOM TEST
			message = message + newline + "custom2" + space2 + str(xbmc.getInfoLabel('Container(50).ListItemPosition(0).Overlay')) #CUSTOM TEST
			message = message + newline + "custom3" + space2 + str(xbmc.getInfoLabel('System.BuildVersion')) #CUSTOM TEST
			message = message + newline + "ListItem.Property(TotalEpisodes)" + space2 + str(xbmc.getInfoLabel('ListItem.Property(TotalEpisodes)')) #CUSTOM TEST
			message = message + newline + "Window(home).Property(RecentMovie.1.Art(fanart))" + space2 + str(xbmc.getInfoLabel('Window(home).Property(RecentMovie.1.Art(fanart))')) #CUSTOM TEST
			message = message + newline + "Window(home).Property(RecentMovie.2.Art(fanart))" + space2 + str(xbmc.getInfoLabel('Window(home).Property(RecentMovie.2.Art(fanart))')) #CUSTOM TEST
			
			
			message = message + newline + "Skin.String(PassProtect)" + space2 + str(xbmc.getInfoLabel('Skin.String(PassProtect)')) #
			message = message + newline + "Window(home).Property(PassProtect)" + space2 + str(xbmc.getInfoLabel('Window(home).Property(PassProtect)')) #
			
			
		if homeW or customhomecustomizerW:
			message = message + newline + "Container(9000).ListItem(0).Property(id)" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Property(id)')
			message = message + newline + "Container(9000).ListItem(0).Property(pwd)" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Property(pwd)')
			message = message + newline + "Container(9000).ListItem(0).Property(off)" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Property(off)')
			message = message + newline + "Container(9000).ListItem(0).Property(sub)" + space2 + xbmc.getInfoLabel('Container(9000).ListItem(0).Property(sub)')

		header = name
		diaogtextviewer(header,message)
		printlog(title="views", printpoint="", text=message, level=0, option="")
							
def mode231(value, value2, admin, name, printpoint):
	'''------------------------------
	---INSTALL-ADDON-----------------
	------------------------------'''
	if not 'resource.' in value: notification_common("24")
	if value2 == "": installaddon(value, update=True)
	else: installaddonP(value, update=True)
	
	'''---------------------------'''

def mode232(value, admin, name, printpoint):
	'''------------------------------
	---ACTION-BUTTON-----------------
	------------------------------'''
	id1 = "" ; id2 = "" ; extra = "" ; TypeError = "" ; xaction = "" ; xlabel = "" ; xicon = "" ; count = 0
	if printpoint != "": printpoint = printpoint + "_"
	if value == "sw": printpoint = printpoint + "sw" ; value = ""
	
	setProperty('mode232', 'true', type="home")
	
	if not xbmc.getCondVisibility('System.HasAddon(script.skinshortcuts)') or not os.path.exists(addons_path + 'script.skinshortcuts'):
		addon1 = installaddonP('script.skinshortcuts', update=True)
		if not xbmc.getCondVisibility('System.HasAddon(script.skinshortcuts)'):
			notification('script.skinshortcuts is disable?','','',4000)
	elif not os.path.exists(addons_path + 'script.module.unidecode'):
		installaddonP('script.module.unidecode', update=True)
	
	else:
		printpoint = printpoint + "0"
		try:
			if value != "":
				if '_' in value or value == 'TEMP': pass
				else: test = int(value) + 1
				id1 = value
			elif custom1175W and not custom1138W:
				if property_widgetbuttonid_ != "":
					id1 = property_widgetbuttonid_
				elif "sw" in printpoint:
					id1 = 'sw' + str(property_buttonid)
				elif property_buttonid_ == "": printpoint = printpoint + "9B"
				else: test = int(property_buttonid) + 1 ; id1 = property_buttonid_
			elif custom1138W:
				if property_subbuttonid_ == "" or (not property_buttonid in property_subbuttonid_): printpoint = printpoint + "9C"
				else: id1 = property_subbuttonid_
		except Exception, TypeError: extra = extra + newline + "TypeError" + space2 + str(TypeError) ; printpoint = printpoint + "9D"
		
		if id1 != "":
			if not xbmc.getInfoLabel('Skin.HasSetting(Action_Thumbnail)'):
				Action_Thumbnail = '&skinThumbnail=icon'+id1
				#Action_Label = '&skinLabel=label'+id1
			else:
				Action_Thumbnail = ""
				#Action_Label = ""
			Action_Label = '&skinLabel=label'+id1
			
			if value == 'TEMP':
				'''add-on'''
				printpoint = printpoint + 'x1'
				Action_Thumbnail = '&skinThumbnail=icon'+id1
				Action_Label = '&skinLabel=label'+id1
				
				xbmc.executebuiltin('RunScript(script.skinshortcuts,type=shortcuts&custom=True&showNone=True'+'&skinList=action'+id1+Action_Thumbnail+Action_Label+')')
			elif custom1175W and not custom1138W:
				'''Main Action'''
				printpoint = printpoint + "x1"
				if 'sw' in printpoint:
					xbmc.executebuiltin('RunScript(script.skinshortcuts,type=widgets&showNone=True&skinWidgetPath='+id1+'&skinWidgetName='+id1+'_name)')
					#xbmc.executebuiltin('RunScript(script.skinshortcuts,type=widgets&amp;showNone=True/False]&amp;grouping=[grouping]&amp;skinWidget=[skinWidget]&amp;skinWidgetType=[skinWidgetType]&amp;skinWidgetName=[skinWidgetName]&amp;skinWidgetTarget=[skinWidgetTarget]&amp;skinWidgetPath=[skinWidgetPath])')
				else:
					xbmc.executebuiltin('RunScript(script.skinshortcuts,type=shortcuts&custom=True&showNone=True&skinAction=action'+id1+Action_Thumbnail+Action_Label+')')
			elif custom1138W:
				'''Sub Action'''
				printpoint = printpoint + "x2"
				xbmc.executebuiltin('RunScript(script.skinshortcuts,type=shortcuts&custom=True&showNone=True&skinAction=action'+id1+Action_Thumbnail+Action_Label+')')
				'''---------------------------'''
			else: printpoint = printpoint + "8"	
			
			if "x" in printpoint:
				'''wait'''
				xbmc.sleep(5000)
				dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
				dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
				dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
				dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
				dialogconfirmW = xbmc.getCondVisibility('Window.IsVisible(DialogConfirm.xml)')
				count = 0
				while ((dialogselectW or dialogprogressW or dialogyesnoW or dialogokW or dialogconfirmW) or count < 2) and not xbmc.abortRequested:
					xbmc.sleep(1000)
					dialogselectW = xbmc.getCondVisibility('Window.IsVisible(DialogSelect.xml)')
					dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
					dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
					dialogokW = xbmc.getCondVisibility('Window.IsVisible(DialogOK.xml)')
					dialogconfirmW = xbmc.getCondVisibility('Window.IsVisible(DialogConfirm.xml)')
					if not dialogselectW and not dialogprogressW and not dialogyesnoW and not dialogokW and not dialogconfirmW:
						count += 1
					elif count > 0: count -= 1
					'''---------------------------'''
				xbmc.sleep(500) ; xlabel = xbmc.getInfoLabel('Skin.String(label'+id1+')')
				if not 'sw' in printpoint:
					if xlabel == "":
						setSkinSetting('0','label'+id1,'...')
						if 'x1' in printpoint and not '_' in id1: setSkinSetting('0','label'+id1,'...', force=True)
					else:
						if 'x1' in printpoint and not '_' in id1: setSkinSetting('0','label'+id1,str(xlabel), force=True)
				
				xicon = xbmc.getInfoLabel('Skin.String(icon'+id1+')')
				if not 'sw' in printpoint:
					x, x_ = TranslatePath(xicon, filename=True, urlcheck_=False)
					if x_ != "": setSkinSetting('0','icon'+id1,x_, force=True)
					else: setSkinSetting('0','icon'+id1,x, force=True)
				
				if 'sw' in printpoint:
					xaction = xbmc.getInfoLabel('Skin.String('+id1+')')
				else:
					xaction = xbmc.getInfoLabel('Skin.String(action'+id1+')')
				xlabel = xbmc.getInfoLabel('Skin.String(label'+id1+')')
					
	text = "value" + space2 + str(value) + space + "property_buttonid" + space2 + str(property_buttonid) + newline + \
	"id1" + space2 + str(id1) + space + "id2" + space2 + str(id2) + newline + \
	"xaction" + space2 + str(xaction) + newline + \
	"xicon" + space2 + str(xicon) + newline + \
	"xlabel" + space2 + str(xlabel) + newline + \
	"count" + space2 + str(count) + newline + \
	extra
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	setProperty('mode232', '', type="home")
			
def mode233(value, admin, name, printpoint):
	'''------------------------------
	---Add-Thumb/Fanart--------------
	------------------------------'''
	printpoint = "" ; returned_ = ""
	x = "" ; path = "" ; x2_ = "" ; x_ = "" ; xf = "" ; xf_ = ""
	if '3' in value:
		printpoint = printpoint + 'C'
		y = property_widgetbuttonid_
	else: y = property_buttonid_
	customiconspath = to_unicode(xbmc.getInfoLabel('Skin.String(CustomIconsPath)'))
	custombackgroundspath = to_unicode(xbmc.getInfoLabel('Skin.String(CustomBackgroundsPath)'))
	property_temp2 = xbmc.getInfoLabel('Window(home).Property(TEMP2)')
	
	if '0' in value:
		printpoint = printpoint + '0'
		y = property_subbuttonid_
		value = value.replace('0',"",1)
	
	if '1' in value:
		'''Add-Fanart'''
		name = localize(20441)
		x = 'background'
		if not '0' in printpoint and not 'C' in printpoint: y = property_buttonid
		nolabel=localize(20438)
		yeslabel=localize(20441)
	
	elif '2' in value:
		'''Add-Thumb'''
		name = localize(20017)
		x = 'icon'
		nolabel=localize(20017)
		yeslabel=localize(20015)
	
	if x != "":
		printpoint = printpoint + '1'
		returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=nolabel, yeslabel=yeslabel)
		if returned == 'ok':
			printpoint = printpoint + '2'
			returned2, value2 = getRandom(0, min=0, max=100, percent=40)
			if returned2 == 'ok': notification('O_o???','Copy & Paste an image URL','',4000)
			'''remote'''
			url = dialogkeyboard("", yeslabel, 0, "1", "", "")
			if url != "skip":
				from shared_modules3 import urlcheck
				returned2 = urlcheck(url, ping=False)
				if returned2 != "ok":
					notification(localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]), addonString_servicefeatherence(32801).encode('utf-8') + space + '..', "", 2000)
					header = localize(2102, s=[addonString_servicefeatherence(32436).encode('utf-8')]) #"URL Error"
					message = addonString_servicefeatherence(32802).encode('utf-8') + space2 + newline + '[B]' + str(value) + '[/B]'
					diaogtextviewer(header,message)
				else:
					setSkinSetting('0',x+y,str(url))
		else:
			printpoint = printpoint + '3'
			
			'''local'''
			if '1' in value:
				if xbmc.getCondVisibility('Skin.HasSetting(MultiFanart)'):
					returned = dialogyesno(str(name), addonString_servicefeatherence(32423).encode('utf-8'), nolabel=localize(20428), yeslabel=addonString_servicefeatherence(32112).encode('utf-8'))
					if returned == 'ok': type = 0
					else: type = 2
				else: type = 2
				printpoint = printpoint + '4'
				
				x_ = xbmc.getInfoLabel('Skin.String(background'+y+')')
				xf, xf_ = TranslatePath(x_, filename=True)
				x2, x2_ = TranslatePath(x_, filename=False)
				
				if os.path.exists(custombackgroundspath): path = custombackgroundspath
				elif os.path.isfile(xf):
					if os.path.exists(x2_): path = x2_
					elif os.path.exists(x2): path = x2
				else: path = featherenceservicebackgrounds_path
				#xbmc.executebuiltin('Skin.SetImage(background'+y+',,'+path+')')
				returned_ = setPath(type=type,mask="pic", folderpath=path, original=False) ; xbmc.sleep(500) ; property_temp2 = xbmc.getInfoLabel('Window(home).Property(TEMP2)')
				if returned_ != "": setSkinSetting('0','background'+y,to_unicode(returned_))
				
			elif '2' in value:
				printpoint = printpoint + '5'
				
				x_ = xbmc.getInfoLabel('Skin.String(icon'+y+')')
				xf, xf_ = TranslatePath(x_, filename=True)
				x2, x2_ = TranslatePath(x_, filename=False)
				
				if os.path.exists(customiconspath): path = customiconspath
				elif os.path.isfile(xf):
					if os.path.exists(x2_): path = x2_
					elif os.path.exists(x2): path = x2
				else: path = featherenceserviceicons_path
				#xbmc.executebuiltin('Skin.SetImage(icon'+y+',,'+path+')')
				returned_ = setPath(type=2,mask="pic", folderpath=path, original=False) ; xbmc.sleep(500) ; property_temp2 = xbmc.getInfoLabel('Window(home).Property(TEMP2)')
				if returned_ != "": setSkinSetting('0','icon'+y,to_unicode(returned_))
			else: printpoint = printpoint + '9'
			
			setProperty('TEMP', '', type="home")
			setProperty('TEMP2', '', type="home")
			
	text = 'value' + space2 + to_utf8(value) + space + 'path' + space2 + to_utf8(path) + newline + \
	'name' + space2 + to_utf8(name) + newline + \
	'x_' + space2 + to_utf8(x_) + newline + \
	'xf' + space2 + to_utf8(xf) + newline + \
	'xf_' + space2 + to_utf8(xf_) + newline + \
	'x2' + space2 + to_utf8(x2) + newline + \
	'x2_' + space2 + to_utf8(x2_) + newline + \
	'y' + space2 + to_utf8(y) + newline + \
	'property_widgetbuttonid_' + space2 + to_utf8(property_widgetbuttonid_) + newline + \
	'customiconspath' + space2 + to_utf8(customiconspath) + newline + \
	'custombackgroundspath' + space2 + to_utf8(custombackgroundspath) + newline + \
	'property_subbuttonid_' + space2 + to_utf8(property_subbuttonid_) + newline + \
	'property_temp2' + space2 + to_utf8(property_temp2)
	printlog(title='mode233', printpoint=printpoint, text=text, level=0, option="")

def mode235(value, value2, name, printpoint):
	'''------------------------------
	---Default-Icon/Background-------
	------------------------------'''
	
	setProperty('TEMP2', 'default', type="home") ; xbmc.executebuiltin('Dialog.Close(filebrowser)')
	if property_temp == 'background':
		printpoint = printpoint + '1'
		if property_subbuttonid_ != "":
			printpoint = printpoint + '4'
			setSkinSetting('0',property_temp+str(property_subbuttonid_),"")
		elif property_buttonid != "":
			setSkinSetting('0',property_temp+str(property_buttonid),"")
			printpoint = printpoint + '2'
			'''---------------------------'''
	elif property_temp == 'icon':
		printpoint = printpoint + '3'
		if property_subbuttonid_ != "":
			printpoint = printpoint + '4'
			setSkinSetting('0',property_temp+str(property_subbuttonid_),"")
		elif property_buttonid_ != "":
			printpoint = printpoint + '5'
			setSkinSetting('0',property_temp+str(property_buttonid_),"")
			mode215(property_buttonid_, 'RESET-ICON', '', '')
	
	else: printpoint = printpoint + '6'
	
	xbmc.sleep(500)
	
	text = 'property_temp' + space2 + str(property_temp) + newline + \
	'property_buttonid' + space2 + str(property_buttonid) + newline + \
	'property_temp2' + space2 + str(property_temp2)
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def mode512(value):
	'''------------------------------
	---INTERNET-BUTTON---------------
	------------------------------'''
	import webbrowser
	name = 'INTERNET-BUTTON' ; TypeError = "" ; extra = "" ; printpoint = ""
	xbmc.executebuiltin('ActivateWindow(busydialog)')
	try:
		url = ""
		if value == '0': url = 'www.google.com'
		elif value == '1': url = 'www.facebook.com/groups/featherence'
		elif value == '2': url = 'www.github.com/finalmakerr/featherence'
		elif value == '3': url = 'www.youtube.com'
		elif value == '4': url = 'https://www.google.co.il/imghp?hl=iw&tab=wi' #Thumbnail
		elif value == '5': url = 'https://www.google.co.il/imghp?hl=iw&tab=wi' #Fanart
		elif value == '7': url = 'www.featherence.com' #Website
		else: url = value
		
		name = localize(443)
		
		
		

		if systemplatformwindows: webbrowser.open(url)
		elif systemplatformandroid:
			webbrowser.open(url)
			app = 'com.android.chrome'
			intent = 'android.intent.action.VIEW'
			dataType = ''
			cmd = 'StartAndroidActivity("%s", "%s", "%s", "%s")' % (app, intent, dataType, url)
			xbmc.executebuiltin(cmd)
			#terminal('adb shell am start -a android.intent.action.VIEW -d '+url+'','')
		elif systemplatformlinux:
			if xbmc.getCondVisibility('System.HasAddon(service.openelec.settings)'):
				if xbmc.getCondVisibility('System.HasAddon(browser.chromium)'): xbmc.executebuiltin('RunAddon(browser.chromium)')
				else: installaddon('browser.chromium', update=True)
			else: webbrowser.open(url)
		elif systemplatformosx: webbrowser.open(url)
		elif systemplatformios: webbrowser.open(url)
		else: notification_common('25')

	except Exception, TypeError:
		extra = extra + 'TypeError' + space2 + str(TypeError)
	
	xbmc.sleep(1000)
	xbmc.executebuiltin('Dialog.Close(busydialog)')
	
	text = 'value' + space2 + str(value) + space + extra
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def videoplayertweak(admin,playerhasvideo):
	if playerhasvideo:
		
		videoplayersubtitlesenabled = xbmc.getInfoLabel('VideoPlayer.SubtitlesEnabled')
		videoplayerhassubtitles = xbmc.getInfoLabel('VideoPlayer.HasSubtitles')
				
		
		videoosd = xbmc.getCondVisibility('Window.IsVisible(VideoOSD.xml)')
		systemidle10 = xbmc.getCondVisibility('System.IdleTime(10)')
		videoosdsettingsW = xbmc.getCondVisibility('Window.IsVisible(VideoOSDSettings.xml)')
		if videoosd and systemidle10 and not videoosdsettingsW:
			'''video osd auto close'''
			subtitleosdbutton = xbmc.getCondVisibility('Control.HasFocus(703)') #subtitleosdbutton
			volumeosdbutton = xbmc.getCondVisibility('Control.HasFocus(707)') #volumeosdbutton
			dialogpvrchannelsosd = xbmc.getCondVisibility('Window.IsVisible(DialogPVRChannelsOSD.xml)')
			'''---------------------------'''
			if (not subtitleosdbutton or not videoplayerhassubtitles) and not volumeosdbutton and not dialogpvrchannelsosd:
				#if admin: xbmc.executebuiltin('Notification(Admin,videoosdauto,1000)')
				xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
				'''---------------------------'''
			else:
				if xbmc.getCondVisibility('System.IdleTime(20)'): xbmc.executebuiltin('Dialog.Close(VideoOSD.xml)')
				'''---------------------------'''

	
def setSkin_Update(admin, datenowS, Skin_Version, Skin_UpdateDate, Skin_UpdateLog):
	'''------------------------------
	---CHECK-FOR-SKIN-UPDATE---------
	------------------------------'''
	name = 'setSkin_Update' ; printpoint = ""
	Skin_Version2 = xbmc.getInfoLabel('System.AddonVersion(skin.featherence)')
	
	if datenowS == "" or datenowS == None: printpoint = printpoint + '9'
	else:
		
		if Skin_Version != Skin_Version2:
			printpoint = printpoint + '1'
			setsetting('Skin_UpdateLog',"true")
			setsetting('Skin_UpdateDate',datenowS)
			setsetting('Skin_Version',Skin_Version2)
			#xbmc.executebuiltin('RunScript(script.featherence.service.debug,,?mode=19)')
			Skin_UpdateLog = 'true'
			
		else: printpoint = printpoint + '2'
		
		if Skin_UpdateLog == 'true':
			printpoint = printpoint + '3'
			printpoint = printpoint + '7'
			setsetting('Skin_UpdateLog',"false")
			setSkin_UpdateLog(admin, Skin_Version2, Skin_UpdateDate, datenowS)
		else:
			printpoint = printpoint + '8'
			
	text = "Skin_Version" + space2 + str(Skin_Version) + newline + \
	"Skin_Version2" + space2 + str(Skin_Version2) + newline + \
	"datenowS" + space2 + str(datenowS) + newline + \
	"Skin_UpdateDate" + space2 + str(Skin_UpdateDate) + newline + \
	"Skin_UpdateLog" + space2 + str(Skin_UpdateLog)
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def setSkin_UpdateLog(admin, Skin_Version, Skin_UpdateDate, datenowS, force=False):	
	'''------------------------------
	---VARIABLES---------------------
	------------------------------'''
	name = 'setSkin_UpdateLog' ; printpoint = "" ; number2S = "" ; extra = "" ; TypeError = "" ; Skin_ShowLogN = ""
	datenowD = stringtodate(datenowS,'%Y-%m-%d')
	datedifferenceD = stringtodate(Skin_UpdateDate, '%Y-%m-%d')
	if "error" in [datenowD, datedifferenceD]: printpoint = printpoint + "9"
	try:
		number2 = datenowD - datedifferenceD
		number2S = str(number2)
		printpoint = printpoint + "2"
		'''---------------------------'''
	except Exception, TypeError:
		extra = extra + newline + 'TypeError' + space2 + str(TypeError)
		printpoint = printpoint + "9"
		'''---------------------------'''
	if (not "9" in printpoint or force == True) and xbmc.getSkinDir() == 'skin.featherence':
		printpoint = printpoint + "4"
		if "day," in number2S: number2S = number2S.replace(" day, 0:00:00","",1)
		elif "days," in number2S: number2S = number2S.replace(" days, 0:00:00","",1)
		else: number2S = "0"
		number2N = int(number2S)
		'''---------------------------'''
		if number2N == 0: header = '[COLOR=yellow]' + localize(31418) + space + localize(33006) + " - " + Skin_Version + '[/COLOR]'
		elif number2N == 1: header = '[COLOR=green]' + localize(31418) + space + addonString_servicefeatherence(32410).encode('utf-8') + " - " + Skin_Version + '[/COLOR]'
		elif number2N <= 7: header = '[COLOR=purple]' + localize(31418) + space + addonString_servicefeatherence(32411).encode('utf-8') + " - " + Skin_Version + '[/COLOR]'
		elif force == True: header = addonString(32091).encode('utf-8') + space + space5 + Skin_Version
		else: header = ""
		'''---------------------------'''
		skinlog_file = os.path.join(addons_path,'skin.featherence','changelog.txt')
		if os.path.exists(skinlog_file):
			printpoint = printpoint + "5"
			log = open(skinlog_file, 'r')
			message2 = log.read()
			log.close()
			message2S = str(message2)
			message3 = message2[70:8000]
			message3 = '"' + message3 + '"'
			message3S = str(message3)
			if header != "":
				printpoint = printpoint + "6"
				if number2N == 0 or xbmc.getCondVisibility('System.IdleTime(0)'):
					printpoint = printpoint + "7"
					try: Skin_ShowLogN = int(Skin_ShowLog2)
					except: Skin_ShowLogN = 7
					
					if Skin_ShowLog == 'true':
						printpoint = printpoint + "A"
						skin_showlog = xbmc.getInfoLabel('Skin.HasSetting(Skin_ShowLog)')
						if not skin_showlog:
							skin_showlog2 = xbmc.getInfoLabel('Skin.String(Skin_ShowLog2)')
							try:
								skin_showlog2 = int(skin_showlog2)
							except:
								skin_showlog2 = 1
								
							if number2N <= int(skin_showlog2):
								printpoint = printpoint + "B"
								if xbmc.getCondVisibility('Player.HasVideo'): xbmc.sleep(10000)
								diaogtextviewer(header, message2)
								'''---------------------------'''
		else: printpoint = printpoint + '9'
			
	setsetting('Skin_UpdateLog',"false")
	
	text = "Skin_Version" + space2 + str(Skin_Version) + newline + \
	"force" + space2 + str(force) + newline + \
	"datenowS" + space2 + str(datenowS) + newline + \
	"Skin_UpdateDate" + space2 + str(Skin_UpdateDate) + newline + \
	"Skin_UpdateLog" + space2 + str(Skin_UpdateLog) + newline + \
	"Skin_ShowLog" + space2 + str(Skin_ShowLog) + newline + \
	"Skin_ShowLog2" + space2 + str(Skin_ShowLog2) + newline + \
	"number2S" + space2 + str(number2S)
	'''---------------------------'''
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
