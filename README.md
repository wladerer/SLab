# SLab
Utilities to work with slabs and add adsorbates

- Specify miller plane of interest
- Automatically plot potential slabs and slabs with adsorbates
- Create unique slabs from POSCAR/CONTCARs
- Generate Kpaths and KPOINTS for slabs
- Create all possible adsorbed structures for a surface
- Quick creation of INCAR with Snippets
- Easy creation of (ordered) POTCARs

A minimal example is shown below:

```
from bulk2slab import *

#Specify the file that contains relaxed bulk
Bi2Se3_contcar = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp" 

#Create an instance of a Bulk object
Bi2Se3_bulk = Bulk(Bi2Se3_contcar) 

 # find all unique possible (001) slabs
slabs = bulk2slab(Bi2Se3_bulk, (0, 0, 1), MIN_SLAB=2, MIN_VAC=2)

#Save each slab if you'd like
#Slab objects filenames are systematized
for slab in slabs:
    slab.saveSlab()

#write KPOINTS file - Kpoints are assigned by length [x,y,z]/[a,b,c], default is [50,50,50]
writeKpoints(slabs[0])
```
Another example:

```
from bulk2slab import *
from Potcar import writePOTCAR

Bi2Se3_contcar = "/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp"
Bi2Te3_contcar = "/SLab/test/BULK_CONTCARS/Bi2Te3_CONTCAR.vasp"
Sb2Se3_contcar = "/SLab/test/BULK_CONTCARS/Sb2Se3_CONTCAR.vasp"
Sb2Te3_contcar = "/SLab/test/BULK_CONTCARS/Sb2Te3_CONTCAR.vasp"
contcars = [Bi2Se3_contcar, Bi2Te3_contcar, Sb2Te3_contcar, Sb2Se3_contcar]

#Write POTCARs
for contcar in contcars:
    writePOTCAR(contcar, "/app/vaspapp/Potentials/PBE")

slabs = prepareSlabs(contcars, [(1,1,1), (1,0,0), (0,1,0), (0,0,1)], 2, 2)

#Write POSCARs and KPOINTS
for slab in slabs:
    slab.saveSlab()
    writeKpoints(slab)

```

# Future Endeavors

- Create submit scripts for multi-step processes (e.g Band Structure, LOBSTERs, adsorbtions to surfaces)
- Estimate NBANDs
