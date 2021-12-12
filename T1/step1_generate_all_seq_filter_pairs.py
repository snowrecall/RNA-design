#!/usr/bin/python

from itertools import product

a=['AA','AC','UC','CA','CU','CC']

for item in product(a,repeat=3):
    print 'GGCGCG'+list(item)[0][0]+list(item)[1][0]+list(item)[2][0]+'GGAAGGGCAACUUUCA'+list(item)[2][1]+list(item)[1][1]+list(item)[0][1]+'CGCGCC'
