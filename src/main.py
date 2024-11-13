from setting import *
from player import Player

class Game:
    def __init__(self):   
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Shooter Shooter')
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player((500, 300), self.all_sprites)

    def run(self):
        while running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.all_sprites.update(dt)
        
            self.display_surface.fill('seagreen1')
            self.all_sprites.draw(self.display_surface)
            # display_surface.blit((width(Increase = right), height(increase = down)))
            # self.display_surface.blit(player.surf, (x, 550))
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()