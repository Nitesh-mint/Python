class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False

oLightSwitch = LightSwitch() # by this lightswitch object is created
print(oLightSwitch)

#oLightSwitch is the instance of the Lightswitch object. 