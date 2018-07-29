#Import necesary libreries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
from mpl_toolkits.mplot3d import Axes3D



#Reading from txt format rain data:
#RainData = np.genfromtxt('Rain.txt', delimiter=';')
RainData = np.genfromtxt('RealRain.txt', delimiter=';')
#RainYearData = RainData[:,0]
#RainMonthData = RainData[:,1]
#RainDayData = RainData[:,2]
#RainHourData = RainData[:,3]
#RainValue = RainData[:,4]
RainValue = RainData[:,1]
RainDate = RainData[:,0]


#Reading from txt format attenuation data:
#AttnData = np.genfromtxt('Attenuation.txt', delimiter=';')
AttnData = np.genfromtxt('RealAtten.txt', delimiter=',')
#AttnYearData = AttnData[:,0]
#AttnMonthData = AttnData[:,1]
#AttnDayData = AttnData[:,2]
#AttnHourData = AttnData[:,3]
#AttnValue = AttnData[:,4]
AttnValue = AttnData[:,1]
AttnDate = AttnData[:,0]


#Testing and generate X and Y matrix
X = np.array([])
Y = np.array([])
for x in xrange(0, len(RainData)):
    #if (RainYearData[x] == AttnYearData[x])and(RainMonthData[x] == AttnMonthData[x])and(RainDayData[x] == AttnDayData[x])and(RainHourData[x] == AttnHourData[x]):
    #if (AttnDate[x] == RainDate[x]):
        Xnorm = AttnValue[x]
        Ynorm = RainValue[x]
        X = np.insert(X, x, Xnorm)
        Y = np.insert(Y, x, Ynorm)



#Plotting for example
ValuesGraph2D = plt.figure(figsize=(6,5))
plt.subplot(2, 1, 1)
plt.title('Data comparison attenuation and rain')
plt.grid(True)
plt.plot(X)
plt.ylabel("Attenuation")
plt.subplot(2, 1, 2)
plt.plot(Y)
plt.ylabel('Rain')
plt.xlabel("Samples")
plt.grid(True)
plt.savefig('DataVsSamples.png')



##################### MULTIPLE LINEAR REGRESSION METHOD ########################

#Generate necesary coeficients
m = len(Y)
X0 = np.ones(m)
Xmatrix = np.array([X0, X]).T
# Initial Values for the method
B = np.array([0, 0])
Ymatrix = Y
alpha = 0.0002

print(m)
print(X0)
print(Xmatrix)
print(Ymatrix)

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
    BForH, CostHistory = GradientDescent(Xmatrix, Y, B, alpha, m, 1000000)
    H_X0 = BForH[0]
    H_X1 = BForH[1]
    return H_X0, H_X1

print(RunCalibrate())
