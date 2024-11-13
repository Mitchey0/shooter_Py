from main import *

# Note: Just to be easier on me, unless I can find a way
# to use the created surface, I can create quick sprites
# and move forward for play testing!

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