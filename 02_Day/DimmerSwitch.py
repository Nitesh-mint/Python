'''
The switch state(on or off)
Brightness level(o to 10)
'''

class Dimmerswitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
    def turnOn(self):
        self.switchIsOn = True
    def raiselevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    def lowerlevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
    def show(self):
        print('switch is on?', self.switchIsOn)
        print('Brightness is:',self.brightness)
    
oDimmer = Dimmerswitch()

oDimmer.turnOn()
print(oDimmer.show())
oDimmer.raiselevel()
print(oDimmer.show())
print()

#creating multiple objects
oDimmer1 = Dimmerswitch()
oDimmer1.turnOn()
oDimmer1.raiselevel()

oDimmer2 = Dimmerswitch()
oDimmer2.turnOn()
oDimmer2.raiselevel()

print(oDimmer1.show())
print()
print(oDimmer2.show())