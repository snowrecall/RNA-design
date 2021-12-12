#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGAAAGGAAGGGCAACUUUCACAACGCGCC&name=seq2&top=100"
./mcfold.static.exe >seq2_5bp_267_GCstem_3nt_bulges.data
