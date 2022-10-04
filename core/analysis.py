from pymatgen.io.vasp.outputs import Vasprun
import os

def files_in_dir(dir):

    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)


def isConverged(dir):
    return Vasprun(dir).converged

dir = "/home/wladerer/github/SLab/outdir/Bi2Se3/001/vasprun.xml"

systems = ("Bi2Se3", "Bi2Te3", "Sb2Se3", "Sb2Te3")
planes = ("001", "010", "100", "111")
dir_prefix = "/home/wladerer/github/SLab/outdir"

not_converged = []
for system, plane in zip(systems,planes):
    xml = f"{dir_prefix}/{system}/{plane}/vasprun.xml"
    if not isConverged(xml):
        not_converged.append(f"{system}_{plane}")

print(not_converged)