import sys
from ursina import *


boxes = []
#draw blank blocks with some data
def createBoxes(_position):
    Box = Entity(model = 'quad' , scale = (.5,.5) , box_Type = 'PlaceHolder' ,position = _position , color = random.choice([color.blue , color.green]))
    boxes.append(Box)
    return Box
#generate a Place holder world
def genWorldUntextured():
    for y in range (-5,5):
        for x in range (-10,10):
            createBoxes((x/2,y/2))


def PaintWorld():
    print('repainting World')
app = Ursina()
#generate untextured world
genWorldUntextured()
app.run()
