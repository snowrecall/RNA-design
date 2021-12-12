#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAUCGGAAGGGCAACUUUCAACCCGCGCC&name=seq52&top=100"
./mcfold.static.exe >seq52_5bp_267_GCstem_3nt_bulges.data
