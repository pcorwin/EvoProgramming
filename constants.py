import numpy as np

steps = 1000

amplitudeB = np.pi/4
frequencyB = 10
phaseOffsetB = 5

amplitudeF = np.pi/4
frequencyF = 10
phaseOffsetF = 0

bLegSensorValues = np.zeros(steps)
fLegSensorValues = np.zeros(steps)

targetAnglesFront = (np.linspace(-np.pi / 4, np.pi / 4, steps))
targetAnglesBack = (np.linspace(-np.pi / 4, np.pi / 4, steps))
