# -*- coding: utf-8 -*-
"""
Created on Wed August 1 17:52 2014

@author: Charles Le Losq
Geophysical Laboratory, Carnegie Institution for Science
clelosq@carnegiescience.edu
lelosq@ipgp.fr

This software is a translation of the pascal routine RAMEAU, associated to 
the publication 

LE LOSQ, NEUVILLE, MORETTI, ROUX, 2012. Determination of water content in 
silicate glasses using Raman spectrometry: implications for the study of explosive volcanism.
American Mineralogist 97, 779-790.

Initial program was written in pascal and is available through the American Mineralogist
website.

This program is a conversion in python, a little bit more "up to date" and
user friendly.

Only initial needs are a python distribution with the 
scipy, numpy, matplotlib, and Tkinter libraries. It may be already installed or
it is easy to find on internet. A good alternative is to use the anaconda
distribution, which is free, and which is perfect for scientific python.
"""

# Import of wrapper for gcvspl.f, wrapper in gcvspl.so and in py function gcvspline.py
import sys
sys.path.append("/Users/charleslelosq/Documents/RamEau/gcvspl/")
import gcvspline

# Import of libraries
import numpy as np
import scipy
from scipy.interpolate import UnivariateSpline
from scipy import interpolate 
from scipy import signal
import matplotlib
import matplotlib.gridspec as gridspec
from pylab import *
from ast import literal_eval

from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
     
#### First thing: we collect the list of spectra

# Collecting the sample spectrum
tkMessageBox.showinfo(
            "Open ",
            "Please open the list of spectra")

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
samplename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# we import the information in an array, skipping the first line
dataliste = np.genfromtxt(samplename,dtype = 'string', skip_header=1,skip_footer=0)

paths = (dataliste[:,0])
sampletype = dataliste[:,1]
H2O = dataliste[:,2]
splinefactor = dataliste[:,3]
BIRS = dataliste[:,4]
 
Rws_H2O = np.zeros((len(BIRS),3)) # In this array we will output the water concentration (if provided), the Rws and its associated error
Rws_H2O[:,0] = H2O

for i in range(len(BIRS)): # We loop over in dataliste
    sample = np.genfromtxt('./dat0/'+paths[i]+'.xy') # we assume here that data are in ./dat0. Use alias or change that
    
    bir = literal_eval(BIRS[i]) # the BIRs
    samplecorr = np.zeros((len(sample[:,0]),5))
    
    for numbir in range(len(bir)): # we individualize the fractions of signals use as BIRS
        if numbir == 0:
            yafit = sample[np.where((sample[:,0]> bir[numbir][0]) & (sample[:,0] < bir[numbir][1]))] 
        else:
            je = sample[np.where((sample[:,0]> bir[numbir][0]) & (sample[:,0] < bir[numbir][1]))]
            yafit = np.concatenate((yafit,je),axis=0)
         
    # gcvspl spline
    xdata = yafit[:,0]
    ydata = np.zeros((len(xdata),1))
    ydata[:,0] = yafit[:,1]
    #ese = yafit[:,2]
    ese = sqrt(yafit[:,1])
    f = np.fromstring(splinefactor[i], dtype = float, sep = ' ')
    VAL = ese**2    
    
    # Spline baseline with mode 3 of gcvspl.f
    c, wk, ier = gcvspline.gcvspline(xdata,ydata,f*ese,VAL,splmode = 3) # we get the spline calues
     
    samplecorr[:,0] = sample[:,0]
    samplecorr[:,1] = sample[:,1]    
    samplecorr[:,2] = gcvspline.splderivative(samplecorr[:,0],xdata,c)
    samplecorr[:,3] = sample[:,1] - samplecorr[:,2]
    
    #### Area calculation
    silicate =  samplecorr[np.where((samplecorr[:,0]> 20) & (samplecorr[:,0] < 1500))]
    eau =  samplecorr[np.where((samplecorr[:,0]> 3000) & (samplecorr[:,0] < 4000))]

    asili = np.trapz(silicate[:,3],silicate[:,0])
    aeau = np.trapz(eau[:,3],eau[:,0])
    
    eseairesili = 1/np.sqrt(asili) # relative areeas
    eseaireeau = 1/np.sqrt(aeau) # relative areas

    Rws_H2O[i,1] = aeau/asili
    Rws_H2O[i,2] = eseairesili/asili + eseaireeau/aeau

    # we normalize the spectra a little bit differently from 2012: total area = 100

    samplecorr[:,3] = samplecorr[:,3]/(asili+aeau)*100
    samplecorr[:,4] = sample[:,2]/sample[:,1]*samplecorr[:,3]

    figure()
    gs = matplotlib.gridspec.GridSpec(1, 2)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax1.plot(samplecorr[:,0],samplecorr[:,1],'k-')
    ax1.plot(samplecorr[:,0],samplecorr[:,2],'r-')
    ax2.plot(samplecorr[:,0],samplecorr[:,3],'r-')
    ax1.set_title(paths[i])

    np.savetxt(('./corrspectra/'+paths[i]+'.txt'),samplecorr)
    savefig(('./plots/'+paths[i]+'.pdf'))    
    
### General output of dtat
np.savetxt(('output.txt'),Rws_H2O)
figure()
errorbar(Rws_H2O[:,0],Rws_H2O[:,1],yerr=Rws_H2O[:,2],fmt='bo')
xlabel('Water concentration, wt%')
ylabel('Rws')
savefig('RatioAndWater.pdf')
