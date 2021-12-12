#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCAAGGAAGGGCAACUUUCAAAUCGCGCC&name=seq145&top=100"
./mcfold.static.exe >seq145_5bp_267_GCstem_3nt_bulges.data
