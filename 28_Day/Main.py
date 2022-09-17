import pygame
from MagicMethod_Rectange import *
import sys
from pygame.locals import *

#set up the constants
WHITE =(255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT= 450
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second '

#set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0,32)
clock = pygame.time.Clock()

rectanglesList = []
for i in range(0,N_RECTANGLES):
    oRectangle = Rectange(window)
    rectanglesList.append(oRectangle)
whichRectangle = FIRST_RECTANGLE

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectanglesList:
                if oRectangle.clickedInside(event.pos):
                    print("Clicked on",whichRectangle,"rectangles.")

                    if whichRectangle == FIRST_RECTANGLE:
                        oFirstRectangle = oRectangle
                        whichRectangle = SECOND_RECTANGLE   
                    
                    elif whichRectangle == SECOND_RECTANGLE:
                        oSecondRectangle2 = oRectangle
                        
                        #user has chosen  2 rectangles, let's compare
                        if oFirstRectangle == oSecondRectangle2:
                            print("The rectangles are of the same size.")

                        elif oFirstRectangle < oSecondRectangle2:
                            print("The second rectangle is Greater.")
                        else:
                            print("First rectangle is greater.")
                        whichRectangle = FIRST_RECTANGLE

        window.fill(WHITE)
        for oRectangle in rectanglesList:
            oRectangle.draw()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)


