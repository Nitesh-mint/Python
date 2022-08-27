import pygame
from pygame.locals import *
from java import *
from SimpleButtonClass import *
from simpleText import *
import sys
import random

#define constants
WHITE = (255,255,255)
BLACK = (0,0,0)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES = 30

#intialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#initialze variables
oJava = Java(window, WINDOW_WIDTH,WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window,(60,20),"Program has to run through this many loops:",BLACK)
oFrameCountDisplay = SimpleText(window, (500,20),"", WHITE)
oRestartButton = simpleButton(window, (280,60),"/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg","/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")
frameCounter = 0

#while Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if oRestartButton.handleEvent(event):
            frameCounter = 0 #clicked the button , reset counter.
        
    oJava.update()
    frameCounter = frameCounter + 1 #increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

    #clear the window before doing it again
    window.fill(WHITE)

    #draw the window element
    oJava.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    #update the window
    pygame.display.update()

    clock.tick(FRAMES)