import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import threading

import time
import re


angAnt = 0
arduinoSerialData = serial.Serial('COM3', 9600)
time.sleep(2)
"""fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xdatos, ydatos = [], []"""


def Animacion(ang=45):
    global ultHilo
    time.sleep(1)
    if ang!=ultHilo:
        return 0
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
        if v0x >= 0:
            ax.set_xlim(0, alc if alc > h else h)
            ax.set_ylim(0, alc if alc > h else h)
        else:
            ax.set_xlim(alc if abs(alc) > h else h, 0)
            ax.set_ylim(0, abs(alc) if abs(alc) > h else h)
        return line,

    def animate(i):
        # Se actualiza la posicion en x del objeto en el momento i
        x.append(v0x*i)
        # Se actualiza la posicion en y del objeto en el momento i
        y.append((v0y*i)-((g*(i**2))/2))
        line.set_data(x, y)  # Se actualiza la linea de la trayectoria
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(
        0, tt, 0.1), interval=10, blit=False, repeat=False)  # Se crea la animacion

    if ang!=ultHilo:
        return 0

    plt.show()


def PrntAnimacion(ang=45):
    global ultHilo
    for j in range(10):
        if ang!=ultHilo:
            break
        print(ang, j)
        time.sleep(3)


def RecibirAngulo():
    try:
        angulo = arduinoSerialData.readline().decode('cp1252')
        angulo = re.findall('[0-9]+', angulo)
        angulo = int(angulo[0])
    except:
        angulo = 0
    return angulo


"""if __name__ == "__main__":
    angl = 120
    animacion(angl)  # Se ejecuta la animacion"""


if __name__ == "__main__":
    #hilos = []
    ultHilo = 0
    while True:  # Se ejecuta el programa hasta que se cierre
        angl = RecibirAngulo()  # Se obtiene el ángulo
        if abs(angl-angAnt) > 1:  # Se verifica que el ángulo haya variado más de 1 grado
            # animacion(angl)  # Se ejecuta la animacion
            t = threading.Thread(target=Animacion,
                                 args=(angl,), daemon=True)
            ultHilo = angl
            #hilos.append(t)
            t.start()
            angAnt = angl  # Se actualiza el ángulo anterior
            ang = angl  # Se actualiza el ángulo
            #print(ang)  # Se imprime el ángulo


"""if __name__ == "__main__":
    while True:  # Se ejecuta el programa hasta que se cierre
        angl = RecibirAngulo()  # Se obtiene el ángulo
        if abs(angl-angAnt) > 1:  # Se verifica que el ángulo haya variado más de 1 grado
            angAnt = angl  # Se actualiza el ángulo anterior
            ang = angl  # Se actualiza el ángulo
            print(ang)  # Se imprime el ángulo
            time.sleep(0.1)"""


"""while True:
    if (arduinoSerialData.inWaiting() > 0):
        def animate(i, xdatos, ydatos):
            datos = arduinoSerialData.readline()
            datos = float(datos)
            xdatos.append(i)
            ydatos.append(datos)
            # ax.clear()
            ax.plot(xdatos, ydatos)
        ani = animation.FuncAnimation(fig, animate, fargs=(xdatos, ydatos))
        plt.show()"""
