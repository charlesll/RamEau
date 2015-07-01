# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:51:27 2015

@author: Charles Le Losq
Geophysical Laboratory, Carnegie Institution for Science
clelosq@carnegiescience.edu
charles.lelosq@gmail.com

This is just a quick script in case you need to perform the long correction.
Please put your files in the folder long, then put a "datalist.txt" file with 
their name (ae099.txt for instance), the temperature and the laser wavelength 
you used.

See provided example
You can run this script by typing in a command line window
python LonCorrection.py
"""
import sys
import os
print("The current working directory is: "+os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/gcvspl/")

from longcorr import *

# Import of libraries
import numpy as np
import scipy
from pylab import *

# we import the information in an array, skipping the first line
dataliste = np.genfromtxt("./data/dataliste_longcorr.txt",dtype = 'string', skip_header=1)

paths = (dataliste[:,0])
temperature = dataliste[:,1]
laserwavelength = dataliste[:,2]

print("\nDataliste successfully imported. ")
for i in range(len(temperature)): # We loop over in dataliste

    print("\nNow Fitting the spline under the file "+paths[i])
    #we import the file    
    sample = np.genfromtxt('./data/raw/'+paths[i],dtype = 'float') # we assume here that data are in ./dat0. Use alias or change that
    
    #Checking if their is nan values somewhere, and putting them to 0
    if np.isnan(sample).any():
        print("\nWarning you have nan or infinite values in the file "+paths[i]+'. We put them to 0 but please check this spectrum')
        sample = np.nan_to_num(sample)
    
    spectrecorr = longcorr(sample,float(temperature[i]),float(laserwavelength[i])) #and then we do the long correction
    np.savetxt(('./data/longcorr/'+paths[i]),spectrecorr)
    
print("Done. Now you can use either the raw files or the long corrected files")
 