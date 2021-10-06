# 6.   Experiment with module reloads: perform the tests in the changer.py
# example, changing the called function’s message and/or behavior repeatedly,
# without stopping the Python interpreter.
# Depending on your system, you might be able to edit changer in another window.

# The reloads() function in python reloads the previously imported module
from mypkg import mymod as md
f = open('mypkg/mymod.py', 'r')
import importlib
importlib.reload(md) #returns module object
print(md.test(f))