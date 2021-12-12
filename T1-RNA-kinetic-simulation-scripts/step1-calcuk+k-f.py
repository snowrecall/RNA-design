#!/usr/bin/python

import math
import numpy as np 

k = 1
# J/K
kB = 1.3806505*(10**(-23))  
# K
T = 273+10
#J*s
h = 6.62607015*(10**(-34))

cons = float(k*kB*T)/(h)

#print cons

#######

#kcal/mol 
Ga = [12.045,11.045,11.045,11.045,10.775] 
Gb = [9.145,11.045,11.045,11.045,12.045]

#kcal/(K*mol)

R = 1.987*(10**(-3))

for i in range(0,5):
    ka = cons * np.e**(-Ga[i]/float(R*T))
    #ka = cons * np.e**(-Ga/float(R*T))
    print 'ka = ', ka
    kb = cons * np.e**(-Gb[i]/float(R*T))
    #kb = np.e**(-Gb/float(R*T))
    print 'kb = ', kb
