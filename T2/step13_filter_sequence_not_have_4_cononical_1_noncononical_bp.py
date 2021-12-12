#!/usr/bin/python

import os
import linecache
import sys

ifile1 = '7776_different_barcode.out'

pool1 = ['CG','GC','AU','UA','GU','UG']

pool2 = ['GG','UU','GA','AG']

count = len(open(ifile1).readlines())

for i in range(1,(count/2)+1):
    line1 = linecache.getline(ifile1,2*i-1)
    line2 = linecache.getline(ifile1,2*i)

    bp_num1 = 0
    bp_num2 = 0
    for j in range(5):
        bp = line1[j]+line2[j]
        if bp in pool1:
            bp_num1 = bp_num1 + 1
        if bp in pool2:
            bp_num2 = bp_num2 + 1

    if (bp_num1 == 4 and bp_num2 == 1) or (bp_num1 == 5):
        line2_new = str(line2).rstrip('\n')
        print line2_new+'GCAA'+line1[5]+line1[4]+line1[3]+line1[2]+line1[1]+line1[0]
