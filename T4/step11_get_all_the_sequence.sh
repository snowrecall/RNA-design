#!/bin/bash

for i in 1

do

#echo ${i}

line=`sed -n "${i}p" left_1bulge_out_consider_base_pair.list`

#echo ${line}

#echo $i

python consider_new_generate_RNA_sequence_like_P5c_like.py ${line} ${i}

done
