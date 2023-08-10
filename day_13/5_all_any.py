# all(iterable) built-in function
#all()function takes an iterable / sequence ad parameter
# If all the elements of that iterable are truthy then it returns True


result = all([1, 2, "Jon"])
print(result) #True

result = all([0, "Jane"])
print(result) #False

result = all([1,0, "Jane"])
print(result)

# any(iterable) built-in function
# all()function takes an iterable / sequence as parameter
# If any one of the elements of that iterable is truthy then it returns True
print(any(["",{}, 1])) # True
print(any([0, []])) # False

# There is one exception in all ()
result=(any({}))
