"""
Author: Christophe Blomsen

This code is for demonstrating nested list and arrays
"""
import numpy as np

a = []                  # empty lists
b = []
for i in range(3):
    a.append(i)         # fill them
    b.append(i+1)

print(f'a = {a[0]} b = {b[0]}')     # for reference
c = [a, b]                          # make a nested list
d = c[0]                            # split it again for print
e = c[1]

print(f'a = {c[0][0]} b = {e[0]}')  # see that using c[0][0] would be
                                    # equal to using d[0]

def f(x):
    '''
    Simple function to show usefulnes of lists
    '''
    return x


listed = [1, 1.5, 'hello world', f, a]
# Lists can take all sorts of types in the same list

# To show difference between list and arrays
array = np.zeros((3, 2))        # make array with zeros
array[0, 1] = 1                 # equiliant to change [0][1]
array[1, 0] = 1.5               # [1][0]
array[2] = 2                    # Will change all in last
# array[2] = 'hello world'      # Will crash since string
print(array)                    # prints out array
print(listed[-1][0])            # prints out the first element of a
