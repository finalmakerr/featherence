# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *

from modulesZ import *
from modulesA import *
'''---------------------------'''
	
def CATEGORIES():
	'''------------------------------
	---MAIN--------------------------
	------------------------------'''
	try: General_Language = getsetting('General_Language')
	except: General_Language = systemlanguage
	
	CATEGORIES_SEARCH(mode=30, url="")
	addDir('-' + addonString(30000).encode('utf-8'),'',100,featherenceserviceicons_path + 'star.png',addonString_servicefeatherence(32800).encode('utf-8'),'1',0,getAddonFanart(100, urlcheck_=True)) #My ROFL
	
	addDir(addonString(30001).encode('utf-8'),'',101,featherenceserviceicons_path + 'fail.png','','1',0,getAddonFanart(101, default="http://funnyvtube.com/wp-content/uploads/2016/07/top-fails-march-2015-%E2%96%BA-best-funny-videos-%E2%96%BA-epic-fail-compilation-2015-%E2%84%961.jpg", urlcheck_=True)) #פספוסים
	addDir(addonString(30002).encode('utf-8'),'',102,featherenceserviceicons_path + 'tvshows.png','','1',0,getAddonFanart(102, default="http://saloona.co.il/netta/wp-content/blogs.dir/300/files/2011/06/ramzor.jpg", urlcheck_=True)) #תוכניות ישראליות
	addDir(addonString(30003).encode('utf-8'),'',103,featherenceserviceicons_path + 'bank.png','','1',2, getAddonFanart(103, default="https://miserylovescompanyuk.files.wordpress.com/2015/08/o-stage-microphone-facebook.jpg", urlcheck_=True)) #סטנדאפ ישראלי
	addDir(addonString(30004).encode('utf-8'),'',104,featherenceserviceicons_path + 'bank.png','','1',2, getAddonFanart(104, default="https://miserylovescompanyuk.files.wordpress.com/2015/08/o-stage-microphone-facebook.jpg", urlcheck_=True)) #סטנדאפ לועזי
	#addDir(addonString(200).encode('utf-8') % (General_Language),'',200,featherenceserviceicons_path + 'ud.png','[COLOR=red]1: %s | 2: %s | 3: %s[/COLOR]' % (General_Language, General_Language2, General_Language3) + '[CR]' + addonString_servicefeatherence(32081).encode('utf-8'),'1',0,getAddonFanart(200, urlcheck_=True)) #Forigen Language


def CATEGORIES100(name, iconimage, desc, fanart):
	'''------------------------------
	---My-ROFL-----------------------
	------------------------------'''
	fanart = 100
	'''כפתור הילדים שלי חדש..'''
	addDir(addonString_servicefeatherence(32450).encode('utf-8'),"New",20,featherenceserviceicons_path + 'clipboard.png',addonString_servicefeatherence(32451).encode('utf-8') + addonString_servicefeatherence(32452).encode('utf-8') + addonString_servicefeatherence(32453).encode('utf-8'),'s',0,getAddonFanart(fanart, urlcheck_=True))
	
	'''רשימת השמעה 1'''
	if Custom_Playlist1_ID != "": addDir(Custom_Playlist1_Name,Custom_Playlist1_ID,18,Custom_Playlist1_Thumb,Custom_Playlist1_Description,'1',0,getAddonFanart("Custom_Playlist1", urlcheck_=True))
	'''רשימת השמעה 2'''
	if Custom_Playlist2_ID != "": addDir(Custom_Playlist2_Name,Custom_Playlist2_ID,18,Custom_Playlist2_Thumb,Custom_Playlist2_Description,'2',0,getAddonFanart("Custom_Playlist2", urlcheck_=True))
	'''רשימת השמעה 3'''
	if Custom_Playlist3_ID != "": addDir(Custom_Playlist3_Name,Custom_Playlist3_ID,18,Custom_Playlist3_Thumb,Custom_Playlist3_Description,'3',0,getAddonFanart("Custom_Playlist3", urlcheck_=True))
	'''רשימת השמעה 4'''
	if Custom_Playlist4_ID != "": addDir(Custom_Playlist4_Name,Custom_Playlist4_ID,18,Custom_Playlist4_Thumb,Custom_Playlist4_Description,'4',0,getAddonFanart("Custom_Playlist4", urlcheck_=True))
	'''רשימת השמעה 5'''
	if Custom_Playlist5_ID != "": addDir(Custom_Playlist5_Name,Custom_Playlist5_ID,18,Custom_Playlist5_Thumb,Custom_Playlist5_Description,'5',0,getAddonFanart("Custom_Playlist5", urlcheck_=True))
	'''רשימת השמעה 6'''
	if Custom_Playlist6_ID != "": addDir(Custom_Playlist6_Name,Custom_Playlist6_ID,18,Custom_Playlist6_Thumb,Custom_Playlist6_Description,'6',0,getAddonFanart("Custom_Playlist6", urlcheck_=True))
	'''רשימת השמעה 7'''
	if Custom_Playlist7_ID != "": addDir(Custom_Playlist7_Name,Custom_Playlist7_ID,18,Custom_Playlist7_Thumb,Custom_Playlist7_Description,'7',0,getAddonFanart("Custom_Playlist7", urlcheck_=True))
	'''רשימת השמעה 8'''
	if Custom_Playlist8_ID != "": addDir(Custom_Playlist8_Name,Custom_Playlist8_ID,18,Custom_Playlist8_Thumb,Custom_Playlist8_Description,'8',0,getAddonFanart("Custom_Playlist8", urlcheck_=True))
	'''רשימת השמעה 9'''
	if Custom_Playlist9_ID != "": addDir(Custom_Playlist9_Name,Custom_Playlist9_ID,18,Custom_Playlist9_Thumb,Custom_Playlist9_Description,'9',0,getAddonFanart("Custom_Playlist9", urlcheck_=True))
	'''רשימת השמעה 10'''
	if Custom_Playlist10_ID != "": addDir(Custom_Playlist10_Name,Custom_Playlist10_ID,18,Custom_Playlist10_Thumb,Custom_Playlist10_Description,'10',0,getAddonFanart("Custom_Playlist10", urlcheck_=True))
	
	'''מעודפים'''
	addDir(localize(1036),"",32,featherenceserviceicons_path + 'star.png','','1',0,getAddonFanart(fanart, urlcheck_=True))

def CATEGORIES101(name, iconimage, desc, fanart):
	'''פספוסים'''
	'''30400-30499'''
	background = 101
	background2 = fanart
	
	'''Cihan Kosif TV'''
	list = []
	list.append('&youtube_ch=UCPgHR8p6lS1D5p-loVhk4xw')
	addDir(addonString(30409).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCPgHR8p6lS1D5p-loVhk4xw',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''Damn Fail'''
	list = []
	list.append('&youtube_ch=UCRvQ6H9unDQSOD0-qZ0EZog')
	addDir(addonString(30408).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCRvQ6H9unDQSOD0-qZ0EZog',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''DmPranksProductions'''
	list = []
	list.append('&youtube_ch=DmPranksProductions')
	addDir(addonString(30401).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=DmPranksProductions',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''failarmy'''
	list = []
	list.append('&youtube_ch=failarmy')
	addDir(addonString(30400).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=failarmy',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''FaiICity'''
	list = []
	list.append('&youtube_ch=FaiICity')
	addDir(addonString(30405).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=FaiICity',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''MegaFail'''
	list = []
	list.append('&youtube_ch=UCo4XcrQ5zB3DUwqa7lvNUeQ')
	addDir(addonString(30404).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCo4XcrQ5zB3DUwqa7lvNUeQ',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''MonthlyFails'''
	list = []
	list.append('&youtube_ch=UCEkZHiGsR4jvWeHunEB3Qaw')
	addDir(addonString(30403).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCEkZHiGsR4jvWeHunEB3Qaw',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''AvtoCrashCar'''
	list = []
	list.append('&youtube_ch=AvtoCrashCar')
	addDir(addonString(30410).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=AvtoCrashCar',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''The Best Fails'''
	list = []
	list.append('&youtube_ch=UCuunebfqIi8uCzAs_fO1D6Q')
	addDir(addonString(30406).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCuunebfqIi8uCzAs_fO1D6Q',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''Top10Compilations'''
	list = []
	list.append('&youtube_ch=UCZAtBTlxs-JzAagqGlWDpag')
	addDir(addonString(30407).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCZAtBTlxs-JzAagqGlWDpag',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''We Love Russia'''
	list = []
	list.append('&youtube_ch=UCZQxEoRjVRXysRZ0vFPrlfw')
	addDir(addonString(30402).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=UCZQxEoRjVRXysRZ0vFPrlfw',0,getAddonFanart(background, default='getAPIdata', custom=""))

def CATEGORIES102(name, iconimage, desc, fanart):
	background = 102
	background2 = fanart
	commonsearch = 'commonsearch101'
	'''30600-30699'''
	
	'''אחד העם'''
	
	'''ביפ קומדי בר'''
	desc_ = 'הכשרונות החדשים והמפתיעים של עולם הסטנד אפ הישראלי עולים על במת מועדון ה"ביפ קומדי בר" ונותנים את החומרים הכי טובים שיש להם להציע. ההופעות מבוצעות בפני קהל חי.'
	thumb = 'http://img.mako.co.il/2011/08/29/bip-comedy_b.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2011%2f08%2f29%2fbip-comedy_b.jpg&mode=1&name=%d7%91%d7%99%d7%a4%20%d7%a7%d7%95%d7%9e%d7%93%d7%99%20%d7%91%d7%a8&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-bip%2fcomedy-bar')
	list.append('&youtube_ch=TLVComedyBar')
	
	addDir(addonString(30661).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''החברים של נאור'''
	desc_ = ''
	thumb = 'http://www.sdarot.wf/media/series/8.jpg'
	list = []
	list.append('&youtube_pl=PL7v5SH1yPnx62P3_Khpr3lArK9dkmmpP7')
	list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f8.jpg&mode=3&name=%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%a0%d7%90%d7%95%d7%a8&series_id=8&series_name=%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d%20%d7%a9%d7%9c%20%d7%a0%d7%90%d7%95%d7%a8&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f8%2fhachaverim-shel-naor-%d7%94%d7%97%d7%91%d7%a8%d7%99%d7%9d-%d7%a9%d7%9c-%d7%a0%d7%90%d7%95%d7%a8')
	
	addDir(addonString(30662).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''הכל הולך'''
	list = []
	list.append('&youtube_pl=PLIuYAcnKhlM7yuZiCXJzSXNJvyVv8eXb0')
	
	addDir(addonString(30650).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=AnythingGoesIsrael',0,getAddonFanart(background, default='getAPIdata', custom=""))
	
	'''הפרלמנט'''
	desc_ = '"הפרלמנט" התחיל כמערכון בעונה השמינית של "ארץ נהדרת" , והפך לסדרה קומית בכיכובם של חמשת חבריו. הפרלמנט ימשיך להיפגש בבית הקפה השכונתי לדיונים על עניינים שברומו של עולם וגם שפחות ברומו, ובמהלך הסדרה נחשף גם לחיים הפרטיים וההזויים של שאולי, אמציה, הקטור, אבי וקרקו'
	thumb = 'http://img.mako.co.il/2013/10/03/parlament_1.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2013%2f10%2f03%2fparlament_1.jpg&mode=1&name=%d7%94%d7%a4%d7%a8%d7%9c%d7%9e%d7%a0%d7%98&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fparliament')
	
	addDir(addonString(30657).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''הסטנדאפיסטים'''
	desc_ = 'רשף לוי מלווה את הסטנדאפיסטים המובילים בישראל להופעה. בדרך הם מספרים על מאחורי הקלעים של הקריירה וכותבים בדיחות חדשות'
	thumb = 'http://img.mako.co.il/2016/08/25/stand-b.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2016%2f08%2f25%2fstand-b.jpg&mode=1&name=%d7%94%d7%a1%d7%98%d7%a0%d7%93%d7%90%d7%a4%d7%99%d7%a1%d7%98%d7%99%d7%9d&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fthe-comedians')
	
	addDir(addonString(30652).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''נוקאאוט'''
	desc_ = 'קרב המתיחות הראשון בטלוויזיה, בהנחיית עפר שכטר. שני מפורסמים נפגשים לתחרות ראשונה מסוגה – מי מותח הכי טוב'
	thumb = 'http://img.mako.co.il/2015/08/09/knockout.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2015%2f08%2f09%2fknockout.jpg&mode=1&name=%d7%a0%d7%95%d7%a7%d7%90%d7%90%d7%95%d7%98&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fknockout')
	
	addDir(addonString(30655).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''נראה אותך'''
	desc_ = 'אבי נוסבאום ושי גולדשטיין בשעשועון מצלמה נסתרת שמשתתפיו נקלעים אליו לגמרי במקרה. עם הגעת המשתתף למקום הוא מופנה לחדר צדדי שם מציעים לו המנחים להשתתף במשחק, ללא ידיעת בת או בן זוגו. במהלך המשימה עליו להישמע להוראותיהם ולמלא אחריהם בקפידה. במידה שיעמוד במשימות שיוטלו עליו, יוכל המתמודד להרוויח אלפי שקלים.'
	thumb = 'http://img.mako.co.il/2013/03/10/nire_otcha.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2013%2f03%2f10%2fnire_otcha.jpg&mode=1&name=%d7%a0%d7%a8%d7%90%d7%94%20%d7%90%d7%95%d7%aa%d7%9a&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fdare-you')
	
	addDir(addonString(30656).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''סברי מרנן'''
	desc_ = 'סיפורה של המשפחה הישראלית המוכרת: יש את "הצד שלו" ויש את "הצד שלה", והמושג "אמא פולניה" ו-"הכבוד המרוקאי" הם מושגים שכבר מזמן לא קשורים לעדה זו או אחרת, אלו סימפטומים... כאשר החוט המקשר בין כולנו הוא הקידוש וארוחות סוף השבוע.  כפי שנאמר בקזבלן פרק י"ג פסוק ז- "כולנו יהודים"'
	thumb = 'http://img.mako.co.il/2014/07/30/savri_maranan.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2014%2f07%2f30%2fsavri_maranan.jpg&mode=1&name=%d7%a1%d7%91%d7%a8%d7%99%20%d7%9e%d7%a8%d7%a0%d7%9f&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fsabri-maranan')
	
	addDir(addonString(30654).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''עם סגולה'''
	desc_ = 'תכנית מערכונים בכיכובם של שלישיית "מה קשור": אסי ישראלוף, ציון ברוך ושלום מיכאשווילי, אשר מביאה למסך דמויות חדשות של ישראלים הפזורים בנקודות שונות על פני הגלובוס, דמויות שיוכיחו שאפשר להוציא את הבנאדם מישראל אבל אי אפשר להוציא את ישראל מהבנאדם'
	thumb = 'http://img.mako.co.il/2011/09/01/am_sg2ula_b.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2011%2f09%2f01%2fam_sg2ula_b.jpg&mode=1&name=%d7%a2%d7%9d%20%d7%a1%d7%92%d7%95%d7%9c%d7%94&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fchosen-poeple')
	
	addDir(addonString(30660).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''צומת מילר'''
	desc_ = 'סדרת דרמה קומית חדשה על חייו של הסטאנדפיסט והקומיקאי אדיר מילר. לצידו של אדיר מילר משחקים גם מירי אלוני, גל זייד, אדווה בולה. בתפקידי אורח: שלמה ארצי, גורי אלפי, ליאור כלפון ואחרים'
	thumb = 'http://img.mako.co.il/2016/06/23/miller-b.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2016%2f06%2f23%2fmiller-b.jpg&mode=1&name=%d7%a6%d7%95%d7%9e%d7%aa%20%d7%9e%d7%99%d7%9c%d7%a8&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fmilers-crossroads')
	
	addDir(addonString(30653).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''צחוק מעבודה'''
	list = []
	
	list.append('&youtube_ch=tzchokmeavoda')
	addDir(addonString(30651).encode('utf-8'),list,17,'getAPIdata','getAPIdata','&getAPIdata=&youtube_ch=tzchokmeavoda',0,getAddonFanart(background, default='getAPIdata', custom=""))

	'''קומי קומי'''
	fanart = 'http://f.frogi.co.il/pic/bidur/IT/RA.png?r=1442740388'
	thumb = 'http://i.imgur.com/hRGIxPQ.png'
	list = []
	list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.pm%2fmedia%2fseries%2f1837.jpg&mode=3&name=comy-comy-%d7%a7%d7%95%d7%9e%d7%99-%d7%a7%d7%95%d7%9e%d7%99&series_id=1837&series_name=comy-comy-%d7%a7%d7%95%d7%9e%d7%99-%d7%a7%d7%95%d7%9e%d7%99&summary&url=http%3a%2f%2fwww.sdarot.pm%2fwatch%2f1837%2fcomy-comy-%d7%a7%d7%95%d7%9e%d7%99-%d7%a7%d7%95%d7%9e%d7%99')
	list.append('&youtube_pl=PLzXQC1m6QYoWsA7rgCJkAL4bqPRSiDhiY')
	list.append('&youtube_pl=PLX7Z5ey7NSDmmSPOEswfNedckidOnx1pS')
	
	addDir(addonString(30600).encode('utf-8'),list,17,thumb,addonString(30601).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רמזור'''
	desc_ = 'סדרה קומית על שלושה חברים בשנות השלושים לחייהם שמוצאים את עצמם בשלושה מצבי זוגיות שונים המשולים לאורות הרמזור: איצקו הנשוי הוא האור האדום והסטטי, אמיר נמצא במערכת יחסים מחייבת - האור צהוב המתנדנד ואילו חפר הוא הרווק הנצחי שנוסע חופשי בירוק. איך משפיעים הבדלי הזוגיות על הדרך בה הם חיים את חייהם?'
	thumb = 'http://img.mako.co.il/2014/03/27/ramzor_2014_b.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2014%2f03%2f27%2framzor_2014_b.jpg&mode=1&name=%d7%a8%d7%9e%d7%96%d7%95%d7%a8&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2framzor')
	
	addDir(addonString(30659).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
	'''תכנית קיציס'''
	desc_ = 'תכנית אירוח המסכמת את אירועי השבוע. כל תכנית מתארחים לשיחה אישית מרואיינים מובילים מתחומי הפוליטיקה, הבידור, הספורט והתרבות הישראלית ומשולבות בה פינות קומיות וסאטיריות'
	thumb = 'http://img.mako.co.il/2014/07/17/B-kitzis_.jpg'
	list = []
	list.append('&custom8=plugin://plugin.video.MakoTV/?iconimage=http%3a%2f%2fimg.mako.co.il%2f2014%2f07%2f17%2fB-kitzis_.jpg&mode=1&name=%d7%aa%d7%9b%d7%a0%d7%99%d7%aa%20%d7%a7%d7%99%d7%a6%d7%99%d7%a1&url=http%3a%2f%2fwww.mako.co.il%2fmako-vod-keshet%2fkitzis')
	
	addDir(addonString(30658).encode('utf-8'),list,17,thumb,desc_,'1',0,getAddonFanart(background, default=thumb, custom=""))
	
		
def CATEGORIES103(name, iconimage, desc, fanart):
	'''סטנדאפ ישראלי'''
	'''30100-30299'''
	
	background = 103
	background2 = fanart
	commonsearch = 'commonsearch103'
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	
	'''אבי קושניר'''
	fanart = 'http://megafon-news.co.il/asys/wp-content/uploads/2013/10/%D7%94%D7%97%D7%99%D7%99%D7%9C-%D7%94%D7%90%D7%9E%D7%99%D7%A5-%D7%A9%D7%95%D7%95%D7%99%D7%A7-%D7%90%D7%91%D7%99-%D7%A7%D7%95%D7%A9%D7%A0%D7%99%D7%A8-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%96%D7%A8%D7%90%D7%A8-%D7%90%D7%9C%D7%95%D7%9F.jpg' #גדול
	thumb = 'http://moridim.me/images/large/1745.jpg' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30100).encode('utf-8'),list,17,thumb,addonString(30101).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אדיר מילר'''
	fanart = 'http://cdn.maba.co.il/ckFiles/images/Tarbut/Events/Adir_Miller/Adir-Miller_1440x550.jpg'
	thumb = 'http://bubblesfest.com/images/photos/face23.jpg'
	list = []
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30102).encode('utf-8'),list,17,thumb,addonString(30103).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אדם שרון'''
	fanart = 'https://i.ytimg.com/vi/FojWxTSIPtw/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/p9YT-JGdDj0/hqdefault.jpg'
	list = []
	list.append('&youtube_pl=PLkGBxxiK0E6D0w0XESXsgnz419EpLb1lP')
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30104).encode('utf-8'),list,17,thumb,addonString(30105).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אורי חזקיה'''
	fanart = 'http://cdn.maba.co.il/ckFiles/images/Tarbut/Events/Uri_Hizkiya/Uri-Hizkia_1440x550.jpg'
	thumb = 'http://www.arieltarbut.co.il/images/bigimages/product_105.jpg'
	list = []
	list.append('&youtube_pl=PL-daUF_r2xa9m-B8aMW1nFhw6rVnmBVGI')
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30106).encode('utf-8'),list,17,thumb,addonString(30107).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אלי ומריאנו'''
	fanart = 'https://i.ytimg.com/vi/vmHTrcmE4zE/maxresdefault.jpg'
	thumb = 'http://www.yap.co.il/prdPics/351_desc3_3_1_1382273640.jpg'
	list = []
	list.append('&youtube_pl=PL2JwMsqYrzYCIoPp1yHVaA8004GjaYqgg')
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30108).encode('utf-8'),list,17,thumb,addonString(30103).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אלי יצפאן'''
	fanart = 'https://i.ytimg.com/vi/40E0pKQ-8uY/maxresdefault.jpg'
	thumb = 'http://dossinet.me/coverage_pics/c87a4f0749853b31b4b95edb69daf33f.jpg'
	list = []
	list.append('&youtube_pl=PLKFp2oldTIL3uxuNtRmXCUybuGG6wgFhn')
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30110).encode('utf-8'),list,17,thumb,addonString(30111).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אמירם טובים'''
	fanart = 'http://www.myavne.co.il/sites/yavne/UserContent/images/ARTICLES/ETI/MITGAYSIM/6.jpg'
	thumb = 'http://images1.ynet.co.il/PicServer3/2012/06/26/4007889/Alex.jpg_wa.jpg'
	list = []
	list.append('&youtube_pl=')
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30112).encode('utf-8'),list,17,thumb,addonString(30113).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אלעד גלעדי'''
	fanart = 'https://i.ytimg.com/vi/sr9bHTgVI38/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/Z_b7L_FB5iM/maxresdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30114).encode('utf-8'),list,17,thumb,addonString(30103).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אמיר הורוביץ'''
	fanart = 'https://i.ytimg.com/vi/kI9ueppGk1A/maxresdefault.jpg'
	thumb = 'http://images1.calcalist.co.il/PicServer2/20122005/389408/01_l.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30116).encode('utf-8'),list,17,thumb,addonString(30117).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אסף יצחקי'''
	fanart = 'https://i.ytimg.com/vi/Zp-Girt4tAQ/maxresdefault.jpg'
	thumb = 'http://images1.ynet.co.il/PicServer4/2014/09/01/5559950/55599491990100408258no.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30118).encode('utf-8'),list,17,thumb,addonString(30119).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''אסף מור יוסף'''
	fanart = 'https://i.ytimg.com/vi/wCd1pJW7NZQ/maxresdefault.jpg'
	thumb = 'http://asafmoryosef.com/2.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30120).encode('utf-8'),list,17,thumb,addonString(30121).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''ארז בירנבוים'''
	fanart = 'https://i.ytimg.com/vi/4AiastfNUd4/maxresdefault.jpg'
	thumb = 'http://calcalist.the-insider.co.il/wp-content/uploads/2015/07/Erez-Birenboim-hp.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30122).encode('utf-8'),list,17,thumb,addonString(30123).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''בן בן ברוך'''
	fanart = 'https://i.ytimg.com/vi/huK-w-nRobc/maxresdefault.jpg'
	thumb = 'https://img.grouponcdn.com/deal/jjk9DicFzwjiyxEm3ZeP/rR-700x420/v1/c700x420.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30124).encode('utf-8'),list,17,thumb,addonString(30125).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''בן לבקוביץ'''
	fanart = 'https://i.ytimg.com/vi/SDP81TTxbE4/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/zzjG7deq7vE/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30126).encode('utf-8'),list,17,thumb,addonString(30127).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''גדי וילצ'רסקי'''
	fanart = 'https://i.ytimg.com/vi/sOKnNg38VSw/maxresdefault.jpg'
	thumb = 'http://www.nrg.co.il/images/archive/465x349/1/553/153.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30128).encode('utf-8'),list,17,thumb,addonString(30129).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''גורי אלפי'''
	fanart = 'https://i.ytimg.com/vi/63peGGD0oOE/maxresdefault.jpg'
	thumb = 'http://www.nrg.co.il/images/archive/465x349/1/411/571.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30130).encode('utf-8'),list,17,thumb,addonString(30131).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''גיורא זינגר'''
	fanart = 'https://i.ytimg.com/vi/p9z2H9tAHWM/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/cz0CkifHL7Y/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30132).encode('utf-8'),list,17,thumb,addonString(30133).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''דדו מילמן'''
	fanart = 'https://i.ytimg.com/vi/9wNcFpfZaR4/maxresdefault.jpg'
	thumb = 'https://pbs.twimg.com/profile_images/3382033899/6b514a058ce5489e3c88347cc948dc70_400x400.jpeg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30134).encode('utf-8'),list,17,thumb,addonString(30135).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''דניאל חן'''
	fanart = ''
	thumb = ''
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30136).encode('utf-8'),list,17,thumb,addonString(30137).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''דניאל כהן'''
	fanart = 'https://i.ytimg.com/vi/SGgwR7Bu5nU/maxresdefault.jpg'
	thumb = 'https://www.goshow.co.il/application/views/website/timthumb.php?w=960&h=344&zc=1&q=80&src=https%3A%2F%2Fwww.goshow.co.il%2Fmanager%2Fuserfiles%2F2015%2F09%2F%D7%91%D7%90%D7%A0%D7%A8-%D7%A2%D7%9C%D7%99%D7%95%D7%9F-%D7%90%D7%AA%D7%A8-0.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30138).encode('utf-8'),list,17,thumb,addonString(30139).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''חיים אלמקיס'''
	fanart = 'http://img.mako.co.il/2011/04/03/comedy_bar_5_haim_almiax_c.jpg'
	thumb = 'https://i.ytimg.com/vi/o9_J55E9F3g/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30140).encode('utf-8'),list,17,thumb,addonString(30141).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''טל טירנגל'''
	fanart = 'https://i.ytimg.com/vi/dMicBOrGn6k/maxresdefault.jpg'
	thumb = 'http://mizbala.com/_uploads/images/2013/06/moneysong.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30142).encode('utf-8'),list,17,thumb,addonString(30143).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''חן מזרחי'''
	fanart = 'http://cdn.maba.co.il/ckFiles/images/Tarbut/Events/Hen_mizrachi/%D7%97%D7%9F-%D7%9E%D7%96%D7%A8%D7%97%D7%99-%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%A8%D7%99%D7%A9%D7%9E%D7%99%D7%AA_1440x550(1).jpg'
	thumb = 'http://www.matnasgan.org.il/html5/web/4450/11870ImageFile2.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30144).encode('utf-8'),list,17,thumb,addonString(30145).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''טל סולומון'''
	fanart = 'https://i.ytimg.com/vi/3y13xS0K4co/maxresdefault.jpg'
	thumb = 'http://images.mouse.co.il/storage//e/2/%D7%98%D7%9C.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30146).encode('utf-8'),list,17,thumb,addonString(30147).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יוחאי ספונדר'''
	fanart = 'https://i.ytimg.com/vi/nosdCc-6Mic/maxresdefault.jpg'
	thumb = 'http://www.mesibot.co.il/com-serve/Images/yohay_sponder_standup/yohay_sponder_standup_1.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30148).encode('utf-8'),list,17,thumb,addonString(30149).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יוסי גבני'''
	fanart = 'https://i.ytimg.com/vi/oDS18mFRknE/maxresdefault.jpg'
	thumb = 'http://www.pashbar.co.il/pictures/show_big_0207254001420978530.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30150).encode('utf-8'),list,17,thumb,addonString(30151).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יוסי טרבלוס'''
	fanart = 'https://i.ytimg.com/vi/rGOEGV16J1A/maxresdefault.jpg'
	thumb = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Yossi_Tarablus.JPG/250px-Yossi_Tarablus.JPG'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	list.append('&youtube_ch=latenight100')
	addDir(addonString(30218).encode('utf-8'),list,17,thumb,addonString(30219).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''ינאי בן נח'''
	fanart = 'https://i.ytimg.com/vi/KfSwVOEMzSQ/maxresdefault.jpg'
	thumb = 'http://comedychildren.com/wp-content/uploads/2013/07/a.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30152).encode('utf-8'),list,17,thumb,addonString(30153).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יעקב כהן'''
	fanart = 'http://www.shapam.co.il/_Uploads/602Yacov_Cohen.JPG'
	thumb = 'http://images1.ynet.co.il/xnet//PicServer2/pic/20122005/57202/6_735.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30154).encode('utf-8'),list,17,thumb,addonString(30155).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''יצפאן וסויסה'''
	fanart = 'https://i.ytimg.com/vi/P8Mki-Uzxi4/maxresdefault.jpg'
	thumb = 'http://img.youtube.com/vi/Swro4sG6nnM/0.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30156).encode('utf-8'),list,17,thumb,addonString(30157).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''ירמי שיק בלום'''
	fanart = 'https://i.ytimg.com/vi/6xkJ-hTnQoU/maxresdefault.jpg'
	thumb = 'http://room404.net/wp-content/uploads/2014/01/irmyshikblum.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30158).encode('utf-8'),list,17,thumb,addonString(30159).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''ישראל קטורזה'''
	fanart = 'https://i.ytimg.com/vi/t5n8_ulCipo/maxresdefault.jpg'
	thumb = 'http://img.mako.co.il/2009/06/04/uri030609k%5B1%5D.p-(9)c.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30160).encode('utf-8'),list,17,thumb,addonString(30161).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מאור ממן'''
	fanart = 'https://i.ytimg.com/vi/4JVvAXirhcU/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/0aWRsmr_wQM/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30162).encode('utf-8'),list,17,thumb,addonString(30163).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מוטי אהרונוביץ'''
	fanart = 'https://i.ytimg.com/vi/P9RYo2_qj7o/maxresdefault.jpg'
	thumb = 'http://images.mouse.co.il/storage//5/4/show_big_0260427001381400485.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30164).encode('utf-8'),list,17,thumb,addonString(30165).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מיטל אבני'''
	fanart = 'https://i.ytimg.com/vi/mWaf7xuinWw/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/JlPMIl95UT4/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30166).encode('utf-8'),list,17,thumb,addonString(30167).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מיטל שפירו'''
	fanart = ''
	thumb = 'http://www.bac.org.il/content/upload/images/%D7%9E%D7%99%D7%98%D7%9C_%D7%A9%D7%A4%D7%99%D7%A8%D7%95_%D7%A7%D7%A8%D7%93%D7%99%D7%98_emy_nechimovsky_(2).png'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30168).encode('utf-8'),list,17,thumb,addonString(30169).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''ירון ברלד'''
	fanart = 'https://i.ytimg.com/vi/Ui5dVLacr3c/maxresdefault.jpg'
	thumb = 'http://img.mako.co.il/2012/02/08/b2222131_g.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30170).encode('utf-8'),list,17,thumb,addonString(30171).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מיקי גבע'''
	fanart = 'https://i.ytimg.com/vi/2HQ0jPazkrY/maxresdefault.jpg'
	thumb = 'http://www.yitzug1.co.il/sites/default/files/styles/big_image/public/11_0.jpg?itok=eP3ghuSf'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30172).encode('utf-8'),list,17,thumb,addonString(30173).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מני מלכה'''
	fanart = 'https://i.ytimg.com/vi/-v4u0QWRPFU/maxresdefault.jpg'
	thumb = 'http://images7.webydo.com/91/9105287/3958%2F655ff644-48de-4cf6-ac1e-21798b748b93.png'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30174).encode('utf-8'),list,17,thumb,addonString(30176).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''מני עוזרי'''
	fanart = 'https://i.ytimg.com/vi/EVbBBtUA8Bw/maxresdefault.jpg'
	thumb = 'http://www.be106.net/upl/uploads/news_images/4924/original.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30176).encode('utf-8'),list,17,thumb,addonString(30177).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''נאור ציון'''
	fanart = 'http://i4.ytimg.com/vi/56GTTAHW1Wc/maxresdefault.jpg'
	thumb = 'http://cdn.ashdodnet.com/dyncontent/t_post/wp-content/uploads/64561.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30178).encode('utf-8'),list,17,thumb,addonString(30179).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''נדב אבוקסיס'''#עוד 21
	fanart = 'http://cdn.maba.co.il/ckFiles/images/Tarbut/Events/Nadav-Abuksis/_1440x550-nadav_2.jpg'
	thumb = 'http://www.ashdodnet.com/dyncontent/t_post/2014/12/9/735000546843443735536.JPG'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30180).encode('utf-8'),list,17,thumb,addonString(30181).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''צביקה הדר'''
	fanart = 'http://www.habama-center.com/wp-content/uploads/2014/11/%D7%A6%D7%91%D7%99%D7%A7%D7%94-%D7%94%D7%93%D7%A8-%D7%97%D7%99-%D7%A2%D7%9C-%D7%94%D7%91%D7%9E%D7%94.jpg'
	thumb = 'http://msc.wcdn.co.il/w/w-635/1872937-18.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30182).encode('utf-8'),list,17,thumb,addonString(30183).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''קארין כהן'''
	fanart = 'https://i.ytimg.com/vi/gkJP7UhaRHY/maxresdefault.jpg'
	thumb = 'http://www.yitzug1.co.il/sites/default/files/styles/big_image/public/%D7%90%D7%9C%D7%9B%D7%A1%20%D7%9C%D7%99%D7%A4%D7%A7%D7%99%D7%9F%203.jpg?itok=UIiuA-P3'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30184).encode('utf-8'),list,17,thumb,addonString(30185).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''קובי מימון'''
	fanart = 'https://i.ytimg.com/vi/zB12CyFBfmA/maxresdefault.jpg'
	thumb = 'http://tzavta.co.il/Upload/Images/%D7%91%D7%99%D7%93%D7%95%D7%A8/%D7%91%D7%99%D7%93%D7%95%D7%A8%20%D7%A4%D7%A0%D7%99%D7%9E%D7%99/kobi%20mimon.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30186).encode('utf-8'),list,17,thumb,addonString(30187).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רוני ששון'''
	fanart = 'https://www.google.co.il/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjNufCj_Y3LAhVM2BoKHYg3A5gQjBwIBA&url=http%3A%2F%2Fksn.co.il%2Fwp-content%2Fuploads%2F2015%2F10%2F%25D7%25A8%25D7%2595%25D7%25A0%25D7%2599-%25D7%25A9%25D7%25A9%25D7%2595%25D7%259F-%25D7%2591%25D7%259C%25D7%2592%25D7%25A0%25D7%25A1%25D7%25A7%25D7%2599.jpg&bvm=bv.114733917,d.d24&psig=AFQjCNGB-ewHcf8UpihCMt8kPOPnJ5eI-g&ust=1456319966533941'
	thumb = 'http://www.habama.co.il/Upload/MediaFiles/%D7%A8%D7%95%D7%A0%D7%99-%D7%A9%D7%A9%D7%95%D7%9F-1.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30188).encode('utf-8'),list,17,thumb,addonString(30189).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רועי כפרי''' #17
	fanart = 'https://i.ytimg.com/vi/gkM2FBiajmc/maxresdefault.jpg'
	thumb = 'http://albums.tapuz.co.il/flix/userPageDesign/userPicture2075228.bmp'
	list = []

	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30190).encode('utf-8'),list,17,thumb,addonString(30191).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רועי צברי'''
	fanart = 'https://eventsimg.blob.core.windows.net/banners/bdbcc39a5501630c0d7f26041ec98d0e'
	thumb = 'http://tarbutbanegev.merage.org.il/wp-content/uploads/2015/01/%D7%A8%D7%95%D7%A2%D7%99-%D7%A6%D7%91%D7%A8%D7%99-640x427.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30194).encode('utf-8'),list,17,thumb,addonString(30195).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רותם זיו'''
	fanart = 'https://i.ytimg.com/vi/plPCBA8HUL4/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/FLTVEeNc9RM/maxresdefault.jpg'
	list = []

	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30196).encode('utf-8'),list,17,thumb,addonString(30197).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''רמי ורד'''
	fanart = 'http://www.habama.co.il/Habama/Upload/other/%D7%A8%D7%9E%D7%99-%D7%95%D7%A8%D7%93-01.jpg'
	thumb = 'http://www.spectacles-israel.com/admin/images/rami-vered.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30198).encode('utf-8'),list,17,thumb,addonString(30199).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שאולי בדישי'''
	fanart = 'http://yoavgross.com/media/61786/%D7%A9%D7%90%D7%95%D7%9C%D7%99-%D7%91%D7%93%D7%99%D7%A9%D7%99-444.jpg'
	thumb = 'http://images7.webydo.com/91/9167411/3958%2F9D22C346-060F-6B97-7D7B-894966689D93.png'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30200).encode('utf-8'),list,17,thumb,addonString(30201).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שגיב פרידמן'''
	fanart = 'https://i.ytimg.com/vi/uYHSoLjOK8o/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/FyWH89y7KOU/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30202).encode('utf-8'),list,17,thumb,addonString(30203).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שחר חסון'''
	fanart = 'http://i4.ytimg.com/vi/w_DKHoHRdfo/maxresdefault.jpg'
	thumb = 'http://ksn.co.il/wp-content/uploads/2016/01/%D7%A9%D7%97%D7%A8-%D7%97%D7%A1%D7%95%D7%9F.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30204).encode('utf-8'),list,17,thumb,addonString(30205).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שי יום טוב'''
	fanart = 'https://i.ytimg.com/vi/oU2ft78YH8c/maxresdefault.jpg'
	thumb = 'https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-xpt1/v/t1.0-9/12112311_889990854371116_259787581650902869_n.jpg?oh=ade582dd58df1909f9a31d336275da2e&oe=5763D21E&__gda__=1465167189_1ca7921d7b8a9625d5eb6e599842f398'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30206).encode('utf-8'),list,17,thumb,addonString(30207).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שלישית מה קשור'''
	fanart = 'http://images1.ynet.co.il/PicServer2/02022009/1951658/DSC_2555_1280.jpg'
	thumb = 'http://www.kvootzati.co.il/Sites/kvoo/content/Images/ma-kashur-r.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30208).encode('utf-8'),list,17,thumb,addonString(30209).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שלישית פרוזק'''
	fanart = 'https://i.ytimg.com/vi/2iiD2f-k2Tk/maxresdefault.jpg'
	thumb = 'https://i.ytimg.com/vi/lNH95YC5tF0/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30210).encode('utf-8'),list,17,thumb,addonString(30211).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שמעון רגב'''
	fanart = ''
	thumb = 'https://i.ytimg.com/vi/yAPmMVjT-78/hqdefault.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30212).encode('utf-8'),list,17,thumb,addonString(30213).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שני מלמד'''
	fanart = 'https://i.ytimg.com/vi/2ZlW_WDACIA/maxresdefault.jpg'
	thumb = 'http://www.taasiya.co.il/sites/taasiya/_media/member_portfolio_items/11106_mpi_src_84482.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30214).encode('utf-8'),list,17,thumb,addonString(30215).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''שלום אסייג'''
	fanart = 'https://i.ytimg.com/vi/uUSoLE8kjrE/maxresdefault.jpg'
	thumb = 'http://tin.tv/site/wp-content/uploads/2012/10/Shalom-asayag-Yahatz.jpg'
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30216).encode('utf-8'),list,17,thumb,addonString(30217).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''תום יער'''
	fanart = ''
	thumb = ''
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30218).encode('utf-8'),list,17,thumb,addonString(30219).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''תמיר בוסקילה'''
	fanart = ''
	thumb = ''
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30220).encode('utf-8'),list,17,thumb,addonString(30221).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
def CATEGORIES104(name, iconimage, desc, fanart):
	'''סטנדאפ לועזי'''
	'''30800-30999'''
	
	background = 104
	background2 = fanart
	commonsearch = 'commonsearch104'
	
	CATEGORIES_RANDOM(background,fanart) #אקראי
	
	
	'''Bill Burr '''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30804).encode('utf-8'),list,17,thumb,addonString(30805).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Brian Regan'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30800).encode('utf-8'),list,17,thumb,addonString(30801).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Chris Rock'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30818).encode('utf-8'),list,17,thumb,addonString(30819).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Dave Chappelle'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30808).encode('utf-8'),list,17,thumb,addonString(30809).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Esther Povitsky'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30802).encode('utf-8'),list,17,thumb,addonString(30803).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''George Carlin'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30806).encode('utf-8'),list,17,thumb,addonString(30807).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Jim Carrey'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30814).encode('utf-8'),list,17,thumb,addonString(30815).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Lewis Black'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30812).encode('utf-8'),list,17,thumb,addonString(30813).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Louis CK'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30810).encode('utf-8'),list,17,thumb,addonString(30811).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Mitch Hedberg'''
	fanart = '' #גדול
	thumb = '' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30816).encode('utf-8'),list,17,thumb,addonString(30817).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	
	'''Russell Peters'''
	fanart = 'https://media.livenation.com/artists/78217/78217-show-94014.jpg?1386819141' #גדול
	thumb = 'http://www.metrocomedy.com/wp-content/uploads/2015/07/russell-peters.jpg' #בינוני
	list = []
	
	list.append('&youtube_se='+commonsearch)
	addDir(addonString(30820).encode('utf-8'),list,17,thumb,addonString(30821).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
	