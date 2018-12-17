import numpy as np
import matplotlib.pyplot as plt
#import geopandas as gp
import Calibrate
import datetime
############################ MAIN METHOD #######################################
def getexpValue(a, b, c, m): 
############################ HYPOTHESIS RESULT CALC ############################


    x= np.fromfile('AttenGenerator/Atenuacion', dtype=np.float32);
    x=x[m:len(x)]
    m=len(x)+m
    x=sum(x) / len(x)
    Xmean, Xmax, Xmin, Ymean, Ymax, Ymin = Calibrate.GetImpValues()
    Xnorm = (x-Xmean)/(Xmax-Xmin)
    Ynorm=a* np.exp(-b * Xnorm) + c
    y = ((Ymax-Ymin)*(Ynorm))+Ymean
    AttenSampleYear = datetime.date.today().strftime("%Y")
    AttenSampleMonth = datetime.date.today().strftime("%m")
    AttenSampleDay = datetime.date.today().strftime("%d")
    AttenSampleHour = datetime.datetime.now().strftime("%H:%M")
    return y, x, m, AttenSampleYear, AttenSampleMonth, AttenSampleDay, AttenSampleHour
