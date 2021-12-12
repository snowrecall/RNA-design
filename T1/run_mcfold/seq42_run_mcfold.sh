#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAACGGAAGGGCAACUUUCACACCGCGCC&name=seq42&top=100"
./mcfold.static.exe >seq42_5bp_267_GCstem_3nt_bulges.data
