import pygame
from pygame.locals import *
import sys

import random

#define constants
BLACK =(0,0,0)
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT- BALL_WIDTH_HEIGHT

#initialze the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load image
dogImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/10_Day/dog.jpg')

# initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #see if user clicked
    if event.type == pygame.MOUSEBUTTONUP:
        # mouseX, mouseY = event.pos # Could do this if we needed it
        # Check if the click was in the rect of the ball
        # If so, choose a random new location
        if ballRect.collidepoint(event.pos):
            ballX = random.randrange(MAX_WIDTH)
            ballY = random.randrange(MAX_HEIGHT)
            ballRect = pygame.rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

    window.fill(BLACK)
    window.blit(dogImage,(ballX,ballY))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)