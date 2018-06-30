

def cacheplugin():
	try:
		from StorageServer import StorageServer
	except:
		import lib.storageserverdummy as StorageServer
	try:
	    import StorageServer
	except:
	    import storageserverdummy as StorageServer

	cache = StorageServer.StorageServer(addonID, 24) # (Your plugin name, Cache time in hours)
	
def addView_(viewtype):
    name = 'addView' ; printpoint = "" ; TypeError = "" ; extra = "" ; content = ""
    import xbmcvfs
    try:
		from sqlite3 import dbapi2 as database
    except:
		from pysqlite2 import dbapi2 as database
    
    try:
        skin = xbmc.getSkinDir()
        skinPath = xbmc.translatePath('special://skin/')
        xml = os.path.join(skinPath,'addon.xml')
        file = xbmcvfs.File(xml)
        read = file.read().replace('\n','')
        file.close()
        try: src = re.compile('defaultresolution="(.+?)"').findall(read)[0]
        except: src = re.compile('<res.+?folder="(.+?)"').findall(read)[0]
        src = os.path.join(skinPath, src)
        src = os.path.join(src, 'MyVideoNav.xml')
        file = xbmcvfs.File(src)
        read = file.read().replace('\n','')
        file.close()
        views = re.compile('<views>(.+?)</views>').findall(read)[0]
        views = [int(x) for x in views.split(',')]
        for view in views:
            label = xbmc.getInfoLabel('Control.GetLabel(%s)' % (view))
            if not (label == '' or label == None): break
        record = (skin, viewtype, str(view))
        xbmcvfs.mkdir(addonProfile)
        dbcon = database.connect(os.path.join(addonProfile, 'views.db'))
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS views (""skin TEXT, ""view_type TEXT, ""view_id TEXT, ""UNIQUE(skin, view_type)"");")
        dbcur.execute("DELETE FROM views WHERE skin = '%s' AND view_type = '%s'" % (record[0], record[1]))
        dbcur.execute("INSERT INTO views Values (?, ?, ?)", record)
        dbcon.commit()
        viewName = xbmc.getInfoLabel('Container.Viewmode')

        notification(addonString_servicefeatherence(32398).encode('utf-8'), viewName + str(view) , '', 2000)
    except Exception, TypeError:
        extra = 'TypeError' + space2 + str(TypeError)
        #return
	
	text = "content" + space2 + str(content) + space + newline + \
	'view' + space2 + str(view) + newline + \
	extra
	printlog(title=name, printpoint=printpoint, text=text, level=7, option="")
