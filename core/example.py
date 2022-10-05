from bulk2slab import *
from Potcar import writePOTCAR

Bi2Se3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp"
Bi2Te3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Te3_CONTCAR.vasp"
Sb2Se3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Sb2Se3_CONTCAR.vasp"
Sb2Te3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Sb2Te3_CONTCAR.vasp"
contcars = [Bi2Se3_contcar, Bi2Te3_contcar, Sb2Te3_contcar]

#Write POTCARs
# for contcar in contcars:
#     writePOTCAR(contcar, "/app/vaspapp/Potentials/PBE")

slabs = prepareSlabs(contcars, [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 2, 2)
sb2se3_slabs = prepareSlabs([Sb2Se3_contcar], [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 3, 3)
all_slabs = slabs + sb2se3_slabs

metaData(all_slabs, "meta_data", wKPOINTS=True)
