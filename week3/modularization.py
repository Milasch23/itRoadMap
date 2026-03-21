# MODULARIZATION

# Import packages
import package.module_example1
from package.module_example2 import exponentiation


#import subpackages

import package.subpackage.module_example3 as me3
from package.subpackage.module_example4 import description

me3.description()
description()

###########################################################

# Import a built-in module in Python

# import random

################################################################

# Import part of a module
from random import randint, randrange

#################################################################

# Import all items from a module

# from random import *

###################################################################

# Imports with aliases

# import random as rd

# random_number = rd.radint(1, 1000)

##############################################################

# Call a module element

# random_number = random.randint(1, 1000)

random_number = randint(1, 1000)
print(random_number)

#############################################################

result = package.module_example1.addition(13, 5)
print(result)

result2 = exponentiation(5, 2)
print(result2)