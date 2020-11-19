
'''
SETS

A set, unlike lists, is a collection of data in no particular order; items cannot be accessed by indexing.

Just like mathematical sets, it cannot contain more than one of the same items.

An item can only be added once in sets. So a set cannot have two identical elements.

We use the set() function to create an empty set.
'''

s = {"python", 5,6,8,5,6,"abc", "python","python","python","python","python","python","python","python","python",}
print(s)

empty= set()
print(type(empty))

empty2 = {}
print(type(empty2))

from math import sqrt

#import math

print({x for x in list(range(10))})

print({sqrt(x) for x in list(range(10))})

