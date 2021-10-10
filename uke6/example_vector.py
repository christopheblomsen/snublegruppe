"""
Author: Christophe Blomsen

This code is for demonstrating numpy arrays
"""
import numpy as np
import matplotlib.pyplot as plt

listed = [0.0, 1.0, 2.0, 3.0, 4.0]
arrays = np.linspace(0, 4, 5)


listed_2 = listed*2
arrays_2 = arrays*2

# print(listed_2)
# print(arrays_2)

# listed[-1] = 8.0
# arrays[-1] = 8.0
'''
for i in range(len(arrays)):
    listed[i] = listed[i]+2
    arrays[i] = arrays[i]+2
'''
listed_2 = []
for i in range(len(listed)):
    listed_2.append(listed[i]*2)


# print(listed)
# print(arrays)

N = 1000
x = np.linspace(0, 2*np.pi, N)
sin_list = []

for i in range(N):
    sin_list.append(np.sin(x[i]))

sin_array = np.sin(x)
cos_array = np.cos(x)
tan_array = np.tan(x)
arctan_array = np.arctan(x)
plot_list = [[sin_array, cos_array],
             [tan_array, arctan_array]]
plot_list2 = [sin_array, cos_array,
             tan_array, arctan_array]

# print(sin_list)
# print(sin_array)
fig, axs = plt.subplots(2,2)
k = 0
for i in range(2):
    for j in range(2):
        print(f'i = {i}, j = {j}')
        #axs[i, j].plot(x, plot_list[i][j])
        axs[i, j].plot(x, plot_list2[k])
        axs[i, j].set_xlabel('x')
        axs[i, j].set_ylabel('y')
        k += 1

plt.show()
'''
axs[0, 0].plot(x, sin_array, c='g', label='sinus', linestyle='dashed')
axs[0, 0].set_title('Title here')
axs[0, 0].set_xlabel('x unit')
axs[0, 0].set_ylabel('sin value')
axs[0, 0].legend()


axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title('Title here')
axs[0,1].set_xlabel('x unit')
axs[0,1].set_ylabel('sin value')
axs[0,1].legend()
plt.show()
#plt.close()

plt.plot(x, np.tan(x))
plt.show()
'''
