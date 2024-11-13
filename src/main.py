import pygame

window_width, window_height = 1280, 720
pygame.init()
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooter Shooter')
clock = pygame.time.Clock()
running = True

# Surface
x = 650
player.surf = Player()
#Imported images
# player_surf = pygame.image.load(join('images', 'filename.png')).convert_alpha()

while running:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ARTSSS
    display_surface.fill('seagreen1')
    # display_surface.blit((width(Increase = right), height(increase = down)))
    display_surface.blit(player.surf, (x, 550))
    pygame.display.update()
pygame.quit()