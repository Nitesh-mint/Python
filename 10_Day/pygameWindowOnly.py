#pygame demo window 

#import packages
import pygame
from pygame.locals import *
import sys

#2 define constants
BLACK  = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECONDS = 60

#3 initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock  = pygame.time.Clock()

#4 load assets: image(s), sounds etc.

#5 Initialize varaibles

#6 Loop forever

while True:
    #check for and handle events
    for event in pygame.event.get():
        #clicked the close button? close the winodow.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#clear the window
    window.fill(BLACK)

#update the window
    pygame.display.update()

#slow things down a bit
    clock.tick(FRAMES_PER_SECONDS)
