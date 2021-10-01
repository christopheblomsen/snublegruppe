"""
Author: Christophe Blomsen

This code is for demonstrating plotting
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
#y = np.zeros(1000)
z = np.cos(x)
a = np.exp(x)

#for i in range(len(x)):
#    y[i] = np.sin(x[i])
#a = np.array([0, 1, 2, 3, 4])
#print(a[2:])
'''
colour = ['r', 'b', 'k']
stillhet = ['sin', 'cos', 'exp']
plots = [y, z, a]

for i in range(3):
    plt.plot(x, plots[i], c=f'{colour[i]}', label=f'{stillhet[i]}')
# plt.plot(x, z, color=f'{colour[1]}', label=f'{stillhet[1]}')
plt.legend()
plt.show()
plt.close()

fig, subplot = plt.subplots(3)

subplot[0].plot(x, y, c='r', label='sin')
subplot[0].legend()

subplot[1].plot(x, z, c='b', label='cos')
subplot[1].legend()

plt.show()

for i in range(3):
    subplot[i].plot(x, plots[i],
                    c=f'{colour[i]}', label=f'{stillhet[i]}')
    subplot[i].legend()

plt.show()
'''
import pandas as pd
f = open("oxygen.txt", "r")

f = f.read().splitlines()

f2 = []

for i in range(len(f)):
    f2.append(f[i].split(" "))



f2[0][3] = str(f2[0][3]) + " " + str(f2[0][4])
del f2[0][4]

f2[0][2] = str(f2[0][1]) + " " + str(f2[0][2])
del f2[0][1]




isotope = []
weight = []
natural_abudance = []

for i in range(1, len(f2)):
    weight.append(eval(f2[i][1]))
    natural_abudance.append(eval(f2[i][2]))
    isotope.append(f2[i][0])

df = pd.DataFrame()

#df = pd.DataFrame([[isotope, natural_abudance, weight]], columns=["isotope", "natural_abudance", "weight"])


df["isotope"] = isotope
df["natural_abundance"] = natural_abudance
df["weight[g/mol]"] = weight
df["molar mass"] = (round(df["weight[g/mol]"] * df["natural_abundance"], 4)).astype(str) + "g"

print(df)

#what units
