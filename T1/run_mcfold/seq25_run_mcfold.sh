#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACAGGAAGGGCAACUUUCAAUACGCGCC&name=seq25&top=100"
./mcfold.static.exe >seq25_5bp_267_GCstem_3nt_bulges.data
