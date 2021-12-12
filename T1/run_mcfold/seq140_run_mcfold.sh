#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCAGGAAGGGCAACUUUCACCACGCGCC&name=seq140&top=100"
./mcfold.static.exe >seq140_5bp_267_GCstem_3nt_bulges.data
