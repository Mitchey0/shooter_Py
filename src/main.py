import pygame

window_width, window_height = 1280, 720
pygame.init()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooter Shooter')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ARTSSS
    display_surface.fill('seagreen1')
    pygame.display.update()
pygame.quit()