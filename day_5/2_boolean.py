#True and false are the boolean Datatypes
# True and False are also keywords in python.
# Boolean type in pyhton is the subclass of the Integer class where False represents 0 and True represents 1.


# Relational Operators yield boolean type
a = 5
b = 3
print(a > b) #True
print(b < a) #True
print(b == a) #False
print(a != b) #True

#Logical Operators yeild boolean type
print(a > b and a != b) #True
print(b > a or a != b) #True
print(a == b or a < b) #False
print(not a) # False
print(not b) # False

c = None
print(not c) # True
print(not[]) # True
print(not"") #True
print(not {}) # True
print(not ()) # True
print(not False) # True
print(not True) # False


# Membership operations yield boolean
print(2 in [1, 2, 3]) #True
print("a" not in ["a", "e", "i", "o", "u"]) # False

#Identity operation yield boolean
a = [1, 2, 3]
b =a
print(a is b) # True
print(id(a) == id(b)) #True
print(a is not b) # False

b= a.copy()
print(a is b) #False
print(a is not b) #True


# We have mentioned, boolean is a subclass of int type.
# Let's see some examples
print(True + 2) # 1 + 2 = 3
print(70 * False) # 70 * 0 = 0
print(True + True) # 1 + 1 = 2
print(True + False) # 1 + 0 = 1


# We have bool() built in function for the boolean type
# Anything truthy inside the bool() function gives True whereas anything Falsy inside bool() gives False

# Any non-empty datatypes sre considered truthy. Examples of truthy are:
a = 23
b = 12.1
c = [1, 2, 3] # It is a non-empty list
d = (1, 2, 3) # It is a non-empty tuple
e = {1, 2, 3} # It is a non-empty set
f = {"name": "John", "age": 23} # It is a non empty dictionary
print(bool(a)) #True
print(bool(b)) #True
print(bool(c)) #True
print(bool(d)) #True
print(bool(e)) #True
print(bool(f)) #True



# All the empty datatypes, None and False are Falsy values
a = 0
b = 0.0
c = []
d = ()
e = {}
f = set()
g = ""
h = None
i = False
bool()
print(bool(a)) #False
print(bool(b)) #False
print(bool(c)) #False
print(bool(d)) #False
print(bool(e)) #False
print(bool(f)) #False
print(bool(g)) #False
print(bool(h)) #False
print(bool(i)) #False