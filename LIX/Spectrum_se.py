import oscars.sr
from oscars.plots_mpl import *
from oscars.util import *

osr = oscars.sr.sr()
osr.set_nthreads_global(8)

osr.set_particle_beam(beam='NSLSII-LongStraight', name='beam', x0=[0, 0, -1.5])
osr.set_ctstartstop(0, 3)

file_list = read_file_list('/Users/dhidas/Desktop/IVU 2,8m A13004/Final Scans_4,16,15/FieldC/List_LIX.txt')

for gap in np.linspace(5.1, 40.0, 20):
    osr.clear_bfields()
    osr.add_bfield_interpolated(mapping=file_list,
                                iformat='OSCARS1D Z Bx By Bz',
                                parameter=gap,
                                scale=[0.001],
                                name='undulator'
                               )
    #osr.add_bfield_gaussian(bfield=[-0.0020, +0.0005, 0], sigma=[0, 0, 0.010], translation=[0, 0, -1.4], name='kick_entry')
    #osr.add_bfield_gaussian(bfield=[+0.0003, +0.0005, 0], sigma=[0, 0, 0.010], translation=[0, 0, +1.5], name='kick_exit')
    #osr.add_bfield_uniform(bfield=[+0.00001, -0.000015, 0], width=[0, 0, 3], name='body_coil')

    spectrum = osr.calculate_spectrum(obs=[0, 0, 30], energy_range_eV=[100, 30000], npoints=30000-100)
    plot_spectrum(spectrum, title=str(gap) + ' mm gap')
    exit(0)

