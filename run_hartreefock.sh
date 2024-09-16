#!/bin/bash
rm -f *.dat *.tex 
cd ../build/ && make -j8 && cd -
../build/src/bachelorthesis/hartreefock3D
#../build/src/bachelorthesis/hartreefock
#./plot_1D.py rho.dat charged_rho.dat potential.dat
#./plot_1D.py potential.dat $(ls Psi_*.dat) 
./plot_iso.py potential.dat $(ls Psi_*.dat)
