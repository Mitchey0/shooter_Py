from main import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill('orange')
        self.rect = self.surf.get_rect()

    def user_input():
        pass

    def move():
        pass

    def update():
        pass