"""
Author: Christophe Blomsen

This code is for demonstrating plotting
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)   # x values from 0 to 2pi, 1000 steps
y = np.sin(x)                       # y is sin(x)
z = np.cos(x)                       # z is cos(x)
a = np.exp(x)                       # a is e^x

colour = ['r', 'b', 'k']            # list of value colours, r-red, b-blue, k-black
stillhet = ['sin', 'cos', 'exp']    # Label list for plot
plots = [y, z, a]                   # list of the different functions to plot

for i in range(3):
    plt.plot(x, plots[i], c=f'{colour[i]}', label=f'{stillhet[i]}')
# plt.plot(x, z, color=f'{colour[1]}', label=f'{stillhet[1]}')
plt.legend()    # shows the labels
plt.show()      # shows the plot
plt.close()     # close the plot, not neccesary

fig, subplot = plt.subplots(3)      # for subplotting

'''
subplot[0].plot(x, y, c='r', label='sin')  # plots in the first box
subplot[0].legend()

subplot[1].plot(x, z, c='b', label='cos')  # plots in the second box
subplot[1].legend()

plt.show()
'''
for i in range(3):  # plots all the subplots
    subplot[i].plot(x, plots[i],
                    c=f'{colour[i]}', label=f'{stillhet[i]}')
    subplot[i].legend()

plt.show()
