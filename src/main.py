import pygame

window_width, window_height = 1280, 720
pygame.init()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooter Shooter')
running = True

# Surface
surf = pygame.surface((100, 200))
surf.fill('orange')
x = 100

#Imported images
# player_surf = pygame.image.load(join('images', 'filename.png')).convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ARTSSS
    display_surface.fill('seagreen1')
    # display_surface.blit((width(Increase = right), height(increase = down)))
    # x += 0.1
    display_surface.blit(surf, (x, 150))
    pygame.display.update()
pygame.quit()