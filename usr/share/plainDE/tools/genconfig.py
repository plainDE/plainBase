import os
import json

releaseVersion = ''
with open('/usr/share/plainDE/release_data', 'r') as reader:
	releaseVersion = reader.read()[:-1]

config = {'accent': '#376594',
		  'appMenuTriangularTabs': True,
		  'applets': ['appmenu', 'windowlist',
					  'spacer', 'workspaces',
					  'volume', 'kblayout',
					  'datetime', 'splitter',
					  'usermenu'],
		  'autostart': [],
		  'background': '',
		  'configVersion': releaseVersion,
		  'dateFormat': 'MMM d',
		  'enableAnimation': True,
		  'expandPanel': True,
		  'favApps': [],
		  'firstDayOfWeek': 1,
		  'fontFamily': 'Open Sans',
		  'fontSize': 10,
		  'iconTheme': '',
		  'kbLayoutToggle': 'grp:win_space_toggle',
		  'kbLayouts': 'us',
		  'menuIcon': '/usr/share/plainDE/menuIcon.png',
		  'menuText': 'Apps',
		  'panelHeight': 28,
		  'panelLocation': 'top',
		  'panelOpacity': 0.85,
		  'showDate': True,
		  'theme': 'gradient-light.qss',
		  'timeFormat': 'h:mm AP',
		  'useCountryFlag': True,
		  'xOffset': 0}


homePath = os.getenv('HOME')
dirPath = homePath + '/.config/plainDE'
if not(os.path.exists(dirPath)):
	if os.path.exists(homePath + '/.config'):
		os.mkdir(dirPath)
	else:
		os.mkdir(homePath + '/.config/')
		os.mkdir(dirPath)


with open(dirPath + '/config.json', 'w') as configWriter:
	json.dump(config, configWriter)
