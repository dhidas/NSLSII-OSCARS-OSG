#!/bin/bash
MYDIR=$PWD
OUTDIR=$1
mkdir -pv $OUTDIR/NSLSII-OSCARS-OSG/SST/U42

./NSLSII-OSCARS-OSG/SST/U42/osg_tgz_files.sh

cp SST_U42_osg.tgz $OUTDIR
cp NSLSII-OSCARS-OSG/SST/U42/osg_run_Spectrum.sh $OUTDIR/NSLSII-OSCARS-OSG/SST/U42/
cp NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor   $OUTDIR/NSLSII-OSCARS-OSG/SST/U42/
cd $OUTDIR

condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=11.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=12.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=12.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=13.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=13.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=14.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=14.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=15.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=15.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=16.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=16.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=17.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=17.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=18.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=18.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=19.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=19.5
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=20.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=21.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=22.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=23.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=24.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=25.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=26.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=27.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=28.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=29.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=30.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=31.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=32.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=33.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=34.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=35.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=36.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=37.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=38.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=39.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=40.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=45.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=50.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=55.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=60.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=65.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=70.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=75.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=80.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=85.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=90.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=95.0
condor_submit NSLSII-OSCARS-OSG/SST/U42/osg_submit.condor -append GAP=100.0
