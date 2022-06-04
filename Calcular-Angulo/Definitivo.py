from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import os
from PIL import Image

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

"""fig = plt.figure()
ax = fig.add_subplot(2, 2, 2)
ax.axis('off')
ax2 = fig.add_subplot(2, 2, 3)

x, y = [], []
line, = ax.plot(x, y, "r-")
line2, = ax2.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], [
                  0, 0, 0, 0, 0, 0, 0, 0, 0], "ro")"""

t = np.arange(0, tt+0.1, 0.1)
x = v0x*t
x = x.tolist()
y = (v0y*t)-((g*(t**2))/2)
y = y.tolist()

img = Image.open(os.path.join('Calcular-Angulo', 'imagen' + '.jpg'))
iimg = img.transpose(method=Image.FLIP_LEFT_RIGHT)
# img.resize((300,300))
ax = plt.subplot2grid((2, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)

x, y = [], []
line, = ax.plot(x, y, "r-")

line1, = ax.plot(x, y)



def init():
    ax.set_xlim(-2, alc2 if alc2 > h2 else h2)
    ax.set_ylim(-2, alc2 if alc2 > h2 else h2)
    return line, line1


def animate(i):
    x.append(v0x*i)
    y.append((v0y*i)-((g*(i**2))/2))
    line.set_data(x, y)
    return line, line1


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=np.arange(0, tt, 0.1), interval=10, blit=False, repeat=False)

if __name__=="__main__":
    #anim.save('animation.gif', fps=30)
    input("Presione una tecla para continuar...")
    # serialArduino = serial.Serial('COM5', 9600)
    # time.sleep(2)
    plt.show()
