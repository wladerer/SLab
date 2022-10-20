from pymatgen.core import Structure, Molecule
from pymatgen.core.composition import Composition
from pymatgen.io.vasp import Poscar
from pymatgen.analysis.adsorption import AdsorbateSiteFinder


def addH(file: str, adsorbate: Molecule, min_z: float=5.0, index=None): 
    #Load slab from CONTCAR file 
    slab = Structure.from_file("CONTCAR")
    
    #Get the formula of the slab
    formula = getreducedFormula(file)
    
    #Create an AdsorbateSiteFinder object
    asf = AdsorbateSiteFinder(slab)

    #Generate all possible adsorption sites for H on the slab
    ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=[1,1,1],find_args={"distance":1.6})


    #Freeze all atoms of each ads_struct with a z-coordinate less than 5.0
    for ads_struct in ads_structs:
        for site in ads_struct:
            if site.z < min_z:
                site.properties["selective_dynamics"] = [False, False, False]
            

    # Save all frozen slabs to a POSCAR file with a unique name
    for i, frozen_slab in enumerate(ads_structs):
        Poscar(frozen_slab).write_file(f"{formula}{index}_POSCAR_{i}.vasp")


def getreducedFormula(file: str):
    '''
    Get the reduced formula of a structure
    '''
    structure = Structure.from_file(file)
    molecular_formula: str = ''.join(structure.formula.split())
    reduced_formula, _ = Composition(molecular_formula).get_reduced_formula_and_factor()            

    return reduced_formula


h = Molecule("H", [[0,0,0]])
co = Molecule("CO", [[0, 0, 0], [0, 0, 1.23]])
co2 = Molecule("CO2", [[0,0,0],[1.65, 0, 0.5701],[1.65, 0, -0.5701]])
ethane = Molecule("CH3CH3", [[0,0,0], [1.08, 0, 0], [2.2, 0, 0],[0,0,1.54], [1.08, 0, 1.54], [2.2, 0, 1.54]])
ethene = Molecule("CH2CH2", [[0,0,0], [0,0,1.54], [1.08, 0, 0.7701], [1.08, 0, 0.7701]])
oh = Molecule("OH", [[0,0,0], [0.96,0,0]])
h2o = Molecule("H2O", [[0,0,0],[0,0,0.9788],[0,0.9726,0]])





