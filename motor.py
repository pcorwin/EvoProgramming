import random

import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName, a, f, p):
        self.jointName = jointName
        self.ampltiude = a
        self.phaseOffset = f
        self.frequency = p
        self.motorValues = (np.zeros(c.steps))
#        self.Prepare_to_Act()

    #def Prepare_to_Act(self):
    #    self.motorValues = self.ampltiude * np.sin(self.frequency * c.targetAngles + self.phaseOffset)

    def Set_Value(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
           bodyIndex=2,
           jointName=self.jointName,
           controlMode=2,
           targetPosition=desiredAngle,
           #targetPosition=self.motorValues[desiredAngle],
           maxForce=500
        )
    #def Save_Values(self):
    #    np.save(f"data/motor_{self.jointName}", self.motorValues)