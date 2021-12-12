#!/usr/bin/python

from itertools import product

#a = ['AU','UA','GC','CG','GU','UG','GG','UU','GA','AG']

a = ['AU','UA','GC','CG','GU','UG']

s = 1

for item in product(a,repeat=4):

        #print list(item)

	print 'G'+list(item)[0][0]+list(item)[1][0]+list(item)[2][0]+list(item)[3][0]+'CUGC'+':'+'seq'+str(s)
	print 'A'+list(item)[0][1]+list(item)[1][1]+list(item)[2][1]+list(item)[3][1]+'G CG'

	s = s + 1
