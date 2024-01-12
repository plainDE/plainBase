import os
import shutil

homePath = os.getenv('HOME')
cfgDirPath = homePath + '/.config/plainDE'
if not os.path.exists(cfgDirPath):
    os.makedirs(cfgDirPath)

if os.path.exists(cfgDirPath + '/config.json'):
    os.rename(cfgDirPath + '/config.json',
              cfgDirPath + '/config.json.sav')

shutil.copyfile('/usr/share/plainDE/defaultCfg.json',
                cfgDirPath + '/config.json')
