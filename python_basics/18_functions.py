from ctypes.wintypes import HRESULT

print("Hello World")
var = 1000
print(var)
print(10,20,30)
print(len("how are you"))
# 'print' function helps to display the output (inbuilt function)
import random
# Here random is module in which functions will be present such as randint etc..
print(random.randint(10,20))
### functions which are already present are "inbuilt functions"
### functions which needed to be imported from modules "importing functions"
### functions which are made by user it can be anything those are "user defined functions"

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")

"""
WHY "USER_DEFINED_FUNCTIONS" ARE REQUIRED:
user defined functions are required because if you have written a logic which is used multiple times at differnt stages of program
then we can create simply our own user defined function and that can be used multiple times at differnt stages of program
where loops can also do the multiple times but consecutively only if it breaks once we need to write again where we need ...
"""
### How to create user defined function ???
# syntax given below: (function name can be anything our wish without any space)
# def function_name(arg1, arg2, arg3,... argn):
#     statement1
#     statement2
#     ...
#     statement3

# examples of user defined functions
def greeting_someone():
    print("Hello World")
    print("How are You ?")

# how to use this user defined function ???
greeting_someone() # now this get displayed how many times we can use that
greeting_someone()
greeting_someone()

# if we wanna also use argument
def greeting_someone(name):
    print(f"Hello {name}")
    print("How are You ?")

# calling user defined function
greeting_someone("Jashwanth")           # here output will be name specific
greeting_someone("Nandini")        # as we used name as argument while preparing
greeting_someone("Rajeshwari")           # the user defined function ...

### now even odd machine i wanna do for that
def even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(10)  # these are just executing we created function simply
even_odd(20)
even_odd(35)

def add(num1, num2):
    result = num1 + num2
    print(f"result: {result}")

add(10, 20)
add(20, -15)

### returning values from function :
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = even_odd(10)
print(result)

"""
DIFFERENCE BETWEEN "PRINT" AND "RETURN"
# Difference between print() and return()

# print() -> Only displays the output on the screen.
# It does not send the value back from the function.
# We cannot store the printed value in a variable.

# return -> Sends the value back from the function.
# The returned value can be stored in a variable,
# printed, or used in another calculation.

# Example:
# print("Even")        -> Shows "Even" on the screen.
# return "Even"        -> Gives "Even" back to the caller.

# If we write:
# even_odd(10)
# The function returns "Even", but since we did not
# store or print it, nothing is shown.

# To see the returned value:
# print(even_odd(10))
# OR
# result = even_odd(10)
# print(result)

# Assignment (=) in Python
# Left side of = must always be a variable.
# Right side can be a value, expression, or function call.

# Correct:
# result = 2 + 5
# x = even_odd(10)

# Wrong:
# 2 + 5 = result
# even_odd(10) = x

# Easy way to remember:
# print() = Show the value.
# return = Give the value back.
# = (assignment) = Store the value in a variable.
"""

### types of arguments in functions
def add(a,b):
    return a+b

# positional arguments : passing the arguments in order of their position
result = add(10,5) # here a and b which are 10 and 5 respectively are positional arguments

# Default arguments : here argument is already given example b = 10
def add(a,b=10):
    return a+b

result = add(10,) # here if you enter b value then it take the b value otherwise it takes the default value of b which is 10
print(result)
result = add(10,5)
print(result) # here you given b value so output wil be 15 not 20

### NOTE: The non default arguments shoulf not follow the default arguments
## example
# def add(a,b=10,c):
#     return a+b+c
# result = add(10,5,10) ### this gives error as c which is non default argument is following b which is default argument which gives syntax error
# print(result)

def add(a,c,b=10):
    return a+c+b
result = add(1,2,9) ### now no error as default argument is at last b which is after c in arguments ...
print(result)

### keyword arguments :
def add(a,b=10,c=10):
    return a+b+c
result = add(1,c=5) ### here your making to give a and c values and b its default value in this case you need to specify c as 5 otherwise it may take as b so this is keyword argument ..
print(result) ### keywords arguments can be randomly too like "add(b=10,c=5,a=23)" ...

### variable length arguments =    * arguments
def add(*args):
    print(args,type(args))
    return sum(args)
add(10,20,2,3,1,0)
result = add(10,20,2,3,1,0)
print(result)

def student_details(sid,name,*marks):
   if len(marks) == 0:
       print(f"{sid} id student named {name} was absent on exam day")
   else:
       percent = sum(marks) / len(marks)
       print(f"{name} with id {sid} secured percent {percent}")

student_details(101,"jash",97,99,95)
student_details(102,"shiny",99,98,99)
student_details(103,"rishi")

### variable length keyword arguments :
### **kwargs - variable length keyword arguments

def func(**kwargs):
    print(kwargs,type(kwargs))

func(x=10,y=20,z=30)
func()

def student_details(sid,name,**marks):
    if len(marks) == 0:
        print(f"{name} didn't secure any marks")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{name} with id {sid} secured percent {percent}")

student_details(101,"jash",sub1=97,sub2=99,sub3=95)
student_details(102,"shiny",sub1=99,sub2=98,sub3=99)
student_details(103,"rishi")

### DOC_STRINGS IN FUNCTIONS : A string enclosed """ """ used to describe a module or function .It makes code easier to understand , maintain, and document ...
def func():                  # these doc function dosen't work inside code it just helps to understand the code for user
    """
    This is a doc string.
    we can write what the function does here
    :return:  None
    """
    return None

print(help(func)) # help word helps in identifying the docstring what does it have

def divide(num1, num2):
    """
    num1: A number to be divided (numerator)
    num2: A number that divides num1 (denominator)
    :param num1:
    :param num2:
    :return: float/ str (if num2 is 0)
    """
    if num2 == 0:
        print("infinite division")
    else:
        result = num1/num2
        return result
print(divide(10,0))
print(divide(0,10))
print(divide(10,100))

help(divide) # help function can be also used without print or with print just to show the docstring which u gave in code
# doc string should be just after defining the function it shouldbe first step it can be used for both inbuilt and user functions too
help(len) # this is the example

### Recursion
"""
Recursion is a process in which a function calls itself till a certain condition is not met
factorial of a number (n!) => n * (n-1) * (n-2) * .... 2 * 1
eg : 4! = 4 * 3 * 2 * 1 = 24 

n! => n * (n-1) * (n-2) * ... 2 * 1
n! => n * (n-1)!
n! => n * (n-1) * (n-2)! ......

There are 2 parts to any recursive function:
1. Base/terminal condition 
2. recursive condition
"""
# without recursion
def factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num   # this is nothing but factorial = factorial * num
        num -= 1           # num = num - 1

    return factorial

print("without recursion")
print(f"factorial of 4 is {factorial(4)}")

# with recursion
def factorial_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * factorial_rec(num - 1)  # here factorial_rec(num - 1) calls again into the function like
        return(factorial)                         # 4 * factorial_rec(3) => 4 * 3 * factorial_rec(2) => 4 * 3 * 2 * factorial_rec(1) => 4 * 3 * 2 * 1

print("with recursion")
print(factorial_rec(4))



x = int(input("enter the factorial number:"))
def factorial_rec(x):
    if x == 1:
        return 1
    else:
        factorial = x * factorial_rec(x-1)
        return factorial

print(f"the factorial of {x} is {factorial_rec(x)}")

### local and global variables
n = 1             # gobal variables
def fn():
    n = 5         # local variable (higher prefernce)
    print("in",n)

fn()

print("out",n)

### passing function as argument
# in python we can pass function as argument of another function

def add_1(number):
    return number + 1

print(add_1(10))

def square(number):
    return number ** 2

print(square(10))

# now we want to write a code in which it takes input of a number and add 1 to it and square the number

num = int(input("enter the number:"))
res_1 = add_1(num)
res_2 = square(res_1)
print(f"output is : {res_2}")

# here in above case we are using one function as argument inside another function



### lambda function : makes function and arguments in single line
## syntax:
# lambda argument: expression
fun = lambda num: num + 1  ## only one argument
res = fun(2)
print(res)

fun = lambda a,b: a + b
res = fun(3,4)
print(res)

### FILTER and MAP functions :
## filter function = has a function and sequence these filter function helps to pick the elemnts from sequence and give output which satisfies the function
## filter(function, sequence)
seq = [1,2,3,4]
odd = lambda x : True if x % 2 != 0 else False
filter_result = filter(odd, seq)
print(filter_result)       # this gives some memory id
print(list(filter_result)) # this gives list


## map function : same function as filter , first argument and sequence as second argument
seq = [1,2,3,4]
odd = lambda x : True if x % 2 != 0 else False
map_result = map(odd, seq)
print(map_result)         # same id ouput you will get
print(list(map_result))   # here we get output as [true , false , true , false] that means in sequence which are following the condition true and which are not false


