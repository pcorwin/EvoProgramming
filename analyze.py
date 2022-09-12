import numpy
import matplotlib.pyplot as mp

bLegSensorValues = numpy.load("data/bLeg.npy")
fLegSensorValues = numpy.load("data/fLeg.npy")

mp.plot(bLegSensorValues,label= "BackLeg")
mp.plot(fLegSensorValues,label= "FrontLeg")
mp.legend()
mp.show()
