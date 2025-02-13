#!/bin/bash
rm -f *.dat *.tex 
cd ../build_eigensolver/ && make -j8 && cd -
#../build/src/examples/1dharmonic
../build_eigensolver/src/AutomatizedEigensolver/eigensolver
python plot_1D.py $(ls Psi_*.dat) potential.dat
#./plot_1D_2.py $(ls Psi*.dat) potential.dat 