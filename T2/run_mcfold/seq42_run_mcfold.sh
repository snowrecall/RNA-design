#!/bin/csh
setenv QUERY_STRING "pass=lucy&sequence=GUUGAGGCAAUUUAAA&name=seq42&top=100"
./mcfold.static.exe >seq42_p5clike_opposite_direction.data
