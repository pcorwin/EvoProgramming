import pybullet as p

class WORLD:
    def __init__(self):
        self.planeID = p.loadURDF("plane.urdf")  # imports 'floor' for simulated environment
        p.loadSDF("world.sdf")  # includes box created in generate.py for simulation