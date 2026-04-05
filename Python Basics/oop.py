# OOP (Object-Oriented Programming) in Python

# creating a basic class
class student:
    pass

s1 = student()


# class with attributes and methods
class sstudent:
    cllg = 'csun'  # class variable shared by all objects

    def __init__(self, name, age): # constructor
        self.name = name  # instance variable
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}"

s = sstudent("kripa", 25)
s.greet()
sstudent.cllg = 'mbit'  # updated class variable for all objects


# Encapsulation
# protects data and prevents misuse
# hides data and allows controlled access

class exampleencap:
    def __init__(self):
        self._marks = 10   # protected - accessible in subclass
        self.__id = 13     # private - cannot access outside class

s11 = exampleencap()
print(s11._marks)


# @property lets you access a method like an attribute while keeping control
# @setter allows validation before setting a value
# without setter you cannot modify the variable from outside the class

class eg:
    def __init__(self):
        self._marks = 0

    @property
    def marks(self):        # getter
        return self._marks

    @marks.setter
    def marks(self, value): # setter with validation
        value = int(value)
        if value >= 1:
            self._marks = value
        else:
            print("invalid marks")

obj1 = eg()
obj2 = eg()
obj2.marks = 10
print(obj2.marks)    # getter called
obj1.marks = -2      # setter called, prints invalid
print(obj1.marks)    # still 0 because setter rejected it


# Inheritance
# child class acquires properties and methods from parent class
#
# types:
# single       A -> B
# multilevel   A -> B -> C
# multiple     A, B -> C
# hierarchical A -> B, A -> C
# hybrid       mix of above
#
# MRO (Method Resolution Order)
# the order python follows to resolve method calls
# prevents ambiguity in multiple inheritance

class GP:
    def __init__(self, name):
        self.name = name
        print("GP here")

class parent(GP):
    def __init__(self, name, age):
        super().__init__(name)  # calls GP __init__
        self.age = age
        print("Parent here")

class child(parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # calls parent __init__
        self.grade = grade
        print("child here")

c = child('krupa', 20, 'a')
# prints: GP here -> Parent here -> child here


# Abstraction
# hides implementation details, shows only essentials

from abc import ABC, abstractmethod

# abstract class cannot be instantiated
# child class must implement all abstract methods

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("car starts with key")

class bike(vehicle):
    def start(self):
        print("bike start with kick")

# same method name, different behavior for each class
veh = [car(), bike()]
for v in veh:
    v.start()


# Polymorphism
# same interface, different behavior

# compile time - method overloading
# python doesnt support overloading like java
# instead we use default arguments

class math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = math()
print(m.add(2, 3))      # uses 2 args
print(m.add(1, 2, 3))   # uses 3 args


# runtime - method overriding
# child class redefines the parent method

class parent:
    def show(self):
        print("hello parent")

class child(parent):
    def show(self):
        print("hello child")

c = child()
c.show()  # calls child version, not parent


# overriding but also calling parent method using super()

class parent:
    def show(self):
        print("hello parent")

class child(parent):
    def show(self):
        super().show()       # calls parent method first
        print("hello child")

c = child()
c.show()  # prints both parent and child