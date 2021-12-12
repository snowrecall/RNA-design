#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAUGGAAGGGCAACUUUCACAACGCGCC&name=seq3&top=100"
./mcfold.static.exe >seq3_5bp_267_GCstem_3nt_bulges.data
