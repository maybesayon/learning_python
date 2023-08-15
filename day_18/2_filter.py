# Filter()
# Filter() is a built in function that takes two parameters as an input. First parameter is function and second
# parameter is an iterable
# Filter() function filters the element from an iterable and returns a new sequence



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_even_nums(data):
    return data % 2 == 0
result = filter(get_even_nums, nums)
print(result)
print(list(result))
result_1= filter(lambda x : x % 2 == 0, nums)
print(list(result_1))

def multiple_of_5(data):
    return data % 5 == 0
result = filter(multiple_of_5, nums)
print(list(result))
result_1 = filter(lambda x: x % 5 == 0, nums)
print(list(result_1))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_1 = map(lambda x: x % 5 == 0, nums)
print(list(result_1))  # [False, False, False, False, True, False, False, False, False, True]

