import pygame
import random
import time 
import sys
from utils import load_background_image

class spaceRocks:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SpaceRocks")
        self.__screen=pygame.display.set_mode((1333, 750))
        self.__background=load_background_image("space", True)
        # self.__x=random.randint(10, 700)
        # self.__y=random.randint(10, 500) #for still
        # self.__r=random.randint(2, 50)

    def main_loop(self):
        
        while True:
            self._background()
            self._game_event()
            self._circle()
            self._displayCircle()

    def _background(self):
        self.__screen.fill((100, 100, 100))
        time.sleep(0.3)
        self.__screen.blit(self.__background, (0,0))

    def _game_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()

    def _circle(self):
        # self.__x=random.randint(10, 700)
        # self.__y=random.randint(10, 500) #For variable
        for _ in range(10):
            self.__x=random.randint(10, 1300) #position
            self.__y=random.randint(10, 700) #position
            self.__xr=random.randint(10, 1300) #position
            self.__yr=random.randint(10, 700) 
            self.__width=random.randint(2, 30) #width
            self.__height=random.randint(2, 30) #height
            self.__r=random.randint(2, 20)
            for _ in range(10):
                # self.__r=random.randint(2, 10) 
                pygame.draw.circle(self.__screen, (200, 200, 200), (self.__x, self.__y), self.__r)
                pygame.draw.rect(self.__screen, (200, 200, 200), (self.__xr, self.__yr, self.__width, self.__height),)
                                #background       #color            #position           #rectangle height, width

    def _displayCircle(self):
        pygame.display.flip()
        time.sleep(0.3)

    def _game_logic(self):
        pass

# sys.exit()

# here=spaceRocks()
