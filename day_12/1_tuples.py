# Tuples are immutable datatype in pyhton. They are sequential datatypes like list, string, dictionary and set

# Creating an empty tuple
a = tuple() #tuple() built-in function can be used to create a tuplr
a = ()
print(a)

#Creating non-empty tuple
a = (1, 2, "a", "e", [1, 3]) # Tuple elements are enclosed in parenthesis or small brackets
print(a)
a = tuple([1, 2, 3])
print(a) #(1, 2, 3)

###########Tuple packing and unpacking###############
a = 1
print(type(a)) #here a is int type. But if we add ',' at the last it is tuple packing.
a = 1,
print(a) #(1, )
print(type(a)) # Here "a" is tuple

a = 1, "a", [1,2], {1,2}
print(a) #(1, 'a', [1, 2], {1, 2})

#####Unpackig Tuple########
a, b = 1, 2
print(a) # 1: integer type
print(b) # 2; integer type


a, b, c = (2, "hello", ["a", "e", "i", "o", "u"])
print(a)
print(b)
print(c)

# If number of element in LHS is not equal to RHS then it raises error in tuple unpacking
# b, c = (2, "hello", ["a", "e", "i", "o", "u"]) #Too many values to unpack
# a, b, c = (2, "hello") #not enough values to unpack (expected 3, got 2)




