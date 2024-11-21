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
        self.rect.y += dy * player_speed
        self.rect.clamp_ip(display_surface.get_rect()) # Code for keeping within screen was here

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, bullet_size, bullet_size)
    
    def move(self):
        self.rect.y -= bullet_speed

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, window_width - enemy_size), 0, enemy_size, enemy_size)

    def move(self):
        self.rect.y += enemy_speed

def main():
    clock = pygame.time.Clock()
    player = Player()
    bullets = []
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

        if keys[pygame.K_SPACE]:
            bullet.append(Bullet(player.rect.centerx, player.rect.top))
        
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullet.remove(bullet)

        if random.randint(1, 30) == 1:
            enemies.append(Enemy())
        
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.top > window_height:
                enemies.remove(enemy)
                score += 1 # Increment sc ore for each enemy that goes off screen

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 5 # Increment score to destroy enemies

        display_surface.fill('midnightblue')
        pygame.draw.rect(display_surface, 'darkorange', player.rect)
        for bullet in bullets:
            pygame.draw.rect(display_surface, 'mediumvioletred', bullet.rect)
        for enemy in enemies:
            pygame.draw.rect(display_surface, 'mediumspringgreen', enemy.rect)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, 'gray100')
        display_surface.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(30) 

    pygame.quit()

if __name__ == "__main__":
    main()