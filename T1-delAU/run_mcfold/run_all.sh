#!/bin/bash

./step1_generate_all_possible_5bp267_minus1.py > 5bp267_minus1bp_all_possible.txt

sed -i 's/seq###//g' 5bp267_minus1bp_all_possible.txt
sed -i 's/ //g' 5bp267_minus1bp_all_possible.txt
sed -i '/^\s*$/d' 5bp267_minus1bp_all_possible.txt

./step2_run_mcfold.sh
./step3_get_operate_file.sh
./step_new_41_get_our_structures_and_deltaG.sh >step_new_41.out
./step_new_42_get_deltaG_value.sh >step_new_42.out
