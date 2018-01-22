#!/bin/bash

NAME=$1
GAP=$2
MODE=$3
PHASE=$4
Cluster=$5
Process=$6

echo $PWD


tar zxf SST_EPU60_osg.tgz


# Load same modules you used to compile oscars
module load gcc/4.9.2
module load python/3.5.2

python3 NSLSII-OSCARS-OSG/SST/EPU60/Spectrum_OSG.py $NAME $GAP $MODE $PHASE $Process

tar zcf $(NAME)_$(Cluster).$(Process).tgz $(NAME)_*
