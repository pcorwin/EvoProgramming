import pyrosim.pyrosim as pyrosim

l = 1       #length
w = 1       #width
h = 1       #height

x = 0       #initial x coord
y = 0       #initial y coord
z = 0.5     #initial z coord

pyrosim.Start_SDF("boxes.sdf")

pyrosim.Send_Cube(name="Box1", pos=[x,y,z], size=[l,w,h])
pyrosim.Send_Cube(name="Box2", pos=[x,y,z+1], size=[l,w,h])

pyrosim.End()