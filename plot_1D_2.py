#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import re
import tikzplotlib

if __name__ == '__main__':

    args = sys.argv[1:]  # get all the arguments

    # Create two separate figures
    #fig1, ax1 = plt.subplots(figsize=(10, 6))  # adjust the figure size (width, height)
    #fig2, ax2 = plt.subplots(figsize=(10, 6))  # adjust the figure size (width, height)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6)) 

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file
        x = data[:, 0]
        y = data[:, 1]
        if arg == 'potential.dat':
            ax1.plot(x, y, label='V(x)')  # plot the data with label as filename
        elif re.match(r'Psi_\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            ax1.plot(x, y, label='$\Psi_{%s}$' % energylevel)  # plot the data with label as filename
        elif arg == 'approximation.dat':
            ax2.plot(x, y, label='$V^{H}(x)$')  # plot the data with label as filename
        # only for double well potential
        elif arg == 'approximation1.dat':
            ax2.plot(x, y, label='$V^{H}_{1}(x)$')  # plot the data with label as filename
        elif re.match(r'PsiApprox_\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            ax2.plot(x, y, label='$\Psi_{%s}^{H}$' % energylevel)
        # only for double well potential
        elif re.match(r'PsiApprox1_\d+.dat', arg):
            match = re.search(r'(?<=_)\d+', arg)
            energylevel = match.group(0)
            ax2.plot(x, y, label='$\Psi_{%s}^{H_{1}}$' % energylevel)
        else:
            ax2.plot(x, y, label=arg)

    # Customize first plot
    ax1.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
    ax1.set_xlabel('x')  # add label for x-axis
    ax1.set_ylabel('y')  # add label for y-axis
    ax1.set_title('Energy levels')  # add title for the plot

    # Customize second plot
    ax2.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))
    #ax2.set_ylim([-7, 20])  # set the y-axis limits
    ax2.set_xlabel('x')  # add label for x-axis
    ax2.set_ylabel('y')  # add label for y-axis
    ax2.set_title('Energy levels 2')  # add title for the plot

    # Adjust layout for both figures
    #fig1.tight_layout()  # adjust layout to prevent clipping
    #fig2.tight_layout()  # adjust layout to prevent clipping
    plt.tight_layout()

    # Save the plots as .tex files
    #tikzplotlib.save('plot1.tex', figure=fig1)
    #tikzplotlib.save('plot2.tex', figure=fig2)
    tikzplotlib.save('plot_2.tex', figure=fig)

    # Show the plots
    plt.show()  # show both plots
