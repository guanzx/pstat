#!/usr/bin/python
#encoding=utf-8

import os
import re
import time

from utils import *

class LogParser(object):
    """ 日志解析:用于对HA日志进行字段(tt/tr)解析."""

    def __init__(self,inputDir,tmpDir,logDir,dateStr,hour):
        self.input_dir_day = inputDir
        self.tmp_dir = tmpDir
        self.log_dir = logDir
        self.date_str = dateStr
        self.hour = hour
        self.date_dir = "/" + self.date_str + "/" + self.hour + "/"
         
    def parseHaLogs(self,logFile):
        """
                      解析每一行日志：
        Aug    25    0:00:00    192.168.111.145    haproxy[7736]:    42.236.168.45:4925    [24/Aug/2014:23:59:59.748]    front1    
        pub/pub_64    245/0/0/6/252    200    1772    -    -    #NAME?    1555/1555/21/0/0    0/0    {pub.funshion.com|}    {}    
        GET /interface/deliver?ap=ape_b_1&mid=113655&mtype=tv&uid=&mac=d4970b638c5f&fck=d4970b638c5fd4970b638c5f&refer=&client=aphone&ver=2.1.4.5&ext=dev%7Caphone_4.2.2_2013023;chan%7C1073;res%7C720*1280&idfa=&fudid=24CB85570EC60CC673C00FC6938BAA9589804AC4488F06C63186DB5104A58399&os=android&osver=4.2.2&imei=864645024749092&ispirvated=&access=1 HTTP/1.1                                        
        """
        log_file = open(logFile,'r')
        pub_count = 0
        mc_count = 0
        for line in log_file:
            columns = re.split('  | ',line)
            request_type = columns[8]
            site = request_type.split("/")[0]
        
            tt_tr = columns[9]
            tr = tt_tr.split("/")[3]
            tt = tt_tr.split("/")[4]         
            #such as 16 00000016
            tt_8 = '%08d' % (int(tt))
            tr_8 = '%08d' % (int(tr))
            if site == 'pub' :
                pub_count += 1
                self.file_pub_tt.write(tt_8 + os.linesep)
                self.file_pub_tr.write(tr_8 + os.linesep)
            elif site == 'mc' :
                mc_count += 1
                self.file_mc_tt.write(tt_8 + os.linesep)
                self.file_mc_tr.write(tr_8 + os.linesep)
        log_file.close()
        return pub_count,mc_count
    
    def openFileStream(self):  
        
        self.dir_pub_tt = self.tmp_dir + self.date_dir + 'pub_tt'
        self.dir_pub_tr = self.tmp_dir + self.date_dir + 'pub_tr'
        self.dir_mc_tt =  self.tmp_dir + self.date_dir + 'mc_tt'
        self.dir_mc_tr =  self.tmp_dir + self.date_dir + 'mc_tr'
        self.file_pub_tt = open(self.dir_pub_tt,'w')
        self.file_pub_tr = open(self.dir_pub_tr,'w')
        self.file_mc_tt = open(self.dir_mc_tt,'w')
        self.file_mc_tr = open(self.dir_mc_tr,'w') 
    
    def closeFileStream(self):
        self.file_pub_tt.close()
        self.file_pub_tr.close()
        self.file_mc_tt.close()
        self.file_mc_tr.close()
    
    def savePubAndMcCount(self,pub_count,mc_count):
        dir_pub_mc = self.tmp_dir + self.date_dir + "count_pub_mc"
        file_pub_mc = open(dir_pub_mc,'w')
        file_pub_mc.write(self.date_str + "," + self.hour + "," + str(pub_count) + ","+ str(mc_count) + os.linesep)
        file_pub_mc.close()
        
    def handleHaLogsByHour(self):       
        """ 对Ha日志按照小时进行解析处理，得到pub_count/mc_count指标，同时将tt/tr指标按照pub/mc存入4个不同的临时文件中，为后续排序做准备. """     
        hh = getFormatHour(self.hour)
        logFile = self.input_dir_day + 'access.'+ self.date_str + hh +'.log'
        if not os.path.isfile(logFile):
            writeErrorlog(self.log_dir,logFile+"  does not exists",self.date_str)
        else:
            writeStdOutLog(self.log_dir,time.ctime() + ' extracting log file ' + 'access.'+ self.date_str + hh +'.log',self.date_str)
            makeDirIfNotExist(self.tmp_dir + self.date_dir)
            self.openFileStream()
            pub_count,mc_count = self.parseHaLogs(logFile)
            self.closeFileStream()
            writeStdOutLog(self.log_dir,time.ctime() +  ' extract ' + 'access.'+ self.date_str + hh +'.log'+' finished...',self.date_str)
            self.savePubAndMcCount(pub_count,mc_count)

  
