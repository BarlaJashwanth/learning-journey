# ## Opening a file in python
# # open("file_name", "mode_to_open")
# # Modes: r, x, w, a, t, b    ("rt" is the default mode:if u leave blank input will be "rt")
#
# file_handler = open("practise.txt","rt")
# print(file_handler)
#
# # Read operation
# print(file_handler.read())
#
# # Closing a file
# file_handler.close()
#
# # Read operation
# # print(file_handler.read())    => this cant work now as we already closed the file we can multiple times close a file but after closing we cant do any action on it we need to open it again before doing any action like read or edit
#
#
# ## Creating_files
# # X mode for creating file
# fh = open("file.txt","xt")
#
# # writing into a file
# # write(content)
# fh.write("This file is created using the 'x' mode in python.\n")
# fh.write("Next line.")
#
# # close the file
# fh.close()

# w mode : file handling is opening the file for writing.
fh = open("file.txt","wt")
fh.write("This file is over written using w mode. \n")
fh.write("have a nice day !")
fh.close()
# while using w mode and file dosent exists then it creates the new file and helps to write if already exists it overwrites

fh2 = open("file1.txt","wt")
fh2.write("this is new file for creating and write content into it\n i made this file for learning the concepts of file handling")
fh2.close()

## Read operation
# read() => reads the content of file as string if it is text mode
fh2 = open("file1.txt","rt")

#read operation
# read() => reads the content of the file as string
# if you wanna read only first some characters of file then we can use
content = fh2.read(2)

# this helps to read remaining content of the file
content2 = fh2.read()

#readline()
content3 = fh2.readline(1)

# closing operation
fh2.close()

print(content)
print(type(content))
print("=========")
print(content2)
print("=========")
print(f"line:{content3}") # empty string : it means file has reached end of file (eof) ...

# read lines : lines = fh2.readlines()
# print(lines)
# output : ['statement 1.\n', 'statement 2.\n', 'statement3.\n']  => in this way we get a list not strings differnce between read and lines
# for removing that \n from lines we can use print(line.rstrip('\n'))
# it will strip out the \n from every lines ...







