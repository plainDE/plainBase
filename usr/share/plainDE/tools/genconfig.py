import os
import json

releaseVersion = ''
with open('/usr/share/plainDE/release_data', 'r') as reader:
	releaseVersion = reader.read()[:-1]

config = {'accent': '#376594',
		  'appMenuTriangularTabs': True,
		  'autostart': [],
		  'background': '',
		  'configVersion': releaseVersion,
		  'dateFormat': 'MMM d',
		  'enableAnimation': True,
		  'favApps': [],
		  'firstDayOfWeek': 1,
		  'fontFamily': 'Open Sans',
		  'fontSize': 10,
		  'iconTheme': '',
		  'kbLayoutToggle': 'grp:win_space_toggle',
		  'kbLayouts': 'us',
		  'menuIcon': '/usr/share/plainDE/menuIcon.png',
		  'menuText': 'Apps',
		  'showDate': True,
		  'theme': 'gradient-light.qss',
		  'timeFormat': 'h:mm AP',
		  'useCountryFlag': True,
		  'ipIfname': '',
		  'panel1': {
		  	'applets': ['appmenu', 
						'spacer', 
						'mpris', 
						'volume', 
						'kblayout', 
						'datetime', 
						'splitter', 
						'usermenu'],
			'expand': True,
			'height': 28,
			'location': "top",
			'opacity': 0.85,
			'xOffset': 0
		  },
		  'panel2': {
		  	'applets': ['windowlist',
						'spacer',
						'localipv4',
						'workspaces'],
			'expand': True,
			'height': 28,
			'location': "bottom",
			'opacity': 0.85,
			'xOffset': 0
		  } 
		 }


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
