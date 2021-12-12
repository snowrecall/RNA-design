#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACAGGAAGGGCAACUUUCACCACGCGCC&name=seq32&top=100"
./mcfold.static.exe >seq32_5bp_267_GCstem_3nt_bulges.data
