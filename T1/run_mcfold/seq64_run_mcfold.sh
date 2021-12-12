#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCAAUCCGCGCC&name=seq64&top=100"
./mcfold.static.exe >seq64_5bp_267_GCstem_3nt_bulges.data
