import xbmc
import os, sys
import subprocess
import xbmcgui, xbmcaddon

from variables import *
from modules import *

url, name, mode, iconimage, desc, num, viewtype, fanart = pluginend(admin)

pluginend2(admin, url, containerfolderpath, viewtype)