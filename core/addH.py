from bulk2slab import *

cont = "/home/wladerer/github/SLab/outdir/Bi2Se3/001/CONTCAR"

bi2se3_wH = adSlab(cont)

seldyn = freezeArray(bi2se3_wH)
structs: list[adSlab] = bi2se3_wH.addH()


