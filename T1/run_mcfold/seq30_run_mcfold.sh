#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCACUACGCGCC&name=seq30&top=100"
./mcfold.static.exe >seq30_5bp_267_GCstem_3nt_bulges.data
