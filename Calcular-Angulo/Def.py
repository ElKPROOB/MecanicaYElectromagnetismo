import os

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


def graf():
    pass


def pedir_angulo():
    angulo = serialArduino.readline().decode('cp1252')
    angulo = PurifyTxt(angulo, chars=["", [48, 57]])
    try:
        angulo = int(angulo)
    except:
        angulo = 45
    return angulo


if __name__ == "__main__":
    while True:
        #angl=input("Presione enter para continuar...")
        angl = pedir_angulo()
        #print(ang, angAnt)
        if abs(angl-angAnt) > 1:
            os.system('cls')
            angAnt = angl
            ang = angl
            print("Angulo: ", ang)
            graf()
            time.sleep(0.1)
