### Errors in python :
## 01} Compile time error = a] Syntax error & b] Indentation error

# age = 24
# print(age
"""
Synta error example
"""

# age = 24
# if age >= 18:
# print("you are am adult")
"""
Indentation error example
"""


## 02} Run time errors (exceptions) => an error that happens while the program is actually running , even when the code is perfect
## like : zero errors , value errors , index errors , name errors , type errors , key erros , file not found errors , operation errors
# Examples 1 :
# print(10/0)
"""
Zero division error (exception)
"""

# Example 2 :
# x = 100
# result = x + y
# print(result)
"""
Name error (exception) as here y is not yet defined hence this is an name error
"""

### How to handle exceptions ? => try-except block

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError :
    print("Oops! Something went wrong.") # zero error will be denied
except ValueError :
    print("Input should be a number") # value error comes when we havent entered integer
except IndexError :
    print("Input should be a number")



# with open("my_file.txt") as fh:
#     data = fh.read()
#
# print(data)
"""
File not found error we are trying to open a file which is not existing 
"""

try:
    with open("test.txt") as fh:
        data = fh.read()

    print(data)

except FileNotFoundError:
    print("File not found ")
print("========================")
### else block and finally block
try:
    fh = open("practise1.txt")
    data = fh.read()

except FileNotFoundError:
    print("File not found ")
else:
    print("else block")
finally:
    print("final block")
    fh.close()

"""
In this we are using 3 functions :
try : this works when code is correct
except : ignoring the errors
else : when there is no error in the code then without going into
       except block it directly comes into else block
       
When there is exception else wont run and irrespective of exception finally block runs
"""
### in above example both else block and final block runs as there is a file practise1 file so there is no exception so else runs and final runs irrespective of exceptions
### but why do we need finally block : like closing file should be always done irrespective of error or no error so that type of mandatory codes which needed to be executed can be given in finally block .

"""
multiple excepts can exists in a code but atleast one except along with try should exist and else ad finally are optional 
"""



### Raising exceptions
# raise

salary = float(input("Enter your salary: "))

if salary < 0 :
    raise ValueError("Salary should be a positive number")
else:
    print("your salary is", salary,"rupees")



