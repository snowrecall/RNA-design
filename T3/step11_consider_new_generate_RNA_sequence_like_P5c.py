#!/usr/bin/python

from itertools import product

#a = ['AU','UA','GC','CG','GU','UG','GG','UU','GA','AG']

a = ['AU','UA','GC','CG','GU','UG']

b = ['A','U','G','C']

s = 1

###pay attention, the first line is 3' terminal sequence, the second line is 5' terminal sequence.

for base in b:
    for item in product(a,repeat=5):
        print ' '+'A'+list(item)[0][0]+list(item)[1][0]+list(item)[2][0]+list(item)[3][0]+list(item)[4][0]+'A'+':'+'seq'+str(s)
        print str(base)+'G'+list(item)[0][1]+list(item)[1][1]+list(item)[2][1]+list(item)[3][1]+list(item)[4][1]+'G'
        s = s + 1
