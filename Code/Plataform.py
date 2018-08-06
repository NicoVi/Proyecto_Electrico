from tkinter import *
from tkinter import messagebox
import datetime
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from datetime import date

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
PromR = np.ones(9)
PromVal = 0
xList = [" "," "," "," "," "," "," "," "," "]
clr = "#b5c3cb"
############################# FRAMES CONFIG ####################################


linkDetail = Frame()
linkDetail.pack()
def linkDetailTimer():
    linkDetail.config(bg=clr)
    linkDetail.config(width="1200", height="50")
    linkDetail.config(bd = 5)
    linkDetail.config(relief = "ridge")
    linkDetail.place(x=0,y=0)
    Label(linkDetail, text="Detalle del enlace San Pedro - UCR", bg=clr, font=("Times New Roman",15)).place(x=450, y=1)
    updateTime = datetime.datetime.now().strftime("%H:%M:%S")
    Label(linkDetail,text= "Ultima actualizacion a las: ", bg=clr, font=("Times New Roman",10)).place(x=496, y=22)
    Label(linkDetail,text= updateTime, bg=clr, font=("Times New Roman",10)).place(x=648, y=22)
    if(TimerFlag):
        window.after(10000, linkDetailTimer)


def rainStatusTimer():
    rainStatus = Frame()
    rainStatus.pack()
    rainStatus.config(bg="#b5c3cb")
    rainStatus.config(width="600", height="100")
    rainStatus.config(bd = 5)
    rainStatus.config(relief = "ridge")
    rainStatus.place(x=0,y=50)
    Label(rainStatus,text= "Para esta hora, el nivel de lluvia en los alrededores de San Pedro es:", bg="#b5c3cb", font=("Times New Roman",13)).place(x=50, y=15)
    rainLevel = ""
    if PromVal <= 0.1:
        rainLevel = "Nulo"
    elif 0.2<PromVal<=2.5:
        rainLevel = "Ligero"
    elif 2.6<PromVal<=7.6:
        rainLevel = "Moderado"
    elif 7.7<PromVal<=50:
        rainLevel = "Pesado"
    elif 7.7<PromVal<=50:
        rainLevel = "Violento"
    Label(rainStatus,text= rainLevel, bg="#b5c3cb", font=("Times New Roman",16,)).place(x=80, y=60)
    Label(rainStatus,text= "Valor promedio en ultima hora: ", bg="#b5c3cb", font=("Times New Roman",13,)).place(x=200, y=60)
    Label(rainStatus,text= "{0:.2f}".format(PromVal), bg="#b5c3cb", font=("Times New Roman",16,)).place(x=450, y=60)
    Label(rainStatus,text= "mm", bg="#b5c3cb", font=("Times New Roman",16,)).place(x=490, y=60)
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
    global PromVal
    global xList
    global clr
    yVal, xVal, gYear, gMonth, gDay, gHour = RainValueCalc.getRainValue(B0, B1)
    DateS = date(int(gYear), int(gMonth), int(gDay))
    DateL =  DateS.strftime("%b %d %Y")
    TimeX = '{:02d}:{:02d}'.format(*divmod(int(gHour), 60))

    if (yVal<0):
        yVal = 0
    if(counterG<9):
        graphDataY[counterG] = yVal
        graphDataX[counterG] = xVal
        xList[counterG] = TimeX
        if(counterG<5):
            PromVal = (np.sum(graphDataY)/(counterG+1))
            PromR = np.ones(9)*PromVal
        else:
            SumVal = graphDataY[counterG] + graphDataY[counterG-1] + graphDataY[counterG-2] + graphDataY[counterG-3] + graphDataY[counterG-4]
            PromVal = (SumVal/5)
            PromR = np.ones(9)*PromVal

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

        xList[0] = xList[1]
        xList[1] = xList[2]
        xList[2] = xList[3]
        xList[3] = xList[4]
        xList[4] = xList[5]
        xList[5] = xList[6]
        xList[6] = xList[7]
        xList[7] = xList[8]
        xList[8] = TimeX

        SumVal = graphDataY[8] + graphDataY[7] + graphDataY[6] + graphDataY[5] + graphDataY[4]
        PromVal = SumVal/5
        PromR = np.ones(9)*PromVal


    ValuesGraph2D = plt.figure(figsize=(5.9,4.9))
    plt.subplot(2, 1, 1)
    plt.title("Fecha actual: "+DateL)
    plt.plot(graphDataX)
    plt.xticks(range(len(graphDataX)), xList, rotation=15)
    plt.legend(loc="upper right")
    plt.ylabel("Atenuacion (dB)")
    plt.grid(True)
    plt.subplot(2, 1, 2)
    X = np.arange(9)
    if PromVal <= 0.1:
        clr = "#b5c3cb"
    elif 0.2<PromVal<=2.5:
        clr = "#277ece"
    elif 2.6<PromVal<=7.6:
        clr = "#00a563"
    elif 7.7<PromVal<=50:
        clr = "#ffc100"
    elif 7.7<PromVal<=50:
        clr = "#8e0e0e"
    plt.bar(X, graphDataY, color = clr, width = 0.50)
    plt.xticks(range(len(graphDataY)), xList, rotation=25)
    plt.plot(PromR, label = "Promedio ultima hora")
    plt.legend(loc="upper right")
    plt.ylabel('Lluvia (mm)')
    plt.grid(True)

    counterG = counterG + 1

    graph = FigureCanvasTkAgg(ValuesGraph2D, master=rainGraph)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)
    graph.draw()

    if(TimerFlag):
        window.after(10000, rainGraphTimer)



calibrateInfo = Frame()
calibrateInfo.pack()
calibrateInfo.config(bg="#b5c3cb")
calibrateInfo.config(width="600", height="100")
calibrateInfo.config(bd = 5)
calibrateInfo.config(relief = "ridge")
calibrateInfo.place(x=600,y=50)
Label(calibrateInfo,text= "Ultima calibracion realizada a las: ", bg="#b5c3cb", font=("Times New Roman",11)).place(x=10, y=15)
updateTime = datetime.datetime.now().strftime("%H:%M:%S")
Label(calibrateInfo,text= updateTime, bg="#b5c3cb", font=("Times New Roman",11)).place(x=225, y=15)
Label(calibrateInfo,text= ", generando la siguiente relacion de atenuacion:", bg="#b5c3cb", font=("Times New Roman",11)).place(x=280, y=15)
Label(calibrateInfo,text= ("Lluvia=",B0,"+",B1,"*Atenuacion"), bg="#b5c3cb", font=("Times New Roman",11)).place(x=100, y=50)


gisShow = Frame()
gisShow.pack()
gisShow.config(bg="white")
gisShow.config(width="600", height="500")
gisShow.config(bd = 5)
gisShow.config(relief = "ridge")
gisShow.place(x=600,y=150)
Label(gisShow,text= "Detalle geografico del enlace:", bg="white", font=("Times New Roman",13)).place(x=5, y=5)
MapImage = PhotoImage(file="Images/Map.png")
graphPlot = Label(gisShow, image=MapImage).place(x=50, y=50)


rainGraphTimer()
linkDetailTimer()
rainStatusTimer()


window.mainloop()
