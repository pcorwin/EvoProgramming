import math
import time
import numpy
import random

import numpy as np
import pybullet as p
import pybullet_data

import pyrosim.pyrosim as pyrosim

STEPS = 1000

physicsClient = p.connect(p.GUI)    #connect
p.setAdditionalSearchPath(
    pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)              #creates gravity in simulated environment

planeID = p.loadURDF("plane.urdf")  #imports 'floor' for simulated environment
robotID = p.loadURDF("body.urdf")   #imports robot body from generate.py
p.loadSDF("world.sdf")                #includes box created in generate.py for simulation

pyrosim.Prepare_To_Simulate(robotID)

bLegSensorValues = numpy.zeros(STEPS)
fLegSensorValues = numpy.zeros(STEPS)

targetAnglesFront = (numpy.linspace(-numpy.pi/4,numpy.pi/4,STEPS))
amplitudeF = numpy.pi/4
frequencyF = 10
phaseOffsetF = 0

targetAnglesBack = (numpy.linspace(-numpy.pi/4,numpy.pi/4,STEPS))
amplitudeB = numpy.pi/4
frequencyB = 10
phaseOffsetB = 5


for i in range(0, STEPS):            #simulation loop
    targetAnglesFront[i] = amplitudeF * np.sin(frequencyF * targetAnglesFront[i] + phaseOffsetF)
    targetAnglesBack[i] = amplitudeB * np.sin(frequencyB * targetAnglesBack[i] + phaseOffsetB)
    p.stepSimulation()
    bLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BLeg")
    fLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=1,
        jointName="Torso_BLeg",
        controlMode=2,
        targetPosition=targetAnglesBack[i],
        maxForce=500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=1,
        jointName="Torso_FLeg",
        controlMode=2,
        targetPosition=targetAnglesFront[i],
        maxForce=500
    )
    time.sleep(1/60)                #time between each step
    if i % 100 == 0:                 #output timestamp for ease of use
        print(int(i/100))

numpy.save("data/bLeg",bLegSensorValues)
numpy.save("data/fLeg",fLegSensorValues)
numpy.save("data/frontMotorAngles",targetAnglesFront)
numpy.save("data/backMotorAngles",targetAnglesBack)


p.disconnect()                      #disconnect
