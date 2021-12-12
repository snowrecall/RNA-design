#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAACGGAAGGGCAACUUUCAAACCGCGCC&name=seq40&top=100"
./mcfold.static.exe >seq40_5bp_267_GCstem_3nt_bulges.data
