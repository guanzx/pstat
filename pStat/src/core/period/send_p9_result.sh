#!/bin/bash

output_dir=/disk_c3/pstat/data/out
code_dir=/disk_c3/pstat/core/period

python ${code_dir}/calc_period.py ${output_dir}/all.csv ${output_dir}/period_result 
python ${code_dir}/p9mail.py ${output_dir}/period_result