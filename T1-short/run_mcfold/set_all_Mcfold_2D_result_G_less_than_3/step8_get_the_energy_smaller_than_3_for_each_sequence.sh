#!/bin/bash

for i in {1..788}

do

python step7_change_the_energy_to_delta.py seq${i}_set_python_input_2D_info.txt >> step8_seq${i}.out

done
