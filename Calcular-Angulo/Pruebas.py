from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

ang = 48
v0 = 30
v0x = v0*np.cos(np.radians(ang))
v0y = v0*np.sin(np.radians(ang))
g = 9.80665
h = ((v0**2)*(np.sin(np.radians(ang))**2))/(2*g)
alc = ((v0**2)*(np.sin(np.radians(ang)*2)))/g
t = (2*v0*(np.sin(np.radians(ang))))/g

th = ((-v0y)/-g)
tt = th*2
alc2 = v0x*tt
h2 = (v0y*th)+((-g*(th**2))/2)

fig = plt.figure()
ax = fig.add_subplot(2, 2, 2)
ax.axis('off')
ax2=fig.add_subplot(2, 2, 3)

x, y = [], []
line, = ax.plot(x, y, "r-")
line2, = ax2.plot([1,2,3,4,5,6,7,8,9], [0,0,0,0,0,0,0,0,0], "ro")


def init():
    ax.set_xlim(-2, alc2 if alc2 > h2 else h2)
    ax.set_ylim(-2, alc2 if alc2 > h2 else h2)
    return line, line2


def animate(i):
    x.append(v0x*i)
    y.append((v0y*i)-((g*(i**2))/2))
    line.set_data(x, y)
    return line, line2


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=np.arange(0, tt, 0.1), interval=10, blit=False, repeat=False)

#anim.save('animation.gif', fps=30)
plt.show()

"""
x = []
y = []
x2 = []
y2 = []

figure, ax = plt.subplots()

# Setting limits for x and y axis
#ax.set_xlim(0, alc)
#ax.set_ylim(0, h)

ax.set_xlim(0, alc)
ax.set_ylim(0, alc)

# Since plotting a single graph
line,  = ax.plot(0, 0, color='red')
line2,  = ax.plot(0, 0, color='blue')


def animation_function(i):
    x.append(v0x*i)
    y.append(v0y*i - (g*(i**2))/2)
    x2.append(v0x*i)
    y2.append(v0y*i - ((g*(i**2))/2))

    line.set_xdata(x)
    line.set_ydata(y)
    line2.set_xdata(x2)
    line2.set_ydata(y2)
    return line, line2,


animation = FuncAnimation(figure,
                          func=animation_function,
                          frames=np.arange(0, t+0.1, 0.1),
                          interval=10)
plt.show()
# animation.save('test.gif')"""
