# -- General Topics --
# Includes concentration terms of mole fraction, molality, and normality
# along with common oxidation-reduction concepts

'''___________________________________________________________________________________________________________________'''


# Mole Fraction
# Takes a dictionary of components and their respective number of moles as input,
# and returns a dictionary of the components and their respective mole fractions.

def mole_fraction(components):
    #dictionary to be returned
    molefrac={}
    #sum of total moles in container
    s=0
    #loop to calculate total number of molecules in container
    for mol in component.values():
        s+=mol
    #for loop to iterate through the molecules
    for molecule in components.keys():
        #divide moles of component by total moles
        components[molecule]/=s
    #return dictionary of components and their respective mole fractions
    return components

# Empirical Formula
# Takes dictionary of elements and their % as input, returns string of molecule
def empirical_formula(table,VD=None):
    final_table={}
    '''   col 1           col 2        col 3                   col 4                col 5                 col 6
        Element/symbol  percentage   atomic number    percentage/atomic mass     lowest ratio        emperical units
                                                             aka moles

        if VD==True, then mass=2*vd, emperical mass= emperical units*element.
        n=mass/emperical mass
        return element emperical units*n
    '''
    
    # percentage/atomic number == molefraction*100/atomic_mass
    
    col_4 = {}
    col_5 = 0
    
    for element in table.keys():
        #fill column 4
        col_4[element] = table[element]/periodic_table[element][1] # periodic_table[element] = [atomic_number][mass_number][full_name]
        #updatet column 5
        if col_4[element]<col_5:
            col_5 = col_4[element]
            
    col_6 = {}
    # col 6 is filled
    
    for element in col_4.keys:
        col_6[element] = round(col_4/col_5)

    # V.D. is given
    n=1 # default
    
    if VD:
        mass=VD*2
        emperical_mass=0
        #function to calculate empirical mass
        for element in col_6.keys():
            emperical_mass+=col_6[element]*periodic_table[element][1]
        n = mass/emperical_mass

    #return string
    compd=''
    for element in table.keys():
        compd+=element+str(n*col_6[element])

    return compd
'''___________________________________________________________________________________________________________________'''

# Molarity
# moles of solute per litre of solution
# takes dictionary and volume of solution as input, and returns float

def molarity(table,volume):
    pass
        
        
        
        

















    
