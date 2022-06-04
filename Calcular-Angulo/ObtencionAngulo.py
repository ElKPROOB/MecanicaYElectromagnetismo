import time
import re

import serial


angAnt = 0
serialArduino = serial.Serial('COM3', 9600) #Se abre el puerto serial
time.sleep(2)


def RecibirAngulo():
    try:
        angulo = serialArduino.readline().decode('cp1252') #Se lee el puerto serial
        angulo = re.findall('[0-9]+', angulo) #Se obtienen solo los números de lo que se leyó
        angulo = int(angulo[0])
    except:
        angulo = 0
    return angulo

if __name__ == "__main__":
    while True: #Se ejecuta el programa hasta que se cierre
        angl = RecibirAngulo() #Se obtiene el ángulo
        if abs(angl-angAnt) > 1: #Se verifica que el ángulo haya variado más de 1 grado
            angAnt = angl #Se actualiza el ángulo anterior
            ang = angl #Se actualiza el ángulo
            print(ang) #Se imprime el ángulo
            time.sleep(0.1)
