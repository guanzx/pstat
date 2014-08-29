#encoding=utf-8
'''
Created on 2014年8月29日

@author: guanzx
'''

from utils import *

def mergeLog(log_dir,tmp_dir,date_str): 
    for x in xrange(0,24):
        hh = getFormatHour(x)
        writeStdOutLog(log_dir,time.ctime() + '|'+ hh +' pub_tt merge start.... ' ,date_str)
        cmd = 'cat ' + tmp_dir + '/' + date_str + '/' + hh + '/pub_tt >> ' + tmp_dir + '/' +date_str +'/pub_tt_'+date_str
        os.system(cmd)
        writeStdOutLog(log_dir,time.ctime() + '|'+ hh +' pub_tr merge start.... ' ,date_str)
        cmd = 'cat ' + tmp_dir + '/' + date_str + '/' + hh + '/pub_tr >> ' + tmp_dir + '/' +date_str +'/pub_tr_'+date_str
        os.system(cmd)
        writeStdOutLog(log_dir,time.ctime() + '|'+ hh +' mc_tt merge start.... ' ,date_str)
        cmd = 'cat ' + tmp_dir + '/' + date_str + '/' + hh + '/mc_tt >> ' + tmp_dir + '/' +date_str +'/mc_tt_'+date_str
        os.system(cmd)
        writeStdOutLog(log_dir,time.ctime() + '|'+ hh +' mc_tr merge start.... ' ,date_str)
        cmd = 'cat ' + tmp_dir + '/' + date_str + '/' + hh + '/mc_tr >> ' + tmp_dir + '/' +date_str +'/mc_tr_'+date_str
        os.system(cmd)
        cmd = 'cat ' + tmp_dir + '/' + date_str + '/' + hh + '/count_pub_mc >> ' + tmp_dir + '/' +date_str +'/count_pub_mc_'+date_str
        os.system(cmd)

def sortLog(log_dir,tmp_dir,date_str):
    writeStdOutLog( log_dir,time.ctime() +' sort start... ' ,date_str)
    cmd = 'sort ' + tmp_dir +'/'+ date_str +'/pub_tt_'+date_str+ ' >> ' + tmp_dir + '/' +date_str+'/pub_tt.sort'
    os.system(cmd)
    writeStdOutLog( log_dir,time.ctime() + ' ' + cmd +' Done ' ,date_str)
    cmd = 'sort ' + tmp_dir +'/'+ date_str +'/pub_tr_'+date_str+ ' >> ' + tmp_dir + '/' +date_str+'/pub_tr.sort'
    os.system(cmd)
    writeStdOutLog( log_dir,time.ctime() + ' ' +  cmd + ' Done ' ,date_str)
    cmd = 'sort ' + tmp_dir +'/'+ date_str +'/mc_tr_'+date_str+ ' >> ' + tmp_dir + '/' +date_str+'/mc_tr.sort'
    os.system(cmd)
    writeStdOutLog( log_dir,time.ctime() + ' ' +  cmd + ' Done ' ,date_str)
    cmd = 'sort ' + tmp_dir +'/'+ date_str +'/mc_tt_'+date_str+ ' >> ' + tmp_dir + '/' +date_str+'/mc_tt.sort'
    os.system(cmd)
    writeStdOutLog( log_dir,time.ctime() + ' ' +  cmd + ' Done ' ,date_str)