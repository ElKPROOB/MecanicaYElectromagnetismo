from msilib.schema import Directory
from operator import length_hint
from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage
from turtle import color, width
from matplotlib import markers
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from comunicacion_serial import Comunicacion
import collections

class Grafica(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)

        self.datos_arduino = Comunicacion()
        self.actualizarPuertos()

        self.muestra=100
        self.datos = 0.0

        self.fig, ax = plt.subplots(facecolor='#000000', dpi=100, figsize=(4, 2))
        plt.title("Grafica", color='white', size=12, family='Arial')
        ax.tick_params(direction="out", length=5, width=2, colors='white', grid_color='r', grid_alpha=0.5)
        self.line, = ax.plot([], [], color='m', marker='o', markersize=1, linewidth=2, markeredgecolor='m')
        self.line2, = ax.plot([], [], color='g', marker='o', markersize=1, linewidth=2, markeredgecolor='g')

        plt.xlim([0,self.muestra])
        plt.ylim([-5,6])

        ax.set_facecolor("#6E6D7000")
        ax.spines['bottom'].set_color('blue')
        ax.spines['top'].set_color('blue')
        ax.spines['left'].set_color('blue')
        ax.spines['right'].set_color('blue')

        self.datosSenalUno=collections.deque([0]*self.muestra,maxlen=self.muestra)
        self.datosSenalDos=collections.deque([0]*self.muestra,maxlen=self.muestra)

        self.widgets()

    def animate(self,i):
        self.datos=(self.datos.arduino.datos_recibidos.get())
        dato1=float(dato[0])
        dato2=float(dato[1])

        self.datosSenalUno.append(dato1)
        self.datosSenalDos.append(dato2)
        self.line.set_data(range(self.muestra),self.datosSenalUno)
        self.line2.set_data(range(self.muestra),self.datosSenalDos)

        #return self.line,self.line2

    def Iniciar(self,):
        self.ani=animation.FuncAnimation(self.fig,self.animate,interval=100, blit=False)
        self.btGraficar.config(state="disabled")
        self.btPausar.config(state="normal")
        self.canvas.draw()

    def pausar(self):
        self.ani.eventSource.stop()
        self.btReanudar.config(state="normal")
