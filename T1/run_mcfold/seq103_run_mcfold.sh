#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGUCAGGAAGGGCAACUUUCAACCCGCGCC&name=seq103&top=100"
./mcfold.static.exe >seq103_5bp_267_GCstem_3nt_bulges.data
