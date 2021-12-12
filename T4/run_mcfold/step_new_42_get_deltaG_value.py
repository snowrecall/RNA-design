#!/usr/bin/python

import os
import linecache
import sys

filename = sys.argv[1]

lines = open(filename).readlines()

print lines[0],
print lines[1],

for i in range(2,len(lines)):
    words = lines[i].split()
    if words[0] == '((((((.(((..)))))))))':
        deltaG = 0
        print words[0]+' '+str(deltaG)+' '+'Type0'
    if words[0] == '.(((((((((..)))))))))':
        deltaG = float(words[1]) - float(lines[2].split()[1])
        print words[0]+' '+str(deltaG)+' '+'Type1'
