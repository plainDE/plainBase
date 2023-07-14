import os
import json

releaseVersion = ''
with open('/usr/share/plainDE/release_data', 'r') as reader:
	releaseVersion = reader.read()[:-1]

config = {'accent': '#376594',
	  'avatar': '',
	  'winListIconSize': 22,
          'ipColor': '#ffffff',
		  'useTriangularTabs': False,
		  'autostart': [],
		  'background': '',
		  'countPanels': 4,
		  'configVersion': releaseVersion,
		  'dateFormat': 'MMM d',
		  'enableAnimation': True,
	  	  'enableOveramplification': False,
		  'favApps': [],
		  'firstDayOfWeek': 1,
		  'fontFamily': 'Open Sans',
		  'fontSize': 10,
		  'iconTheme': '',
		  'kbLayoutToggle': 'grp:win_space_toggle',
		  'kbLayouts': 'us',
		  'menuIcon': '/usr/share/plainDE/menuIcon.png',
	  	  'menuIconSize': 16,
		  'menuText': 'Apps',
		  'showDate': True,
		  'theme': 'gradient-dark.qss',
		  'timeFormat': 'h:mm AP',
		  'useCountryFlag': True,
	  	  'volumeAdjustMethod': 'ALSA',
		  'ipIfname': '',
		  'winListShowTitles': True,
		  'showWeekNumbers': True,
		  'panel1': {
		  	'applets': ['appmenu', 
						'spacer',
                        'sni', 
						'battery',
						'mpris', 
						'volume', 
						'kblayout', 
						'datetime', 
						'splitter', 
						'usermenu'],
			'expand': True,
			'thickness': 28,
			'location': "top",
			'opacity': 0.85,
			'shift': 0,
			'spacing': 5,
			'launcherIconSize': 22
		  },
		  'panel2': {
		  	'applets': ['windowlist',
						'spacer',
						'localipv4',
						'workspaces'],
			'expand': True,
			'thickness': 28,
			'location': "bottom",
			'opacity': 0.85,
			'shift': 0,
			'spacing': 5,
			'launcherIconSize': 22
		  },
		  'panel3': None,
		  'panel4': None
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
