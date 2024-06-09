# spaceRocks/models.py
# from main import spaceRocks ##circular import
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_background_image, Wrap_position
import random


DIRECTION_UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity, wraps=True):
        self.position=Vector2(position)
        self.sprite=sprite
        self.radius=sprite.get_width()/2
        self.velocity=Vector2(velocity)
        self.wraps = wraps

    def draw(self, surface):
        position=self.position-Vector2(self.radius)
        surface.blit(self.sprite, position)

    def move(self, surface):
            move_to = self.position + self.velocity
            if self.wraps:
                self.position = Wrap_position(move_to, surface)
            else:
                self.position = move_to

    def colides_with(self, other): #two instances
        distance=self.position.distance_to(other.position)
        return distance < self.radius + other.radius
      

class Spaceship(GameObject):
    ROTATION_SPEED = 5
    ACCELERATION = 0.25
    Bullet_Speed = 10
    bullet_position = Vector2()
    def __init__(self, position, bullet_container):
        self.direction = Vector2(DIRECTION_UP)
        self.bullet_container = bullet_container
        super().__init__(position, load_background_image("spaceship"), Vector2(0), True)

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
        self.bullet_position = blit_position #unnessary
        surface.blit(rotated_surface, blit_position)

    def shoot(self, surface):
        velocity = self.direction * self.Bullet_Speed + self.velocity
        bullet = Bullet(self.position, velocity)
        # bullet.rotate(self.clockwise)
        # bullet.draw(self.surface)
        self.bullet_container.append(bullet)
        print(f"# bullets: {len(self.bullet_container)}") #count bullet

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
        super().__init__(position, load_background_image("asteroid"), velocity, True)

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_background_image("bullet"), velocity, False)

