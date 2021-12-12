#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCAAGGAAGGGCAACUUUCACAACGCGCC&name=seq110&top=100"
./mcfold.static.exe >seq110_5bp_267_GCstem_3nt_bulges.data
