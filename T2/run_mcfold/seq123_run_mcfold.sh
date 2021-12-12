#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GUUUGGGCAACCGGAA&name=seq123&top=100"
./mcfold.static.exe >seq123_p5clike_opposite_direction.data
