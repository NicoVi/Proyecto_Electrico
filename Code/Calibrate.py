#Import necesary libreries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date


#Reading from txt format rain data:
RainData = np.genfromtxt('Data/RealRain.txt', delimiter=',')
RainYearData = RainData[:,0]
RainMonthData = RainData[:,1]
RainDayData = RainData[:,2]
RainHourData = RainData[:,3]
RainValue = RainData[:,4]



#Reading from txt format attenuation data:
AttnData = np.genfromtxt('Data/RealAtten.txt', delimiter=',')
AttnYearData = AttnData[:,0]
AttnMonthData = AttnData[:,1]
AttnDayData = AttnData[:,2]
AttnHourData = AttnData[:,3]
AttnValue = AttnData[:,4]



#Testing and generate X and Y matrix
X = np.array([])
Y = np.array([])
xList = []
for x in xrange(0, len(RainData)):
    if (RainYearData[x] == AttnYearData[x])and(RainMonthData[x] == AttnMonthData[x])and(RainDayData[x] == AttnDayData[x])and(RainHourData[x] == AttnHourData[x]):
        X = np.insert(X, x, AttnValue[x])
        Y = np.insert(Y, x, RainValue[x])
        if((x%200)==0):
            DateS = date(int(RainYearData[x]), int(RainMonthData[x]), int(RainDayData[x]))
            DateL = DateS.strftime("%d %B %Y")
            TimeX = '{:02d}:{:02d}'.format(*divmod(int(RainHourData[x]), 60))
            xList += [DateL+" "+TimeX]
        else:
            xList += [" "]

#Atten data show
ValuesGraph2D = plt.figure()
plt.rc('xtick', labelsize=6)
plt.title('Muestras de atenuacion del 15 de junio al 22 de junio')
plt.xticks(range(len(X)), xList, rotation=25)
plt.plot(X)
plt.ylabel("Atenuacion")
plt.savefig('Images/Atenuacion.png')

#Rain data show
rainGraphShow = plt.figure()
plt.rc('xtick', labelsize=6)
plt.title('Muestras de lluvia del 15 de junio al 22 de junio')
plt.xticks(range(len(Y)), xList, rotation=25)
plt.plot(Y)
plt.ylabel("Lluvia (mm)")
plt.savefig('Images/Lluvia.png')

#Full calibration show
CalibrationShow = plt.figure()
plt.subplot(2, 1, 1)
plt.title('Comparacion de muestras de lluvia y atenuacion')
plt.grid(True)
plt.plot(X)
plt.ylabel("Atenuacion (dB)")
plt.subplot(2, 1, 2)
plt.plot(Y)
plt.ylabel('Lluvia (mm)')
plt.xlabel("Total de datos")
plt.grid(True)
plt.savefig('Images/Calibration.png')

##################### MULTIPLE LINEAR REGRESSION METHOD ########################

#Generate necesary coeficients
Ynorm = np.array([])
for x in xrange(0, len(RainData)):
    Ynorm = np.insert(Ynorm, x, RainValue[x]*10)
m = len(Y)
X0 = np.ones(m)
Xmatrix = np.array([X0, X]).T
# Initial Values for the method
B = np.array([0, 0])
Ymatrix = Ynorm
alpha = 0.0002

#Cost function algorithm
def CostFunction(X, Y, B, m):
    J = np.sum((X.dot(B) - Y) ** 2)/(2 * m)
    return J


#Gradient descent algorithm
def GradientDescent(X, Y, B, alpha, m, iterations):
    CostHistory = [0] * iterations
    for iteration in range(iterations):
        # Hypothesis Values
        H = X.dot(B)
        # Difference b/w Hypothesis and Actual Y
        DiffHY = H - Y
        # Gradient Calculation
        Gradient = X.T.dot(DiffHY) / m
        # Changing Values of B using Gradient
        B = B - alpha * Gradient
        # New Cost Value
        Cost = CostFunction(X, Y, B, m)
        CostHistory[iteration] = Cost
    return B, CostHistory


############################ HYPOTHESIS VALUES #################################


def RunCalibrate():
    BForH, CostHistory = GradientDescent(Xmatrix, Ynorm, B, alpha, m, 1000000)
    H_X0 = BForH[0]
    H_X1 = BForH[1]
    return H_X0, H_X1
