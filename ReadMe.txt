########## Rameau V2.0 ########
This software is a python version of the Rameau software published as a supplementary material of the article
Le Losq, Neuville, Moretti, Roux, 2012. Determination of water content in silicate glasses using Raman spectrometry: Implications for the study of explosive volcanism. American Mineralogist 97, 779-790.

The Rameau Pascal/fortran initial software is available on the american mineralogist website...

Dependence are : Python, Numpy, Scipy, gfortran, f2py

We use the gcvspl.f code available on the netlib, and wrapped with f2py. Actually its a f77 version that is in the ./gcvspl/ folder, that of the netlib is a little bit impossible to wrap out of the box... Modifications (insertion of wrapping cf2py intent functions) have been made in the initial fortran code to do a "good" wrapping...

If you need to adapt this code to your own problem, please go inside the python code, change those values, do whatever you want, this is software is under GNU GPL2 licence, so you just have to cite the article if you use that and you can modify it as you want. It's simple, but please do not forget to cite the initial work, it's the spirit of the GNU world that provides thousands of great free softwares... 

And if you have improvements, please report them to me :)

C. Le Losq.
clelosq@carnegiescience.edu

###########

Installation instruction:

1) please check that you python/numpy/scipy distrubition is fully functional and not problems with the paths should exist. Also please set up your .bash_profile file accordingly, indicating the $PATH variable....

2) If not already done, install last version of gfortran

3) copy the global directory, use a terminal, go into the gcvspl folder, and do:

f2py -c -m gcvspl gcvspl.f

4) WARNING: in the Rameau.py line 31, change the path in sys.path.append("/Users/charleslelosq/Documents/RamEau/gcvspl/")... Obviously it should point to the path of ./RamEau/gcvspl/ in your system, not mine...

4) launch the Rameau.py script... should work out of the box now

###########

How to use the software...

YOU SHOULD KEEP THE STRUCTURE OF THE REPERTORY INTACT ! 

WARNING: CLEANING IS MANUAL HERE. After using the software, you should move or delete (if you want of course!) the content of the ./corrspectra and ./plots folders, as well as the output.txt and RatioAndWater.pdf files...

WARNING: IN THIS VERSION WE ASSUME ESE = SQRT(Y) FOR BASELINE FITTING, WE DO NOT READ THE ESE COLUMN OF INPUT FILES....... SHOULD BE CHANGED IN NEXT FUTUR BUT WORK QUITE WELL ACTUALLY...

table.txt contains the list of spectra name, type, wt% H2O, spline factor and the background interpolation regions BIRs (see publication)

if you don't know the water concentrations put them at 0 in the table.txt file

table.txt is supposed to be in the same location as the spectra

you should modify table.txt. Spectra can or cannot be corrected from long. We performed long correction for the 2012 publication, it works quite well, but for some problems (ad hoc calibration) you might want to work without this correction...

The software will call the fortran wrapper, then gives to it the BIRs, and the wrapper returns the baseline...

Each spectrum is saved in the ./corrspectra folder as x, y, baseline, ycorrected, eseycorrected

A pdf of each spectrum is saved in the ./plots folder

Areas are calculated between 20 to 1500 and 3000 to 4000 cm-1.

water concentration (if provided, if not 0...), Rws and eseRws are provided in output.txt.

###########
TO BE DONE:

An improved version will implement functions that allows users to save figures, output spectra and global output table where they want.

Improvements of plots, etc...
