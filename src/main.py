import pygame
import os

window_width, window_height = 720, 720

pygame.init()

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