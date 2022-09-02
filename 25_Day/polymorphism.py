class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(self.name, "Bhaw Bhaw Bhw.!")
    
class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(self.name, "MEow Meow!")

class Bird():
    def __init__(self, name):
        self.name =  name
    
    def speak(self):
        print(self.name,"Tweeet")


oDog = Dog("BHUNTE")
oCat = Cat("Maya")
oBird = Bird("Fiste")

listAnimal = [oDog,oCat,oBird]

for i in listAnimal:
    i.speak()