import numpy
import matplotlib.pyplot as mp

bLegSensorValues = numpy.load("data/sensor_BLeg.npy")
fLegSensorValues = numpy.load("data/sensor_FLeg.npy")
targetAnglesF = numpy.load("data/motor_Torso_BLeg.npy")
targetAnglesB = numpy.load("data/motor_Torso_FLeg.npy")

mp.plot(bLegSensorValues,label= "BackLeg")
mp.plot(fLegSensorValues,label= "FrontLeg")
mp.legend()
mp.show()

mp.plot(targetAnglesF,label= "Back")
mp.plot(targetAnglesB,label= "Front")
mp.legend()
mp.show()

