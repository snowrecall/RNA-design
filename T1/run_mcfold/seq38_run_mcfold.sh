#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAAGGAAGGGCAACUUUCACACCGCGCC&name=seq38&top=100"
./mcfold.static.exe >seq38_5bp_267_GCstem_3nt_bulges.data
