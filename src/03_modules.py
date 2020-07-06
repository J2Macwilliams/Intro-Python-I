"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("Name of the script: ", sys.argv[0])
print("Argument List:", str(sys.argv)) 


# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS platform:", sys.platform)

# Print out the version of Python you're using:
print("Python Version:", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current Process ID:", os.getpid())

# Print the current working directory (cwd):
print("cwd:", os.getcwd())

# Print out your machine's login name
print("Machine's Login Name:", os.getlogin())
