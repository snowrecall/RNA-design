#!/usr/bin/python

from common.base import partition

lines = open('all_the_788_seq_have_the_2d_types_deltaG_form.txt').readlines()
lines = map(lambda x: x.strip(),lines)
blks = partition(lines,lambda x:x[0] == '>',include = 'header')

for blk in blks:
    if len(blk)==4 and blk[2][:5]=='Type1' and blk[3][:5]=='Type3':
        print blk
