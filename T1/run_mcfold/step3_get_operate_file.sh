#!/bin/bash

for i in {1..216}

do

###total number of rows###

a=`wc -l seq${i}_5bp_267_GCstem_3nt_bulges.data|awk -F ' ' '{print $1}'`

a=$[$a-4]

###the last match of >seqN###

b=`sed -n "/>seq${i}/=" seq${i}_5bp_267_GCstem_3nt_bulges.data|tail -n1`

sed -n "${b},${a}p" seq${i}_5bp_267_GCstem_3nt_bulges.data >./seq${i}_set_python_input_2D_info.txt

done
