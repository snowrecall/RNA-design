#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGAAGGGCAACUUUA&name=seq2&top=100"
./mcfold.static.exe >seq2_5bp_267_minus1bp_all_possible.data
