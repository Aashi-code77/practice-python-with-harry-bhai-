# write a python program to print the contents of a directory using the os module. search online for the function which does that. 
# label the program written in problem 4 with comments.
import os

# specify the directory you want to list
directory_path = '/'

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name 
for item in contents:
    print(item)