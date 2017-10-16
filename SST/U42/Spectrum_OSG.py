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
Process = sys.argv[5]

out_file_name = NAME + '_g' + str(GAP) '_' + Process + '.dat'

osr = oscars.sr.sr(gpu=0, nthreads=1)

osr.set_particle_beam(beam='NSLSII-ShortStraight', x0=[0, 0, -2.5])
osr.set_ctstartstop(0, 2.5)


file_list = read_file_list('NSLSII-MM-Data/U42/file_list.txt')


osr.add_bfield_interpolated(
    file_list,
    iformat='OSCARS1D Z Bx By Bz',
    scale=[0.001],
    parameter=gap,
    translation=[0, 0, -1.250]
)
osr.add_bfield_gaussian(bfield=[0, +1.5e-4, 0], sigma=[0, 0, 0.050], translation=[0, 0, -2.3])


if int(Process) == 0:
    osr.set_new_particle(particle='ideal')
    osr.calculate_spectrum(
        obs=[0, 0, 17-1.250],
        energy_range_eV=[10, 10000],
        ofile=out_file_name,
    )
else:
    osr.calculate_spectrum(
        obs=[0, 0, 17-1.250],
        energy_range_eV=[10, 10000],
        nparticles=3
        ofile=out_file_name,
    )
