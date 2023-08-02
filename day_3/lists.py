#### LIst indexing####
# List indexing starts from 0 for forward indexing and -1 for backward indexing

# Indexes must be provided in the big bracket

vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[0]) # = a
print(vowels[3]) # = o
# prin(vowels[5]) # It raises index error

print(vowels[-1]) # = 'u'
print(vowels[-3]) # = 'i'
# print(vowels[-6] # It raises index error
print(vowels)
vowels[2] = "I" # Assigning item to the list at wnd position
print(vowels)

vowels[-1] = "U" # Assigning list to the list at last position with negative index
print(vowels)



#### List Slicing####
# In slicing, the first index is inclusive but the second index is always exclusive
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(a[:])
print(a[0:7]) # [a, b, c, d, e, f, g]
print(a[:7]) # [a, b, c, d, e, f, g]
print(a[3:]) # [d, e, f, g, h, i, j]


print(a[2:6]) # [c, d, e, f]
print(a[6:2]) # []

print(a[-7:-2]) # [d, e, f, g, h]
print(a[-2:-7]) # []
print(a[:-2]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[2:-2]) # ['c', 'd', 'e', 'f', 'g', 'h']
print(a[-3:]) # ['h', 'i', 'j']



# In every data-types operations, methods and built-in functions should be studied carefully
