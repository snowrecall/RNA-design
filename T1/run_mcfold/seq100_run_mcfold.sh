#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGUCCGGAAGGGCAACUUUCAAUCCGCGCC&name=seq100&top=100"
./mcfold.static.exe >seq100_5bp_267_GCstem_3nt_bulges.data
