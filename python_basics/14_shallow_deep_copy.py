# these concepts are for mutable data types

import copy

l1 = [1,2.5,[10,20,30],'python']

# shallow copy : as we previously learned for python storing there will be a memmory address if we use
# shallow copy then it just copies the items but without copying the memory adress new list get created with differnt memory adress but with same itmes
l2 = copy.copy(l1)
print(l1,id(l1))
print(l2,id(l2))

l1[0] = 10       # assigned new value now
print(l1,id(l1)) # only this get updated
print(l2,id(l2)) # still same as previous

l1[2][0] = 100   # assigned new internal value
print(l1,id(l1)) # this got updates as known
print(l2,id(l2)) # even this got updated
# this because of memory adress

### Deep copy (memory adress too get copied)
l3 = [10,20,30,[1,2,3]]
l4 = copy.deepcopy(l3)
print(l3,id(l3))
print(l4,id(l4)) # now both also have same memory address too
l3[2] = 300
l3[3][1] = 100
print(l3,id(l3))
print(l4,id(l4)) # now we can observe while deep copy no outer element or inner element is changing in copying list

# summary :
# shallow copy : is creating a new list at differnt memory location the inner elements of list does'nt get copied if in any changes are made for copied list it gets effected in original list
# deep copy : the inner elements are having diffenrt memory location so any change made here won't get reflected

### LOOPS
l = ['jashwanth',19.9,2006] # if you want to print this but every item shold be in new line then we have to use "for" operation before printing
for x in l:
    print(x) # check output every item will be in new line
for x in ['jashwanth',19.9,2006]: # even this will give same output as previous
    print(x)

    x = "apple"
    for i in x:
        print(i) # in this case apple each letter will be in differnt new lines

### if you want to print anyhting code line multiple times we can use "for" loop
## if you wanna print Jashwanth 10 times then
for i in range(1,11):
    print('Jashwanth')

