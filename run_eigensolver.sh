#!/bin/bash
rm -f *.dat *.tex 
cd ../build/ && make -j8 && cd -
#../build/src/examples/1dharmonic
../build/src/bachelorthesis/eigensolver
./plot_1D.py $(ls Psi_*.dat) potential.dat
#./plot_1D_2.py $(ls Psi*.dat) potential.dat 
