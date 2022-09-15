import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.steps)
    def Prepare_to_Act(self, t):
        self.ampltiude = c.amplitude
        self.phaseOffset = c.phaseOffset
        self.frequency = c.frequency
        c.targetAngles[t] = self.ampltiude * \
                            np.sin(self.frequency * c.targetAngles[t] + self.phaseOffset)

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=1,
            jointName=self.jointName,
            controlMode=2,
            targetPosition=c.targetAngles[t],
            maxForce=500
        )