### modules : a file with extension of .py which contain definitions , functions , executable codes , etc ...
## why used : if a function used multiple times then modules can be used
## Two types: inbuilt modules , user defined modules
## 1] user defined modules : math , random , datetime, ...

# how to import a module
# syntax: import module_name
# syntax for importing only few functions/variables : from module_name import f1, f2, f3

import math

from sets_python import nums_2

# calculate square root of a number
num = 100
output = math.sqrt(num) # module.function_name(arg1, arg2, arg3, ...)
print(output)

# calculate the area of a circle
radius = 10
area = math.pi*radius**2
print(f"area of circle is {area}")
print(math.pi)

# this built in math module have all math functions which is an inbuilt module
# in same way we also done for random module which has functions like randint , etc.
# if once we import a module in one file of python it will be cant be used in other new file we need to freshly import it again

# throw a die
from random import randint
value = randint(1, 6) # here we shouldn't use random.randint because we only imported one specific function from random module not entire function
print(value)

### syntax to create an alias (nickname) for the module (full name) : import module_name as alias_name

import datetime as dt
t = dt.datetime.now()
print(t)
print(t.year)
print(t.month)
print(t.day)

## 2] user defined modules
## check in another file
import user_defined_module
a = 10
b = 20
result = user_defined_module.add(a, b)
print(result)
result2 = user_defined_module.square(a)
print(result2)

## in the same way we can also import only one function from user defined same as from inbuilt module
### these two are functions in another module

### __name__ variable (not that important)
# if any executable code is already present in a code file you made and also functions in it
# and you are importing it and using it then it makes that exectuable code also run and also functions
