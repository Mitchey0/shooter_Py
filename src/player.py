from setting import *

# Note: Just to be easier on me, unless I can find a way
# to use the created surface, I can create quick sprites
# and move forward for play testing!

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('src', 'images', 'player_backward.png')).convert_alpha
        self.rect = self.image.get__frect(center = pos)

        self.direction = pygame.Vector2()
        self.speed = 500

    def user_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self):
        self.user_input()
        self.move()