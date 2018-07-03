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

from PyIITChem.Periodic_Table import periodic_table as pt
from PyIITChem.Periodic_Table import constants 

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

def bohr_energy(n,z=1):
    # Formula: E = -13.6 z^2/n^2 eV
    return -13.6*(z^2/n^2)

'''___________________________________________________________________________________________________________________'''

# Function to calculate the deBroglie wavelength of a particle
# Takes momentum as input, and returns a float

def de_broglie_wavelength(p):
    # Formula: wavelength = h/p
    return constants['h']/p

'''___________________________________________________________________________________________________________________'''

# Function to calculate the wavelength of energy emitted when electron transitions from one energy state to another
# Takes 'n' and 'z' as inputs, and returns a float

def photon_from_atom(n1,n2,z=1):
    e1=bohr_energy(n1,z)
    e2=bohr_energy(n2,z)
    e=e1-e2
    wavelength=(12400/e)*10E-10
    return wavelength # wavelength > 0 : emitted, else absorbed

'''___________________________________________________________________________________________________________________'''

# Rydberg's formula
# Returns series name and value of wave number

def Rydberg(n1,n2,z=1):
    wave_number = (constants['rydberg']*z**2)*((n1**(-2)-n2**(-2)))
    if n1==1:
        return [wave_number,'Lymann']
    elif n1==2:
        return [wave_number,'Balmer']
    elif n1==3:
        return [wave_number,'Paschen']
    elif n1==4:
        return [wave_number,'Brackett']
    elif n1==5:
        return [wave_number,'Pfund']
    elif n1==6:
        return [wave_number,'Humpherey']
    else:
        return [wave_number,None]

'''___________________________________________________________________________________________________________________'''


# Function to return Electronic Configuraton of an element
# Takes atomic number as input, returns string

def atomic_config(num): # num = atomic number = number of electrons (if neutral)
    # s orbital : 2 electrons
    # p orbital : 6 electrons
    # d orbital : 10 electrons
    # f orbital : 14 electrons
    
    order=['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p','8s','6f','7d','8p','9s']
    
    # Exceptions (atomic, but valid for configurations too):
    if num == 24: # Chromium 
        return '1s2 2s2 2p6 3s2 3p6 4s1 3d5'
    elif num == 29: # Copper
        return '1s2 2s2 2p6 3s2 3p6 4s1 3d10'
    elif num == 41: # Niobium
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4'
    elif num == 42: # Molybdenum
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5'
    elif num == 44: # Ruthenium
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7'
    elif num == 45: # Rodhium
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8'
    elif num == 46: # Palladium
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10'
    elif num == 47: # Silver
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10'
    elif num == 78: # Platinum
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10 5s2 5p6 6s1 4f14 5d9'
    elif num == 79: # Gold
        return '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10 5s2 5p6 6s1 4f14 5d10'
    
    config=''
    i=0
    # While loop for others
    while num>0: 
        ele=0
        if 's' in order[i]: # s orbital
            ele=2
        elif 'p' in order[i]: # p orbital
            ele=6
        elif 'd' in order[i]: # d orbital
            ele=10
        else: # f orbital
            ele=14
        
        if num-ele>0:
            config+=order[i]+str(ele)+' '
            num-=ele # reduce the electrons from the total number
            i+=1 # increases i by one
            continue
        else:
            config+=order[i]+str(num)+' '
            break
    return config

'''___________________________________________________________________________________________________________________'''
