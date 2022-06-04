from random import randint
from PIL import Image
import os

from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt


def pedir_angulo():
    print("Ingrese el angulo:")
    angulo = int(input())
    angulo=randint(0,90)
    return angulo


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
        plt.tight_layout()
        ang = pedir_angulo()
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
        line1, = ax.plot(x, y)
        # time.sleep(0.01)
