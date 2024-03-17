import os
import json

with open('/usr/share/plainDE/release_data', 'r') as releaseReader:
    release = releaseReader.read()
    if release.endswith('\n'):
        release = release[:-1]

cfgPath = f'{os.getenv("HOME")}/.config/plainDE/config.json'
with open(cfgPath, 'r') as cfgReader:
    config = json.load(cfgReader)

configVersion = config['configVersion']
if configVersion != release:
    with open('/usr/share/plainDE/defaultCfg.json', 'r') as cfgReader:
        defaultConfig = json.load(cfgReader)

    for entry in defaultConfig:
        if not entry.startswith('panel'):
            if entry not in config:
                config[entry] = defaultConfig[entry]
            elif not isinstance(config[entry], type(defaultConfig[entry])):
                commentedKey = f'#{entry}'
                config[commentedKey] = config[entry]
                config[entry] = defaultConfig[entry]

    config['configVersion'] = release

    with open(cfgPath, 'w') as cfgWriter:
        json.dump(config, cfgWriter, indent=4)
