#!/usr/bin/python

from collections import defaultdict

from mplot import *

ifile=open('step2_3.out')

dict1=defaultdict(list)

for line in ifile.readlines():

	word=line.split(' ')

	st = word[0]

	energy_info = word[1].strip('\n')

	try:

		dict1[st].append(energy_info)

	except KeyError:

		dict1[st]=energy_info

for i in dict1:

	#print i,dict1[i]
    total=0
    num = 0
    for deltaG in dict1[i]:
        total+=float(deltaG)
        num+=1
    ave=total/num
    
    s=0
    for deltaG in dict1[i]:
        s+=(float(deltaG)-ave)**2

    delta=sqrt(s/num)

    print i,"mean= %.3f"%ave,"delta= %.3f"%delta,"number= %d"%num
