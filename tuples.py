'''

TUPLES

It is an ordered data structure, it has an index value like lists, it can contain all data types.
Unlike lists, they have a structure that cannot be changed.
If we have more than one unchangeable values, we can collect them in a bunch.

'''

tupl = (1,2,3,4,5)
print(tupl)
print(type(tupl))

a = {(x, x+1): x for x in range(10)}
print(a)