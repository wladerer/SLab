from bulk2slab import *

Bi2Se3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp"
Bi2Te3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Te3_CONTCAR.vasp"
Sb2Se3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Sb2Se3_CONTCAR.vasp"
Sb2Te3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Sb2Te3_CONTCAR.vasp"
contcars = [Bi2Se3_contcar, Bi2Te3_contcar, Sb2Te3_contcar]

sb_slabs = prepareSlabs([Sb2Se3_contcar], [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 3, 3)
all_others = prepareSlabs(contcars, [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 2, 2)

for slab in sb_slabs:
    all_others.append(slab)

for slab in all_others:
    slab.saveSlab()
