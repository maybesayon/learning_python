# *args and **kwargs are the arbitrary arguments
# These arguments can take dynamic number of parameters
# They are like an expandable bucket

def addition(*args):
    print(args)
    print(type(args))
    return sum(args)

result = addition(1, 2, 3, 4)
print(result)



def addition(**kwargs):
    print(kwargs) # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs))  # <class 'dict'>
    return (sum(kwargs.values()))
result = addition(a=1, b=2, c=3)
print(result)



