# -*- coding: utf-8 -*-

'''------------------------------
---shared_variables--------------
------------------------------'''
import xbmc, xbmcgui, xbmcaddon, sys, os

addon = 'script.featherence.service'
if not xbmc.getCondVisibility('System.HasAddon('+ addon +')'):
	printpoint = "" ; count = 0
	dialogyesnoW = xbmc.getCondVisibility('Window.IsVisible(DialogYesNo.xml)')
	dialogprogressW = xbmc.getCondVisibility('Window.IsVisible(DialogProgress.xml)')
	if not dialogyesnoW and not dialogprogressW:
		printpoint = printpoint + "1"
		xbmc.executebuiltin('Notification(Required addon is missing!,'+addon+',4000)')
		xbmc.executebuiltin('ActivateWindow(10025,plugin://'+ addon +'),returned') ; xbmc.sleep(2000)
		'''---------------------------'''
		dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
		while count < 10 and (not xbmc.getCondVisibility('System.HasAddon('+ addon +')') or dialogbusyW) and not xbmc.abortRequested:
			if count == 0: printpoint = printpoint + "2"
			count += 1
			if xbmc.getCondVisibility('System.HasAddon('+ addon +')'): xbmc.executebuiltin('Dialog.Close(busydialog)')
			xbmc.sleep(500)
			dialogbusyW = xbmc.getCondVisibility('Window.IsVisible(DialogBusy.xml)')
			xbmc.sleep(500)
			'''---------------------------'''
		if count < 10:
			printpoint = printpoint + "7"
			xbmc.executebuiltin('Action(Back)') ; xbmc.executebuiltin('Action(Back)') ; xbmc.sleep(1000)
			xbmc.executebuiltin('Notification(Required addon installed!,Try again!,4000)')
			'''---------------------------'''
		else: printpoint = printpoint + "9"
		
	else: printpoint = printpoint + "8"
	
	print 'script.featherence.service_install_LV' + printpoint + " count: " + str(count)
	sys.exit(1)
else:
	servicehtptPath          = xbmcaddon.Addon('script.featherence.service').getAddonInfo("path")
	sharedlibDir = os.path.join(servicehtptPath, 'resources', 'lib', 'shared')
	sys.path.insert(0, sharedlibDir)
	try:
		from shared_variables import *
		from shared_variables3 import *
		'''---------------------------'''
	except Exception, TypeError:
		xbmc.executebuiltin('Notification(FEATHERENCE SERVICE ADDON ERROR, Solution: Reinstall the addon, 2000)')
		print 'TypeError: ' + str(TypeError)
		sys.exit(1)
		
templates2_path = os.path.join(addonPath, 'resources', 'templates2', '')
General_OnlyPopular = getsetting('General_OnlyPopular')
'''---------------------------'''
Custom_10001 = getsetting('Custom_10001')
Custom_10002 = getsetting('Custom_10002')
Custom_10003 = getsetting('Custom_10003')
Custom_10004 = getsetting('Custom_10004')
Custom_10005 = getsetting('Custom_10005')
Custom_10006 = getsetting('Custom_10006')
Custom_10007 = getsetting('Custom_10007')
Custom_10008 = getsetting('Custom_10008')
Custom_10009 = getsetting('Custom_10009')
'''---------------------------'''
commonsearch101 = "שיר"
commonsearch102 = "קריוקי"
commonsearch104 = "הופעה חיה"
commonsearch106 = "שיר מזרחי"
commonsearch107 = "קריוקי מזרחי"
commonsearch108 = ""
commonsearch109 = "הופעה חיה מזרחי"
commonsearch111 = "songs video"
commonsearch112 = "Karaoke"
commonsearch114 = "LiveShow"
sefilter = ['עונת ההופעות']