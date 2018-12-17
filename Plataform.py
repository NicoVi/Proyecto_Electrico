from tkinter import *
from tkinter import messagebox
import datetime
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from datetime import date
plt.rcParams.update({'figure.max_open_warning': 0})
import time
import threading
import pandas as pd
import numpy as np

########################## MAIN WINDOW CONFIG ##################################

window = Tk()
window.title("Estimacion de precipitacion")
window.geometry('1300x700')
window.resizable(0,0)
window.config(bg="white")

##################### IMPORT THE CALIBRATION AND ALERT #########################

import Calibrate
import RainValueCalc
import RainexpCalc
############################# DEFINITIONS ######################################

TimerFlag = True
sTime = 5000
m = 0
graphDataY = np.zeros(9)
graphDataX = np.ones(9)*(-47)
counterG = 0
B0, B1 = Calibrate.RunCalibrate()
a, b, c = Calibrate.expfunc()
PromR = np.ones(9)
PromVal = 0
xList = [" "," "," "," "," "," "," "," "," "]
clr = "#b5c3cb"
############################# FRAMES CONFIG ####################################


linkDetail = Frame()
linkDetail.pack()
def linkDetailTimer():
    linkDetail.config(bg=clr)
    linkDetail.config(width="1300", height="100")
    linkDetail.config(bd = 5)
    linkDetail.config(relief = "ridge")
    linkDetail.place(x=0,y=0)
    Label(linkDetail, text="Detalle del enlace San Pedro - UCR", bg=clr, font=("Times New Roman",15)).place(x=500, y=1)
    updateTime = datetime.datetime.now().strftime("%H:%M:%S")
    #Label(linkDetail,text= "Ultima actualizacion a las: ", bg=clr, font=("Times New Roman",10)).place(x=546, y=18)
    #Label(linkDetail,text= updateTime, bg=clr, font=("Times New Roman",10)).place(x=698, y=18)
    Label(linkDetail, text="Este programa extrae datos de atenuacion cada cierto tiempo, los procesa y genera el calculo estimado de nivel de precipitacion equivalente, la grafica que se muestra se actualiza conforme recibe una nueva", bg=clr, font=("Times New Roman",11)).place(x=20, y=25)
    Label(linkDetail, text="muestra. El detalle del valor promedio de precipitacion en la ultima hora se representa mediante el cambio de color en la ventana y la grafica, asi como tambien de manera textual. Los valores de atenuacion", bg=clr, font=("Times New Roman",11)).place(x=20, y=45)
    Label(linkDetail, text="para esta demostracion son generados por un algorimo que exporta un archivo de texto a un directorio cada 5 segundos.", bg=clr, font=("Times New Roman",11)).place(x=20, y=65)

    if(TimerFlag):
        window.after(sTime, linkDetailTimer)


def rainStatusTimer():
    rainStatus = Frame()
    rainStatus.pack()
    rainStatus.config(bg="#b5c3cb")
    rainStatus.config(width="600", height="100")
    rainStatus.config(bd = 5)
    rainStatus.config(relief = "ridge")
    rainStatus.place(x=100,y=100)
    Label(rainStatus,text= "El nivel de lluvia en los alrededores de San Pedro es:", bg="#b5c3cb", font=("Times New Roman",13)).place(x=50, y=15)
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
    Label(rainStatus,text= "Valor promedio: ", bg="#b5c3cb", font=("Times New Roman",13,)).place(x=200, y=60)
    Label(rainStatus,text= "{0:.2f}".format(PromVal), bg="#b5c3cb", font=("Times New Roman",16,)).place(x=450, y=60)
    Label(rainStatus,text= "mm", bg="#b5c3cb", font=("Times New Roman",16,)).place(x=490, y=60)
    if(TimerFlag):
        window.after(sTime, rainStatusTimer)


def rainGraphTimer():
    rainGraph = Frame()
    rainGraph.pack()
    rainGraph.config(bg="white")
    rainGraph.config(width="600", height="500")
    rainGraph.config(bd = 5)
    rainGraph.config(relief = "ridge")
    rainGraph.place(x=100,y=200)
    global m
    global counterG
    global PromVal
    global xList
    global clr
  #yVal, xVal, gYear, gMonth, gDay, gHour = RainValueCalc.getRainValue(B0, B1)
    yVal, xVal, contador, gYear, gMonth, gDay, gHour = RainexpCalc.getexpValue(a, b, c, m)
    DateS = date(int(gYear), int(gMonth), int(gDay))
    DateL =  DateS.strftime("%b %d %Y")
    #TimeX = '{:02d}:{:02d}'.format(*divmod(int(gHour), 60))
    TimeX = gHour

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
    m= contador +1

    graph = FigureCanvasTkAgg(ValuesGraph2D, master=rainGraph)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)
    graph.draw()

    if(TimerFlag):
        window.after(sTime, rainGraphTimer)



calibrateInfo = Frame()
calibrateInfo.pack()
calibrateInfo.config(bg="#b5c3cb")
calibrateInfo.config(width="600", height="100")
calibrateInfo.config(bd = 5)
calibrateInfo.config(relief = "ridge")
calibrateInfo.place(x=700,y=100)
Label(calibrateInfo,text= "Ultima calibracion realizada a las: ", bg="#b5c3cb", font=("Times New Roman",11)).place(x=10, y=15)
updateTime = datetime.datetime.now().strftime("%H:%M:%S")
Label(calibrateInfo,text= updateTime, bg="#b5c3cb", font=("Times New Roman",11)).place(x=225, y=15)
Label(calibrateInfo,text= ", generando la siguiente relacion de atenuacion:", bg="#b5c3cb", font=("Times New Roman",11)).place(x=280, y=15)
#Label(calibrateInfo,text= ("Lluvia=",B0,"+",B1,"*Atenuacion"), bg="#b5c3cb", font=("Times New Roman",11)).place(x=100, y=50)
Label(calibrateInfo,text= ("Lluvia=",a,"exp(",-b,"*Atenuacion)", c), bg="#b5c3cb", font=("Times New Roman",11)).place(x=20, y=50)

gisShow = Frame()
gisShow.pack()
gisShow.config(bg="white")
gisShow.config(width="600", height="500")
gisShow.config(bd = 5)
gisShow.config(relief = "ridge")
gisShow.place(x=700,y=200)
Label(gisShow,text= "Detalle geografico del enlace:", bg="white", font=("Times New Roman",13)).place(x=5, y=5)
MapImage = PhotoImage(file="Images/Map.png")
graphPlot = Label(gisShow, image=MapImage).place(x=50, y=50)

scaleDetail = Frame()
scaleDetail.pack()
scaleDetail.config(bg="#b5c3cb")
scaleDetail.config(width="100", height="100")
scaleDetail.config(bd = 5)
scaleDetail.config(relief = "ridge")
scaleDetail.place(x=0,y=100)
Label(scaleDetail,text= "Escala de", bg="#b5c3cb", font=("Times New Roman",12)).place(x=10, y=5)
Label(scaleDetail,text= "intensidad", bg="#b5c3cb", font=("Times New Roman",12)).place(x=8, y=25)
Label(scaleDetail,text= "de la", bg="#b5c3cb", font=("Times New Roman",12)).place(x=25, y=45)
Label(scaleDetail,text= "Lluvia mm/h", bg="#b5c3cb", font=("Times New Roman",12)).place(x=3, y=65)


scaleShow = Frame()
scaleShow.pack()
scaleShow.config(bg="white")
scaleShow.config(width="100", height="500")
scaleShow.config(bd = 5)
scaleShow.config(relief = "ridge")
scaleShow.place(x=0,y=200)
Label(scaleShow,text= "Nulo", bg="white", font=("Times New Roman",12)).place(x=25, y=20)
Label(scaleShow,text= "X < 0.1", bg="white", font=("Times New Roman",10)).place(x=20, y=40)
Label(scaleShow,text= "Ligero", bg="white", font=("Times New Roman",12)).place(x=20, y=60)
Label(scaleShow,text= "0.1 < X < 2.5", bg="white", font=("Times New Roman",10)).place(x=5, y=80)
Label(scaleShow,text= "Moderado", bg="white", font=("Times New Roman",12)).place(x=12, y=100)
Label(scaleShow,text= "2.5 < X < 7.6", bg="white", font=("Times New Roman",10)).place(x=5, y=120)
Label(scaleShow,text= "Pesado", bg="white", font=("Times New Roman",12)).place(x=18, y=140)
Label(scaleShow,text= "7.6 < X < 50", bg="white", font=("Times New Roman",10)).place(x=5, y=160)
Label(scaleShow,text= "Violento", bg="white", font=("Times New Roman",12)).place(x=13, y=180)
Label(scaleShow,text= "X > 50", bg="white", font=("Times New Roman",10)).place(x=20, y=200)

Label(scaleShow,text= "Codigo de", bg="white", font=("Times New Roman",12)).place(x=5, y=285)
Label(scaleShow,text= "colores:", bg="white", font=("Times New Roman",12)).place(x=15, y=308)
Label(scaleShow,text= "             ", bg="#b5c3cb", font=("Times New Roman",13)).place(x=5, y=340)
Label(scaleShow,text= "N", bg="White", font=("Times New Roman",13)).place(x=70, y=340)
Label(scaleShow,text= "             ", bg="#277ece", font=("Times New Roman",13)).place(x=5, y=360)
Label(scaleShow,text= "L", bg="White", font=("Times New Roman",13)).place(x=70, y=360)
Label(scaleShow,text= "             ", bg="#00a563", font=("Times New Roman",13)).place(x=5, y=380)
Label(scaleShow,text= "M", bg="White", font=("Times New Roman",13)).place(x=70, y=380)
Label(scaleShow,text= "             ", bg="#ffc100", font=("Times New Roman",13)).place(x=5, y=400)
Label(scaleShow,text= "P", bg="White", font=("Times New Roman",13)).place(x=70, y=400)
Label(scaleShow,text= "             ", bg="#8e0e0e", font=("Times New Roman",13)).place(x=5, y=420)
Label(scaleShow,text= "V", bg="White", font=("Times New Roman",13)).place(x=70, y=420)





rainGraphTimer()
linkDetailTimer()
rainStatusTimer()


window.mainloop()
