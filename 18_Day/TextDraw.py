import pygame
from pygame.locals import *
import sys
from simpleText import *

#defining constants
Black  = (255,255,255)
WHITE = (0,0,0)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
frames = 30

#initialze
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(Black)
    oText1 = SimpleText(window,(150,50),"Nitesh",(WHITE))
    oText1.draw()
    oText2 = SimpleText(window,(150, 90), "Raya", (WHITE))
    oText2.draw()
    pygame.display.update()
    clock.tick(frames)
