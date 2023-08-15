# reduce()
# reduce() is a built in function that takes two parameters as an input. First parameter is function and second
# parameter is an iterable
# Freduce() function returns one element from the final computation in the iterable

from functools import reduce
nums = [1, 2, 3, 4, 5]
def sum_all(x, y):
    return x + y

result = reduce(sum_all, nums)
print(nums)
print(result)
result_1 = reduce(lambda x, y: x + y, nums)
print(result_1)




