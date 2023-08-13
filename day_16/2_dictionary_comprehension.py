squared = {data: data**2 for data in range(1,13)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

student = [("name", "Jon"), ("age", 25), ("address", "KTM")]
student = dict(student)
print(student)


# Create dictionary of the above data using dictionary comprehension
student = {key: value for key, value in [("name", "Jon"), ("age", 25), ("address", "KTM")]}


####enumerate()########
# enumerate can take two parameters, iterable and start_value
vowels = ["a", "e", "i", "o", "u"]
print(enumerate(vowels))  #enumerate object
print(list(enumerate(vowels)))
for index, value in enumerate(vowels):
    print(index)
    print(value)

for index, value in enumerate(vowels, start = 1):
    # Here indexing starts from 1
    print(index)
    print(value)

