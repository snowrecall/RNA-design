#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCCGGAAGGGCAACUUUCACCUCGCGCC&name=seq180&top=100"
./mcfold.static.exe >seq180_5bp_267_GCstem_3nt_bulges.data
