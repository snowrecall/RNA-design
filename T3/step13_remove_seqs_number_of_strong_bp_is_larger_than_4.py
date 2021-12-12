#!/usr/bin/python
import os

import linecache

import sys

ifile1='29040_different_barcode.out'

pool1 = ['CG','GC','AU','UA','GU','UG']

pool2 = ['CG','GC','AU','UA','GU','UG','GG','UU','GA','AG']

count = len(open(ifile1).readlines())

for i in range(1,(count/2)+1):
    line1 = linecache.getline(ifile1,2*i-1)
    line2 = linecache.getline(ifile1,2*i)

    bp_num1 = 0
    bp_num2 = 0
    for j in range(6):
        bp = line1[j+2]+line2[j+2]
        if bp in pool1:
            bp_num1 = bp_num1 + 1
        if bp in pool2:
            bp_num2 = bp_num2 + 1
    if bp_num2 == 6 and bp_num1 >= 4:
        #line1_new = line1[1:8]
        line2_new = line2[2:10]
        print line2_new+'CA'+line1[7]+line1[6]+line1[5]+line1[4]+line1[3]+line1[2]+line1[1]
