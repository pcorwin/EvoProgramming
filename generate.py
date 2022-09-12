import pyrosim.pyrosim as pyrosim

l = 1       #length
w = 1       #width
h = 1       #height

x = 0       #initial x coord
y = 0       #initial y coord
z = 0.5     #initial z coord


def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box1", pos=[x+2,y+2,z], size=[l,w,h])
    pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[x,y,1.5], size=[l,w,h])
    pyrosim.Send_Joint(name="Torso_FLeg", parent="Torso", child="FLeg", type="revolute", position=[0.5,0,1])
    pyrosim.Send_Cube(name="FLeg", pos=[0.5,y,-0.5], size=[l,w,h])
    pyrosim.Send_Joint(name="Torso_BLeg", parent="Torso", child="BLeg", type="revolute", position=[-0.5,0,1])
    pyrosim.Send_Cube(name="BLeg", pos=[-0.5,y,-0.5], size=[l,w,h])

    #pyrosim.Send_Cube(name="Link0", pos=[x,y,z], size=[l,w,h])
    #pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0.5,0,1])
    #pyrosim.Send_Cube(name="Link1", pos=[0.5,y,z], size=[l,w,h])
    #pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[1,0,0])
    #pyrosim.Send_Cube(name="Link2", pos=[0.5,y,-0.5], size=[l,w,h])
    pyrosim.End()

create_world()
create_robot()

#pyrosim.Start_SDF("world.sdf")

#for i in range(0,10):
#    for j in range(0,10):
#        for k in range(0,2):
#            pyrosim.Send_Cube(name=f"Box[{i+1},{j+1}, {z+1}]", pos=[x + i, y + j, z + k], size=[l, w, h])

#pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size=[l,w,h])
#pyrosim.Send_Cube(name="Box2", pos=[x,y,z+1], size=[l,w,h])

#pyrosim.End()