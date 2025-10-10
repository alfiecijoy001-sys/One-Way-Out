import pygame
import sys
from settings import *
from level import Level

#blocks=name of file
#Block=class
#block=actual tile
#Setup
pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((screen_width,screen_height))

level=Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.exit()
            sys.exit()
            
    screen.fill('black')
    level.run()
    clock.tick(60)
    

    pygame.display.update()
    