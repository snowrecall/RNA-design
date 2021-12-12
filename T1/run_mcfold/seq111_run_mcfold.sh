#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCAUGGAAGGGCAACUUUCACAACGCGCC&name=seq111&top=100"
./mcfold.static.exe >seq111_5bp_267_GCstem_3nt_bulges.data
