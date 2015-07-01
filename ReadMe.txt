########## Rameau V2.0 ########
This software is a python version of the Rameau software published as a supplementary material of the article
Le Losq, Neuville, Moretti, Roux, 2012. Determination of water content in silicate glasses using Raman spectrometry: Implications for the study of explosive volcanism. American Mineralogist 97, 779-790.

The Rameau Pascal/fortran initial software is available through the american mineralogist website.

Dependence are : Python, Numpy, Scipy, gfortran, f2py

We use the gcvspl.f code available on the netlib, and wrapped with f2py. Actually its a f77 version that is in the ./gcvspl/ folder, that of the netlib is a little bit impossible to wrap out of the box... Modifications (insertion of wrapping cf2py intent functions) have been made in the initial fortran code to do a "good" wrapping...

If you need to adapt this code to your own problem, please go inside the python code, change those values, do whatever you want, this is software is under GNU GPL2 licence, so you just have to cite the article if you use that and you can modify it as you want. It's simple, but please do not forget to cite the initial work, it's the spirit of the GNU world that provides thousands of great free softwares... 

And if you have improvements, please report them to me, you can also directly contribute in the Github repository if you want (thanks in advance if you do so!).

C. Le Losq.
clelosq@carnegiescience.edu

###########

Installation instruction:

1) please check that you python/numpy/scipy distribution is fully functional and no problems with the paths should exist. Also please set up your .bash_profile file accordingly, indicating the $PATH variable....

2) If not already done, install last version of gfortran

3) copy the global directory, use a terminal, go into the gcvspl folder in the Rameau main directory, and do:

f2py -c -m gcvspl gcvspl.f

4) launch the Rameau.py script... should work out of the box now

###########

HOW TO USE THE SOFTWARE

There is several folders, YOU SHOULD KEEP THE STRUCTURE OF THE REPERTORY INTACT unless you know what you're doing. This also goes for the name of the dataliste files. You can modify the Rameau.py and LongCorrection.py scripts to provide different paths/input files.

For now, data are in the folder data/raw and data/longcorr for raw spectra and spectra corrected from long, respectively.

The software Rameau.py will automatically search the spectra to correct from baseline in the data/longcorr/ folder. You can modify that line 68 in the Rameau.py script if you need.

The software LongCorrection.py will automatically search the spectra in the data/raw/ folder. Same comment as above.

I added a Makefile to make things faster. Three commands: clean, long, and run (with all to run the three). So you can type: make clean, make long, and make run; This first cleans the corrspectra and plots folders and erases the RatioAndWater.pdf and output.txt files, and after runs the LongCorrection.py and Rameau.py scripts, respectively.

Or you can do it manually. You can run the scripts using python LongCorrection.py and python Rameau.py in a terminal. You have to go into the Rameau folder before, of course.

WARNING: IN THIS VERSION WE ASSUME ESE = SQRT(Y) FOR BASELINE FITTING, WE DO NOT READ THE ESE COLUMN OF INPUT FILES....... SHOULD BE CHANGED IN NEXT FUTUR BUT WORK QUITE WELL ACTUALLY...

Anyway, the ese are only used for the smoothing factor before entry into the gcvspl fortran code. You can read the fortran code for further details.

dataliste_baseline.txt contains the list of spectra name, type, wt% H2O, spline factor and the background interpolation regions BIRs (see publication). This file is the input to the Rameau.py script.

dataliste_longcorr contains the list of spectra name, the temperature and the wavelengths at which they have been acquirred. This file is the input of the LongCorrection.py script.

###########

OUTPUTS and RUNNING NOTES:

The Rameau.py software will call the fortran wrapper, then gives to it the BIRs, and the wrapper returns the baseline...

Each spectrum is saved in the ./corrspectra folder as x, y, baseline, ycorrected, eseycorrected.

A pdf of each spectrum is saved in the ./plots folder.

Areas are calculated between 20 to 1500 and 3000 to 4000 cm-1.

water concentration (if provided, if not 0...), Rws and eseRws are provided in output.txt.

###########

UPDATE NOTE FOR WATER DETERMINATION

=> If you don't know the water concentrations put them at 0 in the table.txt file.

=> Spectra can or cannot be corrected from long. We performed long correction for the 2012 publication, it works quite well, but for some problems (ad hoc calibration) you might want to work without this correction... We did that at the Geophysical Laboratory, as explained in Le Losq, Cody and Mysen, 2015, American Mineralogist 100, 466-473 (see supplementary materials).

###########
TO BE DONE:

An improved version will implement functions that allows users to save figures, output spectra and global output table where they want.

Improvements of plots, etc...
