# SLab
Utilities to work with slabs and add adsorbates

- Specify miller plane of interest
- Automatically plot potential slabs and slabs with adsorbates
- Create unique slabs from POSCAR/CONTCARs
- Generate Kpaths for slabs

A minimal example is shown below:

```
Bi2Te3_CONTCAR = "/home/wladerer/github/minis/pymatgen_test/bulk_contcars/CONTCARs/Bi2Te3_CONTCAR.vasp"
slab_data = bulk2slab(Bi2Te3_CONTCAR,(0,0,1), MIN_SLAB=3)
Bi2Te3_slabs_H = addH(slab_data[0][0], plot=True)
```
