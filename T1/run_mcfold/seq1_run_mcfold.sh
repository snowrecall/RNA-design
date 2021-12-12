#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAAGGAAGGGCAACUUUCAAAACGCGCC&name=seq1&top=100"
./mcfold.static.exe >seq1_5bp_267_GCstem_3nt_bulges.data
