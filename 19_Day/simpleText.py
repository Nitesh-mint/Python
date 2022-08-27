from curses import window
import pygame
from pygame.locals import *

class SimpleText():
    def __init__(self,window,loc,value,textColor):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None,30)
        self.textColor = textColor
        self.text = None
        self.setValue(value)
    
    def setValue(self, newText):
        if self.text == newText:
            return  #noting to change 

        self.text = newText 
        self.textSurface = self.font.render(self.text,True,self.textColor)
    
    def draw(self):
        self.window.blit(self.textSurface,self.loc) 