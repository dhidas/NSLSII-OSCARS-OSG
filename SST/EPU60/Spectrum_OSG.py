# This is meant to be run on OSG or similar condor-type systems

# Command line arguments are given by condor at runtime
import sys
sys.path.append('.')

# import oscars
import oscars.sr
from oscars.util import *
from oscars.fit import *
from oscars.plots_mpl import *

# Get process number and gap from input
NAME = sys.argv[1]
GAP = float(sys.argv[2])
MODE = sys.argv[3]
PHASE = float(sys.argv[4])
PHASEPM = 'p' if PHASE >=0 else 'm'
Process = sys.argv[5]


out_name = '{}_gap_{:07.3f}_mode_{}_phase_{}{:07.3f}_{:04.0f}'.format(NAME, GAP, MODE, PHASEPM, PHASE, int(Process))


# Geometric constants
FIELDOFFSET = - 1.05
IDOFFSET = 1.250
OBS = 30 + IDOFFSET
ESTART = 10
ESTOP = 2600

# Number of particles each node for multi-particle simulations
NPARTICLES = 50

# Setting 1 thread and no GPU for OSG
osr = oscars.sr.sr(gpu=0, nthreads=10)

osr.set_particle_beam(beam='NSLSII-ShortStraight', x0=[0, 0, IDOFFSET - 1.6/2])
osr.set_ctstartstop(0, 1.6)


file_list = read_file_list2('/Users/dhidas/OSCARS-dev/NSLSII-MM-Data/SST/EPU60/'+MODE+'/file_list.txt', gap=GAP, phase_mode=MODE)


osr.add_bfield_interpolated(
    file_list,
    iformat='OSCARS1D Z Bx By Bz',
    scale=[0.001],
    parameter=PHASE,
    translation=[0, 0, IDOFFSET + FIELDOFFSET]
)

# Trajectory correction
False and correct_trajectory(osr, position=[0, 0, IDOFFSET + 1.6/2], beta=[0, 0, 1],
                   bfields=[[[0, 0.5, 0], [0, 0, 0.15], [0, 0, IDOFFSET - 0.7], 'kick_entry_x'],
                            [[0.5, 0, 0], [0, 0, 0.15], [0, 0, IDOFFSET - 0.7], 'kick_entry_y'],
                            [[0, 0.5, 0], [0, 0, 0.15], [0, 0, IDOFFSET + 0.7], 'kick_exit_x'],
                            [[0.5, 0, 0], [0, 0, 0.15], [0, 0, IDOFFSET + 0.7], 'kick_exit_y']
                           ],
                  tol=1e-16)
osr.print_all()

osr.set_new_particle(particle='ideal')
trajectory_ideal = osr.calculate_trajectory()


# Trajectory tests
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
        polarization='linear-horizontal',
        ofile=out_name+'_LH.txt',
    )

    osr.set_new_particle(particle='ideal')
    osr.calculate_spectrum(
        obs=[0, 0, OBS],
        energy_range_eV=[ESTART, ESTOP],
        polarization='linear-vertical',
        ofile=out_name+'_LV.txt',
    )


else:
    osr.calculate_spectrum(
        obs=[0, 0, OBS],
        energy_range_eV=[ESTART, ESTOP],
        polarization='linear-horizontal',
        nparticles=NPARTICLES,
        ofile=out_name+'_LH.txt',
    )

    osr.calculate_spectrum(
        obs=[0, 0, OBS],
        energy_range_eV=[ESTART, ESTOP],
        polarization='linear-vertical',
        nparticles=NPARTICLES,
        ofile=out_name+'_LV.txt',
    )

