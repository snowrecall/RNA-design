#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCACGGAAGGGCAACUUUCACCACGCGCC&name=seq120&top=100"
./mcfold.static.exe >seq120_5bp_267_GCstem_3nt_bulges.data
