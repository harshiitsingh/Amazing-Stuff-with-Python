'''
The task are :

    1. go to a specific folder
    2. create a virtual environment in that folder
    3. go inside the virtual environment folder and then activate the virtual environment
    4. install django using pip command
I am using subprocess module in python and for now I am able to achieve till step 2

Here is the code :
'''

import os
import subprocess

path = input("Enter the path where you want to create the venv :") #'/var/www'

try:
    os.chdir(path)
    print("Current working directory: {0}".format(os.getcwd()))
except FileNotFoundError:
    print("Directory: {0} does not exist".format(path))
except NotADirectoryError:
    print("{0} is not a directory".format(path))
except PermissionError:
    print("You do not have permissions to change to {0}".format(path))

# cwd = os.getcwd()

# change_dir = os.chdir(cwd)

# to create a virtual env
virtualenv = input('Enter the name of virtual env : ')

#run the python virtualenv command
p1 = subprocess.run('python -m virtualenv {}'.format(virtualenv),shell=True)


virtualenv = os.path.join(os.getcwd(), virtualenv)

#go inside the virtual env folder
os.chdir(virtualenv)

#activate the virtual environment
p2 = subprocess.run(r'.\Scripts\activate.bat',shell=True)