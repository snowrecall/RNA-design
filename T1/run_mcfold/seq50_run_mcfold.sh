#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAUAGGAAGGGCAACUUUCACCCCGCGCC&name=seq50&top=100"
./mcfold.static.exe >seq50_5bp_267_GCstem_3nt_bulges.data
