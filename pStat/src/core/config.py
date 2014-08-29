#encoding=utf-8
'''
Created on 2014年8月29日

@author: guanzx
'''

import ConfigParser

class Configuration(object):
    
    def __init__(self,confDir):   
        self._confDir = confDir
            
    def getConfigDir(self):
        """ 得到配置路径. """
        config = ConfigParser.ConfigParser()
        config.readfp(open(self._confDir))
        input_dir=config.get("config","input_dir")
        output_dir=config.get("config","output_dir")
        tmp_dir=config.get("config","tmp_dir")
        log_dir=config.get("config","log_dir")
        return input_dir,output_dir,tmp_dir,log_dir