# -- General Topics --
# Includes concentration terms of mole fraction, molality, molarity, etc

'''___________________________________________________________________________________________________________________'''

# Import statements

from __future__ import absolute_import
from __future__ import print_function

from Periodic_Table import periodic_table


'''___________________________________________________________________________________________________________________'''

# Mole Fraction
# Takes a dictionary of components and their respective number of moles as input,
# and returns a dictionary of the components and their respective mole fractions.

def mole_fraction(components):
    #dictionary to be returned
    #sum of total moles in container
    s  =  0
    #loop to calculate total number of molecules in container
    for mol in components.values():
        s+=mol
    #for loop to iterate through the molecules
    for molecule in components.keys():
        #divide moles of component by total moles
        components[molecule]/=s
    #return dictionary of components and their respective mole fractions
    return components

'''___________________________________________________________________________________________________________________'''

# Empirical Formula
# Takes dictionary of elements and their % as input, returns string of molecule

def empirical_formula(table,VD  =  None):
    '''
            col 1           col 2        col 3                   col 4                col 5                 col 6
        Element/symbol  percentage   atomic number    percentage/atomic mass     lowest ratio        emperical units
                                                             aka moles

        if VD  =    =  True, then mass  =  2*vd, emperical mass  =   emperical units*element.
        n  =  mass/emperical mass
        return element emperical units*n
    '''
    
    # percentage/atomic number==molefraction*100/atomic_mass
    
    col_4 = {}
    col_5 = 0
    
    for element in table.keys():
        #fill column 4
        col_4[element]  =  table[element]/periodic_table[element][1] # periodic_table[element] = [atomic_number][mass_number][full_name]
        #updatet column 5
        if col_4[element]<col_5:
            col_5= col_4[element]
            
    col_6={}
    # col 6 is filled
    
    for element in col_4.keys():
        col_6[element]= round(col_4/col_5)

    # V.D. is given
    n=1 # default
    
    if VD:
        mass= VD*2
        emperical_mass = 0
        #function to calculate empirical mass
        for element in col_6.keys():
            emperical_mass+=col_6[element]*periodic_table[element][1]
        n= mass/emperical_mass

    #return string
    compd=''
    for element in table.keys():
        compd+=element+str(n*col_6[element])

    return compd
'''___________________________________________________________________________________________________________________'''

# Molar Mass
# Calculates molar mass of compound
# Takes dictionary as input and returns a float
# dictionary contains key-order pair of element name (NOT SYMBOL) and its subscript

def molar_mass(compound):
    mol_mass=0.0
    for element in compound.keys():
        for i in periodic_table:
            if i[1].lower()==element.lower():
                mol_mass+=periodic_table[i][3]
    return mol_mass


'''___________________________________________________________________________________________________________________'''

# Moles
# Calculates moles of a compound, when mass and compound is given
# Takes dictionary and mass taken as input and returns a float
# dictionary contains key-order pair of element name (NOT SYMBOL) and its subscript

def moles_of_compound(compound,mass):
    mol_mass=molar_mass(compound)
    return mass/mol_mass

'''___________________________________________________________________________________________________________________'''


# Molarity
# Moles of solute per litre of solution
# takes dictionary, mass taken and volume(in liters) of solution as input, and returns float
# dictionary contains key-order pair of element name (NOT SYMBOL) and its subscript
# formula : Moles(of solute)/volume(of solution)

def molarity(compound,volume,mass=0,moles=0):
    # mass given
    if mass:
        # Calculates moles       
        return moles_of_compound(compound,mass)/volume
    # Moles given
    elif moles:
        return moles/volume
    else:
        print("Error!")
        return None
'''___________________________________________________________________________________________________________________'''

# Molality
# Moles per kilogram of solution
# takes dictionary, mass of substance taken and mass of solvent as input, and returns float
# dictionary contains key-order pair of element name (NOT SYMBOL) and its subscript
# formula : Moles(of solute)/mass(of solvent)

def molality(compound,solv_mass,subs_moles=0.0,subs_mass=0.0):
    # Moles given
    if subs_moles:
        return subs_moles/solv_mass
    # Mass given
    elif subs_mass:
        return moles_of_compound(compound,subs_mass)/solv_mass

'''___________________________________________________________________________________________________________________'''

# Function to convert molarity into molality
# Takes molarity, density and weight of solute and returns a float

def molar_to_molal(molar,density,wt_of_solute):
    # Returns Molality
    return molar/(density-(molar*wt_of_solute))

'''___________________________________________________________________________________________________________________'''

# Converts Molality into Molarity
# Takes molality, density and weight of solute and returns a float

def molal_to_molar(molal,density,wt_of_solute):
    # Returns Molarity
    return molal*(density-wt_of_solute)

'''___________________________________________________________________________________________________________________'''  
    
    
        
        
        
        

















    
