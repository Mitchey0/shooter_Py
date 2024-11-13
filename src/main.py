import pygame

class Game:
    def __init__(self):   
        window_width, window_height = 1280, 720
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Shooter Shooter')
        clock = pygame.time.Clock()
        running = True

def run(self):
    while running:
        dt = self.clock.tick() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # ARTSSS
        self.display_surface.fill('seagreen1')
        # display_surface.blit((width(Increase = right), height(increase = down)))
        self.display_surface.blit(player.surf, (x, 550))
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()