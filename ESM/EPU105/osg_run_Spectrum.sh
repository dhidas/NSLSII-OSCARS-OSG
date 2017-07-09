#!/bin/bash

NAME=$1
GAP=$2
PHASEMODE=$3
PHASE=$4
Process=$5

echo $PWD


tar zxf ESM_EPU105_osg.tgz


# Load same modules you used to compile oscars
module load gcc/4.9.2
module load python/3.5.2

python3 NSLSII-OSCARS-OSG/ESM/EPU105/Spectrum_OSG.py $NAME $GAP $PHASEMODE $PHASE $Process
