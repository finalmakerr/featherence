import xbmc, xbmcgui, xbmcaddon
import os, sys

from variables import *
from modules2 import *
from shared_variables import *
from shared_modules import *

def del_game(plugin, category, launcher, rom, filename, filepath):
	name = 'del_game' ; printpoint = ""
	if not os.path.exists(os.path.join(filepath)):
		printpoint = printpoint + '9'
		notification('Error!','Invalid Path','',2000)
	else:
		returned = dialogyesno(addonString(30102).encode('utf-8') % (filename), addonString(30103).encode('utf-8'))
		if returned == 'ok':
			removefiles(filepath, filteroff=[], dialogprogress="")
			notification('ROM Deleted!', filename, "", 2000)
			xbmc.executebuiltin('Container.Refresh')
			
	text = "category" + space2 + str(category) + newline + \
	"launcher" + space2 + str(launcher) + newline + \
	"rom" + space2 + str(rom) + newline + \
	"filename" + space2 + str(filename) + newline + \
	"filepath" + space2 + str(filepath) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def testme():
	notification('Featherence Emu Console addon is missing!',"Manual download from addon settings","",4000)
def startup():
	name = 'startup' ; printpoint = "" ; VerReset = "" ; value = False
	
	setProperty('emu_startup', 'true', type="home")
	
	from shared_modules3 import checkAddon_Update
	checkAddon_Update("", Addon_Update, Addon_Version, addonVersion, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2, VerReset)
	
	if Addon_UpdateLog == "true":
		list = []
		list.append(addonString_servicefeatherence(32060).encode('utf-8')) #Would you like thanks us? Would love to hear you!
		list.append(addonString_servicefeatherence(32061).encode('utf-8')) #Do you want to contribute?
		list.append(addonString_servicefeatherence(32062).encode('utf-8')) #Having fun yet ;)
		list.append(addonString_servicefeatherence(32063).encode('utf-8')) #Looking for support?
		list.append(addonString_servicefeatherence(32064).encode('utf-8')) #Having a question?
		returned, value = getRandom(0, min=0, max=len(list), percent=50)
		
		notification(list[int(value)],'YouPlay Nostalgia','',4000)
	
	mkdirs()
	chmod()
	copydreamcastmem(force=False)
	
	if Addon_Update == "true":
		notification("Received new update!","Check YouPlay Nostalgia for support","",4000)
		value = True
	
	copylaunchers(force=value)
	copycores(force=value)
	copyarcade(force=value)
	resolution_check()
	if custom_emu != 'true': copyconfig(force=value)
	else: copyconfig(force=False)
	
	
	installemuconsole(force=value)
	
	text = "Force" + space2 + str(value) + newline + \
	'Addon_Update' + space2 + str(Addon_Update) + newline + \
	'emu_startup' + space2 + str(emu_startup) + newline + \
	'Addon_Version' + space2 + str(Addon_Version) + newline + \
	'addonVersion' + space2 + str(addonVersion) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def chmod():
	if systemplatformlinux:
		os.system('chmod +x '+ emulator_path +'bin/*')
		os.system("export LD_LIBRARY_PATH='"+ emulator_path +"lib/'")

def resolution_check():
	if systemplatformlinux:
		output = terminal('xrandr| grep -e "1920x1080"')
		if "1920x1080" in output:
			if not "59.94*" in output:
				if resolution_force != 'true': notification("Refresh Rate isn't 59.94!",'You should enable resoultion check option in the addon settings!','',2000)
				else:
					output2 = terminal("xrandr | awk '/connected/{print $1$2}'")
					output2 = output2.split('\n')
					for line in output2:
						if "disconnected" in line: continue
						else:
							device = line.replace("connected","")
							device = device.replace(" ","")
							notification('Setting Refresh Rate to 59.94!','Device found!' + space + str(device),'',3000)
							terminal('xrandr --output '+device+' --mode 1920x1080 -r 59.94')
				

def searchtrailer(filename):
	from shared_modules3 import *
	name = filename ; url = filename ; desc = "" ; num = "" ; viewtype = ""
	YoutubeSearch(name, url, desc, num, viewtype)
	
def copyarcade(force=False):
	name = 'copyarcade' ; printpoint = ""
	path = os.path.join(rom_path, 'Arcade', '')
	if (not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'cfg', '')) or force==True) and os.path.exists(os.path.join(featherence_emu_module_path,'save','mame', 'cfg', '')):
		printpoint = printpoint + '1'
		notification('copying Arcade CFG','','',2000)
		source = os.path.join(featherence_emu_module_path,'save', 'mame')
		target = os.path.join(emulatordata_path,'save', 'MAME 2014', 'mame')
		copyfiles(source, target)
	elif not os.path.exists(path): printpoint = printpoint + '8'
	elif not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'diff', '')) or not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'nvram', '')):
		printpoint = printpoint + '2'
		downloads2('nvram_diff.zip', os.path.join(emulatordata_path,'save', 'MAME 2014', 'mame'))
	
	text = "force" + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def copydolphin(force=False):
	name = 'copydolphin' ; printpoint = ""
	path1 = os.path.join(save_path, 'dolphin-emu', 'User', 'Config', '')
	path2 = os.path.join(system_path, 'dolphin-emu', '')
	if (not os.path.exists(os.path.join(path1)) or force==True) and os.path.exists(os.path.join(featherence_emu_module_path,'save','dolphin-emu', 'User', '')):
		printpoint = printpoint + '1'
		notification('copying to save/dolphin-emu','','',2000)
		source = os.path.join(featherence_emu_module_path,'save', 'dolphin-emu')
		target = os.path.join(emulatordata_path,'save', 'dolphin-emu')
		copyfiles(source, target)
	if (not os.path.exists(path2) or force==True) and os.path.exists(os.path.join(featherence_emu_module_path,'system','dolphin-emu', 'Sys', '')):
		printpoint = printpoint + '2'
		notification('copying to system/dolphin-emu','','',2000)
		source = os.path.join(featherence_emu_module_path,'system', 'dolphin-emu')
		target = os.path.join(emulatordata_path,'system', 'dolphin-emu')
		copyfiles(source, target)
	
	text = "force" + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def copycores(force=False):
	name = 'copycores' ; printpoint = "" ; i = 0
	path = os.path.join(emulator_path, 'cores', '')
	for file in os.listdir(cores_path):
		i = i+1
	if not os.path.exists(cores_path) and os.path.exists(path) or i < 200 :
		printpoint = printpoint + '1'
		notification('copying cores','','',2000)
		source = os.path.join(path)
		target = os.path.join(cores_path)
		copyfiles(source, target)
	text = "force" + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
	
	
def installemuconsole(force=False):
	name = 'installemuconsole' ; printpoint = "" ; text = "" ; extra = ""
	if force == True:
		if os.path.exists(emulator_path): notification('Emulator already exists!',emulator_path,"",7000)
	if systemplatformwindows and OS == 'win32': installaddon('emulator.retroarch_win32', update=True)
	elif systemplatformwindows: installaddon('emulator.retroarch_win64', update=True)
	elif systemplatformlinuxraspberrypi: installaddon('emulator.tools.retroarch', update=True)
	elif systemplatformandroid:
		installaddon('emulator.retroarch_android', update=True)
		if OS == 'armv7': subprocess.call("adb RetroArch-armv7-v1.0.0.2-r34.apk ")
		else: subprocess.call("adb RetroArch-x86-v1.0.0.2-r35.apk ")
	elif systemplatformlinux and not systemplatformandroid:
		if OS == 'i386': installaddon('emulator.retroarch_i386', update=True)
		elif OS == 'oe2': installaddon('emulator.tools.retroarch', update=True)
		else: installaddon('emulator.retroarch', update=True)
	else:
		printpoint = printpoint + '6'
		notification(addonString_servicefeatherence(32045).encode('utf-8'),"","YouPlay Nostalgia",2000) #OS and hardware are not supported!
	
	installaddonP('script.module.featherence.emu', update=True)
	copyingtestgames(force=force)
	
	if not os.path.exists(emulator_path) and not '6' in printpoint: notification('Featherence Emu Console addon is missing!',"Manual download from addon settings","",4000)
	text = "extra" + space2 + str(extra) + newline + \
	'force' + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
	
def copyingtestgames(force=False):
	name = 'copyingtestgames' ; printpoint = "" ; text = "" ; extra = "" ; x = ""
	
	if os.path.exists(roms_dir):
		printpoint = printpoint + '1'
		for x in rom_testL:
			if not os.path.exists(x):
				printpoint = printpoint + '2'
				notification(addonString_servicefeatherence(32051).encode('utf-8') + '...',addonString_servicefeatherence(32052).encode('utf-8') + '!',"",4000) #Getting a few games for you, Goodluck running them
				copyfiles(roms_dir, rom_path)
				break
			continue
		
		
	else:
		printpoint = printpoint + '9'
	
	text = "extra" + space2 + str(extra) + newline + \
	'force' + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def runtestgames(force=False):
	name = 'runtestgames' ; printpoint = "" ; text = "" ; extra = "" ; x = "" ; launcherID = "" ; romName = "" ; roms_test_path = "" ; returned = "" ; value = ""
	xbmc.executebuiltin('ActivateWindow(busydialog)')
	xbmc.executebuiltin('AlarmClock(busydialog,Dialog.Close(busydialog),00:03,silent)')
	list = ['-> (Exit)','1.Arcade','2.DOS','3.Nintendo','4.Sega Genesis','5.Super Nintendo'] #ID
	returned, value = dialogselect(addonString_servicefeatherence(32423).encode('utf-8'),list,0)
	
	if returned == -1: printpoint = printpoint + "9"
	elif returned == 0: printpoint = printpoint + "8"
	else: printpoint = printpoint + "7"
	
	if "7" in printpoint:
		notification(addonString_servicefeatherence(32165).encode('utf-8'),value,"",3000) #Running a test game
		if returned == 1: roms_test_path = roms_test_1 ; launcherID = roms_test_1_launcherID ; romName = roms_test_1_romName
		elif returned == 2: roms_test_path = roms_test_2 ; launcherID = roms_test_2_launcherID ; romName = roms_test_2_romName
		elif returned == 3: roms_test_path = roms_test_3 ; launcherID = roms_test_3_launcherID ; romName = roms_test_3_romName
		elif returned == 4: roms_test_path = roms_test_4 ; launcherID = roms_test_4_launcherID ; romName = roms_test_4_romName
		elif returned == 5: roms_test_path = roms_test_5 ; launcherID = roms_test_5_launcherID ; romName = roms_test_5_romName
		elif returned == 6: roms_test_path = roms_test_6 ; launcherID = roms_test_6_launcherID ; romName = roms_test_6_romName
	text = "extra" + space2 + str(extra) + newline + \
	"returned" + space2 + str(returned) + space + "value" + space2 + str(value) + newline + \
	"roms_test_path" + space2 + str(roms_test_path) + space + "launcherID" + space2 + str(launcherID) + space + "romName" + space2 + str(romName) + newline + \
	'force' + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
	
	return launcherID, romName
	
def copyconfig(force=False):
	name = 'copysettings' ; printpoint = "" ; extra = ""
	
	path = config_path2
	if not os.path.exists(path) or force==True:
		printpoint = printpoint + '1'
		installemuconsole()
	elif systemplatformlinux and not systemplatformandroid:
		printpoint = printpoint + '2'
		for file in os.listdir(path):
			y = False
			if file =='retroarch-core-options.cfg' or file == 'retroarch.cfg': y = True
			if os.path.isdir(os.path.join(path,file)):
				extra = extra + newline + str(os.path.join(config_path, file)) + space2 + 'IsDir!!'
				continue
			else: x = os.path.join(config_path, file)
			if not os.path.exists(x) or force == True:
				printpoint = printpoint + 'c'
				extra = extra + newline + 'copyfiles from: ' + str(os.path.join(path,file)) + ' To: ' + str(x)
				copyfiles(os.path.join(path,file), x)
				if y == True: copyfiles(os.path.join(path,file), os.path.join(storageconfig_path,'retroarch',file))
			
			if not os.path.exists(system_path) or force==True:
				copyfiles(os.path.join(featherence_emu_module_path,"system"), system_path)
		if not os.path.exists(config_path) or force==True:
			printpoint = printpoint + '3'
			notification('Recreating configs','','',1000)
			mkdirs()
			setconfig(force=True)
		if (not os.path.exists(remaps_path) or force==True) and os.path.exists(remaps_path2):
			printpoint = printpoint + '4'
			notification('copying remaps','','',1000)
			copyfiles(remaps_path2, remaps_path)
		
		copydolphin(force)
	elif force==True and systemplatformwindows:
		pass
		notification('setconfig Win','','',1000)
		setconfig(force=True)
	
	
	text = "extra" + space2 + str(extra) + newline + \
	'os.listdir(path)' + space2 + str(os.listdir(path)) + newline + \
	'force' + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")
	
def copyautoconfig(force=False):
	name = 'copyautoconfig' ; printpoint = "" ; returned = 'ok'
	
	try: autoconfig_path2_ = os.listdir(autoconfig_path2)
	except: autoconfig_path2_ = "" ; printpoint = printpoint + '9' ; notification("Error! Folder not found!",str(autoconfig_path2),"",4000)

	if not '9' in printpoint:
		
		if force == True: returned = dialogyesno('Would you like to continue?','This action will overwrite your current related files!')
		else: returned = 'ok'

		if returned == 'ok':
			copyfiles(autoconfig_path2, autoconfig_path)
			if force == True:
				header = 'Joysticks in-game keys (autoconfig)'
				message = str(autoconfig_path2_)
				message = message.replace("u'","")
				message = message.replace("'","")
				message = message.replace(",","[CR]")
				xbmc.executebuiltin('RunScript(script.featherence.service,,?mode=31&value='+header+'&value2='+message+')')
	
	text = "autoconfig_path2" + space2 + str(autoconfig_path2) + newline + \
	"autoconfig_path2_" + space2 + str(autoconfig_path2_) + newline + \
	"autoconfig_path" + space2 + str(autoconfig_path) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def keys_help(filename):
	from shared_modules3 import *
	name = 'keys_help' ; printpoint = "" ; url = ""
	if filename != '..': url = '&youtube_id=b3NE_vZUVCo'
	name_ = filename ; mode = 4 ; iconimage = "" ; desc = "" ; num = "" ; viewtype = "" ; fanart = ""
	if '9' in printpoint:
		pass
	else:
		PlayVideos(name_, mode, url, iconimage, desc, num, fanart)
	
	text = "filename" + space2 + str(filename)
	printlog(title=name, printpoint=printpoint, text=text, level=1, option="")

def copykeymaps():
	filename_ = ""
	returned = dialogyesno('Would you like to continue?','This action will overwrite your current related files!')
	if returned == 'ok':
		keymaps_path = os.path.join(userdata_path, 'keymaps', '')
		copyfiles(emukeymaps_path, keymaps_path)
		
		keymaps2_path = os.path.join(userdata_path, 'addon_data', 'peripheral.joystick', 'resources', 'buttonmaps', 'xml', '')
		if os.path.exists(keymaps2_path) and 1 + 1 == 3:
			copyfiles(emukeymaps2_path, keymaps2_path)
			for file in os.listdir(emukeymaps2_path):
				filename = os.path.basename(file)
				filename_ = filename_ + ', ' + filename
		
		xbmc.executebuiltin('Action(reloadkeymaps)')
				
		for file in os.listdir(emukeymaps_path):
			filename = os.path.basename(file)
			filename_ = filename_ + ', ' + filename
		
		
		dialogok('Keymaps copied!', filename_, '', '')
	
def setconfig(force=False):
	name = 'setconfig' ; printpoint = "" ; extra = ""
	dp = xbmcgui.DialogProgress()
	dp.create('setup consoles configuration files',"","")
	if os.path.exists(config_path):
		printpoint = printpoint + '1'
		notification('set configs','','',1000)
		
		i = 0
		progress_ = 0
		dp_total = len(os.listdir(config_path))
		for file in os.listdir(config_path):
			if not ".cfg" in file or "core" in file:
				continue
			progress_ = i * 90 / dp_total
			dp.update(progress_,str(file)," ")
			
			extra = extra + newline + str(i) + space2 + str(file)
			infile_ = read_from_file(to_utf8(config_path) + to_utf8(file), silent=True, lines=False, retry=True, createlist=True, printpoint="", addlines="")
			
			i2 = 0
			for x in optionsL:
				dp.update(progress_+ (i2 / 2),str(file),str(x))
				extra = extra + newline + str(i2) + space2 + 'x' + space2 + str(x)
				z = getsetting(x)
				z2 = options_L[i2]
				#if z2 == "": printpoint = printpoint + 'c' ; continue
				if force == True and z2 != '*': z = z2
				elif z == "" and z2 == '*':
					extra = extra + space + 'pass' ; i2 += 1 ; continue
					
				from_string = x + ' = "'
				to_string = '\n'
				y = regex_from_to(infile_, from_string, to_string, excluding=True)
				if y != z:
					replace_word(to_utf8(config_path) + to_utf8(file),from_string + to_utf8(y),from_string + to_utf8(z) + '"', infile_="", LineR=False , LineClean=False)
					if file == 'retroarch.cfg' and x == 'audio_device' and systemplatformlinux and not systemplatformandroid:
						extra = extra + newline + 'ad_' + space2
						'''need to test!'''
						infile = os.path.join(emumedia_path, 'asound.conf')
						copyfiles(infile, '/storage/.config/') ; xbmc.sleep(100)
						
						if os.path.exists(infile):
							ad = regex_from_to(infile, 'pcm "', '"', excluding=True)
							extra = extra + ad
							#replace_word(infile,ad,z, infile_="", LineR=False , LineClean=False)
					
					elif file == 'retroarch.cfg' and systemplatformwindows:
						extra = extra + newline + 'retroarch.cfg' + space2
						#copyfiles(retroarchcfg_file2, retroarchcfg_file) ; xbmc.sleep(100)
					
					elif file == '.retroarch-core-options.cfg' and systemplatformwindows:
						extra = extra + newline + '.retroarch-core-options.cfg' + space2
						#copyfiles(retroarchcoreoptionscfg_file2, retroarchcoreoptionscfg_file) ; xbmc.sleep(100)
					
				extra = extra + space + 'y' + space2 + str(y) + space + 'z' + space2 + str(z) + space + 'z2' + space2 + str(z2)
				
				i2 += 1
			
			
			i += 1
	
	
	dp.update(95,"dolphin_ini..", "...")
	if os.path.exists(dolphin_ini_file):
		replace_word(dolphin_ini_file,'SIDevice1 = 0','SIDevice1 = 6', infile_="", LineR=False , LineClean=False)
		replace_word(dolphin_ini_file,'SIDevice2 = 0','SIDevice2 = 6', infile_="", LineR=False , LineClean=False)
		replace_word(dolphin_ini_file,'SIDevice3 = 0','SIDevice3 = 6', infile_="", LineR=False , LineClean=False)
	
	dp.update(96,"staticconfig..", "...")
	staticconfig(force=True)
	dp.update(98,"retroarch.cfg..", "...")

	if systemplatformandroid: pass
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		x = 'retroarch.cfg'
		copyfiles(os.path.join(config_path,x), '/storage/.config/retroarch/')
		x = '.retroarch-core-options.cfg'
		copyfiles(os.path.join(config_path,x), '/storage/.config/retroarch/')
		if os.path.exists('/storage/.kodi/addons/script.module.featherence.emu/assets/xmb/monochrome/font.ttf'):
			copyfiles('/storage/.kodi/addons/script.module.featherence.emu/assets/xmb/monochrome/font.ttf','/storage/.config/retroarch/assets/xmb/monochrome/font.ttf')
	elif systemplatformwindows:
		if os.path.exists('/storage/.kodi/addons/script.module.featherence.emu/assets/xmb/monochrome/font.ttf'):
			copyfiles('/storage/.kodi/addons/script.module.featherence.emu/assets/xmb/monochrome/font.ttf','~/.kodi/userdata/addon_data/emulator.retroarch/assets/xmb/monochrome/font.ttf')
	
	dp.update(100,"Finishing Configuration...", "") ; xbmc.sleep(200) ; dp.close

	text = 'force' + space2 + str(force) + newline + \
	"extra" + space2 + str(extra)
	printlog(title=name, printpoint=printpoint, text=text, level=7, option="")

def staticconfig(force=True):
	name = 'staticconfig' ; printpoint = "" ; extra = ""
	
	if os.path.exists(config_path):
		printpoint = printpoint + '1'
		
		i = 0
		for file in os.listdir(config_path):
			extra = extra + newline + str(i) + space2 + str(file)
			infile_ = read_from_file(to_utf8(config_path) + to_utf8(file), silent=True, lines=False, retry=True, createlist=True, printpoint="", addlines="")
			
			i2 = 0
			for x in staticL:
				extra = extra + newline + str(i2) + space2 + 'x' + space2 + str(x)
				
				z = static_L[i2]
				from_string = x + ' = "'
				to_string = '"'
				y = regex_from_to(infile_, from_string, to_string, excluding=True)
				
				if y != z and y != "":
					if '"' in y: y = ""
					replace_word(config_path + file,from_string + str(y) + to_string,from_string + str(z) + to_string, infile_="", LineR=False , LineClean=False)
						
				extra = extra + space + 'y' + space2 + str(y) + space + 'y_len' + space2 + str(len(y)) + space + 'z' + space2 + str(z)
				
				i2 += 1
			
			
			i += 1
		
		
		infile_ = read_from_file(retroarchcfg_file, silent=True, lines=False, retry=True, createlist=True, printpoint="", addlines="")
		i2 = 0
		for x in staticL:
			extra = extra + newline + str(i2) + space2 + 'x' + space2 + str(x)
			
			z = static_L[i2]
			from_string = x + ' = "'
			to_string = '"'
			y = regex_from_to(infile_, from_string, to_string, excluding=True)
			
			if y != z and y != "":
				if '"' in y: y = ""
				replace_word(retroarchcfg_file,from_string + str(y) + to_string,from_string + str(z) + to_string, infile_="", LineR=False , LineClean=False)
					
			extra = extra + space + 'y' + space2 + str(y) + space + 'y_len' + space2 + str(len(y)) + space + 'z' + space2 + str(z)
			
			i2 += 1
			
	text = "extra" + space2 + str(extra)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def mkdirs():
	for x in dirsL:
		if not os.path.exists(x):
			try: os.mkdir(x)
			except: pass

def copydreamcastmem(force=False):
	name = 'copydreamcastmem' ; returned = '' ; printpoint = ""
	source = os.path.join(featherence_emu_module_path,'system', 'dc','formatted_vmu','')
	target = os.path.join(featherence_emu_module_path,'system', 'dc')
	if not os.path.exists(source) and force == True:
		notification('Source dir is missing!',str(source),4000)
		printpoint = printpoint + '9'
	else:
		if force == True:
			if os.path.exists(os.path.join(target,'vmu_save_A1.bin')) or os.path.exists(os.path.join(target,'vmu_save_B1.bin')) or os.path.exists(os.path.join(target,'vmu_save_C1.bin')) or os.path.exists(os.path.join(target,'vmu_save_D1.bin')):
				returned = dialogyesno('Dreamcast memory cards exists!','Are you sure you want to proceed?')
				printpoint = printpoint + '1'
			else:
				returned = 'ok'
				printpoint = printpoint + '2'
		else:
			if not ( os.path.exists(os.path.join(target,'vmu_save_A1.bin')) or os.path.exists(os.path.join(target,'vmu_save_B1.bin')) or os.path.exists(os.path.join(target,'vmu_save_C1.bin')) or os.path.exists(os.path.join(target,'vmu_save_D1.bin')) ):
				returned = 'ok'
				printpoint = printpoint + '3'
			else: printpoint = printpoint + '8'

		if returned == 'ok':
			printpoint = printpoint + '7'
			notification('Formating Dreamcast memory slots','','',1000)
			copyfiles(source,target)
			xbmc.sleep(1000)
			notification('Formating done!','','',1000)
	
	test = os.path.join(target,'vmu_save_A1.bin')
	text = "force" + space2 + str(force) + newline + \
	'source' + space2 + str(source) + newline + \
	'target' + space2 + str(target) + newline + \
	'returned' + space2 + str(returned) + newline + \
	'test' + space2 + str(test)
	
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def copylaunchers(force=False):
	
	name = 'copylaunchers' ; printpoint = ""
	if not os.path.exists(emudata_launcher_file) or force==True:
		
		dp = xbmcgui.DialogProgress()
		dp.create('Generating Launchers file',emudata_launcher_file,"")
		printpoint = printpoint + '1'
		if not os.path.exists(emudata_launcher_file):
			copyconfig(force=False)
		dp.update(5,'Generating Launchers file',"Copying emulanuncher_file...")
		copyfiles(emulanuncher_file, emudata_launcher_file) ; xbmc.sleep(500)
		
		if not os.path.exists(emulanuncher_file):
			dp.update(95,'Generating Launchers file',"Error emulanuncher_file is missing!") ; xbmc.sleep(1000)
		else:
			if systemplatformandroid: pass
			elif systemplatformlinuxraspberrypi: pass
			elif systemplatformlinux: pass
			elif systemplatformwindows:
				dp.update(10,'Generating Launchers file',"Setting windows symbols")
				replacements = {'/_': '\\_', 'rom/': 'rom\\', '_EN/': '_EN\\', '_RU/': '_RU\\', '_FUN/': '_FUN\\', '_ADULT/': '_ADULT\\', 'P/': 'P\\'}
				for key, value in replacements.items(): replace_word(emudata_launcher_file,key,value, infile_="", LineR=False , LineClean=False)

				replacements = {'/A': '\\A', '/B': '\\B', '/C': '\\C', '/D': '\\D', '/E': '\\E', '/F': '\\F', '/G': '\\G', '/H': '\\H', '/I': '\\I', '/J': '\\J', '/K': '\\K', '/L': '\\L', '/M': '\\M', '/N': '\\N', '/O': '\\O', '/P': '\\P', '/Q': '\\Q', '/R': '\\R', '/S': '\\S', '/T': '\\T', '/U': '\\U', '/V': '\\V', '/W': '\\W', '/X': '\\X', '/Y': '\\Y', '/Z': '\\Z'}
				for key, value in replacements.items(): replace_word(emudata_launcher_file,key,value, infile_="", LineR=False , LineClean=False)
				
				replacements = {'gameplay(video)/': 'gameplay(video)\\', 'screenshot/': 'screenshot\\', 'boxfront/': 'boxfront\\', '_Artwork/': '_Artwork\\'}
				for key, value in replacements.items(): replace_word(emudata_launcher_file,key,value, infile_="", LineR=False , LineClean=False)
			
			dp.update(15,'Generating Launchers file',"Setting rom_path..")
			replace_word(emudata_launcher_file,'rom_path',rom_path, infile_="", LineR=False , LineClean=False)
			dp.update(25,'Generating Launchers file',"Setting emulator_file..")
			replace_word(emudata_launcher_file,'emulator_file',emulator_file_, infile_="", LineR=False , LineClean=False)
			dp.update(35,'Generating Launchers file',"Setting lib_args..")
			replace_word(emudata_launcher_file,'lib_args',lib_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _arcade_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/mame2014_android.so'
			elif systemplatformlinux:
				if OS == "oe2" or systemplatformlinuxraspberrypi: _arcade_args = 'mame2010'
				elif OS == "i386": _arcade_args = 'fb.alpha'
				else: _arcade_args = 'mame2014'
			elif systemplatformwindows:
				if OS == "win32": _arcade_args = 'mame2010_libretro.dll'
				else: _arcade_args = 'mame2014_libretro.dll' #'mame_libretro.dll
			dp.update(40,'Generating Launchers file',"Setting _arcade_args..")
			replace_word(emudata_launcher_file,'_arcade_args',_arcade_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _nintendo_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/nestopia_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendo_args = 'fceumm'
				elif OS == "i386": _nintendo_args = 'nestopia'
				else: _nintendo_args = 'nestopia'
			elif systemplatformwindows: _nintendo_args = 'nestopia_libretro.dll'
			dp.update(45,'Generating Launchers file',"Setting _nintendo_args..")
			replace_word(emudata_launcher_file,'_nintendo_args',_nintendo_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _nintendo64_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/mupen64plus_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendo64_args = 'mupen64plus'
				elif OS == "i386": _nintendo64_args = 'mupen64plus'
				else: _nintendo64_args = 'mupen64plus'
			elif systemplatformwindows: _nintendo64_args = 'mupen64plus_libretro.dll'
			#start -n com.androidemu.n64/.EmulatorActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"
			dp.update(50,'Generating Launchers file',"Setting _nintendo64_args..")
			replace_word(emudata_launcher_file,'_nintendo64_args',_nintendo64_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _nintendods_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/desmume_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendods_args = "desmume"
				elif OS == "i386": _nintendods_args = 'desmume'
				else: _nintendods_args = 'desmume'
			elif systemplatformwindows: _nintendods_args = 'desmume_libretro.dll'
			dp.update(55,'Generating Launchers file',"Setting _nintendods_args..")
			replace_word(emudata_launcher_file,'_nintendods_args',_nintendods_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _segagenesis_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/genesis_plus_gx_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _segagenesis_args = 'genesis.plus.gx'
				elif OS == "i386": _segagenesis_args = 'genesis.plus.gx'
				else: _segagenesis_args = 'genesis.plus.gx'
			elif systemplatformwindows: _segagenesis_args = 'genesis.plus.gx_libretro.dll'
			dp.update(60,'Generating Launchers file',"Setting _segagenesis_args..")
			replace_word(emudata_launcher_file,'_segagenesis_args',_segagenesis_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _ps1_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/pcsx2_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _ps1_args = 'pcsx.rearmed'
				elif OS == "i386": _ps1_args = 'mednafen.psx'
				else: _ps1_args = 'mednafen.psx'
			elif systemplatformwindows: _ps1_args = 'mednafen.psx_libretro.dll'
			dp.update(65,'Generating Launchers file',"Setting _ps1_args..")
			replace_word(emudata_launcher_file,'_ps1_args',_ps1_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _ps2_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/pcsx2_libretro_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _ps2_args = 'pcsx2'
				elif OS == "i386": _ps2_args = ''
				else: _ps2_args = 'play'
			elif systemplatformwindows: _ps2_args = 'pcsx2_libretro.dll'
			dp.update(65,'Generating Launchers file',"Setting _ps2_args..")
			replace_word(emudata_launcher_file,'_ps2_args',_ps2_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _supernintendo_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/snes9x_next_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _supernintendo_args = 'pocketsnes'
				elif OS == "i386": _supernintendo_args = 'snes9x.next'
				else: _supernintendo_args = 'snes9x.next'
			elif systemplatformwindows: _supernintendo_args = 'snes9x.next_libretro.dll'
			dp.update(70,'Generating Launchers file',"Setting _supernintendo_args..")
			replace_word(emudata_launcher_file,'_supernintendo_args',_supernintendo_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _turbografx16_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/mednafen_pce_fast_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _turbografx16_args = 'mednafen.pce.fast'
				elif OS == "i386": _turbografx16_args = 'mednafen.pce.fast'
				else: _turbografx16_args = 'mednafen.pce.fast'
			elif systemplatformwindows: _turbografx16_args = 'mednafen.pce.fast_libretro.dll'
			dp.update(80,'Generating Launchers file',"Setting _segagenesis_args..")
			replace_word(emudata_launcher_file,'_turbografx16_args',_turbografx16_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _dreamcast_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/reicast_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _dreamcast_args = ""
				elif OS == "i386": _dreamcast_args = 'reicast'
				else: _dreamcast_args = 'reicast'
			elif systemplatformwindows: _dreamcast_args = 'reicast_libretro.dll'
			dp.update(90,'Generating Launchers file',"Setting _dreamcast_args..")
			replace_word(emudata_launcher_file,'_dreamcast_args',_dreamcast_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _gamecube_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/dolphin_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _gamecube_args = ""
				elif OS == "i386": _gamecube_args = 'dolphin'
				else: _gamecube_args = 'dolphin'
			elif systemplatformwindows: _gamecube_args = 'dolphin_libretro.dll'
			dp.update(95,'Generating Launchers file',"Setting _gamecube_args..")
			replace_word(emudata_launcher_file,'_gamecube_args',_gamecube_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _dos_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/dosbox_libretro.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _dos_args = ""
				elif OS == "i386": _dos_args = 'dosbox'
				else: _dos_args = 'dosbox_pure'
			elif systemplatformwindows: _dos_args = 'dosbox_pure_libretro.dll'
			replace_word(emudata_launcher_file,'_dos_args',_dos_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _scummvm_args = ''
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _scummvm_args = ""
				elif OS == "i386": _scummvm_args = 'scummvm'
				else: _scummvm_args = 'scummvm'
			elif systemplatformwindows: _scummvm_args = 'scummvm_libretro.dll'
			dp.update(98,'Generating Launchers file',"Setting _scummvm_args..")
			replace_word(emudata_launcher_file,'_scummvm_args',_scummvm_args, infile_="", LineR=False , LineClean=False)
			
			
		dp.update(100,'Generating Launchers file',"Finising..")
		dp.close
	
	text = "force" + space2 + str(force) + newline + \
	'emudata_launcher_file' + space2 + str(emudata_launcher_file)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def filterbyos(x):
	'''Simply hide some consoles for specific OS'''
	name = 'filterbyos' ; printpoint = "" ; returned = ""
	
	if systemplatformwindows:
		if OS == "win32":
			if x == 'Featherence_nintendods': returned = "filter"
			if x == 'Featherence_gamecube': returned = "filter"
	
	elif systemplatformandroid: pass
	
	elif systemplatformlinux:
		if systemplatformlinuxraspberrypi or OS == "oe2":
			if x == 'Featherence_nintendods': returned = "filter"
			if x == 'Featherence_dreamcast': returned = "filter"
			if x == 'Featherence_gamecube': returned = "filter"
		elif OS == "i386":
			if x == 'Featherence_nintendods': returned = "filter"
			if x == 'Featherence_dreamcast': returned = "filter"
			if x == 'Featherence_gamecube': returned = "filter"
			
	
	
	
	text = "x" + space2 + str(x) + newline + \
	'returned' + space2 + str(returned)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
	return returned

def AudioDevices():
	'''------------------------------
	---AUDIO-DEVICES-----------------
	------------------------------'''
	if systemplatformlinux:
		output = terminal('aplay -l | grep -e "card" | grep -n ""')
		output = output.split('\n')
		CARD_DEVICE = ""
		i = 0
		for line in output:
			if line != "":
				i += 1
				CARD_ = find_string(line, "card ", ": ")
				CARD_ = CARD_.replace("card ","")
				CARD_ = CARD_.replace(": ",",")
				DEVICE_ = find_string(line, "device ", ": ")
				DEVICE_ = DEVICE_.replace("device ","")
				DEVICE_ = DEVICE_.replace(": ","")
				CARD_DEVICE = CARD_DEVICE + newline + "OPTION" + str(i) + space2 + "hw:" + CARD_ + DEVICE_
				
		print CARD_ + space + DEVICE_ + newline + str(output) + "CARD_DEVICE" + space2 + CARD_DEVICE
		header = 'AUDIO DEVICES'
		message2 = "[CR]---------------------------[CR]" + CARD_DEVICE + "[CR]---------------------------[CR][CR]" + 'Try each of those devices'
		w = TextViewer_Dialog('DialogTextViewer.xml', "", header=header, text=message2)
		w.doModal()
		'''---------------------------'''
