#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAUGGAAGGGCAACUUUCACCCCGCGCC&name=seq45&top=100"
./mcfold.static.exe >seq45_5bp_267_GCstem_3nt_bulges.data
