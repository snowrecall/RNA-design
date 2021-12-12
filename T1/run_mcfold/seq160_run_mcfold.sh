#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCUCGGAAGGGCAACUUUCAACUCGCGCC&name=seq160&top=100"
./mcfold.static.exe >seq160_5bp_267_GCstem_3nt_bulges.data
