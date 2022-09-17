import pygame
import random

RED = (255,0,0)
GREEN= (0,255,0)
BLUE = (0,0,255)

class Rectange():
    def __init__(self,window):
        self.window = window
        self.width = random.choice((20,30,40))
        self.height = random.choice((20,30,40))
        self.color = random.choice((RED,GREEN,BLUE))
        self.x = random.randrange(0,400)
        self.y = random.randrange(0,400)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.area = self.width * self.height

    def clickedInside(self,mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    #magic method call when you compare two rectangles with == operator.
    def __eq__(self,oOtherRectangle):
        if not isinstance(oOtherRectangle,Rectange):
            raise TypeError("Second object was not recatangle.")
        if self.area == oOtherRectangle.area:
            return True
        else:
            return False
        
    #magic method call when you compare two rectangles with < operator.
    def __lt__(self,oOtherRectangle):
        if not isinstance(self,oOtherRectangle):
            raise TypeError("Second object was not rectangle.")
        if self.area < oOtherRectangle.area:
            return True
        else:
            return False
        

    #magic method for greater or not?
    def __gt__(self,oOtherRectangle):
        if not isinstance(self,oOtherRectangle):
            raise TypeError("Second object was not rectangle.")
        if self.area < oOtherRectangle.area:
            return True
        else:
            return False
    
    def getArea(self):
        return self.area
    
    def draw(self):
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.height))