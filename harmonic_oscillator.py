#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial, hermite
import sys

def harmonic_wavefunction(x, n, m, omega, hbar):
    prefactor = 1 / np.sqrt(2**n * factorial(n)) * (m * omega/(np.pi * hbar))**(1/4)
    exponent = -m * omega * x**2 / (2 * hbar)

    return prefactor * np.exp(exponent) * hermite(n)(x)

# Parameter of the harmonic oscillator
m = 1.0  # Mass
omega = 1.0  # circular frequency
hbar = 1.0  # reduced Planck constant

# Range of x values
x_values = np.linspace(-5, 5, 1000)

# Create figure 1
plt.figure(1)
plt1 = plt.subplot(1, 1, 1)

# Plot Wavefunctions for n=0,1,2,3,4
for n in range(5):
    psi_n = harmonic_wavefunction(x_values, n, m, omega, hbar)
    plt1.plot(x_values, psi_n, label=f'n={n}', linestyle='dashed')

args_p = [arg for arg in sys.argv[1:] if arg.startswith('phi')] # get all the arguments
for arg in args_p:
    data = np.loadtxt(arg)  # load the data from the file
    x = data[:,0] - 10 
    y = data[:,1] 
    plt1.plot(x, y, label=arg)  # plot the data

plt1.set_title('Harmonic Oscillator Wavefunctions before Transformation')
plt1.set_xlabel('x')
plt1.set_ylabel('Psi(x)')
plt1.legend()
plt1.grid(True)

# Create figure 1
plt.figure(2)
plt2 = plt.subplot(1, 1, 1)

for n in range(5):
    psi_n = harmonic_wavefunction(x_values, n, m, omega, hbar)
    plt2.plot(x_values, psi_n, label=f'n={n}', linestyle='dashed')

args_n= [arg for arg in sys.argv[1:] if arg.startswith('n_phi')]
for arg in args_n:
    data = np.loadtxt(arg)
    x = data[:, 0] - 10
    y = data[:, 1]
    plt2.plot(x, y, label=arg) 

plt2.set_title('Harmonic Oscillator Wavefunctions after Transformation')
plt2.set_xlabel('x')
plt2.set_ylabel('Psi(x)')
plt2.legend()
plt2.grid(True)

plt.tight_layout()
plt.show()



