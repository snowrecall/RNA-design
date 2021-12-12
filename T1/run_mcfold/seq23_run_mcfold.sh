#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCAUAACGCGCC&name=seq23&top=100"
./mcfold.static.exe >seq23_5bp_267_GCstem_3nt_bulges.data
