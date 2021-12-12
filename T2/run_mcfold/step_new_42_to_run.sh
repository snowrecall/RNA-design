#!/bin/bash

for i in {1..485}

do

python step_new_42_get_deltaG_value.py seq${i}_type_info.txt

done
