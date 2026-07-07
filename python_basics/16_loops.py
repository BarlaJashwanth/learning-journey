### loops : are two types  (its for repetation of program)
## a) for loop
## b) while loop

'''
# for loop : it is an iterator based loop which steps through the items of a collection
(lists, tuples, sets, dict, str) and executes a block of code repeatedly
for a number of times equal to the items/elements of that collection
'''
# for var in sequence:
#     sequence1
#     sequence2
#     ...
#     sequenceN

percents = [85.5, 89, 86.0, 95.0]
print(percents[0])
print(percents[1])
print(percents[2])
print(percents[3])

for p in percents:
    print(p) # same output as above code this is what use of loop

## for loop for strings
s1 = "Hello world"
for c in s1:
    print(c) # check output one by one character will be printed
print("End of the loop") # this is not in loop for being in loop indentation is required ...

## 'for loop' for dictionaries
D1 = {'Id': 1001,'Name': 'Jash','Department':'Hr'}
for d in D1:
    print(d) # here only key's will be displayed one after one no value is given here
    print(d, D1[d]) # in this case both key value pairs will come

## 'for loop' for tuples
# we already knew we learnt items concept in dictionaries which gives output as tuples for each key value pair
# same above example
print(D1.items())
for i in D1.items():
    print(i) # now key value pair in form of tuples will be displayed oneafter other .

### Range function
## range() - built in function used to generate sequence of integers in a given intervel
## syntax1: range(start, stop, step) stop is not included in generation
# for i in range(start, stop, step)
    #statements

for i in range(1,11,1): # here step cant be zero !!!
    print(i)

# if we wanna generate even numbers between 1 to 10 (10 excluded)
for j in range(2,10,2):
    print(j)

# if we wanna generate 20 to 10 reverse order excluding 10
for k in range(20,10,-1): # here step can't be step 1 here step will be -1
    print(k)

# coutdown from 10 to 1
for l in range(10,0,-1):
    print(l)
print("Happy New Year")


## syntax2: range(start,stop) => step 1 willbe by default
for n in range(1,11):
    print(n)


## syntax3: range(stop) => here start will be 0 by default and step will be 1
for p in range(5):
    print(p)

groceries = ['salt','milk','sugar']
for index in range(len(groceries)): #range(3) =>0,1,2  [syntax3 example]
    print(index) # by printing this we get index numbers 0,1,2

profits = [9, 11, 6, 10] # length is 4
# index :  0   1  2   3
# quaters  1   2  3   4
# i wanna print quaters and profits too
for index in range(len(profits)):

    quaters = index + 1
    print(f"profit for quater {quaters} is {profits[index]}")

### adding by loops

scores = [2,45,100,3,67,8,41,43,1,0,1]

total = 0
for score in scores:
    total = total + score

print(f" total runs scored is {total}")

# instead of doing this we have sum function "sum"
total = sum(scores)
print(f"total runs scored is {total}")

### highest score find out:
highest = scores[0] #assuming that the highest value is first score so index given is 0
for score in scores:
    if highest < score:
        highest = score

print(f'highest score is {highest}') # how this actually worked ???
"""
first we assumed first value of score as highest which has index 0 and value is 
2 is that highest no, then according to line 104 , now observe line 105 you can see
we used for loop so it checks the score list one by one score if the next score satisfies the 
code line 106 then it updates new highest score in code line 107 and for loop reads all the scores
and keeps on updating the highest score till it gets highest score and it stores the highest score in 
variable highest and when we use f string and print we get output the highest score ...
"""
## task lowest score for this
scores = [2,45,100,3,67,8,41,43,1,0,1]
lowest = scores[0]
for score in scores:
    if lowest > score:
        lowest = score
print(f"lowest score is {lowest}")
# for loop just go next after next in list, sets, dictionaries

### instead of loop we have for highest we have function "max"
### instead of loop we have for lowest we have function "min"
highest = max(scores)
print(f"highest score is {highest}")
lowest = min(scores)
print(f"lowest score is {lowest}")

### control statements for loops (continue,break,)
# 01
for num in range(1,10):
    if num % 3 == 0: #if number is divisible by 3 and reminder is 0
        continue
    print(num) # output : 1,2,4,5,7,8

print('next observation')

for num in range(1,10):
    if num % 3 == 0: #if number is divisible by 3 and reminder is 0
        print(num) # output : 0,3,6,9
        continue

### CONTINUE : what is this ???
'''
carefully observe both the cases you can observe that in first case you used for loop for
numbers range 1 to 9 and gave a condition to by using if for dividing with 3 then output
we got in first case is 1,2,4,5,7,8 because of control statement "continue" which is before 
print(num) function, that means when the condition is getting satisfied then it is going inside continue and it is
not letting to go further down print function it is making numb down functions

but in case of second observation

"continue" is after wards the print(num) function which is making the scenerio like after satisfaction of
if condition it is going into next function print(num) hence the output we expected 0,3,6,9 is coming...
'''
print("next observation")
#02
for num in range(1,10):
    if num % 3 == 0:
        break
    print(num)
'''
Here 'break' function is making to break the loop numbers are starting for 1 and then its going into condition of divisible by 3 
until when the break function arrives it is exiting the loop exactly when the number 3 came as it needs to go for further function
print(num) its denying and making it to stop ...
CONTINUE AND BREAK are only used inside a loop it cant be used outside ...
'''

#### While loop: (conditional based loop)
"""
incase of for loop we have fixed range or length of tuples, sets, dictionaries and it has a fixed length to run
finite loop (for loop), but in this case while loop
while loop : runs on condition based it runs till the condition is true if once it get false condition then it terminates 
the loop ...
"""
## syntax: while condition:
##         statements

# the main difference between the "while loop" and "if , elif" are those runs only once if the condition is true
# but these while loop runs until the statement is true once if the statement is false it exits the loop and it continues the further program.

for i in range(1,5,1):
    print(i)

print("next observation")

num = 1
while num < 5:
    print(num)
    num = num + 1   #If these line is not written the code runs infintely long as there is no condition for this loop never ends ...

print("next observation")

num = 1
while num < 5:
    num = num + 1
    print(num)

### infinite while loop
## Live example for using while loop(infintiely)

correct_password = "python"
while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("password is correct!!!")
        break # this makes help us to break infinte loop
    else:
        print("password is not correct!!!")
print("logged in!")

# example 2
num = 10

while num <= 20:
    print(num)
    num = num + 2

print('from here')

### NESTED LOOPS : loops inside the loops ...

for i in range(3):  ### outer loop
    for j in range(2): ### inner loop
        print(i,j)

"""
The inner loop runs completely every time the outer loop runs once         0 0
when first outer loop runs once because range is 3 so it need to runs 3    0 1                                                                         
times the output will be 0,1,2 so when it runs 0 and then inner loop runs  1 0
as its range is 2 output should 0,1 so it run two times completely and     1 1
and then print function displays both i and j (0,0)(0,1) and next line     2 0
simply first outer loop once next innerloop completely and then print      2 1
function and then again into outer loop this is the mechanism of working with this concept star pattern is drawn with next code
"""

### star_patterns by using python :
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

"""
outer loop is deciding number of lines for star patterns inner loop is deciding number of    *
stars in each line as range is (1,6) so total 5 lines of stars and inner loop is deciding    * *
the stars range is (1,i+1) that is 1 to 5+1 range which gives total 5 stars at end line      * * *
now the end function helps to make gap after stars and also that second print function       * * * *
is helping to cursor automatically move down after the required stars completed in that      * * * * *
line and again outer loop starts for next number and inner loop runs completely and inner print functions to run and again go to outer loop till outer loop ends this continues
"""

### Random modules:
## modules: files which have program in it like(print,input ,....)
# for importing new modules into python which are not part of previous existed modules we use keyword "import"...

import random

#random() - returns random float between 0.0 and 1.0 (excluded)
print(random.random())
print(random.random())
print(random.random()) # here we can see  3 times we get differnt floats which are between 0.0 and 1.0

# randint(a, b) => returns random int between a and b (both included)
print(random.randint(1,15))
print(random.randint(1,15))
print(random.randint(1,15))
print(random.randint(1,15))
print(random.randint(1,15))
print(random.randint(1,15))
print(random.randint(1,15)) # here all random numbers but these can be also repetetive ...

nums = [1,2,3,4,5,6,7,8,9,0]

#choice(sequence) => returns a random item from the sequence
print(nums)
print(random.choice(nums))
print(random.choice(nums))
print(random.choice(nums))
print(random.choice(nums))
print(random.choice(nums))

#shuffle(sequence) : returns the elements shuffled in random order
print(random.shuffle(nums)) # here output will be none as it dont show output it just completely shuffle the elements in list
print(nums)


###Exercises of loops
"""
write a program to stimulate a roll of a die/dice 
A die has 6 faces with numbers 1 to 6 written on them
the program should randomly print a number between 1 and 6
"""
import random

print("welcome to game of rolling a dice")
while True:
    choice = input("press 'enter' to roll the dice or 'q' to quit")
    choice = choice.strip() # this makes to delete the leading or lagging spaces when we are giving oyr input ...
    if choice == "q":
        print("Thanks for playing the game, bye!")
        break
    elif choice == "":
        number = random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("please enter a valid input")

print("Game Over!!!")

### word count
countries = ["India","America","Ireland","Indonesia","cuba","Iran","poland"]

# count all the countries which are starting with "I"
# also, print all these countries as a list
# ['India','Ireland','Indonesia','Iran']
counter = 0
output = []
for country in countries:
    if country.startswith("I"): # new function ".startswith" used in strings ony for finding the starting letter
        counter = counter + 1
        output.append(country) # these code is making a new list from pre existing list
print(counter)
print(output)
