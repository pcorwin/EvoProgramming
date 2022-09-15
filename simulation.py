import time
from robot import ROBOT
from world import WORLD
import pybullet as p
import pybullet_data
import constants as c

class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)  # connect
        p.setAdditionalSearchPath(
            pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)  # creates gravity in simulated environment
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(0, c.steps):  # simulation loop
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(1 / 60)  # time between each step
            if i % 100 == 0:  # output timestamp for ease of use
                print(int(i / 100))

    def __del__(self):
        for m in self.robot.motors.values():
            m.Save_Values()
        for s in self.robot.sensors.values():
            s.Save_Values()
        p.disconnect()  # disconnect