import sys
from ursina import *
from ursina.color import rgba
import assetManagement as assets
import sampleSeeds as samples




#seed
stringSeed = input('Enter numeric Seed : ')
def getCharacter():
    seedCharsString = []
    for i in stringSeed:
        seedCharsString.append(i)
    return seedCharsString
#changing the seed into a float
def numberify_Seed(seedCharsString):
    seed = []
    try:
        for i in seedCharsString:
            seed.append(float(i)/100)
    except:
        print('please make sure all characters are numbers')
    return seed

seed = numberify_Seed(getCharacter())

boxes = []
#draw blank blocks with some data
def createBoxes(_position , state_float):
    Box = Entity(model = 'quad' , scale = (.5,.5) ,position = _position , color = rgba(255,255,255,state_float*20000))
    boxes.append(Box)
    return Box
#generate a Place holder world
def genWorldUntextured():
    for y in range (-5,5):
        for x in range (-10,10):
            createBoxes((x/2,y/2) ,  random.choice(seed))

app = Ursina()
#window Settings
window.borderless = False
window.show_ursina_splash = True
window.exit_button.enabled = False


#generate untextured world
genWorldUntextured()
app.run()
