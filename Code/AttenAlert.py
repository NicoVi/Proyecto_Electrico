import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
import Calibrate

############################ MAIN METHOD ###################################
def dataToShow():
########################## INPUT VALUES ########################################
    AttenSample = np.genfromtxt('Sample.txt', delimiter=';')
    AttenSampleYear = AttenSample[:,0]
    AttenSampleMonth = AttenSample[:,1]
    AttenSampleDay = AttenSample[:,2]
    AttenSampleHour = AttenSample[:,3]
    AttenSampleValue = AttenSample[:,4]
############################ HYPOTHESIS RESULT CALC ############################
def YCalc(X, B0, B1):
    Y = B0 + B1*X
    print(B0, B1)
    return Y
