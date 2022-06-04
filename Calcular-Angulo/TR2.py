from PIL import Image
import os

from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
import serial
import time

serialArduino = serial.Serial('COM5', 9600)
time.sleep(2)
angAnt=0


def PurifyTxt(text1: str = " ", strip: bool = True, change: bool = True,
              upp_f_low_t: bool = True, removeAccents: bool = True,
              prohiC_f_permiC_t: bool = True,
              chars: list = ["+ áéíóúñ", [97, 122], [65, 90], [48, 57]]) -> str:
    text2 = ""
    if strip == True:
        text1 = text1.strip()
    if change == True:
        if upp_f_low_t == True:
            text1 = text1.lower()
        else:
            text1 = text1.upper()
    if removeAccents == True:
        text1 = text1.replace("á", "a")
        text1 = text1.replace("é", "e")
        text1 = text1.replace("í", "i")
        text1 = text1.replace("ó", "o")
        text1 = text1.replace("ú", "u")
        text1 = text1.replace("ñ", "n")
    if prohiC_f_permiC_t == True:
        for i in range(len(text1)):
            if text1[i] in chars[0]:
                text2 += text1[i]
                continue
            else:
                for j in range(len(chars)):
                    if j > 0:
                        lim_i = chars[j][0]
                        lim_s = chars[j][1]
                        if ord(text1[i]) >= lim_i and ord(text1[i]) <= lim_s:
                            text2 += text1[i]
                            break
    else:
        for i in range(len(text1)):
            adding = True
            if text1[i] in chars[0]:
                continue
            else:
                for j in range(len(chars)):
                    if j > 0:
                        lim_i = chars[j][0]
                        lim_s = chars[j][1]
                        if ord(text1[i]) >= lim_i and ord(text1[i]) <= lim_s:
                            adding = False
                            break
            if adding == True:
                text2 += text1[i]
    return text2


def pedir_angulo():
    angulo = serialArduino.readline().decode('cp1252')
    angulo = PurifyTxt(angulo,chars=["",[48,57]])
    try:
        return int(angulo)
    except:
        return 90


if __name__ == '__main__':
    ang = 0
    v0 = 30
    v0x = v0*np.cos(np.radians(ang))
    v0y = v0*np.sin(np.radians(ang))
    g = 9.80665

    th = ((-v0y)/-g)
    tt = th*2
    alc = v0x*tt
    h = (v0y*th)+((-g*(th**2))/2)

    t = np.arange(0, tt+0.1, 0.1)
    x = v0x*t
    x = x.tolist()
    y = (v0y*t)-((g*(t**2))/2)
    y = y.tolist()
    plt.ion()

    img = Image.open(os.path.join('Calcular-Angulo', 'imagen' + '.jpg'))
    iimg = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    # img.resize((300,300))
    ax = plt.subplot2grid((2, 3), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
    ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)
    #figure, ax2 = plt.subplots(figsize=(8, 6))
    plt.tight_layout()
    #plt.setp([a.get_xticklabels() for a in figure.axes[:-1]], visible=False)
    #figure = plt.figure()
    #ax = figure.add_subplot(2,3,2)
    #(ax,ax2) = figure.add_subplot()
    #ax2 = figure.add_subplot(2, 3, 3)
    # figure.subplots_adjust(wspace=0)

    x, y = [], []
    line, = ax.plot(x, y, "r-")

    #ax.set_ylim(-2, (v0*((-v0)/-g))+((-g*(((-v0)/-g)**2))/2))
    #ax.set_ylim(-2, 15)
    #plt.ylim(-2, 10)
    #ax.set_xlim(-2, v0*(((-v0y)/-g)*2))
    line1, = ax.plot(x, y)

    while True:
        ax.axis('off')
        ax2.axis('off')
        ax3.axis('off')
        #plt.tight_layout()
        ang = pedir_angulo()
        if abs(ang-angAnt)>1:
            v0x = v0*np.cos(np.radians(ang))
            v0y = v0*np.sin(np.radians(ang))

            th = ((-v0y)/-g)
            tt = th*2
            alc = v0x*tt
            h = (v0y*th)+((-g*(th**2))/2)

            t = np.arange(0, tt+0.1, 0.1)
            x = v0x*t
            x = x.tolist()
            y = (v0y*t)-((g*(t**2))/2)
            y = y.tolist()
            #updated_y = np.cos(x-0.05*p)

            if ang % 180 < 90:

                ax3.clear()
                ax2.imshow(img, vmin=0, vmax=1)
            else:
                ax2.clear()
                ax3.imshow(iimg, vmin=0, vmax=1)

            # line1.set_xdata(x)
            # line1.set_ydata(updated_y)

            # figure.canvas.draw()

            # figure.canvas.flush_events()
            ax.clear()
            #plt.ylim(0, (v0*((-v0)/-g))+((-g*(((-v0)/-g)**2))/2))
            #plt.xlim(-150, 150)
            ax.set_ylim(0, (v0*((-v0)/-g))+((-g*(((-v0)/-g)**2))/2))
            ax.set_xlim(-150, 150)
            #line1, = ax.plot(x, y)
            #time.sleep(1000)
            angAnt=ang
            print(ang,len(x),len(y))
