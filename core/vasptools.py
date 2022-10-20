from pymatgen.core import Structure
from pymatgen.core.composition import Composition
from pymatgen.io.vasp import Poscar, Kpoints, Outcar
from dataclasses import dataclass
import os
import yaml


@dataclass
class User:
    potential_directory: str
    pbs_script_template: str
    yaml_scripts_directory: str


class StructureData:
    
    def __init__(self, directory: str):        
        self.directory = directory
        self.structure = Structure.from_file(os.path.join(directory, "CONTCAR"))
        self.reduced_formula, _ = Composition(self.structure.formula).get_reduced_formula_and_factor()
        self.outcar = Outcar(os.path.join(directory, "OUTCAR"))
        self.poscar = Poscar(self.structure)
        self.kx, self.ky, self.kz = self.getKpoints()

    def getKpoints(self) -> str:
        '''
        Returns kx, ky, kz from KPOINTS file
        '''
        kpoints = Kpoints.from_file(os.path.join(self.directory, "KPOINTS"))
        kpts = kpoints.as_dict()['kpoints'][0]
        
        return kpts[0], kpts[1], kpts[2]



class vaspInputGenerator:

    def __init__(self, user: User, directory: str="."):
        self.user = user
        self.pbs_script_template = user.pbs_script_template
        self.yaml_scripts_directory = user.yaml_scripts_directory
        self.directory = directory
        self.structure = Structure.from_file(os.path.join(directory, "CONTCAR"))
        self.reduced_formula, _ = Composition(self.structure.formula).get_reduced_formula_and_factor()


    def makePOTCAR(self, user: User) -> None:
        '''
        Creates POTCAR file from POTENTIAL_DIRECTORY
        '''
        potential_dict = {"Bi":"Bi_d","Ba":"Ba_sv","Ca":"Ca_sv","Li":"Li_sv","K":"K_sv","Cr":"Cr_pv", "Cu":"Cu_pv", "Cs":"Cs_sv", "Hf":"Hf_pv", "Mn":"Mn_pv", "Mo":"Mo_pv", "Nb":"Nb_pv", "Ni":"Ni_pv", "Os":"Os_pv", "Pd":"Pd_pv", "Rb":"Rb_sv", "Re":"Re_pv", "Rh":"Rh_pv", "Ru":"Ru_pv", "Ta":"Ta_pv", "Tc":"Tc_pv", "Ti":"Ti_pv", "V":"V_pv", "W":"W_pv"}

        '''Handles writing POTCARs'''
        
        order: list[str] = []
        with open(self.poscar, 'r') as poscar:
            lines = poscar.readlines()
            order = lines[5].split()
        
        potcar_strings = []
        for atom in order:

            if atom in potential_dict:

                potcar_strings.append(f"{User.potcar_directory}/{potential_dict[atom]}/POTCAR")
            
            else:

                potcar_strings.append(f"{User.potcar_directory}/{atom}/POTCAR")

        potcar_string = " ".join(potcar_strings)
            
        os.system(f"cat {potcar_string}")
    

    def writeKpoints(self, density: list=[50,50,50], save=True): 
        '''Writes KPOINT file to current directory
        
        Kpoints are assigned by length [x,y,z]/[a,b,c]
        '''

        kpts = Kpoints.automatic_density_by_lengths(self.structure, density, force_gamma=True)
        kpoints = kpts.as_dict()['kpoints'][0]
        if save:
            kpts.write_file(f"{self.formula}_{self.plane}.kpoints")

        return f"{int(kpoints[0])}x{int(kpoints[1])}x{int(kpoints[2])}"

    def writePBS(self):

        #read yaml file from yaml scripts directory
        with open(os.path.join(self.yaml_scripts_directory, "pbs_script.yaml"), "r") as pbs_script:
            pbs_script = yaml.load(pbs_script, Loader=yaml.FullLoader)

        # #write pbs_script
        # with open(f"{self.formula}_{self.plane}.pbs", "w") as pbs_file:
            





def makeDirectory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def iterate_over_files(directory: str):
    for file in os.listdir(directory):
        if file:
            print(str(os.path.join(directory, file)))

def iterate_through_all_dirs(directory: str):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print only the two parent directories
            name, plane = str(os.path.join(root, file)).split("/")[-3:-1]


def getreducedFormula(file: str):
    '''
    Get the reduced formula of a structure
    '''
    structure = Structure.from_file(file)
    molecular_formula: str = ''.join(structure.formula.split())
    reduced_formula, _ = Composition(molecular_formula).get_reduced_formula_and_factor()            

    return reduced_formula

