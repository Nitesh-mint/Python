#class to make a Button objects.
import pygame
from pygame.locals import *

class simpleButton():
    #used to track the state of the button
    STATE_IDLE = "idle" #button is up, mouse not over button
    STATE_ARMED = "armed" #button is down, mouse mover button
    STATE_DISARMED = "disarmed" #clicked down on button, rolled off

    def __init__(self,window, loc,up,down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        #get the rect of the button(used to see if the mouse is over the button?)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = simpleButton.STATE_IDLE
    
    def handleEvent(self, eventObj):
        #this method will return true if the user clicks the button
        #normally it is false
        if eventObj.type not in (MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN):
            return False
        
        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == simpleButton.STATE_IDLE:
            if(eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = simpleButton.STATE_ARMED
        elif self.state == simpleButton.STATE_ARMED:
            if(eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = simpleButton.STATE_ARMED
                return True#CLICKED
            if(eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = simpleButton.STATE_DISARMED
        elif self.state == simpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = simpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = simpleButton.STATE_IDLE   
            return False
    def draw(self):
        #draw the button current apperance to the widnow
        if self.state == simpleButton.STATE_IDLE:
            self.window.blit(self.surfaceDown,self.loc)

        else:
            self.window.blit(self.surfaceUp,self.loc)