import bulk2slab as b2s
from pymatgen.io.vasp import Poscar, Kpoints, Incar
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.electronic_structure.plotter import BSDOSPlotter, BSPlotter, DosPlotter
from pymatgen.core import Lattice, Structure, Molecule

def write_kpath(CONTCAR):
    struct = Structure.from_file(CONTCAR)
    kpath = HighSymmKpath(struct)
    kpts = Kpoints.automatic_linemode(divisions=40,ibz=kpath)
    kpts.write_file("KPOINTS_nsc")


