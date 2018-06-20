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
AttnData = np.genfromtxt('Attenuation.txt', delimiter=';')
AttnYearData = AttnData[:,0]
AttnMonthData = AttnData[:,1]
AttnDayData = AttnData[:,2]
AttnHourData = AttnData[:,3]
AttnValue = AttnData[:,4]

#Testing and generate X and Y matrix
X = np.array([])
Y = np.array([])
for x in xrange(0, len(RainData)):
    if (RainYearData[x] == AttnYearData[x])and(RainMonthData[x] == AttnMonthData[x])and(RainDayData[x] == AttnDayData[x])and(RainHourData[x] == AttnHourData[x]):
        X = np.insert(X, x, AttnValue[x])
        Y = np.insert(Y, x, RainValue[x])

#




def Hypothesis():

    Ht = 234.567 + 456.78*x;
    return Ht;
