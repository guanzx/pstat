#!usr/bin/python
#encoding=utf-8
'''
Created on 2014.8.26

@author: guanzx

    设置定时任务，解析完tt/tr日志后，开始运行该脚本，每天4点执行前一天的解析好的数据
    >>> 00 05 * * *  cd /disk11/core/; python controller.py &
'''

from sys import argv,exit
from utils import *
from calculate import Calculate
from send_graphite import *
from config import Configuration
from merge_sort import *

def gatherData(data_dict,all_data):
    for k,v in data_dict.iteritems():
        if k not in all_data:
            all_data[k] = v
    return all_data
    
def getDateStr(date_str,pub_count,mc_count,pub_tt_data,pub_tr_data,mc_tt_data,mc_tr_data):
    all_data = {}
    all_data = gatherData(pub_tt_data,all_data)
    all_data = gatherData(pub_tr_data,all_data)
    all_data = gatherData(mc_tt_data,all_data)
    all_data = gatherData(mc_tr_data,all_data)
    list = [date_str,str(pub_count),str(mc_count)]
    for key in sorted(all_data.keys()):
        list.append(str(all_data[key]))
    return list

def saveDataAsCsv(date_str,pub_count,mc_count,output_dir,pub_tt_data,pub_tr_data,mc_tt_data,mc_tr_data):
    """ 
                为计算一周的数据，要把每天的指标存储在文件中，
    2种存储策略：(1)每月存储一个文件;(2)所有数据存储一个大文件 .
    """
    result_str = getDateStr(date_str,pub_count,mc_count,pub_tt_data,pub_tr_data,mc_tt_data,mc_tr_data)
    month_stat_file_name = output_dir+"/" + get_currrent_month_str() + '.csv'
    all_stat_file_name = output_dir +"/"+ "all.csv"
    if not os.path.isfile(month_stat_file_name) :
        month_stat_file = open(month_stat_file_name,'a')
        month_stat_file.write('date,pub_count,mc_count,mc_count_p90,mc_count_p95,mc_count_p98,mc_tr_sum,mc_tr_sum_p90,mc_tr_sum_p95,mc_tr_sum_p98,mc_tt_sum,mc_tt_sum_p90,mc_tt_sum_p95,mc_tt_sum_p98,pub_count_p90,pub_count_p95,pub_count_p98,pub_tr_sum,pub_tr_sum_p90,pub_tr_sum_p95,pub_tr_sum_p98,pub_tt_sum,pub_tt_sum_p90,pub_tt_sum_p95,pub_tt_sum_p98' + os.linesep)
        month_stat_file.close()
    
    month_stat_file = open(month_stat_file_name,'a')
    all_stat_file = open(all_stat_file_name,'a')   
    month_stat_file.write(','.join(result_str)+os.linesep)
    all_stat_file.write(','.join(result_str)+os.linesep)  
    month_stat_file.close()
    all_stat_file.close()
 
def calculate_pub_mc(tmp_dir,date_str):
    file_pub_mc = open(tmp_dir +"/"+date_str+ '/count_pub_mc_'+date_str,'r')
    pub_count = 0;
    mc_count = 0;
    for line in file_pub_mc:
        date_str,hour,pub,mc = line.rstrip().split(",")
        pub_count += int(pub)
        mc_count += int(mc)
    return pub_count,mc_count
  
if __name__ == '__main__':  
    
    if len(argv) >= 2: 
        date_str = argv[1]
        if is_valid_date(date_str):
            pass
        else:
            print "please enter the correct date[yyyymmdd]..."
            exit()
    else:
        date_str = get_days_ago_day_str(1)
    
    input_dir,output_dir,tmp_dir,log_dir = Configuration("conf/p9.cfg").getConfigDir()
    input_dir_day = formatInputDir(input_dir,date_str)

    clearSortTmpDir(tmp_dir,date_str)  
    
    #---merge and sort -------
    mergeLog(log_dir,tmp_dir,date_str)
    sortLog(log_dir,tmp_dir,date_str)
 
    #----计算性能指标------
    pub_count,mc_count = calculate_pub_mc(tmp_dir,date_str)
    calc = Calculate(tmp_dir+'/'+date_str+'/',pub_count,mc_count)
    writeStdOutLog(log_dir,time.ctime() + '  start calculate tt/tr .... ',date_str)
    pub_tt_data,pub_tt_pdata= calc.calculate_pub_tt()
    pub_tr_data,pub_tr_pdata= calc.calculate_pub_tr()
    mc_tt_data,mc_tt_pdata= calc.calculate_mc_tt()
    mc_tr_data,mc_tr_pdata= calc.calculate_mc_tr()
    writeStdOutLog(log_dir,time.ctime() + '  finish calculate tt/tr .... ',date_str)
    
    #----send to graphite----
    writeStdOutLog(log_dir,time.ctime() + '  send p-series data to graphite .... ',date_str)
    sendPubAndMcRequest(pub_count,mc_count)
    sendDataToGraphite(pub_tt_pdata,pub_tr_pdata,mc_tt_pdata,mc_tr_pdata)
    writeStdOutLog(log_dir,time.ctime() + '  send p-series data to graphite success.... ',date_str)
    
    #----save-----
    saveDataAsCsv(date_str,pub_count,mc_count,output_dir,pub_tt_data,pub_tr_data,mc_tt_data,mc_tr_data)
