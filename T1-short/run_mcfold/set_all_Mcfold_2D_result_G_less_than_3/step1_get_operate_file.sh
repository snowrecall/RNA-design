#!/bin/bash

for i in {1..788}

do

###total number of rows###

a=`wc -l seq${i}_P5c.dada|awk -F ' ' '{print $1}'`

a=$[$a-4]

###the last match of >seqN###

b=`sed -n "/>seq${i}/=" seq${i}_P5c.dada|tail -n1`

sed -n "${b},${a}p" seq${i}_P5c.dada >./seq${i}_set_python_input_2D_info.txt

done
