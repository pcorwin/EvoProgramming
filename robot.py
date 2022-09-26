import pybullet as p
import constants as c
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.ID = p.loadURDF("body.urdf")  # imports robot body from generate.py
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.ID)
        self.Prepare_to_Sense()
        self.Prepare_to_Act()

    def Prepare_to_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for s in self.sensors.values():
            s.Get_Value(t)

    def Prepare_to_Act(self):
        first = True
        for jointName in pyrosim.jointNamesToIndices:
            if first:
                self.motors[jointName] = MOTOR(jointName,
                                               c.amplitudeA,
                                               c.frequencyA,
                                               c.phaseOffsetA)
                first = False
            else:
                self.motors[jointName] = MOTOR(jointName,
                                               c.amplitudeB,
                                               c.frequencyB,
                                               c.phaseOffsetB)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)
        #for m in self.motors.values():
        #    m.Set_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
