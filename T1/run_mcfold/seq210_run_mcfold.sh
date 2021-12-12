#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCCCGGAAGGGCAACUUUCACUCCGCGCC&name=seq210&top=100"
./mcfold.static.exe >seq210_5bp_267_GCstem_3nt_bulges.data
