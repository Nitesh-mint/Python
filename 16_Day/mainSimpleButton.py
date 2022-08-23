import pygame
from pygame.locals import *
import sys
from SimpleButtonClass import *

#initialze constants
BLACK =(0,0,0)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

#INITLIALZE THE WORLD
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock  = pygame.time.Clock()

#initialze variables
#create instance of simmpleButton
oButton = simpleButton(window,(150,30),
                        "/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg",
                        "/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")


#loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #pass the button to event and see if the user has clicked it or not .
        if oButton.handleEvent(event):
            print("User has clicked the button")
    
    window.fill(BLACK)

    oButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)