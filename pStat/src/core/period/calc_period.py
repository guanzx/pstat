#encoding=utf-8
'''
Created on 2014.8.26

@author: guanzx
'''

from sys import argv,exit

if len(argv) == 3:
    file_name = argv[1]
    out_file = argv[2]
else:
    print "path is wrong"
    exit()

total_lines = 0
for line in open(file_name):
    total_lines += 1

pub_tr = 0.0
pub_tr_p90 = 0.0
pub_tr_p95 = 0.0
pub_tr_p98 = 0.0
pub_tt = 0.0
pub_tt_p90 = 0.0
pub_tt_p95 = 0.0
pub_tt_p98 = 0.0
mc_tr = 0.0
mc_tr_p90 = 0.0
mc_tr_p95 = 0.0
mc_tr_p98 = 0.0
mc_tt = 0.0
mc_tt_p90 = 0.0
mc_tt_p95 = 0.0
mc_tt_p98 = 0.0

sum_pub_count = 0;
sum_pub_sum_tt = 0
sum_pub_sum_tr = 0
sum_pub_count_p90 = 0
sum_pub_sum_tt_90 = 0
sum_pub_sum_tr_90 = 0
sum_pub_count_p95 = 0
sum_pub_sum_tt_95 = 0
sum_pub_sum_tr_95 = 0
sum_pub_count_p98 = 0
sum_pub_sum_tt_98 = 0
sum_pub_sum_tr_98 = 0
sum_mc_count = 0
sum_mc_sum_tt = 0
sum_mc_sum_tr = 0
sum_mc_count_p90 = 0
sum_mc_sum_tt_90 = 0
sum_mc_sum_tr_90 = 0
sum_mc_count_p95 = 0
sum_mc_sum_tt_95 = 0
sum_mc_sum_tr_95 = 0
sum_mc_count_p98 = 0
sum_mc_sum_tt_98 = 0
sum_mc_sum_tr_98 = 0

cur_line_num = 0
for line in open(file_name):
    cur_line_num += 1
    if (cur_line_num > total_lines - 7): 
        columns = line.rstrip().split(',')
        pub_count = columns[1]
        pub_sum_tt = columns[21]
        pub_sum_tr = columns[17]
        pub_count_p90 = columns[14]
        pub_sum_tt_90 = columns[22]
        pub_sum_tr_90 = columns[18]
        pub_count_p95 = columns[15]
        pub_sum_tt_95 = columns[23]
        pub_sum_tr_95 = columns[19]
        pub_count_p98 = columns[16]
        pub_sum_tt_98 = columns[24]
        pub_sum_tr_98 = columns[20]
        mc_count = columns[2]
        mc_sum_tt = columns[10]
        mc_sum_tr = columns[6]
        mc_count_p90 = columns[3]
        mc_sum_tt_90 = columns[11]
        mc_sum_tr_90 = columns[7]
        mc_count_p95 = columns[4]
        mc_sum_tt_95 = columns[12]
        mc_sum_tr_95 = columns[8]
        mc_count_p98 = columns[5]
        mc_sum_tt_98 = columns[13]
        mc_sum_tr_98 = columns[9]
         
        sum_pub_count += float(pub_count)
        sum_pub_sum_tt += float(pub_sum_tt)   
        sum_pub_sum_tr += float(pub_sum_tr)
        sum_pub_count_p90 += float(pub_count_p90)
        sum_pub_sum_tt_90 += float(pub_sum_tt_90)
        sum_pub_sum_tr_90 += float(pub_sum_tr_90)
        sum_pub_count_p95 += float(pub_count_p95)
        sum_pub_sum_tt_95 += float(pub_sum_tt_95)
        sum_pub_sum_tr_95 += float(pub_sum_tr_95)
        sum_pub_count_p98 += float(pub_count_p98)
        sum_pub_sum_tt_98 += float(pub_sum_tt_98)
        sum_pub_sum_tr_98 += float(pub_sum_tr_98)
        sum_mc_count += float(mc_count)
        sum_mc_sum_tt += float(mc_sum_tt)
        sum_mc_sum_tr += float(mc_sum_tr)
        sum_mc_count_p90 += float(mc_count_p90)
        sum_mc_sum_tt_90 += float(mc_sum_tt_90)
        sum_mc_sum_tr_90 += float(mc_sum_tr_90)
        sum_mc_count_p95 += float(mc_count_p95)
        sum_mc_sum_tt_95 += float(mc_sum_tt_95)
        sum_mc_sum_tr_95 += float(mc_sum_tr_95)
        sum_mc_count_p98 += float(mc_count_p98)
        sum_mc_sum_tt_98 += float(mc_sum_tt_98)
        sum_mc_sum_tr_98 += float(mc_sum_tr_98)

pub_tr = float(sum_pub_sum_tr)/float(sum_pub_count)
pub_tr_p90 = float(sum_pub_sum_tr_90)/float(sum_pub_count_p90) 
pub_tr_p95 = float(sum_pub_sum_tr_95)/float(sum_pub_count_p95)
pub_tr_p98 = float(sum_pub_sum_tr_98)/float(sum_pub_count_p98)
pub_tt = float(sum_pub_sum_tt)/float(sum_pub_count)
pub_tt_p90 = float(sum_pub_sum_tt_90)/float(sum_pub_count_p90) 
pub_tt_p95 = float(sum_pub_sum_tt_95)/float(sum_pub_count_p95)
pub_tt_p98 = float(sum_pub_sum_tt_98)/float(sum_pub_count_p98)
mc_tr = float(sum_mc_sum_tr)/float(sum_mc_count)
mc_tr_p90 = float(sum_mc_sum_tr_90)/float(sum_mc_count_p90) 
mc_tr_p95 = float(sum_mc_sum_tr_95)/float(sum_mc_count_p95)
mc_tr_p98 = float(sum_mc_sum_tr_98)/float(sum_mc_count_p98)
mc_tt = float(sum_mc_sum_tt)/float(sum_mc_count)
mc_tt_p90 = float(sum_mc_sum_tt_90)/float(sum_mc_count_p90)
mc_tt_p95 = float(sum_mc_sum_tt_95)/float(sum_mc_count_p95)
mc_tt_p98 = float(sum_mc_sum_tt_98)/float(sum_mc_count_p98)


result = "pub_tr = " + str(pub_tr) + " ms \n" +"pub_tr_p90 = " + str(pub_tr_p90) + " ms \n" +"pub_tr_p95 = " + str(pub_tr_p95) + " ms \n"+"pub_tr_p98 = " + str(pub_tr_p98) + " ms \n"+"pub_tt = " + str(pub_tt) + " ms \n" +"pub_tt_p90 = " + str(pub_tt_p90) + " ms \n" +"pub_tt_p95 = " + str(pub_tt_p95) + " ms \n"+"pub_tt_p98 = " + str(pub_tt_p98) + " ms \n"+ "mc_tr = " + str(mc_tr) + " ms \n" + "mc_tr_p90 = " + str(mc_tr_p90) + " ms \n"+ "mc_tr_p95 = " + str(mc_tr_p95) + " ms \n"+ "mc_tr_p98 = " + str(mc_tr_p98) + " ms \n"+ "mc_tt = " + str(mc_tt) + " ms \n"+ "mc_tt_p90 = " + str(mc_tt_p90) + " ms \n"+ "mc_tt_p95 = " + str(mc_tt_p95) + " ms \n"+ "mc_tt_p98 = " + str(mc_tt_p98) + " ms"

p = open(out_file,"w")

print >> p,result