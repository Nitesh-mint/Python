from types import GeneratorType
import pygame
from pygame.locals import *
import sys

#define constants
WHITE = (255,255,255)
BLACK = (0,0,0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

#initialze wolrd
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

#LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)  
    #draw all window elements
    
    #draw a box
    pygame.draw.line(window,BLACK, (20,20),(60,20),4) #top
    pygame.draw.line(window,BLACK, (20,20),(20,60),4) #left
    pygame.draw.line(window, BLACK, (20,60), (60,60), 4) #bottom
    pygame.draw.line(window,BLACK, (60,20),(60,60),4)

    #draw an x in the box
    pygame.draw.line(window,BLACK, (20,20),(60,60), 1)
    pygame.draw.line(window,BLACK, (20,60), (60,20),1)

    #draw a filled and empty circle
    pygame.draw.circle(window, BLACK, (250,50), 30,0) #filled circle
    pygame.draw.circle(window,BLACK, (400, 50), 30,2) #2 pixel edge

    #draw filled and empty rectangle
    pygame.draw.rect(window,BLACK, (250, 150, 100, 50),0) #filled 
    pygame.draw.rect(window, BLACK, (400, 150, 100, 50),1) #1 pixel edge

    #draw filled and empty elipse
    pygame.draw.ellipse(window,BLACK, (250, 250, 80, 40), 0) #filled 
    pygame.draw.ellipse(window,BLACK,(400, 250, 80, 40), 2) #2 pixel edge

    #draw 6 sided polygon
    pygame.draw.polygon(window,BLACK, ((240, 350), (350, 350),
                                       (410, 410), (350, 470),
                                       (240, 470), (170, 410)))
                                    



    pygame.display.update()

