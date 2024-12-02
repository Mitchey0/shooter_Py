import pygame
from pygame import mixer
import random

pygame.init()
window_width, window_height = 800, 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pizza Blaster')

# Settings
mixer.music.load("src/sound/backgroundmusic.mp3")
bg_image = pygame.image.load("src/images/spacebackground.png")
logo = pygame.image.load("src/images/pb_logo.png")
pygame.mixer.music.set_volume(0.3)
mixer.music.play(-1)

player_size = 50
player_speed = 6
bullet_size = 5
bullet_speed = 10
enemy_size = 50
enemy_speed = 4

#Create a class for button :D
#load images for buttons

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
            bullets.append(Bullet(player.rect.centerx, player.rect.top))
            bullet_sound = mixer.Sound('src/sound/pewpew.mp3')
            bullet_sound.play()
        
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        if random.randint(1, 30) == 1:
            enemies.append(Enemy())
        
        for enemy in enemies[:]:
            enemy.move()
            if enemy.rect.top > window_height:
                enemies.remove(enemy)
                score += -3 # Increment sc ore for each enemy that goes off screend 

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    direct_hit = mixer.Sound('src/sound/retrohurt.mp3')
                    direct_hit.play()
                    direct_hit.set_volume(0.5)
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 5 # Increment score to destroy enemies

        display_surface.fill('midnightblue')
        display_surface.blit(bg_image, (0,0))
        pygame.draw.rect(display_surface, 'darkmagenta', player.rect)
        for bullet in bullets:
            pygame.draw.rect(display_surface, 'deeppink1', bullet.rect)
        for enemy in enemies:
            pygame.draw.rect(display_surface, 'mediumspringgreen', enemy.rect)
        
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, 'gray100')
        display_surface.blit(score_text, (10, 10))
        display_surface.blit(logo, (400, 15))
        pygame.display.update()
        clock.tick(30) 
    pygame.quit()

if __name__ == "__main__":
    main()