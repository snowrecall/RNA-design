#!/bin/bash

for i in {1..27}

do

echo ">seq${i}" >>seq${i}_type_info.txt

sed -n '2p' seq${i}_set_python_input_2D_info.txt>>seq${i}_type_info.txt

grep '((((((\.(((\.\.)))))))))' seq${i}_set_python_input_2D_info.txt|head -n1>>seq${i}_type_info.txt 

grep '\.(((((((((\.\.)))))))))'  seq${i}_set_python_input_2D_info.txt|head -n1>>seq${i}_type_info.txt

done
