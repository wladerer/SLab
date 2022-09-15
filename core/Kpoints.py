from bulk2slab import Slab, Bulk, find_slabs
from pymatgen.io.vasp import Poscar, Kpoints, Incar
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, DosPlotter
from pymatgen.core import Lattice, Structure, Molecule

def writeKPATH(CONTCAR: str):
    struct: Structure = Structure.from_file(CONTCAR)
    kpath = HighSymmKpath(struct)
    kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
    kpts.write_file("KPOINTS_nsc")

def makeKPOINTs(slab: Slab, density: list=[50,50,50], save=True): 
    '''Writes KPOINT file to current directory
    
       Kpoints are assigned by length [x,y,z]/[a,b,c]
    '''

    kpts = Kpoints.automatic_density_by_lengths(slab.structure, density, force_gamma=True)
    kpoints = kpts.as_dict()['kpoints'][0]
    if save:
        kpts.write_file("KPOINTS")

    return f"{int(kpoints[0])}{int(kpoints[1])}{int(kpoints[2])}"



