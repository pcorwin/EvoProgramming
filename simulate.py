import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)    #connect
p.setAdditionalSearchPath(
    pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)              #creates gravity in simulated environment

planeID = p.loadURDF("plane.urdf")  #imports 'floor' for simulated environment
p.loadSDF("box.sdf")                #includes box created in generate.py for simulation

for i in range(0, 1000):            #simulation loop
    p.stepSimulation()
    time.sleep(1/60)                #time between each step
    if i % 10 == 0:                 #output timestamp for ease of use
        print(int(i/10))

p.disconnect()                      #disconnect
