import pygame
from SimpleButtonClass import *
import sys

#initialize constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
frames = 30

#create a world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Clock = pygame.time.Clock()
Obutton1 = simpleButton(window, (150,50),
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg",
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")
Obutton2 = simpleButton(window, (150,120),
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg",
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")
Obutton3 = simpleButton(window, (150,200),
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/clicked.jpg",
                                "/home/nitesh/Desktop/OOP_in_python/16_Day/Noclicked.jpg")

#loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if Obutton1.handleEvent(event):
            print("The Button 1 is clicked.")

        if Obutton2.handleEvent(event):
            print("The Button 2 is clicked.")

        if Obutton3.handleEvent(event):
            print("The Button 3 is clicked.")

    window.fill("White")
    #calling all the objects one by one
    Obutton1.draw()
    Obutton2.draw()
    Obutton3.draw()
    
    #calling the handleEvent method
    pygame.display.update()
    Clock.tick(frames)
    