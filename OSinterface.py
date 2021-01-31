import os
print(os.getcwd())  # return the current working directory

os.chdir('../')  # change current working directory
if 'today' not in os.listdir():
    os.system('mkdir today')  # run the command mkdir in the system shell

# the built-in dir() and help() functions are useful 
# as interactive aids for working with large modules
# like os
# dir(os)
# help(os)


# For daily file and directory management tasks,
# the "shutil" module provides a higher level interface
# that is easier to use
import shutil
"""
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
"""

# The "glob" module provides a function for 
# making file lists from dicectory wildcard searches
import glob
print(os.getcwd())
os.chdir('Learn_')
print('change dir to ', os.getcwd())
print(glob.glob('*.py'))

# command line arguments
# arguments are stored in the sys.module's 
# 'argv' attribute as a list
import sys
print(sys.argv)  # no arguments
# 'getopt' module processes sys.argv using the 
# conventions of the Unix getopt() function,
# more powerful and flexible command line 
# processing is provided by 'argparse' module


# Error output redirection and program termination
sys.stderr.write('Warning, this is an information which contain sensative content')
'''sys.exit()  # to terminate a script'''


# string matching, regualr expressions
import re
print('\n',re.findall(r'\bf[a-z]*', 'which foot and hand fell feastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat'))
'tea for too'.replace('too', 'two')


# Mathematics
import math
print(math.cos(math.pi / 4))
print(math.log(1024,2))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100),10))  # sampling without replacement
print(random.random())  # random float
print(random.randrange(6))  # random integer chosen from range(6)

import statistics
data = [2.75, 1.75, 1.25, 0.5, 1.25, 3.5]
print('data: ', data)
print('mean: ', statistics.mean(data))
print('median: ', statistics.median(data))
print('variance: ', statistics.variance(data))