'''
    Simple XBMC Download Script
    Copyright (C) 2013 Sean Poyser (seanpoyser@gmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import urllib
import urllib2
import xbmc
import xbmcgui
import xbmcplugin
import xbmcvfs
import os
import inspect

from variables import *
from shared_modules import *

def getResponse(url, size, referer, agent, cookie, silent):
    resp = "" ; req = "" ; returned = "" ; printpoint = "" ; req_str = "" ; response_data = "" ; TypeError = ""
    url = url.replace(" ","%20")
    try:
        req = urllib2.Request(url) ; printpoint = printpoint + '1' ; req_str = urllib2.urlopen(req).geturl()
        if len(referer) > 0:
            req.add_header('Referer', referer) ; printpoint = printpoint + '2'

        if len(agent) > 0:
            req.add_header('User-Agent', agent) ; printpoint = printpoint + '3'

        if len(cookie) > 0:
            req.add_header('Cookie', cookie) ; printpoint = printpoint + '4'

        if size > 0:
            size = int(size)
            req.add_header('Range',   'bytes=%d-' % size) ; printpoint = printpoint + '5'

        resp = urllib2.urlopen(req, timeout=20)
        #response_data = resp.read() #TypeError: out of memory
        returned = resp ; printpoint = printpoint + '7'
    except Exception, TypeError:
        returned = None
    
    text = 'url' + space2 + str(url) + newline + \
    'req' + space2 + str(req) + newline + \
    'req_str' + space2 + str(req_str) + newline + \
    'resp' + space2 + str(resp) + newline + \
    'size' + space2 + str(size) + newline + \
    'referer' + space2 + str(referer) + newline + \
    'response_data' + space2 + str(response_data) + newline + \
    'TypeError' + space2 + str(TypeError) + newline + \
    'agent' + space2 + str(agent)
    printlog(title="getResponse-commondownloader", printpoint=printpoint, text=text, level=1, option="")
	
    return returned, str(TypeError)
	
def download(url, dest, title=None, referer=None, agent=None, cookie=None, silent=False):
    #agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    #agent={"Chrome/80.0.3987.149"}
    if not title:
        title  = 'Kodi Download'

    if not referer:
        referer  = ''

    if not agent:
        agent  = ''

    if not cookie:
        cookie  = ''

    #quote parameters
    url     = urllib.quote_plus(url)
    dest    = urllib.quote_plus(dest)
    title   = urllib.quote_plus(title)
    referer = urllib.quote_plus(referer)
    agent   = urllib.quote_plus(agent)
    cookie  = urllib.quote_plus(cookie)

    script = inspect.getfile(inspect.currentframe())
    cmd    = 'RunScript(%s, %s, %s, %s, %s, %s, %s, %s)' % (script, url, dest, title, referer, agent, cookie, silent)

    xbmc.executebuiltin(cmd)


def doDownload(url, dest, title, referer, agent, cookie, silent=False, percentinfo=20):
    printpoint = "" ; extra = "" ; TypeError = "" ; returned = "" ; respheaders = "" ; resumable = ""
    exe = printlog(title="exe", printpoint="", text="", level=0, option="")
    try: test = percentinfo + 1
    except: percentinfo = 20
    xbmc.executebuiltin('ActivateWindow(busydialog)')
    xbmc.executebuiltin('AlarmClock(busydialog,Dialog.Close(busydialog),00:05,silent)')
    url     = urllib.unquote_plus(url)
    dest    = urllib.unquote_plus(dest)
    title   = urllib.unquote_plus(title)
    referer = urllib.unquote_plus(referer)
    agent   = urllib.unquote_plus(agent)
    cookie  = urllib.unquote_plus(cookie)

    file = dest.rsplit(os.sep, 1)[-1]

    resp, TypeError = getResponse(url, 0, referer, agent, cookie, silent)
    
    xbmc.executebuiltin('Dialog.Close(busydialog)')
    ContainerFolderPath = xbmc.getInfoLabel('Container.FolderPath')
    
    if not resp:
        printpoint = printpoint + '1'
        if silent != True or exe != "":
            if TypeError == "":
                if 'plugin.program.featherence.emu' in ContainerFolderPath:
                    dialogok(title, 'Game is unavailable at the moment', '[CR]www.youtube.com/@youplay.nostalgia') #Game is unavailable at the moment
                else:
                    dialogok(title, dest, localize(13036, s=[localize(33003)]), localize(15301)) #Failed for %s, Couldn't connect to network server
            else:
                if 'plugin.program.featherence.emu' in ContainerFolderPath:
                    #dialogok(title, dest, localize(13036, s=[localize(32161)]), localize(32158) + '1') #Game is unavailable at the moment
                    dialogok(title, str(TypeError), '', 'www.youtube.com/@youplay.nostalgia') #Game is unavailable at the moment
                else:
                    dialogok(title, str(TypeError), localize(13036, s=[localize(33003)]), localize(15301)) #Failed for %s, Couldn't connect to network server
        returned = "skip"

    try:
        respheaders = str(resp.headers) ; content = int(resp.headers.get("Content-Length", 0)) ; printpoint = printpoint + '2A'
    except Exception, TypeError:
        content = 0
        TypeError = str(TypeError) + " " + str(TypeError)

    if 1 + 1 == 2:
        try:    resumable = 'bytes' in resp.headers['Accept-Ranges'].lower()
        except Exception, TypeError: resumable = False ; printpoint = printpoint + '4' ; TypeError = str(TypeError) + " " + str(TypeError)

        if resumable:
            pass ; printpoint = printpoint + '5'

    text = 'url' + space2 + str(url) + newline + \
    'dest' + space2 + str(dest) + newline + \
    'title' + space2 + str(title) + newline + \
    'content' + space2 + str(content) + newline + \
    'TypeError' + space2 + str(TypeError) + newline + \
    'resumable' + space2 + str(resumable) + newline + \
    'ContainerFolderPath' + space2 + str(ContainerFolderPath) + newline + \
    'resp' + space2 + str(resp) + newline + \
    'resp.headers' + space2 + str(respheaders)
    printlog(title="doDownload", printpoint=printpoint, text=text, level=0, option="")
	
    
    if content < 1 and returned != "skip":
        if silent != True or exe != "":
            if 'plugin.program.featherence.emu' in ContainerFolderPath:
                if url == "" or url == "#": dialogok(title, addonString_servicefeatherence(32167).encode('utf-8'), addonString_servicefeatherence(32157).encode('utf-8'),"") #I haven't uploaded it yet :(
                else:
                    dialogok(title, 'Game archive has en error', "",'[CR]www.youtube.com/@youplay.nostalgia') #Game archive has en error
            else:
                dialogok(title, file, localize(1446) + space + localize(21802), localize(13036, s=[localize(33003)]))
        if 'drive.google.com' in url: content = 1
        else: returned = "skip"
    else:
        pass
        
    '''There will be no download'''
    if returned == "skip": printpoint = printpoint + '9' ; return "skip"

    size = 1024 * 1024
    mb   = content / (1024 * 1024)

    if content < size:
        size = content

    total   = 0
    notify  = 0
    errors  = 0
    count   = 0
    resume  = 0
    sleep   = 0

    if silent == False or exe != "":
        returned = dialogyesno(to_utf8(title) + addonString_servicefeatherence(32138).encode('utf-8') + '[CR]' + to_utf8(file), addonString_servicefeatherence(32139).encode('utf-8') % (to_utf8(mb)) + '[CR]' + addonString_servicefeatherence(32140).encode('utf-8'), nolabel=localize(222),  yeslabel=localize(12321))
        if returned != 'ok':
			return "abort"

    text = 'Download File Size : %dMB %s ' % (mb, dest)
    printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")

    #f = open(dest, mode='wb')
    f = xbmcvfs.File(dest, 'w')

    chunk  = None
    chunks = []
    
    

    while True and not xbmc.abortRequested:
        downloaded = total
        for c in chunks:
            downloaded += len(c)
        percent = min(100 * downloaded / content, 100)
        if percent >= notify:
			if silent != True or exe != "":
				xbmc.executebuiltin( "XBMC.Notification(%s,%s,%i)" % ( title + " - " + str(percent)+'%', dest, 10000))

				text = 'Download percent : %s %s %dMB downloaded : %sMB File Size : %sMB' % (str(percent)+'%', dest, mb, downloaded / 1000000, content / 1000000)
				printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")

				notify += percentinfo

        chunk = None
        error = False

        try:        
            chunk  = resp.read(size)
            if not chunk:
                if percent < 99:
                    error = True
                else:
                    while len(chunks) > 0 and not xbmc.abortRequested:
                        c = chunks.pop(0)
                        f.write(c)
                        del c

                    f.close()
                    #print '%s download complete' % (dest)
                    if not xbmc.Player().isPlaying() and silent != True:
                        xbmcgui.Dialog().ok(title, dest, '' , 'Download finished')
                    return "ok"
					
        except Exception, e:
            text = str(e)
            printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")
			
            error = True
            sleep = 10
            errno = 0

            if hasattr(e, 'errno'):
                errno = e.errno

            if errno == 10035: # 'A non-blocking socket operation could not be completed immediately'
                pass

            if errno == 10054: #'An existing connection was forcibly closed by the remote host'
                errors = 10 #force resume
                sleep  = 30

            if errno == 11001: # 'getaddrinfo failed'
                errors = 10 #force resume
                sleep  = 30

        if chunk:
            errors = 0
            chunks.append(chunk)
            if len(chunks) > 5:
                c = chunks.pop(0)
                f.write(c)
                total += len(c)
                del c

        if error:
            errors += 1
            count  += 1
            text = '%d Error(s) whilst downloading %s' % (count, dest)
            printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")
            xbmc.sleep(sleep*1000)

        if (resumable and errors > 0) or errors >= 10:
            if (not resumable and resume >= 10) or resume >= 100:
                #Give up!
                text = '%s download canceled - too many error whilst downloading' % (dest)
                printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")
                xbmcgui.Dialog().ok(title, dest, '' , 'Download failed')
                return "error"

            resume += 1
            errors  = 0
            if resumable:
                chunks  = []
                #create new response
                text = 'Download resumed (%d) %s' % (resume, dest)
                printlog(title="doDownload", printpoint=printpoint, text=text, level=1, option="")
                resp, TypeError = getResponse(url, total, referer, agent, cookie, silent)
            else:
                #use existing response
                pass


if __name__ == '__main__':
    if 'commondownloader.py' in sys.argv[0]:
        doDownload(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])