#!/usr/bin/python

import os

import linecache

import sys

ifile1='31104_like_p5c_groud_state.txt'

count = len(open(ifile1).readlines())

for i in range(1,(count/2)+1):
    line1 = linecache.getline(ifile1,2*i-1)
    line2 = linecache.getline(ifile1,2*i)
    m=2
    n=2
    barcode_pool=[]
    for j in range(5):
        barcode_cis=line2[m]+line1[n]+'-'+line2[m-1]+line1[n-1]+'-'+line2[m+1].rstrip('\n')+line1[n+1].rstrip(':')
        barcode_pool.append(barcode_cis)
        m += 1
        n += 1
    p=6
    q=6
    for s in range(5):
        barcode_trans=line1[p]+line2[q]+'-'+line1[p+1]+line2[q+1]+'-'+line1[q-1]+line2[q-1]
        barcode_pool.append(barcode_trans)
        p -= 1
        q -= 1
    barcode_pool_new=set(barcode_pool)
    if len(barcode_pool_new) == 10:
#        print barcode_pool_new
        print line1,
        print '  '+line2,
