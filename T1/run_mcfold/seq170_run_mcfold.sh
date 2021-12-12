#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCAGGAAGGGCAACUUUCACUUCGCGCC&name=seq170&top=100"
./mcfold.static.exe >seq170_5bp_267_GCstem_3nt_bulges.data
