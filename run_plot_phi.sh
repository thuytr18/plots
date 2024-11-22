# ----------------------------------------------------------------------------------------
# This script is used to make .png files of the wavefunctions and the potential
# for each energy level. 
# With these .png files, the user can create a gif of the wavefunctions and the potential
# with the python script togif.py.
# ----------------------------------------------------------------------------------------


#!/bin/bash 
# $1 is directory containing the data

# Initialize counter for PsiCollection
counter=0
declare -a PsiCollection

# Iterate over all directories in the root folder
for directory in "$1"*; do
    # Extract energy level from the directory name (e.g., *_5 -> 5)
    energylevel=$(echo $directory | sed -r 's/.*_([0-9]*).*/\1/') 
    echo "Processing directory: $directory (Energy level: $energylevel)"

    # Loop over all phi-*.dat files in the current directory
    for wavefunction_file in "$directory"/phi-*.dat; do
        echo "Processing wavefunction file: $wavefunction_file"
        # Plot current wavefunction
        # first argument is potential, second is previous wavefunction, third is current wavefunction
        ./plot_phi.py $(ls "$directory"/../../*Potential.dat) ${PsiCollection[@]} $wavefunction_file
    done

    # Update the PsiCollection with the Psi file corresponding to the current energy level
    PsiCollection[$counter]="$(ls "$directory"/../../*_Psi/Psi_"$energylevel".dat)"

    # Plot the final wavefunction for the current Phi directory
    ./plot_phi.py "$(ls "$directory"/../../*Potential.dat)" "${PsiCollection[@]}"

    # Move the generated Psi plot to the current directory and rename it
    mv "$(ls "$directory"/../../*Psi/Psi_"$energylevel".png)" "$directory"/psi_"$energylevel".png

    # Increment the counter for PsiCollection
    counter=$((counter + 1))
done

