from pymatgen.core import Structure, Molecule
from pymatgen.core.composition import Composition
from pymatgen.core.surface import SlabGenerator
from pymatgen.io.vasp import Poscar, Kpoints
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.analysis.adsorption import plot_slab
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from matplotlib import pyplot as plt
import numpy as np


class Bulk:
    
    def __init__(self, CONTCAR: str):
            self.CONTCAR = CONTCAR
            self.structure: Structure = Structure.from_file(CONTCAR)
            self.formula = self.getreducedFormula()
            self.getParams(self.structure)

    def getParams(self, valid_slab):
        self.length: float = valid_slab.as_dict()['lattice']['c']
        self.a: float = valid_slab.as_dict()['lattice']['a']
        self.b: float = valid_slab.as_dict()['lattice']['b']
        self.c: float = valid_slab.as_dict()['lattice']['c']


    def getreducedFormula(self):
        '''Pymatgen does not have a simple way of getting a reduced formula from a Structure object'''
        molecular_formula: str = ''.join(self.structure.formula.split())
        reduced_formula, factor = Composition(molecular_formula).get_reduced_formula_and_factor()            

        return reduced_formula

    def addH(self, plot=False):

        adsorbate = Molecule("H", [[0,0,0]])
        asf = AdsorbateSiteFinder(self.structure)
        ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=[1,1,1],find_args={"distance":1.6})
        
        if plot ==True:
            
            # Plot all adsorption sites such that they are arranged in a grid using subplot2grid function
            fig = plt.figure(figsize=(300, 200))
            n = len(ads_structs)
            for i, ads_struct in enumerate(ads_structs):
                ax = plt.subplot2grid((int(np.ceil(n/2)), 2), (i//2, i%2), fig=fig)
                plot_slab(ads_struct, ax=ax, adsorption_sites=True)
                ax.set_title("Adsorption site {}".format(i+1))
            plt.tight_layout()
            plt.show()




class Slab(Bulk):

    def __init__(self, valid_slab, index: tuple, MIN_SLAB: int, MIN_VAC: int):
        super().__init__(valid_slab)
        self.structure: Structure = valid_slab
        self.getParams(valid_slab)
        self.plane = f"{str(index[0]) + str(index[1]) + str(index[2])}"
        self.filename: str = f"{self.formula}_{self.plane}_POSCAR.vasp"
    
    
    def getParams(self, valid_slab):
        self.length: float = valid_slab.as_dict()['lattice']['c']
        self.a: float = valid_slab.as_dict()['lattice']['a']
        self.b: float = valid_slab.as_dict()['lattice']['b']
        self.c: float = valid_slab.as_dict()['lattice']['c']

    def longestAxis(self):
        lattice_params: list[str] = ["a", "b", "c"]
        axis: float = np.argmax([self.a, self.b, self.c])
        longest_axis: str = lattice_params[axis]

        return longest_axis
    
    def __str__(self):
        return str(self.structure)

    def addH(self, plot=False):

        adsorbate = Molecule("H", [[0,0,0]])
        asf = AdsorbateSiteFinder(self.structure)
        ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=[1,1,1],find_args={"distance":1.6})
        
        if plot ==True:

            fig = plt.figure(figsize=[15,60])
            for n, ads_struct in enumerate(ads_structs):
                ax = fig.add_subplot(1,len(ads_structs),n+1)
                plot_slab(ads_struct, ax, adsorption_sites=False)
                self.configPlot(n, ax)
            plt.show()

        return ads_structs

    def saveSlab(self, freeze: bool = False):

        if freeze:
            POSCAR = Poscar(self.structure, sort_structure=True)
            POSCAR.selective_dynamics = freezeArray(self)
            POSCAR.write_file(self.filename)
        
        else:
            POSCAR = Poscar(self.structure, sort_structure=True)
            POSCAR.write_file(self.filename)
        

class adSlab(Bulk):

    def __init__(self, CONTCAR: str):
        super().__init__(CONTCAR)
        self.a: float = self.structure.as_dict()['lattice']['a']
        self.b: float = self.structure.as_dict()['lattice']['b']
        self.c: float = self.structure.as_dict()['lattice']['c']

    def longestAxis(self):
        lattice_params: list[str] = ["a", "b", "c"]
        axis: float = np.argmax([self.a, self.b, self.c])
        longest_axis: str = lattice_params[axis]

        return longest_axis
    
    def __str__(self):
        return str(self.structure)

    def addH(self, plot=False):

        adsorbate = Molecule("H", [[0,0,0]])
        asf = AdsorbateSiteFinder(self.structure)
        ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=[1,1,1],find_args={"distance":1.6})
        
        if plot ==True:

            fig = plt.figure(figsize=[15,60])
            for n, ads_struct in enumerate(ads_structs):
                ax = fig.add_subplot(1,len(ads_structs),n+1)
                plot_slab(ads_struct, ax, adsorption_sites=False)
                self.configPlot(n, ax)
            plt.show()

        return ads_structs

    def configPlot(self, n, ax):
        ax.set_title(n+1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5,5)
    
    def saveSlab(self, freeze: bool = False, selective_dynamics=None):

        if freeze:
            POSCAR = Poscar(self.structure, sort_structure=True)
            POSCAR.selective_dynamics = selective_dynamics
            POSCAR.write_file()
        
        else:
            POSCAR = Poscar(self.structure, sort_structure=True)
            POSCAR.write_file()
    

def bulk2slab(bulk, index: tuple, MIN_SLAB: int, MIN_VAC: int):
        '''
        Returns valid slabs according to their symmetry and polarity

        MIN_SLAB: this is the minimium slab size in multiples of the hkl planes
        '''
        slabgen = SlabGenerator(bulk.structure, index, MIN_SLAB, MIN_VAC, primitive=False, in_unit_planes=True) #this will find all unique surfaces of the structure within the specified miller plane
        slabs: list = slabgen.get_slabs()
        valid_slabs = isValid(bulk, index, MIN_SLAB, MIN_VAC, slabs)

        return valid_slabs

def isValid(bulk, index, MIN_SLAB, MIN_VAC, slabs):
    '''
    Helper function to check for symmetric, non-polar slabs
    '''
    valid_slabs: list = [slab for slab in slabs if (not slab.is_polar() and slab.is_symmetric())] #list comprehension that creates an array of valid slabs according to our criteria
    valid_slabs: list = [Slab(slab, bulk.CONTCAR, index, MIN_SLAB, MIN_VAC) for slab in valid_slabs]
    return valid_slabs

def prepareSlabs(contcars: list[str], indices: list[tuple], min_slab: int=2, min_vac: int=2):
    '''
    Creates a list of Slab objects from a list of CONTCARs for quick use
    '''

    bulk_list = [Bulk(contcar) for contcar in contcars]
    slab_list = []
    for index in indices:
        for bulk in bulk_list:
            for slab in bulk2slab(bulk, index, min_slab, min_vac):
                slab_list.append(slab)
    
    return slab_list


def metaData(slab_list: list[Slab], filename: str="metadata", wKPOINTS: bool=False, mode: str='w'):
    '''Creates CSV with slab attributes
    
       Useful for checking possible errors
    '''

    with open(f"{filename}.csv", mode) as meta:
        meta.write("Formula,index,a,b,c,kpoints\n")

        for slab in slab_list:

            kpoints = None
            if wKPOINTS:
                kpoints = writeKpoints(slab)
            
            meta.write(f"{slab.formula},{slab.plane},{slab.a:10.5f},{slab.b:10.5f},{slab.c:10.5f},{(kpoints or '')},\n")


def writeKpath(CONTCAR: str):
    '''
    Writes Kpath from CONTCAR in linemode according to unit cell type
    '''
    struct: Structure = Structure.from_file(CONTCAR)
    kpath = HighSymmKpath(struct)
    kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
    kpts.write_file("KPOINTS_nsc")

def writeKpoints(slab: Slab, density: list=[50,50,50], save=True): 
    '''Writes KPOINT file to current directory
    
       Kpoints are assigned by length [x,y,z]/[a,b,c]
    '''

    kpts = Kpoints.automatic_density_by_lengths(slab.structure, density, force_gamma=True)
    kpoints = kpts.as_dict()['kpoints'][0]
    if save:
        kpts.write_file(f"{slab.formula}_{slab.plane}.kpoints")

    return f"{int(kpoints[0])}x{int(kpoints[1])}x{int(kpoints[2])}"

def findLowestAtoms(slab, depth):
    df = slab.structure.as_dataframe()
    frac2cart = {"a":"x","b":"y","c":"z"}
    longest_cartesian  = frac2cart[slab.longestAxis()]
    rows: list[float] = df.index[df[longest_cartesian] <= depth]
    natoms = len(df.index)

    return rows, natoms

def freezeArray(slab, depth=5):
    rows_to_freeze, natoms = findLowestAtoms(slab, depth)
    mobile = [True, True, True]
    freeze = [False, False, False]
    selective_dynamics = []
    for j in range(natoms):
        if j in rows_to_freeze:
            selective_dynamics.append(freeze)
        else:
            selective_dynamics.append(mobile)
    
    return selective_dynamics
