# NSLSII-OSCARS-OSG

This repository is for Open Science Grid configuration files and OSCARS python scripts for calculating spectra, flux, etc using OSG.  These are the scripts that I use for calculations.  They are provided as examples and one should know that modification for their use is required.  Paths, data files, beamlines, etc must be customized for your own use case.  The instructions below are largely reminders to myself, but can serve as a guide for your own use.

These scripts require an accompanying directory containing magnetic measurement data for a given beamline:
NSLSII-MM-Data

In order to run on OSG I recommend the following (for OSG only):
```
# Load the desired modules
module load gcc/4.9.2
module load python/3.5.2

# Clone oscars (whiever version you like)
git clone https://github.com/dhidas/OSCARS.git
cd OSCARS

# Compile OSCARS locally
python3 setup.py build_ext --inplace

# Clone this repo
git clone https://github.com/dhidas/NSLSII-OSCARS-OSG.git

# Copy magnetic data to NSLSII-MM-Data folder in this dir
scp -r user@host.com:~/NSLSII-MM-Data .

# gzip files for submission, for examples
./NSLSII-OSCARS-OSG/LIX/osg_tgz.sh

# Submit to OSG (check file first for parameters, and +ProjectName is correct)
condor_submit NSLSII-OSCARS-OSG/LIX/osg_submit.condor

# OR submit "all" using something like
./NSLSII-OSCARS-OSG/LIX/submit_all.sh

# You must make sure the paths to data files is correct!!
```

