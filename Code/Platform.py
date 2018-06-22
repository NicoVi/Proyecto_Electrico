import time
import Calibrate
import AttenAlert

##################### CALIBRATION AND HYPOTHESIS ###############################

B0, B1 = Calibrate.RunCalibrate()

################################################################################
def RunPlataform():

    AttenAlert.YCalc(5, B0, B1)
    time.sleep(10)

######################### INFINITE LOOP ########################################
while True:
    RunPlataform()
