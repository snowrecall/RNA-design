#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCAGGAAGGGCAACUUUCACACCGCGCC&name=seq200&top=100"
./mcfold.static.exe >seq200_5bp_267_GCstem_3nt_bulges.data
