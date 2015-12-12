![](http://i.imgur.com/zfdrpSG.png)

# **Features:**

* This addon is a core for every Featherence's addon.
* Wide range of tools to be used from within Kodi.
* Wide range of modules to be used by addons developers.
* Widget to be used on any supported skin.
* IR remote control for OpenELEC os.
* Please note that many modules are being used in Featherence skin and are not possible on others skins yet.


# **Available scripts commands:**

```
SOFT-RESTART (Terminal supported)
RunScript(script.featherence.service,,?mode=50)
```

```
RESTART (Terminal supported)
RunScript(script.featherence.service,,?mode=51)
```

```
SUSPEND (Terminal supported)
RunScript(script.featherence.service,,?mode=52)
```

```
POWEROFF (Terminal supported)
RunScript(script.featherence.service,,?mode=53)
```

```
QUIT (Terminal supported)
RunScript(script.featherence.service,,?mode=54)
```

```
LAUNCH EXTENDEDINFO MOVIES INFO
RunScript(script.featherence.service,,?mode=70&amp;value=0)
```

```
LAUNCH EXTENDEDINFO TVSHOWS INFO
RunScript(script.featherence.service,,?mode=70&amp;value=1)
```

```
LAUNCH EXTENDEDINFO ACTORS INFO
RunScript(script.featherence.service,,?mode=70&amp;value=3)
```

```
LAUNCH EXTENDEDINFO DIRECTOR INFO
RunScript(script.featherence.service,,?mode=70&amp;value=4)
```

```
OPEN CUSTOM DIALOG TEXT VIEWER
RunScript(script.featherence.service,,?mode=31&amp;value=header&amp;value2=message)
```

```
READ FROM FILE AND DISPLAY
RunScript(script.featherence.service,,?mode=31&amp;value=header&amp;value2=message&amp;value3=filepath)
```

# **Integrating Widget:**
* [Match Skin Widgets Property](http://kodi.wiki/view/Add-on:Skin_Widgets)

```
Run Widget Recent Movie
<onclick>RunScript(script.featherence.service,,?mode=24&amp;value=RecentMovie.1)</onclick>
```

```
Run Widget Random Movie Trailer Full screen
<onclick>RunScript(script.featherence.service,,?mode=24&amp;value=RecentMovie.1&amp;value2=trailers)</onclick>
```

```
Run Widget Random Movie Trailer
<onclick>RunScript(script.featherence.service,,?mode=24&amp;value=RecentMovie.10&amp;value2=trailers2)</onclick>
```

```
Run Widget Recent Episode
<onclick>RunScript(script.featherence.service,,?mode=24&amp;value=RecentEpisode.1)</onclick>
```

```
Run Widget Recommended Episode
<onclick>RunScript(script.featherence.service,,?mode=24&amp;value=RecommendedEpisode.10)</onclick>
```

```
Auto Refresh Widget contents upon end of Movie / Episode
VideoFullScreen.xml
<onload condition="IsEmpty(Window(home).Property(mode10))">RunScript(script.featherence.service,,?mode=10)</onload>
```

```
Refresh Widget
RunScript(script.featherence.service,,?mode=23)
```

```
PLAY RANDOM TRAILERS
RunScript(script.featherence.service,,?mode=25)
```

# **Links:**

* [Facebook](https://www.facebook.com/groups/featherence/)
* [YouTube](https://www.youtube.com/user/finalmakerr)
* [Featherence Repository](https://github.com/finalmakerr/featherence/raw/master/repository.featherence/repository.featherence-1.1.0.zip)
