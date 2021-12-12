#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GGCGCGCACGGAAGGGCAACUUUCACAUCGCGCC&name=seq150&top=100"
./mcfold.static.exe >seq150_5bp_267_GCstem_3nt_bulges.data
