import pygame
import random

pygame.init()
window_width, window_height = 800, 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Shooter Shooter')

# Settings
player_size = 50
player_speed = 10
bullet_size = 5
bullet_speed = 15
enemy_size = 50
enemy_speed = 4

class Player():
    def __init__(self):
        self.rect = pygame.Rect(window_width // 2, window_height // 2, player_size, player_size)

    def move(self, dx, dy):
        self.rect.x += dx * player_speed
        self.rect.y += dx * player_speed
        Player.rect.clamp_ip(display_surface.get_rect()) # Code for keeping within screen was here

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, bullet_size, bullet_size)
    
    def move(self):
        self.rect.y -= bullet_size

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.radint(0, window_width - enemy_size, 0, enemy_size, enemy_size))

    def move(self):
        self.rect.y += enemy_speed #speed

def main():
    clock = pygame.time.Clock()
    player = Player()
    bullet = []
    enemies = []
    score = 0
    running = True

    while running:
        dt = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        player.move(dx, dy)

        display_surface.fill('seagreen1')
        # display_surface.blit((width(Increase = right), height(increase = down)))
        # self.display_surface.blit(player.surf, (x, 550))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()