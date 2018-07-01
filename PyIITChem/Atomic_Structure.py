# -- Atomic Structure --

'''

This program contains the functions related with the chapter of atomic structure 
They include:
    1. Calculation of Bohr Radius
    2. Calculation of energy levels for hydrogen like atoms
    3. Calculation of velocity, etc.

'''
'''___________________________________________________________________________________________________________________'''

# Import statements

from __future__ import absolute_import
from __future__ import print_function

from Periodic_Table import periodic_table as pt
from Periodic_Table import constants 
from Periodic_Table import atomic_config

from math import pi

'''___________________________________________________________________________________________________________________'''

# Function to calculate angular momentum of an electron in nth bohr orbit
# Takes 'n' as input and returns a float

def bohr_angluar_momentum(n):
    # Formula: mvr=nh/2pi
    return (n*constants['h'])/(2*pi)

'''___________________________________________________________________________________________________________________'''

# Function to calculate bohr radius
# Takes 'n' and 'z' as inputs, and returns a float

def bohr_radius(n,z=1):
    # Formula: r=(0.0529 n^2/z) * 10E-10 meters
    return ((0.0529*(n**2))/z)*10E-10 # returns in meters

'''___________________________________________________________________________________________________________________'''

# Function to calcualte velocity of nth bohr radius
# Takes 'n' and 'z' as inputs, and returns a float

def bohr_velocity(n,z=1):
    # Formula: v=(2.18*n/z)*10E6 meters per second
    return ((2.18*n)/z)*10E6

'''___________________________________________________________________________________________________________________'''

# Function to calculate energy of nth bohr orbit
# Takes 'n' and 'z' as inputs, and returns a float

def bohr_energy(n,unit='eV',z=1):
    # Formula: E = -13.6 z^2/n^2 eV
    return -13.6*(z^2/n^2)

'''___________________________________________________________________________________________________________________'''

# Function to calculate the deBroglie wavelength of a particle
# Takes momentum as input, and returns a float

def de_broglie_wavelength(p):
    # Formula: wavelength = h/p
    return constants['h']/p

'''___________________________________________________________________________________________________________________'''

