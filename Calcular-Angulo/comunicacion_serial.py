import serial, serial.tools.list_ports
from threading import Thread, Event
from tkinter import StringVar

class Comunicacion():
    def __init__(self, *args):
        super().__init__(*args)
        self.datos_recibidos = StringVar()

        self.arduino = serial.Serial()
        self.arduino.timeout = 0.5

        self.baudrates=["1200", "2400", "4800", "9600", "19200", "38400", "115200"]
        self.puertos = []

        self.senal=Event()
        self.hilo = None

    def PuertosDisponibles(self):
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]

    def ConnexionSerial(self):
        try:
            self.arduino.open()
        except:
            pass
        if self.arduino.is_open:
            self.IniciarHilo()
            print("Conectado")

    def LeerDatos(self):
        try:
            while self.senal.isSet() and self.arduino.is_open:
                data=self.arduino.readline().decode("utf-8").strip()
                if len(data) > 1:
                    self.datos_recibidos.set(data)
        except TypeError:
            pass

    def IniciarHilo(self):
        self.hilo = Thread(target=self.LeerDatos)
        self.hilo.setDaemon(1)
        self.senal.set()
        self.hilo.start()

    def DetenerHilo(self):
        if self.hilo is not None:
            self.senal.clear()
            self.hilo.join()
            self.hilo = None

    def Desconectar(self):
        self.arduino.close()
        self.DetenerHilo()
