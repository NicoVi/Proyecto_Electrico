#Import necesary libreries
import pandas as pd
import numpy as np
import random as rm

#Reading CSV format:
#rainData=pd.read_csv('Rain.csv', header = 0, sep=";");
#print(rainData);

#Reading from txt format rain data:
RainData = np.genfromtxt('Rain.txt', delimiter=';')
RainYearData = RainData[:,0]
RainMonthData = RainData[:,1]
RainDayData = RainData[:,2]
RainHourData = RainData[:,3]
RainValue = RainData[:,4]

#Reading from txt format attenuation data:
AttnData = np.genfromtxt('Rain.txt', delimiter=';')
AttnYearData = AttnData[:,0]
AttnMonthData = AttnData[:,1]
AttnDayData = AttnData[:,2]
AttnHourData = AttnData[:,3]
AttnValue = AttnData[:,4]


print(len(RainData))
print(rm.random()*10)


def Hypothesis():

    Ht = 234.567 + 456.78*x;
    return Ht;
