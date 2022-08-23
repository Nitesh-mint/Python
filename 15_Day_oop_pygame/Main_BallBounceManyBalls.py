import pygame
from pygame.locals import *
from java import *
import random
import sys

WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 60
N_JAVA = 3

#initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#initialze variables
javaList = []
for oJava in range(0,N_JAVA):
    #each time through the loop create a ball object
    oJava = Java(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    javaList.append(oJava) #append the new java to the list.

#loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for oJava in javaList:
        oJava.update() #tell each object to update itslef

    window.fill(WHITE)
    for oJava in javaList:
        oJava.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
