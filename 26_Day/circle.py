import pygame
import random
import math

#define colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Circle():
    def __init__(self,window,maxWidth,maxHeight):
        self.window = window
        self.color = random.choice((RED,GREEN,BLUE))
        self.X = random.randrange(1,maxWidth-100)
        self.Y = random.randrange(25,maxHeight-100)
        self.radius = random.randrange(10,50)
        self.centerX = self.X + self.radius
        self.centerY = self.Y + self.radius
        self.rect = pygame.Rect(self.X,self.Y,self.radius*2,self.radius*2)
        self.shape = "Circle"

    def clickedInside(self,mousePoint):
        distance = math.sqrt(((mousePoint[0] - self.centerX)**2)+((mousePoint[1]-self.centerY)**2))
        if distance <= self.radius:
            return True
        else:
            return False

    def getArea(self):
        theArea = math.pi*(self.radius ** 2)
        return theArea
    
    def getType(self):
        return self.Type

    def draw(self):
        pygame.draw.circle(self.window,self.color,(self.centerX,self.centerY),self.radius,0)