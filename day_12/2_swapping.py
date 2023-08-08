a = 2
b = 4
print(a)
print(b)

temp = a
a = b
b = temp
print(a)
print(b)


a, b = 1, 2
a, b = b, a
print(a) # 2
print(b) # 1
