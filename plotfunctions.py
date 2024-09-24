#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib

def tikzplotlib_fix_ncols(obj):
    """
    workaround for matplotlib 3.6 renamed legend's _ncol to _ncols, which breaks tikzplotlib
    """
    if hasattr(obj, "_ncols"):
        obj._ncol = obj._ncols
    for child in obj.get_children():
        tikzplotlib_fix_ncols(child)

def evaluate_function(func, x_range):
    """
    Evaluates the function over the provided x_range
    """
    return func(x_range)

if __name__ == '__main__':
    
    # Define your custom functions here
    def f(x):
        return -5 * np.exp(-(x - 3.5)**2 / 2) - 5 * np.exp(-(x - 6.5)**2 / 2)

    def g(x):
        return 2.2779 * (x - 5 - 1.46)**2 - 5.05

    def h(x):
        return 2.2779 * (x - 5 + 1.46)**2 - 5.05
    
    def i(x):
        return 0.6 * (x-5)**2 - 6.8

    # Define x range for plotting the functions
    x_range = np.linspace(-0.5, 10.5, 1000)  # Matching x-range from the TikZ code
    
    plt.figure(figsize=(10, 6))  # adjust the figure size (width, height)
    
    # Plot f(x) in color #2E7D32
    y_f = evaluate_function(f, x_range)
    plt.plot(x_range, y_f, label=r'$V(x)$', color='#2E7D32')

    # Plot g(x) in color #1565C0
    # y_g = evaluate_function(g, x_range)
    # plt.plot(x_range, y_g, label=r'$a_1(x)$', color='#1565C0')

    # Plot h(x) in color #D32F2F
    # y_h = evaluate_function(h, x_range)
    # plt.plot(x_range, y_h, label=r'$a_2(x)$', color='#D32F2F')

    # Plot i(x) in color #FF9900
    y_h = evaluate_function(i, x_range)
    plt.plot(x_range, y_h, label=r'$a(x)$', color='#FF9900')

    # Set the axis limits to match the TikZ plot
    plt.xlim([-0.5, 10.5])
    plt.ylim([-7.31065775681879, 0.241430029027375])

    # Add labels and title
    plt.xlabel('x')  # add label for x-axis
    plt.ylabel('y')  # add label for y-axis
    plt.title('Approximation with one single parabola')  # add title for the plot

    # Add legend to the plot
    plt.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

    plt.tight_layout()  # adjust layout to prevent clipping

    tikzplotlib_fix_ncols(plt.gcf())  # call the hack to fix the issue of the deprecated _ncol attribute being called by tikzplotlib

    tikzplotlib.save('plot.tex')  # save the plot as a .tex file
    plt.show()  # show the plot
