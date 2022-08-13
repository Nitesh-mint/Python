import pygame
from pygame.locals import *
import sys

import random

#define constants
WHITE =(255,255,255)
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 400
FRAMES_PER_SECOND = 60
BALL_WIDTH_HEIGHT = 80
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT- BALL_WIDTH_HEIGHT

#initialze the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load image
ballImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/10_Day/ball.png')

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
    if event.type == pygame.MOUSEMOTION:
        # mouseX, mouseY = event.pos # Could do this if we needed it
        # Check if the click was in the rect of the ball
        # If so, choose a random new location
        if ballRect.collidepoint(event.pos):
            ballX = random.randrange(MAX_WIDTH)
            ballY = random.randrange(MAX_HEIGHT)
            ballRect = pygame.Rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

    window.fill(WHITE)
    window.blit(ballImage,(ballX,ballY)) #draw the ball

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)