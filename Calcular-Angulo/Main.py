import threading
import time
import os
import re

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import readchar
import serial


angAnt = 0
arduinoSerialData = serial.Serial('COM5', 9600)  # Se abre el puerto serial
time.sleep(2)  # Se espera 2 segundos para que el arduino se inicialice


def RequestData():
    """
    Funcion encargada de solicitar indeterminadamente una entrada al usuario
    """
    while True:
        try:
            userInput = readchar.readkey()  # Se lee el dato ingresado por el usuario
            if userInput == "\r":
                return 1  # Se retorna 1 si el usuario ingreso la tecla enter
            elif userInput == "\x1b":
                return -1  # Se retorna -1 si el usuario ingreso la tecla escape
            return 0  # Se retorna 0 si el usuario ingreso una tecla que no es enter o escape
        except:
            return -2  # Se retorna -2 si ocurrio un error


def Animacion(ang=45):
    """
    Funcion encargada de generar la animacion
    """
    time.sleep(1)
    v0 = .05 # Velocidad inicial
    g = 9.80665  # Gravedad
    if ang != 90:  # Si el angulo no es 90
        v0x = v0*np.cos(np.radians(ang))  # Se calcula la velocidad en x
        v0y = v0*np.sin(np.radians(ang))  # Se calcula la velocidad en y
    else:
        v0x = 0  # Si el angulo es 90, la velocidad en x es 0
        v0y = v0  # Si el angulo es 90, la velocidad en y es la velocidad inicial
    th = ((-v0y)/-g)  # Se obtiene el tiempo de caida
    tt = th*2  # Se obtiene el tiempo total que se tarda en recorrer la trayectoria
    alc = v0x*tt  # Se obtiene el alcance
    h = (v0y*th)+((-g*(th**2))/2)  # Se obtiene la altura

    fig = plt.figure()  # Se crea la figura
    ax = fig.add_subplot(111)  # Se crea el espacio de graficacion
    # ax.axis('off')  # Se ocultan los ejes

    x, y = [], []  # Se crean las listas para los puntos
    line, = ax.plot(x, y, "r-")  # Se crea la linea de la trayectoria

    def init():
        """
        Funcion encargada de inicializar la animacion
        """
        if v0x > 0:  # Si la velocidad en x es mayor a 0 se asigna el cuadrante 1
            ax.set_xlim(0, alc if alc > h else h)
            ax.set_ylim(0, alc if alc > h else h)
        elif v0x < 0:  # Si la velocidad en x es menor a 0 se asigna el cuadrante 2
            ax.set_xlim(alc if abs(alc) > h else -h, 0)
            ax.set_ylim(0, abs(alc) if abs(alc) > h else h)
        else:  # Si la velocidad en x es 0 se asignan los dos cuadrantes
            ax.set_xlim(-(h//2), h//2)
            ax.set_ylim(0, h)
        ax.set_title("Tiro parabolico a un angulo de " +
                     str(ang) + " grados")  # Se asigna el titulo
        return line,

    def animate(i):
        """
        Funcion encargada de actualizar la animacion
        """
        # Se actualizan laa posicionea en (x, y) del objeto en el momento i
        x.append(v0x*i)
        y.append((v0y*i)-((g*(i**2))/2))
        line.set_data(x, y)  # Se actualiza la linea de la trayectoria
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(
        0, tt+0.1, 0.1), interval=10, blit=False, repeat=False)  # Se crea la animacion

    plt.show()  # Se muestra la animacion


def RecibirAngulo():
    """
    Funcion encargada de recibir el angulo del arduino
    """
    try:
        angulo = arduinoSerialData.readline().decode(
            'cp1252')  # Se lee el dato recibido
        # Se obtienen los digitos del string
        angulo = re.findall('[0-9]+', angulo)
        angulo = int(angulo[0])  # Se convierte el string a un entero
    except:
        angulo = 45  # Se retorna 45 si ocurrio un error
    return angulo


def Comparar():
    """
    Funcion encargada de comparar el angulo recibido con el anterior
    """
    global angAnt
    global anguloG
    while True:
        angl = RecibirAngulo()  # Se obtiene el angulo
        if abs(angl-angAnt) > 1:  # Si el angulo ha variado en mas de 1 grado
            angAnt = angl  # Se actualiza el angulo anterior
            anguloG = angl  # Se actualiza el angulo global


def Prnt():
    """
    Funcion encargada de imprimir el angulo en la consola
    """
    global anguloG
    global angAnt2
    while True:
        if anguloG != angAnt2:  # Si el angulo global ha variado
            angAnt2 = anguloG  # Se actualiza el angulo anterior global
            os.system('cls')  # Se limpia la pantalla
            print(anguloG)  # Se imprime el angulo global
        time.sleep(0.01)


def main():
    """
    Funcion principal
    """
    global anguloG
    # Se crea un hilo para leer el angulo
    t = threading.Thread(target=Comparar, daemon=True)
    t.start()
    # Se crea un hilo para imprimir el angulo
    t1 = threading.Thread(target=Prnt, daemon=True)
    t1.start()
    while True:
        code = RequestData()  # Se solicita una entrada al usuario
        if code == 1:  # Si el usuario presiono enter
            Animacion(anguloG)  # Se genera la animacion
        elif code == -1:  # Si el usuario presiono escape
            return 0  # Se termina el programa
        time.sleep(1)


if __name__ == "__main__":
    anguloG = 0  # Se inicializa el angulo global
    angAnt2 = 0  # Se inicializa el angulo anterior global
    main()  # Se llama a la funcion principal
