import pymatgen.core
from pymatgen.core.composition import Element, Composition
from pymatgen.core.periodic_table import Specie
from pymatgen.core import Lattice, Structure, Molecule
from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar, Kpoints, Incar
from pymatgen.io.cif import CifWriter
from pymatgen.analysis.adsorption import plot_slab
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from matplotlib import pyplot as plt

class Bulk:
    
    def __init__(self, CONTCAR):
            self.CONTCAR = CONTCAR
            self.structure = Structure.from_file(CONTCAR)
            self.formula = ''.join(self.structure.formula.split())


class Slab(Bulk):

    def __init__(self, valid_slab, CONTCAR, index, MIN_SLAB, MIN_VAC):
        super().__init__(CONTCAR)
        self.structure = valid_slab
        self.length = valid_slab.as_dict()['lattice']['c']
        self.filename = f"{self.formula}_{str(index[0]) + str(index[1]) + str(index[2])}_POSCAR.vasp"
    
    def __str__(self):
        return str(self.structure)

    def save_slab(self):

        POSCAR = Poscar(self.structure, sort_structure=True)
        POSCAR.write_file(self.filename)
        
    def addH(self, plot=False):

        adsorbate = Molecule("H", [[0,0,0]])
        asf = AdsorbateSiteFinder(self.structure)
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

def find_slabs(bulk, index, MIN_SLAB, MIN_VAC):
        slabgen = SlabGenerator(bulk.structure, index, MIN_SLAB, MIN_VAC, primitive=False, in_unit_planes=True) #this will find all unique surfaces of the structure within the specified miller plane
        slabs = slabgen.get_slabs()
        valid_slabs = [slab for slab in slabs if (not slab.is_polar() and slab.is_symmetric())] #list comprehension that creates an array of valid slabs according to our criteria
        valid_slabs = [Slab(slab, bulk.CONTCAR, index, MIN_SLAB, MIN_VAC) for slab in valid_slabs]

        return valid_slabs