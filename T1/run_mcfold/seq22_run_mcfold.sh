#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCAAAACGCGCC&name=seq22&top=100"
./mcfold.static.exe >seq22_5bp_267_GCstem_3nt_bulges.data
