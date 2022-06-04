import matplotlib as mpl
from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np

ang = 48
v0 = 30
v0x = v0*np.cos(np.radians(ang))
v0y = v0*np.sin(np.radians(ang))
g = -9.80665

h2 = ((v0**2)*(np.sin(np.radians(ang))**2))/(2*-g)
alc2 = ((v0**2)*(np.sin(np.radians(ang)*2)))/-g
t2 = (2*v0*(np.sin(np.radians(ang))))/-g

th = ((-v0y)/g)
tt = th*2
alc = v0x*tt
h = (v0y*th)+((g*(th**2))/2)

# x = []
# y = []

# for i in range(100):
#     x.append(i)
#     y.append(i)

# Mention x and y limits to define their range
#plt.xlim(0, 100)
#plt.ylim(0, 100)

# Ploting graph
# plt.plot(x, y, color='green')
# plt.title(str(h)+" - "+str(h2))

t = np.arange(0, tt, 0.1)
x = v0x*t
y = (v0y*t)-((-g*(t**2))/2)

fig = plt.figure(figsize=(15, 5))
# fig.tight_layout()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.plot(x, y, color='green')
ax2.plot(t, y, color='green')
ax2.plot(t, x, color='red')
ax1.set_xlabel('Distancia')
ax1.set_ylabel('Altura')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Altura')
ax1.set_title('Altura respecto a la Distancia')
ax1.legend(['Altura'])
ax2.set_title('Altura y Distancia respecto al Tiempo')
ax2.legend(['Altura', 'Distancia'])
escala = 10
ticks_x = ticker.FuncFormatter(lambda x, pos: '{:.1f} mts'.format(x))
ax1.xaxis.set_major_formatter(ticks_x)
ticks_y = ticker.FuncFormatter(lambda y, pos: '{:.1f} mts'.format(y))
ax1.yaxis.set_major_formatter(ticks_y)
ticks_x = ticker.FuncFormatter(lambda x, pos: '{:.1f} segs'.format(x))
ax2.xaxis.set_major_formatter(ticks_x)
ax2.yaxis.set_major_formatter(ticks_y)

plt.show()
