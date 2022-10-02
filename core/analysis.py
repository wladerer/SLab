from pymatgen.io.vasp.outputs import Vasprun


def isConverged(xml):
    print(Vasprun(xml).converged)

xml = "/home/wladerer/github/SLab/outdir/Bi2Se3_001_vasprun.xml"

isConverged(xml)