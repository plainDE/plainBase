import os
import json

config = {'accent': '#376594',
		  'appMenuTriangularTabs': True,
		  'applets': ['appmenu', 'windowlist',
					  'spacer', 'workspaces',
					  'volume', 'kblayout',
					  'datetime', 'splitter',
					  'usermenu'],
		  'autostart': [],
		  'background': '',
		  'dateFormat': 'MMM d',
		  'enableAnimation': True,
		  'expandPanel': True,
		  'favApps': [],
		  'firstDayOfWeek': 'Monday',
		  'fontFamily': 'Open Sans',
		  'fontSize': 10,
		  'iconTheme': '',
		  'menuIcon': '/usr/share/plainDE/menuIcon.png',
		  'menuText': 'Apps',
		  'panelHeight': 28,
		  'panelLocation': 'top',
		  'panelOpacity': 0.85,
		  'showDate': True,
		  'theme': 'gradient-light.qss',
		  'timeFormat': 'h:mm AP',
		  'xOffset': 0}


homePath = os.getenv('HOME')
dirPath = homePath + '/.config/plainDE'
if os.path.exists(homePath + '/.config'):
	os.mkdir(dirPath)
else:
	os.mkdir(homePath + '/.config/')
	os.mkdir(dirPath)


with open(dirPath + '/config.json', 'w') as configWriter:
	json.dump(config, configWriter)
