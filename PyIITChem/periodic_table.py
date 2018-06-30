periodic_table = [
    # symbol name  atomic number    atomic weight     state      category     
    ['H', 'Hydrogen', '1','1.01','Gas','Alkali Metals'],
    ['Li', 'Lithium', '3','6.94','Solid','Category = Alkali Metals'],
    ['Na', 'Sodium', '11','22.99','Solid','Alkali Metals'],
    ['K', 'Potassium', '19','39.10','Solid','Alkali Metals'],
    ['Rb', 'Rubidium', '37','85.47','Solid','Alkali Metals'],
    ['Cs', 'Cesium', '55','132.91','Solid','Alkali Metals'],
    ['Fr', 'Francium', '87','223.00','Solid','Alkali Metals']
    ['Be', 'Beryllium', '4','9.01','Solid','Alkaline Earth Metals'],
    ['Mg', 'Magnesium', '12','24.31','Solid','Alkaline Earth Metals'],
    ['Ca', 'Calcium', '20','40.08','Solid','Alkaline Earth Metals'],
    ['Sr', 'Strontium', '38','87.62','Solid','Alkaline Earth Metals'],
    ['Ba', 'Barium', '56','137.33','Solid','Alkaline Earth Metals'],
    ['Ra', 'Radium', '88','226.03','Solid','Alkaline Earth Metals']
    ['Sc', 'Scandium', '21','44.96','Solid','Transitional Metals'],
    ['Y', 'Yttrium', '39','88.91','Solid','Transitional Metals'],
    ['La', 'Lanthanum', '57','138.91','Solid','Transitional Metals'],
    ['Ac', 'Actinium', '89','227.03','Solid','Transitional Metals']
    ['Ti', 'Titanium', '22','47.90','Solid','Transitional Metals'],
    ['Zr', 'Zirconium', '40','91.22','Solid','Transitional Metals'],
    ['Hf', 'Hanium', '72','178.49','Solid','Transitional Metals'],
    ['Rf', 'Rutherfordium', '104','261.00','Synthetic','Transitional Metals']
    ['V', 'Vanadium', '23','50.94','Solid','Transitional Metals'],
    ['Nb', 'Niobium', '41','92.91','Solid','Transitional Metals'],
    ['Ta', 'Tantalum', '73','180.95','Solid','Transitional Metals'],
    ['Ha', 'Hahnium', '105','262.00','Synthetic','Transitional Metals']
    ['Cr', 'Chromium', '24','51.99','Solid','Transitional Metals'],
    ['Mo', 'Molybdenum', '42','95.94','Solid','Transitional Metals'],
    ['W', 'Tungsten', '74','183.85','Solid','Transitional Metals'],
    ['Sg', 'Seaborgium', '106','266.00','Synthetic','Transitional Metals']
    ['Mn', 'Manganese', '25','178.49','Solid','Transitional Metals'],
    ['Tc', 'Technetium', '43','178.49','Synthetic','Transitional Metals'],
    ['Re', 'Rhenium', '75','178.49','Solid','Transitional Metals'],
    ['Bh', 'Bohrium', '107','262.00','Synthetic','Transitional Metals']
    ['Fe', 'Iron', '26','55.85','Solid','Transitional Metals'],
    ['Ru', 'Ruthenium', '44','101.07','Solid','Transitional Metals'],
    ['Os', 'Osmium', '76','190.20','Solid','Transitional Metals'],
    ['Hs', 'Hassium', '108','265.00','Synthetic','Transitional Metals']
    ['Co', 'Cobalt', '27','58.93','Solid','Transitional Metals'],
    ['Rh', 'Rhodium', '45','102.91','Solid','Transitional Metals'],
    ['Ir', 'Iridium', '77','192.22','Solid','Transitional Metals'],
    ['Mt', 'Meitnerium', '109','266.00','Synthetic','Transitional Metals']
    ['Ni', 'Nickle', '28','58.70','Solid','Transitional Metals'],
    ['Pd', 'Palladium', '46','106.40','Solid','Transitional Metals'],
    ['Pt', 'Platinum', '78','195.09','Solid','Transitional Metals']
    ['Cu', 'Copper', '29','63.55','Solid','Transitional Metals'],
    ['Ag', 'Silver', '47','107.97','Solid','Transitional Metals'],
    ['Au', 'Gold', '79','196.97','Solid','Transitional Metals']
    ['Zn', 'Zinc', '30','65.37','Solid','Transitional Metals'],
    ['Cd', 'Cadmium', '48','112.41','Solid','Transitional Metals'],
    ['Hg', 'Mercury', '80','200.59','Liquid','Transitional Metals']
    ['B', 'Boron', '5','10.81','Solid','Nonmetals'],
    ['Al', 'Aluminum', '13','26.98','Solid','Other Metals'],
    ['Ga', 'Gallium', '31','69.72','Solid','Other Metals'],
    ['In', 'Indium', '49','69.72','Solid','Other Metals'],
    ['Ti', 'Thallium', '81','204.37','Solid','Other Metals']
    ['C', 'Carbon', '6','12.01','Solid','Nonmetals'],
    ['Si', 'Silicon', '14','28.09','Solid','Nonmetals'],
    ['Ge', 'Germanium', '32','72.59','Solid','Other Metals'],
    ['Sn', 'Tin', '50','118.69','Solid','Other Metals'],
    ['Pb', 'Lead', '82','207.20','Solid','Other Metals']
    ['N', 'Nitrogen', '7','14.01','Gas','Nonmetals'],
    ['P', 'Phosphorus', '15','30.97','Solid','Nonmetals'],
    ['As', 'Arsenic', '33','74.92','Solid','Nonmetals'],
    ['Sb', 'Antimony', '51','121.75','Solid','Other Metals'],
    ['Bi', 'Bismuth', '83','208.98','Solid','Other Metals']
    ['O', 'Oxygen', '8','15.99','Gas','Nonmetals'],
    ['S', 'Sulfur', '16','32.06','Solid','Nonmetals'],
    ['Se', 'Selenium', '34','78.96','Solid','Nonmetals'],
    ['Te', 'Tellurium', '52','127.60','Solid','Nonmetals'],
    ['Po', 'Polonium', '84','209.00','Solid','Other Metals']
    ['F', 'Fluorine', '9','18.99','Gas','Nonmetals'],
    ['Cl', 'Chlorine', '17','35.45','Gas','Nonmetals'],
    ['Br', 'Bromine', '35','79.90','Liquid','Nonmetals'],
    ['I', 'Iodine', '53','126.90','Solid','Nonmetals'],
    ['At', 'Astatine', '85','210.00','Solid','Nonmetals']
    ['He', 'Helium', '2','4.00','Gas','Nobel Gases'],
    ['Ne', 'Neon', '10','20.18','Gas','Nobel Gases'],
    ['Ar', 'Argon', '18','39.95','Gas','Nobel Gases'],
    ['Kr', 'Krypton', '36','83.80','Gas','Nobel Gases'],
    ['Xe', 'Xenon', '54','131.30','Gas','Nobel Gases'],
    ['Rn', 'Radon', '86','222.00','Gas','Nobel Gases']
    ['Ce', 'Cerium', '58','140.12','Solid','Transitional Metals'],
    ['Pr', 'Praseodymium', '59','140.91','Solid','Transitional Metals'],
    ['Nd', 'Neodymium', '60','144.24','Solid','Transitional Metals'],
    ['Pm', 'Promethium', '61','145.00','Synthetic','Transitional Metals'],
    ['Sm', 'Samarium', '62','150.40','Solid','Transitional Metals'],
    ['Eu', 'Europium', '63','151.96','Solid','Transitional Metals'],
    ['Gd', 'Gadolinium', '64','157.25','Solid','Transitional Metals'],
    ['Tb', 'Terbium', '65','158.93','Solid','Transitional Metals'],
    ['Dy', 'Dyprosium', '66','162.50','Solid','Transitional Metals'],
    ['Ho', 'Holmium', '67','164.93','Solid','Transitional Metals'],
    ['Er', 'Erbium', '68','167.26','Solid','Transitional Metals'],
    ['Tm', 'Thulium', '69','168.93','Solid','Transitional Metals'],
    ['Yb', 'Ytterbium', '70','173.04','Solid','Transitional Metals'],
    ['Lu', 'Lutetium', '71','174.97','Solid','Transitional Metals']
    ['Th', 'Thorium', '90','232.04','Solid','Transitional Metals'],
    ['Pa', 'Protactinium', '91','231.04','Solid','Transitional Metals'],
    ['U', 'Uranium', '92','238.03','Solid','Transitional Metals'],
    ['Np', 'Neptunium', '93','237.05','Synthetic','Transitional Metals'],
    ['Pu', 'Plutonium', '94','244.00','Synthetic','Transitional Metals'],
    ['Am', 'Americium', '95','243.00','Synthetic','Transitional Metals'],
    ['Cm', 'Curium', '96','247','Synthetic','Transitional Metals'],
    ['Bk', 'Berkelium', '97','247','Synthetic','Transitional Metals'],
    ['Cf', 'Californium', '98','247','Synthetic','Transitional Metals'],
    ['Es', 'Einsteinium', '99','252.00','Synthetic','Transitional Metals'],
    ['Fm', 'Fermium', '100','257.00','Synthetic','Transitional Metals'],
    ['Md', 'Mendelevium', '101','260.00','Synthetic','Transitional Metals'],
    ['No', 'Nobelium', '102','259','Synthetic','Transitional Metals'],
    ['Lr', 'Lawrencium', '103','262','Synthetic','Transitional Metals']
    ]


