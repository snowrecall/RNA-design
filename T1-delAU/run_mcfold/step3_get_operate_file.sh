#!/bin/bash

for i in {1..5}

do

###total number of rows###

a=`wc -l seq${i}_5bp_267_minus1bp_all_possible.data|awk -F ' ' '{print $1}'`

a=$[$a-4]

###the last match of >seqN###

b=`sed -n "/>seq${i}/=" seq${i}_5bp_267_minus1bp_all_possible.data|tail -n1`

sed -n "${b},${a}p" seq${i}_5bp_267_minus1bp_all_possible.data >./seq${i}_set_python_input_2D_info.txt

done
