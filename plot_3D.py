#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib import cm
from scipy.interpolate import griddata
import math

if __name__ == '__main__':
    args = sys.argv[1:]  # get all the arguments
    fig = plt.figure(figsize=(10, 6))  # adjust the figure size (width, height)
    

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file
        #too_large = (data[:,0] < 10) & (data[:,0] > 7) & (data[:,1] > 7) & (data[:,1] < 10)
        x = data[:, 0]
        y = data[:, 1]
        z = data[:, 2]
        f = data[:, 3]

        n_plots = 7
        for i in range(n_plots):
            ax = fig.add_subplot(math.ceil(math.sqrt(n_plots)), math.ceil(math.sqrt(n_plots)), i+1)

            if n_plots > 1:
                current_z = z[round(i*(len(z)-1)/(n_plots-1))]
            else:
                current_z = z[round(len(z)/2)]

            indices = (z == current_z)
            current_x = x[indices]
            current_y = y[indices]
            current_f = f[indices]

            # Create grid values first.
            xi = np.linspace(min(x), max(x), 100)
            yi = np.linspace(min(y), max(y), 100)
            X, Y = np.meshgrid(xi, yi)

            # Interpolate Z values on grid.
            F = griddata((current_x, current_y), current_f, (X, Y))

            surf = ax.contourf(X, Y, F)
            plt.colorbar(surf)  # add a color bar to the plot
            # im = plt.imshow(z.reshape(100, 100))

            ax.set_xlabel('x')  # add label for x-axis
            ax.set_ylabel('y')  # add label for y-axis
            ax.set_title(f"$V(x,y,z={current_z})$")  # add title for the plot

    #ax.legend()  # add legend to the plot
    
    plt.tight_layout()  # adjust layout to prevent clipping
    #tikzplotlib.save('plot.tex')  # save the plot as a .tex file
    plt.show()  # show the plot
    