import pygame
from pygame.locals import *
import sys
from java import *

#define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECONDS =60

#initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#initialize variables
oJava = Java(window,WINDOW_WIDTH,WINDOW_HEIGHT)

#loop forever
while True:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            pygame.quit()
            sys.exit()

    oJava.update() #tell the java to update itself
    window.fill(WHITE)
    oJava.draw() #calling the draw function
    pygame.display.update()
    clock.tick(FRAMES_PER_SECONDS)