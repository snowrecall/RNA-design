#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACUGGAAGGGCAACUUUCACAACGCGCC&name=seq21&top=100"
./mcfold.static.exe >seq21_5bp_267_GCstem_3nt_bulges.data
