# Arguments in the function are the elements that are sent in the function call
# Parameters in the functions are the elements that are present in the function definition

# Types of arguments in a function
# 1. Positional / Required Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments

def addition(a, b , c = 5):
    return a + b + c

result = addition(2 , 3, 10)
print(result) # 15

# Here "a" and "b" are the positional arguments and "c" is a default argument
# Positional arguments must be sent during a function call i.e They are the required arguments
# Default areguments are not required in funcgtion call

