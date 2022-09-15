import time
from robot import ROBOT
from world import WORLD
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)  # connect
        p.setAdditionalSearchPath(
            pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)  # creates gravity in simulated environment

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.ID)
        self.robot.Prepare_to_Sense()

    def Run(self):
        for i in range(0, c.steps):  # simulation loop
            #c.targetAngles[i] = c.amplitudeF * np.sin(c.frequencyF * c.targetAnglesFront[i] + c.phaseOffsetF)
            #c.targetAnglesBack[i] = c.amplitudeB * np.sin(c.frequencyB * c.targetAnglesBack[i] + c.phaseOffsetB)
            p.stepSimulation()
            self.robot.Sense(i)
            #c.bLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BLeg")
            #c.fLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FLeg")
            #self.robot.sensors.values()[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BLeg")
            #self.robot.sensors.values()[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FLeg")
            #pyrosim.Set_Motor_For_Joint(
            #    bodyIndex=1,
            #    jointName="Torso_BLeg",
            #    controlMode=2,
            #    targetPosition=c.targetAnglesBack[i],
            #    maxForce=500
            #)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=1,
            #     jointName="Torso_FLeg",
            #     controlMode=2,
            #     targetPosition=c.targetAnglesFront[i],
            #     maxForce=500
            # )
            time.sleep(1 / 60)  # time between each step
            if i % 100 == 0:  # output timestamp for ease of use
                print(int(i / 100))
        # np.save("data/bLeg", c.bLegSensorValues)
        # np.save("data/fLeg", c.fLegSensorValues)
        # np.save("data/frontMotorAngles", c.targetAnglesFront)
        # np.save("data/backMotorAngles", c.targetAnglesBack)

    def __del__(self):
        p.disconnect()  # disconnect