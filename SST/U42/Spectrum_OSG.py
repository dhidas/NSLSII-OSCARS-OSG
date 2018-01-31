# This is meant to be run on OSG or similar condor-type systems

# Command line arguments are given by condor at runtime
import sys
sys.path.append('.')

# import oscars
import oscars.sr
from oscars.util import *
from oscars.fit import *

from math import sqrt

# Get process number and gap from input
NAME = sys.argv[1]
GAP = float(sys.argv[2])
Process = sys.argv[3]

# Constants
IDOFFSET = -1.250
OBS = 30 + IDOFFSET
ESTART = 250
ESTOP = 9000

out_file_name = '{}_gap_{:07.3f}_{:04.0f}.dat'.format(NAME, GAP, int(Process))

osr = oscars.sr.sr(gpu=0, nthreads=10)


osr.set_particle_beam(beam='NSLSII-ShortStraight', x0=[0, 0, -2.5])
osr.set_ctstartstop(0, 2.5)


file_list = read_file_list('NSLSII-MM-Data/SST/U42/file_list.txt')


osr.clear_bfields()
osr.add_bfield_interpolated(
    file_list,
    iformat='OSCARS1D Z Bx By Bz',
    scale=[0.001],
    parameter=GAP,
    translation=[0, 0, IDOFFSET]
)

correct_trajectory(osr, position=[0, 0, 0], beta=[0, 0, 1],
                   bfields=[[[0, 0.5, 0], [0, 0, 0.1], [0, 0, IDOFFSET - 1.1], 'kick_entry_x'],
                            [[0.5, 0, 0], [0, 0, 0.1], [0, 0, IDOFFSET - 1.1], 'kick_entry_y'],
                            [[0, 0.5, 0], [0, 0, 0.1], [0, 0, IDOFFSET + 1.1], 'kick_exit_x'],
                            [[0.5, 0, 0], [0, 0, 0.1], [0, 0, IDOFFSET + 1.1], 'kick_exit_y']
                           ],
                  tol=1e-17)
osr.print_all()

# Trajectory tests
osr.set_new_particle(particle='ideal')
trajectory_ideal = osr.calculate_trajectory()

x = trajectory_ideal[-1][1]
b = trajectory_ideal[-1][2]

t_dist = sqrt(x[0]*x[0] + x[1]*x[1])
t_angle = sqrt(b[0]*b[0] + b[1]*b[1]) / b[2]

print('Distance:', t_dist, 'PASSED' if t_dist < 1e-9 else 'FAILED')
print('Angle:', t_angle, 'PASSED' if t_angle < 1e-9 else 'FAILED')

if int(Process) == 0:
    osr.set_new_particle(particle='ideal')
    osr.calculate_spectrum(
        obs=[0, 0, OBS],
        energy_range_eV=[ESTART, ESTOP],
        bofile=out_file_name
    )
else:
    osr.calculate_spectrum(
        obs=[0, 0, OBS],
        energy_range_eV=[ESTART, ESTOP],
        nparticles=5000,
        ofile=out_file_name
    )


