class Car():
    def __init__(self,wheel,color,door):
        self.wheel = wheel #it is global(instance) variable.
        self.color = color
        self.door  = door

#object initilization
tesla = Car(4,"white","door") #creates an object named tesla
print(tesla.color) #to get the attributes of the car tesla object

