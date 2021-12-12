#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCACACCGCGCC&name=seq60&top=100"
./mcfold.static.exe >seq60_5bp_267_GCstem_3nt_bulges.data
