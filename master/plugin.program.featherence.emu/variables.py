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

getsetting         = xbmcaddon.Addon().getSetting
setsetting         = xbmcaddon.Addon().setSetting
addonName          = xbmcaddon.Addon().getAddonInfo("name")
addonString        = xbmcaddon.Addon().getLocalizedString
addonID          = xbmcaddon.Addon().getAddonInfo("id")
addonPath          = xbmcaddon.Addon().getAddonInfo("path")
addonVersion          = xbmcaddon.Addon().getAddonInfo("version")

printfirst = addonName + ": !@# "
'''---------------------------'''

show_adult = getsetting('show_adult')
OS = getsetting('OS')
addonuserdata_path = os.path.join(addondata_path, addonID, '')

'''Emulator'''
if systemplatformwindows:
	if getsetting('OS') != "":
		if getsetting('OS') == "win64": emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
		elif getsetting('OS') == "win32": emulator_path = os.path.join(addons_path, 'emulator.retroarch_win32', '')
		else: emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
	else: emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
	
	emulator_file = os.path.join(emulator_path, 'retroarch.exe')
	emulator_file_ = emulator_file + space + '-D'
	retroarchcfg_file = os.path.join(emulator_path, 'retroarch.cfg')
	
elif systemplatformlinuxraspberrypi:
	emulator_path = os.path.join(addons_path, 'emulator.tool.retroarch', '')
	
	emulator_file = os.path.join(emulator_path, 'bin', 'retroarch.sh')	
	emulator_file_ = emulator_file
	retroarchcfg_file = os.path.join(emulator_path, 'config', 'retroarch.cfg')
	
else:
	emulator_path = os.path.join(addons_path, 'emulator.retroarch', '')
	
	emulator_file = os.path.join(emulator_path, 'bin', 'retroarch.sh')	
	emulator_file_ = emulator_file
	retroarchcfg_file = os.path.join(emulator_path, 'config', 'retroarch.cfg')
	
#subprocess.call("adb install path-to-file.apk ")

cores_path = os.path.join(emulator_path,'cores','')	
coresinfo_path = cores_path

'''Featherence Emu Module'''
featherence_emu_module_path = os.path.join(addons_path, 'script.module.featherence.emu', '')
system_path = os.path.join(featherence_emu_module_path, 'system','')
shader_path = os.path.join(featherence_emu_module_path,'shaders','')
config_path2 = os.path.join(featherence_emu_module_path,'config','')

'''Emulator userdata'''
emulatordata_path = os.path.join(addondata_path, 'emulator.retroarch', '')
retroarchcfg_file2 = os.path.join(emulatordata_path, 'config', 'retroarch.cfg')
rom_path = os.path.join(emulatordata_path,'rom','')
config_path = os.path.join(emulatordata_path,'config','')

save_path = os.path.join(emulatordata_path,'save','')
savestate_path = os.path.join(emulatordata_path,'save','savestate', '')
autoconfig_path = os.path.join(emulatordata_path,'autoconfig','')
emukeymaps_path = os.path.join(addonPath,'resources','keymaps','')
emumedia_path = os.path.join(addonPath,'resources','media','')
screenshots_path = os.path.join(emulatordata_path,'screenshots','')
cheats_path = os.path.join(emulatordata_path,'cheats','')
dirsL = [save_path, savestate_path, autoconfig_path, screenshots_path, cheats_path, rom_path]

'''Featherence Emu'''
emulanuncher_file = os.path.join(addonPath,'resources','launchers','launchers.xml')
emudata_launcher_file = os.path.join(addonuserdata_path + 'launchers.xml')

launcher_args = '--config' + space + os.path.join(emulator_path, 'retroarch.cfg') + space + '--appendconfig' + space + os.path.join(config_path, 'retroarch.cfg')
if systemplatformwindows:
	lib_args = launcher_args + space + '-L' + space + os.path.join(emulator_path, 'cores','')
else:
	lib_args = ""


optionsL = [] ; options_L = []
video_black_frame_insertion = getsetting('video_black_frame_insertion') ; optionsL.append('video_black_frame_insertion') ; options_L.append('false')
video_refresh_rate =getsetting('video_refresh_rate') ; optionsL.append('video_refresh_rate') ; options_L.append('59.950001')
video_smooth =getsetting('video_smooth') ; optionsL.append('video_smooth') ; options_L.append('true')
audio_device =getsetting('audio_device') ; optionsL.append('audio_device')
if systemplatformwindows: options_L.append('')
elif systemplatformlinux: options_L.append('hw:0,3')
else: options_L.append('')
audio_latency =getsetting('audio_latency') ; optionsL.append('audio_latency') ; options_L.append('*')
audio_out_rate =getsetting('audio_out_rate') ; optionsL.append('audio_out_rate') ; options_L.append('*')
audio_sync =getsetting('audio_sync') ; optionsL.append('audio_sync') ; options_L.append('*')
audio_volume =getsetting('audio_volume') ; optionsL.append('audio_volume') ; options_L.append('*')
input_enable_hotkey =getsetting('input_enable_hotkey') ; optionsL.append('input_enable_hotkey') ; options_L.append('ctrl')

audio_driver =getsetting('audio_driver') ; optionsL.append('audio_driver')
if systemplatformwindows: options_L.append('dsound')
elif systemplatformlinux: options_L.append('alsathread') #alsathread

video_driver =getsetting('video_driver') ; optionsL.append('video_driver')
if systemplatformwindows: options_L.append('gl')
elif systemplatformlinux: options_L.append('gl')


audio_volume =getsetting('')
optionsL.append('audio_volume') ; options_L.append('*')

staticL = [] ; static_L = []
staticL.append('libretro_path') ; static_L.append(cores_path)
staticL.append('libretro_info_path') ; static_L.append(coresinfo_path)
staticL.append('system_directory') ; static_L.append(system_path) 
staticL.append('rgui_config_directory') ; static_L.append(config_path)
staticL.append('video_shader_dir') ; static_L.append(shader_path)
staticL.append('video_shader') ; static_L.append(os.path.join(shader_path, '*','') + '.{cg,cgp,shader}')

staticL.append('joypad_autoconfig_dir') ; static_L.append(autoconfig_path)
staticL.append('screenshot_directory'); static_L.append(screenshots_path)
staticL.append('cheat_database_path') ; static_L.append(cheats_path)
staticL.append('savefile_directory') ; static_L.append(save_path)
staticL.append('savestate_directory') ; static_L.append(savestate_path)
staticL.append('content_directory') ; static_L.append(rom_path)
staticL.append('rgui_browser_directory') ; static_L.append(rom_path)
staticL.append('overlay_directory') ; static_L.append(config_path)

staticL.append('config_save_on_exit') ; static_L.append('true')
staticL.append('fps_show') ; static_L.append('false')
staticL.append('core_specific_config')
if systemplatformwindows:
	static_L.append('false')
else:
	static_L.append('true')
staticL.append('libretro_log_level') ; static_L.append('0')
staticL.append('input_autodetect_enable') ; static_L.append('true')
staticL.append('input_driver')
if systemplatformwindows:
	static_L.append('dinput')
else:
	static_L.append('linuxraw')

filter_games =getsetting('filter_games')
delete_games =getsetting('delete_games')
download1L = ['Arcade', 'Sony Playstation']

emu_startup = xbmc.getInfoLabel('Window(home).Property(emu_startup)')

if emu_startup == "" or 1 + 1 == 3:
	from modules import startup
	startup()