### JSON module : JavaScript Object Notation
"""
JSON is a plain text format used to store and share data that looks
almost exactly like a python dictionary
"""
# Json : human readable format for data storage ...
# it can be used in python and other programing languages too

import json

students = {'student1':{'name':'Jash','roll no':100,'percent':99.5,'sports':True},
            'student2':{'name':'Shiny','roll no':101,'percent':99.0,'sports':False},
            'student3':{'name':'rishi','roll no':102,'percent':98,'sports':False}}

print(type(students),students)
print('========================')
# If we wanna keep this data in JSON file than ,
# dump() : makes data to dump inside json file ...

with open('students.json', 'w') as fh:
    json.dump(students, fh,indent=4) ### In Python's json module, the indent parameter is used to format and "pretty-print" your data so it is easy for humans to read.
"""
Remember in json files data booleans are not kept in capital as True and False rather it keeps 
true and false and also double coated strings instead of single coated
"""

# for reading the json file we have load function

# load()
with open('students.json', 'r') as fh:
    students = json.load(fh)

print(type(students),students) # this gives dictionary and json file data


# for updating the data inside a json file
# update()

# read the old data from json file

students = {'student1':{'name':'Jash','roll no':100,'percent':97.5,'sports':True},
            'student2':{'name':'Shiny','roll no':101,'percent':99.0,'sports':True},
            'student3':{'name':'rishi','roll no':102,'percent':93,'sports':False}}
with open('students.json', 'r') as fh:
    data = json.load(fh)
    data.update(students) # update operation

# dump - write the updated data in the json file
with open('students.json', 'w') as fh:
    json.dump(data, fh,indent=4)









