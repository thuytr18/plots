# -----------------------------------------------------------------------------------------
# This script is used to build and run the Eigensolver project and plot the results. 
# Before running this script, make sure that the project has been built successfully.
# The script assumes that the project has been built in the build directory and 
# the python script for plotting is located in the project_directory/Eigensolver/plot.
# -----------------------------------------------------------------------------------------

#!/bin/bash

# Navigate to the build directory
BUILD_DIR="../build_eigensolver"  # Change this directory to your build directory of the project

echo "Cleaning up old files"
rm -f "$BUILD_DIR"/*.dat "$BUILD_DIR"/*.tex

echo "Building the project"
(cd "$BUILD_DIR" && make -j8 && cd -) || { echo "Build failed."; exit 1; }

echo "Running Eigensolver..."
(cd "$BUILD_DIR" && ./Eigensolver) || { echo "Eigensolver execution failed."; exit 1; }

# Plot results
# this is the directory to the python script that plots the results, located in the project_directory/Eigensolver/plot
PLOT_SCRIPT="../automatized_eigensolver/Eigensolver/plot/plot_1D.py"  # plot_1D.py can be replaced with plot_1D_2.py for a different plot style 

if ls "$BUILD_DIR"/Psi_*.dat 1> /dev/null 2>&1 && [ -f "$BUILD_DIR/potential.dat" ]; then
    python3 "$PLOT_SCRIPT" "$BUILD_DIR"/Psi_*.dat "$BUILD_DIR/potential.dat" || { echo "Plotting failed."; exit 1; }
else
    echo "Error: Required data files not found in $BUILD_DIR."
    exit 1
fi

echo "All steps completed successfully!"