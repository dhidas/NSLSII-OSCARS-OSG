# This is meant to be run on OSG or similar condor-type systems

print('Python has started')

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
NPARTICLES = 5000

# Setting 1 thread and no GPU for OSG
osr = oscars.sr.sr(gpu=0, nthreads=10)

osr.set_particle_beam(beam='NSLSII-ShortStraight', x0=[0, 0, IDOFFSET - 1.6/2])
osr.set_ctstartstop(0, 1.6)


fn = read_file_list_interpolate_2d(
    ifile='NSLSII-MM-Data/SST/EPU60/'+MODE+'/file_list.txt',
    iformat='OSCARS1D Z Bx By Bz',
    phase_mode=MODE,
    gap=GAP,
    phase=-PHASE,
    ofile='test.dat'
    )

osr.add_bfield_file(ifile=fn, iformat='OSCARS1D Z Bx By Bz', scale=[0.001], translation=[0, 0, IDOFFSET + FIELDOFFSET])


# Trajectory correction
correct_trajectory(osr, position=[0, 0, IDOFFSET + 1.6/2], beta=[0, 0, 1],
                   bfields=[[[0, 0.5, 0], [0, 0, 0.15], [0, 0, IDOFFSET - 0.7], 'kick_entry_x'],
                            [[0.5, 0, 0], [0, 0, 0.15], [0, 0, IDOFFSET - 0.7], 'kick_entry_y'],
                            [[0, 0.5, 0], [0, 0, 0.15], [0, 0, IDOFFSET + 0.7], 'kick_exit_x'],
                            [[0.5, 0, 0], [0, 0, 0.15], [0, 0, IDOFFSET + 0.7], 'kick_exit_y']
                           ],
                  tol=1e-16)
#osr.print_all()

osr.set_new_particle(particle='ideal')
trajectory_ideal = osr.calculate_trajectory(bofile=out_name+'_TJ.dat', oformat='t x y z bx by bz')


# Trajectory tests
x = trajectory_ideal[-1][1]
b = trajectory_ideal[-1][2]

t_dist = sqrt(x[0]*x[0] + x[1]*x[1])
t_angle = sqrt(b[0]*b[0] + b[1]*b[1]) / b[2]
print('Distance:', t_dist, 'PASSED' if t_dist < 1e-9 else 'FAILED')
print('Angle:', t_angle, 'PASSED' if t_angle < 1e-9 else 'FAILED')


if int(Process) == 0:
    osr.set_new_particle(particle='ideal')
    if MODE.upper().startswith('ANTIPARALLEL'):
        osr.calculate_spectrum(
            obs=[0, 0, OBS],
            energy_range_eV=[ESTART, ESTOP],
            polarization='linear-horizontal',
            bofile=out_name+'_LH.dat',
        )

        osr.set_new_particle(particle='ideal')
        osr.calculate_spectrum(
            obs=[0, 0, OBS],
            energy_range_eV=[ESTART, ESTOP],
            polarization='linear-vertical',
            bofile=out_name+'_LV.dat',
        )
    elif MODE.upper().startswith('PARALLEL'):
        if abs(PHASE) < 14.0 or abs(PHASE) > 16.0:
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='linear-horizontal',
                bofile=out_name+'_LH.dat',
            )
         
            osr.set_new_particle(particle='ideal')
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='linear-vertical',
                bofile=out_name+'_LV.dat',
            )
        else:
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='cl',
                bofile=out_name+'_CL.dat',
            )
 
            osr.set_new_particle(particle='ideal')
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='cr',
                bofile=out_name+'_CR.dat',
            )
    else:
        raise ValueError('MODE not recognized: ' + MODE)
 


else:
    if MODE.upper().startswith('ANTIPARALLEL'):
        osr.calculate_spectrum(
            obs=[0, 0, OBS],
            energy_range_eV=[ESTART, ESTOP],
            polarization='linear-horizontal',
            nparticles=NPARTICLES,
            bofile=out_name+'_LH.dat',
        )
 
        osr.calculate_spectrum(
            obs=[0, 0, OBS],
            energy_range_eV=[ESTART, ESTOP],
            polarization='linear-vertical',
            nparticles=NPARTICLES,
            bofile=out_name+'_LV.dat',
        )
    elif MODE.upper().startswith('PARALLEL'):
        if abs(PHASE) < 14.0 or abs(PHASE) > 16.0:
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='linear-horizontal',
                nparticles=NPARTICLES,
                bofile=out_name+'_LH.dat',
            )
         
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='linear-vertical',
                nparticles=NPARTICLES,
                bofile=out_name+'_LV.dat',
            )
        else:
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='cl',
                nparticles=NPARTICLES,
                bofile=out_name+'_CL.dat',
            )
 
            osr.calculate_spectrum(
                obs=[0, 0, OBS],
                energy_range_eV=[ESTART, ESTOP],
                polarization='cr',
                nparticles=NPARTICLES,
                bofile=out_name+'_CR.dat',
            )
    else:
        raise ValueError('MODE not recognized: ' + MODE)


