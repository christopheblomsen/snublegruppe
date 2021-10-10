"""
Author: Christophe Blomsen

This code is for demonstrating diffs
"""
import numpy as np
import matplotlib.pyplot as plt

N = 10

"""
x_2 = x_1**2 - x_0
"""

x_prev_prev = 5
x_prev = 7

x_list = [x_prev_prev, x_prev]

x_array = np.zeros(N)
x_array[0] = x_prev_prev
x_array[1] = x_prev
#print(f'{x_prev_prev}')
#print(f'{x_prev}')

for i in range(2, N):
    # Fast and ugly version
    #x_new = x_prev**2 - x_prev_prev
    #print(x_new)
    #x_prev = x_new
    #x_prev_prev = x_prev

    # list version
    #x_new = x_list[i-1]**2 - x_list[i-2]
    #x_list.append(x_new)

    # array version
    x_array[i] = x_array[i-1]**2 - x_array[i-2]

    print(f'{x_array[i]:.2f}')
