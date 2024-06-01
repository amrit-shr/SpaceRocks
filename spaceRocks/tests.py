import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Multiple Key Presses Example")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Rectangle settings
rect_size = 50
rect = pygame.Rect((400, 300, rect_size, rect_size))

# Movement settings
speed = 5

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the rectangle based on key presses
    if keys[K_UP] and keys[K_LEFT]:  # Move diagonally up-left
        rect.y -= speed
        rect.x -= speed
    elif keys[K_UP] and keys[K_RIGHT]:  # Move diagonally up-right
        rect.y -= speed
        rect.x += speed
    elif keys[K_DOWN] and keys[K_LEFT]:  # Move diagonally down-left
        rect.y += speed
        rect.x -= speed
    elif keys[K_DOWN] and keys[K_RIGHT]:  # Move diagonally down-right
        rect.y += speed
        rect.x += speed
    else:
        if keys[K_UP]:
            rect.y -= speed
        if keys[K_DOWN]:
            rect.y += speed
        if keys[K_LEFT]:
            rect.x -= speed
        if keys[K_RIGHT]:
            rect.x += speed

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()

pygame.quit()
