#!/bin/env python3
import plotly.graph_objects as go
import numpy as np

import sys
from matplotlib import cm
from scipy.interpolate import griddata
import math

if __name__ == '__main__':
    args = sys.argv[1:]  # get all the arguments

    for arg in args:
        data = np.loadtxt(arg)  # load the data from the file
        #too_large = (data[:,0] < 10) & (data[:,0] > 7) & (data[:,1] > 7) & (data[:,1] < 10)
        x = data[:, 0]
        y = data[:, 1]
        z = data[:, 2]
        f = data[:, 3]


        fig = go.Figure(data=go.Isosurface(
            x=x,
            y=y,
            z=z,
            value=f,
            opacity=0.2,
            isomin=min(f)+0.05*(max(f) - min(f)),
            isomax=max(f)-0.05*(max(f) - min(f)),
            surface_count=5,
            caps=dict(x_show=False, y_show=False)
            ))
        fig.show()