import xbmc, xbmcgui, xbmcaddon
import os, sys

from variables import *
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
	
def downloads(plugin, category="", launcher="", rom="", filename="", filepath=""):
	name = 'downloads' ; printpoint = "" ; filename_ = ""
	skincheck() #; 
	Featherence_auth = getsetting_servicefeatherence('Featherence_auth')
	if Featherence_auth != Featherence_auth2:
		notification(str(Featherence_auth),"","",2000)
		frun()
	else:
		if category != "" and filename != "" and filepath != "":
			if not os.path.exists(os.path.join(filepath)): printpoint = '1'
			else:
				returned = dialogyesno('Folder exist!', 'Would you like to redownload?')
				if returned != 'skip': printpoint = '2'
			
			if printpoint != "":
				if category == 'Featherence_segamastersystem':
					if launcher == 'Featherence_segamastersystem1P':
						filename_ = filename.replace(':',"")
						file = "SMS" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							if not '[GD]' in fileID:
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/SMS" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
							else:
								fileID = fileID.replace('[GD]',"")
								DownloadFile("https://drive.google.com/uc?export=download&id="+fileID, "1.zip", temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						file = "SMS.zip"
						fileID = getfileID(file)
						if fileID != "":
							if not '[GD]' in fileID:
								DownloadFile("https://www.dropbox.com/s/"+fileID+"/SMS.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
							else:
								fileID = fileID.replace('[GD]',"")
								DownloadFile("https://drive.google.com/uc?export=download&id="+fileID, file, temp_path, rom_path, percentinfo=5)
							
					
			
				elif category == 'Featherence_turbografx16':
					if launcher == 'Featherence_turbografx161P':
						filename_ = filename.replace(':',"")
						file = "TG16_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/TG16_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_turbografx162P':
						filename_ = filename.replace(':',"")
						file = "TG16_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/TG16_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						file = "TG16.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/TG16.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
					
					
				elif category == 'Featherence_segagenesis':
					if launcher == 'Featherence_segagenesis1P':
						filename_ = filename.replace(':',"")
						file = "SG_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/SG_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_segagenesis2P':
						filename_ = filename.replace(':',"")
						file = "SG_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/SG_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						file = "SG.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/SG.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
					
				
				elif category == 'Featherence_nintendo':
					if launcher == 'Featherence_nintendo1P':
						filename_ = filename.replace(':',"")
						file = "NES_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/NES_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_nintendo2P':
						filename_ = filename.replace(':',"")
						file = "NES_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/NES_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						file = "NES.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/NES.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif category == 'Featherence_supernintendo':
					if launcher == 'Featherence_supernintendo1P':
						filename_ = filename.replace(':',"")
						file = "SNES_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/SNES_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_supernintendo2P':
						filename_ = filename.replace(':',"")
						file = "SNES_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/SNES_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						file = "SNES.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/SNES.zip?dl=1", file, temp_path, rom_path, percentinfo=2)				
			
				elif category == 'Featherence_nintendo64':
					if launcher == 'Featherence_nintendo641P':
						filename_ = filename.replace(':',"")
						file = "N64_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_nintendo642P':
						filename_ = filename.replace(':',"")
						file = "N64_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					
					elif launcher == 'Featherence_nintendo644P':
						filename_ = filename.replace(':',"")
						file = "N64_4P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else: printpoint = printpoint + 'D'
					else: printpoint = printpoint + 'D'
					
					if 'D' in printpoint:
						if launcher == 'Featherence_nintendo641P':
							file = "N64_1P.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_1P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
						elif launcher == 'Featherence_nintendo642P':
							file = "Nintendo 64_2P.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_2P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
						elif launcher == 'Featherence_nintendo644P':
							file = "N64_4P.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/N64_4P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
						
					
							
				elif category == 'Featherence_arcade':
					if launcher == 'Featherence_arcade1P':
						filename_ = filename.replace(':',"")
						file = "Arcade_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_1P.zip"
							fileID = getfileID(file)
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_1P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_arcade2P':
						filename_ = filename.replace(':',"")
						file = "Arcade_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_2P.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_2P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
					elif launcher == 'Featherence_arcade3P':
						file = "Arcade_3P.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_3P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_arcade4P':
						filename_ = filename.replace(':',"")
						file = "Arcade_4P_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_4P.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_4P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_arcadeGEAR':
						filename_ = filename.replace(':',"")
						file = "Arcade_GEAR_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_GEAR_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_GEAR.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_GEAR.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_arcadeFUN':
						filename_ = filename.replace(':',"")
						file = "Arcade_FUN_" + filename_ + ".zip"
						fileID = getfileID(file)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_FUN_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_FUN.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_FUN.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_arcadeADULT':
						filename_ = filename.replace(':',"")
						file = "Arcade_ADULT" + filename_ + ".zip"
						fileID = getfileID(file)
						notification('1',file,'',1000)
						if fileID != "":
							filename__ = filename_.replace(" ", "%20")
							DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_ADULT" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						else:
							file = "Arcade_ADULT.zip"
							fileID = getfileID(file)
							if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_ADULT.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif category == 'Featherence_nintendods':
					if launcher == 'Featherence_nintendods1P':
						filename_ = '_' + filename.replace(':',"")
						
						if '4225 -' in filename or 'Professor Layton' in filename: file = "NDS2.zip"
						else: file = "NDS_1P.zip"
						fileID = getfileID(file)
						filename__ = file.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
				elif category == 'Featherence_playstation':
					if launcher == 'Featherence_playstation1P':
						filename_ = filename.replace(':',"")
						file = "Sony Playstation_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_playstation2P':
						filename_ = filename.replace(':',"")
						file = "Sony Playstation_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_playstation4P':
						filename_ = filename.replace(':',"")
						file = "Sony Playstation_4P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif category == 'Featherence_dreamcast':
					if launcher == 'Featherence_dreamcast1P':
						filename_ = filename.replace(':',"")
						file = "Dreamcast_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Dreamcast_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_dreamcast2P':
						filename_ = filename.replace(':',"")
						file = "Dreamcast_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Dreamcast_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_dreamcast4P':
						filename_ = filename.replace(':',"")
						file = "Dreamcast_4P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/Dreamcast_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif category == 'Featherence_gamecube':
					if launcher == 'Featherence_gamecube1P':
						filename_ = filename.replace(':',"")
						file = "GameCube_1P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/GameCube_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_gamecube2P':
						filename_ = filename.replace(':',"")
						file = "GameCube_2P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/GameCube_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_gamecube4P':
						filename_ = filename.replace(':',"")
						file = "GameCube_4P_" + filename_ + ".zip"
						fileID = getfileID(file)
						filename__ = filename_.replace(" ", "%20")
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/GameCube_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif category == 'Featherence_dos':
					if launcher == 'Featherence_dosEN':
						file = "DOS.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/DOS.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
					elif launcher == 'Featherence_dosHE':
						file = "DOS.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/DOS.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
					elif launcher == 'Featherence_dosRU':
						file = "DOS.zip"
						fileID = getfileID(file)
						if fileID != "": DownloadFile("https://www.dropbox.com/s/"+fileID+"/DOS.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
		
	text = "category" + space2 + str(category) + newline + \
	"launcher" + space2 + str(launcher) + newline + \
	"rom" + space2 + str(rom) + newline + \
	"filename" + space2 + str(filename) + newline + \
	"filename_" + space2 + str(filename_) + newline + \
	"filepath" + space2 + str(filepath) + newline
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def downloads2(file):
	fileID = getfileID(file)
	file_ = file
	file_ = file_.replace(" ", "%20")
	DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file_+"?dl=1", file, temp_path, rom_path)
	
def startup():
	name = 'startup' ; printpoint = "" ; VerReset = "" ; value = False
	
	setProperty('emu_startup', 'true', type="home")
	
	from shared_modules3 import checkAddon_Update
	checkAddon_Update("", Addon_Update, Addon_Version, addonVersion, Addon_UpdateDate, Addon_UpdateLog, Addon_ShowLog, Addon_ShowLog2, VerReset)
	
	if Addon_UpdateLog == "true":
		list = []
		list.append(addonString_servicefeatherence(32060).encode('utf-8')) #Would you like thanks us? Would love to hear you!
		list.append(addonString_servicefeatherence(32061).encode('utf-8')) #Do you want to contribute?
		list.append(addonString_servicefeatherence(32062).encode('utf-8')) #Have an idea for new addon?
		list.append(addonString_servicefeatherence(32063).encode('utf-8')) #Looking for support?
		list.append(addonString_servicefeatherence(32064).encode('utf-8')) #Having a question?
		returned, value = getRandom(0, min=0, max=len(list), percent=50)
		
		notification(list[int(value)],'www.featherence.com','',4000)
	
	chmod()
	copydreamcastmem(force=False)
	
	if Addon_Update == "true":
		notification("Received new update!","Check www.featherence.com for support","",4000)
		value = True
	
	copylaunchers(force=value)
	copyarcade(force=value)
	resolution_check()
	if custom_emu != 'true': copyconfig(force=value)
	else: copyconfig(force=False)
	
	
	installemuconsole()
	
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
				
	
def getfileID(file):
	name = 'getfileID' ; printpoint = ""
	fileID = "" ; fileID_L = [""] ; fileName_L = ['--> (Exit)']
	if file == "linux.featherence.emu.zip": fileID = "1i7zhab80o8chyn" #finalmakerr
	elif file == "nvram_diff.zip": fileID = 'rsi3jgrht99iwwc' #featherence.user3

	elif file == "_Artworks.zip": fileID = 'spb79jo0zelhv38' #featherence.user48
	
	elif file == "Arcade_1P.zip": fileID = 'ff5suc5a8u6vss8' #featherence.user5
	elif file == "Arcade_1P_Turret Tower.zip": fileID = "usyvftx1cx85528" #htptuser1
	
	elif file == "Arcade_2P.zip": fileID = 'lc5rdhqms9i7q6q' #featherence.user51

	elif file == "Arcade_2P_Age Of Heroes - Silkroad 2.zip":
		fileID_L.append('bqrt9ltcb1h5zjh') #guser26
		fileID_L.append('5k1kkdavv5klqvh') #featherence.user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Area 51.zip": fileID = 'zgg4mpg6dh71z02' #htptuser2
		
	elif file == "Arcade_2P_Area 51 Maximum Force Duo v2.0.zip": fileID = 'v74zfmphjua4xo6' #featherence.user35
		
	elif file == "Arcade_2P_Demon Front.zip": fileID = 'q6dyv0bzu7xvcdz' #guser26
		
	elif file == "Arcade_2P_Flame Gunner.zip":
		fileID_L.append('ag0k2gh5a20e7yg') #guser26
		fileID_L.append('1aor06jv3zm1sxy') #featherence.user15
		fileID_L.append('pah5c5cmsiv5deu') #featherence.user28
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Arcade_2P_Garou - Mark of the Wolves.zip": fileID = 'ol5f0v2d9nkodyd' #featherence.user51
	elif file == "Arcade_2P_Killer Instinct.zip": fileID = 'yztr7wx3xeb0xxf' #guser24
	elif file == "Arcade_2P_Killer Instinct 2.zip": fileID = 's4jlqn4316uxrq6' #guser24
	elif file == "Arcade_2P_Lansquenet 2004.zip":
		fileID_L.append('wpa5dmhsomtmq8j') #guser21
		fileID_L.append('013po8qcsywg42l') #featherence.user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Mace The Dark Age.zip": fileID = '0fnst5ov2muys5r' #htptuser15
	elif file == "Arcade_2P_Metal Slug 3.zip": fileID = 'r7l3ay23pop3vt2' #htptuser15
	elif file == "Arcade_2P_Metal Slug 4.zip": fileID = 'm9vvqp6qv3zzcwv' #htptuser15
	elif file == "Arcade_2P_Metal Slug 5.zip": fileID = 'vez9r4w9fk1wah4' #htptuser15
	elif file == "Arcade_2P_Prehistoric Isle 2.zip": fileID = 'yxtqtuk9o787ooo' #htptuser17
	elif file == "Arcade_2P_Rage of the Dragons.zip": fileID = '4gcdai4k67tm0nv' #htptuser17
	elif file == "Arcade_2P_Red Earth.zip": fileID = '9hhzwyqmk2ucpza' #htptuser15
	elif file == "Arcade_2P_Sengoku 3.zip": fileID = '1p2vnxnxkklgxaz' #featherence.user51
	elif file == "Arcade_2P_SNK vs. Capcom - SVC Chaos.zip": fileID = 'kzbct5liwenmmaa' #htptuser20
	elif file == "Arcade_2P_Street Fighter III 3rd Strike Fight for the Future.zip": fileID = 'lkl0it20ui5gi70' #htptuser11
	elif file == "Arcade_2P_Tekken Tag Tournament.zip": fileID = '7i5kxmk5d6g0cfj' #
	elif file == "Arcade_2P_Tenth Degree.zip": fileID = '4qvlwo6odg7nbyz' #user55
	elif file == "Arcade_2P_Tekken 3.zip":
		fileID_L.append('m1qg58ukl1f4xve') #htptuser9
		fileID_L.append('c51pfektqxuzry2') #featherence.user28
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_The Crystal of Kings.zip": fileID = 'urk6eqnvmxxk1pv' #htptuser9
	elif file == "Arcade_2P_The King of Fighters '98 - The Slugfest.zip": fileID = 'byo2ses423lgjud' #guser24
	elif file == "Arcade_2P_The King of Fighters 2002.zip": fileID = 'flya0lnhzcngx0u' #htptuser20
	elif file == "Arcade_2P_The Last Blade 2.zip": fileID = 'qrlctae8cd6omml' #infohtpt

	elif file == "Arcade_3P.zip":
		fileID_L.append('86hwvrrhp8xzxdx') #featherence.user41
		fileID_L.append('z72bbl6goev3tm9') #featherence.user6
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_4P.zip":
		fileID_L.append('ubya3wg60fx3e6b') #guser14
		fileID_L.append('2divr39cj5fgh77') #guser21
		fileID_L.append('4e3645if0m5uom4') #htptuser
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
		
	elif file == "Arcade_4P_Gauntlet Dark Legacy.zip": fileID = 'oijy0kiz0l792xc' #htptuser15
	elif file == "Arcade_4P_Gauntlet Legends.zip": fileID = 'jdrbwfesdgm97tr' #infohtpt
	elif file == "Arcade_ADULT.zip": fileID = 'gabtdr7exw1s9x4' #infohtpt
		
	elif file == "Arcade_GEAR.zip":
		fileID_L.append('v0si3xo3pt72xpa')
		fileID_L.append('glurpmeqf0wbw68') #featherence.user19
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		
	elif file == "Arcade_GEAR_California Speed.zip": fileID = "gbfxppac8bbnw2b" #infohtpt
	elif file == "Arcade_GEAR_Hyperdrive.zip": fileID = "wlmirerbe5dpezq" #htptuser15
		
	elif file == "Arcade_FUN.zip": fileID = 'nhcj88dm4k2yovn' #featherence.user3 (featherence.user6, guser19!)
	elif file == "N64_1P.zip": fileID = 'rxrcxn2jwvu7uya' #featherence.user40
	elif file == "N64_2P.zip": fileID = 'nik1li3j3dy6qfh' #buy
	elif file == "N64_4P.zip": fileID = 'k1judhtx8kxj17y' #buy (#htpt)
	elif file == "NES.zip": fileID = 'x34c6ra4x7p5md6' #buyhtpt
	elif file == "DOS.zip": fileID ='af88lxievh3nuo3' #featherence.guser37
	elif file == "NDS.zip": fileID = '5abhum0vadjjeec' #htptdebugout2
	elif file == "NDS2.zip": fileID = 'u5cueqkzg5knx8o' #featherence.user30 (guser28,htpt)
	
	elif file == "SG.zip": fileID = '6rrdcw00yn7m6v6' #buy (guser21)
		
	elif file == "SMS.zip":
		fileID = '6xexl5kseczr2aw' #buy (#guser21, #guser26)
		
	elif file == "SNES.zip":
		fileID_L.append('yp2tgk57kzgzznk') #featherence.user28
		fileID_L.append('47q9q73un8ohjax') #buy (#featherence.user3, #featherence.user38)
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		
	elif file == "TG16.zip": fileID = 'kjccmraju49sw3a' #buy
	
	
	elif file == "Sony Playstation_1P_Alundra.zip": fileID = "8ajszedon75tzwx" #htptuser12
	elif file == "Sony Playstation_1P_Ape Escape.zip": fileID = "2fcd8w79gplfqxm" #htptuser12
	elif file == "Sony Playstation_1P_Battle Hunter.zip": fileID = "bnltlp9nqovzare" #htptuser12
	elif file == "Sony Playstation_1P_Brigandine - The Legend of Forsena.zip": fileID = "t3if5116f3z5ok2" #htptuser12
	elif file == "Sony Playstation_1P_Bust-a-Move '99.zip": fileID = "r31jozc8ujr0z5i" #htptuser12 not downloading!
	elif file == "Sony Playstation_1P_Castlevania - Symphony Of The Night.zip": fileID = "1d8sik6zdjp5ago" #htptuser8
	elif file == "Sony Playstation_1P_Chrono Cross.zip": fileID = "blx6e047sty05ga" #htptuser12
	elif file == "Sony Playstation_1P_Command & Conquer.zip": fileID = "zw7gt9f65fbj9eu" #htptuser13
	elif file == "Sony Playstation_1P_Command & Conquer - Red Alert.zip": fileID = "5m9je5lv7ed2y83" #htptuser13
	elif file == "Sony Playstation_1P_Command & Conquer - Red Alert - Retaliation.zip": fileID = "k6vmk2hy7ir61mn" #htptuser14
	elif file == "Sony Playstation_1P_Crash Bandicoot.zip": fileID = 'qid216wds25xr0i' #buy
	elif file == "Sony Playstation_1P_Crash Bandicoot 2.zip":
		fileID_L.append('m0hnjiy8sup4jtv') #htptuser7
		fileID_L.append('gzvtu17iebdflze') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Sony Playstation_1P_Crash Bandicoot 3.zip":
		fileID_L.append('lduolj8k0n4wwld') #htptuser14
		fileID_L.append('jz2fpm9lrh8udzm')
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Sony Playstation_1P_Digimon World.zip": fileID = "qhnqm6wejqtzhzt" #htptuser14
	elif file == "Sony Playstation_1P_Digimon World 2.zip": fileID = "o6unftle6in4oz5" #htptuser13
	elif file == "Sony Playstation_1P_Digimon World 3.zip": fileID = "esiv8i4on1h6wso" #htptuser7
	elif file == "Sony Playstation_1P_Dino Crisis.zip": fileID = "2efwp6im1aotg8v" #htptuser12
	elif file == "Sony Playstation_1P_Dino Crisis 2.zip": fileID = "awmx89zo20kmks4" #htptuser7
	elif file == "Sony Playstation_1P_Disney's Hercules Action Game.zip": fileID = "0lbyhyvt8qmpsc1" #htptuser14
	elif file == "Sony Playstation_1P_Driver.zip": fileID = "553sd3fh7lpoumn" #htptuser14
	elif file == "Sony Playstation_1P_Final Fantasy VII.zip": fileID = "85llpgfjz4uih2z" #htptuser7
	elif file == "Sony Playstation_1P_Final Fantasy VIII.zip": fileID = "gt5its29qvdt4f9" #htptuser6
	elif file == "Sony Playstation_1P_Final Fantasy IX.zip":
		fileID_L.append('i09gmh6nqruibmu') #htptuser19
		fileID_L.append('rgivtj2fjbbekvj') #htptuser27
		fileName_L.append('CD1-2')
		fileName_L.append('CD3-4')
	
	elif file == "Sony Playstation_1P_Front Mission 3.zip": fileID = "3dwdqau409oe5m8" #htptuser19
	elif file == "Sony Playstation_1P_Galerians.zip": fileID = "cstcaokpbmsvbxx" #htptuser19
	elif file == "Sony Playstation_1P_Grand Theft Auto 2.zip": fileID = "zti40bzu1o5e2os" #htptuser8
	elif file == "Sony Playstation_1P_Jackie Chan Stuntmaster.zip": fileID = "kbm6jb9pvg9fyza" #htptuser8
	elif file == "Sony Playstation_1P_Lunar - Silver Star Story Complete.zip": fileID = "l85h27qa1qt9sdh" #htptuser21
	elif file == "Sony Playstation_1P_Mega Man Legends.zip": fileID = "zjdxzliibvtl1df" #htptuser21
	elif file == "Sony Playstation_1P_Mega Man X4.zip": fileID = "8kopww6klbqn0jq" #htptuser8
	elif file == "Sony Playstation_1P_Mega Man X5.zip": fileID = "9f6bk6px1wtauxp" #htptuser14
	elif file == "Sony Playstation_1P_Mega Man X6.zip": fileID = "impb58cqacc3ba1" #htptuser14
	elif file == "Sony Playstation_1P_Metal Gear Solid.zip": fileID = "zreea6rsbo6t7ca" #htptuser8
	elif file == "Sony Playstation_1P_Metal Gear Solid VR Missions.zip": fileID = "tql0ori6cqge22s" #htptuser21
	elif file == "Sony Playstation_1P_Oddworld - Abes Oddysee.zip": fileID = "gbibjsf4mzhbq0w" #htptuser21
	elif file == "Sony Playstation_1P_Pac-Man World.zip": fileID = "5f7sadldxokszrz" #htptuser5
	elif file == "Sony Playstation_1P_Parasite Eve 2.zip": fileID = "j7ok6yv3k1aljpk" #htptuser22
	elif file == "Sony Playstation_1P_Populous - The Beginning.zip": fileID = "u3s4s391tz2vayc" #htptuser22
	elif file == "Sony Playstation_1P_Railroad Tycoon II.zip": fileID = "v272g24r6ii5djn" #htptuser22
	elif file == "Sony Playstation_1P_Rayman Brain Games.zip": fileID = "z07w776e6o62xwt" #htptuser22
	elif file == "Sony Playstation_1P_Rayman Rush.zip": fileID = "vn5ssuexnirgmb3" #htptuser22
	elif file == "Sony Playstation_1P_Resident Evil 2.zip": fileID = "pafqxpgs1qhhgw5" #htptuser17
	elif file == "Sony Playstation_1P_Resident Evil 3.zip": fileID = "5m8ln06e5ehc6oh" #htptuser17
	elif file == "Sony Playstation_1P_Road Rash 3D.zip": fileID = "my6lt21oixpuy3l" #htptuser5
	elif file == "Sony Playstation_1P_Silent Hill.zip": fileID = "ryfa2ekrjoe8aa6" #htptuser17
	elif file == "Sony Playstation_1P_Spider-Man.zip": fileID = "e2wc0xa7pk85sf1" #htptuser6
	elif file == "Sony Playstation_1P_Spider-Man 2 - Enter Electro.zip": fileID = "icecnzvirlewruv" #htptuser17
	elif file == "Sony Playstation_1P_Spyro Year of the Dragon.zip": fileID = "c8j2hgeyd6x33xi" #htptuser9
	elif file == "Sony Playstation_1P_Spyro 2 - Riptos Rage.zip": fileID = "m5fa4oj1m1vbv1h" #htptuser17
	elif file == "Sony Playstation_1P_Suikoden.zip": fileID = "3opm0of6yblj7x1" #htptuser20
	elif file == "Sony Playstation_1P_Super Shot Soccer.zip": fileID = "x0cu2c8up654ca9" #htptuser18
	elif file == "Sony Playstation_1P_Syphon Filter.zip": fileID = "xbcwozn9f2cvzxu" #htptuser18
	elif file == "Sony Playstation_1P_Tales of Destiny.zip": fileID = "xtzt22coc1omcko" #htptuser9
	elif file == "Sony Playstation_1P_Tales of Destiny II.zip": fileID = "wb0xqy8tqc38r63" #htptuser18
	elif file == "Sony Playstation_1P_Tenchu 2 - Birth Of The Stealth Assassins.zip": fileID = "vkpx8d21b517a1g" #htptuser18
	elif file == "Sony Playstation_1P_The Legend of Dragoon.zip": fileID = "cp6foxr496i78ay" #htptuser9
	elif file == "Sony Playstation_1P_Theme Hospital.zip": fileID = "rwofbkoodqr5m17" #htptuser18
	elif file == "Sony Playstation_1P_Thousand Arms.zip": fileID = "h8dieiggps4km5z" #htptuser20
	elif file == "Sony Playstation_1P_Tigger's Honey Hunt.zip": fileID = 'laxrgtg4eg90pdf' #guser9

	elif file == "Sony Playstation_1P_Tigger's Honey Hunt.zip": fileID = "laxrgtg4eg90pdf" #guser9
	elif file == "Sony Playstation_1P_Valkyrie Profile.zip": fileID = "bc9gg84b9r39ewx" #htptuser20
	elif file == "Sony Playstation_1P_WarCraft II - The Dark Saga.zip": fileID = "prnuctnm8zls2ce" #htptuser23
	elif file == "Sony Playstation_1P_Warhammer - Dark Omen.zip": fileID = "sn8irts9j710jmw" #htptuser23
	
	elif file == "Sony Playstation_2P_Bloody Roar II.zip": fileID = "monmvljc2xh48od" #htptuser23
	elif file == "Sony Playstation_2P_Bomberman Fantasy Race.zip": fileID = "28je9q85l4tibzc" #htptuser23
	elif file == "Sony Playstation_2P_Bomberman World.zip": fileID = "p00rtmr02r7stoq" #htptuser23
	elif file == "Sony Playstation_2P_Diablo.zip": fileID = "k05atfov22r8ywu" #htptuser10
	elif file == "Sony Playstation_2P_Digimon Digital Card Battle.zip": fileID = "s4sw4flxxzz64ca" #htptuser10
	elif file == "Sony Playstation_2P_Digimon Rumble Arena.zip": fileID = "npgiws620kteu8x" #htptuser10
	elif file == "Sony Playstation_2P_Fighting Force.zip": fileID = "jep1hofgub7vuef" #tulu
	elif file == "Sony Playstation_2P_Gauntlet Legends.zip": fileID = "g4qcakkuz3hxne6" #htptuser10
	elif file == "Sony Playstation_2P_Gran Turismo 2.zip": fileID = "2ptmzcafa9amtbq" #htptuser27
	elif file == "Sony Playstation_2P_Mega Man 8.zip": fileID = "mx2wsf5zjyk6qk8" #htptuser
	elif file == "Sony Playstation_2P_Metal Slug X.zip": fileID = "nhlpyhikcbbowb9" #htptuser10
	elif file == "Sony Playstation_2P_Moto Racer World Tour.zip": fileID = "ps07jb486i6oiav" #htptuser10
	elif file == "Sony Playstation_2P_Need For Speed III - Hot Pursuit.zip": fileID = "xflg3q638bd57f3" #htptuser NOT WORKING?
	elif file == "Sony Playstation_2P_NHL Open Ice.zip": fileID = "1alwsil1x4jeao0" #htptuser10
	elif file == "Sony Playstation_2P_Re-Loaded.zip": fileID = "gke0d4uw1s3ce5l" #fix
	elif file == "Sony Playstation_2P_Rival Schools.zip": fileID = "lxlwycnvtsmdll5" #htptuser
	elif file == "Sony Playstation_2P_Running Wild.zip": fileID = "nwl1uahiwoyowjq" #htptuser10
	elif file == "Sony Playstation_2P_Small Soldiers.zip": fileID = "ylc3mmdqyqduyu0" #fix
	elif file == "Sony Playstation_2P_Speed Punks.zip": fileID = "k05atfov22r8ywu" #htptuser10
	elif file == "Sony Playstation_2P_Street Fighter Alpha 3.zip": fileID = "a06awji699g86h0" #htptuser11
	elif file == "Sony Playstation_2P_Super Puzzle Fighter II Turbo.zip": fileID = "acfsgyrxt3vqfjk" #htptuser
	elif file == "Sony Playstation_2P_Syphon Filter 2.zip": fileID = "f9g6t8mkisybzev" #htptuser11
	elif file == "Sony Playstation_2P_Tekken 3.zip": fileID = "mxhx48jousad3zg" #fix
	elif file == "Sony Playstation_2P_Thrill Kill.zip": fileID = "ooyshbkenk68gpl" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater.zip": fileID = "4nopoihpr7zo9yo" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 2.zip": fileID = "xx9kyy4g0n7nfq5" #htptuser11
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 3.zip": fileID = "8npbop2z33gaubn" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 4.zip": fileID = "xiz3j6dpcao86ou" #fix
	elif file == "Sony Playstation_2P_Twisted Metal 2.zip": fileID = "yi8a2jze1w6j7mf" #htptuser11
	elif file == "Sony Playstation_2P_Twisted Metal 3.zip": fileID = "owddyt09auhirg7" #fix
	elif file == "Sony Playstation_2P_Twisted Metal 4.zip": fileID = "i6riyjeulk01j03" #fix
	elif file == "Sony Playstation_2P_Worms World Party.zip": fileID = "4dplcbknvt3v8nt" #tulu
	elif file == "Sony Playstation_2P_WWF Attitude.zip": fileID = "0fcs44bmfl0kan6" #tulu
	elif file == "Sony Playstation_2P_Vigilante 8 - 2nd Offense.zip": fileID = "3fpblfwgwkd734l" #tulu
	
	elif file == "Sony Playstation_4P_Crash Bash.zip":
		fileID_L.append('afaane71ersuibs') #tulu
		fileID_L.append('9baiwsh35hutzo2')
		fileID_L.append('nfc9wq282ra7q12') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Sony Playstation_4P_Family Card Game Fun Pak.zip": fileID = "81icbmbdbq7hgta" #tulu
	elif file == "Sony Playstation_4P_FoxKids.com - Micro Maniacs Racing.zip": fileID = "ups6wzko2rktb1y" #tulu
	elif file == "Sony Playstation_4P_Grind Session.zip": fileID = "mxlkx51805uluab" #tulu
	elif file == "Sony Playstation_4P_International Track & Field 2000.zip": fileID = "pejppkuekj24e3l" #tulu
	elif file == "Sony Playstation_4P_International Track & Field.zip": fileID = "p2dedvf4eu4s30u" #tulu
	elif file == "Sony Playstation_4P_Monopoly.zip": fileID = "i34fhra6cm9vvg9" #tulu
	elif file == "Sony Playstation_4P_Quake II.zip": fileID = "3y75682fb1idj61" #tulu
	elif file == "Sony Playstation_4P_Rally Cross.zip": fileID = "84a68ip4qqtaq2n" #tulu
	elif file == "Sony Playstation_4P_Risk - The Game of Global Domination.zip": fileID = "943zezcgovk9884" #tulu
	elif file == "Sony Playstation_4P_Team Buddies.zip": fileID = "09df5thqr8hvh56" #tulu
	elif file == "Sony Playstation_4P_Worms Armageddon.zip": fileID = "50otyujunwds25k" #tulu
	elif file == "Sony Playstation_4P_Worms.zip":
		fileID_L.append('0okrzyk6mphsvgu') #buy
		fileID_L.append('ibgnouatrbli7w7')
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')

		
	elif file == "Dreamcast_2P_Project Justice - Rival Schools 2.zip": fileID = "n9mnlaffe27f3h1" #featherence.user1
	elif file == "Dreamcast_2P_Sonic Adventure 2.zip": fileID = "gyehvme4ky3bo93" #featherence.user1
	elif file == "Dreamcast_1P_Headhunter.zip": fileID = "nogvxl1mabgj6uo" #featherence.user2
	elif file == "Dreamcast_2P_Street Fighter III - 3rd Strike.zip": fileID = "tew77v2lqhybj2j" #featherence.user2
	
	elif file == "Dreamcast_2P_Capcom vs. SNK.zip": fileID = "7373ygc3fk66rtq" #featherence.user4
	elif file == "Dreamcast_2P_Samba De Amigo.zip": fileID = "2407wbot7t6alzr" #featherence.user4
	
	elif file == "Dreamcast_1P_Sonic Adventure.zip": fileID = "7p877gb0zfsclzl" #featherence.user5
	elif file == "Dreamcast_1P_Rayman 2 - The Great Escape.zip": fileID = "sy884basx1e9fdm" #featherence.user5
	elif file == "Dreamcast_1P_Crazy Taxi.zip": fileID = "o7ps9hb7iyn7v73" #featherence.user5
	
	elif file == "Dreamcast_1P_Jet Grind Radio.zip": fileID = "d9vrc7jll590gby" #featherence.user6
	elif file == "Dreamcast_1P_Resident Evil 3 - Nemesis.zip": fileID = "763t2fmkl6xoqxd" #featherence.user6
	elif file == "Dreamcast_2P_Daytona USA 2001.zip": fileID = "40jl8wu4iatjw7f" #featherence.user6
	
	elif file == "Dreamcast_1P_Grandia II.zip": fileID = "hwfzizwyg8n1fwd" #featherence.user7
	elif file == "Dreamcast_4P_90 Minutes - Sega Championship Football.zip": fileID = "wjv6tz7k330tzru" #featherence.user7
	elif file == "Dreamcast_4P_NFL Blitz 2001.zip": fileID = "sg7nv9jz2jjklpe" #featherence.user7
	
	elif file == "Dreamcast_1P_Airforce Delta.zip": fileID = "qp9ni9hwtiejn04" #featherence.user9
	elif file == "Dreamcast_2P_4 Wheel Thunder.zip": fileID = "tvk2crtgpv50la7" #featherence.user9
	elif file == "Dreamcast_1P_Illbleed.zip": fileID = "stbpzbrtmofinox" #featherence.user9
	
	elif file == "Dreamcast_1P_Alone in the Dark - The New Nightmare.zip": fileID = "8fle779l57z4kf5" #featherence.user11
	
	elif file == "Dreamcast_1P_Sword of the Berserk - Guts Rage.zip": fileID = "nlxzy78c9bsy1oh" #featherence.user12
	elif file == "GameCube_4P_Hot Wheels - Velocity X.zip": fileID = "h4lv9b2h43r9j24" #featherence.user12
	elif file == "GameCube_1P_Luigi's Mansion.zip": fileID = "tu401zv75orudob" #htptuser5
	
	elif file == "Dreamcast_1P_Skies of Arcadia.zip": fileID = "ans8hoynble9s7s" #featherence.user13
	elif file == "Dreamcast_1P_Evolution 2 - Far Off Promise.zip": fileID = "jvwyia29ys2hmkt" #featherence.user13
	
	elif file == "Dreamcast_1P_Headhunter.zip": fileID = "6yl549o5zyts48t" #featherence.user14
	elif file == "Dreamcast_2P_Dead or Alive 2.zip": fileID = "8ahdxi4zw0d4hy5" #featherence.user14
	
	elif file == "Dreamcast_2P_Cyber Troopers Virtual On - Oratorio Tangram.zip": fileID = "pusgq1cl8hqzbud" #featherence.user15
	elif file == "Dreamcast_2P_Marvel vs. Capcom 2.zip": fileID = "vxgcov3dfud8sil" #featherence.user15
	elif file == "Dreamcast_2P_Sega GT.zip": fileID = "pq5mxuo045ctygj" #featherence.user15
	
	elif file == "Dreamcast_1P_Blue Stinger.zip": fileID = "yw72w512amnkf6f" #featherence.user16
	elif file == "Dreamcast_1P_Metropolis Street Racer.zip": fileID = "yjlglju05dyh0ck" #featherence.user16
	elif file == "Dreamcast_2P_Ready 2 Rumble Boxing.zip": fileID = "klfpbqlx7mmjrs1" #featherence.user16
	
	elif file == "Dreamcast_1P_AeroWings 2 - Airstrike.zip": fileID = "cmgiv70684dgdio" #featherence.user17
	elif file == "Dreamcast_4P_V-Rally 2 - Expert Edition.zip": fileID = "4s8z1ya5rgnfm3a" #featherence.user17
	elif file == "Dreamcast_2P_Frogger 2 - Swampy's Revenge.zip": fileID = "v3oyukmbbn6to1d" #featherence.user17
	elif file == "Dreamcast_1P_Ikaruga.zip": fileID = "gxrryumrj9u3br9" #featherence.user17
	
	elif file == "Dreamcast_2P_Confidential Mission.zip": fileID = "f00lw5iu8slv5ks" #featherence.user18
	elif file == "Dreamcast_2P_Flag to Flag.zip": fileID = "6ggdjke6uq1aq3q" #featherence.user18
	elif file == "Dreamcast_2P_Plasma Sword - Nightmare of Bilstein.zip": fileID = "ray1fhclvn23rlf" #featherence.user18
	
	elif file == "Dreamcast_2P_Expendable.zip": fileID = "t1nokjtgb76uqch" #featherence.user19
	elif file == "Dreamcast_1P_Prince of Persia - Arabian Nights.zip": fileID = "6in3lc79e7hiw4h" #featherence.user19
	elif file == "Dreamcast_1P_Tokyo Xtreme Racer 2.zip": fileID = "0g74y3q1ou8nmsr" #featherence.user19
	
	elif file == "Dreamcast_4P_Striker Pro 2000.zip": fileID = "6yml24yioziii8j" #featherence.user20
	elif file == "Dreamcast_4P_Tee Off.zip": fileID = "9rj00cxbcthxsib" #featherence.user20
	elif file == "Dreamcast_2P_Dead or Alive 2.zip": fileID = "5ypl35mj4bysuci" #featherence.user20
	elif file == "Dreamcast_4P_Walt Disney World Quest - Magical Racing Tour.zip": fileID = "drp9hemxgm0wxzb" #featherence.user20
	
	elif file == "Dreamcast_1P_ECCO the Dolphin - Defender of the Future.zip": fileID = "hheupvn8sik5f2q" #featherence.user21
	elif file == "Dreamcast_1P_Record of Lodoss War.zip": fileID = "12rdubuwm8fo51l" #featherence.user21
	elif file == "Dreamcast_2P_Soul Calibur.zip": fileID = "7to98uj6iwgl657" #featherence.user21
	
	elif file == "Dreamcast_1P_Legacy of Kain - Soul Reaver.zip": fileID = "ylhvvpcftm7kxbg" #featherence.guser1
	elif file == "Dreamcast_1P_Chicken Run.zip": fileID = "tfptc1k2gyek83z" #featherence.guser1
	elif file == "Dreamcast_2P_Virtua Fighter 3tb.zip": fileID = "nsvr0pe2hbsqffw" #featherence.guser1
	
	elif file == "Dreamcast_1P_PenPen TriIcelon.zip": fileID = "ge9tpiw7fdw0ofw" #featherence.guser2
	elif file == "Dreamcast_1P_Snow Surfers.zip": fileID = "9hf0jcrrxar34ss" #featherence.guser2
	elif file == "Dreamcast_4P_Exhibition of Speed.zip": fileID = "bsdur801mn9u7l5" #featherence.guser2
	
	elif file == "Dreamcast_1P_KAO the Kangaroo.zip": fileID = "2z1mlgks35y8upf" #featherence.guser3
	elif file == "Dreamcast_1P_Maken X.zip": fileID = "vx81423u25uvb65" #featherence.guser3
	elif file == "Dreamcast_4P_Spawn - In the Demon's Hand.zip": fileID = "tlwo34jfiu4xy61" #featherence.guser3
	
	elif file == "Dreamcast_1P_Donald Duck - Goin' Quackers.zip": fileID = "9ddwvsyxvonbdof" #featherence.guser4
	elif file == "Dreamcast_2P_Power Stone.zip": fileID = "y6n6uhe8fgsacw6" #featherence.guser4
	elif file == "Dreamcast_4P_Bomberman Online.zip": fileID = "58wve2p4xeznrba" #featherence.guser4
	elif file == "Dreamcast_4P_Quake III Arena.zip": fileID = "gitt8vkzijg5ud2" #featherence.guser4

	elif file == "Dreamcast_2P_Tony Hawk's Pro Skater.zip": fileID = "vioqjp3wvhidwjr" #featherence.user50
	elif file == "Dreamcast_1P_Rippin' Riders Snowboarding.zip": fileID = "0j9gv4l8ew4wtcr" #featherence.user50
	elif file == "Dreamcast_1P_Seventh Cross Evolution.zip": fileID = "dl6hetwzduvvpj5" #featherence.user50
	elif file == "Dreamcast_1P_Magforce Racing.zip": fileID = "0nw24vpxmtbpquc" #featherence.user50
	
	elif file == "Dreamcast_4P_ChuChu Rocket!.zip": fileID = "heeb8qqagnphxzl" #featherence.guser6
	elif file == "Dreamcast_4P_Virtua Tennis.zip": fileID = "wu843fsy9eql7wt" #featherence.guser6
	elif file == "Dreamcast_4P_WWF Royal Rumble.zip": fileID = "4o0q92vuewas1s3" #featherence.guser6
	elif file == "Dreamcast_4P_Red Dog - Superior Firepower.zip": fileID = "lahkk5xhkppo9q1" #featherence.guser6
	elif file == "Dreamcast_2P_Gunbird 2.zip": fileID = "4j3dilb8yxkdxdn" #featherence.guser6
	elif file == "Dreamcast_2P_Psychic Force 2012.zip": fileID = "esnf4i1p55dtnmo" #featherence.guser6
	
	elif file == "Dreamcast_2P_Under Defeat.zip": fileID = "mgsvwb0brxdazyr" #featherence.user47
	elif file == "Dreamcast_1P_Spider-Man.zip": fileID = "6djdeqnm2sr5z51" #featherence.user47
	elif file == "Dreamcast_2P_Garou Mark of the Wolves.zip": fileID = "mhz7v5x6vbaoviy" #featherence.user47
	elif file == "Dreamcast_4P_Sega Worldwide Soccer 2000 - Euro Edition.zip": fileID = "5vjlyqk2ihrzpxp" #featherence.user47
	
	elif file == "Dreamcast_2P_Iron Aces.zip": fileID = "lql3v266oymp0w3" #featherence.guser8
	elif file == "Dreamcast_2P_Under Defeat.zip": fileID = "oxuyfp1thzd294m" #featherence.guser8
	elif file == "Dreamcast_2P_Zombie Revenge.zip": fileID = "341gpnc1qvhc6ps" #featherence.guser8
	elif file == "Dreamcast_4P_GigaWing 2.zip": fileID = "gec0iw3mw712lwe" #featherence.guser8
	elif file == "Dreamcast_4P_Toy Commander.zip": fileID = "3mch97gzj160x29" #featherence.guser8
	
	elif file == "Dreamcast_1P_Super Magnetic Neo.zip":
		fileID_L.append('e5y0na0wxub395u') #featherence.guser9
		fileID_L.append('pr2f65l4sgyb5mx') #featherence.guser14
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Dreamcast_4P_Tetris 4D.zip":
		fileID_L.append('gkw2qyvgqnbvjxh') #featherence.guser9
		fileID_L.append('00058przunx5ss9') #featherence.guser14
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Dreamcast_2P_World Series Baseball 2K1.zip":
		fileID_L.append('vl84nsaxl8ub3x4') #featherence.guser9
		fileID_L.append('m30uet1g0z9zo80') #featherence.guser14
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Dreamcast_2P_TrickStyle.zip":
		fileID_L.append('75ig1in12omssr9') #featherence.guser9
		fileID_L.append('xpwmd5q8ky31nr6') #featherence.guser14
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Dreamcast_1P_Time Stalkers.zip": fileID = "ajshhv8ju30i4hh" #featherence.guser9
	elif file == "Dreamcast_4P_Sonic Shuffle.zip": fileID = "vf2466gbp4oyn0v" #featherence.guser9 #500MB FREE
	
	elif file == "Dreamcast_1P_Draconus - Cult of the Wyrm.zip": fileID = "hnqwsz9ojd5jmz4" #featherence.user49
	elif file == "Dreamcast_4P_Power Stone 2.zip": fileID = "ind1zhr75zspyy8" #featherence.user49
	elif file == "Dreamcast_1P_Crazy Taxi 2": fileID = "zf4uaiyavw7j249" #featherence.user49
	elif file == "Dreamcast_1P_Buzz Lightyear of Star Command": fileID = "q60nlnq5nnezwl1" #featherence.user49
	
	elif file == "Dreamcast_2P_Tech Romancer.zip": fileID = "m6342fmoz0x18fa" #featherence.guser11
	elif file == "Dreamcast_2P_Ultimate Fighting Championship.zip": fileID = "3ztpdgjeiglgxzp" #featherence.guser11

	elif file == "Dreamcast_1P_Fighting Force 2.zip": fileID = "owp5a3e8sxj0sh3" #featherence.guser12
	elif file == "Dreamcast_2P_Capcom vs. SNK 2.zip": fileID = "ue73pbxrffpwf3c" #featherence.guser12
	elif file == "Dreamcast_1P_Crazy Taxi 2.zip": fileID = "abgr81mdxxmvex9" #featherence.guser12
	elif file == "Dreamcast_1P_Rez.zip": fileID = "vraq5mgqsd0sqx2" #featherence.guser12
	elif file == "Dreamcast_2P_Test Drive 6.zip": fileID = "ja583d5z77lbvn9" #featherence.guser12
	elif file == "Dreamcast_4P_Propeller Arena.zip": fileID = "41h77xde159helg" #featherence.guser12
	
	elif file == "Dreamcast_1P_Seventh Cross Evolution.zip": fileID = "lddzct1g75fiqk4" #featherence.guser13
	elif file == "Dreamcast_2P_POD - Speedzone.zip": fileID = "ezut8yb2i66nwxd" #featherence.guser13
	elif file == "Dreamcast_2P_Suzuki ALSTARE Extreme Racing.zip": fileID = "f63m0770wh2to90" #featherence.guser13
	elif file == "Dreamcast_2P_Cannon Spike.zip": fileID = "frhxnwxjok071ok" #featherence.guser13
	
	elif file == "Dreamcast_2P_Buggy Heat": fileID = "fh0j7lpyyh3ep89" #featherence.guser14
	
	elif file == "Dreamcast_1P_Industrial Spy - Operation Espionage.zip": fileID = "6hk44eq154qohpo" #featherence.user54
	elif file == "Dreamcast_1P_MDK 2.zip": fileID = "hg1ogro1tv0twq4" #featherence.user54
	elif file == "Dreamcast_1P_Mr Driller.zip": fileID = "qya7f8ezviyuuty" #featherence.user54
	elif file == "Dreamcast_2P_The King of Fighters '99.zip": fileID = "8e83i6xwnai5pme" #featherence.user54
	
	elif file == "GameCube_2P_Dragon Ball Z - Sagas.zip": fileID = "whko171pzg4xvpu" #htptdebugout3
	elif file == "GameCube_1P_Harvest Moon - A Wonderful Life.zip": fileID = "xomv5o1u5abarpg" #htptdebugout4
	elif file == "GameCube_1P_Batman - Dark Tomorrow.zip": fileID = "3wo0r02xzgipd9y" #htptuser3
	elif file == "GameCube_2P_Bust-A-Move 3000.zip": fileID = "iqt9mudq0483wll" #htptuser3
	elif file == "GameCube_2P_Burnout.zip": fileID = "ympk2wnovncjwds" #htptuser4
	elif file == "GameCube_2P_Burnout 2 - Point of Impact.zip": fileID = "pg08xuthz63slcg" #htptuser4
	
	elif file == "GameCube_1P_The Hobbit.zip": fileID = "grjwl1dn5n6v3hd" #htptdebugout
	elif file == "GameCube_1P_Pac-Man World 3.zip": fileID = "nlvtsmh6pdd6mky" #featherence.user23
	elif file == "GameCube_2P_The Legend of Zelda - The Wind Waker.zip": fileID = "zuo9eiuj2a2ne94" #featherence.user56
	elif file == "GameCube_1P_Eternal Darkness.zip": fileID = "qyz7xkxm9z7pc37" #featherence.user55
	elif file == "GameCube_1P_Skies of Arcadia Legends.zip": fileID = "lrhhqtzg5wugume" #featherence.guser26
	elif file == "GameCube_2P_Pokemon Colosseum.zip": fileID = "4rccmdlldfiyxqi" #featherence.user38
	
	elif file == "GameCube_2P_Virtua Striker 2002.zip": fileID = "qjkno0uja4b154m" #featherence.user32
	elif file == "GameCube_4P_Metal Arms - Glitch in the System.zip": fileID = "uvwkvrp6yg8tw2r" #featherence.user32
	
	elif file == "GameCube_2P_Sonic Mega Collection.zip": fileID = "dcx3mtdtgcb3q2a" #featherence.user23
	elif file == "GameCube_2P_Need for Speed - Most Wanted.zip": fileID = "" #NOT WORKING! featherence.user23
	elif file == "GameCube_2P_The Sims Bustin Out.zip": fileID = "inlmjf6lsaezxgs" #featherence.user28
	elif file == "GameCube_2P_LEGO Star Wars - The Video Game.zip": fileID = "qrxh3vu41udqakx" #featherence.user24
	elif file == "GameCube_1P_Beyond Good And Evil.zip": fileID = "ogosdnzb06fbuid" #featherence.user24
	elif file == "GameCube_1P_MegaMan Network Transmission.zip": fileID = "52no9knaz7fx4x4" #featherence.user25
	elif file == "GameCube_2P_Lost Kingdoms 2.zip": fileID = "jwj5efow82r1lwi" #featherence.user25
	
	elif file == "GameCube_4P_1080 Avalanche.zip": fileID = "083elwvzh12f8b8" #featherence.guser21
	elif file == "GameCube_1P_Barnyard.zip": fileID = "ya52mb9fhnniqxg" #featherence.guser21 #Black 1/4 screen
	
	elif file == "GameCube_1P_Ultimate Spider-Man.zip": fileID = "p0484g4119jzi8b" #featherence.user44
	elif file == "GameCube_1P_Spartan - Total Warrior.zip": fileID = "i5c27a8awei1k0z" #featherence.user44
	
	elif file == "GameCube_2P_Sonic Adventure 2 - Battle.zip": fileID = "s5d367qymxmoigh" #featherence.guser22
	elif file == "GameCube_1P_Yu-Gi-Oh! The Falsebound Kingdom.zip": fileID = "c6esgpae2pbw4rh" #featherence.guser22
	
	elif file == "GameCube_2P_Capcom VS SNK 2 EO.zip": fileID = "u1vyisqgwvvkdbq" #featherence.guser23
	elif file == "GameCube_1P_SpongeBob SquarePants - Battle for Bikini Bottom.zip": fileID = "v8prwjjfag2bama" #featherence.guser23
	
	elif file == "GameCube_1P_Resident Evil 3 - Nemesis.zip": fileID = "9u8wbt79c6zev16" #featherence.user57
	elif file == "GameCube_4P_XGIII.zip": fileID = "qicdolmuxsw4evy" #featherence.user57
	elif file == "GameCube_1P_Pikmin.zip": fileID = "jeiy3pht3q2kcmm" #featherence.guser??
	elif file == "GameCube_2P_Bloody Roar Primal Fury.zip": fileID = "fxguxoavyxkchjh" #featherence.user27
	elif file == "GameCube_4P_WWE Day Of Reckoning 2.zip": fileID = "h0qdzpeapt6nk8r" #featherence.user27
	elif file == "GameCube_1P_Rayman 3 - Hoodlum Havoc.zip": fileID = "4hx8geahm9stum9" #featherence.guser??
	elif file == "GameCube_1P_Viewtiful Joe.zip": fileID = "ab4unal3wlq65cr" #featherence.user31
	elif file == "GameCube_1P_Pikmin 2.zip": fileID = "ab6c3ivn1cg1if0" #featherence.user31
	elif file == "GameCube_4P_Custom Robo.zip": fileID = "" #NOT WORKING!
	elif file == "GameCube_1P_Chibi Robo.zip": fileID = "m3oec7vxcen985x" #featherence.user56
	elif file == "GameCube_4P_Def Jam Vendetta.zip": fileID = "zekunpm2ehqo0rp" #featherence.user22
	elif file == "GameCube_4P_Gladius.zip": fileID = "ahvog0vseddtntm" #featherence.user22
	elif file == "GameCube_4P_FIFA Street 2.zip": fileID = "axypvfzxwor788a" #featherence.guser20
	elif file == "GameCube_4P_Mobile Suit Gundam - Gundam vs. Z Gundam.zip": fileID = "gauf1jwg268tsp7" #featherence.guser20
	elif file == "GameCube_4P_Final Fantasy Crystal Chronicles.zip": fileID = "raw54ghb5cghxfr" #htptdebugout
	elif file == "GameCube_4P_Gauntlet - Dark Legacy.zip": fileID = "l8z2iz55tkub33j" #featherence.user28
	elif file == "GameCube_4P_Super Smash Bros Melee.zip": fileID = "va1jvchx86eryv5" #featherence.guser19
	elif file == "GameCube_1P_Vexx.zip": fileID = "7xqbnqafef6j166" #featherence.guser19
	
	elif file == "GameCube_1P_The Legend of Spyro - A New Beginning.zip": fileID = "wusr92t77ozqsuj" #featherence.guser24
	elif file == "GameCube_1P_King Kong.zip": fileID = "dmx9ryunnf631vk" #featherence.guser24
	
	elif file == "GameCube_4P_TimeSplitters 2.zip": fileID = "nhnofqnm6cfvhwq" #featherence.user30
	elif file == "GameCube_2P_Baldur's Gate - Dark Alliance.zip": fileID = "cksb86uf0w87i3t" #featherence.user30
	
	elif file == "GameCube_2P_The Lord of the Rings - The Return of the King.zip": fileID = "xmpa9ecrlilrmz0" #featherence.user33
	elif file == "GameCube_4P_NBA Street Vol 2.zip": fileID = "stdt6dwbktug678" #featherence.user33
	
	elif file == "GameCube_2P_Knockout Kings 2003 2.zip": fileID = "e1043a31c43y3t7" #featherence.user34
	elif file == "GameCube_2P_Mortal Kombat - Deadly Alliance.zip": fileID = "h6v0mvijruye3e1" #featherence.user34
	
	elif file == "GameCube_2P_Tony Hawk's American Wasteland.zip": fileID = "0u39ias29dovu8d" #featherence.user26
	
	elif file == "GameCube_1P_Super Monkey Ball Adventure.zip": fileID = "yrpv3fzxnqd52kh" #featherence.guser13
	elif file == "GameCube_1P_Geist.zip": fileID = "irm0lxcc35c0tik" #featherence.guser28
	elif file == "GameCube_4P_Worms 3D.zip": fileID = "2p9bdstvhsyvuca" #featherence.guser28
	
	elif file == "GameCube_4P_Godzilla - Destroy All Monsters Melee.zip": fileID = "eyyfxhm4o16lm3z" #featherence.user36
	elif file == "GameCube_2P_Fight Night Round 2.zip": fileID = "pg21w7v9vf6nlm1" #featherence.user36
	
	elif file == "GameCube_2P_SSX 3.zip": fileID = "8uvxv4r1rqb6pgi" #featherence.user37
	elif file == "GameCube_1P_Tak and the Power of Juju.zip": fileID = "tdy74pmhw93ax5b" #featherence.user37
	elif file == "GameCube_1P_The Incredible Hulk - Ultimate Destruction.zip": fileID = "eilwozrt4f9fqsi" #featherence.user3
	elif file == "GameCube_1P_Battalion Wars.zip": fileID = "mvpo4uc2mi4pfuw" #featherence.user10
	elif file == "GameCube_2P_SSX Tricky.zip": fileID = "xj6x992avblo56m" #featherence.user10
	elif file == "GameCube_4P_Digimon World 4.zip": fileID = "mkkszlr6il4rc7q" #featherence.user10
	elif file == "GameCube_1P_TY the Tasmanian Tiger.zip": fileID = "8tgsii63y94lzje" #featherence.guser30
	elif file == "GameCube_1P_Star Wars Rogue Squadron II - Rogue Leader.zip": fileID = "z2aommzvxdnaolz" #featherence.guser30
	elif file == "GameCube_1P_P.N.03.zip": fileID = "59796rfj9csxv3o" #featherence.guser31
	elif file == "GameCube_1P_The Simpsons Hit And Run.zip": fileID = "v9dr2ym9p0msffw" #featherence.guser31
	elif file == "GameCube_1P_Spider Man 2.zip": fileID = "paymahssgfwrt1c" #featherence.guser32
	elif file == "GameCube_4P_Viewtiful Joe Red Hot Rumble.zip": fileID = "we1jow8w43xzzly" #featherence.guser32
	elif file == "GameCube_4P_Crash Tag Team Racing.zip": fileID = "bbjqevootnn4y4o" #featherence.guser33
	elif file == "GameCube_4P_Sonic Riders.zip": fileID = "w98uu0tqyo9tvkz" #featherence.guser33
	elif file == "GameCube_4P_Sonic Heroes.zip": fileID = "6j70ncnz1p3vca1" #featherence.user38
	elif file == "GameCube_2P_Need For Speed Underground 2.zip": fileID = "juh4bhi3wr2tm3i" #featherence.user39
	elif file == "GameCube_4P_Wave Race - Blue Storm.zip": fileID = "jv963oaea4fmj90" #featherence.user39
	elif file == "GameCube_1P_Crash Bandicoot The Wrath Of Cortex.zip": fileID = "6ze2dx0lf8vfjkf" #featherence.user40
	elif file == "GameCube_4P_Super Monkey Ball 2.zip": fileID = "hovulkbsqnypjt5" #featherence.user40
	elif file == "GameCube_4P_WWE WRESTLEMANIA 19.zip": fileID = "2bikwiexotc0n5q" #featherence.user41
	elif file == "GameCube_1P_Evolution Worlds.zip": fileID = "ypmaqgt3ayuk7um" #featherence.user41
	elif file == "GameCube_1P_Lost Kingdoms.zip": fileID = "scdowm0p6818exi" #featherence.user42
	elif file == "GameCube_2P_Tony Hawks Pro Skater 3.zip": fileID = "g7zpqhv8zxmoutn" #featherence.user42
	elif file == "GameCube_2P_Rocky.zip": fileID = "j6o2kjcp7wkyhyb" #featherence.user8
	elif file == "GameCube_4P_X-Men Legends II.zip": fileID = "7boqseyn7pprex0" #featherence.user8
	elif file == "GameCube_4P_Conflict - Desert Storm.zip": fileID = "l9jo0em2w4bobxf" #featherence.guser29
	elif file == "GameCube_4P_X-Men Legends.zip": fileID = "csad6xei9znxpr4" #featherence.guser29
	elif file == "GameCube_1P_Power Rangers - Dino Thunder.zip": fileID = "cajp6q438lxvp5m" #featherence.guser34
	elif file == "GameCube_2P_Street Racing Syndicate.zip": fileID = "08dc53hfrnjv7mo" #featherence.guser34
	elif file == "GameCube_4P_Bomberman Jetters.zip": fileID = "w9g3urlf4rdyog2" #featherence.user43
	elif file == "GameCube_4P_Shadow The Hedgehog.zip": fileID = "of9gkwc91eo0v61" #featherence.user43
	elif file == "GameCube_2P_Batman Rise Of Sin Tzu.zip": fileID = "ix5tcxlrcs5ka0u" #featherence.user8
	elif file == "GameCube_2P_Teenage Mutant Ninja Turtles.zip": fileID = "nvxwwr1piadlfoe" #featherence.guser35
	elif file == "GameCube_4P_Teenage Mutant Ninja Turtles 2 - Battle Nexus.zip": fileID = "riodsm03p0mofjb" #featherence.guser35
	elif file == "GameCube_1P_Finding Nemo.zip": fileID = "99t6ku1q7w7czj9" #featherence.guser36 !Error No videos + stuck
	elif file == "GameCube_1P_Ultimate Spider-Man.zip": fileID = "6pff01wgo9x7yxy" #featherence.guser36
	elif file == "GameCube_4P_Teenage Mutant Ninja Turtles 2 - Battle Nexus.zip": fileID = "57d7hgd8fkvm62w" #featherence.guser30
	elif file == "GameCube_4P_Shrek Smash n' Crash Racing.zip": fileID = "yf1j51c74br89qg" #featherence.user45
	elif file == "GameCube_1P_Metroid Prime.zip": fileID = "mswgar93zgrmldt" #featherence.user45
	elif file == "GameCube_1P_Donkey Kong Jungle Beat.zip": fileID = "fovcv8hiz8uee8m" #htpthtpt
	elif file == "GameCube_1P_Looney Tunes - Back in Action.zip": fileID = "2xfm3mb8dmtdkhr" #htpthtpt
	elif file == "GameCube_1P_Paper Mario.zip": fileID = "mrd633ech5qe3b2" #htpthtpt
	elif file == "GameCube_1P_Super Mario Sunshine.zip": fileID = "oc3jghj34uuf98k" #featherence.user46
	elif file == "GameCube_2P_The Legend of Zelda - The Wind Waker.zip": fileID = "" #
	elif file == "GameCube_1P_Fire Emblem - Path Of Radiance.zip": fileID = "ifkx98xibicdqgi" #featherence.user48
	elif file == "GameCube_2P_Disney Pixar Cars.zip": fileID = "xgaht15rxtjakwv" #htpthtpt
	elif file == "GameCube_1P_Winnie the Pooh's Rumbly Tumbly Adventure.zip": fileID = "" #NOT WORKING!
	elif file == "GameCube_4P_Crash Nitro Kart.zip": fileID = "nr7nsj3s5fjcz0m" #infohtpt
	elif file == "GameCube_1P_Resident Evil 4.zip":
		fileID_L.append('383any8nhvuv1j6') #htpthtpt
		fileID_L.append('25147rcdgbc57pr') #featherence.user46
		fileName_L.append('CD1')
		fileName_L.append('CD2')
	elif file == "GameCube_1P_Metal Gear Solid - The Twin Snakes.zip": #
		fileID_L.append('q16v5u5e6grfsje') #htptuser2
		fileID_L.append('pcy0ai21a8ysf09') #htptuser2
		fileName_L.append('CD1')
		fileName_L.append('CD2')
	elif file == "Sony Playstation_2P_Test Drive 5.zip": fileID = "vtrhfh1iqsf9ydz" #featherence.guser35
	
	elif file == ".zip":
		fileID_L.append('[GD]') #featherence.user1 [GD]
		fileID_L.append('') #
		fileID_L.append('') #
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	
	if fileID_L != [""] and fileName_L != ['--> (Exit)'] and fileID == "":
		returned, value = dialogselect('Choose a file to download', fileName_L)
		if returned > 0 and not '-1' in str(returned):
			fileID = fileID_L[int(returned)]
			'''---------------------------'''
		else: fileID = ""
	
	text = "fileID" + space2 + str(fileID) + newline + \
	"fileID_L" + space2 + str(fileID_L)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	return fileID

def searchtrailer(filename):
	from shared_modules3 import *
	name = filename ; url = filename ; desc = "" ; num = "" ; viewtype = ""
	YoutubeSearch(name, url, desc, num, viewtype)
	
def copyarcade(force=False):
	name = 'copyarcade' ; printpoint = ""
	path = os.path.join(rom_path, 'Arcade', '')
	if not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'cfg', '')) and os.path.exists(os.path.join(featherence_emu_module_path,'save','mame', 'cfg', '')):
		printpoint = printpoint + '1'
		setconfig(force=True)
	elif not os.path.exists(path): printpoint = printpoint + '8'
	elif not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'diff', '')) or not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'nvram', '')):
		printpoint = printpoint + '2'
		file = "nvram_diff.zip"
		fileID = getfileID(file)
		notification('Downloading NVRAM and DIFF Arcade settings','','',1000)
		DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+"?dl=1", file, temp_path, os.path.join(emulator_path,'save','MAME 2014', 'mame', ''), percentinfo=2)
	
	elif not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'diff', '')) or not os.path.exists(os.path.join(emulatordata_path,'save','MAME 2014', 'mame', 'nvram', '')):
		printpoint = printpoint + '3'
	
	if '1' in printpoint or '2' in printpoint or '3' in printpoint or force==True:
		printpoint = printpoint + '7'
		notification('copying Arcade settings','CFG, DIFF, NVRAM','',1000)
		source = os.path.join(emulator_path,'save', 'mame')
		target = os.path.join(emulatordata_path,'save', 'MAME 2014', 'mame')
		copyfiles(source, target)
	
	text = "force" + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def installemuconsole(force=False):
	printpoint = ""
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
		notification("OS and hardware are not supported!","www.featherence.com","",2000)
	
	installaddonP('script.module.featherence.emu', update=True)
	if not os.path.exists(emulator_path) and not '6' in printpoint: notification('Featherence Emu Console addon is missing!',"Manual download from addon settings","",4000)

def copyconfig(force=False):
	name = 'copysettings' ; printpoint = "" ; extra = ""
	
	path = config_path2
	if not os.path.exists(path):
		installemuconsole()
	else:
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
			
		if not os.path.exists(config_path) or force==True:
			printpoint = printpoint + '1'
			notification('Recreating configs','','',1000)
			mkdirs()
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
	name = 'keys_help' ; printpoint = ""
	from shared_modules3 import *
	if filename == 'Arcade': url = '&youtube_id=L12S_XuO9kQ'
	elif filename == 'Nintendo': url = '&youtube_id=HrxGGOB8W8M'
	elif filename == 'Nintendo 64': url = '&youtube_id=6U6435hKBnI'
	elif filename == 'Nintendo DS': url = '&youtube_id=mSi8q2g-JIw'
	elif filename == 'Sega Genesis': url = '&youtube_id=H2tOwo4f0AE'
	elif filename == 'Sega Master System': url = '&youtube_id=DcDqe4UmoJI'
	elif filename == 'Sony Playstation': url = '&youtube_id=XHr-svFqDm0'
	elif filename == 'Super Nintendo': url = '&youtube_id=zLHY2ImgHRM'
	elif filename == 'TurboGrafx 16': url = '&youtube_id=DLZwdLiPzqc'
	else:
		url = ''
		printpoint = printpoint + '9'
		notification(addonString(30035).encode('utf-8'),"","",3000)
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
						copyfiles(retroarchcfg_file2, retroarchcfg_file) ; xbmc.sleep(100)
					
					elif file == '.retroarch-core-options.cfg' and systemplatformwindows:
						extra = extra + newline + '.retroarch-core-options.cfg' + space2
						copyfiles(retroarchcoreoptionscfg_file2, retroarchcoreoptionscfg_file) ; xbmc.sleep(100)
					
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
				if 1 + 1 == 2:
					#replace_word(emudata_launcher_file,old_word,new_word, infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'rom/','rom\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'/_','\\_', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'_EN/','_EN\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'_HE/','_HE\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'_RU/','_RU\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'/GO.BAT','\\GO.BAT', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'_Artwork/','_Artwork\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'boxfront/','boxfront\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'screenshot/','screenshot\\', infile_="", LineR=False , LineClean=False)
					replace_word(emudata_launcher_file,'P/','P\\', infile_="", LineR=False , LineClean=False)
			
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
				else: _arcade_args = 'mame2014_libretro.dll'
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

			if systemplatformandroid: _ps1_args = 'start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -e ROM "%rom%" -e LIBRETRO /data/data/com.retroarch/cores/mednafen_psx_libretro_android.so'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _ps1_args = 'pcsx.rearmed'
				elif OS == "i386": _ps1_args = 'mednafen.psx'
				else: _ps1_args = 'mednafen.psx'
			elif systemplatformwindows: _ps1_args = 'mednafen.psx_libretro.dll'
			dp.update(65,'Generating Launchers file',"Setting _ps1_args..")
			replace_word(emudata_launcher_file,'_ps1_args',_ps1_args, infile_="", LineR=False , LineClean=False)

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
				else: _dos_args = 'dosbox'
			elif systemplatformwindows: _dos_args = 'dosbox_libretro.dll'
			dp.update(95,'Generating Launchers file',"Setting _dos_args..")
			replace_word(emudata_launcher_file,'_dos_args',_dos_args, infile_="", LineR=False , LineClean=False)
			
			
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
