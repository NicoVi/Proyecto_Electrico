from tkinter import *
from tkinter import messagebox
import datetime
########################## MAIN WINDOW CONFIG ##################################

window = Tk()
window.title("Estimacion de precipitacion")
window.geometry('1200x650')
window.resizable(0,0)
window.config(bg="white")

##################### IMPORT THE CALIBRATION AND ALERT #########################

import Calibrate
import AttenValue

############################# FRAMES CONFIG ####################################
TimerFlag = True
B0, B1 = Calibrate.RunCalibrate()

linkDetail = Frame()
linkDetail.pack()
def linkDetailTimer():
    linkDetail.config(bg="white")
    linkDetail.config(width="1200", height="50")
    linkDetail.place(x=0,y=0)
    Label(linkDetail, text="Detalle del enlace San Pedro - UCR", bg="white", font=("Times New Roman",15)).place(x=450, y=1)
    updateTime = datetime.datetime.now().strftime("%H:%M:%S")
    Label(linkDetail,text= "Ultima actualizacion a las: ", bg="white", font=("Times New Roman",10)).place(x=508, y=22)
    Label(linkDetail,text= updateTime, bg="white", font=("Times New Roman",10)).place(x=648, y=22)
    if(TimerFlag):
        window.after(5000, linkDetailTimer)


def rainStatusTimer():
    rainStatus = Frame()
    rainStatus.pack()
    rainStatus.config(bg="white")
    rainStatus.config(width="600", height="100")
    rainStatus.place(x=0,y=50)
    Label(rainStatus,text= "Para esta hora, el nivel de lluvia en los alrededores de San Pedro es:", bg="white", font=("Times New Roman",13)).place(x=50, y=15)
    rainValue = AttenValue.getAttenValue(B0, B1)
    rainLevel = ""
    if rainValue <= 0.1:
        rainLevel = "Nulo"
    elif 0.2<rainValue<=5:
        rainLevel = "Bajo"
    elif 5.1<rainValue<=18:
        rainLevel = "Alto"
    elif 18.1<rainValue<=40:
        rainLevel = "Muy Alto"
    Label(rainStatus,text= rainLevel, bg="white", font=("Times New Roman",16)).place(x=280, y=60)
    print(rainValue)
    if(TimerFlag):
        window.after(5000, rainStatusTimer)

rainGraph = Frame()
rainGraph.pack()
rainGraph.config(bg="red")
rainGraph.config(width="600", height="500")
rainGraph.place(x=0,y=150)
rGImage = PhotoImage(file="DataVsSamples.png")
Label(rainGraph, image=rGImage).place(x=-1, y=-1)


calibrateInfo = Frame()
calibrateInfo.pack()
calibrateInfo.config(bg="black")
calibrateInfo.config(width="600", height="100")
calibrateInfo.place(x=600,y=50)
Label(calibrateInfo,text= "Ultima calibracion realizada a las: ", bg="white", font=("Times New Roman",11)).place(x=10, y=15)
updateTime = datetime.datetime.now().strftime("%H:%M:%S")
Label(calibrateInfo,text= updateTime, bg="white", font=("Times New Roman",11)).place(x=225, y=15)
Label(calibrateInfo,text= ", generando la siguiente relacion de atenuacion:", bg="white", font=("Times New Roman",11)).place(x=280, y=15)
Label(calibrateInfo,text= ("Lluvia=",B0,"+",B1,"*Atenuacion"), bg="white", font=("Times New Roman",11)).place(x=100, y=50)


gisShow = Frame()
gisShow.pack()
gisShow.config(bg="yellow")
gisShow.config(width="600", height="500")
gisShow.place(x=600,y=150)
Label(gisShow,text= "Detalle del enlace:", bg="white", font=("Times New Roman",13)).place(x=5, y=5)


linkDetailTimer()
rainStatusTimer()

window.mainloop()
