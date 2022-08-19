import pygame
from pygame.locals import *
import sys
import random

#define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
JAVA_WIDTH_HEIGHT = 90
FRAMES_PER_SECOND = 60
N_PIXEL_PER_FRAME = 2

#initialze world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#load assets
javaImage = pygame.image.load('/home/nitesh/Desktop/OOP_in_python/12_Day/java.png')
bounceSound = pygame.mixer.Sound("/home/nitesh/Desktop/OOP_in_python/14_Day/indon harp note 1.wav")
backgroundMusic = pygame.mixer.music.load("/home/nitesh/Desktop/OOP_in_python/14_Day/la-capricciosa-30-sec-110908.mp3")
pygame.mixer.music.play(-1,0.0)

#initialize varaiables

MAX_WIDTH = WINDOW_WIDTH - JAVA_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - JAVA_WIDTH_HEIGHT
javaX = random.randrange(MAX_WIDTH)
javaY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXEL_PER_FRAME
ySpeed = N_PIXEL_PER_FRAME

#loop forever
while True:
    #check for event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #do any frame action
    if (javaX < 0) or (javaX >= MAX_WIDTH):
        xSpeed = -xSpeed #reverse X direction\
        bounceSound.play()
    if (javaY < 0) or (javaY >= MAX_WIDTH):
        ySpeed = -ySpeed #reverse Y direction
        bounceSound.play()

    #update the ball's locatin using speed in two direction

    javaX = javaX + xSpeed
    javaY = javaY + ySpeed

    #fill window
    window.fill(WHITE)

    #draw the elements in window
    window.blit(javaImage,(javaX,javaY))

    #update the display
    pygame.display.update()

    #frames
    clock.tick(FRAMES_PER_SECOND)