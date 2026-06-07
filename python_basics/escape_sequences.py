# \n - new/next line
# \t - tab
# \\ - backslash
# \' - inserts a single quote inside a single-quoted string
# \" - inserts a double quote inside a double quoted string

#\n
print("hello everyone,\nmyself jashwanth")

#\t
print("hello everyone")
print("hello\teveryone")

#\\
#print("new\old") but may give warning sometimes
print("new\\old")

#\'
#print('This is Python's class') wont work beacuse after 's class will be unidentified by python
print("This is python's class")
print('This is python\'s class')

#\"   same as \'