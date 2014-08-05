# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 16:50:59 2014

@author: charleslelosq
"""

import sys
sys.path.append("/Users/charleslelosq/Documents/RamEau/gcvspl/")
import gcvspline
#import gcvspl
import gcvspl

import numpy as np
from matplotlib import *
from pylab import *
    
x1 = np.arange(0,1000,1) # 1D input x
y1 = np.zeros((len(x1),1)) # 2D array input y
y1[:,0] = 10*np.exp(-np.log(2)*((x1[:]-500)/200)**2)
ese1 = np.sqrt(np.abs(y1[:,0])) # ERRORS ON Y
x2 = np.arange(1500,2000,1) # 1D input x
y2 = np.zeros((len(x2),1)) # 2D array input y
y2[:,0] = 10*np.exp(-np.log(2)*((x2[:]-1700)/100)**2)

ese2 = np.sqrt(np.abs(y2[:,0])) # ERRORS ON Y

x = np.concatenate((x1,x2))
y = np.concatenate((y1,y2))
ese = np.concatenate((ese1,ese2))
f=100
rvar = 1/(f*ese)**2
xcalc = np.arange(0,2000,1)

wx = rvar # relative variance of observations
wy = np.zeros((1))+1 # systematic errors... not used so put them to 1

splorder = 2
splmode = 3
NC = len(y)
VAL = ese**2

#c, wk, ier = gcvspl.gcvspl(x,y,wx,wy,splorder,splmode,VAL,NC)

c, wk, ier = gcvspline.gcvspline(x,y,100*ese,VAL,splmode=3)

#L = 1
#IDER = 0
#q = np.zeros((2*splorder))  # working array
#ycalc = np.zeros((len(xcalc))) # Output array
#
## we loop other xfull to create the output values
#for i in range(len(xcalc)):
#    ycalc[i] = gcvspl.splder(IDER,splorder,xcalc[i],x,y,L)
    
plot(x,y,'k.')
#plot(xcalc,ycalc,'r-')
plot(x,c,'g-')