CONTCARs created using VASP with the following specifications

```
 Dimension of arrays:
   k-points           NKPTS =     44   k-points in BZ     NKDIM =     44   number of bands    NBANDS=     88
   number of dos      NEDOS =    301   number of ions     NIONS =     15
   non local maximal  LDIM  =      6   non local SUM 2l+1 LMDIM =     18
   total plane-waves  NPLWV = 324000
   max r-space proj   IRMAX =   7207   max aug-charges    IRDMAX=  31168
   dimension x,y,z NGX =    36 NGY =   36 NGZ =  250
   dimension x,y,z NGXF=    72 NGYF=   72 NGZF=  500
   support grid    NGXF=    72 NGYF=   72 NGZF=  500
   ions per type =               6   9
   NGX,Y,Z   is equivalent  to a cutoff of  14.28, 14.28, 13.67 a.u.
   NGXF,Y,Z  is equivalent  to a cutoff of  28.57, 28.57, 27.33 a.u.

 SYSTEM =  Bi2Se3 I-structure opt
 POSCAR =  Bi6 Se9

 Startparameter for this run:
   NWRITE =      2    write-flag & timer
   PREC   = accura    normal or accurate (medium, high low for compatibility)
   ISTART =      0    job   : 0-new  1-cont  2-samecut
   ICHARG =      2    charge: 1-file 2-atom 10-const
   ISPIN  =      1    spin polarized calculation?
   LNONCOLLINEAR =      F non collinear calculations
   LSORBIT =      F    spin-orbit coupling
   INIWAV =      1    electr: 0-lowe 1-rand  2-diag
   LASPH  =      T    aspherical Exc in radial PAW
   METAGGA=      F    non-selfconsistent MetaGGA calc.

 Electronic Relaxation 1
   ENCUT  =  600.0 eV  44.10 Ry    6.64 a.u.   8.37  8.37 60.74*2*pi/ulx,y,z
   ENINI  =  600.0     initial cutoff
   ENAUG  =  446.8 eV  augmentation charge cutoff
   NELM   =    100;   NELMIN=  2; NELMDL= -5     # of ELM steps
   EDIFF  = 0.1E-04   stopping-criterion for ELM
   LREAL  =      T    real-space projection
   NLSPLINE    = F    spline interpolate recip. space projectors
   LCOMPAT=      F    compatible to vasp.4.4
   GGA_COMPAT  = T    GGA compatible to vasp.4.4-vasp.4.6
   LMAXPAW     = -100 max onsite density
   LMAXMIX     =    4 max onsite mixed and CHGCAR
   VOSKOWN=      0    Vosko Wilk Nusair interpolation
   ROPT   =   -0.00025  -0.00025
 Ionic relaxation
   EDIFFG = -.1E-01   stopping-criterion for IOM
   NSW    =    100    number of steps for IOM
   NBLOCK =      1;   KBLOCK =    100    inner block; outer block
   IBRION =      2    ionic relax: 0-MD 1-quasi-New 2-CG
   NFREE  =      1    steps in history (QN), initial steepest desc. (CG)
   ISIF   =      3    stress and relaxation
   IWAVPR =     11    prediction:  0-non 1-charg 2-wave 3-comb
   ISYM   =      2    0-nonsym 1-usesym 2-fastsym
   LCORR  =      T    Harris-Foulkes like correction to forces

   POTIM  = 0.5000    time-step for ionic-motion
   TEIN   =    0.0    initial temperature
   TEBEG  =    0.0;   TEEND  =   0.0 temperature during run
   SMASS  =  -3.00    Nose mass-parameter (am)
   estimated Nose-frequenzy (Omega)   =  0.10E-29 period in steps =****** mass=  -0.401E-27a.u.
   SCALEE = 1.0000    scale energy and forces
   NPACO  =    256;   APACO  = 16.0  distance and # of slots for P.C.
   PSTRESS=    0.0 pullay stress
```
