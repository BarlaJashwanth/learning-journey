# os.path.exists() : helps to check weather fil exists or not
# already we have practise.txt file and no practise1.txt file


import os
file_name = "practise.txt"
if os.path.exists(file_name):
    print("File exists")     # this will be the output file exists
else:
    print("File does not exist")


# pathlib.path.exists()
from pathlib import Path
file_path = Path("practise1.txt")
if file_path.exists():
    print("File exists.cannot create")
else:
    print("File does not exist,creating it")
    fh = open(file_path, "xt")
    fh.write("hello world")
    fh.close()



# ### ERRORS in FILE HANDLING :

# 01] File not found error : if we are trying to read a file which is not even existing then we get thus error
# fh = open("practise2.text","rt")
# content = fh.read()
# fh.close()
# print(content)

# 2.a] Unsupported operation error :if we are opening a file with one operation but making it to perform other operation then we get this error
# fh = open("practise.txt","rt")
# fh.write("hello world")
# fh.close()
"""
in above case we opened file in read mode but doing write function which is unsupported function
"""

# 2.b] unsupported operation
# fh = open("practise1.txt","wt")
# content = fh.read()
# fh.close()
"""
This above mistake is also a unsupported operation but the file which is already existing by using w it makes the information inside the file to vanish
"""

# 3] File exists error :
# fh = open("practise.txt","xt")
# fh.write("hello world")
# fh.close()
"""
As i already told when file is already existing we cant use x function ...
"""









