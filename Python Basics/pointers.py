"""Python has pointers, it just doesn't expose them to you. 
You get the benefits without the risks. 
That's why id() exists — it shows you the memory address python is using behind the scenes.
# immutable (int, string, tuple) - points to a new object
# mutable (list, dict, set) - points to the same object
Garbage collection : When no variable is pointing to a value anymore, 
Python deletes that value from memory. You don't have to do it manually."""

n1 = 10
n2 = n1

print("Here n2 = n1")
print(f" n1 is {n1} and n2 is {n2}")
print(f" n1 add is {id(n1)}, n2 is {id(n2)}")

n2 = 20
print("Here n2 = 20 now")
print(f" n1 is {n1} and n2 is {n2}")
print(f" n1 add is {id(n1)}, n2 is {id(n2)}")

print("This is beacuse integers are immutable. So it cannot change n1")
print("This can be done by dict.")

dict1 = {
    "value" : 111
}
dict2 = dict1 

print("Here dict1 = dict2")
print(f" dict1 is {dict1} and dict2 is {dict2}")
print(f" dict1 add is {id(dict1)}, dict2 is {id(dict2)}")

dict2['value'] = 222
print("Here dict2 = 222 now")
print(f" dict1 is {dict1} and dict2 is {dict2}")
print(f" dict1 add is {id(dict1)}, dict2 is {id(dict2)}")



