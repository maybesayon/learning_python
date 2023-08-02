#operators are the special symbols in any programming language to carry out Arithemstic and logical Operations


a = 1
b = 2
c = a + b
# Here '=' is an assignment operator and '+' is an arithematic operator

# Arthematic operators
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Floor Division (//) => Floor division removes the decimal value and only provides the integer towards floor

print(3//2) # It gives 1
print(-3//2) # It gives -1

#Exponential (**)
print(3**2) # It gives 9

# Modulus (%) => Gives remainder of a division
print(3 % 2)# Gives 1
print(4 % 2)# gives 0


# Comparision / Relational operators
# ==, !=, >, <, >=, <=



# Logoical operators
# and, or, not are the logical operations and their operators are "and", "or", "not" respectively. The results in
# operations are either true or false


# Identity operators
# Identity operators check whether the two qbjects are same or not. 'is' and 'is not' are used for identity check.
a=1
b=1
print(a is b) # True
print(id(a))
print(id(b)) # For the same object, id() gives equal value



# Membership Operators
# It is used to check membership of an opject in a sequance. 'in' and 'not in' are used for membership check
print(2 in [1, 2, 3]) # True
print(3 not in [1, 2, 3]) # False


# Assignment Operatoe
# The result of sny operation can be assigned to a variable using an assignment operator.
# "=" is a basic assignment operator
name = "John" # here = is an assignment operator

# +=, -=, *=, /= are also some assignment operators
a = 1
a = a+1 # This line can also be written as a += 1
a += 1 #3
print(a)


# Precedence and Associativity
# Precedence of the operators is the rule that determines which operator should be executed first
# If multiple operator in an operation have the same precedence then the associativity determines the operation sequence


# Normally associativity is from left-right except for the case '**'.
# For exponent(**), it is from right-left

print(2**3**2)