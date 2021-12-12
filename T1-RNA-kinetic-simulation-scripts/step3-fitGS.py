#!/usr/bin/python

from mplot import *
from openopt import *

#===============================================================================
def expfun(p, X):
    a,k,b = p
    return a*exp(-k*X) + b

#===============================================================================
def expfit(X, Y, p0=None):
    # --------------------------------------------------------------------------
    def chi2(p):
        YS = expfun(p, X)
        return sum((Y-YS)**2)
    # --------------------------------------------------------------------------
    if not p0:
        p0 = [0.5, 10., 0.5]
    nlp = NLP(chi2, p0)
    result = nlp.solve('ralg', iprint=-1)
    return result.xf
#===============================================================================

t,c = loadtxt('T-GS.txt', unpack=True)
# nonlinear fitting
a,k,b = expfit(t, c)
print 'a = ', a
print 'k = ', k
print 'b = ', b
# generate simulated curve
tt = linspace(t[0], t[-1], 1000)
cc = expfun([a,k,b], tt)

plot(tt, cc, 'b-')
plot(t, c, 'ro')

xlim([0, 0.15])
ylim([0, 1.05])

xlabel('t [s]')
ylabel('GS concentration')

show()
