class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2,4,6,8,10,11,45,67,90]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM / 2
    
    def power(self): #this method is to power on the tv
        self.isOn = not self.isOn #not self.isON returns True
        
    
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False #changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM :
            self.volume = self.volume - 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # last ko channel ma puger add garyo bhane first channel ma leidine

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nchannels - 1 #last ko channel ma pughcha
    
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
    def setchannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)#finds the channel
        #if the newChannel is not in our list of channels, don't do anything

    def showInfo(self):
        print()
        print("TV Status:")
        if self.isOn:
            print("    TV is : On")
            print("    Channel is:",self.channelList[self.channelIndex])
            if self.isMuted:
                print("    Volume is: ", self.volume, "sound is muted")
            else:
                print("    Volume is: ", self.volume)
        else:
            print("    TV is: Off") 


oTV = TV()

oTV.power()
oTV.showInfo()

#changing the channel twice, raise the volume twice
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

#setting channel 
oTV.setchannel(10)
oTV.mute()
oTV.showInfo()

print()
