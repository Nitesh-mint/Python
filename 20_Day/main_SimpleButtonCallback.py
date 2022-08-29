import pygame
from pygame.locals import *
from SimpleButtonClass import *
import sys

#define constants
WHITE = (255,255,255)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAMES = 30

#define a fucntion to be used as callback

def myCallBackFunction():
    print("User Pressed button B, called myCallBackFunction.")

#define a class to be used as callback

class callback():
    def myMethod(self):
        print("User Pressed button C, called calss method.")


#initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

oCallBackTest = callback()

#No callback
oButtonA = simpleButton(window,(100,20),"/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg","/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")

#specifing function to callback
oButtonB = simpleButton(window,(100,20),"/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg","/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg", callBack = myCallBackFunction)

#specifing method of the object to callback
oButtonC = simpleButton(window,(100,20),"/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg","/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg", callBack = oCallBackTest.myMethod)

counter = 0

#loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #pass the event to button and see if the button has been clicked.
        if oButtonA.handleEvent(event):
            print("User pressed button A, Handled in the main loop.") 
        
        #other both oButton has callbacks so no need to do it here.
        oButtonB.handleEvent(event)
        oButtonC.handleEvent(event)


        #do any frames per action 
        counter  = counter + 1

        window.fil(WHITE)

        #drew it to the GUI
        oButtonA.draw()
        oButtonB.draw()
        oButtonC.draw()

        pygame.display.update()

        clock.tick(FRAMES)