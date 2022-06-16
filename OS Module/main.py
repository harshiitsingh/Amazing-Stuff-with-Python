# https://www.youtube.com/watch?v=tJxcKyFMTGo
'''
os module allows us to interact with the underlying
operating system in several different ways.
So for example we can navigate the file system, get file information,
look up and change the environment variables, we can move files around
and all kind of useful stuff.'''

import os # built-in module, so no need to install any 3rd party library or anything like that

print(dir(os)) # print all of the attributes and methods which one can access within this module

print(os.getcwd()) # print the current directory, get current working directory.

# to navigate to desktop here
os.chdir('/Users/Harshit Singh/Desktop/') # change directory
print(os.getcwd())

# to get list of directories
print(os.listdir())

# to make a new folder
# os.mkdir('OS-Demo') # Method-1
os.makedirs('OS-Demo') # makedirs is used to create a directory that are few levels deep then
# makedirs will create all of the intermediate level directories that you need 
# and makedirs won't do that, like:
# os.mkdir('OS-Demo/Sub-Dir-1') # it will give an error, cuz top level directory(OS-Demo) doesn't exist yet
os.makedirs('OS-Demo/Sub-Dir-1') # so most preferable method to use

# to delete the folder
os.rmdir('OS-Demo') # will not delete intermediate dir
os.removedirs('OS-Demo') # it will delete

# to rename the file or dir
os.rename('text.txt', 'demo.txt')

# to print the information about the file
print(os.stat('demo.txt')) # look online for the meaning of result shown by the stat
print(os.stat('demo.txt').st_size) # size of the file 
print(os.stat('demo.txt').st_mtime) # last modification time, but it returns a timestamp and mostly people don't know how to read a timestamp and a human readable format, so:

from datetime import date, datetime
mod_time = print(os.stat('demo.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))
# this is really useful if you are working with a web application that has a lot of files that has been updated or created recently
# and you wanna know exactly when that was then this is the good way you can do that within python.

# to traverse all the directory trees and want to print all of the directories and the files
for dirpath, dirnames, filenames in os.walk('/Users/Harshit Singh/Desktop/'): # or os.walk(os.getcwd())
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

    # this can be extremely useful if say that I had a file somewhere within one of the folders of my desktop
    # but I didn't remember exactly where it was, then it will search or go through all of those files and folders on the desktop.

    # or if you had a web application and you wanted to keep track of all of the file information within a certain directory structure
    # then just go through this os.walk() method which will go through all of the files and folders within your web application
    # and collect file information.

# to get environment variables
# print(os.environ) # will print all of the environment variables
print(os.environ.get('HOME')) # want to just get the home environment variable
# to create a new file within the home directory
# file_path = os.environ.get('HOME') + 'test.txt' # not relevent method, sometimes miss slashes and double slashes
# print(file_path)

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# with open(file_path, 'w') as f:
    # f.write

# to grab the filename of any path that we're working on and this doesn't have to be real path
print(os.path.basename('/tmp/test.txt')) # this path doesn't exist
# to get the directory name
print(os.path.dirname('/tmp/test.txt')) # this path doesn't exist
# to get both dir name and file name
print(os.path.split('/tmp/test.txt')) # this path doesn't exist # fake path

# to check whether the path exist or not
print(os.path.exists('/tmp/test.txt')) # return False
# sometimes files named without extension so to check whether something is directory or file
print(os.path.isdir('/tmp/sdnknk')) # return True
print(os.path.isfile('/tmp/sdnknk')) # return False

print(os.path.splitext('/tmp/test.txt')) # it will split the file root (or root of the path) and the extension
# it is lot easier to do rather than string slicing or anything like that
# it's lot easier just to split it off and then take the first value if you want the file name without the extension
# it's lot used in file manipulation

print(dir(os.path))