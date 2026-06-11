### Mutability & Immutability
## mutability   : It is the ability of a value or data to be modified or changed
## immutability : inability of a value or data to be changed or modified ...
# Lists are mutable
# Tuples and Strings are immutable

# Strings are immutable
s1 = "python is fun"
s2 = s1.replace("python","java")
print(s1)
print(s2)
# in the above case existing string (s1) didn't change it created new string completely which stored in new variable (s2)

# Tuples are immutable
t1 = ("Banana" , "mango" , "apple")
print(t1)
# print(t1.append("mango"))    this will be an attribute error because your trying to append a tuple which only can be in list
# t1[-1] = "pineapple"  type error 'tuple' object does not support item assignment

# Lists are mutable
l1=[1,2,3,4,4,5,6]
print(id(l1))
l1.append(5)
print(l1)
print(id(l1))
# here the existing list(l1) got changed by adding an element to the existing list (l1) which cant be seen in tuples and strings
# MEMORY ADDRESS : In Python, a memory address is a unique integer that acts as a "street address" or specific location in your computer's RAM where a piece of data (an object) is physically stored
# print(id(list/any data variable))

