#encoding=utf-8
'''
Created on 2014.8.28

@author: guanzx

    设置专门用于解析tt/tr字段的定时任务，每小时的第10分钟解析前1小时的日志,将解析后的日志按小时存临时文件
    >>> python parser.py
    >>> 10 * * * * cd /disk11/core/;python parser.py &
'''

from sys import argv

from config import Configuration
from utils import *
from logparser import LogParser

def deligateParserObject(input_dir_day,tmp_dir,log_dir,date_str,hour):
    """ 调用解析日志文件的对象. """
    logParser = LogParser(input_dir_day,tmp_dir,log_dir,date_str,hour)
    logParser.handleHaLogsByHour()

if __name__ == '__main__':

    if len(argv) == 2: 
        statDate = argv[1]
    else:
        statDate = getHourAgo(1)

    date_str = statDate[:8]
    hour = statDate[8:]
    config = Configuration("conf/p9.cfg")
    input_dir,output_dir,tmp_dir,log_dir = config.getConfigDir()
    input_dir_day = formatInputDir(input_dir,date_str)
    deligateParserObject(input_dir_day,tmp_dir,log_dir,date_str,hour)
    
    