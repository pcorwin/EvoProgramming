import pybullet as p
import time

physicsClient = p.connect(p.GUI)    #connect

p.loadSDF("box.sdf")                #includes box created in generate.py for simulation

for i in range(0, 1000):            #simulation loop
    p.stepSimulation()
    time.sleep(1/60)                #time between each step
    if i % 10 == 0:                 #output timestamp for ease of use
        print(int(i/10))

p.disconnect()                      #disconnect
