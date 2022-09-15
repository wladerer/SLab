# SLab
Utilities to work with slabs and add adsorbates

- Specify miller plane of interest
- Automatically plot potential slabs and slabs with adsorbates
- Create unique slabs from POSCAR/CONTCARs
- Generate Kpaths and KPOINTS for slabs
- Create all possible adsorbed structures for a surface

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
# Future Endeavors

- Generate remaining VASP input files
- Create submit scripts for multi-step processes (e.g Band Structure, LOBSTERs, adsorbtions to surfaces)
- Estimate NBANDs
- Easy INCAR editor for on the fly adjustments (bye bye sed -i)
