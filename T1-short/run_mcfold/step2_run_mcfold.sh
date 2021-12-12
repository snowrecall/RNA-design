#!/bin/bash

count=0

cat mcfold_input_sequence_head_add_G_tail_add_A.txt | while read line

#cat test | while read line

do

let count=count+1

echo '#!/bin/csh' >seq${count}_run_mcfold.sh

echo "setenv QUERY_STRING pass=lucy&sequence=${line}&name=seq${count}&top=100" >>seq${count}_run_mcfold.sh

echo "./mcfold.static.exe >seq${count}_P5c.data" >>seq${count}_run_mcfold.sh

chmod 771 seq${count}_run_mcfold.sh

sed -ig 's/pass/"pass/g' seq${count}_run_mcfold.sh

sed -ig 's/100/100"/g' seq${count}_run_mcfold.sh

./seq${count}_run_mcfold.sh

done

rm seq*_run_mcfold.shg
