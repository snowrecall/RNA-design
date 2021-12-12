#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAUUGGAAGGGCAACUUUCACCACGCGCC&name=seq15&top=100"
./mcfold.static.exe >seq15_5bp_267_GCstem_3nt_bulges.data
