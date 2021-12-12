#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACAGGAAGGGCAACUUUCACAACGCGCC&name=seq20&top=100"
./mcfold.static.exe >seq20_5bp_267_GCstem_3nt_bulges.data
