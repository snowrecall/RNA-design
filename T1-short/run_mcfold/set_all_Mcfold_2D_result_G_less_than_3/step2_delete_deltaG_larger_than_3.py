#!/usr/bin/python

import sys

import linecache

ifile = sys.argv[1]

file=open(ifile)

save_energy=[]

for line in file.readlines()[2:]:

	word=line.split()

	save_energy.append(word[1])

for i in range(len(save_energy)):

    dG = float(save_energy[i])-float(save_energy[0])    
    
    if float(save_energy[i])-float(save_energy[0])<=3:

		line1 = linecache.getline(ifile,i+3)

		print line1.split()[0],dG
	
