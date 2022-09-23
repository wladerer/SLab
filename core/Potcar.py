from os import system

#These are the recommended PAW settings
potential_dict = {"Bi":"Bi_d","Ba":"Ba_sv","Ca":"Ca_sv","Li":"Li_sv","K":"K_sv","Cr":"Cr_pv", "Cu":"Cu_pv", "Cs":"Cs_sv", "Hf":"Hf_pv", "Mn":"Mn_pv", "Mo":"Mo_pv", "Nb":"Nb_pv", "Ni":"Ni_pv", "Os":"Os_pv", "Pd":"Pd_pv", "Rb":"Rb_sv", "Re":"Re_pv", "Rh":"Rh_pv", "Ru":"Ru_pv", "Ta":"Ta_pv", "Tc":"Tc_pv", "Ti":"Ti_pv", "V":"V_pv", "W":"W_pv"}

def writePOTCAR(POSCAR: str, potcar_directory: str):
    '''Handles writing POTCARs'''
    
    order: list[str] = []
    with open(POSCAR, 'r') as poscar:
        lines = poscar.readlines()
        order = lines[5].split()
    
    potcar_strings = []
    for atom in order:

        if atom in potential_dict:

            potcar_strings.append(f"{potcar_directory}/{potential_dict[atom]}/POTCAR")
        
        else:

            potcar_strings.append(f"{potcar_directory}/{atom}/POTCAR")

    potcar_string = " ".join(potcar_strings)
        
    print(f"cat {potcar_string}")




        

