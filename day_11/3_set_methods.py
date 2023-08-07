s = {1, 2, 3}
result = s.add(4)
print(result) # None; Because add() method returns nothing
print(s)#{1, 2, 3, 4}

#update
s = {1, 2, 3}
s.update([4, 5, 6, 7, 8])
print(s) # {1, 2, 3, 4, 5, 6, 7, 8}

#discard
s = {1, 2, 3, 4}
s.discard(4)
print(s)# {1, 2, 3}

#remove
s = {1, 2, 3, 4}
s.remove(3)
print(s) # {1, 2, 4}

#clear
s = {1, 2, 3, 4}
s.clear()
print(s) # {}

#pop
s = {1, 2, 3, 4}
s.pop()
print(s)

# diffrence()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.difference(b) #a-b
print(result)
print(a - b) #is used for set diffrence

#intersection()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b)) #{3, 4}
print(a & b) # & operator is used for set intersection

#union
a = {1, 2, 3, 4 }
b = {3, 4, 5, 6}
print(a.union(b))# {1, 2, 3, 4, 5, 6}
print(a | b)# | is used for union

#isdisjoint()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a. isdisjoint(b)) #False

#issubset
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.issuperset(a)) #True
print(b.issuperset(a)) # True


# symmetric difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference(b)
print(result) # {1, 2, 5, 6}
print(a^b) # ^ is used for symmetric difference

# symmetric difference update
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference_update(b)
print(result) # None
print(a) #{1, 2, 5, 6}
