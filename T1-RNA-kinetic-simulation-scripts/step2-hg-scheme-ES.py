#!/usr/bin/python

from mplot import *
from numpy import *
from openopt import *
import matplotlib.pyplot as plt

#===============================================================================
def expfun1(p,X):
    a,R = p
    return a*(1.0-exp(-R*X))

#===============================================================================
def expfit1(X, Y, p0):
    #---------------------------------------------------------------------------
    def chi2(p):
        YS = expfun1(p,X)
        return sum((Y-YS)**2)

    nlp=NLP(chi2,p0)
    result = nlp.solve('ralg', iprint=-1)
    return result.xf    
#===============================================================================
def expfun2(p,X):
    a,b,R = p
    return b+a*exp(-R*X)
#===============================================================================
def expfit2(X, Y, p0):
    #---------------------------------------------------------------------------
    def chi2(p):
        YS = expfun2(p,X)
        return sum((Y-YS)**2)
    #---------------------------------------------------------------------------
    nlp = NLP(chi2, p0)
    result = nlp.solve('ralg',iprint=-1)
    return result.xf

#===============================================================================
p0 = 1.
p1 = 0.
p2 = 0.
p3 = 0.
p4 = 0.
p5 = 0.
######
k1 = 2937.38818669 
k_1 = 510156.481326
k2 =  17389.4639186
k_2 = 17389.4639186
k3 = 17389.4639186
k_3 = 17389.4639186
k4 = 17389.4639186
k_4 = 17389.4639186
k5 = 28106.9617899
k_5 = 2937.38818669
#k1 = 0.523
#k_1 = 1.815
#k2 = 18.322
#k_2 = 220.917
#k3 = 18.322
#k_3 = 37.317
#k4 = 129.578
#k_4 = 31.237
#k5 = 0.625
#k_5 = 0.551


C0 = array([p0,p1,p2,p3,p4,p5])
K = array([
  [-k1,    k_1,      0,      0,      0,      0],
  [k1 ,-k_1-k2,    k_2,      0,      0,      0],
  [0  ,     k2,-k_2-k3,    k_3,      0,      0],
  [0  ,      0,     k3,-k_3-k4,    k_4,      0],
  [0  ,      0,      0,     k4,-k_4-k5,    k_5],
  [0  ,      0,      0,      0,     k5,   -k_5]])


w,M = linalg.eig(K)
M_1 = linalg.inv(M)
#print 'w = ', w

T = linspace(0, 0.25, 1000.)
GS = zeros(T.shape)
I1 = zeros(T.shape)
I2 = zeros(T.shape)
I3 = zeros(T.shape)
I4 = zeros(T.shape)
ES = zeros(T.shape)

for i,t in enumerate(T):
    A = dot(dot(M,diag(exp(w*t))),M_1)
    GS[i] = dot(A[0,:], C0)
    I1[i] = dot(A[1,:], C0)
    I2[i] = dot(A[2,:], C0)
    I3[i] = dot(A[3,:], C0)
    I4[i] = dot(A[4,:], C0)
    #I5[i] = dot(A[5,:], C0)
    ES[i] = dot(A[5,:], C0)

# get kobs
#a0,b0,R0 = expfit2(T, GS, [0.5,0.5,w[0]])
#print a0,b0,R0  
a0,b0,R0 = expfit2(T, GS, [0.5,0.5,6.])
GSG = expfun2([a0,b0,R0],T)
plot(T,GS,'mo')

#for i in range(len(T)):
#    print T[i],GS[i]
#print 'kobs = R(GS) =', R0


a1,b1,R1 = expfit2(T, I1, [0.5,0.5,6.])
I1I = expfun2([a1,b1,R1],T)
plot(T,I1,'yo')
#print 'kobs = R(I1) =', R1


a2,b2,R2 = expfit2(T, I2, [0.5,0.5,6.])
I2I = expfun2([a2,b2,R2],T)
plot(T,I2,'co')
#print 'kobs = R(I2) =', R2


a3,b3,R3 = expfit2(T, I3, [0.5,0.5,6.])
I3I = expfun2([a3,b3,R3],T)
plot(T,I3,'go')
#print 'kobs = R(I3) =', R3


a4,b4,R4 = expfit2(T, I4, [0.5,0.5, 6.])
I4I = expfun2([a4,b4,R4],T)
plot(T,I4,'bo')
#print 'kobs = R(I4) =', R4

# draw pic

# fit [ES](t)
#a5,R5 = expfit1(T, ES, [0.5, w[5]])
a5,R5 = expfit1(T, ES, [0.5, 6.])
ESE = expfun1([a5,R5],T)
plot(T, ES, 'ro')

for j in range(len(T)):
    print T[j],ES[j] 


#######
plot(T,GSG,'m-',lw=2)
plot(T,I1I,'y-',lw=2)
plot(T,I2I,'c-',lw=2)
plot(T,I3I,'g-',lw=2)
plot(T,I4I,'b-',lw=2)
plot(T,ESE, 'r-',lw=2)
xlabel('t [s]', fontsize=18)
ylabel('species concentration', fontsize=18)

plt.legend(['GS','I1','I2','I3','I4','ES'],loc='lower left',ncol=3)
plt.title('scheme2')
show()


