#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACUGGAAGGGCAACUUUCACCACGCGCC&name=seq33&top=100"
./mcfold.static.exe >seq33_5bp_267_GCstem_3nt_bulges.data
