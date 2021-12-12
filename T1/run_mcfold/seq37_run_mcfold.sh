#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAAGGAAGGGCAACUUUCAAACCGCGCC&name=seq37&top=100"
./mcfold.static.exe >seq37_5bp_267_GCstem_3nt_bulges.data
