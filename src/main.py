import pygame
import random

pygame.init()

window_width, window_height = 800, 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooter Shooter')
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('seagreen1')
    # display_surface.blit((width(Increase = right), height(increase = down)))
    # self.display_surface.blit(player.surf, (x, 550))
    pygame.display.update()

pygame.quit()

player_size = 50
player_speed = 10


class Player():
    def __init__(self):
        self.rect = pygame.Rect(window_width // 2, window_height // 2, player_size, player_size)

    def move(self, dx, dy):
        self.rect.x += dx * player_speed
        self.rect.y += dx * player_speed
        self.rect.clamp_ip(display_surface.get_rect())
