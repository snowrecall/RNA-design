#!/bin/bash

for i in {1..788}

do

python step2_delete_deltaG_larger_than_3.py seq${i}_set_python_input_2D_info.txt >> step2_3.out

done
