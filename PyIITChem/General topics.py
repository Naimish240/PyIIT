# -- General Topics --
# Includes concentration terms of mole fraction, molality, and normality
# along with common oxidation-reduction concepts

'''___________________________________________________________________________________________________________________'''

#periodic table

# pylint: disable=bad-whitespace
periodic_table = {
    # number: name symbol common_ions uncommon_ions
    # ion info comes from Wikipedia: list of oxidation states of the elements.
    0: ['Neutron',     'n',  [],         []],
    1: ['Hydrogen',    'H',  [-1, 1],    []],
    2: ['Helium',      'He', [],         [1, 2]],  # +1,+2  http://periodic.lanl.gov/2.shtml
    3: ['Lithium',     'Li', [1],        []],
    4: ['Beryllium',   'Be', [2],        [1]],
    5: ['Boron',       'B',  [3],        [-5, -1, 1, 2]],
    6: ['Carbon',      'C',  [-4, -3, -2, -1, 1, 2, 3, 4], []],
    7: ['Nitrogen',    'N',  [-3, 3, 5], [-2, -1, 1, 2, 4]],
    8: ['Oxygen',      'O',  [-2],       [-1, 1, 2]],
    9: ['Fluorine',    'F',  [-1],       []],
    10: ['Neon',       'Ne', [],         []],
    11: ['Sodium',     'Na', [1],        [-1]],
    12: ['Magnesium',  'Mg', [2],        [1]],
    13: ['Aluminum',   'Al', [3],        [-2, -1, 1, 2]],
    14: ['Silicon',    'Si', [-4, 4],    [-3, -2, -1, 1, 2, 3]],
    15: ['Phosphorus', 'P',  [-3, 3, 5], [-2, -1, 1, 2, 4]],
    16: ['Sulfur',     'S',  [-2, 2, 4, 6],    [-1, 1, 3, 5]],
    17: ['Chlorine',   'Cl', [-1, 1, 3, 5, 7], [2, 4, 6]],
    18: ['Argon',      'Ar', [],         []],
    19: ['Potassium',  'K',  [1],        [-1]],
    20: ['Calcium',    'Ca', [2],        [1]],
    21: ['Scandium',   'Sc', [3],        [1, 2]],
    22: ['Titanium',   'Ti', [4],        [-2, -1, 1, 2, 3]],
    23: ['Vanadium',   'V',  [5],        [-3, -1, 1, 2, 3, 4]],
    24: ['Chromium',   'Cr', [3, 6],     [-4, -2, -1, 1, 2, 4, 5]],
    25: ['Manganese',  'Mn', [2, 4, 7],  [-3, -2, -1, 1, 3, 5, 6]],
    26: ['Iron',       'Fe', [2, 3, 6],  [-4, -2, -1, 1, 4, 5, 7]],
    27: ['Cobalt',     'Co', [2, 3],     [-3, -1, 1, 4, 5]],
    28: ['Nickel',     'Ni', [2],        [-2, -1, 1, 3, 4]],
    29: ['Copper',     'Cu', [2],        [-2, 1, 3, 4]],
    30: ['Zinc',       'Zn', [2],        [-2, 1]],
    31: ['Gallium',    'Ga', [3],        [-5, -4, -2, -1, 1, 2]],
    32: ['Germanium',  'Ge', [-4, 2, 4], [-3, -2, -1, 1, 3]],
    33: ['Arsenic',    'As', [-3, 3, 5], [-2, -1, 1, 2, 4]],
    34: ['Selenium',   'Se', [-2, 2, 4, 6], [-1, 1, 3, 5]],
    35: ['Bromine',    'Br', [-1, 1, 3, 5], [4, 7]],
    36: ['Krypton',    'Kr', [2],        []],
    37: ['Rubidium',   'Rb', [1],        [-1]],
    38: ['Strontium',  'Sr', [2],        [1]],
    39: ['Yttrium',    'Y',  [3],        [1, 2]],
    40: ['Zirconium',  'Zr', [4],        [-2, 1, 2, 3]],
    41: ['Niobium',    'Nb', [5],        [-3, -1, 1, 2, 3, 4]],
    42: ['Molybdenum', 'Mo', [4, 6],     [-4, -2, -1, 1, 2, 3, 5]],
    43: ['Technetium', 'Tc', [4, 7],     [-3, -1, 1, 2, 3, 5, 6]],
    44: ['Ruthenium',  'Ru', [3, 4],     [-4, -2, 1, 2, 5, 6, 7, 8]],
    45: ['Rhodium',    'Rh', [3],        [-3, -1, 1, 2, 4, 5, 6]],
    46: ['Palladium',  'Pd', [2, 4],     [1, 3, 5, 6]],
    47: ['Silver',     'Ag', [1],        [-2, -1, 2, 3, 4]],
    48: ['Cadmium',    'Cd', [2],        [-2, 1]],
    49: ['Indium',     'In', [3],        [-5, -2, -1, 1, 2]],
    50: ['Tin',        'Sn', [-4, 2, 4], [-3, -2, -1, 1, 3]],
    51: ['Antimony',   'Sb', [-3, 3, 5], [-2, -1, 1, 2, 4]],
    52: ['Tellurium',  'Te', [-2, 2, 4, 6], [-1, 1, 3, 5]],
    53: ['Iodine',     'I',  [-1, 1, 3, 5, 7], [4, 6]],
    54: ['Xenon',      'Xe', [2, 4, 6],  [8]],
    55: ['Cesium',     'Cs', [1],        [-1]],
    56: ['Barium',     'Ba', [2],        [1]],
    57: ['Lanthanum',  'La', [3],        [1, 2]],
    58: ['Cerium',     'Ce', [3, 4],     [2]],
    59: ['Praseodymium', 'Pr', [3],      [2, 4, 5]],
    60: ['Neodymium',  'Nd', [3],        [2, 4]],
    61: ['Promethium', 'Pm', [3],        [2]],
    62: ['Samarium',   'Sm', [3],        [2]],
    63: ['Europium',   'Eu', [2, 3],     []],
    64: ['Gadolinium', 'Gd', [3],        [1, 2]],
    65: ['Terbium',    'Tb', [3],        [1, 2, 4]],
    66: ['Dysprosium', 'Dy', [3],        [2, 4]],
    67: ['Holmium',    'Ho', [3],        [2]],
    68: ['Erbium',     'Er', [3],        [2]],
    69: ['Thulium',    'Tm', [3],        [2]],
    70: ['Ytterbium',  'Yb', [3],        [2]],
    71: ['Lutetium',   'Lu', [3],        [2]],
    72: ['Hafnium',    'Hf', [4],        [-2, 1, 2, 3]],
    73: ['Tantalum',   'Ta', [5],        [-3, -1, 1, 2, 3, 4]],
    74: ['Tungsten',   'W',  [4, 6],     [-4, -2, -1, 1, 2, 3, 5]],
    75: ['Rhenium',    'Re', [4],        [-3, -1, 1, 2, 3, 5, 6, 7]],
    76: ['Osmium',     'Os', [4],        [-4, -2, -1, 1, 2, 3, 5, 6, 7, 8]],
    77: ['Iridium',    'Ir', [3, 4],     [-3, -1, 1, 2, 5, 6, 7, 8, 9]],
    78: ['Platinum',   'Pt', [2, 4],     [-3, -2, -1, 1, 3, 5, 6]],
    79: ['Gold',       'Au', [3],        [-3, -2, -1, 1, 2, 5]],
    80: ['Mercury',    'Hg', [1, 2],     [-2, 4]],  # +4  doi:10.1002/anie.200703710
    81: ['Thallium',   'Tl', [1, 3],     [-5, -2, -1, 2]],
    82: ['Lead',       'Pb', [2, 4],     [-4, -2, -1, 1, 3]],
    83: ['Bismuth',    'Bi', [3],        [-3, -2, -1, 1, 2, 4, 5]],
    84: ['Polonium',   'Po', [-2, 2, 4], [5, 6]],
    85: ['Astatine',   'At', [-1, 1],    [3, 5, 7]],
    86: ['Radon',      'Rn', [2],        [6]],
    87: ['Francium',   'Fr', [1],        []],
    88: ['Radium',     'Ra', [2],        []],
    89: ['Actinium',   'Ac', [3],        []],
    90: ['Thorium',        'Th', [4],    [1, 2, 3]],
    91: ['Protactinium',   'Pa', [5],    [3, 4]],
    92: ['Uranium',        'U',  [6],    [1, 2, 3, 4, 5]],
    93: ['Neptunium',      'Np', [5],    [2, 3, 4, 6, 7]],
    94: ['Plutonium',      'Pu', [4],    [2, 3, 5, 6, 7]],
    95: ['Americium',      'Am', [3],    [2, 4, 5, 6, 7]],
    96: ['Curium',         'Cm', [3],    [4, 6]],
    97: ['Berkelium',      'Bk', [3],    [4]],
    98: ['Californium',    'Cf', [3],    [2, 4]],
    99: ['Einsteinium',    'Es', [3],    [2, 4]],
    100: ['Fermium',       'Fm', [3],    [2]],
    101: ['Mendelevium',   'Md', [3],    [2]],
    102: ['Nobelium',      'No', [2],    [3]],
    103: ['Lawrencium',    'Lr', [3],    []],
    104: ['Rutherfordium', 'Rf', [4],    []],
    105: ['Dubnium',       'Db', [5],    []],
    106: ['Seaborgium',    'Sg', [6],    []],
    107: ['Bohrium',       'Bh', [7],    []],
    108: ['Hassium',       'Hs', [8],    []],
    109: ['Meitnerium',    'Mt', [],     []],
    110: ['Darmstadtium',  'Ds', [],     []],
    111: ['Roentgenium',   'Rg', [],     []],
    112: ['Copernicium',   'Cn', [2],    []],
    113: ['Nihonium',      'Nh', [],     []],
    114: ['Flerovium',     'Fl', [],     []],
    115: ['Moscovium',     'Mc', [],     []],
    116: ['Livermorium',   'Lv', [],     []],
    117: ['Tennessine',    'Ts', [],     []],
    118: ['Oganesson',     'Og', [],     []],
}
# pylint: enable=bad-whitespace

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
        
        
        
        

















    
