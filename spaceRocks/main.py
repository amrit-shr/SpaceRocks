import pygame
# import random
import time 
# import sys
from utils import load_background_image
# from models import GameObject
from models import Spaceship

class spaceRocks:
    def __init__(self):
        #initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption("SpaceRocks")
        self.__screen = pygame.display.set_mode((1333, 750))
        self.__background=load_background_image("space", True)

        self.ship = Spaceship((400, 400))

        self.pos=50
        self.fps=30
        self.speed=1
        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True: #this one is the most important
            self._input_handle()
            self._draw()
            self._game_logic()
            self._display()

    def _draw(self):
        self.__screen.blit(self.__background, (0,0))
        self.ship.draw(self.__screen)
        
    def _input_handle(self):
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()

        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_ESCAPE] or is_key_pressed[pygame.K_q]:
            quit()   
        elif is_key_pressed[pygame.K_d]:
            self.ship.rotate(clockwise = True)

        elif is_key_pressed[pygame.K_a]:
            self.ship.rotate(clockwise = False)
        

        elif is_key_pressed[pygame.K_UP] and is_key_pressed[pygame.K_LEFT]:
            self.ship.velocity = (-1, -1)

        elif is_key_pressed[pygame.K_RIGHT] and is_key_pressed[pygame.K_DOWN]:
            self.ship.velocity = (1, 1)

        elif is_key_pressed[pygame.K_RIGHT] and is_key_pressed[pygame.K_UP]:
            self.ship.velocity = (1, -1)

        elif is_key_pressed[pygame.K_LEFT] and is_key_pressed[pygame.K_DOWN]:
            self.ship.velocity = (-1, 1)

        else:
            if is_key_pressed[pygame.K_UP]:
                self.ship.velocity = (0, -1)

            if is_key_pressed[pygame.K_DOWN]:
                self.ship.velocity = (0, 1)

            if is_key_pressed[pygame.K_RIGHT]:
                self.ship.velocity = (1, 0)

            if is_key_pressed[pygame.K_LEFT]:
                self.ship.velocity = (-1, 0)

        


            
    def _game_logic(self):
        self.ship.move() #doesn't matter

    
    def _display(self):
        pygame.display.flip()
        # time.sleep(0.3)
        self.clock.tick(self.fps)

        


# sys.exit()

# here=spaceRocks()
