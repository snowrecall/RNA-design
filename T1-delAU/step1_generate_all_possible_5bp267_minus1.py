#!/usr/bin/python

seq_list = ['G','G','G','A','A','G','G','G','C','A','A','C','U','U','U','C','A']

for i in range(1,7):
    print 'seq###'
    for j in range(len(seq_list)):
        if j != i and j != (17-i):
            print seq_list[j],
