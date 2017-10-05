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
custom_emu = getsetting('custom_emu')
games_color2 = getsetting('Games_Color2')
OS = getsetting('OS')

Addon_ShowLog = getsetting('Addon_ShowLog')
Addon_ShowLog2 = getsetting('Addon_ShowLog2')
Addon_Update = getsetting('Addon_Update')
Addon_UpdateDate = getsetting('Addon_UpdateDate')
Addon_UpdateLog = getsetting('Addon_UpdateLog')
Addon_Version = getsetting('Addon_Version')

addonuserdata_path = os.path.join(addondata_path, addonID, '')

'''Emulator'''
core_updater_buildbot_url = ""
if systemplatformwindows:
	if getsetting('OS') != "":
		if getsetting('OS') == "win64":
			emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
			core_updater_buildbot_url = "http://buildbot.libretro.com/nightly/windows/x86_64/latest/"
		elif getsetting('OS') == "win32": emulator_path = os.path.join(addons_path, 'emulator.retroarch_win32', '')
		else: emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
	else: emulator_path = os.path.join(addons_path, 'emulator.retroarch_win64', '')
	
	emulator_file = os.path.join(emulator_path, 'retroarch.exe')
	emulator_file_ = '"' + emulator_file  + '"' + space + '-D'
	retroarchcfg_file = os.path.join(emulator_path, 'retroarch.cfg')
	retroarchcoreoptionscfg_file = os.path.join(emulator_path, '.retroarch-core-options.cfg')
	
elif systemplatformlinuxraspberrypi or OS == 'oe2':
	emulator_path = os.path.join(addons_path, 'emulator.tools.retroarch', '')
	
	emulator_file = os.path.join(emulator_path, 'bin', 'retroarch.sh')	
	emulator_file_ = '"' + emulator_file + '"'
	retroarchcfg_file = os.path.join(emulator_path, 'config', 'retroarch.cfg')
	retroarchcoreoptionscfg_file = os.path.join(emulator_path, '.retroarch-core-options.cfg')
	core_updater_buildbot_url = "http://buildbot.libretro.com/nightly/linux/x86_64/latest/"

elif systemplatformlinux and not systemplatformandroid:
	if getsetting('OS') == "i386": emulator_path = os.path.join(addons_path, 'emulator.retroarch_i386', '')
	else: emulator_path = os.path.join(addons_path, 'emulator.retroarch', '')
	
	emulator_file = os.path.join(emulator_path, 'bin', 'retroarch.sh')	
	emulator_file_ = '"' + emulator_file + '"'
	retroarchcfg_file = os.path.join(emulator_path, 'config', 'retroarch.cfg')
	retroarchcoreoptionscfg_file = os.path.join(emulator_path, '.retroarch-core-options.cfg')
	core_updater_buildbot_url = "http://buildbot.libretro.com/nightly/linux/x86_64/latest/"

elif systemplatformandroid:
	emulator_path = '/data/data/com.retroarch/'
	
	emulator_file = '/system/bin/am'
	emulator_file_ = '"' + emulator_file + '"'
	retroarchcfg_file = "/data/data/com.retroarch/retroarch.cfg"
	retroarchcoreoptionscfg_file = "/data/data/com.retroarch/.retroarch-core-options.cfg"
	
else:
	emulator_path = os.path.join(addons_path, 'emulator.retroarch', '')
	
	emulator_file = os.path.join(emulator_path, 'bin', 'retroarch.sh')	
	emulator_file_ = '"' + emulator_file + '"'
	retroarchcfg_file = os.path.join(emulator_path, 'config', 'retroarch.cfg')
	retroarchcoreoptionscfg_file = os.path.join(emulator_path, '.retroarch-core-options.cfg')
	
#subprocess.call("adb install path-to-file.apk ")

if systemplatformlinuxraspberrypi or OS == 'oe2': cores_path = os.path.join(emulator_path,'lib','libretro','')
elif systemplatformandroid: cores_path = os.path.join(emulator_path,'cores','')
else: cores_path = os.path.join(emulator_path,'cores','')

if systemplatformandroid: coresinfo_path = os.path.join(emulator_path,'info','')
else: coresinfo_path = cores_path

'''Featherence Emu Module'''
featherence_emu_module_path = os.path.join(addons_path, 'script.module.featherence.emu', '')
system_path = os.path.join(featherence_emu_module_path, 'system','')
if systemplatformandroid: shader_path = os.path.join(emulator_path,'shaders_glsl','')
else: shader_path = os.path.join(featherence_emu_module_path,'shaders','')
if systemplatformlinuxraspberrypi or OS == 'oe2': config_path2 = os.path.join(featherence_emu_module_path,'config2','')
else: config_path2 = os.path.join(featherence_emu_module_path,'config','')
'''New Version'''
content_database_path = os.path.join(featherence_emu_module_path,'database','')
cursor_directory_path = os.path.join(featherence_emu_module_path,'database','cursors','')
audio_filter_dir = os.path.join(featherence_emu_module_path,'filters','audio','')
video_filter_dir = os.path.join(featherence_emu_module_path,'filters','video','')

autoconfig_path2 = os.path.join(featherence_emu_module_path,'autoconfig','')
assets_directory = os.path.join(featherence_emu_module_path,'assets','')
dynamic_wallpapers_directory = os.path.join(featherence_emu_module_path,'assets','wallpapers','')
overlay_directory = os.path.join(featherence_emu_module_path,'overlay','')

'''Emulator userdata'''
emulatordata_path = os.path.join(addondata_path, 'emulator.retroarch', '')
retroarchcfg_file2 = os.path.join(emulatordata_path, 'config', 'retroarch.cfg')
retroarchcoreoptionscfg_file2 = os.path.join(emulatordata_path, 'config', '.retroarch-core-options.cfg')
rom_path = os.path.join(emulatordata_path,'rom','')
config_path = os.path.join(emulatordata_path,'config','')

save_path = os.path.join(emulatordata_path,'save','')
savestate_path = os.path.join(emulatordata_path,'save','savestate', '')
autoconfig_path = os.path.join(emulatordata_path,'autoconfig','')
emukeymaps_path = os.path.join(addonPath,'resources','keymaps','')
emukeymaps2_path = os.path.join(addonPath,'resources','keymaps2','')
emumedia_path = os.path.join(addonPath,'resources','media','')
screenshots_path = os.path.join(emulatordata_path,'screenshots','')
cheats_path = os.path.join(emulatordata_path,'cheats','')
dirsL = [save_path, savestate_path, autoconfig_path, screenshots_path, cheats_path, rom_path]

'''New Version'''
input_remapping_directory_path = os.path.join(emulatordata_path,'remaps','')
core_assets_directory = os.path.join(emulatordata_path,'downloads','')

'''Featherence Emu'''
emulanuncher_file = os.path.join(addonPath,'resources','launchers','launchers.xml')
emudata_launcher_file = os.path.join(addonuserdata_path + 'launchers.xml')

launcher_args = '--config' + space + os.path.join(emulator_path, 'retroarch.cfg') + space + '--appendconfig' + space + os.path.join(config_path, 'retroarch.cfg')
if systemplatformwindows:
	lib_args = launcher_args + space + '-L' + space + cores_path
elif systemplatformandroid:
	lib_args = launcher_args + space + '-e CONFIGFILE /data/data/com.retroarch/retroarch.cfg -e IME tv.ouya.console.ime.keyboard/.OUYAKeyboard -n com.retroarch/.browser.retroactivity.RetroActivityFuture'
else:
	lib_args = ""


optionsL = [] ; options_L = []
video_black_frame_insertion = getsetting('video_black_frame_insertion') ; optionsL.append('video_black_frame_insertion') ; options_L.append('false')
video_refresh_rate =getsetting('video_refresh_rate') ; optionsL.append('video_refresh_rate') ; options_L.append('59.950001')
video_hard_sync =getsetting('video_hard_sync') ; optionsL.append('video_hard_sync') ; options_L.append('false')
video_hard_sync_frames =getsetting('video_hard_sync_frames') ; optionsL.append('video_hard_sync_frames') ; options_L.append('*')
video_threaded =getsetting('video_threaded') ; optionsL.append('video_threaded') ; options_L.append('*')
video_smooth =getsetting('video_smooth') ; optionsL.append('video_smooth') ; options_L.append('true')
video_vsync =getsetting('video_vsync') ; optionsL.append('video_vsync') ; options_L.append('true')
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
elif systemplatformlinuxraspberrypi or OS == 'oe2': options_L.append('sdl')
elif systemplatformlinux: options_L.append('alsathread') #alsathread
else: options_L.append('')

video_driver =getsetting('video_driver') ; optionsL.append('video_driver')
if systemplatformwindows: options_L.append('gl')
elif systemplatformlinuxraspberrypi or OS == 'oe2': options_L.append('gl')
elif systemplatformlinux: options_L.append('gl')
else: options_L.append('')


audio_volume =getsetting('')
optionsL.append('audio_volume') ; options_L.append('*')

staticL = [] ; static_L = []
staticL.append('libretro_path') ; static_L.append(cores_path)
staticL.append('libretro_directory') ; static_L.append(cores_path)
staticL.append('libretro_info_path') ; static_L.append(coresinfo_path)
staticL.append('system_directory') ; static_L.append(system_path)
staticL.append('content_database_path') ; static_L.append(content_database_path)
staticL.append('cursor_directory') ; static_L.append(cursor_directory_path)
staticL.append('input_remapping_directory') ; static_L.append(input_remapping_directory_path)
staticL.append('video_filter_dir') ; static_L.append(video_filter_dir)
staticL.append('audio_filter_dir') ; static_L.append(audio_filter_dir)
staticL.append('core_assets_directory') ; static_L.append(core_assets_directory)
staticL.append('assets_directory') ; static_L.append(assets_directory)
staticL.append('dynamic_wallpapers_directory') ; static_L.append(dynamic_wallpapers_directory)
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
staticL.append('overlay_directory') ; static_L.append(overlay_directory)

staticL.append('core_updater_buildbot_url') ; static_L.append(core_updater_buildbot_url)

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
elif systemplatformlinuxraspberrypi or OS == 'oe2': options_L.append('sdl')
else:
	static_L.append('linuxraw')

filter_games =getsetting('filter_games')
delete_games =getsetting('delete_games')
download1L = ['Arcade', 'Sony Playstation']

emu_startup = xbmc.getInfoLabel('Window(home).Property(emu_startup)')

if emu_startup == "" or Addon_Version != addonVersion or Addon_Update == "true":
	from modules import startup
	startup()