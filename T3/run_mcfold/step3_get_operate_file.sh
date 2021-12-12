#!/bin/bash

for i in {1..411}

do

###total number of rows###

a=`wc -l seq${i}_like_p5c_shift_2bp_type3.data|awk -F ' ' '{print $1}'`

a=$[$a-4]

###the last match of >seqN###

b=`sed -n "/>seq${i}/=" seq${i}_like_p5c_shift_2bp_type3.data|tail -n1`

sed -n "${b},${a}p" seq${i}_like_p5c_shift_2bp_type3.data >./seq${i}_set_python_input_2D_info.txt

done
