"""
Python is an interpreted language.

It reads code line by line, converts it into bytecode, and executes it using
the Python Virtual Machine (PVM).
"""

# number types
a = 10          # integer
b = 2.3         # float
c = 2 + 1j      # complex number

# boolean
d = True

# string
text = "Machine Learning"

# sequence types include list, tuple, set
# mapping type is dictionary

# binary
e = bytes(4)   # creates 4 empty bytes
type(e)

"""List - mutable, ordered, changeable, allows duplicates"""

courses = ['history', 'math', 'comp', 'ml', 'ai']
print(courses)

print(len(courses))  # length of list

print(courses[2:])   # slicing from index 2 to end

print(courses[:2])   # slicing from start to index 1

courses.append('ds')  # adds item at end
print(courses)

courses.insert(1, 'dl')  # insert at specific index
print(courses)

list2 = ['sd', 'fend']

courses.append(list2)  # adds entire list as one element
print(courses)

courses.extend(list2)  # adds each item separately
print(courses)

courses.remove('math')  # removes specific item
print(courses)

courses.pop()  # removes last item by default
print(courses)

courses.reverse()  # reverses list
print(courses)

num = [3, 6, 8, 1, 0]
num.sort()  # ascending order
print(num)

num.sort(reverse=True)  # descending order
print("rev:", num)

print(min(num))
print(max(num))
print(sum(num))

print(courses.index('dl'))  # find index of item

print('art' in courses)  # check if element exists

for item in courses:
    print(item)

for index, i in enumerate(courses):
    print(index, i)

for index, i in enumerate(courses, start=1):
    print(index, i)

courses.pop(1)  # remove item at index 1

# convert list to string
cstr = ','.join(courses)
print(cstr)

# convert string back to list
nc = cstr.split(',')
print(nc)

# list comprehension
y = ["Even" if x % 2 == 0 else "odd" for x in range(5)]
print(y)

# nested comprehension
[(i, j) for i in range(3) for j in range(2)]

"""Tuples - immutable, ordered, allow duplicates but cannot be changed"""

tuple1 = ('art', 'ai', 'ml', 'dl')
tup2 = tuple1
print(tuple1)
print(tup2)

# tuple1[0] = 'ds'  # error because tuple is immutable

"""Set - unordered, no duplicates, mutable"""

csc = {'ml', 'cs', 'ai', 'ml'}
print(csc)

print('cs' in csc)

cscc = {'ai', 'art', 'museum', 'geo'}
print(csc.intersection(cscc))  # common elements
print(csc.union(cscc))         # all elements
print(csc.difference(cscc))    # elements only in csc

# set is mutable, frozenset is immutable
s = frozenset([1, 2, 3])
print(s)

"""Dictionary - ordered, mutable, keys must be unique"""

student = {
    'name': 'kripa',
    'age': 24,
    'gpa': 3.9
}
print(student)

print(student['name'])  # access value by key
print(student.get('phone'))  # safe access

student['phone'] = 333  # add new key
print(student)

student.update({'age': 25})  # update value
print(student)

del student['age']  # delete key
print(student)

student.pop('gpa')  # remove and return value
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for i in student:
    print(i)

"""Conditional statements"""

score = 90
if score >= 90:
    grade = 'a'
elif score >= 70:
    grade = 'b'
else:
    grade = 'c'

# identity operator (used with True, False, None)
x = True
if x is True:
    print("hhhiiii")

# ternary operator
score = 50
result = "pass" if score >= 75 else "fail"
print(result)

"""Loops"""

# for loop
for i in range(1, 5, 2):
    print(i)

# while loop runs until condition becomes false
i = 0
while i < 5:
    print(i)
    i += 1

# zip combines two lists
for x, y in zip([1, 2], [3, 4]):
    print(x, y)

# enumerate gives index and value
for i, v in enumerate(['a', 'v', 's', 'f'], start=1):
    print(i, v)

square = [x * x for x in range(3)]
print(square)

"""Functions
Parameters: variables in function definition
Arguments: values passed when calling function
"""

def add(a, b):
    return a + b

add(2, 3)  # positional
add(a=2, b=3)  # keyword

def power(x, p=2):  # default argument
    return x ** p

print(power(3))

# variable length arguments
def total(*args):
    return sum(args)

def info(**kwargs):
    return kwargs

arr = [1, 2, 3, 4]
print(total(*arr))

data = {
    'name': 'krupa',
    'id': 1,
    'phone': 22
}
print(info(**data))

# lambda functions
square = lambda x: x * x
print(square(3))

add = lambda a, b: a + b
print(add(1, 2))

# map applies function to each element
a = [1, 2, 3]
b = [3, 4, 5]
print(list(map(lambda x, y: x + y, a, b)))

# filter selects elements based on condition
num = [1, 2, 3, 4, 56, 67, 8, 90, 4]
print(list(filter(lambda x: x % 2 == 0, num)))

# reduce aggregates values
from functools import reduce
print(reduce(lambda x, y: x - y, [1, 2, 3, 4]))

"""Generator
Uses yield instead of return, memory efficient

Decorator
Function that modifies another function

Error handling
Prevents program from crashing
"""

try:
    x = int('a')
except ValueError as e:
    print("invalid input", e)
finally:
    print("done")

def setage(age):
    if age <= 0:
        raise ValueError("age must be greater than 0")
    return age

setage(2)

# custom exception
class invaliderrors(Exception):
    pass

def setlr(lr):
    if lr <= 0:
        raise invaliderrors("learning rate must be > 0")
    return lr

"""Debugging and logging"""

import pdb
def calc(a, b):
    # pdb.set_trace()
    return a / b

calc(10, 2)

# logging keeps track of events
import logging
logging.info('mssg')