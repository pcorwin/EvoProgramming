import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):

        self.motors = {}
        self.ID = p.loadURDF("body.urdf")  # imports robot body from generate.py

    def Prepare_to_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
