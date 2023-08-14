# Break, control and pass are the control statement in python. They can alter the normal flow of the program.

# Break
for i in range(10):
    if i == 4:
        break
    print(i) #0, 1, 2, 3

n = 0
while n <= 10:
    if n == 7:
        break
    print(n)
    n +=1

# Continue
for i in range(10):
    if i == 4:
        continue
    print(i)

n = 0
while n <= 10:
    n += 1
    if n in [4, 7, 9]:
        continue
    print(n)


# pass
# pass is a block of code. It literally does nothing. It is also used in the place where code may occur in the future
def addition(a, b):
    pass




