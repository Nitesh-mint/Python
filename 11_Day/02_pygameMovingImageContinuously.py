import pygame
from pygame.locals import *
import sys
import random

#define constants
WHITE = (255,255,255)
WIDNOW_HEIGHT = 500
WINDOW_WIDTH = 400
JAVA_WIDTH_HEIGHT = 100
MAX_HEIGHT = WIDNOW_HEIGHT - JAVA_WIDTH_HEIGHT
MAX_WIDTH = WINDOW_WIDTH - JAVA_WIDTH_HEIGHT
TARGET_X = 10 #the x-ordinate of the targetImage below
TARGET_Y = 20 #Y-ordinate of the targetImage below
TARGET_WIDTH=100
TARGET_HEIGHT = 100
N_PIXELS_TO_MOVE = 5
FRAMES_PER_SECOND = 60

#initialize the world
pygame.init()
window = pygame.display.set_mode((WIDNOW_HEIGHT,WINDOW_WIDTH))
clock = pygame.time.Clock()

#load assets
javaImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/11_Day/ball.png')
targetImage = pygame.image.load("/home/nitesh/Desktop/OOP_in_python/11_Day/target.jpg")

#initialze variables
javaX = random.randrange(MAX_WIDTH)
javaY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH,TARGET_HEIGHT)

#LOop
while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        keyPressedTuple = pygame.key.get_pressed()

        if keyPressedTuple[pygame.K_LEFT]:
            javaX = javaX - N_PIXELS_TO_MOVE
        if keyPressedTuple[pygame.K_RIGHT]:
            javaX = javaX + N_PIXELS_TO_MOVE
        if keyPressedTuple[pygame.K_UP]:
            javaY = javaY - N_PIXELS_TO_MOVE
        if keyPressedTuple[pygame.K_DOWN]:
            javaY = javaY + N_PIXELS_TO_MOVE
        
        #check if the java touches the target?
        javaRect = pygame.Rect(javaX,javaY,JAVA_WIDTH_HEIGHT,JAVA_WIDTH_HEIGHT)

        if javaRect.colliderect(targetRect): #checks the if the java touches it.
            print("Java is touching the target.")

        window.fill(WHITE)

        #draw the java and target
        window.blit(javaImage,(javaX,javaY))
        window.blit(targetImage,(TARGET_X,TARGET_Y))

        #UPDATE THE WINDOW
        pygame.display.update()

        #frames
        clock.tick(FRAMES_PER_SECOND)
