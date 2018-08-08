import numpy as np
from random import randrange
import time

dataYear = 2018
dataMonth = 3
dataDay = 5
dataHour = 555
dataCounter = -1
dataValue = -46
def generateSample():
    global dataYear
    global dataMonth
    global dataDay
    global dataHour
    global dataCounter
    global dataValue
    dataCounter += 1
    if 0<dataCounter<=5:
        dataValue = randrange(47, 48) * (-1)
    elif 5<dataCounter<=10:
        dataValue = randrange(50, 60) * (-1)
    elif 10<dataCounter<=15:
        dataValue = randrange(61, 74) * (-1)
    elif 15<dataCounter<=20:
        dataValue = randrange(75, 100) * (-1)
    elif 20<dataCounter<=25:
        dataValue = randrange(50, 60) * (-1)
        dataCounter = -1
    dataArray = [dataYear, dataMonth, dataDay, dataHour, dataValue]
    np.savetxt('Sample.txt', dataArray, delimiter=',')
    if(dataHour == 1425):
        if(dataDay == 31):
            if(dataMonth == 12):
                dataHour = 0
                dataDay = 1
                dataMonth = 1
                dataYear +=1
            else:
                dataHour = 0
                dataDay = 1
                dataMonth += 1
        else:
            dataHour = 0
            dataDay += 1
    else:
        dataHour += 15

while True:
    generateSample()
    time.sleep(5)
