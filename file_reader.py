"""
Author: Christophe Blomsen

This code is for demonstrating reading
"""
import numpy as np
import matplotlib.pyplot as plt

with open('file.txt', 'r') as infile:
    infile.readline()

    ans = 0
    for line in infile:
        line = line.split()
        for i in range(1, len(line)):
            print(line[i])
            ans += eval(line[i])

print(f'ans = {ans}')
