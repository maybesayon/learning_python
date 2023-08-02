# remove() method
# remove method takes list item as parameter


vowels = ["a", "e", "i", "o", "u"]
vowels.remove('e')
print(vowels)


# if we pass a parameter not present in the list then it raises error
# vowels.remove("p") # it raises error

# pop() method
# pop takes index as operator
vowels = ["a", "e", "i", "o", "u"]
vowels.pop(2)
print(vowels)

# pop method also returns a valur from the index passes as the parameter.
# In the above example result gives 'i' because 'i' is at 2nd position index and finally. 'i' is also removed from the
#list vowels


#clear() method. It clear the list
vowels = ["a", "e", "i", "o", "u"]
vowels.clear()# It clears the list
print(vowels)

#index() method. It takes list item as an argument
vowels = ["a","o", "i", "o", "u"]
result = vowels.index("o")
print(result)#3

# index() method also takes start and end as parameters
characters = [3, 5, 7, "s", 7, 3, "b", "s"]
result = characters.index("s",4,10)
print(result)


#count() method takes list irem as a parameter and returns the number of repetition of that item
vowels = ["a", "e", "i", "o", "u", "o", "o", "a", "i"]
result = vowels.count("o")
print(result)

#reverse() method. It reverses the item of the list
fruit = ["banana", "apple", "mango"]
fruit.reverse()
print(fruit)



