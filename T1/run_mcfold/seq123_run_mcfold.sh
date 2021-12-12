#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCUUGGAAGGGCAACUUUCACCACGCGCC&name=seq123&top=100"
./mcfold.static.exe >seq123_5bp_267_GCstem_3nt_bulges.data
