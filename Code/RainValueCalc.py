import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
import Calibrate

############################ MAIN METHOD #######################################
def getRainValue(B0, B1):
########################## INPUT VALUES ########################################
    AttenSampleData = np.genfromtxt('AttenGenerator/Sample.txt', delimiter=';')
    AttenSampleYear = AttenSampleData[0]
    AttenSampleMonth = AttenSampleData[1]
    AttenSampleDay = AttenSampleData[2]
    AttenSampleHour = AttenSampleData[3]
    AttenSampleValue = AttenSampleData[4]
############################ HYPOTHESIS RESULT CALC ############################
    x = AttenSampleValue
    y = B0 + (B1 * x)

    return y, x
