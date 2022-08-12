from itertools import count


class Myclass():
    def __init__(self):
        self.count = 0 #creating self.count and set it to 0.
#create increment method.
    def increment(self):
        self.count = self.count + 1 #increment the varaible 
        return self.count

a = Myclass() #creates a Myclass object
print(a.increment()) #calling increment method