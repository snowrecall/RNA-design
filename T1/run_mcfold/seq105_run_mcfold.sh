#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGUCUGGAAGGGCAACUUUCACCCCGCGCC&name=seq105&top=100"
./mcfold.static.exe >seq105_5bp_267_GCstem_3nt_bulges.data
