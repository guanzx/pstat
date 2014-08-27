#encoding=utf-8
'''
Created on 2014.08.26

@author: guanzx
'''

import os
from utils import *

class Calculate(object):
    """ 具体的计算类,计算tt/tr指标值. """
    
    def __init__(self,tmpDir,pubCount,mcCount):
        self.tmp_dir = tmpDir
        self.pub_count = pubCount
        self.mc_count = mcCount

    def initCountParam(self,calcType):
        if calcType == "pub":
            pub_count_90 = self.pub_count * 0.9
            pub_count_95 = self.pub_count * 0.95
            pub_count_98 = self.pub_count * 0.98
            return pub_count_90,pub_count_95,pub_count_98
        elif calcType == "mc":
            mc_count_90 = self.mc_count * 0.9
            mc_count_95 = self.mc_count * 0.95
            mc_count_98 = self.mc_count * 0.98
            return mc_count_90,mc_count_95,mc_count_98
    
    def saveAsDict(self,sum,avg,sum_p90,avg_p90,count_p90,sum_p95,avg_p95,count_p95,sum_p98,avg_p98,count_p98,calcType,tType):
        data={}
        pData = {} 
        pData[tType+"_p90"] = avg_p90
        pData[tType+"_p95"] = avg_p95
        pData[tType+"_p98"] = avg_p98
        
        data[calcType+"_"+tType+"_sum"] = sum
        data[calcType+"_"+tType+"_sum_p90"] = sum_p90 
        data[calcType+"_"+tType+"_sum_p95"] = sum_p95  
        data[calcType+"_"+tType+"_sum_p98"] = sum_p98   
        
        data[calcType+"_count_p90"] = count_p90
        data[calcType+"_count_p95"] = count_p95
        data[calcType+"_count_p98"] = count_p98
        return data,pData
    
    def calculate(self,sort_file,calcType,tType):
        """ haproxy计算tt/tr均值及p90、p95、p98. """
        counter = 0
        sum = 0
        avg = 0
        sum_p90 = 0
        avg_p90 = 0 
        sum_p95 = 0
        avg_p95 = 0
        sum_p98 = 0
        avg_p98 = 0
        count_p90,count_p95,count_p98 = self.initCountParam(calcType)
        for line in sort_file :
            counter += 1
            value_str = line.lstrip('0').rstrip().rstrip(os.linesep)
            value_int = 0.0
            if (value_str ) and (value_str != '') :
                value_int = float(value_str)
            
            sum += value_int
            if counter <= count_p90 :
                sum_p90 += value_int
            if counter <= count_p95:
                sum_p95 += value_int
            if counter <= count_p98:
                sum_p98 += value_int
        
        if self.pub_count != 0:
            avg = float(sum) / float(self.pub_count)
            avg_p90 = float(sum_p90) / float(count_p90)
            avg_p95 = float(sum_p95) / float(count_p95)
            avg_p98 = float(sum_p98) / float(count_p98)  
        return self.saveAsDict(sum,avg,sum_p90,avg_p90,count_p90,sum_p95,avg_p95,count_p95,sum_p98,avg_p98,count_p98,calcType,tType)
    
    def calculate_pub_tt(self):
        file_pub_tt_sort = open(self.tmp_dir + 'pub_tt.sort','r')   
        return self.calculate(file_pub_tt_sort,"pub","tt")
                  
    def calculate_pub_tr(self):
        file_pub_tr_sort = open(self.tmp_dir + 'pub_tr.sort','r')  
        return self.calculate(file_pub_tr_sort,"pub","tr")
    
    def calculate_mc_tt(self):
        file_mc_tt_sort = open(self.tmp_dir + 'mc_tt.sort','r')
        return self.calculate(file_mc_tt_sort, "mc", "tt")
    
    def calculate_mc_tr(self):
        file_mc_tr_sort = open(self.tmp_dir + 'mc_tr.sort','r')
        return self.calculate(file_mc_tr_sort, "mc", "tr")
