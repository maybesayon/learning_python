### Mutable and Immutable objects###
"""
If an object once created can be changed later, then object is a mutable object

But if an object once created can never be changed throughout its life cycle then it is an immutable object.

List, dictionary, set are the example of Mutable objects
Numbers, Tuple, Boolean, String are exampple of Immutable.
"""
"""
>>> a= [1, 2, 3, 4]
>>> a[1] = 5
>>> a
[1, 5, 3, 4]
>>> b =(1, 2, 3)
>>> b[1] = 5 # This raises error
TypeError: 'tuple' object does not support item assignment
"""

 
