#!/bin/bash

DATENOW=`(date +%F)`
#echo $DATENOW

LOGFILE=$HOME/.kodi/guikeeper.log
EXEFILE=$HOME/.kodi/guikeeper.txt
COMMAND=`head -1 "$EXEFILE"`

USERDATA_PATH=$HOME/.kodi/userdata
SKIN_USERDATA_PATH=$USERDATA_PATH/addon_data/skin.htpt/userdata

GUISETTINGS_FILE_=$USERDATA_PATH/guisettings.xml
GUISETTINGS2_FILE_=$SKIN_USERDATA_PATH/guisettings.xml
GUISETTINGS3_FILE_=$SKIN_USERDATA_PATH/guisettings2.xml
GUISETTINGS4_FILE_=$SKIN_USERDATA_PATH/guisettings_.xml

exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>$LOGFILE 2>&1

echo DATE: $DATENOW
echo COMMAND: $COMMAND
#echo HOME: $HOME
#echo USERDATA_PATH: $USERDATA_PATH
#echo SKIN_USERDATA_PATH: $SKIN_USERDATA_PATH
#echo GUISETTINGS_FILE_: $GUISETTINGS_FILE_
#echo GUISETTINGS2_FILE_: $GUISETTINGS2_FILE_


`$COMMAND`
#exec $COMMAND
#`$COMMAND`
#sh $COMMAND
#echo `"$COMMAND"`
	
#killall -9 org.xbmc.kodi && cp -f $GUISETTINGS4_FILE_ $GUISETTINGS_FILE_

exit
{ #SKIN_CHECK
echo
echo ----------------------------------------
PRINTPOINT=""
if [ $GUISETTINGS_FILE_CON1 -eq 0 ]; then
	echo Error: GUISETTINGS_FILE_CON1!
	PRINTPOINT=$PRINTPOINT\1
	if [ $GUISETTINGS_FILE2_CON1 -eq 0 ]; then
		PRINTPOINT=$PRINTPOINT\2
		if [ $GUISETTINGS_FILE3_CON1 -eq 0 ]; then
			PRINTPOINT=$PRINTPOINT\3
			echo NO BACKUP FOUND!
		else
			PRINTPOINT=$PRINTPOINT\4
			echo Copy: $USERDATA_PATH3/guisettings2.xml '->' $USERDATA_PATH/guisettings.xml
			cp -f $USERDATA_PATH3/guisettings2.xml $USERDATA_PATH/guisettings.xml
			RESET=$T
		fi
	else
		PRINTPOINT=$PRINTPOINT\5
		echo Copy: $USERDATA_PATH3/guisettings.xml '->' $USERDATA_PATH/guisettings.xml
		cp -f $USERDATA_PATH3/guisettings.xml $USERDATA_PATH/guisettings.xml
		RESET=$T
	fi

	
else
	if [ $GUISETTINGS_FILE2_CON1 -eq 0 ]; then
		PRINTPOINT=$PRINTPOINT\6
		echo Error: GUISETTINGS_FILE2_CON1!!
	else
		PRINTPOINT=$PRINTPOINT\7
		echo Old Backup: guisettings2.xml
		cp -f $USERDATA_PATH3/guisettings.xml $USERDATA_PATH3/guisettings2.xml
	fi
	if [ $VALIDATION2 -eq 1 ]; then ###must run before startup.xml (autostart.sh)
		PRINTPOINT=$PRINTPOINT\8
		echo New Backup: guisettings.xml
		cp -f $USERDATA_PATH/guisettings.xml $USERDATA_PATH3/guisettings.xml
	else
		PRINTPOINT=$PRINTPOINT\9
		echo ERROR: VALIDATION2!!! CANT CREATE NEW BACKUP $VALIDATION2
	fi
fi
echo
echo SKIN_CHECK_LV: $PRINTPOINT   '|'   RESET: $RESET
echo ----------------------------------------
}

{ #SERVICE_CHECK
SKIN_PATH=/storage/.kodi/addons/skin.htpt
SKIN_FOLDER_SIZE=`du $SKIN_PATH/ -s | awk {'print $1'}`
SERVICE_PATH=/storage/.kodi/addons/service.htpt
echo
echo ----------------------------------------
PRINTPOINT=""

if [ ! -d "$SERVICE_PATH" ]; then
	PRINTPOINT=$PRINTPOINT\1
	SERVICE_FILE=`$HOME/.kodi/addons/packages/service.htpt*`
	ls $SERVICE_FILE -r | awk {'print $1'} | tee /storage/servicepackage.log
	SERVICE_FILE1=`head -1 servicepackage.log`
	SERVICE_FILE1_SIZE=`du $SERVICE_FILE1 -s | awk {'print $1'}`
	SERVICE_FILE2=`sed -n 2p servicepackage.log`
	SERVICE_FILE2_SIZE=`du $SERVICE_FILE2 -s | awk {'print $1'}`
	SERVICE_FILE3=`sed -n 3p servicepackage.log`
	SERVICE_FILE3_SIZE=`du $SERVICE_FILE3 -s | awk {'print $1'}`
	
	if [ $SERVICE_FILE1 -gt 10000 ] && [ -f SERVICE_FILE1 ]; then
		PRINTPOINT=$PRINTPOINT\2
		echo EXTRACTING SERVICE_FILE1
		unzip -o -q $SERVICE_FILE1 -d /storage/.kodi/addons/
		rm $SERVICE_FILE1
		
		PERMISSION1=`ls -l /storage/.kodi/addons/service.htpt/specials/scripts/ | awk {'print $1'}`
		chmod +x $SERVICE_PATH/specials/scripts/*
		PERMISSION2=`ls -l /storage/.kodi/addons/service.htpt/specials/scripts/ | awk {'print $1'}`
		echo EXTRACTING COMPLETE! $PERMISSION1 -'>' $PERMISSION2
		#RESET=$T
	else
		PRINTPOINT=$PRINTPOINT\3
		echo SERVICE_FILE NOT FOUNDS!
	fi

else
	PRINTPOINT=$PRINTPOINT\7
fi
echo
echo SERVICE_CHECK_LV: $PRINTPOINT
echo ----------------------------------------
}

{ ###SKIN
	ALL='[^ ]*<'
	SKIN='<skin>'
	SKIN2='<skin default="true">'
	SKINHTPT='skin.htpt<'
	###SED
	#sed -i "s/$SKIN$ALL/$SKIN$SKINHTPT/g" $SETTINGS
	#sed -i "s/$SKIN2$ALL/$SKIN$SKINHTPT/g" $SETTINGS
}
	
if [ $RESET == $T ]; then
	
	echo RESET = $RESET -'>' killall, sleep4 && sleep 2 && killall -9 kodi.bin && sed -i "s/$SKIN$ALL/$SKIN$SKINHTPT/g" $GUI && sed -i "s/$SKIN2$ALL/$SKIN$SKINHTPT/g" $GUI
	
else
	{ ## CustomGUI
	if [ $CustomGUI != '"true"' ]; then
		$HOME/.kodi/addons/service.htpt.fix/specials/scripts/copygui.sh
		#$HOME/.kodi/addons/service.htpt/specials/scripts/copyfix.sh
		
	else
		echo CustomGUI IS TRUE
	fi
	}
	
	sleep 1
fi


###GET CustomGUI###
GUI=$HOME/.kodi/userdata/guisettings.xml
FIND1='>[^ ]*<' ###?###
FINDIN=$GUI
FINDWHAT='"skin.htpt.CustomGUI"'
FINDLINE=`find $FINDIN -type f -exec grep $FINDWHAT /dev/null {} \;`
FINDEXACT=`echo $FINDLINE | grep -o '>[^ ]*<' | sed 's/[<>]//g'`
CUSTOMGUI='"'$FINDEXACT'"'

