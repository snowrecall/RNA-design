#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAACGGAAGGGCAACUUUCACCACGCGCC&name=seq12&top=100"
./mcfold.static.exe >seq12_5bp_267_GCstem_3nt_bulges.data
