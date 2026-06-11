# Tuple
# (item1,item2,item3,...)
# difference between list and tuple is that
# list : in square brackets elements are separated by commas
# Tuple : in parentheses round brackets() elements are separated by commas
# what's the need of tuples ?
# tuple in which we cant modify anything elements are fixed, but in case of list we can modify the list
# tuples are used where in months of year which are fixed so here instead of list we can use tuple because no need to add or remove anything , spelling correction is okay.
# lists are used where in number of students in classroom because here student may be present or be absented so we can use list rather tuples ...
# same as list any data type can be used as elements in tuple : integer , float , strings , lists and also tuple itself

t = ["Python",10,1.3,True,[1,2,3],(10,20)]
print(t)
print(type(t))
t1 = ("Python",10,1.3,True,[1,2,3],(10,20))
print(t1)
print(type(t1))
print(len(t1))

t2 = 10,20,30,40
print(t2)
print(type(t2))
# here we haven't used parentheses even though showing class as tuple because brackets in case of tuples are not mandatory

## Accessing items of a tuple - index
# same positive and negetive indexing and also chain indexing
print(t1[0])
print(t1[-1])
print(t1[-1][1])

## Type casting (conversion of one data type into another)
# list into tuple / tuple into list
l1 = [1,2,3,4]
print(l1,type(l1))
t3 = tuple(l1)
print(t3,type(t3))
# if you want to add any item into tuple then jus type cast it into list and then modify it by using operations

## Operations in Tuples
# 1) concatenation of tuples
student_detail1 =("r no : 09" , "Jashwanth")
student_detail2 =("marks :95,96,98,93","CGPA:9.5")
print(student_detail1,type(student_detail1))
print(student_detail2,type(student_detail2))
student_details = student_detail1 + student_detail2
print(student_details,type(student_details))

# 2) repetition operator (* operator)
t4 = ("class 5", 5000)
print(t4 * 3)

# 3) membership operator
# in and not in
t5 = (1,2,4,5,7,8,0)
print(3 in t5)
print(3 not in t5)
print(5 in t5)
print(5 not in t5)

# 4) count
# print(tuple.count(element))
t6 = (22,11,44,88,99,22,55)
print(t6,type(t6))
print(t6.count(22))

# 5) index (just tells us about index number of element) it works with list , string and also tuple
# print(tuple.index(element))
print(t6.index(11))
print(t6.index(22))   # for this first occurrence will be the index number value
# print(t6.index(33))   This will be a 'value error' because value is not present in the tuple

# min(tuple) , max(tuple) , sum(tuple)
print(f"biggest number is {max(t6)}")
print(f"smallest number is {min(t6)}")
print(f"sum of both numbers is {sum(t6)}")