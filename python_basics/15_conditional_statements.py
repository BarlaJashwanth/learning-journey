### fundamental concept of programing language used to code on based of criterias
## ==, >= , <= ,>, < , != these operators are for defining the condtions which gives output as boolean data true or false
# indentation : concept of making space before block of code lines this blocks are nothing but where multiple lines of codes can be written together
# syntax of if
# if condition:
#    statement1
#    statement2
#    statement3
#    statementN
# statementM
# in this above example space before statements are indentation and
# statement1,statement2,statement3,statementN this are block of code lines
# HOW python reads this code
# if condition is true then it goes inside the block for every statement and it goes outside of block for statementM at last .
# if condtion is false then it won't goes inside the block it directly goes to statementM which is outside the block

age = float(input("what is your age ?"))
if age >= 18:
    print("congratulations! you are an adult. You can cast your vote ")
print("Rest of the program")

### if-else conditional statement
## here else only works along with if but if can work without else but else need if

age = float(input("what is your age ?"))
if age >= 18:
    print("congrats! you can cast your vote ")
else:
    print("sorry please wait for few more years")

print("Rest of the program")

# in case of "if" only works when statement is true and goes further into block
# in case of "else" works when statement is false and goes further into block .

## task
# print if a number (int) is odd or even
# even - when the number is divisible by 2 . reminder is 0
# odd - the number is not divisible by 2 . reminder is not 0

x= int(input("whats your number?"))
if x % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


y = int(input("whats your number?"))
if y > 0:
    print("The number is positive")
else:
    print("The number is negative")

# if - elif - else condtional sentence
z = int(input("whats your number?"))
if z > 0:
    print("The number is positive")
elif z == 0:                         # if condtion is false then it checks elif and if all elif completed then it goes to else ...
    print("The number is zero")
else :
    print("The number is negative")

### Nested if statements (conditional sentences under normal conditional sentences multiple sentences)

'''
if marks >= 60, student is pass else student is fail
and the student is pass, then we print the grade

>= 90, grade A
80 to 89, grade B
70 to 79 grade C
60 to 69 grade D
'''
marks = float(input("whats your marks?"))
if marks >= 60:
    print('congrats! your pass in exam')
    if marks >= 90:
        print('congrats! your grade is A')
    elif marks >= 80:
        print('congrats! your grade is B')
    elif marks >= 70:
         print('congrats! your grade is C')
    else:
        print('congrats! your grade is D')
else:
    print('sorry! you failed in exam')

### ternary operator : entire condtional sentences of multiple line can be written in single line which is called as ternary operator
## syntax : true-expression if condition else false-expression
# for example

name = str(input("what is your name?"))

# if name == "Jash":
#     print("welcome again")
# else:
#     print("Sorry wrong username")     these code can be also written as ternery operator given down

print("welcome again") if name == "Jash" else print("sorry! wrong username")


