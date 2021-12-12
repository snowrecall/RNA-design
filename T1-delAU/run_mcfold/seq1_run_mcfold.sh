#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGAAGGGCAACUUUC&name=seq1&top=100"
./mcfold.static.exe >seq1_5bp_267_minus1bp_all_possible.data
