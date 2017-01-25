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
	name = 'downloads' ; printpoint = ""
	
	if category != "" and filename != "" and filepath != "":
		if not os.path.exists(os.path.join(filepath)): printpoint = '1'
		else:
			returned = dialogyesno('Folder exist!', 'Would you like to redownload?')
			if returned != 'skip': printpoint = '2'
		
		if printpoint != "":
			if category == 'Featherence_segamastersystem':
				file = "Sega Master System.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sega%20Master%20System.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
		
			elif category == 'Featherence_turbografx16':
				file = "TurboGrafx 16.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/TurboGrafx%2016.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
				
				
			elif category == 'Featherence_segagenesis':
				file = "Sega Genesis.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sega%20Genesis.zip?dl=1", file, temp_path, rom_path, percentinfo=5)
			
			elif category == 'Featherence_nintendo':
				file = "Nintendo.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
			
			elif category == 'Featherence_supernintendo':
				file = "Super Nintendo.zip"
				fileID = getfileID(file)
				DownloadFile("https://www.dropbox.com/s/"+fileID+"/Super%20Nintendo.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
		
			elif category == 'Featherence_nintendo64':
				if launcher == 'Featherence_nintendo641P':
					file = "Nintendo 64_1P.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo%2064_1P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif launcher == 'Featherence_nintendo642P':
					file = "Nintendo 64_2P.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo%2064_2P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif launcher == 'Featherence_nintendo644P':
					file = "Nintendo 64_4P.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Nintendo%2064_4P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
						
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
						DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_2P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
				elif launcher == 'Featherence_arcade3P':
					file = "Arcade_3P.zip"
					fileID = getfileID(file)
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_3P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
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
						DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_4P.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
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
						DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_GEAR.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
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
						DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_FUN.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
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
						DownloadFile("https://www.dropbox.com/s/"+fileID+"/Arcade_ADULT.zip?dl=1", file, temp_path, rom_path, percentinfo=2)
			
			elif category == 'Featherence_nintendods':
				if launcher == 'Featherence_nintendods1P':
					filename_ = '_' + filename.replace(':',"")
					
					if '4225 -' in filename or 'Professor Layton' in filename: file = "Nintendo DS_1P_.zip"
					else: file = "Nintendo DS_1P.zip"
					fileID = getfileID(file)
					filename__ = file.replace(" ", "%20")
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
					
			elif category == 'Featherence_playstation':
				if launcher == 'Featherence_playstation1P':
					filename_ = filename.replace(':',"")
					file = "Sony Playstation_1P_" + filename_ + ".zip"
					fileID = getfileID(file)
					filename__ = filename_.replace(" ", "%20")
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_1P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif launcher == 'Featherence_playstation2P':
					filename_ = filename.replace(':',"")
					file = "Sony Playstation_2P_" + filename_ + ".zip"
					fileID = getfileID(file)
					filename__ = filename_.replace(" ", "%20")
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_2P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
				
				elif launcher == 'Featherence_playstation4P':
					filename_ = filename.replace(':',"")
					file = "Sony Playstation_4P_" + filename_ + ".zip"
					fileID = getfileID(file)
					filename__ = filename_.replace(" ", "%20")
					DownloadFile("https://www.dropbox.com/s/"+fileID+"/Sony%20Playstation_4P_" + filename__ + ".zip?dl=1", file, temp_path, rom_path, percentinfo=2)
	
	text = "category" + space2 + str(category) + newline + \
	"launcher" + space2 + str(launcher) + newline + \
	"rom" + space2 + str(rom) + newline + \
	"filename" + space2 + str(filename) + newline + \
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
	copyconfig(force=value)
	
	
	installemuconsole()
	
	text = ""
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
def chmod():
	if systemplatformlinux:
		os.system('chmod +x '+ emulator_path +'bin/*')
		os.system("export LD_LIBRARY_PATH='"+ emulator_path +"lib/'")
	
def getfileID(file):
	fileID = "" ; fileID_L = [""] ; fileName_L = ['--> (Exit)']
	if file == "linux.featherence.emu.zip": fileID = "1i7zhab80o8chyn" #finalmakerr
	elif file == "nvram_diff.zip":
		fileID_L.append('msw4odgs3ydipo7') #debugout1
		fileID_L.append('xsmyxnqfso08y60') #user23
		fileID_L.append('itg5n8msf3worpn') #debugout2
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "_Artworks.zip":
		fileID_L.append('zrsm0pnnd18bsqv') #debugout4
		fileID_L.append('v4m7dx4448mwlxj') #debugout3
		fileID_L.append('nfb5s7garbwdoj4') #user16
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	
	elif file == "Arcade_1P.zip":
		fileID_L.append('7yfdgvzhduoihn3') #user2
		fileID_L.append('6wgx2fnsg4le83w') #htpt
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_1P_Turret Tower.zip":
		fileID = "usyvftx1cx85528" #user1
	
	elif file == "Arcade_2P.zip":
		fileID_L.append('ccaqjedfl22e3ul') #user2
		fileID_L.append('89gy9rn4qd64eln') #htpt
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')

	elif file == "Arcade_2P_Age Of Heroes - Silkroad 2.zip": fileID = "895suamvsymjpno" #user3
	elif file == "Arcade_2P_Area 51.zip":
		fileID_L.append('zgg4mpg6dh71z02') #user2
		fileID_L.append('nwr1p6pthf4x56r') #user3
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Area 51 Maximum Force Duo v2.0.zip": fileID = "o85q8ug25q9mp2l" #user4
	elif file == "Arcade_2P_Demon Front.zip":
		fileID_L.append('txhs5uh9clmc3r6') #user3
		fileID_L.append('ayhbrx2w0bd8h8v') #user1
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Flame Gunner.zip":
		fileID_L.append('vuijmkadpd046zq') #user3
		fileID_L.append('') #
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Garou - Mark of the Wolves.zip":
		fileID_L.append('vto2ejyf6c1ujdi') #user4
		fileID_L.append('y2wgykv8e4h8yct') #user1
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Killer Instinct.zip":
		fileID_L.append('r8fe105ibq1q5h1') #user3
		fileID_L.append('razg6k6kx4r3anj') #user2
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Killer Instinct 2.zip":
		fileID_L.append('fpypqhka6xpgitp') #user2
		fileID_L.append('ivkug7s9cqwmle3') #user4
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Lansquenet 2004.zip": fileID = "guveg252aaulyt6" #user3
	elif file == "Arcade_2P_Mace The Dark Age.zip":
		fileID_L.append('0fnst5ov2muys5r') #user15
		fileID_L.append('xbc793jnfkv08ig') #user2
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Metal Slug 3.zip":
		fileID_L.append('19d6olgmwnck2mm') #user16
		fileID_L.append('r7l3ay23pop3vt2') #user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Metal Slug 4.zip":
		fileID_L.append('c4gev22fialfe3l') #user16
		fileID_L.append('m9vvqp6qv3zzcwv') #user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Metal Slug 5.zip":
		fileID_L.append('z06jeyo28muofkn') #user16
		fileID_L.append('vez9r4w9fk1wah4') #user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Prehistoric Isle 2.zip":
		fileID_L.append('xkupgotlujvj85s') #user15
		fileID_L.append('yxtqtuk9o787ooo') #user17
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Rage of the Dragons.zip":
		fileID_L.append('k39kc1mvodbg043') #user15
		fileID_L.append('4gcdai4k67tm0nv') #user17
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Red Earth.zip":
		fileID_L.append('9hhzwyqmk2ucpza') #user15
		fileID_L.append('engk0ny84jm6tk3') #user13
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Sengoku 3.zip":
		fileID_L.append('4ic19rfzksh6xfh') #user3
		fileID_L.append('drj6txmxc4solns') #user2
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_SNK vs. Capcom - SVC Chaos.zip":
		fileID_L.append('ghzus8r4jtd9ysb') #user2
		fileID_L.append('i9bev4l2ezw344t') #user3
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Street Fighter III 3rd Strike Fight for the Future.zip":
		fileID_L.append('lkl0it20ui5gi70') #user11
		fileID_L.append('lkou7298nbfm0sw') #user13
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Tekken Tag Tournament.zip":
		fileID_L.append('y85tbiwx1t5y29d') #user5
		fileID_L.append('7i5kxmk5d6g0cfj') #user9
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_Tenth Degree.zip": fileID = "gjcgxchm9qyb58c" #
	elif file == "Arcade_2P_Tekken 3.zip":
		fileID_L.append('n292k4l4rzdgxdf') #user5
		fileID_L.append('m1qg58ukl1f4xve') #user9
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_The Crystal of Kings.zip":
		fileID_L.append('xh7444nz8urd69o') #user5
		fileID_L.append('urk6eqnvmxxk1pv') #user9
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_The King of Fighters '98 - The Slugfest.zip":
		fileID_L.append('pnl27a9n5ehqulg') #user4
		fileID_L.append('tzm0tk9pgdj2qg5') #user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_The King of Fighters 2002.zip":
		fileID_L.append('p4xyb1efbbu1u36') #user4
		fileID_L.append('3073773k6010fdk') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_2P_The Last Blade 2.zip":
		fileID_L.append('l0v1h690y55yx8j') #user15
		fileID_L.append('qrlctae8cd6omml') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')

	elif file == "Arcade_3P.zip":
		fileID_L.append('j6bl5uaa01uzspj') #user2
		fileID_L.append('ix147pc6kx3d4ku') #htpt
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_4P.zip":
		fileID_L.append('5alcp543pmyqrzh') #user2
		fileID_L.append('ps0tzg70af5d9nj') #htpt
		fileID_L.append('') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
		
	elif file == "Arcade_4P_Gauntlet Dark Legacy.zip":
		fileID_L.append('oijy0kiz0l792xc') #user14
		fileID_L.append('l53nlcya5phrlp5') #debugout2
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	elif file == "Arcade_4P_Gauntlet Legends.zip": fileID = "jdrbwfesdgm97tr" #info
	elif file == "Arcade_ADULT.zip":
		fileID_L.append('dzbucsurdxfx8lk') #user4
		fileID_L.append('rg4m5oi50c0g4e7') #user2
		fileID_L.append('gabtdr7exw1s9x4') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
		
	elif file == "Arcade_GEAR.zip":
		fileID_L.append('v0si3xo3pt72xpa') #user34
		fileID_L.append('xn0t39q28xan2t6') #htpt
		fileID_L.append('tffxq1rku4n0b3r') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
		
	elif file == "Arcade_GEAR_California Speed.zip": fileID = "gbfxppac8bbnw2b" #info
	elif file == "Arcade_GEAR_Hyperdrive.zip":
		fileID_L.append('dqa6ql7tzb9e6xb') #user4
		fileID_L.append('wlmirerbe5dpezq') #user15
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		
	elif file == "Arcade_FUN.zip":
		fileID_L.append('p64howpq8a0p3yy') #user23
		fileID_L.append('1q8f4gv6ra6ritp') #htpt
		fileID_L.append('xp1k65cp1f9ltai') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo 64_1P.zip":
		fileID_L.append('jp4xzb03m7nbghp') #buy
		fileID_L.append('iu9ntsgd5g4csnw') #htpt
		fileID_L.append('75u5jhdbep4t8ub') #user34
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo 64_2P.zip":
		fileID_L.append('liq3qlqvjef9yjm') #buy
		fileID_L.append('vmc7dedt0516cb0') #htpt
		fileID_L.append('8p3vke6gwcs7pw5') #user34
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo 64_4P.zip":
		fileID_L.append('c3ddp0m09kn35p6') #buy
		fileID_L.append('12o4qm2ys6pyczl') #htpt
		fileID_L.append('c8cf8stqy28rndz') #user34
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo.zip":
		fileID_L.append('nt05zl4ygnynxen') #user1
		fileID_L.append('5ahtgh6bjq1gn42') #htpt
		fileID_L.append('ie9dlkr4xxv44s7') #user34
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo DS_1P.zip":
		fileID_L.append('e7e3yaudsjp629n') #user16
		fileID_L.append('tajqg91605p22m2') #debugout1
		fileID_L.append('e5oh0k4ixhnqlk8') #user3
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Nintendo DS_1P_.zip":
		fileID_L.append('su8o3qbbickjk81') #info
		fileID_L.append('8rk5qwv3t9whb4c') #htpt
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
	
	elif file == "Sega Genesis.zip":
		fileID_L.append('b8lph86pb4b5e0l') #user1
		fileID_L.append('wzn29u4rg0251sq') #htpt
		fileID_L.append('f8orv8r0hgrgm43') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Sega Master System.zip":
		fileID_L.append('c5ingtyhgkwjmx7') #user1
		fileID_L.append('3v6kt7hcj4udnrq') #htpt
		fileID_L.append('nbzv9gotdcksbng') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Super Nintendo.zip":
		fileID_L.append('dficnt390sp2j8w') #user1
		fileID_L.append('fn27r1mmyos91hd') #htpt
		fileID_L.append('rlsyu3fa8pusvs3') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "TurboGrafx 16.zip":
		fileID_L.append('0zg9x4uw1hrm8zb') #user1
		fileID_L.append('nn7rdkeke5vxm10') #htpt
		fileID_L.append('r6dw9ippymncpo4') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	
	
	elif file == "Sony Playstation_1P_Alundra.zip": fileID = "8ajszedon75tzwx" #user12
	elif file == "Sony Playstation_1P_Ape Escape.zip": fileID = "2fcd8w79gplfqxm" #user12
	elif file == "Sony Playstation_1P_Battle Hunter.zip": fileID = "bnltlp9nqovzare" #user12
	elif file == "Sony Playstation_1P_Brigandine - The Legend of Forsena.zip": fileID = "t3if5116f3z5ok2" #user12
	elif file == "Sony Playstation_1P_Bust-a-Move '99.zip": fileID = "r31jozc8ujr0z5i" #user12
	elif file == "Sony Playstation_1P_Castlevania - Symphony Of The Night.zip": fileID = "1d8sik6zdjp5ago" #user8
	elif file == "Sony Playstation_1P_Chrono Cross.zip": fileID = "blx6e047sty05ga" #user12
	elif file == "Sony Playstation_1P_Command & Conquer.zip": fileID = "zw7gt9f65fbj9eu" #user13
	elif file == "Sony Playstation_1P_Command & Conquer - Red Alert.zip": fileID = "5m9je5lv7ed2y83" #user13
	elif file == "Sony Playstation_1P_Command & Conquer - Red Alert - Retaliation.zip": fileID = "k6vmk2hy7ir61mn" #user14
	elif file == "Sony Playstation_1P_Crash Bandicoot.zip":
		fileID_L.append('st3jd9y0no8pbn0') #user5
		fileID_L.append('0jo5bm41o08orpm') #htpt
		fileID_L.append('qid216wds25xr0i') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Sony Playstation_1P_Crash Bandicoot 2.zip":
		fileID_L.append('m0hnjiy8sup4jtv') #user7
		fileID_L.append('x1xnbiwetx1x8q5') #htpt
		fileID_L.append('gzvtu17iebdflze') #buy
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Sony Playstation_1P_Crash Bandicoot 3.zip":
		fileID_L.append('lduolj8k0n4wwld') #user14
		fileID_L.append('jz2fpm9lrh8udzm') #user34
		fileID_L.append('ukehtps2kbxlea9') #info
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')
		fileName_L.append('Source 3')
	elif file == "Sony Playstation_1P_Digimon World.zip": fileID = "qhnqm6wejqtzhzt" #
	elif file == "Sony Playstation_1P_Digimon World 2.zip": fileID = "o6unftle6in4oz5" #user13
	elif file == "Sony Playstation_1P_Digimon World 3.zip": fileID = "esiv8i4on1h6wso" #user7
	elif file == "Sony Playstation_1P_Dino Crisis.zip": fileID = "2efwp6im1aotg8v" #user12
	elif file == "Sony Playstation_1P_Dino Crisis 2.zip": fileID = "awmx89zo20kmks4" #user7
	elif file == "Sony Playstation_1P_Disney's Hercules Action Game.zip": fileID = "0lbyhyvt8qmpsc1" #user12
	elif file == "Sony Playstation_1P_Dragon Valor.zip": fileID = "7q43b820d8hd71i" #user5
	elif file == "Sony Playstation_1P_Driver.zip": fileID = "553sd3fh7lpoumn" #user12
	elif file == "Sony Playstation_1P_Final Fantasy VII.zip": fileID = "85llpgfjz4uih2z" #user7
	elif file == "Sony Playstation_1P_Final Fantasy VIII.zip": fileID = "gt5its29qvdt4f9" #user6
	elif file == "Sony Playstation_1P_Final Fantasy IX.zip":
		fileID_L.append('i09gmh6nqruibmu') #user19
		fileID_L.append('rgivtj2fjbbekvj') #user27
		fileName_L.append('CD1-2')
		fileName_L.append('CD3-4')
	
	elif file == "Sony Playstation_1P_Front Mission 3.zip": fileID = "3dwdqau409oe5m8" #user19
	elif file == "Sony Playstation_1P_Galerians.zip": fileID = "cstcaokpbmsvbxx" #user19
	elif file == "Sony Playstation_1P_Grand Theft Auto 2.zip": fileID = "zti40bzu1o5e2os" #user8
	elif file == "Sony Playstation_1P_Jackie Chan Stuntmaster.zip": fileID = "kbm6jb9pvg9fyza" #user8
	elif file == "Sony Playstation_1P_Lunar - Silver Star Story Complete.zip": fileID = "l85h27qa1qt9sdh" #user21
	elif file == "Sony Playstation_1P_Mega Man Legends.zip": fileID = "zjdxzliibvtl1df" #user21
	elif file == "Sony Playstation_1P_Mega Man X4.zip": fileID = "8kopww6klbqn0jq" #user8
	elif file == "Sony Playstation_1P_Mega Man X5.zip": fileID = "9f6bk6px1wtauxp" #user14
	elif file == "Sony Playstation_1P_Mega Man X6.zip": fileID = "impb58cqacc3ba1" #user14
	elif file == "Sony Playstation_1P_Metal Gear Solid.zip": fileID = "zreea6rsbo6t7ca" #user8
	elif file == "Sony Playstation_1P_Metal Gear Solid VR Missions.zip": fileID = "tql0ori6cqge22s" #user21
	elif file == "Sony Playstation_1P_Oddworld - Abes Oddysee.zip": fileID = "gbibjsf4mzhbq0w" #user21
	elif file == "Sony Playstation_1P_Pacman World.zip": fileID = "5j36isrgl4pasx7" #user5
	elif file == "Sony Playstation_1P_Parasite Eve 2.zip": fileID = "j7ok6yv3k1aljpk" #user22
	elif file == "Sony Playstation_1P_Populous - The Beginning.zip": fileID = "u3s4s391tz2vayc" #user22
	elif file == "Sony Playstation_1P_Railroad Tycoon II.zip": fileID = "v272g24r6ii5djn" #user22
	elif file == "Sony Playstation_1P_Rayman Brain Games.zip": fileID = "z07w776e6o62xwt" #user22
	elif file == "Sony Playstation_1P_Rayman Rush.zip": fileID = "vn5ssuexnirgmb3" #user22
	elif file == "Sony Playstation_1P_Resident Evil 2.zip": fileID = "pafqxpgs1qhhgw5" #user17
	elif file == "Sony Playstation_1P_Resident Evil 3.zip": fileID = "5m8ln06e5ehc6oh" #user17
	elif file == "Sony Playstation_1P_Road Rash 3D.zip": fileID = "my6lt21oixpuy3l" #user5
	elif file == "Sony Playstation_1P_Silent Hill.zip": fileID = "ryfa2ekrjoe8aa6" #user17
	elif file == "Sony Playstation_1P_Spider-Man.zip": fileID = "e2wc0xa7pk85sf1" #user6
	elif file == "Sony Playstation_1P_Spider-Man 2 - Enter Electro.zip": fileID = "icecnzvirlewruv" #user17
	elif file == "Sony Playstation_1P_Spyro Year of the Dragon.zip": fileID = "c8j2hgeyd6x33xi" #user9
	elif file == "Sony Playstation_1P_Spyro 2 - Riptos Rage.zip": fileID = "m5fa4oj1m1vbv1h" #user17
	elif file == "Sony Playstation_1P_Suikoden.zip": fileID = "3opm0of6yblj7x1" #user20
	elif file == "Sony Playstation_1P_Super Shot Soccer.zip": fileID = "x0cu2c8up654ca9" #user18
	elif file == "Sony Playstation_1P_Syphon Filter.zip": fileID = "xbcwozn9f2cvzxu" #user18
	elif file == "Sony Playstation_1P_Tales of Destiny.zip": fileID = "xtzt22coc1omcko" #user9
	elif file == "Sony Playstation_1P_Tales of Destiny II.zip": fileID = "wb0xqy8tqc38r63" #user18
	elif file == "Sony Playstation_1P_Tenchu 2 - Birth Of The Stealth Assassins.zip": fileID = "vkpx8d21b517a1g" #user18
	elif file == "Sony Playstation_1P_The Legend of Dragoon.zip": fileID = "cp6foxr496i78ay" #user9
	elif file == "Sony Playstation_1P_Theme Hospital.zip": fileID = "rwofbkoodqr5m17" #user18
	elif file == "Sony Playstation_1P_Thousand Arms.zip": fileID = "h8dieiggps4km5z" #user20
	elif file == "Sony Playstation_1P_Tigger's Honey Hunt.zip": fileID = "2h9ieslidi0hnae" #user4
	elif file == "Sony Playstation_1P_Valkyrie Profile.zip": fileID = "bc9gg84b9r39ewx" #user20
	elif file == "Sony Playstation_1P_WarCraft II - The Dark Saga.zip": fileID = "prnuctnm8zls2ce" #user23
	elif file == "Sony Playstation_1P_Warhammer - Dark Omen.zip": fileID = "sn8irts9j710jmw" #user23
	
	elif file == "Sony Playstation_2P_Bloody Roar II.zip": fileID = "monmvljc2xh48od" #user23
	elif file == "Sony Playstation_2P_Bomberman Fantasy Race.zip": fileID = "28je9q85l4tibzc" #user23
	elif file == "Sony Playstation_2P_Bomberman World.zip": fileID = "p00rtmr02r7stoq" #user23
	elif file == "Sony Playstation_2P_Diablo.zip": fileID = "k05atfov22r8ywu" #user10
	elif file == "Sony Playstation_2P_Digimon Digital Card Battle.zip": fileID = "s4sw4flxxzz64ca" #user10
	elif file == "Sony Playstation_2P_Digimon Rumble Arena.zip": fileID = "npgiws620kteu8x" #user10
	elif file == "Sony Playstation_2P_Fighting Force.zip": fileID = "jep1hofgub7vuef" #tulu
	elif file == "Sony Playstation_2P_Gauntlet Legends.zip": fileID = "g4qcakkuz3hxne6" #user10
	elif file == "Sony Playstation_2P_Gran Turismo 2.zip": fileID = "2ptmzcafa9amtbq" #user27
	elif file == "Sony Playstation_2P_Mega Man 8.zip": fileID = "mx2wsf5zjyk6qk8" #user
	elif file == "Sony Playstation_2P_Metal Slug X.zip": fileID = "nhlpyhikcbbowb9" #user10
	elif file == "Sony Playstation_2P_Moto Racer World Tour.zip": fileID = "ps07jb486i6oiav" #user10
	elif file == "Sony Playstation_2P_Need For Speed III - Hot Pursuit.zip": fileID = "xflg3q638bd57f3" #user
	elif file == "Sony Playstation_2P_NHL Open Ice.zip": fileID = "1alwsil1x4jeao0" #user10
	elif file == "Sony Playstation_2P_Re-Loaded.zip": fileID = "gke0d4uw1s3ce5l" #fix
	elif file == "Sony Playstation_2P_Rival Schools.zip": fileID = "lxlwycnvtsmdll5" #user
	elif file == "Sony Playstation_2P_Running Wild.zip": fileID = "nwl1uahiwoyowjq" #user10
	elif file == "Sony Playstation_2P_Small Soldiers.zip": fileID = "ylc3mmdqyqduyu0" #fix
	elif file == "Sony Playstation_2P_Speed Punks.zip": fileID = "k05atfov22r8ywu" #user10
	elif file == "Sony Playstation_2P_Street Fighter Alpha 3.zip": fileID = "a06awji699g86h0" #user11
	elif file == "Sony Playstation_2P_Super Puzzle Fighter II Turbo.zip": fileID = "acfsgyrxt3vqfjk" #user
	elif file == "Sony Playstation_2P_Syphon Filter 2.zip": fileID = "f9g6t8mkisybzev" #user11
	elif file == "Sony Playstation_2P_Tekken 3.zip": fileID = "mxhx48jousad3zg" #fix
	elif file == "Sony Playstation_2P_Test Drive 5.zip": fileID = "ft1qjwsj5korqi3" #fix
	elif file == "Sony Playstation_2P_Thrill Kill.zip": fileID = "ooyshbkenk68gpl" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater.zip": fileID = "4nopoihpr7zo9yo" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 2.zip": fileID = "xx9kyy4g0n7nfq5" #user11
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 3.zip": fileID = "8npbop2z33gaubn" #fix
	elif file == "Sony Playstation_2P_Tony Hawk's Pro Skater 4.zip": fileID = "xiz3j6dpcao86ou" #fix
	elif file == "Sony Playstation_2P_Twisted Metal 2.zip": fileID = "yi8a2jze1w6j7mf" #user11
	elif file == "Sony Playstation_2P_Twisted Metal 3.zip": fileID = "owddyt09auhirg7" #fix
	elif file == "Sony Playstation_2P_Twisted Metal 4.zip": fileID = "i6riyjeulk01j03" #fix
	elif file == "Sony Playstation_2P_Worms World Party.zip": fileID = "4dplcbknvt3v8nt" #tulu
	elif file == "Sony Playstation_2P_WWF Attitude.zip": fileID = "0fcs44bmfl0kan6" #tulu
	elif file == "Sony Playstation_2P_Vigilante 8 - 2nd Offense.zip": fileID = "3fpblfwgwkd734l" #tulu
	
	elif file == "Sony Playstation_4P_Crash Bash.zip":
		fileID_L.append('afaane71ersuibs') #tulu
		fileID_L.append('9baiwsh35hutzo2') #user34
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
		fileID_L.append('ibgnouatrbli7w7') #user34
		fileName_L.append('Source 1')
		fileName_L.append('Source 2')

		
	elif file == "Dreamcast_2P_Project Justice - Rival Schools 2": fileID = "n9mnlaffe27f3h1" #featherence.user1
	elif file == "Dreamcast_2P_Sonic Adventure 2": fileID = "gyehvme4ky3bo93" #featherence.user1
	elif file == "Dreamcast_1P_Headhunter": fileID = "" #featherence.user2 #NEED TO FILL!!!
	elif file == "Dreamcast_2P_Street Fighter III - 3rd Strike": fileID = "tew77v2lqhybj2j" #featherence.user2
	elif file == "Dreamcast_1P_Skies of Arcadia": fileID = "" #featherence.user3
	
	elif file == "Dreamcast_2P_Capcom vs. SNK": fileID = "7373ygc3fk66rtq" #featherence.user4
	elif file == "Dreamcast_2P_Samba De Amigo": fileID = "2407wbot7t6alzr" #featherence.user4
	
	elif file == "Dreamcast_1P_Sonic Adventure": fileID = "7p877gb0zfsclzl" #featherence.user5
	elif file == "Dreamcast_1P_Rayman 2 - The Great Escape": fileID = "sy884basx1e9fdm" #featherence.user5
	elif file == "Dreamcast_1P_Crazy Taxi": fileID = "o7ps9hb7iyn7v73" #featherence.user5
	
	elif file == "Dreamcast_1P_Jet Grind Radio": fileID = "d9vrc7jll590gby" #featherence.user6
	elif file == "Dreamcast_1P_Resident Evil 3 - Nemesis": fileID = "763t2fmkl6xoqxd" #featherence.user6
	elif file == "Dreamcast_2P_Daytona USA 2001": fileID = "40jl8wu4iatjw7f" #featherence.user6
	
	elif file == "Dreamcast_1P_Grandia II": fileID = "hwfzizwyg8n1fwd" #featherence.user7
	elif file == "Dreamcast_4P_90 Minutes - Sega Championship Football": fileID = "wjv6tz7k330tzru" #featherence.user7
	elif file == "Dreamcast_4P_NFL Blitz 2001": fileID = "sg7nv9jz2jjklpe" #featherence.user7
	
	elif file == "Dreamcast_1P_Airforce Delta": fileID = "qp9ni9hwtiejn04" #featherence.user9 (Possibly disc2 missing!)
	elif file == "Dreamcast_2P_4 Wheel Thunder": fileID = "tvk2crtgpv50la7" #featherence.user9
	elif file == "Dreamcast_1P_Illbleed": fileID = "stbpzbrtmofinox" #featherence.user9
	
	elif file == "Dreamcast_1P_Alone in the Dark - The New Nightmare": fileID = "8fle779l57z4kf5" #featherence.user11
	
	elif file == "Dreamcast_1P_Sword of the Berserk - Guts Rage": fileID = "nlxzy78c9bsy1oh" #featherence.user12 #1.35GB FREE
	
	elif file == "Dreamcast_1P_Skies of Arcadia": fileID = "ans8hoynble9s7s" #featherence.user13
	elif file == "Dreamcast_1P_Evolution 2 - Far Off Promise": fileID = "jvwyia29ys2hmkt" #featherence.user13
	
	elif file == "Dreamcast_1P_Headhunter": fileID = "6yl549o5zyts48t" #featherence.user14
	elif file == "Dreamcast_2P_Dead or Alive 2": fileID = "8ahdxi4zw0d4hy5" #featherence.user14
	
	elif file == "Dreamcast_2P_Cyber Troopers Virtual On - Oratorio Tangram": fileID = "pusgq1cl8hqzbud" #featherence.user15
	elif file == "Dreamcast_2P_Marvel vs. Capcom 2": fileID = "vxgcov3dfud8sil" #featherence.user15
	elif file == "Dreamcast_2P_Sega GT": fileID = "pq5mxuo045ctygj" #featherence.user15
	
	elif file == "Dreamcast_1P_Blue Stinger": fileID = "yw72w512amnkf6f" #featherence.user16
	elif file == "Dreamcast_1P_Metropolis Street Racer": fileID = "yjlglju05dyh0ck" #featherence.user16
	elif file == "Dreamcast_2P_Ready 2 Rumble Boxing": fileID = "klfpbqlx7mmjrs1" #featherence.user16
	
	elif file == "Dreamcast_1P_AeroWings 2 - Airstrike": fileID = "cmgiv70684dgdio" #featherence.user17
	elif file == "Dreamcast_4P_V-Rally 2 - Expert Edition": fileID = "4s8z1ya5rgnfm3a" #featherence.user17
	
	elif file == "Dreamcast_2P_Confidential Mission": fileID = "f00lw5iu8slv5ks" #featherence.user18
	elif file == "Dreamcast_2P_Flag to Flag": fileID = "6ggdjke6uq1aq3q" #featherence.user18
	elif file == "Dreamcast_2P_Plasma Sword - Nightmare of Bilstein": fileID = "ray1fhclvn23rlf" #featherence.user18
	
	elif file == "Dreamcast_2P_Expendable": fileID = "t1nokjtgb76uqch" #featherence.user19
	elif file == "Dreamcast_1P_Prince of Persia - Arabian Nights": fileID = "6in3lc79e7hiw4h" #featherence.user19
	elif file == "Dreamcast_1P_Tokyo Xtreme Racer 2": fileID = "0g74y3q1ou8nmsr" #featherence.user19
	
	elif file == "Dreamcast_4P_Striker Pro 2000": fileID = "6yml24yioziii8j" #featherence.user20
	elif file == "Dreamcast_4P_Tee Off": fileID = "9rj00cxbcthxsib" #featherence.user20
	elif file == "Dreamcast_2P_Dead or Alive 2": fileID = "5ypl35mj4bysuci" #featherence.user20
	elif file == "Dreamcast_4P_Walt Disney World Quest - Magical Racing Tour": fileID = "drp9hemxgm0wxzb" #featherence.user20
	
	elif file == "Dreamcast_1P_ECCO the Dolphin - Defender of the Future": fileID = "hheupvn8sik5f2q" #featherence.user21
	elif file == "Dreamcast_1P_Record of Lodoss War": fileID = "12rdubuwm8fo51l" #featherence.user21
	elif file == "Dreamcast_2P_Soul Calibur": fileID = "7to98uj6iwgl657" #featherence.user21
	
	elif file == "Dreamcast_1P_Legacy of Kain - Soul Reaver": fileID = "ylhvvpcftm7kxbg" #featherence.guser1
	elif file == "Dreamcast_1P_Chicken Run": fileID = "tfptc1k2gyek83z" #featherence.guser1
	elif file == "Dreamcast_2P_Virtua Fighter 3tb": fileID = "nsvr0pe2hbsqffw" #featherence.guser1
	
	elif file == "Dreamcast_1P_KAO the Kangaroo": fileID = "2z1mlgks35y8upf" #featherence.guser3
	elif file == "Dreamcast_1P_Maken X": fileID = "vx81423u25uvb65" #featherence.guser3
	elif file == "Dreamcast_4P_Spawn - In the Demon's Hand": fileID = "tlwo34jfiu4xy61" #featherence.guser3
	
	elif file == "Dreamcast_1P_Donald Duck - Goin' Quackers": fileID = "9ddwvsyxvonbdof" #featherence.guser4
	elif file == "Dreamcast_2P_Power Stone": fileID = "y6n6uhe8fgsacw6" #featherence.guser4
	elif file == "Dreamcast_4P_Bomberman Online": fileID = "58wve2p4xeznrba" #featherence.guser4
	elif file == "Dreamcast_4P_Quake III Arena": fileID = "gitt8vkzijg5ud2" #featherence.guser4

	elif file == "Dreamcast_2P_Tony Hawk's Pro Skater": fileID = "vioqjp3wvhidwjr" #featherence.guser5
	
	elif file == "Dreamcast_4P_ChuChu Rocket!": fileID = "heeb8qqagnphxzl" #featherence.guser6
	elif file == "Dreamcast_4P_Virtua Tennis": fileID = "wu843fsy9eql7wt" #featherence.guser6
	elif file == "Dreamcast_4P_WWF Royal Rumble": fileID = "4o0q92vuewas1s3" #featherence.guser6
	elif file == "Dreamcast_4P_Red Dog - Superior Firepower": fileID = "lahkk5xhkppo9q1" #featherence.guser6
	elif file == "Dreamcast_2P_Gunbird 2": fileID = "4j3dilb8yxkdxdn" #featherence.guser6
	elif file == "Dreamcast_2P_Psychic Force 2012": fileID = "esnf4i1p55dtnmo" #featherence.guser6
	
	elif file == "Dreamcast_2P_Under Defeat": fileID = "mgsvwb0brxdazyr" #featherence.guser7
	elif file == "Dreamcast_1P_Spider-Man": fileID = "6djdeqnm2sr5z51" #featherence.guser7
	elif file == "Dreamcast_2P_Garou Mark of the Wolves": fileID = "mhz7v5x6vbaoviy" #featherence.guser7
	elif file == "Dreamcast_4P_Sega Worldwide Soccer 2000 - Euro Edition": fileID = "5vjlyqk2ihrzpxp" #featherence.guser7
	
	elif file == "Dreamcast_2P_Iron Aces": fileID = "lql3v266oymp0w3" #featherence.guser8
	elif file == "Dreamcast_2P_Under Defeat": fileID = "oxuyfp1thzd294m" #featherence.guser8
	elif file == "Dreamcast_2P_Zombie Revenge": fileID = "341gpnc1qvhc6ps" #featherence.guser8
	elif file == "Dreamcast_4P_GigaWing 2": fileID = "gec0iw3mw712lwe" #featherence.guser8
	elif file == "Dreamcast_4P_Toy Commander": fileID = "3mch97gzj160x29" #featherence.guser8
	
	elif file == "Dreamcast_1P_Fighting Force 2": fileID = "owp5a3e8sxj0sh3" #featherence.guser12
	elif file == "Dreamcast_2P_Capcom vs. SNK 2": fileID = "ue73pbxrffpwf3c" #featherence.guser12 #MORE!
	
	
	
	if fileID_L != [""] and fileName_L != ['--> (Exit)'] and fileID == "":
		returned, value = dialogselect('Choose a file to download', fileName_L)
		if returned > 0 and not '-1' in str(returned):
			fileID = fileID_L[int(returned)]
			'''---------------------------'''
		else:
			fileID = ""
	return fileID

def searchtrailer(filename):
	from shared_modules3 import *
	name = filename ; url = filename ; desc = "" ; num = "" ; viewtype = ""
	YoutubeSearch(name, url, desc, num, viewtype)
	
def copyarcade(force=False):
	name = 'copyarcade' ; printpoint = ""
	path = os.path.join(rom_path, 'Arcade', '')
	if not os.path.exists(os.path.join(emulatordata_path,'save','mame', 'cfg', '')) and os.path.exists(os.path.join(featherence_emu_module_path,'save','mame', 'cfg', '')):
		printpoint = printpoint + '1'
		setconfig(force=True)
	elif not os.path.exists(path): printpoint = printpoint + '8'
	elif not os.path.exists(os.path.join(emulatordata_path,'save','mame', 'diff', '')) or not os.path.exists(os.path.join(emulatordata_path,'save','mame', 'nvram', '')):
		printpoint = printpoint + '2'
		file = "nvram_diff.zip"
		fileID = getfileID(file)
		notification('Downloading NVRAM and DIFF Arcade settings','','',1000)
		DownloadFile("https://www.dropbox.com/s/"+fileID+"/"+file+"?dl=1", file, temp_path, os.path.join(emulator_path,'save','mame', ''), percentinfo=2)
	
	elif not os.path.exists(os.path.join(emulatordata_path,'save','mame', 'diff', '')) or not os.path.exists(os.path.join(emulatordata_path,'save','mame', 'nvram', '')):
		printpoint = printpoint + '3'
	
	if '1' in printpoint or '2' in printpoint or '3' in printpoint or force==True:
		printpoint = printpoint + '7'
		notification('copying Arcade settings','CFG, DIFF, NVRAM','',1000)
		source = os.path.join(emulator_path,'save', 'mame')
		target = os.path.join(emulatordata_path,'save', 'mame')
		copyfiles(source, target)
	
	text = "force" + space2 + str(force)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")

def installemuconsole(force=False):
	printpoint = ""
	if force == True:
		if os.path.exists(emulator_path): notification('Emulator already exists!',emulator_path,"",7000)
	if systemplatformwindows and OS == 'win32': installaddon('emulator.retroarch_win32', update=True)
	elif systemplatformwindows: installaddon('emulator.retroarch_win64', update=True)
	elif systemplatformlinuxraspberrypi: installaddon('emulator.tool.retroarch', update=True)
	elif systemplatformlinux and not systemplatformandroid:
		if OS == 'i386': installaddon('emulator.retroarch_i386', update=True)
		elif OS == 'oe2': installaddon('emulator.tool.retroarch', update=True)
		else: installaddon('emulator.retroarch', update=True)
	else:
		printpoint = printpoint + '6'
		notification("OS and hardware are not supported!","www.featherence.com","",2000)
	
	#installaddon('script.module.featherence.emu', update=True)
	installaddonP('script.module.featherence.emu', update=True)
	if not os.path.exists(emulator_path) and not '6' in printpoint: notification('Featherence Emu Console addon is missing!',"Manual download from addon settings","",4000)

def copyconfig(force=False):
	name = 'copysettings' ; printpoint = "" ; extra = ""
	
	path = config_path2
	if not os.path.exists(path):
		installemuconsole()
	else:
		for file in os.listdir(path):
			#print file
			x = os.path.join(config_path, file)
			if not os.path.exists(x) or force == True:
				copyfiles(os.path.join(path,file), x)
			
		if not os.path.exists(config_path) or force==True:
			printpoint = printpoint + '1'
			notification('Recreating configs','','',1000)
			mkdirs()
			setconfig(force=True)

	text = "extra" + space2 + str(extra)
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

def copyconfig(force=False):
	name = 'copysettings' ; printpoint = "" ; extra = ""
	
	path = config_path2
	if not os.path.exists(path):
		installemuconsole()
	else:
		for file in os.listdir(path):
			#print file
			x = os.path.join(config_path, file)
			if not os.path.exists(x) or force == True:
				copyfiles(os.path.join(path,file), x)
			
		if not os.path.exists(config_path) or force==True:
			printpoint = printpoint + '1'
			notification('Recreating configs','','',1000)
			mkdirs()
			setconfig(force=True)

	text = "extra" + space2 + str(extra)
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
	elif filename == 'TurboGrafx 16': url = '&youtube_id=evg1Q6Ly3AY'
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
				if force == True and z2 != '*': z = z2
				elif z == "" and z2 == '*':
					extra = extra + space + 'pass' ; i2 += 1 ; continue
					
				from_string = x + ' = "'
				to_string = '\n'
				y = regex_from_to(infile_, from_string, to_string, excluding=True)
				if y != z:
					replace_word(to_utf8(config_path) + to_utf8(file),from_string + to_utf8(y),from_string + to_utf8(z) + '"', infile_="", LineR=False , LineClean=False)
					if file == 'retroarch.cfg' and x == 'audio_device' and systemplatformlinux:
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
					
				extra = extra + space + 'y' + space2 + str(y) + space + 'z' + space2 + str(z)
				
				i2 += 1
			
			
			i += 1
	
	dp.update(95,"staticconfig..", "")
	staticconfig(force=True)
	dp.update(100,"Finishing Configuration...", "")

	if systemplatformandroid: pass
	elif systemplatformlinux or systemplatformlinuxraspberrypi:
		x = 'retroarch.cfg'
		copyfiles(os.path.join(config_path,x), '/storage/.config/retroarch/')
		x = '.retroarch-core-options.cfg'
		copyfiles(os.path.join(config_path,x), '/storage/.config/retroarch/')
	
	xbmc.sleep(200) ; dp.close

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
			
			if systemplatformandroid: _arcade_args = 'start -n com.reicast.emulator/.GL2JNIActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if OS == "oe2" or systemplatformlinuxraspberrypi: _arcade_args = 'mame2010'
				elif OS == "i386": _arcade_args = 'fb.alpha'
				else: _arcade_args = 'mame2014'
			elif systemplatformwindows:
				if OS == "win32": _arcade_args = 'mame2010_libretro.dll'
				else: _arcade_args = 'mame2014_libretro.dll'
			dp.update(40,'Generating Launchers file',"Setting _arcade_args..")
			replace_word(emudata_launcher_file,'_arcade_args',_arcade_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _nintendo_args = 'start -n com.explusalpha.NesEmu/com.imagine.BaseActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendo_args = 'fceumm'
				elif OS == "i386": _nintendo_args = 'nestopia'
				else: _nintendo_args = 'nestopia'
			elif systemplatformwindows: _nintendo_args = 'nestopia_libretro.dll'
			dp.update(45,'Generating Launchers file',"Setting _nintendo_args..")
			replace_word(emudata_launcher_file,'_nintendo_args',_nintendo_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _nintendo64_args = 'start -n paulscode.android.mupen64plus.free/paulscode.android.mupen64plusae.MainActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendo64_args = 'mupen64plus'
				elif OS == "i386": _nintendo64_args = 'mupen64plus'
				else: _nintendo64_args = 'mupen64plus'
			elif systemplatformwindows: _nintendo64_args = 'mupen64plus_libretro.dll'
			#start -n com.androidemu.n64/.EmulatorActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"
			dp.update(50,'Generating Launchers file',"Setting _nintendo64_args..")
			replace_word(emudata_launcher_file,'_nintendo64_args',_nintendo64_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _nintendods_args = 'start -n com.reicast.emulator/.GL2JNIActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _nintendods_args = "desmume"
				elif OS == "i386": _nintendods_args = 'desmume'
				else: _nintendods_args = 'desmume'
			elif systemplatformwindows: _nintendods_args = 'desmume_libretro.dll'
			dp.update(55,'Generating Launchers file',"Setting _nintendods_args..")
			replace_word(emudata_launcher_file,'_nintendods_args',_nintendods_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _segagenesis_args = 'start -n com.reicast.emulator/.GL2JNIActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _segagenesis_args = 'genesis_plus.gx'
				elif OS == "i386": _segagenesis_args = 'genesis.plus.gx'
				else: _segagenesis_args = 'genesis.plus.gx'
			elif systemplatformwindows: _segagenesis_args = 'genesis.plus.gx_libretro.dll'
			dp.update(60,'Generating Launchers file',"Setting _segagenesis_args..")
			replace_word(emudata_launcher_file,'_segagenesis_args',_segagenesis_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _ps1_args = 'start -n com.reicast.emulator/.GL2JNIActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _ps1_args = 'pcsx.rearmed'
				elif OS == "i386": _ps1_args = 'mednafen.psx'
				else: _ps1_args = 'mednafen.psx'
			elif systemplatformwindows: _ps1_args = 'mednafen.psx_libretro.dll'
			dp.update(65,'Generating Launchers file',"Setting _ps1_args..")
			replace_word(emudata_launcher_file,'_ps1_args',_ps1_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _supernintendo_args = 'start -n com.explusalpha.Snes9xPlus/com.imagine.BaseActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _supernintendo_args = 'pocketsnes'
				elif OS == "i386": _supernintendo_args = 'snes9x.next'
				else: _supernintendo_args = 'snes9x.next'
			elif systemplatformwindows: _supernintendo_args = 'snes9x.next_libretro.dll'
			dp.update(70,'Generating Launchers file',"Setting _supernintendo_args..")
			replace_word(emudata_launcher_file,'_supernintendo_args',_supernintendo_args, infile_="", LineR=False , LineClean=False)

			if systemplatformandroid: _turbografx16_args = 'start -n com.explusalpha.Snes9xPlus/com.imagine.BaseActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _turbografx16_args = 'mednafen.pce.fast'
				elif OS == "i386": _turbografx16_args = 'mednafen.pce.fast'
				else: _turbografx16_args = 'mednafen.pce.fast'
			elif systemplatformwindows: _turbografx16_args = 'mednafen.pce.fast_libretro.dll'
			dp.update(90,'Generating Launchers file',"Setting _segagenesis_args..")
			replace_word(emudata_launcher_file,'_turbografx16_args',_turbografx16_args, infile_="", LineR=False , LineClean=False)
			
			if systemplatformandroid: _dreamcast_args = 'start -n com.explusalpha.Snes9xPlus/com.imagine.BaseActivity -a android.intent.action.VIEW -eu Uri "file://%rom%"'
			elif systemplatformlinux:
				if systemplatformlinuxraspberrypi or OS == "oe2": _dreamcast_args = ""
				elif OS == "i386": _dreamcast_args = 'reicast'
				else: _dreamcast_args = 'reicast'
			elif systemplatformwindows: _dreamcast_args = 'reicast_libretro.dll'
			dp.update(95,'Generating Launchers file',"Setting _dreamcast_args..")
			replace_word(emudata_launcher_file,'_dreamcast_args',_dreamcast_args, infile_="", LineR=False , LineClean=False)
			dp.update(100,'Generating Launchers file',"Finising..") ; xbmc.sleep(500)
			
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
	
	elif systemplatformandroid: pass
	
	elif systemplatformlinux:
		if systemplatformlinuxraspberrypi or OS == "oe2":
			#if x == 'Featherence_nintendods': returned = "filter"
			if x == 'Featherence_dreamcast': returned = "filter"
		elif OS == "i386":
			if x == 'Featherence_nintendods': returned = "filter"
			if x == 'Featherence_dreamcast': returned = "filter"
			
	
	
	
	text = "x" + space2 + str(x) + newline + \
	'returned' + space2 + str(returned)
	printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	
	return returned
		
def terminal(command):
	'''Execute commands to OS terminal'''
	import subprocess
	name = 'terminal' ; printpoint = "" ; TypeError = "" ; extra = "" ; output = ""

	process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
	output = process.communicate()[0]
				
	text = str(output) + extra
	try: printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
	except Exception, TypeError:
		extra = extra + newline + "TypeError" + space2 + str(TypeError)
		printlog(title=name, printpoint=printpoint, text=text, level=0, option="")
		'''---------------------------'''
	return output

	
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
