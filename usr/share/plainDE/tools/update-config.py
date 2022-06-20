import os
import json

currentRelease = ''
with open('/usr/share/plainDE/release_data', 'r') as releaseReader:
	currentRelease = releaseReader.read()[:-1]

currentConfig = dict()
configDir = os.getenv('HOME') + '/.config/plainDE/'
with open(configDir + 'config.json', 'r') as configReader:
	json.load(currentConfig, configReader)

if currentConfig['configVersion'] != currentRelease:
	os.rename(configDir + 'config.json', configDir + 'config.json.sav')
	os.system('python3 /usr/share/plainDE/tools/genconfig.py')
	
	newConfig = dict()
	with open(configDir + 'config.json', 'r') as configReader:
		json.load(newConfig, configReader)
	
	for key in newConfig.keys():
		if not(key in currentConfig.keys()):
			currentConfig[key] = newConfig[key]
		elif not(isinstance(currentConfig[key], type(newConfig[key]))):
			currentConfig[key] = newConfig[key]

	with open(configDir + 'config.json.sav', 'w') as configWriter:
		json.dump(currentConfig, configWriter)
	
	os.remove(configDir + 'config.json')
	os.rename(configDir + 'config.json.sav', configDir + 'config.json')
