# Map()
# map ois a built in function that takes two parameters as an input. First parameter is function and second parameter is
# an iterable
# map function changes every element in an iterable to some other form

nums = [1, 2, 3, 4, 5]
def increase_by_10(data):
    return data + 10

result = map(increase_by_10, nums)
print(nums)
print(list(result))
result_1 = map(lambda x: x+10, nums)
print(list(result_1))

def increse_power_by_3(data):
    return data ** 3
result = map(increse_power_by_3, nums)
print(list(result))

result_1 = map(lambda x: x**3, nums)
print(list(result_1))

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_1 = filter(lambda x: x**3, nums)
print(list(result_1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
