from tkinter import *
from tkinter import messagebox
import datetime
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import time
import threading
import numpy as np
########################## MAIN WINDOW CONFIG ##################################

window = Tk()
window.title("Estimacion de precipitacion")
window.geometry('1200x650')
window.resizable(0,0)
window.config(bg="white")

##################### IMPORT THE CALIBRATION AND ALERT #########################

import Calibrate
import RainValueCalc

############################# DEFINITIONS ######################################

TimerFlag = True
graphDataY = np.zeros(9)
graphDataX = np.ones(9)*(-47)
counterG = 0
B0, B1 = Calibrate.RunCalibrate()

############################# FRAMES CONFIG ####################################


linkDetail = Frame()
linkDetail.pack()
def linkDetailTimer():
    linkDetail.config(bg="white")
    linkDetail.config(width="1200", height="50")
    linkDetail.config(bd = 5)
    linkDetail.config(relief = "ridge")
    linkDetail.place(x=0,y=0)
    Label(linkDetail, text="Detalle del enlace San Pedro - UCR", bg="white", font=("Times New Roman",15)).place(x=450, y=1)
    updateTime = datetime.datetime.now().strftime("%H:%M:%S")
    Label(linkDetail,text= "Ultima actualizacion a las: ", bg="white", font=("Times New Roman",10)).place(x=508, y=22)
    Label(linkDetail,text= updateTime, bg="white", font=("Times New Roman",10)).place(x=648, y=22)
    if(TimerFlag):
        window.after(10000, linkDetailTimer)


def rainStatusTimer():
    rainStatus = Frame()
    rainStatus.pack()
    rainStatus.config(bg="white")
    rainStatus.config(width="600", height="100")
    rainStatus.config(bd = 5)
    rainStatus.config(relief = "ridge")
    rainStatus.place(x=0,y=50)
    Label(rainStatus,text= "Para esta hora, el nivel de lluvia en los alrededores de San Pedro es:", bg="white", font=("Times New Roman",13)).place(x=50, y=15)
    rainValue, attenValue = RainValueCalc.getRainValue(B0, B1)
    rainLevel = ""
    if rainValue <= 0.1:
        rainLevel = "Nulo"
    elif 0.2<rainValue<=3:
        rainLevel = "Bajo"
    elif 3.1<rainValue<=5:
        rainLevel = "Alto"
    elif 5.1<rainValue<=20:
        rainLevel = "Muy Alto"
    Label(rainStatus,text= rainLevel, bg="white", font=("Times New Roman",16)).place(x=280, y=60)
    if(TimerFlag):
        window.after(10000, rainStatusTimer)


def rainGraphTimer():
    rainGraph = Frame()
    rainGraph.pack()
    rainGraph.config(bg="white")
    rainGraph.config(width="600", height="500")
    rainGraph.config(bd = 5)
    rainGraph.config(relief = "ridge")
    rainGraph.place(x=0,y=150)
    global counterG
    yVal, xVal = RainValueCalc.getRainValue(B0, B1)
    if (yVal<0):
        yVal = 0
    if(counterG<9):
        graphDataY[counterG] = yVal
        graphDataX[counterG] = xVal
    else:
        graphDataY[0] = graphDataY[1]
        graphDataY[1] = graphDataY[2]
        graphDataY[2] = graphDataY[3]
        graphDataY[3] = graphDataY[4]
        graphDataY[4] = graphDataY[5]
        graphDataY[5] = graphDataY[6]
        graphDataY[6] = graphDataY[7]
        graphDataY[7] = graphDataY[8]
        graphDataY[8] = yVal

        graphDataX[0] = graphDataX[1]
        graphDataX[1] = graphDataX[2]
        graphDataX[2] = graphDataX[3]
        graphDataX[3] = graphDataX[4]
        graphDataX[4] = graphDataX[5]
        graphDataX[5] = graphDataX[6]
        graphDataX[6] = graphDataX[7]
        graphDataX[7] = graphDataX[8]
        graphDataX[8] = xVal

    PromA = np.ones(8) * (-50)
    PromR = np.ones(8) * 0.4

    ValuesGraph2D = plt.figure(figsize=(5.9,4.9))
    plt.subplot(2, 1, 1)
    plt.title('Datos de atenuacion y lluvia estimada')
    plt.grid(True)
    plt.plot(graphDataX)
    plt.plot(PromA, label = "Promedio ultima hora")
    plt.legend(loc="upper right")
    plt.ylabel("Atenuacion")
    plt.subplot(2, 1, 2)
    plt.plot(graphDataY)
    plt.plot(PromR, label = "Promedio ultima hora")
    plt.legend(loc="upper right")
    plt.ylabel('Rain')
    plt.xlabel("Samples")
    plt.grid(True)

    counterG = counterG + 1

    graph = FigureCanvasTkAgg(ValuesGraph2D, master=rainGraph)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)
    graph.draw()

    if(TimerFlag):
        window.after(10000, rainGraphTimer)



calibrateInfo = Frame()
calibrateInfo.pack()
calibrateInfo.config(bg="white")
calibrateInfo.config(width="600", height="100")
calibrateInfo.config(bd = 5)
calibrateInfo.config(relief = "ridge")
calibrateInfo.place(x=600,y=50)
Label(calibrateInfo,text= "Ultima calibracion realizada a las: ", bg="white", font=("Times New Roman",11)).place(x=10, y=15)
updateTime = datetime.datetime.now().strftime("%H:%M:%S")
Label(calibrateInfo,text= updateTime, bg="white", font=("Times New Roman",11)).place(x=225, y=15)
Label(calibrateInfo,text= ", generando la siguiente relacion de atenuacion:", bg="white", font=("Times New Roman",11)).place(x=280, y=15)
Label(calibrateInfo,text= ("Lluvia=",B0,"+",B1,"*Atenuacion"), bg="white", font=("Times New Roman",11)).place(x=100, y=50)


gisShow = Frame()
gisShow.pack()
gisShow.config(bg="white")
gisShow.config(width="600", height="500")
gisShow.config(bd = 5)
gisShow.config(relief = "ridge")
gisShow.place(x=600,y=150)
Label(gisShow,text= "Detalle del enlace:", bg="white", font=("Times New Roman",13)).place(x=5, y=5)
MapImage = PhotoImage(file="Images/Map.png")
graphPlot = Label(gisShow, image=MapImage).place(x=50, y=50)


rainGraphTimer()
linkDetailTimer()
rainStatusTimer()


window.mainloop()
