#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGGAAGGGCAACUUUCUGA&name=seq1&explore=50&top=100"
./mcfold.static.exe >seq1_5bp_267_add2bp_all_possible.data
