import time
import numpy

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

for i in range(0, STEPS):            #simulation loop
    p.stepSimulation()
    bLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BLeg")
    fLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FLeg")
    time.sleep(1/60)                #time between each step
    #if i % 100 == 0:                 #output timestamp for ease of use
    #    print(int(i/100))

numpy.save("data/bLeg",bLegSensorValues)
numpy.save("data/fLeg",fLegSensorValues)


p.disconnect()                      #disconnect
