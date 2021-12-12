#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGUCCGGAAGGGCAACUUUCAUUCCGCGCC&name=seq101&top=100"
./mcfold.static.exe >seq101_5bp_267_GCstem_3nt_bulges.data
