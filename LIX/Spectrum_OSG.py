# This is meant to be run on OSG or similar condor-type systems

# Command line arguments are given by condor at runtime
import sys
sys.path.append('.')

# import oscars
import oscars.sr
from oscars.util import *

# Get process number and gap from input
NAME = sys.argv[1]
GAP = float(sys.argv[2])
Process = sys.argv[3]

# Name of the output file
out_file_name = NAME + '_g' + str(GAP) + '_' + Process + '.dat'
print(out_file_name)

# Create oscars.sr object
osr = oscars.sr.sr()

# Set nthreads to 1 for OSG use
osr.set_nthreads_global(1)

# Setup nsls2 long straight beam parameters
osr.set_particle_beam(beam='NSLSII-LongStraight', name='beam', x0=[0, 0, -1.5])

# Set start and stop time for calculation
osr.set_ctstartstop(0, 3)

# Input file list
file_list = read_file_list('NSLSII-MM-Data/LIX/file_list.txt')

# Add bfield for this gap according to the file list
osr.clear_bfields()
osr.add_bfield_interpolated(mapping=file_list,
                            iformat='OSCARS1D Z Bx By Bz',
                            parameter=GAP,
                            scale=[0.001],
                            name='undulator'
                           )

# Number of particles per node of rank > 1
particles_per_node = 1000

# Observation point for spectrum
observation_point = [0, 0, 30]

# Energy range for spectrum
range_eV = [100, 20000]

# Number of points in the spectrum
npoints = int((range_eV[1]-range_eV[0])/2.)

# Ideal single-particle data 
if int(Process) == 0:
    osr.set_new_particle(particle='ideal')
    spectrum = osr.calculate_spectrum(obs=observation_point,
                                      energy_range_eV=range_eV,
                                      npoints=npoints,
                                      ofile=out_file_name)

# Multi-particle simulation
else:
    spectrum = osr.calculate_spectrum(obs=observation_point,
                                      energy_range_eV=range_eV,
                                      npoints=npoints,
                                      nparticles=particles_per_node,
                                      ofile=out_file_name)

