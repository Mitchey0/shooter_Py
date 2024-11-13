from setting import *

# Note: Just to be easier on me, unless I can find a way
# to use the created surface, I can create quick sprites
# and move forward for play testing!

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player_backward.png')).convert_alpha
        self.rect = self.image.get_frect(center = pos)

    def user_input():
        pass

    def move():
        pass

    def update():
        pass