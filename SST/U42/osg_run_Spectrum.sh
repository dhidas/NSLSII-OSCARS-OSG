#!/bin/bash

NAME=$1
GAP=$2
Cluster=$3
Process=$4

echo $PWD


tar zxf SST_U42_osg.tgz


# Load same modules you used to compile oscars
module load gcc/4.9.2
module load python/3.5.2
module load all-pkgs

python3 NSLSII-OSCARS-OSG/SST/U42/Spectrum_OSG.py $NAME $GAP $Process

ls -a

tar zcf ${NAME}_${Cluster}.${Process}.tgz ${NAME}_*
