import pyrosim.pyrosim as pyrosim

l = 1       #length
w = 1       #width
h = 1       #height

x = 0       #initial x coord
y = 0       #initial y coord
z = 0.5     #initial z coord

pyrosim.Start_SDF("boxes.sdf")

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,2):
            pyrosim.Send_Cube(name=f"Box[{i+1},{j+1}, {z+1}]", pos=[x + i, y + j, z + k], size=[l, w, h])

#pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size=[l,w,h])
#pyrosim.Send_Cube(name="Box2", pos=[x,y,z+1], size=[l,w,h])

pyrosim.End()