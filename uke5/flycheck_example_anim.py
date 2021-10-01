import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Creating the plot for the animation
fig = plt.figure()
axis = plt.axes(xlim=(-50, 50),  # the size of the x axis
                ylim=(-50, 50))  # the size of the y axis

line, = axis.plot([], [], lw=2)  # lw is linewidth


def init():
    line.set_data([], [])
    return line,


def animate(i):
    """
    t is a parameter which varies
    with the frame number
    """
    t = 0.1 * i  # dt

    # what is to be plotted
    x = t * np.sin(t)
    y = np.cos(t)
    # Important


    xdata.append(x)
    ydata.append(y)

    line.set_data(xdata, ydata)

    return line,


xdata, ydata = [], []

anim = FuncAnimation(fig, animate,
                     init_func=init,
                     frames=500,
                     interval=20,
                     blit=True)

plt.show()
