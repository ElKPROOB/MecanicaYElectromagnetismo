from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

"""Dado un angulo y una velocidad inicial, se calcula la altura y el alcance"""
ang = 48
v0 = 30
g = 9.80665
v0x = v0*np.cos(np.radians(ang))  # Se obtiene la velocidad en x
v0y = v0*np.sin(np.radians(ang))  # Se obtiene la velocidad en y
th = ((-v0y)/-g)  # Se obtiene el tiempo de caida
tt = th*2  # Se obtiene el tiempo total que se tarda en recorrer la trayectoria
alc = v0x*tt  # Se obtiene el alcance
h = (v0y*th)+((-g*(th**2))/2)  # Se obtiene la altura

fig = plt.figure()  # Se crea la figura
ax = fig.add_subplot(111)  # Se crea el eje x
ax.axis('off')  # Se ocultan los ejes

x, y = [], []  # Se crean las listas para los puntos
line, = ax.plot(x, y, "r-")  # Se crea la linea de la trayectoria


def init():
    """
    Funcion que se ejecuta al iniciar la animacion
    """
    ax.set_xlim(-2, alc if alc >
                h else h)  # Se establecen los limites del eje x
    # Se establecen los limites del eje y
    ax.set_ylim(-2, alc if alc > h else h)
    return line,


def animate(i):
    """
    Funcion que se ejecuta cada vez que se actualiza la animacion
    """
    x.append(v0x*i)  # Se actualiza la posicion en x del objeto en el momento i
    # Se actualiza la posicion en y del objeto en el momento i
    y.append((v0y*i)-((g*(i**2))/2))
    line.set_data(x, y)  # Se actualiza la linea de la trayectoria
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=np.arange(
    0, tt, 0.1), interval=10, blit=False, repeat=False)  # Se crea la animacion

plt.show() # Se muestra la animacion
