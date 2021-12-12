#!/usr/bin/python

def get_barcode(s):
    barcode = []
    for i in range(2,9)+range(13,20):
        barcode.append(s[i]+s[21-i]+'-'+s[i-1]+s[22-i]+'-'+s[i+1]+s[20-i])
    return barcode


seq = open('5bp267_add2bp_all_possible.txt').readlines()

s = 1

for i in range(len(seq)):
    seq1 = seq[i].strip()
    barcode = get_barcode(seq1)
    if len(set(barcode)) == 14:
        print seq[i],
        print barcode
    s += 1
