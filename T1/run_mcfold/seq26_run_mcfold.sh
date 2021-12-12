#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACAGGAAGGGCAACUUUCACUACGCGCC&name=seq26&top=100"
./mcfold.static.exe >seq26_5bp_267_GCstem_3nt_bulges.data
