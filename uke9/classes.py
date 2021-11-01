"""
Author: Christophe Blomsen

This code is for demonstating classes
"""
import numpy as np
import matplotlib.pyplot as plt


class FIBONACCI:
    def __init__(self, x0, x1):
        """
        The constructor that INITilize the class
        Important to have self as a pointer
        """
        self.x0 = x0
        self.x1 = x1

    def plotyplot(self, N):
        """
        For plotting, the same as the code at the end of the
        code
        """
        x = np.linspace(1, N+1, N)
        y = self.calculate(N)

        plt.plot(x, y, label=f'Fibonacci')
        plt.xlabel("Iteration")
        plt.ylabel("Value")
        plt.legend()
        plt.show()

    def seq(self, x_prev, x_prev_prev):
        """
        The fibonacci sequence
        """
        x_new = x_prev + x_prev_prev
        return x_new

    def calculate(self, N):
        fib_array = np.zeros(N)

        # Sets the init value
        fib_array[0] = self.x0
        fib_array[1] = self.x1

        for i in range(2, N):
            fib_array[i] = self.seq(fib_array[i-1], fib_array[i-2])

        self.fib_array = fib_array  # if you want to save the values
        return fib_array


A = 1
B = 1
N = 8

fib1 = FIBONACCI(x0=A, x1=B)  # instance of the fibonacci sequence starting at 1, 1
fib1.plotyplot(N)

"""
x = np.linspace(1, N+1, N)
fib_array1 = fib1.calculate(N)
plt.plot(x, fib_array1)
plt.show()
"""
