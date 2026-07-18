### Pickle module :
"""
The pickle module is a built-in Python tool
used to convert complex Python objects
(like lists, dictionaries, or custom classes)
into a stream of bytes, and vice versa.
This allows you to save the exact state of
your Python data to a file or send it over a network and load it exactly as it was later
"""

students = {'student1':{'name':'Jash','roll no':100,'percent':97.5,'sports':True},
            'student2':{'name':'Shiny','roll no':101,'percent':99.0,'sports':True},
            'student3':{'name':'rishi','roll no':102,'percent':93,'sports':False}}

print(students,type(students))

# storing this data in text file first
# with open('students_information.txt','xt') as fh:
#     fh.write(str(students))
# fh.close()


"""
we saved the data in text file
"""
with open('students_information.txt','rt') as fh:
    content = fh.read()
print(type(content))  ### this will be string now dictionary information got transformed into string so data type by saving in text file got changed
### this is the reason why pickle module came into play

import pickle
# serialization : process of giving input inside pickle module
students = {'student1':{'name':'Jash','roll no':100,'percent':97.5,'sports':True},
            'student2':{'name':'Shiny','roll no':101,'percent':99.0,'sports':True},
            'student3':{'name':'rishi','roll no':102,'percent':93,'sports':False}}
# pickle module runs in binary format
with open("students.bin","bw") as fh:
    for student in students:
        pickle.dump(students[student],fh)

# Deserialisation : taking data from pickle module into pycharm
with open('students.bin','rb') as fh :
    print(pickle.load(fh))
    print(pickle.load(fh))
    print(pickle.load(fh))

"""
By using this pickle module we imported the data from binary language into dictionary 
but in case of text file it stored in format of text
JSON : anyone can read 
PICKLE : binary language only python can understand
"""

# in above case we knew that there are 3 dictionaries so we peinted 3 times what if we dont know then what to do ???
# we can use loop

print('================================')

### Pickle Exception handling :
students = {'student1':{'name':'Jash','roll no':100,'percent':97.5,'sports':True},
            'student2':{'name':'Shiny','roll no':101,'percent':99.0,'sports':True},
            'student3':{'name':'rishi','roll no':102,'percent':93,'sports':False}}
print(students,type(students))

print("========================================")

# Serialisation :
with open("students.bin","wb") as fh:
    for student in students:
        pickle.dump(students[student],fh)

# Deserialisation :
with open('students.bin','rb') as fh:
    # data1 = pickle.load(fh)
    # print(data1,type(data1))
    # data2 = pickle.load(fh)
    # print(data2, type(data2))
    # data3 = pickle.load(fh)
    # print(data3, type(data3))
   #data4 = pickle.load(fh)     '''''' This will give run time error as there is no 4th dictionary
   #print(data4, type(data4))   '''''' it shows "EOFError" for fixing this we need exception handling in pickles
    while True:
        try:
            data = pickle.load(fh)
            print(data,type(data))
        except EOFError:
            print("Done")
            break

print("=====================")

""""
This above code helps us to run one time and all dictionaries came while printing once and instead of typing printing multiple time
equal to the dictionary length to get all output
"""

# print the names of student who are participating in sports
with open("students.bin","rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data["sports"] == True:
                print(data['name'])
        except EOFError:
            print("Only these students are playing the sports")
            break



