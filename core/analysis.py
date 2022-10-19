from pymatgen.io.vasp.outputs import Vasprun
import os

def files_in_dir(dir):

    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)


def isConverged(xml):
    return Vasprun(xml).converged

def getStatistics(xml):
    data = Vasprun(xml)
    final_energy = data.final_energy
    band_gap, cbm, vbm, is_direct = data.eigenvalue_band_properties
    hubbard_U = data.hubbards
    run_type = data.run_type
    stat_string = f"{final_energy},{run_type}\n"

    return stat_string


def toCSV(rows):

    header = "Name,Final Energy,Band Gap,Valence band maximum,Conduction Band minimum,Direct BG,Hubbard U,Run Type"

    with open("slab_data.csv", 'w') as file:

        file.writelines(header + '\n')
        file.writelines(rows)

# systems = ("Bi2Se3", "Bi2Te3", "Sb2Se3", "Sb2Te3")
# planes = ("001", "010", "100", "111")
# dir_prefix = "/home/wladerer/github/SLab/outdir"
# not_converged = []
# rows = []
# for system in systems:
#     for plane in planes:
#         xml = f"{dir_prefix}/{system}/{plane}/vasprun.xml"
#         name = f"{system}_{plane}"
#         if not isConverged(xml):
#             not_converged.append(f"{name}")

#         row = getStatistics(xml)
#         rows.append(f"{name},{row}")




import sys
sys.path.append("/home/wladerer/github/SLab/outdir/Bi2Te3/010")
test = Vasprun("/home/wladerer/github/SLab/outdir/Bi2Te3/010/vasprun.xml").parameters
print(test)