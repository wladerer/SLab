from bulk2slab import *
from Potcar import writePOTCAR

Bi2Se3_contcar = "/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp"
Bi2Te3_contcar = "/SLab/test/BULK_CONTCARS/Bi2Te3_CONTCAR.vasp"
Sb2Se3_contcar = "/SLab/test/BULK_CONTCARS/Sb2Se3_CONTCAR.vasp"
Sb2Te3_contcar = "/SLab/test/BULK_CONTCARS/Sb2Te3_CONTCAR.vasp"
contcars = [Bi2Se3_contcar, Bi2Te3_contcar, Sb2Te3_contcar]

#Write POTCARs
for contcar in contcars:
    writePOTCAR(contcar, "/app/vaspapp/Potentials/PBE")

slabs = prepareSlabs(contcars, [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 2, 2)

#Write POSCARs and KPOINTS
for slab in slabs:
    slab.saveSlab(freeze=True)
    writeKpoints(slab)
