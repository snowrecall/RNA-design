#!/bin/bash

for i in {1..788}

do

python step9_calculate_each_sequence_2D_type.py step8_seq${i}.out>>./all_the_788_seq_have_the_2d_types_deltaG_form.txt

done
