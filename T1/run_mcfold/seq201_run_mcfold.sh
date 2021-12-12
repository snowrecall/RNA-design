#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCUGGAAGGGCAACUUUCACACCGCGCC&name=seq201&top=100"
./mcfold.static.exe >seq201_5bp_267_GCstem_3nt_bulges.data
