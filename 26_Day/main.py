import pygame
import random
from square import *
from circle import *
import sys
import pygwidgets

#define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES = 30
N_SHAPES = 10

#set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

shapesList = []
shapeClassTuple = (square,Circle)
for i in range(0,N_SHAPES):
    randomlyChoosenClass = random.choice(shapeClassTuple)
    oShape = randomlyChoosenClass(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    shapesList.append(oShape)

oStatusLine =pygwidgets.DisplayText(window,(4,4),"Click on shapes",fontSize=28)

#main loop
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
                for oShape in reversed(shapesList):
                    if oShape.clickedInside(event.pos):
                        area = oShape.getArea()
                        area = str(area)
                        theType = oShape.getArea()
                        newText = "Clcked on a"+ theType + "whose area is " + area
                        oStatusLine.setValue(newText)
                        break 
            
        
        window.fill(WHITE)
        for oShape in shapesList:
            oShape.draw()
        oStatusLine.draw()

        pygame.display.update()
        clock.tick(FRAMES)

        

