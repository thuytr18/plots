# ----------------------------------------------------------------------------------------------------
# Description:
# This script is used to plot the data from the files provided as arguments.
# The files should be .dat files created by the Eigensolver.
# This script can be executed from the command line as follows: python3 plot_1D.py file1.dat file2.dat ...
# ----------------------------------------------------------------------------------------------------

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import re
import tikzplotlib

def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols, which breaks tikzplotlib
    """
    if hasattr(obj, "_ncols"):
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)

if __name__ == '__main__':

    args = sys.argv[1:]  # get all the arguments

    plt.figure(figsize=(10, 6))  # adjust the figure size (width, height)

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file
        x = data[:, 0]
        y = data[:, 1]
        if(arg == 'potential.dat'):
            plt.plot(x, y, label='V(x)')  # plot the data with label as filename
        elif(re.match(r'Psi_\d+.dat', arg)):
            energylevel = re.findall(r'\d+', arg)[0]
            plt.plot(x, y, label=r'$\Psi_{%s}$' % energylevel)  # plot the data with label as filename
        elif re.match(r'(.*/)?phi-\d+-\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0:2]
            plt.plot(x, y, label=r'$\phi_{%s.%s}$' % (energylevel[0], energylevel[1]))
        elif re.match(r'(.*/)?phi-\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            plt.plot(x, y, label=r'$\phi_{%s}$' % energylevel)
        elif(arg == 'approximation.dat'):
            plt.plot(x, y, label=r'$V^{H}(x)$')  # plot the data with label as filename
            # only for double well potential
        elif arg == 'approximation1.dat':
            plt.plot(x, y, label=r'$V^{H}_{1}(x)$')  # plot the data with label as filename
        elif re.match(r'PsiApprox_\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            plt.plot(x, y, label=r'$\Psi_{%s}^{H}$' % energylevel)
        # only for double well potential
        elif re.match(r'PsiApprox1_\d+.dat', arg):
            match = re.search(r'(?<=_)\d+', arg)
            energylevel = match.group(0)
            plt.plot(x, y, label=r'$\Psi_{%s}^{H_{1}}$' % energylevel)
        elif (arg == 'rho.dat'):
            plt.plot(x, y, label=r'$\rho(x)$')
        elif (arg == 'charged_rho.dat'):
            plt.plot(x, y, label=r'$\rho_{charged}(x)$')
        else:
            plt.plot(x,y, label=arg)

    #plt.legend()  # add legend to the plot
    plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    #plt.ylim([-10.5, 0.5])  # set the y-axis limits
    
    plt.xlabel('x')  # add label for x-axis
    plt.ylabel('y')  # add label for y-axis
    plt.title('Energy levels')  # add title for the plot


    plt.tight_layout()  # adjust layout to prevent clipping


    tikzplotlib_fix_ncols(plt.gcf()) # call the hack to fix the issue of the deprecated _ncol attribute being called by tikzplotlib

    tikzplotlib.save('plot.tex')  # save the plot as a .tex file
    plt.show()  # show the plot
    