# Python lists are mutable objects
# We can create a list by enclosing sequence in big brackets[]

# We can also create a list using list() built-in function

a = [] #An empty list
b = () # An empty list using () function

a = [1, 2, 3] # Non-empty list
# In this list all data type are of integer data type but list can also have heterogenous type

a = [1, "Hello", 2.1, {1, 2, 3}, {"a": 1, "b": 2 }]
# In this list, the data are of different types which is also supported by a python list


# We can use built-in type() function to check the type of object
type([1, 2, 3]) # list
type ((1, 2, 3)) # tuple
type (1) # int
# and so on......
