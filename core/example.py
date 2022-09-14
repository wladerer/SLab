import bulk2slab as b2s

CONTCAR = "/home/wladerer/github/SLab/test/BULK_CONTCARS/Bi2Se3_CONTCAR.vasp"
Bi2Se3_bulk = b2s.Bulk(CONTCAR)
slabs = b2s.find_slabs(Bi2Se3_bulk, (1,0,0), 2, 2)