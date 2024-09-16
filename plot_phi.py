#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import re


if __name__ == '__main__':

    args = sys.argv[1:]  # get all the arguments -> first argument is the potential file, second previous wavefunctions, third current wavefunctions

    #print(args)

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file

        x = data[:, 0]
        y = data[:, 1]
        
        if re.match(r'(.*/)?phi-\d+-\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)
            plt.plot(x, y, label=r'$\phi_{%s.%s}$' % (energylevel[-2], energylevel[-1]))
        elif re.match(r'(.*/)?phi-\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            plt.plot(x, y, label=r'$\phi_{%s}$' % energylevel)  # plot the data with label as filename
        elif re.match(r'.*Potential.dat', arg):
            plt.plot(x, y, label='V(x) ')  # plot the data with label as filename
        elif re.match(r'.*Psi_\d+.dat', arg):
            energylevel = re.findall(r'\d+', arg)[0]
            plt.plot(x, y, label=r'$\Psi_{%s}$' % energylevel)
        else:
            plt.plot(x, y, label=arg)
    
    plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))  # add legend to the plot
    
    plt.xlabel('x')  # add label for x-axis
    plt.ylabel('y')  # add label for y-axis
    plt.title('Energy levels')  # add title for the plot

    # set the x-axis limits
    #plt.ylim([-10.5, 2])       # only for Gaussian Potential
    #plt.ylim([-5.5, 1])       # only for Double Well Potential
    plt.ylim([-10.5, 2])       # only for Exponential Potential
    #plt.ylim([-5.5, 2])       # only for Morse Potential

    png_filename = args[-1].replace('.dat', '.png')
    plt.savefig(png_filename, bbox_inches='tight')
    plt.close()

