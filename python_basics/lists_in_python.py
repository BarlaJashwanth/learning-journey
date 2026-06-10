### LISTS in python
## TOPICS :
# lists
# operations in lists
# number lists
# nested lists 

name = 'Jashwanth'
age = 20
percentage = 95.9
student = ['Jashwanth', 20, 95.9]
print(type(student))
print(student)
# A built in data structure used to store a collection of items in a single variable

day_of_week =           ["mon","Tue","Wed","Thur","Fri","Sat","Sun"]
#this too have indexing   0      1     2     3      4     5     6
#negetive indexing too    -7    -6    -5     -4    -3    -2    -1
print(day_of_week)
print(day_of_week[0])
print(day_of_week[-1])
print(f"first day of week is {day_of_week[0]}")

# slicing of lists
l1 = [3,8,1,0,4,9,7,3]
print(l1)
print(l1[1:8:1])
print(l1[2:7:2])
#slicing in lists is similar to slicing in strings

# concatenation of lists
l2 = ["these are numbers",2,"is missing"]
print(l2)
print(l1 +l2)

# Repetition of lists
print(l1*4)

# append()
# adds an item to the end of the list
fruits = ["mango","apple","banana"]
print(fruits)
# list.append(item)
fruits.append("watermelon")
print(fruits)
# here print(fruits.append("watermelon")) wont work because of a concept MUTABILITY which is not seen in strings while using replace function or any other function in strings .

# insert()
# adds as element before the specialised index
# list.insert(index, item)
fruits.insert(1,"coconut")
print(fruits)
fruits.insert(-1,"orange")
print(fruits)

# extend()
# adds an element end of the list
# diffence between append and extend is that append can add one item at a time but extend can add more than one item at end at a time to list
# list.extend(["A","B","C"])
fruits.extend(["dragonfruit","grapes"])
print(fruits)
print(len(fruits))
fruits.append(["coco","strawberry"])
print(fruits)
print(len(fruits))
# in just above example append is adding one list in other list if you check length before append and after append only +1 in increase we can see which ensures that append can add only 1 item at a time

# remove()
# list.remove(item)
fruits.remove(["coco","strawberry"])
print(fruits)
fruits.remove("mango")
print(fruits)
# if there are same multiple elements the first occurance will be deleted

# pop()
# deletes the element but based on index numbering
fruits.pop(2)
print(fruits)
fruits.pop(-5)
print(fruits)
fruits.pop()
print(fruits)
# list.pop() no indexing last or -1 will be delted by default

# reverse
# list.reverse()
print(day_of_week)
day_of_week.reverse()
print(day_of_week)

# sort
# list.sort()
numbers = [2,9,5,4,3,1,0]
print(numbers)
numbers.sort()
print(numbers)
# sort: helps to arrange numbers in ascending order
# then if we wanna arrange in descending order then ???
# list.sort(reverse=True)
numbers.sort(reverse=True)
print(numbers)

# count()
# list.count()
# helps to count how many times a element got repeated in the list
numbers1 = [2,2,2,0,5,3,6,9,4,2,6,9,0,4,1,4,6,7,8,8,8,4,]
# no mutabilty here because its just giving an output of how many times element is present it is not changing its current list .
print(f"numbers1 is {numbers1}")
number_to_be_counted = int(input("enter the number to be counted from the above list"))
print(f"occurrence of your selected number in list numbers1 is :{numbers1.count(number_to_be_counted)}")

# membership
# in
language = ['python','java','c+','c++']
# print("item" in list) if it is present true or false
print(language)
print("Telugu" in language)
print("python" in language)
print("Python" in language)
print('python' in language)
# not in
print("Telugu"  not in language)
print("python"  not in language)
print("Python"  not in language)
print('python'  not in language)

### OPERATIONS OF LISTS CONTATINING SPECIALLY NUMBERS
numbers2 = [10,4,5.5,7,-1,20]

# smallest numbers in the list
# min()
# min function can be used for other data types also
# print(min(list))
print(numbers2)
print(min(numbers2))

# biggest number in list
# max()
print(max(numbers2))
print(f"Smallest number is : {min(numbers2)} and biggest number is : {max(numbers2)}")
# if a string is inserted in above numbers2 list then we cant use min and max functions

# Total of the numbers in the list
# sum()
print(f"total : {sum(numbers2)}")

### NESTED LISTS
# list inside a list
l3 =        [1,2,3,4,5,6,7,8,9,[2,3,4,5,6,7,8,9,0],[3,4,5,6,7,8,9,0],[4,5,6,7,8,9,0]]
# indexing : 0,1,2,3,4,5,6,7,8,       9,                  10,             11
# in this case the length of the list will be 12 why beacuse [] inside brackets will be as a sub list under the main list
print(l3)
print(l3[8])
print(l3[-9])
print(len(l3))

# CHAIN INDEXING : When we have sub list then we can also find the element in that by chain indexing
print(l3[9][0])
print(l3[10][-1])
# there is no limitation for creating list inside list inside list you can make how much as you want
l4 = [1,2,3,[1,2,3],[1,[2,6]]]
print(l4)
print(len(l4))
# if you wanna print number 6 by indexing then below code will be perfect in which chain indexingis done
print(l4[-1][-1][-1])
