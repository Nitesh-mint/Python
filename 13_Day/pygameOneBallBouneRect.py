import pygame
from pygame.locals import *
import sys
import random

#define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 60
N_PIXELS_PER_SECOND = 3

#initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load assets
javaImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/13_Day/java.png')

#initialize varaibles 
javaRect = javaImage.get_rect() #creating rect variable
MAX_WIDTH = WINDOW_WIDTH - javaRect.width
MAX_HEIGHT = WINDOW_HEIGHT -  javaRect.height
javaRect.left = random.randrange(MAX_WIDTH)
javaRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_SECOND
ySpeed = N_PIXELS_PER_SECOND

#loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if(javaRect.left < 0) or (javaRect.right >= WINDOW_WIDTH):
             xSpeed = -xSpeed
        
        if(javaRect.top < 0) or (javaRect.bottom >= WINDOW_HEIGHT):
            ySpeed = -ySpeed
        
        #update the ball's rectangle
        javaRect.left = javaRect.left + xSpeed
        javaRect.top = javaRect.top + ySpeed

        #setting background
        window.fill(WHITE)

        #draw the image
        window.blit(javaImage,javaRect)

        #update
        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)