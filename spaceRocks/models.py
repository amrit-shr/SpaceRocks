# spaceRocks/models.py

from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_background_image, Wrap_position
import random


DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position=Vector2(position)
        self.sprite=sprite
        self.radius=sprite.get_width()/2
        self.velocity=Vector2(velocity)

    def draw(self, surface):
        position=self.position-Vector2(self.radius)
        surface.blit(self.sprite, position)

    def move(self, surface):
            move_to = self.position + self.velocity
            self.position = Wrap_position(move_to, surface)

        # self.position += Vector2(self.velocity) 
        
        # if self.position.x > 1350 + self.radius:
        #     self.position.x = -self.radius
        # elif self.position.x < -self.radius:
        #     self.position.x = 1350 + self.radius

        # if self.position.y > 750 + self.radius:
        #     self.position.y = -self.radius
        # elif self.position.y < -self.radius:
        #     self.position.y = 750 + self.radius


class Spaceship(GameObject):
    ROTATION_SPEED = 10
    ACCELERATION = 0.25
    def __init__(self, position):
        self.direction = Vector2(DIRECTION_UP)
        super().__init__(position, load_background_image("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.ROTATION_SPEED * sign
        self.direction.rotate_ip(angle)

    def acceleration(self):
        self.velocity += Vector2(self.direction) * self.ACCELERATION 

    def deceleration(self):
        self.velocity -= Vector2(self.direction) * self.ACCELERATION
    
    def draw(self, surface):
        angle = self.direction.angle_to(DIRECTION_UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        # print(angle)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        # print(rotated_surface)
        blit_position = self.position - rotated_surface_size * 0.5
        # print(f"blit {blit_position}")
        surface.blit(rotated_surface, blit_position)

class Rock(GameObject):
    Min_Start_Gap = 222
    MinSpeed = 1
    MaxSpeed =4
    def __init__(self, surface, ship_position):
        while True:
            position = Vector2(
                random.randrange(surface.get_width()),
                random.randrange(surface.get_height())
            )
            if position.distance_to(ship_position) > self.Min_Start_Gap:
                break
        
        #Random velocity
        speed = random.randint(self.MinSpeed, self.MaxSpeed)
        angle = random.randint(0, 360)
        velocity = Vector2(speed, 0).rotate(angle)
        super().__init__(position, load_background_image("asteroid"), velocity)