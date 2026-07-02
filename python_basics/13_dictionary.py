### DICTIONARIES : comma separated key:value pairs enclosed within {} and each key:value pair are separated by commas
## {'key1':value1, 'key2':value2, 'key3':value3, .....}
# dictionaries are used for example in supermarket we have item names and their prices too so we can use in the format of key:value pair

groceries = {'milk':32, 'Buiscuits':20,'rice':100,'bread':45}
print(groceries,type(groceries))
print(len(groceries))

# print(groceries(0)) this is indexing which is showing 'type error'
# No indexing

# but we can get values using key not indexing
# syntax: print(dictionary["key"])
print(groceries["milk"]) # u will get value of milk
print(groceries["rice"])

# If the value need to be changes can we modify ?? that means are dictionaries are mutable ???
# DICTIONARIES are MUTABLE !!!
groceries["rice"] = 102 # updates the key:value pair
print(groceries)
print(groceries["rice"])
# print(groceries["eggs"]) "key error" because that key is not available in the dictionary

# if you wanna add anything new key:value pair to dictionary then
groceries["egg"] = 6 # adds new key:value pair to dictionary
print(groceries)

### OPERATIONS ON DICTIONARIE
student1 = {'maths': 95, 'english': 92,"physics": 95}
print(student1,type(student1))

## fetch the marks for phy
print(student1["physics"]) # without get() he is using square brackets
# get()
print(student1.get("physics")) # with get function paraenthesis are used
# while using get() if the key value is not present it gives output 'none' if normal fetching is done
# of a subject without get() for the key value which is not present gives "key error"
# print(student1["Telugu"])  this will be an error
print(student1.get("Telugu")) # None

emp1 = {"id" : 1001,"name" : "Jash" , "salary":10000000}
print(emp1,type(emp1))
print(emp1.get("id"))
print(emp1.get("phone number",9700313655)) # here phone number is not present the reason why it shows default value itself
print(emp1.get("id",6767)) # here even default value given but from before the key value exists the output will be not default value

# membership
# in
print(1001 in emp1) # false because it checks the only key
print("name" in emp1) # true because it has key word
# not in
print(1001 not in emp1)
print("name" not in emp1)

# update function
sem1={"math": 98,"chem":99}
sem2={"phy":97,"biology":96}
sem1.update(sem2)
print(sem2)
print(sem1)
sem2.update(sem1)
print(sem1)
print(sem2)

groceries_1 = {"milk": 32, "rice": 100, "bread": 45}
groceries_2 = {"milk": 33, "choclate": 45}
print(groceries_1,type(groceries_1))
print(groceries_2,type(groceries_2))
groceries_1.update(groceries_2) # here in both groceries 1 and 2 there is milk but costs are differnt one is 32 and other is 33 so it updates the milk value
print(groceries_1)
groceries_2.update(groceries_1)

# deletion (pop)
groceries_1.pop("milk") # both key and value pair erases
print(groceries_1)

# repetetive key values in dictionaries
groceries_3 = {"milk": 20 , "rice": 34 , "choco":78 , "milk": 45} # here the python read dictionaries from right to left so if two keys are repeating it takes right most one
print(groceries_3,type(groceries_3))

# d = {[1,2,3]: 9,[3,2,1]: 4} # Here key is "list"
# print(d1,type(d1))

d1 = {"one": 1 , "two": 2} # Here key is "String"
print(d1,type(d1))

d2 = {1:True, 0: False} # Here key is "integer"
print(d2,type(d2))

d3 = {1.0:True, 0.0:False} # Here key is "float"
print(d3,type(d3))

d4 = {True:1 , False:0} # Here key is "boolean"
print(d4,type(d4))

d5 = {(1,2,3,):6,(2,3,4):9} # Here key is "tuple"
print(d5,type(d5))

# d6 = {{1,2,3,}:6,{1,2,4}:7} # Here key is "set"
# print(d6,type(d6))

# d7 = {{"a":1,"b":2}:6} # Here key itself is other "dictionary"
# print(d7,type(d7))

# so allowed keys are : String , floats , integers , Boolean , Tuple
# not allowed keys are : sets , lists , dictionaries
## why so ???
# lists,  sets , dictionaries are "mutable" they can be changed so cant be used in keys
# That means keys of a dictionary can only be mutable datatypes ...
# Value can be any data type

d8 = {"stu1":[1,2,3], "stu2":{4,5,6}} # here value is "list" and "set"
print(d8,type(d8))
print(d8["stu1"][1]) # indexing done for list value here
# print(d8["stu2"][1]) # here the indexing wont work as it is set
print(d8.keys(),type(d8.keys())) # data type is dict_keys
print(d8.values(),type(d8.values())) # data type is dict_values .

# items()
print(d8.items(),type(d8.items())) # here we get both key and values of a dictionay but seperated by comma .
