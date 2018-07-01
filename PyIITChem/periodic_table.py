# -- Periodic Table --

'''
    Module periodic table (upto element 109/index 108)
    Stores the periodic table in two forms:
        1. By group
        2. By Atomic Number
    Also contains the methods to return electronic configuration of the elements
    
    Sub atomic particles at the end (index 109 to 111)
'''

'''___________________________________________________________________________________________________________________'''


# Returns the elements sorted by atomic number, rather than group

def sorted_by_atomic_number(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i):
            if int(arr[i][2])<int(arr[j][2]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr

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

# For first 109 elements along with proton, neutron and electron at end

periodic_table = [
    
# symbol | name | atomic number(str) | atomic weight(amu)(str) | state | category | oxidation state(common) | oxidation state(rare) 

# Group 1 Alkali Metals
['H','Hydrogen','1','1.01','Gas','Alkali Metals',[-1, 1],None],
['Li','Lithium','3','6.94','Solid','Alkali Metals',[1],None],
['Na','Sodium','11','22.99','Solid','Alkali Metals',[1],[-1]],
['K','Potassium','19','39.10','Solid','Alkali Metals',[1],[-1]],
['Rb','Rubidium','37','85.47','Solid','Alkali Metals',[1],[-1]],
['Cs','Cesium','55','132.91','Solid','Alkali Metals',[1],[-1]],
['Fr','Francium','87','223.00','Solid','Alkali Metals',[1],None],
# Group 2 Alkali Earth Metals
['Be','Beryllium','4','9.01','Solid','Alkaline Earth Metals',[2],[1]],
['Mg','Magnesium','12','24.31','Solid','Alkaline Earth Metals',[2],[1]],
['Ca','Calcium','20','40.08','Solid','Alkaline Earth Metals',[2],[1]],
['Sr','Strontium','38','87.62','Solid','Alkaline Earth Metals',[2],[1]],
['Ba','Barium','56','137.33','Solid','Alkaline Earth Metals',[2],[1]],
['Ra','Radium','88','226.03','Solid','Alkaline Earth Metals',[2],None],
# Group 3
['Sc','Scandium','21','44.96','Solid','Transitional Metals',[3],[1,2]],
['Y','Yttrium','39','88.91','Solid','Transitional Metals',[3],[1,2]],
['La','Lanthanum','57','138.91','Solid','Transitional Metals',[3],[1,2]],
['Ac','Actinium','89','227.03','Solid','Transitional Metals',[3],None],
# Group 4
['Ti','Titanium','22','47.90','Solid','Transitional Metals',[4],[-2, -1, 1, 2, 3]],
['Zr','Zirconium','40','91.22','Solid','Transitional Metals',[4],[-2, 1, 2, 3]],
['Hf','Hafnium','72','178.49','Solid','Transitional Metals',[4],[-2, 1, 2, 3]],
['Rf','Rutherfordium','104','261.00','Synthetic','Transitional Metals',[4],None],
# Group 5
['V','Vanadium','23','50.94','Solid','Transitional Metals',[5],[-3, -1, 1, 2, 3, 4]],
['Nb','Niobium','41','92.91','Solid','Transitional Metals',[5],[-3, -1, 1, 2, 3, 4]],
['Ta','Tantalum','73','180.95','Solid','Transitional Metals',[5],[-3, -1, 1, 2, 3, 4]],
['Ha','Hahnium','105','262.00','Synthetic','Transitional Metals',[5],None],
# Group 6
['Cr','Chromium','24','51.99','Solid','Transitional Metals',[3, 6],[-4, -2, -1, 1, 2, 4, 5]],
['Mo','Molybdenum','42','95.94','Solid','Transitional Metals',[4, 6],[-4, -2, -1, 1, 2, 3, 5]],
['W','Tungsten','74','183.85','Solid','Transitional Metals',[4, 6],[-4, -2, -1, 1, 2, 3, 5]],
['Sg','Seaborgium','106','266.00','Synthetic','Transitional Metals',[6],None],
# Group 7
['Mn','Manganese','25','178.49','Solid','Transitional Metals',[2, 4, 7],[-3, -2, -1, 1, 3, 5, 6]],
['Tc','Technetium','43','178.49','Synthetic','Transitional Metals',[2, 4, 7],[-3, -1, 1, 3, 5, 6]],
['Re','Rhenium','75','178.49','Solid','Transitional Metals',[4],[-3, -1, 1, 3, 5, 6,7]],
['Bh','Bohrium','107','262.00','Synthetic','Transitional Metals',[7],None],
# Group 8
['Fe','Iron','26','55.85','Solid','Transitional Metals',[2, 3, 6],[-4, -2, -1, 1, 4, 5, 7]],
['Ru','Ruthenium','44','101.07','Solid','Transitional Metals',[3, 4],[-4, -2, 1, 2, 5, 6, 7, 8]],
['Os','Osmium','76','190.20','Solid','Transitional Metals',[4],[-4, -2, -1, 1, 2, 3, 5, 6, 7, 8]],
['Hs','Hassium','108','265.00','Synthetic','Transitional Metals',[8],None],
# Group 9
['Co','Cobalt','27','58.93','Solid','Transitional Metals',[2, 3],[-3, -1, 1, 4, 5]],
['Rh','Rhodium','45','102.91','Solid','Transitional Metals',[3],[-3, -1, 1, 2, 4, 5, 6]],
['Ir','Iridium','77','192.22','Solid','Transitional Metals',[3, 4],[-3, -1, 1, 2, 5, 6, 7, 8, 9]],
['Mt','Meitnerium','109','266.00','Synthetic','Transitional Metals',None,None],
# Group 10
['Ni','Nickle','28','58.70','Solid','Transitional Metals',[2],[-2, -1, 1, 3, 4]],
['Pd','Palladium','46','106.40','Solid','Transitional Metals',[2, 4],[1, 3, 5, 6]],
['Pt','Platinum','78','195.09','Solid','Transitional Metals',[2, 4],[-3, -2, -1, 1, 3, 5, 6]],
# Group 11 Coinage Metals
['Cu','Copper','29','63.55','Solid','Transitional Metals',[2],[-2, 1, 3, 4]],
['Ag','Silver','47','107.97','Solid','Transitional Metals',[1],[-2, -1, 2, 3, 4]],
['Au','Gold','79','196.97','Solid','Transitional Metals',[3],[-3, -2, -1, 1, 2, 5]],
# Group 12
['Zn','Zinc','30','65.37','Solid','Transitional Metals',[2],[-2, 1]],
['Cd','Cadmium','48','112.41','Solid','Transitional Metals',[2],[-2, 1]],
['Hg','Mercury','80','200.59','Liquid','Transitional Metals',[1, 2],[-2, 4]],
# Group 13 Boron Family
['B','Boron','5','10.81','Solid','Nonmetals',[3],[-5, -1, 1, 2]],
['Al','Aluminum','13','26.98','Solid','Other Metals',[3],[-2, -1, 1, 2]],
['Ga','Gallium','31','69.72','Solid','Other Metals',[3],[-5, -4, -2, -1, 1, 2]],
['In','Indium','49','69.72','Solid','Other Metals',[3],[-5, -2, -1, 1, 2]],
['Ti','Thallium','81','204.37','Solid','Other Metals',[1, 3],[-5, -2, -1, 2]],
# Group 14 Carbon Family
['C','Carbon','6','12.01','Solid','Nonmetals',[-4, -3, -2, -1, 1, 2, 3, 4],None],
['Si','Silicon','14','28.09','Solid','Nonmetals',[-4, 4],[-3, -2, -1, 1, 2, 3]],
['Ge','Germanium','32','72.59','Solid','Other Metals',[-4, 2, 4],[-3, -2, -1, 1, 3]],
['Sn','Tin','50','118.69','Solid','Other Metals',[-4, 2, 4],[-3, -2, -1, 1, 3]],
['Pb','Lead','82','207.20','Solid','Other Metals',[2, 4],[-4, -2, -1, 1, 3]],
# Group 15 Pnictogens
['N','Nitrogen','7','14.01','Gas','Nonmetals',[-3, 3, 5],[-2, -1, 1, 2, 4]],
['P','Phosphorus','15','30.97','Solid','Nonmetals',[-3, 3, 5],[-2, -1, 1, 2, 4]],
['As','Arsenic','33','74.92','Solid','Nonmetals',[-3, 3, 5],[-2, -1, 1, 2, 4]],
['Sb','Antimony','51','121.75','Solid','Other Metals',[-3, 3, 5],[-2, -1, 1, 2, 4]],
['Bi','Bismuth','83','208.98','Solid','Other Metals',[3],[-3, -2, -1, 1, 2, 4, 5]],
# Group 16 Chalcogens
['O','Oxygen','8','15.99','Gas','Nonmetals',[-2],[-1, 1, 2]],
['S','Sulfur','16','32.06','Solid','Nonmetals',[-2, 2, 4, 6],[-1, 1, 3, 5]],
['Se','Selenium','34','78.96','Solid','Nonmetals',[-2, 2, 4, 6],[-1, 1, 3, 5]],
['Te','Tellurium','52','127.60','Solid','Nonmetals',[-2, 2, 4, 6],[-1, 1, 3, 5]],
['Po','Polonium','84','209.00','Solid','Other Metals',[-2, 2, 4],[5, 6]],
# Group 17 Halogens
['F','Fluorine','9','18.99','Gas','Nonmetals',[-1],None],
['Cl','Chlorine','17','35.45','Gas','Nonmetals',[-1, 1, 3, 5, 7],[2, 4, 6]],
['Br','Bromine','35','79.90','Liquid','Nonmetals',[-1, 1, 3, 5],[4, 7]],
['I','Iodine','53','126.90','Solid','Nonmetals',[-1, 1, 3, 5, 7],[4, 6]],
['At','Astatine','85','210.00','Solid','Nonmetals',[-1, 1],[3, 5, 7]],
# Group 18 Noble gases
['He','Helium','2','4.00','Gas','Nobel Gases',None,[1, 2]],
['Ne','Neon','10','20.18','Gas','Nobel Gases',None,None],
['Ar','Argon','18','39.95','Gas','Nobel Gases',None,None],
['Kr','Krypton','36','83.80','Gas','Nobel Gases',[2],None],
['Xe','Xenon','54','131.30','Gas','Nobel Gases',[2,4,6],[8]],
['Rn','Radon','86','222.00','Gas','Nobel Gases',[2],[6]],
# Lanthanides
['Ce','Cerium','58','140.12','Solid','Transitional Metals',[3, 4],[2]],
['Pr','Praseodymium','59','140.91','Solid','Transitional Metals',[3],[2, 4, 5]],
['Nd','Neodymium','60','144.24','Solid','Transitional Metals',[3],[2, 4]],
['Pm','Promethium','61','145.00','Synthetic','Transitional Metals',[3],[2]],
['Sm','Samarium','62','150.40','Solid','Transitional Metals',[3],[2]],
['Eu','Europium','63','151.96','Solid','Transitional Metals',[2,3],None],
['Gd','Gadolinium','64','157.25','Solid','Transitional Metals',[3],[1,2]],
['Tb','Terbium','65','158.93','Solid','Transitional Metals',[3],[1,2,4]],
['Dy','Dyprosium','66','162.50','Solid','Transitional Metals',[3],[2,4]],
['Ho','Holmium','67','164.93','Solid','Transitional Metals',[3],[2]],
['Er','Erbium','68','167.26','Solid','Transitional Metals',[3],[2]],
['Tm','Thulium','69','168.93','Solid','Transitional Metals',[3],[2]],
['Yb','Ytterbium','70','173.04','Solid','Transitional Metals',[3],[2]],
['Lu','Lutetium','71','174.97','Solid','Transitional Metals',[3],[2]],
#Actinides
['Th','Thorium','90','232.04','Solid','Transitional Metals',[4],[1, 2, 3]],
['Pa','Protactinium','91','231.04','Solid','Transitional Metals',[5],[3, 4]],
['U','Uranium','92','238.03','Solid','Transitional Metals',[6],[1, 2, 3, 4, 5]],
['Np','Neptunium','93','237.05','Synthetic','Transitional Metals',[5],[2, 3, 4, 6, 7]],
['Pu','Plutonium','94','244.00','Synthetic','Transitional Metals',[4],[2, 3, 5, 6, 7]],
['Am','Americium','95','243.00','Synthetic','Transitional Metals',[3],[2, 4, 5, 6, 7]],
['Cm','Curium','96','247','Synthetic','Transitional Metals',[3],[4, 6]],
['Bk','Berkelium','97','247','Synthetic','Transitional Metals',[3],[4]],
['Cf','Californium','98','247','Synthetic','Transitional Metals',[3],[2, 4]],
['Es','Einsteinium','99','252.00','Synthetic','Transitional Metals',[3],[2, 4]],
['Fm','Fermium','100','257.00','Synthetic','Transitional Metals',[3],[2]],
['Md','Mendelevium','101','260.00','Synthetic','Transitional Metals',[3],[2]],
['No','Nobelium','102','259','Synthetic','Transitional Metals',[2],[3]],
['Lr','Lawrencium','103','262','Synthetic','Transitional Metals',[3],None],
# Sub Atomic Particles
['n','Neutron', None,'1.008664' , None,'Sub Atomic Particle',[0],None],
['e','Electorn', None,'0.00054858', None,'Sub Atomic Particle',[-1],None],
['p','Proton', None,'1.007276' , None,'Sub Atomic Particle',[+1],None],
# Other Particles
['α','Alpha Particle',None,'4.00',None,'Other Particle',[2],None],
['β','Beta Particle',None,'5.49e-4',None,'Other Particle',[-1],None],
['γ','Gamma Particle',None,None,None,'Other Particle',None,None],
]

'''___________________________________________________________________________________________________________________'''


# Dictionary of constants

constants={
    'avagadro' : 6.022*10E23,  # Avagadro's const
    'faraday' : 96485.33,      # Faraday's const
    'amu' : 1.66*10E-27,       # One atomic mass unit
    'coulomb' : 8.987*10E9,    # Coulomb's const
    'c' : 299792458,           # Speed of light in vacuum
    'boltzmann' : 1.38*10E-23, # Boltzmann constant
    'q' : 1.602*10E-19,        # Charge on proton
    'g' : 9.80665,             # std accn due to gravity on earth
    'rydberg' : 10973731,      # Rydberg's const
    'h' : 6.626*10E-34,        # Plank's constant
    'sp_heat_water' : 4.18,    # Specific heat capacity of water
    'gas_const' : 8.3144      # Universal gas constant
}

'''___________________________________________________________________________________________________________________'''