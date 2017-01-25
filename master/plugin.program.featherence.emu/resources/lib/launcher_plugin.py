# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


"""
    Plugin for Launching an applications
"""

# -*- coding: UTF-8 -*
import sys, os, fnmatch, time, datetime, math, random, shutil
import re, urllib, urllib2, subprocess_hack, socket, exceptions

from traceback import print_exc
from operator import itemgetter

import xbmc, xbmcgui, xbmcplugin
from xbmcaddon import Addon

import subprocess_hack
from user_agent import getUserAgent
from file_item import Thumbnails
from xml.dom.minidom import parse
#from variables import *

# Dharma compatibility (import md5)
try:
    import hashlib
except:
    import md5

# Addon paths definition
PLUGIN_DATA_PATH = xbmc.translatePath(os.path.join("special://profile/addon_data","plugin.program.featherence.emu"))
BASE_PATH = xbmc.translatePath(os.path.join("special://","profile"))
HOME_PATH = xbmc.translatePath(os.path.join("special://","home"))
BASE_CURRENT_SOURCE_PATH = os.path.join(PLUGIN_DATA_PATH,"launchers.xml")
TEMP_CURRENT_SOURCE_PATH = os.path.join(PLUGIN_DATA_PATH,"launchers.tmp")
MERGED_SOURCE_PATH = os.path.join(PLUGIN_DATA_PATH,"merged-launchers.xml")
DEFAULT_THUMB_PATH = os.path.join(PLUGIN_DATA_PATH,"thumbs")
SHORTCUT_FILE = os.path.join(PLUGIN_DATA_PATH,"shortcut.cut")

# Addon paths creation
if not os.path.exists(DEFAULT_THUMB_PATH): os.makedirs(DEFAULT_THUMB_PATH)
if not os.path.isdir(PLUGIN_DATA_PATH): os.makedirs(PLUGIN_DATA_PATH)



# Addon commands
ADD_COMMAND = "%%ADD%%"
DOWNLOAD_COMMAND = "%%DOWNLOAD%%"
DOWNLOAD_ARTWORKS = "%%DOWNLOAD_ARTWORKS%%"
DOWNLOAD_NVRAM = "%%DOWNLOAD_NVRAM%%"
DOWNLOAD_CFG = "%%DOWNLOAD_CFG%%"
COMMAND_ARGS_SEPARATOR = "^^"
RESET_LANUCHER = "%%RESET_LANUCHER%%"
RESET_DREAMCAST_MEM = "%%RESET_DREAMCAST_MEM%%"
OS_INSTALL = "%%OS_INSTALL%%"
RESET_CONFIG = "%%RESET_CONFIG%%"
COPY_KEYMAPS = "%%COPY_KEYMAPS%%"
COPY_AUTOCONFIG = "%%COPY_AUTOCONFIG%%"
SET_CONFIG = "%%SET_CONFIG%%"
AUDIO_DEVICES = "%%AUDIO_DEVICES%%"
KEYS_HELP = "%%KEYS_HELP%%"
DEL_GAME = "%%DEL_GAME%%"
SEARCH_COMMAND = "%%SEARCH%%"
SEARCH_ITEM_COMMAND = "%%SEARCH_ITEM%%"
SEARCH_DATE_COMMAND = "%%SEARCH_DATE%%"
SEARCH_PLATFORM_COMMAND = "%%SEARCH_PLATFORM%%"
SEARCH_STUDIO_COMMAND = "%%SEARCH_STUDIO%%"
SEARCH_GENRE_COMMAND = "%%SEARCH_GENRE%%"
SEARCH_TRAILER_COMMAND = "%%SEARCH_TRAILER%%"

# Locales parameters
__settings__ = Addon( id="plugin.program.featherence.emu" )
__lang__ = __settings__.getLocalizedString

# Main code
from shared_variables import *
from shared_modules import *
from modules import *

class Main:
    launchers = {}
    categories = {}
    def __init__( self, *args, **kwargs ):
        command_part = ""
        launcher = ""
        category = ""
        
        
        # store an handle pointer
        self._handle = int(sys.argv[ 1 ])
        self._path = sys.argv[ 0 ]

        # get users preference
        self._get_settings()

        # Load launchers
        emudata_launcher_file_size = getFileAttribute(2, emudata_launcher_file, option="1")
        if emudata_launcher_file_size == "": copylaunchers_ = True
        elif int(emudata_launcher_file_size) < 1000: copylaunchers_ = True
        else: copylaunchers_ = False
        copylaunchers(force=copylaunchers_)
        self._load_launchers(self.get_xml_source(BASE_CURRENT_SOURCE_PATH))

        # get emulators preference
        exec "import resources.lib.emulators as _emulators_data"
        self._get_program_arguments = _emulators_data._get_program_arguments
        self._get_program_extensions = _emulators_data._get_program_extensions
        self._get_mame_title = _emulators_data._get_mame_title
        self._test_bios_file = _emulators_data._test_bios_file

        # if a commmand is passed as parameter
        param = sys.argv[ 2 ].replace("%2f","/")

        if ( self._handle > 0 ):
            xbmcplugin.addSortMethod(handle=self._handle, sortMethod=xbmcplugin.SORT_METHOD_LABEL)
            xbmcplugin.addSortMethod(handle=self._handle, sortMethod=xbmcplugin.SORT_METHOD_VIDEO_YEAR)
            xbmcplugin.addSortMethod(handle=self._handle, sortMethod=xbmcplugin.SORT_METHOD_STUDIO)
            xbmcplugin.addSortMethod(handle=self._handle, sortMethod=xbmcplugin.SORT_METHOD_GENRE)
            xbmcplugin.addSortMethod(handle=self._handle, sortMethod=xbmcplugin.SORT_METHOD_UNSORTED)

        # If parameters are passed...
        if param:
            param = param[1:]
            param = param.replace('%2F',"/")
            command = param.split(COMMAND_ARGS_SEPARATOR)
            command_part = command[0].split("/")

            # check the action needed
            if ( len(command_part) == 4 ):
                category = command_part[0]
                launcher = command_part[1]
                rom = command_part[2]
                action = command_part[3]
                filename = self.launchers[launcher]["roms"][rom]["name"]
                filepath = self.launchers[launcher]["roms"][rom]["filename"]
                filerelease = self.launchers[launcher]["roms"][rom]["release"]
                if (action == SEARCH_COMMAND):
                    self._find_roms(False)
                elif (action == SEARCH_TRAILER_COMMAND):
                    searchtrailer(str(filename) + space + str(filerelease))
                    notification(str(filerelease),str(filename),"",4000)
                elif (action == DOWNLOAD_COMMAND):
                    downloads(self._path, category, launcher, rom, filename, filepath)
                elif (action == DEL_GAME):
					del_game(self._path, category, launcher, rom, filename, filepath)
					
            if ( len(command_part) == 3 ):
                category = command_part[0]
                launcher = command_part[1]
                rom = command_part[2]
                #notification('rom (3): ' + str(rom),'','',4000)
                if (rom == SEARCH_COMMAND):
                    self._find_roms(False)
                else:
                    self._run_rom(launcher, rom)
            if ( len(command_part) == 2 ):
                category = command_part[0]
                launcher = command_part[1]

                if (launcher == SEARCH_COMMAND):
                    self._find_roms(False)
					
                # Search commands
                elif (launcher == SEARCH_ITEM_COMMAND):
                    self._find_add_roms(category)
                elif (launcher == SEARCH_DATE_COMMAND):
                    self._find_date_add_roms(category)
                elif (launcher == SEARCH_PLATFORM_COMMAND):
                    self._find_platform_add_roms(category)
                elif (launcher == SEARCH_STUDIO_COMMAND):
                    self._find_studio_add_roms(category)
                elif (launcher == SEARCH_GENRE_COMMAND):
                    self._find_genre_add_roms(category)
                elif (category == KEYS_HELP):
				    keys_help(launcher)
					
                else:
                    if (self.launchers[launcher]["rompath"] == ""):
                        self._run_launcher(launcher)
                    else:
                        self._get_roms(launcher)

            if ( len(command_part) == 1 ):
                category = command_part[0]
                launcher = ""

                if (category == SEARCH_COMMAND):
                    self._find_roms(False)
                elif (category == RESET_LANUCHER):
                    copylaunchers(force=True)
                elif (category == RESET_DREAMCAST_MEM):
                    copydreamcastmem(force=True)
                elif (category == OS_INSTALL):
					installemuconsole(force=True)
                elif (category == RESET_CONFIG):
                    copyconfig(force=True)
                elif (category == COPY_AUTOCONFIG):
					copyautoconfig(force=True)
                elif (category == COPY_KEYMAPS):
                    copykeymaps()
                elif (category == DOWNLOAD_ARTWORKS):
                    downloads2('_Artworks.zip')
                elif (category == DOWNLOAD_NVRAM):
                    downloads2('nvram_diff.zip')
                elif (category == DOWNLOAD_CFG):
                    copyarcade(force=True)
                elif (category == AUDIO_DEVICES):
                    AudioDevices()
                elif (category == SET_CONFIG):
                    setconfig(force=False)
                else:
                    self._get_launchers(category)

        else:
            if (len(self.categories) == 0):
                if (len(self.launchers) == 0):
                    print empty0
                else:
                    categorydata = {}
                    categorydata["name"] = 'Default'
                    self.categories['default'] = categorydata
                    
                    self._get_launchers('default')
            else:
                self._get_categories()
        
        text = "len(command_part)" + space2 + str(len(command_part)) + newline + \
        'param' + space2 + str(param) + newline + \
        'category' + space2 + str(category) + newline + \
        'launcher' + space2 + str(launcher)
        printlog(title='__init__', printpoint="", text=text, level=0, option="")

    def _run_launcher(self, launcherID):
        if (self.launchers.has_key(launcherID)):
            launcher = self.launchers[launcherID]
            apppath = os.path.dirname(launcher["application"])
            if ( os.path.basename(launcher["application"]).lower().replace(".exe" , "") == "xbmc" ) or ("xbmc-fav-" in launcher["application"]) or ("xbmc-sea-" in launcher["application"]):
                xbmc.executebuiltin('XBMC.%s' % launcher["args"])
            else:
                if ( os.path.exists(apppath) ) :
                    arguments = launcher["args"].replace("%apppath%" , apppath).replace("%APPPATH%" , apppath)
                    if xbmc.Player().isPlaying() or 1 + 1 == 2:
						xbmc.Player().stop()
						xbmc.sleep(self.settings[ "start_tempo" ]+100)
						try:
							xbmc.audioSuspend()
						except:
							pass
                    if (launcher["minimize"] == "true"):
                        _toogle_fullscreen()
                    try:
                        xbmc.enableNavSounds(False)                                 
                    except:
                        pass
                    xbmc.sleep(self.settings[ "start_tempo" ])
                    if (os.environ.get( "OS", "xbox" ) == "xbox"):
                        xbmc.executebuiltin('XBMC.Runxbe(' + launcher["application"] + ')')
                    else:
                        if (sys.platform == 'win32'):
                            if ( launcher["application"].split(".")[-1] == "lnk" ):
                                os.system("start \"\" \"%s\"" % (launcher["application"]))
                            else:
                                if ( launcher["application"].split(".")[-1] == "bat" ):
                                    info = subprocess_hack.STARTUPINFO()
                                    info.dwFlags = 1
                                    info.wShowWindow = 0
                                else:
                                    info = None
                                startproc = subprocess_hack.Popen(r'%s %s' % (launcher["application"], arguments), cwd=apppath, startupinfo=info)
                                startproc.wait()
                        elif (sys.platform.startswith('linux')):
                            if ( self.settings[ "lirc_state" ] ):
                                xbmc.executebuiltin('LIRC.stop')
                            os.system("\"%s\" %s " % (launcher["application"], arguments))
                            if ( self.settings[ "lirc_state" ] ):
                                xbmc.executebuiltin('LIRC.start')
                        elif (sys.platform.startswith('darwin')):
                            os.system("\"%s\" %s " % (launcher["application"], arguments))
                        else:
                            notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30609).encode('utf-8'),"",3000)
                    xbmc.sleep(self.settings[ "start_tempo" ])
                    if (launcher["minimize"] == "true"):
                        _toogle_fullscreen()
                    try:
                        xbmc.enableNavSounds(True)                            
                    except:
                        pass
					
                    try:
						xbmc.audioResume()
                    except:
						pass
                else:
                    notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30611).encode('utf-8') % os.path.basename(launcher["application"]),"",3000)

    def _get_settings( self ):
        # get the users preference settings
        self.settings = {}
        self.settings[ "lirc_state" ] = ( __settings__.getSetting( "lirc_state" ) == "true" )
        self.settings[ "start_tempo" ] = int(round(float(__settings__.getSetting( "start_tempo" ))))

    def _run_rom(self, launcherID, romName):
        if (self.launchers.has_key(launcherID)):
            launcher = self.launchers[launcherID]
            if (launcher["roms"].has_key(romName)):
                rom = self.launchers[launcherID]["roms"][romName]
                romfile = os.path.basename(rom["filename"])
                if ( rom["altapp"] != "" ):
                    application = rom["altapp"]
                else:
                    application = launcher["application"]
                apppath = os.path.dirname(application)
                rompath = os.path.dirname(rom["filename"])
                romname = os.path.splitext(romfile)[0]
    
                if ( os.path.exists(apppath) ) :
                    if ( os.path.exists(rom["filename"]) ) :
                        files = []
                        filesnames = []
                        ext3s = ['.cd1', '-cd1', '_cd1', ' cd1']
                        for ext3 in ext3s:
                            cleanromname = re.sub('(\[.*?\]|\{.*?\}|\(.*?\))', '', romname)
                            if ( cleanromname.lower().find(ext3) > -1 ):
                                temprompath = os.path.dirname(rom["filename"])
                                try:
                                    filesnames = os.listdir(temprompath)
                                except:
                                    notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30610).encode('utf-8'),"",3000)
                                namestem = cleanromname[:-len(ext3)]

                                for filesname in filesnames:
                                    altname=re.findall('\{.*?\}',filesname)
                                    searchname = re.sub('(\[.*?\]|\{.*?\}|\(.*?\))', '', filesname)
                                    if searchname[0:len(namestem)] == namestem and searchname[len(namestem):len(namestem)+len(ext3) - 1]  == ext3[:-1]:
                                        for romext in launcher["romext"].split("|"):
                                            if searchname[-len(romext):].lower() == romext.lower() :
                                                Discnum = searchname[(len(namestem)+len(ext3)-1):searchname.rfind(".")]
                                                try:
                                                    int(Discnum)
                                                    if not altname:
                                                        files.append([Discnum, xbmc.getLocalizedString(427)+" "+Discnum, os.path.join(os.path.dirname(rom["filename"]),filesname)])
                                                    else:
                                                        files.append([Discnum, altname[0][1:-1], os.path.join(os.path.dirname(rom["filename"]),filesname)])
                                                except:
                                                    pass
                                if len(files) > 0:
                                    files.sort(key=lambda x: int(x[0]))
                                    discs = []
                                    for file in files:
                                        discs.append(file[1])
                                    dialog = xbmcgui.Dialog()
                                    type3 = dialog.select("%s:" % addonString_servicefeatherence(32423).encode('utf-8'), discs)
                                    if type3 > -1 :
                                        myresult = files[type3]
                                        rom["filename"] = myresult[2]
                                        romfile = os.path.basename(rom["filename"])
                                        rompath = os.path.dirname(rom["filename"])
                                        romname = os.path.splitext(romfile)[0]
                                    else:
                                        return ""

                        if ( rom["altarg"] != "" ):
                            arguments = rom["altarg"]
                        else:
                            arguments = launcher["args"]
                        arguments = arguments.replace("%rom%" , rom["filename"]).replace("%ROM%" , rom["filename"])
                        arguments = arguments.replace("%romfile%" , romfile).replace("%ROMFILE%" , romfile)
                        arguments = arguments.replace("%romname%" , romname).replace("%ROMNAME%" , romname)
                        arguments = arguments.replace("%rombasename%" , base_filename(romname)).replace("%ROMBASENAME%" , base_filename(romname))
                        arguments = arguments.replace("%apppath%" , apppath).replace("%APPPATH%" , apppath)
                        arguments = arguments.replace("%rompath%" , rompath).replace("%ROMPATH%" , rompath)
                        arguments = arguments.replace("%romtitle%" , rom["name"]).replace("%ROMTITLE%" , rom["name"])
                        arguments = arguments.replace("%romspath%" , launcher["rompath"]).replace("%ROMSPATH%" , launcher["rompath"])

                        if ( os.path.basename(application).lower().replace(".exe" , "") == "xbmc" ):
                            xbmc.executebuiltin('XBMC.' + arguments)
                        else:
                            if ( xbmc.Player().isPlaying() ) or 1 + 1 == 2:
								xbmc.Player().stop()
								xbmc.sleep(self.settings[ "start_tempo" ]+100)
								try:
									xbmc.audioSuspend()
								except:
								    pass
                            if (launcher["minimize"] == "true"):
                                _toogle_fullscreen()
                            try:
                                xbmc.enableNavSounds(False)                                 
                            except:
                                pass
                            xbmc.sleep(self.settings[ "start_tempo" ])
                            if (os.environ.get( "OS", "xbox" ) == "xbox"):
                                f=open(SHORTCUT_FILE, "wb")
                                f.write("<shortcut>\n")
                                f.write("    <path>" + application + "</path>\n")
                                f.write("    <custom>\n")
                                f.write("       <game>" + rom["filename"] + "</game>\n")
                                f.write("    </custom>\n")
                                f.write("</shortcut>\n")
                                f.close()
                                xbmc.executebuiltin('XBMC.Runxbe(' + SHORTCUT_FILE + ')')
                            else:
                                if (sys.platform == 'win32'):
                                    if ( launcher["lnk"] == "true" ) and ( launcher["romext"] == "lnk" ):
                                        os.system("start \"\" \"%s\"" % (arguments))
                                    else:
                                        if ( application.split(".")[-1] == "bat" ):
                                            info = subprocess_hack.STARTUPINFO()
                                            info.dwFlags = 1
                                            info.wShowWindow = 0
                                        else:
                                            info = None
                                        startproc = subprocess_hack.Popen(r'%s %s' % (application, arguments), cwd=apppath, startupinfo=info)
                                        startproc.wait()
                                elif (sys.platform.startswith('linux')):
                                    if ( self.settings[ "lirc_state" ] ):
                                        xbmc.executebuiltin('LIRC.stop')
                                    os.system("\"%s\" %s " % (application, arguments))
                                    if ( self.settings[ "lirc_state" ] ):
                                        xbmc.executebuiltin('LIRC.start')
                                elif (sys.platform.startswith('darwin')):
                                    os.system("\"%s\" %s " % (application, arguments))
                                else:
                                    notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30609).encode('utf-8'),"",3000)
                            xbmc.sleep(self.settings[ "start_tempo" ])
                            try:
                                xbmc.enableNavSounds(True)                            
                            except:
                                pass
                            if (launcher["minimize"] == "true"):
                                _toogle_fullscreen()
                            try:
								xbmc.audioResume()
                            except:
								pass
                    else:
                        notification(addonString(30611).encode('utf-8') % os.path.basename(rom["filename"]),'You should download the game first!','',3000)
                else:
                    notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30611).encode('utf-8') % os.path.basename(launcher["application"]),"",3000)

    def get_xml_source( self, xmlpath ):
        try:
            usock = open( xmlpath, 'r' )
            # read source
            xmlSource = usock.read()
            # close socket
            usock.close()
            ok = True
        except:
            ok = False
        if ( ok ):
            # clean, save and return the xml string
            xmlSource = xmlSource.replace("&amp;", "&")
            xmlSource = xmlSource.replace("&", "&amp;")
            f = open(BASE_CURRENT_SOURCE_PATH, 'w')
            f.write(xmlSource)
            f.close()
            return xmlSource.replace("\n","").replace("\r","")
        else:
            return ""

    def _load_launchers(self, xmlSource):
        # clean, save and return the xml string
        xmlSource = xmlSource.replace("&amp;", "&").replace('\r','').replace('\n','').replace('\t','')
        # Get categories list from XML source
        xml_categories = re.findall( "<categories>(.*?)</categories>", xmlSource )
        # If categories exist ()...
        if len(xml_categories) > 0 :
            categories = re.findall( "<category>(.*?)</category>", xml_categories[0] )
            for category in categories:
                categorydata = {}
                category_index = ["id","name","thumb","fanart","genre","plot"]
                values = [re.findall("<id>(.*?)</id>",category), re.findall("<name>(.*?)</name>",category), re.findall("<thumb>(.*?)</thumb>",category), re.findall("<fanart>(.*?)</fanart>",category), re.findall("<genre>(.*?)</genre>",category), re.findall("<description>(.*?)</description>",category)]
                for index, n in enumerate(category_index):
                    try:
                        categorydata[n] = values[index][0]
                    except:
                        categorydata[n] = ""
                self.categories[categorydata["id"]] = categorydata
        # Else create the default category
        else:
            self.categories["default"] = {"id":"default", "name":"Default", "thumb":"", "fanart":"", "genre":"", "plot":""}
        # Get launchers list from XML source
        xml_launchers = re.findall( "<launchers>(.*?)</launchers>", xmlSource )
        # If launchers exist ()...
        if len(xml_launchers) > 0 :
            launchers = re.findall( "<launcher>(.*?)</launcher>", xml_launchers[0] )
            for launcher in launchers:
                launcherdata = {}
                launcher_index = ["id","name","category","application","args","rompath","thumbpath","fanartpath","trailerpath","custompath","romext","gamesys","thumb","fanart","genre","release","studio","plot","minimize","lnk","roms"]        
                values = [re.findall("<id>(.*?)</id>",launcher), re.findall("<name>(.*?)</name>",launcher), re.findall("<category>(.*?)</category>",launcher), re.findall("<application>(.*?)</application>",launcher), re.findall("<args>(.*?)</args>",launcher), re.findall("<rompath>(.*?)</rompath>",launcher), re.findall("<thumbpath>(.*?)</thumbpath>",launcher), re.findall("<fanartpath>(.*?)</fanartpath>",launcher), re.findall("<trailerpath>(.*?)</trailerpath>",launcher), re.findall("<custompath>(.*?)</custompath>",launcher), re.findall("<romext>(.*?)</romext>",launcher), re.findall("<platform>(.*?)</platform>",launcher), re.findall("<thumb>(.*?)</thumb>",launcher), re.findall("<fanart>(.*?)</fanart>",launcher), re.findall("<genre>(.*?)</genre>",launcher), re.findall("<release>(.*?)</release>",launcher), re.findall("<publisher>(.*?)</publisher>",launcher), re.findall("<launcherplot>(.*?)</launcherplot>",launcher), re.findall("<minimize>(.*?)</minimize>",launcher), re.findall("<lnk>(.*?)</lnk>",launcher), re.findall("<roms>(.*?)</roms>",launcher)]
                for index, n in enumerate(launcher_index):
                    try:
                        launcherdata[n] = values[index][0]
                    except:
                        launcherdata[n] = ""
                # Fix category to unassigned launcher
                if (launcherdata["category"] == ""):
                    launcherdata["category"] = "default"
                # Get roms list from XML source
                roms = re.findall( "<rom>(.*?)</rom>", launcherdata["roms"] )
                roms_list = {}
                # If roms exist...
                if len(roms) > 0 :
                    for rom in roms:
                        romdata = {}
                        rom_index = ["id","name","filename","thumb","fanart","trailer","custom","genre","release","studio","plot","altapp","altarg"]        
                        r_values = [re.findall("<id>(.*?)</id>",rom), re.findall("<name>(.*?)</name>",rom), re.findall("<filename>(.*?)</filename>",rom), re.findall("<thumb>(.*?)</thumb>",rom), re.findall("<fanart>(.*?)</fanart>",rom), re.findall("<trailer>(.*?)</trailer>",rom), re.findall("<custom>(.*?)</custom>",rom), re.findall("<genre>(.*?)</genre>",rom), re.findall("<release>(.*?)</release>",rom), re.findall("<publisher>(.*?)</publisher>",rom), re.findall("<gameplot>(.*?)</gameplot>",rom), re.findall("<altapp>(.*?)</altapp>",rom), re.findall("<altarg>(.*?)</altarg>",rom)]
                        for r_index, r_n in enumerate(rom_index):
                            try:
                                romdata[r_n] = r_values[r_index][0]
                            except :
                                romdata[r_n] = ""
                        romdata["gamesys"] = launcherdata["gamesys"]
                        roms_list[romdata["id"]] = romdata
                launcherdata["roms"] = roms_list
                self.launchers[launcherdata["id"]] = launcherdata

    def _get_categories( self ):
        from modules import filterbyos
        for key in sorted(self.categories, key= lambda x : self.categories[x]["name"]):
            returned = filterbyos(self.categories[key]['id'])
            if ( self.categories[key]['id'] != "default" ) and returned == "":
                self._add_category(self.categories[key]["name"], self.categories[key]["thumb"], self.categories[key]["fanart"], self.categories[key]["genre"], self.categories[key]["plot"], len(self.categories), key)
        xbmcplugin.endOfDirectory( handle=int( self._handle ), succeeded=True, cacheToDisc=False )

    def _get_launchers( self, categoryID ):
        for key in sorted(self.launchers, key= lambda x : self.launchers[x]["application"]):
            if ( self.launchers[key]["category"] == categoryID ) :
                if self.launchers[key]["id"] == 'Featherence_arcadeADULT' and show_adult != 'true': pass
                else:
			        self._add_launcher(self.launchers[key]["name"], self.launchers[key]["category"], self.launchers[key]["application"], self.launchers[key]["rompath"], self.launchers[key]["thumbpath"], self.launchers[key]["fanartpath"], self.launchers[key]["trailerpath"], self.launchers[key]["custompath"], self.launchers[key]["romext"], self.launchers[key]["gamesys"], self.launchers[key]["thumb"], self.launchers[key]["fanart"], self.launchers[key]["genre"], self.launchers[key]["release"], self.launchers[key]["studio"], self.launchers[key]["plot"], self.launchers[key]["lnk"], self.launchers[key]["minimize"], self.launchers[key]["roms"], len(self.launchers), key)
        xbmcplugin.endOfDirectory( handle=int( self._handle ), succeeded=True, cacheToDisc=False )
        
        text = "categoryID" + space2 + str(categoryID) + newline + \
        'self.launchers[key]' + space2 + str(self.launchers[key]) + newline + \
        'self.launchers[key]["id"]' + space2 + str(self.launchers[key]["id"])
        printlog(title='_get_launchers', printpoint="", text=text, level=0, option="")

    def _get_roms( self, launcherID ):
        if (self.launchers.has_key(launcherID)):
            selectedLauncher = self.launchers[launcherID]
            roms = selectedLauncher["roms"]
            
			
            if launcherID == 'Featherence_arcadeADULT' and show_adult != 'true': pass
            else:
				if ( len(roms) != 0 ):
					for key in sorted(roms, key= lambda x : roms[x]["filename"]):
						if (roms[key]["fanart"] ==""):
							defined_fanart = selectedLauncher["fanart"]
						else:
							defined_fanart = roms[key]["fanart"]
						rom_name = roms[key]["name"]
						if not os.path.exists(roms[key]["filename"]): rom_name = '[COLOR=red]' + rom_name + '[/COLOR]'
						if os.path.exists(roms[key]["filename"]) or filter_games != 'true': self._add_rom(launcherID, rom_name, roms[key]["filename"], roms[key]["gamesys"], roms[key]["thumb"], defined_fanart, roms[key]["trailer"], roms[key]["custom"], roms[key]["genre"], roms[key]["release"], roms[key]["studio"], roms[key]["plot"], roms[key]["altapp"], roms[key]["altarg"], len(roms), key, False, "")
					xbmcplugin.endOfDirectory( handle=int( self._handle ), succeeded=True, cacheToDisc=False )
				else:
					notification(addonName + " - " + addonString(30349).encode('utf-8'),"","",3000)

    def _add_category(self, name, thumb, fanart, genre, plot, total, key):
        commands = []
        commands.append((localize(137), "XBMC.RunPlugin(%s?%s)" % (self._path, SEARCH_COMMAND) , ))
        commands.append((addonString(30100).encode('utf-8') % (name), "XBMC.RunPlugin(%s?%s/%s)" % (self._path, KEYS_HELP, name) , ))
        commands.append((localize(10140), 'Addon.OpenSettings('+addonID+')'))
		
        folder = True
        icon = "DefaultFolder.png"
        if (thumb):
            listitem = xbmcgui.ListItem( name, iconImage=icon, thumbnailImage=thumb )
        else:
            listitem = xbmcgui.ListItem( name, iconImage=icon )

        listitem.setProperty("fanart_image", fanart)
        listitem.setInfo( "video", { "Title": name, "Genre" : genre, "Plot" : plot, "overlay": 6 } )
        listitem.addContextMenuItems( commands, replaceItems=True)
        xbmcplugin.addDirectoryItem( handle=int( self._handle ), url="%s?%s"  % (self._path, key), listitem=listitem, isFolder=True)

    def _add_launcher(self, name, category, cmd, path, thumbpath, fanartpath, trailerpath, custompath, ext, gamesys, thumb, fanart, genre, release, studio, plot, lnk, minimize, roms, total, key) :
        if (int(xbmc.getInfoLabel("System.BuildVersion")[0:2]) < 12 ):
            # Dharma / Eden compatible
            display_date_format = "Date"
        else:
            # Frodo & + compatible
            display_date_format = "Year"
        commands = []
        commands.append((localize(137), "XBMC.RunPlugin(%s?%s/%s)" % (self._path, category, SEARCH_COMMAND) , ))
        commands.append((localize(10140), 'Addon.OpenSettings('+addonID+')'))

        if (path == ""):
            folder = False
            icon = "DefaultProgram.png"
        else:
            folder = True
            icon = "DefaultFolder.png"

        if (thumb):
            listitem = xbmcgui.ListItem( name, iconImage=icon, thumbnailImage=thumb )
        else:
            listitem = xbmcgui.ListItem( name, iconImage=icon )

        filename = os.path.splitext(cmd)

        listitem.setProperty("fanart_image", fanart)
        listitem.setInfo( "video", { "Title": name, "Label": os.path.basename(cmd), "Plot" : plot , "Studio" : studio , "Genre" : genre , "Premiered" : release  , display_date_format : release  , "Writer" : gamesys , "Trailer" : os.path.join(trailerpath), "Director" : os.path.join(custompath), "overlay": 6 } )
        listitem.addContextMenuItems( commands, replaceItems=True)
        xbmcplugin.addDirectoryItem( handle=int( self._handle ), url="%s?%s/%s"  % (self._path, category, key), listitem=listitem, isFolder=folder)

    def _add_rom( self, launcherID, name, cmd , romgamesys, thumb, romfanart, romtrailer, romcustom, romgenre, romrelease, romstudio, romplot, altapp, altarg, total, key, search, search_url):
        filepath = self.launchers[launcherID]["roms"][key]["filename"]

        if (int(xbmc.getInfoLabel("System.BuildVersion")[0:2]) < 12 ):
            # Dharma / Eden compatible
            display_date_format = "Date"
        else:
            # Frodo & + compatible
            display_date_format = "Year"
        filename = os.path.splitext(cmd)
        icon = "DefaultProgram.png"
        if (thumb):
            listitem = xbmcgui.ListItem( name, iconImage=icon, thumbnailImage=thumb)
        else:
            listitem = xbmcgui.ListItem( name, iconImage=icon)
       
        listitem.setProperty("fanart_image", romfanart)
        listitem.setInfo( "video", { "Title": name, "Label": os.path.basename(cmd), "Plot" : romplot, "Studio" : romstudio, "Genre" : romgenre, "Premiered" : romrelease  , display_date_format : romrelease, "Writer" : romgamesys, "Trailer" : os.path.join(romtrailer), "Director" : os.path.join(romcustom), "overlay": 6 } )

        commands = []
        #commands.append((localize(137), "XBMC.RunPlugin(%s?%s/%s/%s)" % (self._path, self.launchers[launcherID]["category"], launcherID, SEARCH_COMMAND) , ))

        commands.append((localize(137) + space + localize(20410), "XBMC.RunPlugin(%s?%s/%s/%s/%s)" % (self._path, self.launchers[launcherID]["category"], launcherID, key, SEARCH_TRAILER_COMMAND) , ))
        #commands.append((localize(137) + space + localize(20410), "XBMC.RunPlugin(plugin://plugin.video.youtube/search/?q=%s)" % (name), ))
        commands.append((localize(33003), "XBMC.RunPlugin(%s?%s/%s/%s/%s)" % (self._path, self.launchers[launcherID]["category"], launcherID, key, DOWNLOAD_COMMAND) , )) #DOWNLOAD
        if os.path.exists(filepath) and delete_games == 'true': commands.append((addonString(30101).encode('utf-8'), "XBMC.RunPlugin(%s?%s/%s/%s/%s)" % (self._path, self.launchers[launcherID]["category"], launcherID, key, DEL_GAME) , )) #DEL_GAME
        commands.append((localize(10140), 'Addon.OpenSettings('+addonID+')'))
		
        listitem.addContextMenuItems( commands, replaceItems=True)
        xbmcplugin.addDirectoryItem( handle=int( self._handle ), url="%s?%s/%s/%s"  % (self._path, self.launchers[launcherID]["category"], launcherID, key), listitem=listitem, isFolder=False)

    def _find_roms( self, is_launcher ):
        dialog = xbmcgui.Dialog()
        type = dialog.select(addonString(30400).encode('utf-8'), [addonString(30401).encode('utf-8'),addonString(30402).encode('utf-8'),addonString(30403).encode('utf-8'),addonString(30404).encode('utf-8'),addonString(30405).encode('utf-8')])
        type_nb = 0

        #Search by Title
        if (type == type_nb ):
            keyboard = xbmc.Keyboard("", addonString(30036).encode('utf-8'))
            keyboard.doModal()
            if (keyboard.isConfirmed()):
                search = keyboard.getText()
                if (is_launcher):
                    return "%s?%s/%s" % (self._path, search, SEARCH_ITEM_COMMAND), search
                else:
                    xbmc.executebuiltin("ReplaceWindow(Programs,%s?%s/%s)" % (self._path, search, SEARCH_ITEM_COMMAND))

        #Search by Release Date
        type_nb = type_nb+1
        if (type == type_nb ):
            search = []
            search = _search_category(self,"release")
            dialog = xbmcgui.Dialog()
            selected = dialog.select(addonString(30406).encode('utf-8'), search)
            if (not selected == -1 ):
                if (is_launcher):
                    return "%s?%s/%s" % (self._path, search[selected], SEARCH_DATE_COMMAND), search[selected]
                else:
                    xbmc.executebuiltin("ReplaceWindow(Programs,%s?%s/%s)" % (self._path, search[selected], SEARCH_DATE_COMMAND))

        #Search by System Platform
        type_nb = type_nb+1
        if (type == type_nb ):
            search = []
            search = _search_category(self,"gamesys")
            dialog = xbmcgui.Dialog()
            selected = dialog.select(addonString(30407).encode('utf-8'), search)
            if (not selected == -1 ):
                if (is_launcher):
                    return "%s?%s/%s" % (self._path, search[selected], SEARCH_PLATFORM_COMMAND), search[selected]
                else:
                    xbmc.executebuiltin("ReplaceWindow(Programs,%s?%s/%s)" % (self._path, search[selected], SEARCH_PLATFORM_COMMAND))

        #Search by Studio
        type_nb = type_nb+1
        if (type == type_nb ):
            search = []
            search = _search_category(self,"studio")
            dialog = xbmcgui.Dialog()
            selected = dialog.select(addonString(30408).encode('utf-8'), search)
            if (not selected == -1 ):
                if (is_launcher):
                    return "%s?%s/%s" % (self._path, search[selected], SEARCH_STUDIO_COMMAND), search[selected]
                else:
                    xbmc.executebuiltin("ReplaceWindow(Programs,%s?%s/%s)" % (self._path, search[selected], SEARCH_STUDIO_COMMAND))

        #Search by Genre
        type_nb = type_nb+1
        if (type == type_nb ):
            search = []
            search = _search_category(self,"genre")
            dialog = xbmcgui.Dialog()
            selected = dialog.select(addonString(30409).encode('utf-8'), search)
            if (not selected == -1 ):
                if (is_launcher):
                    return "%s?%s/%s" % (self._path, search[selected], SEARCH_GENRE_COMMAND), search[selected]
                else:
                    xbmc.executebuiltin("ReplaceWindow(Programs,%s?%s/%s)" % (self._path, search[selected], SEARCH_GENRE_COMMAND))

    def _find_add_roms( self, search ):
        _find_category_roms( self, search, "name" )

    def _find_date_add_roms( self, search ):
        _find_category_roms( self, search, "release" )

    def _find_platform_add_roms( self, search ):
        _find_category_roms( self, search, "gamesys" )

    def _find_studio_add_roms( self, search ):
        _find_category_roms( self, search, "studio" )

    def _find_genre_add_roms( self, search ):
        _find_category_roms( self, search, "genre" )

class MainGui( xbmcgui.WindowXMLDialog ):
    def __init__( self, *args, **kwargs ):
        xbmcgui.WindowXMLDialog.__init__( self, *args, **kwargs )
        xbmc.executebuiltin( "Skin.Reset(AnimeWindowXMLDialogClose)" )
        xbmc.executebuiltin( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
        self.listing = kwargs.get( "listing" )

    def onInit(self):
        try :
            self.img_list = self.getControl(6)
            self.img_list.controlLeft(self.img_list)
            self.img_list.controlRight(self.img_list)
            self.getControl(3).setVisible(False)
        except :
            print_exc()
            self.img_list = self.getControl(3)

        self.getControl(5).setVisible(False)

        for index, item in enumerate(self.listing):
            listitem = xbmcgui.ListItem( item[2] )
            listitem.setIconImage( item[1] )
            listitem.setLabel2( item[0] )
            
            self.img_list.addItem( listitem )
        self.setFocus(self.img_list)

    def onAction(self, action):
        #Close the script
        if action == 10 :
            self.close()

    def onClick(self, controlID):
        #action sur la liste
        if controlID == 6 or controlID == 3:
            #Renvoie l'item selectionne
            num = self.img_list.getSelectedPosition()
            self.selected_url = self.img_list.getSelectedItem().getLabel2()
            self.close()

    def onFocus(self, controlID):
        pass

def MyDialog(img_list):
    w = MainGui( "DialogSelect.xml", BASE_PATH, listing=img_list )
    w.doModal()
    try:
        return w.selected_url
    except:
        print_exc()
        return False
    del w

def get_encoding():
    try:
        return sys.getfilesystemencoding()
    except (UnicodeEncodeError, UnicodeDecodeError):
        return "utf-8"

def _update_cache(file_path):
    cached_thumb = Thumbnails().get_cached_covers_thumb( file_path ).replace("tbn" , os.path.splitext(file_path)[-1][1:4])
    try:
        shutil.copy2( file_path.decode(get_encoding(),'ignore'), cached_thumb.decode(get_encoding(),'ignore') )
    except OSError:
        notification(addonName + " - " + addonString(30612).encode('utf-8'),addonString(30608).encode('utf-8'),"",3000)
    xbmc.executebuiltin("XBMC.ReloadSkin()")

def title_format(self,title):
    if ( self.settings[ "clean_title" ] ):
       title = re.sub('\[.*?\]', '', title)
       title = re.sub('\(.*?\)', '', title)
       title = re.sub('\{.*?\}', '', title)
    new_title = title.rstrip()
    if ( self.settings[ "title_formating" ] ):
        if (title.startswith("The ")): new_title = title.replace("The ","",1)+", The"
        if (title.startswith("A ")): new_title = title.replace("A ","",1)+", A"
        if (title.startswith("An ")): new_title = title.replace("An ","",1)+", An"
    else:
        if (title.endswith(", The")): new_title = "The "+"".join(title.rsplit(", The",1))
        if (title.endswith(", A")): new_title = "A "+"".join(title.rsplit(", A",1))
        if (title.endswith(", An")): new_title = "An "+"".join(title.rsplit(", An",1))
    return new_title                            

def base_filename(filename):
    filename = re.sub('(\[.*?\]|\(.*?\)|\{.*?\})', '', filename)
    filename = re.sub('(\.|-| |_)cd\d+$', '', filename)
    return filename.rstrip()

def _toogle_fullscreen():
    try:
        # Dharma / Eden compatible
        xbmc.executehttpapi("Action(199)")
    except:
        # Frodo & + compatible
        xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.ExecuteAction","params":{"action":"togglefullscreen"},"id":"1"}')

def _get_SID():
    t1 = time.time()
    t2 = t1 + random.getrandbits(32)
    try: 
        # Eden & + compatible
        base = hashlib.md5( str(t1 +t2) )
    except:
        # Dharma compatible
        base = md5.new( str(t1 +t2) )
    sid = base.hexdigest()
    return sid

def _get_game_system_list():
    platforms = []
    try:
        rootDir = __settings__.getAddonInfo('path')
        if rootDir[-1] == ';':rootDir = rootDir[0:-1]
        resDir = os.path.join(rootDir, 'resources')
        scrapDir = os.path.join(resDir, 'scrapers')
        csvfile = open( os.path.join(scrapDir, 'gamesys'), "rb")
        for line in csvfile.readlines():
            result = line.replace('\n', '').replace('"', '').split(',')
            platforms.append(result[0])
        platforms.sort()
        csvfile.close()
        return platforms
    except:
        return platforms

def _search_category(self,category):
    search = []
    if (len(self.launchers) > 0):
        for key in sorted(self.launchers.iterkeys()):
            if (len(self.launchers[key]["roms"]) > 0) :
                for keyr in sorted(self.launchers[key]["roms"].iterkeys()):
                    if ( self.launchers[key]["roms"][keyr][category] == "" ):
                        search.append("[ %s ]" % addonString(30410).encode('utf-8'))
                    else:
                        search.append(self.launchers[key]["roms"][keyr][category])
    search = list(set(search))
    search.sort()
    return search

def _find_category_roms( self, search, category ):
    #sorted by name
    if category == 'name' : 
        s_cmd = SEARCH_ITEM_COMMAND
    if category == 'release' :
        s_cmd = SEARCH_DATE_COMMAND
    if category == 'gamesys' :
        s_cmd = SEARCH_PLATFORM_COMMAND
    if category == 'studio' :
        s_cmd = SEARCH_STUDIO_COMMAND
    if category == 'genre' :
        s_cmd = SEARCH_GENRE_COMMAND
    s_url = 'plugin://plugin.program.featherence.emu/?'+search+'/'+s_cmd
    if (len(self.launchers) > 0):
        rl = {}
        for launcherID in sorted(self.launchers.iterkeys()):
            selectedLauncher = self.launchers[launcherID]
            roms = selectedLauncher["roms"]
            notset = ("[ %s ]" % addonString(30410).encode('utf-8'))
            text = search.lower()
            empty = notset.lower()
            if (len(roms) > 0) :
                #go through rom list and search for user input
                for keyr in sorted(roms.iterkeys()):
                    rom = roms[keyr][category].lower()
                    if (rom == "") and (text == empty):
                        rl[keyr] = roms[keyr]
                        rl[keyr]["launcherID"] = launcherID
                    if category == 'name':
                        if (not rom.find(text) == -1):
                            rl[keyr] = roms[keyr]
                            rl[keyr]["launcherID"] = launcherID
                    else:
                        if (rom == text):
                            rl[keyr] = roms[keyr]
                            rl[keyr]["launcherID"] = launcherID
    #print the list sorted
    for key in sorted(rl.iterkeys()):
        self._add_rom(rl[key]["launcherID"], rl[key]["name"], rl[key]["filename"], rl[key]["gamesys"], rl[key]["thumb"], rl[key]["fanart"], rl[key]["trailer"], rl[key]["custom"], rl[key]["genre"], rl[key]["release"], rl[key]["studio"], rl[key]["plot"], rl[key]["altapp"], rl[key]["altarg"], len(rl), key, True, s_url)
    xbmcplugin.endOfDirectory( handle=int( self._handle ), succeeded=True, cacheToDisc=False )
