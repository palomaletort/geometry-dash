import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Geometry Dash Clone")
clock = pygame.time.Clock()

player = pygame.Rect(100, 500, 50, 50)
velocity_y = 0
gravity = 0.5
jump_power = -10
on_ground = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power
        on_ground = False

    velocity_y += gravity
    player.y += int(velocity_y)

    if player.y >= 500:
        player.y = 500
        on_ground = True
        velocity_y = 0

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.display.flip()
    clock.tick(60)
