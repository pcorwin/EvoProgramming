import numpy
import matplotlib.pyplot as mp

bLegSensorValues = numpy.load("data/bLeg.npy")
fLegSensorValues = numpy.load("data/fLeg.npy")
targetAnglesF = numpy.load("data/frontMotorAngles.npy")
targetAnglesB = numpy.load("data/backMotorAngles.npy")

mp.plot(bLegSensorValues,label= "BackLeg")
mp.plot(fLegSensorValues,label= "FrontLeg")
mp.legend()
mp.show()

mp.plot(targetAnglesF,label= "Front")
mp.plot(targetAnglesB,label= "Back")
mp.legend()
mp.show()

