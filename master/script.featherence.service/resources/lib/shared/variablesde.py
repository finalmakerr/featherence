# -*- coding: utf-8 -*-
import xbmc
#from variablesp import addonID
from shared_modules import get_types, printlog

from shared_variables import space, space2, newline
def getDebug(value):
	returned = "" ; name='getDebug' ; value_len = 0 ; extra = ""
	value_len = len(value)
	check = get_types(value)
	
	#print str(value_len)
	#print str(value) #.encode('utf-8')
	if 'list' in check:
		for x in value:
			if 'א' in x: returned = str(returned) +  't'
			elif 'ב' in x: returned = str(returned) + 'b'
			elif 'ג' in x: returned = str(returned) + 'd'
			elif 'ד' in x: returned = str(returned) + 's'
			elif 'ה' in x: returned = str(returned) + 'v'
			elif 'ו' in x: returned = str(returned) + 'u'
			elif 'ז' in x: returned = str(returned) + 'z'
			elif 'ח' in x: returned = str(returned) + 'j'
			elif 'ט' in x: returned = str(returned) + 'y'
			elif 'י' in x: returned = str(returned) + 'h'
			elif 'כ' in x: returned = str(returned) + 'f'
			elif 'ך' in x: returned = str(returned) + 'l'
			elif 'ל' in x: returned = str(returned) + 'k'
			elif 'מ' in x: returned = str(returned) + 'n'
			elif 'ם' in x: returned = str(returned) + 'o'
			elif 'נ' in x: returned = str(returned) + 'b'
			elif 'ן' in x: returned = str(returned) + 'i'
			elif 'ס' in x: returned = str(returned) + 'x'
			elif 'ע' in x: returned = str(returned) + 'g'
			elif 'פ' in x: returned = str(returned) + 'p'
			elif 'ף' in x: returned = str(returned) + 'm'
			elif 'צ' in x: returned = str(returned) + 'm'
			elif 'ץ' in x: returned = str(returned) + '.'
			elif 'ק' in x: returned = str(returned) + 'e'
			elif 'ר' in x: returned = str(returned) + 'r'
			elif 'ש' in x: returned = str(returned) + 'a'
			elif 'ת' in x: returned = str(returned) + ','
			else: returned = str(returned) + str(x)
			extra = str(extra) + newline + 'x' + space2 + str(x) + space + 'returned' + space2 + str(returned)
	
	return returned
	
ap = "r"
bp = "o"
cp = "m"
dp = "1"
ep = "2"
fp = "3"
gp = "4"
hp = "5"
hi = "6"
ip = "d"
jp = "D"
kp = "#"
sendtostr = "htptdebugout@gmail.com"
sendtostr1 = "htptdebugout@mail.com"
sendtostr2 = "htptdebugout2@gmail.com"
sendtostr3 = "htptdebugout3@gmail.com"
sendtostr4 = "htptdebugout4@gmail.com"
sendtostr5 = "htptdebugout@outlook.com"
sendtostr14 = "htptdebugout@yahoo.com"
recipientstr = "fixhtpt@gmail.com"
recipientstr2 = "infohtpt@gmail.com"
'''---------------------------'''
mystr = ap + bp + cp + dp + ep + fp + gp + hp + hi
mystr2 = ap + bp + cp + dp + ep + fp + gp + hp
mystr3 = ['ר', 'ם', 'מ', '1', '2', '3', '4', '5']
mystr3 = getDebug(mystr3)