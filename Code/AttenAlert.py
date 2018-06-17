import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
import Calibrate

MatrixResults = np.zeros((5,5))

def main():

    DataArray = np.genfromtxt('DatosAtenuacion.txt', delimiter=',')
    x1 = DataArray[0]
    x2 = DataArray[1]
    x3 = DataArray[2]
    x4 = DataArray[3]


    DataArray = np.insert(DataArray,5,y)


main()
