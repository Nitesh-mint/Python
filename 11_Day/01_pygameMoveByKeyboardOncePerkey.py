import pygame 
from pygame.locals import *
import sys
import random

#define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FRAMES_PER_SECOND= 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 20

#initialze the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load assets
ballImage = pygame.image.load("/home/nitesh/Desktop/OOP_in_python/11_Day/ball.jpg")
targetImage = pygame.image.load("/home/nitesh/Desktop/OOP_in_python/11_Day/target.jpg")

#initialize variables 
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #see if the user pressed the key or not
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE

# check if the ball is colliding with the user?
    ballRect = pygame.Rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)

    if ballRect.colliderect(targetRect):
        print("The ball is thouchng the target.")

    #clear the window
    window.fill(BLACK)

    #draw the window elements
    window.blit(targetImage,(TARGET_X,TARGET_Y)) #DRAW THE TARGET
    window.blit(ballImage,(ballX,ballY)) #draw the ball

    #update the window
    pygame.display.update()

    #slow things
    clock.tick(FRAMES_PER_SECOND)

