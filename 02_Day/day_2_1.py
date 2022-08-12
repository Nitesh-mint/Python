
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    
    def turnOn(self):
        self.switchIsOn = True
    
    def turnOff(self):
        self.switchIsOn = False
    
    def show(self):#to show the output
        return self.switchIsOn

oLightswitch1 = LightSwitch() #creates a light switch oject
oLightswitch2 = LightSwitch() #creates another light switch object

oLightswitch1.turnOn()
print(oLightswitch1.show())

oLightswitch2.turnOff()
print(oLightswitch2.show())