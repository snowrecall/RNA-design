#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCAGGAAGGGCAACUUUCACAACGCGCC&name=seq128&top=100"
./mcfold.static.exe >seq128_5bp_267_GCstem_3nt_bulges.data
