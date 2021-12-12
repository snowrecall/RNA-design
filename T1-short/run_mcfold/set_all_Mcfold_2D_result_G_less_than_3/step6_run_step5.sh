#!/bin/bash

for i in {1..788}

do

python step5_calculate_each_sequence_2D_type.py seq${i}_set_python_input_2D_info.txt>>./all_the_788_seq_have_the_2d_types.txt

done
