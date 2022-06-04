import serial
import time

serialArduino = serial.Serial('COM5', 9600)
time.sleep(2)

while True:
    cod=serialArduino.readline().decode('cp1252')
    print(cod)
    print("--------------------------------")
