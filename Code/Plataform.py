from tkinter import *
import datetime
import time

########################## MAIN WINDOW CONFIG ##################################

window = Tk()
window.title("Estimacion de precipitacion")
window.geometry('1200x650')
window.resizable(0,0)
window.config(bg="white")
import Calibrate
import AttenAlert
TimerFlag = True
B0, B1 = Calibrate.RunCalibrate()
############################# FRAMES CONFIG ####################################

linkDetail = Frame()
linkDetail.pack()
def linkDetailTimer():
    linkDetail.config(bg="white")
    linkDetail.config(width="1200", height="50")
    linkDetail.place(x=0,y=0)
    Label(linkDetail, text="Detalle del enlace San Pedro - UCR", bg="white", font=("Times New Roman",15)).place(x=500, y=1)
    updateTime = datetime.datetime.now().strftime("%H:%M:%S")
    Label(linkDetail,text= "Ultima actualizacion a las: ", bg="white", font=("Times New Roman",10)).place(x=548, y=22)
    Label(linkDetail,text= updateTime, bg="white", font=("Times New Roman",10)).place(x=698, y=22)
    if(TimerFlag):
        window.after(5000, linkDetailTimer)

rainStatus = Frame()
rainStatus.pack()
rainStatus.config(bg="white")
rainStatus.config(width="600", height="100")
rainStatus.place(x=0,y=50)


rainGraph = Frame()
rainGraph.pack()
rainGraph.config(bg="white")
rainGraph.config(width="600", height="500")
rainGraph.place(x=0,y=150)
rGImage = PhotoImage(file="DataVsSamples.png")
Label(rainGraph, image=rGImage).place(x=-1, y=-1)


calibrateInfo = Frame()
calibrateInfo.pack()
calibrateInfo.config(bg="white")
calibrateInfo.config(width="600", height="100")
calibrateInfo.place(x=600,y=50)


gisShow = Frame()
gisShow.pack()
gisShow.config(bg="white")
gisShow.config(width="600", height="500")
gisShow.place(x=600,y=150)



linkDetailTimer()


window.mainloop()
