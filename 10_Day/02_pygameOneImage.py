import pygame
from pygame.locals import *
import sys

#define constants\
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
FRAMES_PER_SECOND = 30


#INITIALIZE THE WORLD
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load asset
ballImage = pygame.image.load("/home/nitesh/Desktop/OOP_in_python/10_Day/ball.png")

#draw the window element
#draw ball at position 100 across (x) and 200 downn (y)
while True:
        #check for and handle events
    for event in pygame.event.get():
        #clicked the close button? close the winodow.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(ballImage,(170,150))

    pygame.display.update()

    window.fill(WHITE)

    clock.tick(FRAMES_PER_SECOND)