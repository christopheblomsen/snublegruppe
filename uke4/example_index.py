"""
Author: Christophe Blomsen

This code is for showing of sys.argv and IndexError
And user inputs
"""
import sys


try:                                        # Tries to do the indent
    a = int(eval(sys.argv[1]))              # Takes an int from first terminal argument
    b = float(sys.argv[2])                  # Takes an float as second
    c = round(eval(sys.argv[3]))            # Takes a round as third
except IndexError:                          # If it fails to do previous indent because
                                            # of IndexError do this instead
    print('Did you forget something: \n')   # \n is for new line
    a = int(eval(input('a = ')))
    b = float(input('b = '))
    c = round(eval(input('c = ')))

if a < 1:                                   # If a is less then 1
    raise ValueError                        # We raise a value error
    print('a is smaller then 1')


print(f'a = {a}, b = {b} and c = {c}')
dt = round(3.9)                             # to prove the difference
da = int(3.9)                               # of int and round
for i in range(dt):
    print(i)

for i in range(da):
    print(i)
