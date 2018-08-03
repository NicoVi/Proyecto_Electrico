import numpy as np
from random import randrange
import time

dataYear = 2018
dataMonth = 1
dataDay = 1
dataHour = 555

def generateSample():
    global dataYear
    global dataMonth
    global dataDay
    global dataHour
    dataValue = randrange(46, 90) * (-1)
    dataArray = [dataYear, dataMonth, dataDay, dataHour, dataValue]
    np.savetxt('Sample.txt', dataArray, delimiter=',')
    if(dataHour == 1435):
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
    time.sleep(10)
