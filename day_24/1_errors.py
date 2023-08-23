# In python the errors can be broadly classified into two sections:
# 1. Syntactic error
# 2. Non-Syntactic error


# Syntactic error
# This type of error occurs when you mess up with the grammer of the language
# For example: making typo in keywords, messing up the indentation, whitespaces at unwanted spaces
# a = 1 # Syntax error because of a whitespace in the beginning
# fo i in range(10): # Syntax error because of the type in keyword
#    pass
# a = 5
# if a:
# print("Hello World") #Indentation error

# Non-Syntactic Error
# These are all the errors except syntax error. They can further be classified in followings:
# 1. TypeError
# 2. ValueError
# 3. ZeroDivision Error
# 4. Attribute Error
# 5.





# TypeError
# It is raised when operations in different datatypes are performed which is not acceptable
# For example: 2 + "Hello". Int and String can't be operated with '+' operator
# 2 + "Hello" raises error

# ValueError
# It is raised if we try to convert a datatype to other datatype which is not possible
# For eg int("Hello"). This raises error

# ZeroDivision Error
# It is raised when we try to divide an object with 0
# print(3/0) # ZeroDivision error


# Attribute Error
# It is raised if an object tries to get an attribute which is not present in that object
# example if a list object tries to access the join() method. join() is actually a mehthod in string.
# a = [1, 2, 3]
# a.join("") # Attribute error


# Key Error
# std = {"name": "Jon', "address": "KTM"}
# print(std["phone"]) # Index Error

# Index Error
# data = [1, 2, 3, 4]
#print(data[10])



# Name Error
