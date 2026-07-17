### THE 'with' STATEMENT:
"""
The with statement in Python is a tool used
to safely manage resources like files, network
connections, or database locks. It ensures that
these resources are automatically cleaned up or
closed when you are done, even if your code crashes
or runs into an error.
"""
# fh = open("practise.txt","rt") # fh = file handler
# contents = fh.read()
# fh.close()
# print(contents)

### This above procedure is normally done manually
### after work we need to close the file manually

### Now by using 'with' statement
with open("practise.txt","rt") as fh:
    contents = fh.read()

print(contents)
# Here we havent closed function when we used with function .
