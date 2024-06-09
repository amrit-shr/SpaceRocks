import pygame
# import random
import time 
# import sys
from utils import load_background_image
# from models import GameObject
from models import Spaceship, Rock

class spaceRocks:
    def __init__(self):
        #initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption("SpaceRocks")
        self.__screen = pygame.display.set_mode((1333, 750))
        self.__background=load_background_image("space", True)

        self.bullets = []

        self.ship = Spaceship((777, 375), self.bullets)

        self.rocks = [Rock(self.__screen, self.ship.position) for _ in range(6)]

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
        for obj in self.game_objects:
            obj.draw(self.__screen)

    def _input_handle(self):
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ship.shoot(self.__screen)

        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_ESCAPE] or is_key_pressed[pygame.K_q]:
            quit()   
        elif is_key_pressed[pygame.K_RIGHT]:
            self.ship.rotate(clockwise = True)
            # self.ship.shoot(self.__screen, True)

        elif is_key_pressed[pygame.K_LEFT]:
            self.ship.rotate(clockwise = False)
            # self.ship.shoot(self.__screen, False)

        elif is_key_pressed[pygame.K_UP]:
            self.ship.acceleration() #magic happens here 
                                                        
                                                    
        elif is_key_pressed[pygame.K_DOWN]:
            self.ship.deceleration()

        elif is_key_pressed[pygame.K_SPACE]:
            self.ship.velocity = (0, 0)

    @property    
    def game_objects(self):
        return [*self.rocks, *self.bullets, self.ship]

    def _game_logic(self):
        for obj in self.game_objects:
            obj.move(self.__screen)
        
        rect = self.__screen.get_rect()
        for bullet in self.bullets[:]:
            if not rect.collidepoint(bullet.position):
                self.bullets.remove(bullet)

        #rocks and bullets collision
        for bullet in self.bullets[:]:
            for rock in self.rocks[:]:
                if rock.colides_with(bullet):
                    self.rocks.remove(rock)
                    self.bullets.remove(bullet)
                    break
        
        #rocks and ship collision
        if self.ship:
            for rock in self.rocks[:]:
                if rock.colides_with(self.ship):
                    self.ship = None
                    time.sleep(0.5)
                    # quit()
                    break

        # self.ship.move() 

    
    def _display(self):
        pygame.display.flip()
        # time.sleep(0.3)
        for obj in self.game_objects:
            obj.draw(self.__screen)

        self.clock.tick(self.fps)

        


# sys.exit()

# here=spaceRocks()
