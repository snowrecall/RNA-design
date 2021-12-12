#!/usr/bin/python

import os
import linecache
import sys

ifile1 = '2802_mcfold_input_sequence.txt'

pool1 = ['GC-GU','UA-UG']

pool2 = ['GC-GG','GC-GA','UA-UU']

count = len(open(ifile1).readlines())

for i in range(1,count+1):
    line = linecache.getline(ifile1,i)
    m = 0
    n = 0
    for j in range(1,7)+range(11,17):
        bp_change = line[j]+line[17-j]+'-'+line[j]+line[15-j]
        if bp_change in pool1:
            m = m + 1
        if bp_change in pool2:
            n = n + 1
    if m >= 1 and m + n >= 3:
        print line,
