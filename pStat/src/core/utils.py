#!encoding=utf-8
'''
Created on 2014.8.26

@author: guanzx
'''

import os,time,datetime

def get_days_ago_day_str(n):
    """ 获取前n天的日期"""
    today = datetime.date.today()
    bdt = time.mktime(today.timetuple())
    bdt -= n*24*60*60
    ndt = datetime.datetime.fromtimestamp(bdt)
    return ndt.strftime('%Y%m%d')

def getHourAgo(n):
    """ 获取前一天的数据"""
    current = time.time()
    current -= n*60*60
    ndt = time.localtime(current)
    return time.strftime("%Y%m%d%H", ndt)

def getFormatHour(hour):
    if hour <= 9:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    return hour

def writeStdOutLog(log_dir,logstr,date_str):
    file_dir = log_dir +"/"+ date_str + "/"
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    outLog = open(file_dir + 'day_output.log','a')
    outLog.write(logstr + os.linesep)
    outLog.close()

def writeErrorlog(log_dir,logstr,date_str):
    file_dir = log_dir +"/"+ date_str + "/"
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    errorLog = open(file_dir  + 'day_error.log','a')
    errorLog.write(logstr + os.linesep)
    errorLog.close()
    
def deleteFileIfExist(fileName):
    if os.path.isfile(fileName):
        os.remove(fileName)

def makeDirIfNotExist(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def formatInputDir(input_dir,date_str):
    year,month,day = getYMD(date_str)
    return input_dir +"/"+ year + month +'/' + day + '/' 

def getYMD(date_str):
    year = date_str[0:4]
    month = date_str[4:6]
    day = date_str[6:]
    return year,month,day

def get_currrent_month_str():
    today = datetime.date.today()
    return today.strftime('%Y%m')

def is_valid_date(date_str):
    try:
        time.strptime(date_str, "%Y%m%d")
        return True
    except:
        return False

def clearSortTmpDir(tmp_dir,date_str):
    """ 清除临时路径中的文件. """
    tmp_dir = tmp_dir + "/" + date_str + "/"
    dir_pub_mc = tmp_dir + 'count_pub_mc_'+date_str;
    dir_pub_tt = tmp_dir + 'pub_tt_'+date_str;
    dir_pub_tr = tmp_dir + 'pub_tr_'+date_str;
    dir_mc_tt = tmp_dir + 'mc_tt_'+date_str;
    dir_mc_tr = tmp_dir + 'mc_tr_'+date_str;
    dir_pub_tt_sort = tmp_dir + 'pub_tt.sort';
    dir_pub_tr_sort = tmp_dir + 'pub_tr.sort';
    dir_mc_tt_sort = tmp_dir + 'mc_tt.sort';
    dir_mc_tr_sort = tmp_dir + 'mc_tr.sort';
    deleteFileIfExist(dir_pub_mc)
    deleteFileIfExist(dir_pub_tt)
    deleteFileIfExist(dir_pub_tr)
    deleteFileIfExist(dir_mc_tt)
    deleteFileIfExist(dir_mc_tr)
    deleteFileIfExist(dir_pub_tt_sort)
    deleteFileIfExist(dir_pub_tr_sort)
    deleteFileIfExist(dir_mc_tt_sort)
    deleteFileIfExist(dir_mc_tr_sort)