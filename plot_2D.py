#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
from matplotlib import cm
from scipy.interpolate import griddata

if __name__ == '__main__':
    args = sys.argv[1:]  # get all the arguments
    fig = plt.figure(figsize=(10, 6))  # adjust the figure size (width, height)
    ax = fig.add_subplot(111, projection='3d')

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file
        #too_large = (data[:,0] < 10) & (data[:,0] > 7) & (data[:,1] > 7) & (data[:,1] < 10)
        x = data[:, 0]
        y = data[:, 1]
        z = data[:, 2]

        # Create grid values first.
        xi = np.linspace(min(x), max(x), 100)
        yi = np.linspace(min(y), max(y), 100)
        X, Y = np.meshgrid(xi, yi)

        # Interpolate Z values on grid.
        Z = griddata((x, y), z, (X, Y), method='cubic')

        surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis,
                               linewidth=0, antialiased=False)
        # im = plt.imshow(z.reshape(100, 100))

    ax.set_xlabel('x')  # add label for x-axis
    ax.set_ylabel('y')  # add label for y-axis
    ax.set_zlabel('z')  # add label for z-axis
    ax.set_title('$\Psi(x)$')  # add title for the plot

    ax.legend()  # add legend to the plot
    
    plt.colorbar(surf)  # add a color bar to the plot
    plt.tight_layout()  # adjust layout to prevent clipping
    #tikzplotlib.save('plot.tex')  # save the plot as a .tex file
    plt.show()  # show the plot
    