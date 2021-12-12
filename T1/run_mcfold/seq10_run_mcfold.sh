#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAACGGAAGGGCAACUUUCAACACGCGCC&name=seq10&top=100"
./mcfold.static.exe >seq10_5bp_267_GCstem_3nt_bulges.data
