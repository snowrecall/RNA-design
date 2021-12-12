#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGACCGGAAGGGCAACUUUCAAUACGCGCC&name=seq28&top=100"
./mcfold.static.exe >seq28_5bp_267_GCstem_3nt_bulges.data
