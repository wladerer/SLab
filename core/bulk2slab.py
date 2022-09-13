import pymatgen.core
from pymatgen.core.composition import Element, Composition
from pymatgen.core.periodic_table import Specie
from pymatgen.core import Lattice, Structure, Molecule
from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar, Kpoints, Incar
from pymatgen.io.cif import CifWriter
from pymatgen.analysis.adsorption import plot_slab
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, DosPlotter
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from matplotlib import pyplot as plt

def bulk2slab(CONTCAR, INDEX=(1,0,0), MIN_SLAB = 2, MIN_VAC=2, plot_slabs=False, plot_valid_slabs=False):

    bulk = Structure.from_file(CONTCAR)
    formula = ''.join(bulk.formula.split())
    slabgen = SlabGenerator(bulk, INDEX, MIN_SLAB, MIN_VAC, primitive=False, in_unit_planes=True) #this will find all unique 111 surfaces of the structure
    slabs = slabgen.get_slabs()

    
    #Bi2Se3, Bi2Te3, Sb2Te3 - unit cell contains 3 QLs
    #Sb2Se3 - unit cell contains 2 layers

    if plot_slabs == True:

        fig = plt.figure(figsize=[15,60])
        for n, slab in enumerate(slabs):
            ax = fig.add_subplot(1, len(slabs), n+1)
            plot_slab(slab, ax, adsorption_sites=False)
            ax.set_title(n+1)
            ax.set_xticks([])
            ax.set_yticks([])

        plt.show()

    valid_slabs = [slab for slab in slabs if (not slab.is_polar() and slab.is_symmetric())] #list comprehension that creates an array of valid slabs according to our criteria
    print("There are " + str(len(valid_slabs)) + " valid slabs out of " + str(len(slabs)) + " possible slabs")

    if plot_valid_slabs == True:

        fig = plt.figure(figsize=[15,60])
        for n, slab in enumerate(valid_slabs):
            ax = fig.add_subplot(1, len(valid_slabs), n+1)
            plot_slab(slab, ax, adsorption_sites=False)
            ax.set_title(n+1)
            ax.set_xticks([])
            ax.set_yticks([])

        plt.show()

        
    return valid_slabs, INDEX, formula, bulk

def save_slab(slab_data):

    valid_slabs = slab_data[0]
    miller_plane = slab_data[1]
    formula = slab_data[2]
    plane = str(miller_plane[0]) + str(miller_plane[1]) + str(miller_plane[2])

    with open("slab_metadata.csv",'w',encoding = 'utf-8') as f:

        f.write("filename,formula,supercell_length")
        f.write('\n')
        
        for n,slab in enumerate(valid_slabs): 
            POSCAR = Poscar(slab, sort_structure=True)
            filename = f"{formula}_{plane}_POSCAR{n+1}.vasp"
            POSCAR.write_file(filename)
            length = slab.as_dict()['lattice']['c']

            f.write(f"{filename},{formula},{length}")
            f.write('\n')

def write_kpath(file):
    struct = Structure.from_file(file)
    kpath = HighSymmKpath(struct)
    kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
    kpts.write_file("KPOINTS_nsc")

def addH(slab, plot=False):

    adsorbate = Molecule("H", [[0,0,0]])
    asf = AdsorbateSiteFinder(slab)
    ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=[1,1,1],find_args={"distance":1.6})
    
    if plot ==True:

        fig = plt.figure(figsize=[15,60])
        for n, ads_struct in enumerate(ads_structs):
            ax = fig.add_subplot(1,len(ads_structs),n+1)
            plot_slab(ads_struct, ax, adsorption_sites=False)
            ax.set_title(n+1)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xlim(-5, 5)
            ax.set_ylim(-5,5)
        plt.show()

    return ads_struct
