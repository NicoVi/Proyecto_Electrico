import Calibrate
import numpy as np

a = np.array([])
b = 45

for x in xrange(len(RainData)-1, -1, -1):
    if RainValue[x] == 0:
        b = 45
        a = np.insert(a, 0, b)

    elif 0<RainValue[x]<=1:
        b = 45 - rm.random()*5
        a = np.insert(a, 0, b)

    elif 1<RainValue[x]<=5:
        b = 40 - rm.random()*5
        a = np.insert(a, 0, b)

    elif 5<RainValue[x]<=10:
        b = 35 - rm.random()*5
        a = np.insert(a, 0, b)

    elif 10<RainValue[x]<=20:
        b = 30 - rm.random()*5
        a = np.insert(a, 0, b)

    elif 20<RainValue[x]<=40:
        b = 25 - rm.random()*5
        a = np.insert(a, 0, b)

Atten = np.vstack(a)
np.savetxt('Attenuation.txt',Atten,delimiter=';')
print(Atten)
