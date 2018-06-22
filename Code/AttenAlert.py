import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
import Calibrate


############################ HYPOTHESIS CONSTANTS ##############################


def YCalc(X, B0, B1):
    Y = B0 + B1*X
    print(B0, B1)
    return Y

################################### INPUT VALUES ###############################
