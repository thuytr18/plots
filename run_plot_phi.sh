#!/bin/bash 
# $1 is directory containing the data
counter=0
for directory in "$1"*; do  # loop over all directories
    energylevel=$(echo $directory | sed -r 's/.*_([0-9]*).*/\1/') # extract energy level from directory name
    for i in $(ls "$directory"/phi-*.dat); do # loop over all iterations of the wavefunction
        echo $i 
        ./plot_phi.py $(ls "$directory"/../../*Potential.dat) ${PsiCollection[@]} $i  # first argument is potential, second is previous wavefunction, third is current wavefunction
    done
    PsiCollection[$counter]="$(ls "$directory"/../../*Psi/Psi_"$energylevel".dat)"  # update list of wavefunctions
    ./plot_phi.py "$(ls "$directory"/../../*Potential.dat)" "${PsiCollection[@]}"
    mv "$(ls "$directory"/../../*Psi/Psi_"$energylevel".png)" "$directory"/psi_"$energylevel".png
    counter=$((counter+1))
done

