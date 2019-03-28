# Check if we can use IPython console instead

# The "compulsory" Hello world program
print("Hello World")

###########################
# DATA TYPES
###########################

# First type: Boolean
x = True
y = 100 < 10
y
x * y
x + y

# Numeric data (integers and floats)
a = 3
b = 2
a + b
a * b

# Exact division (real numbers)
a / b

# Integer division
a // b
c, d = 2.5, 10.0

# Complex numbers
z = complex(1, 2)
z

# Strings
x = "I am a string"
y = "... and I am a string too"

# String methods:
x.upper()
x.lower()
x.capitalize()
x.split(" ")
x.find('string')
y.replace('.', '*')

# Tells us the type of the object
type(x)

x + y
x * 2

'test ' * 2
"test " * 2

###########################
# CONTAINERS
###########################
# These are objects that contain other objects.

# LISTS
x = [1, 'a', 2.0]
x
x[0]
x[2]
x[-1]
x[-2]

x[0] = 'pablo'
x  # The new list is now modified

# List can be used for arrays
v = [0.5, 0.75, 1.0, 1.5]
m = [v, v, v]
m[0][0], m[1][0]

# Slicing
v[1:]

# Last index not included
v[1:3]

# Last but one
v[:-1]

# Read the list in reverse order
v[::-1]

# Lists copy values by reference!
v[0] = 'hi'

# Values of m have now changed
m

# To avoid this, you can use deepcopy
from copy import deepcopy
v = [0.5, 0.75, 1.0, 1.5]
m = [deepcopy(v), ]
print(m)

v[0] = 'hi'
print(m)

#  TUPLES
y = (1, 'a', 2.0)
y
type(y)
y[0]
y[0] = 'something'  # Error! You can not overwrite tuples

# Unpacking: Storing the information of an object in different parts

names = ('Juan', 'Pablo', 'Maldonado')
first_name, second_name, last_name = names
first_name

# Parse a string into a list
single_line = 'pablo,maldonado,zizkov'
my_data = single_line.split(',')
my_data

# put it again together
new_single_line = ','.join(my_data)
new_single_line

# SETS

s = set(['u','d', 'ud', 'd'])
t = set(['d', 'du'])
s.intersection(t)
s.union(t)
s.difference(t)
s.symmetric_difference(t)

# Sets are useful for removing duplicates
from random import randint
l = [randint(0,10) for i in range(1000)]
len(l)
set(l)


# DICTIONARIES

d = {'name': 'Pablo', 'last_name': 'M'}
type(d)
d['name']
d['last_name']
d.keys()
d.items()
del d['name']

################################
# CONTROL STRUCTURES
################################

x_vals = [1, 2, 3, 4, 5]
for x in x_vals:
    print(x * x)

# Sum of squares
total = 0
for x in x_vals:
    total = total + x * x
total

# The Python way: Using list comprehension!
sum([x * x for x in x_vals])

# List comprehension is a very useful way of doing loops "faster"
[x * x for x in x_vals]

# Ranges of numbers:
my_vals = range(1, 20)

# Run the following. What does it print?
for i in my_vals:
    print(i)

my_vals

# Calculating squares in two different ways
sum([x * x for x in my_vals])
sum([x ** 2 for x in my_vals])

# Example: Calculate the distance between two vectors

####
from math import sqrt

x = [3, 0]
y = [0, 4]
dist = 0
for i in range(len(x)):
    dist += (x[i] - y[i]) ** 2
dist = sqrt(dist)
dist


# How can we re-write this?
def my_dist(x, y):
    dist2 = sum([(x[i] - y[i]) ** 2 for i in range(len(x))])
    dist = sqrt(dist2)
    return dist