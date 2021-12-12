#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGUCCGGAAGGGCAACUUUCACUCCGCGCC&name=seq102&top=100"
./mcfold.static.exe >seq102_5bp_267_GCstem_3nt_bulges.data
