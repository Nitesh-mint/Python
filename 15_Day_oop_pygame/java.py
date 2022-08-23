import pygame
from pygame.locals import *
import random

class Java():
    def __init__(self,window,window_width,window_height):
        self.window = window #for drawing the window later.
        self.window_width = window_width
        self.window_height =  window_height
        self.image = pygame.image.load("/home/nitesh/Desktop/OOP_in_python/13_Day/java.png")
        #a rect is made up of [x,y, width and height]
        javaRect = self.image.get_rect()
        self.width = javaRect.width
        self.height = javaRect.height
        self.max_width =window_width - self.width
        self.max_height =window_height - self.height

        #pick a random starting position
        self.x = random.randrange(0,self.max_width)
        self.y = random.randrange(0,self.max_height)

        #choose a random speed between -4 and 4 but not 0
        #in both x and y direction
        speedsList = [-4,-3,-2,-1,1,2,3,4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)
    
    def update(self):
        #check for java if it hits the corner or not
        if(self.x < 0) and (self.x >=self.max_width):
            self.xSpeed = -self.xSpeed
        if(self.y < 0) and (self.y >=self.max_height):
            self.ySpeed = -self.ySpeed
            
        #update the java's x and y in both direction
        self.x  = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image,(self.x, self.y))
