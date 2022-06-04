from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animacion(ang=48):
    v0 = 30
    g = 9.80665
    if ang!=90:
        v0x = v0*np.cos(np.radians(ang))
        v0y = v0*np.sin(np.radians(ang))
    else:
        v0x = 0
        v0y = v0
    th = ((-v0y)/-g)  # Se obtiene el tiempo de caida
    tt = th*2  # Se obtiene el tiempo total que se tarda en recorrer la trayectoria
    alc = v0x*tt  # Se obtiene el alcance
    h = (v0y*th)+((-g*(th**2))/2)  # Se obtiene la altura

    fig = plt.figure()  # Se crea la figura
    ax = fig.add_subplot(111)  # Se crea el eje x
    # ax.axis('off')  # Se ocultan los ejes

    x, y = [], []  # Se crean las listas para los puntos
    line, = ax.plot(x, y, "r-")  # Se crea la linea de la trayectoria

    def init():
        if v0x > 0:
            ax.set_xlim(0, alc if alc > h else h)
            ax.set_ylim(0, alc if alc > h else h)
        elif v0x < 0:
            ax.set_xlim(alc if abs(alc) > h else -h, 0)
            ax.set_ylim(0, abs(alc) if abs(alc) > h else h)
        else:
            ax.set_xlim(-h, h)
            ax.set_ylim(0, h)
        return line,

    def animate(i):
        # Se actualiza la posicion en x del objeto en el momento i
        x.append(v0x*i)
        # Se actualiza la posicion en y del objeto en el momento i
        y.append((v0y*i)-((g*(i**2))/2))
        line.set_data(x, y)  # Se actualiza la linea de la trayectoria
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(
        0, tt+0.1, 0.1), interval=10, blit=False, repeat=False)  # Se crea la animacion
    plt.show()


animacion(135)
