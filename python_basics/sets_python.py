### SETS are different data types
## sets are non-sequential collection of items or elements
# comma separated elements enclosed within flower brackets {}

set1 = {1,"python",2.4}
print(set1,type(set1))
# cannot have indexing concept in sets because they are non sequential collection of items

# length of set
print(len(set1))

# slicing of sets is also not allowed same as indexing
# in list and tuple we can have repeated items in it but in sets we cant have repeated items
l1 = [1,1,2,2,3,3]
t1 = (1,1,2,2,3,3)
s1 = {1,1,2,2,3,3}
print(l1,type(l1))
print(t1,type(t1))
print(s1,type(s1)) # there will be no error in this code but in output when you run code you can see differnce that it takes only one item and neglate repeated items
# sets are usually used in unique individual numbers which cant be repeated (passport numbers which can be repeated so if we want all passport numbers only once we can use set)

## operations in sets
nums = {1,3,2,0,-1}

# membership operator
# in and not in
print(nums,type(nums))
print(1 in nums)
print(1 not in nums)

# concatenation (not possible)
nums_1 = {1,2,3,4,5}
nums_2 = {6,7,8,9,10}
# print(nums_1 + nums_2) this will be a 'type error' because concatenation cant be perfor,ed in sets

# repetition operator (won't support this operatio too )

# Type casting
weekdays = ("mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays,type(weekdays))
weekdays1 = set(weekdays)
print(weekdays1,type(weekdays1)) # also you can see by running different times your output is too changing the sequence of elements inside the brackets which means that they are non sequencial order

# add()
set2 = {2,3,4,5}
print(set2,type(set2))
set2.add(1)
print(set2,type(set2))
# if we are adding again existing element then it won't

# remove()
set2.remove(5)
print(set2,type(set2))
# if we try to remove non existing item from list then it shows 'type error'

# discard()
set2.discard(3)
print(set2,type(set2))
# difference between discard and remove is that if we are trying to remove the non existing element it shows error and if you try to discard the element which is not available then it will be showing no error
# if you are not sure about if either item present or not and to delete it from set so we can use discard instead of remove .

# so we can conclude from above' add remove and discard operations ' sets are "MUTABLE"

## Mathematical operations of sets
student1 = {"English","Biology","Physics","Python"}
student2 = {"English","Maths","Physics","Java"}
print(student1,type(student1))
print(student2,type(student2))

# if we wanna find common subjects between two students 1 and 2
# intersection (helps to find common between two sets)
# set1.intersection(set2) = common
common_subjects = student1.intersection(student2)
print(common_subjects,type(common_subjects))

# if we wanna know all the subjects of student1 and student2
# we need to use operation called 'union'
# set1.union(set2) = all items
all_subjects = student1.union(student2)
print(all_subjects,type(all_subjects))

# empty set = if there are no common items between sets
student3 = {"sanskrit","chemistry","computers"}
common_subjects = student3.intersection(student2)
print(common_subjects,type(common_subjects)) # this will be an empty set
common_subjects = student3.intersection(student2,student1)
print(common_subjects,type(common_subjects)) # this too will be an empty set

all_subjects = student3.union(student2,student1)
print(all_subjects,type(all_subjects))

print(weekdays1)
weekends = {"Sat","Sun"}
print(weekends)

# difference of sets
days = weekdays1 - weekends # days which are NOT in weekends
print(days)

### Frozen sets
setA = {1,2,3,4,0}
setA.add(5)
print(setA,type(setA))
# frozen sets are immutable
FsetA = frozenset({1,2,3,4,5,6})
print(FsetA,type(FsetA))
# FsetA.add(7)
# print(FsetA,type(FsetA)) cant be printed because we cant add anything in the set or remove because frozen sets are immutable
# intersection , union and differnce operations can be performed in frozen sets because they wont change any existing frosen sets
FsetB = frozenset({1,0,3,0,4,0,5})
print(FsetB,type(FsetB))
print(FsetA.intersection(FsetB))
print(FsetA.difference(FsetB))
print(FsetA.union(FsetB))
