#Import necesary libreries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
from mpl_toolkits.mplot3d import Axes3D



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


#Plotting for example
ValuesGraph2D = plt.figure(figsize=(6,5))
plt.plot(X)
plt.xlabel("Samples")
plt.ylabel("Data")
plt.ion()
plt.plot(Y)
plt.plot(X, label = "Attenuation")
plt.plot(Y, label = "Rain")
plt.legend(loc="center")
plt.savefig('DataVsSamples.png')
#plt.show()
ValuesGraph3D = plt.figure(figsize=(5,5))
Axes = Axes3D(ValuesGraph3D)
Axes.scatter(X, Y, color='#ef1434')
plt.savefig('3DPlot.png')
#plt.show()


##################### MULTIPLE LINEAR REGRESSION METHOD ########################


#Generate necesary coeficients
m = len(Y)
X0 = np.ones(m)
Xmatrix = np.array([X0, X]).T
# Initial Values for the method
B = np.array([0, 0])
Ymatrix = Y
alpha = 0.0001


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
    BForH, CostHistory = GradientDescent(Xmatrix, Y, B, alpha, m, 100000)
    H_X0 = BForH[0]
    H_X1 = BForH[1]
    return H_X0, H_X1
