#!/usr/bin/python

import sys

mcfold_file=sys.argv[1]

file1=open('new_new_considerable_2D_structure.txt')

file2=open(mcfold_file)

save_type_info=[]

for line1 in file1.readlines():
    info1 = line1.split()[0]
    save_type_info.append(info1)

#print save_type_info

for line2 in file2.readlines():
    info2 = line2.split()[0]
    if info2[0]=='>' or info2[0] in ['A','U','C','G']:
        print line2,
    for i in save_type_info:
        if info2==i[-17:]:
            print i[:-17]+line2,
