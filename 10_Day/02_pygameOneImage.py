import pygame
from pygame.locals import *
import sys

#define constants
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FRAMES_PER_SECOND = 30


#INITIALIZE THE WORLD
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load asset
dogImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/Day10/dog.jpg')

#draw the window element
#draw ball at position 100 across (x) and 200 downn (y)
while True:
        #check for and handle events
    for event in pygame.event.get():
        #clicked the close button? close the winodow.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(dogImage,(0,0))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)