import pygame
import random
current_time=0
pygame.init()
win = pygame.display.set_mode((200, 200))

font = pygame.font.Font('text.txt', 15)

score_surface = font.render('SCORE-', False, (64, 64, 64))
score_rect = score_surface.get_rect(topleft=(0, 0))

ld_surface = font.render('CUBE DODGE', False, (0, 0, 0))
ld_rect = score_surface.get_rect(midtop=(70, 5))

best_surface = font.render('best', False, (0, 0, 0))
best_rect = score_surface.get_rect(midtop=(100, 30))

ld2_surface = font.render('PRESS SPACE', False, (0, 0, 0))
ld2_rect = score_surface.get_rect(midtop=(70, 160))
ld3_surface = font.render('TO PLAY', False, (0, 0, 0))
ld3_rect = score_surface.get_rect(midtop=(100, 180))

best = int(0)


def best_score(highest, best):
    if highest > best:
        best = highest
        best_surface = font.render(f'best:{best}', False, (0, 0, 0))
        best_rect = score_surface.get_rect(midtop=(100, 30))
        win.blit(best_surface, best_rect)
    else:
        best_surface = font.render(f'best:{best}', False, (0, 0, 0))
        best_rect = score_surface.get_rect(midtop=(100, 30))
        win.blit(best_surface, best_rect)

    return best


def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'SCORE:{current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(topleft=(0, 0))
    win.blit(score_surface, score_rect)

    return current_time


start_time = 0
current_time = 0

logo = pygame.image.load('logo.jpg')
from sys import exit

clock = pygame.time.Clock()
x = 90
y = 90

en_x = -20
en_y = random.randint(0, 180)

en2_x = random.randint(0, 180)
en2_y = -20

en3_y = random.randint(0, 180)
en3_x = 200

en4_y = 200
en4_x = random.randint(0, 180)

game_active = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    win.fill(('white'))

    if game_active == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            en_x = -20
            en_y = random.randint(0, 180)

            en2_x = random.randint(0, 180)
            en2_y = -20

            en3_y = random.randint(0, 180)
            en3_x = 200

            player = pygame.draw.rect(win, 'blue', (x, y, 20, 20))

            en4_y = 200
            en4_x = random.randint(0, 180)
            game_active = True
            start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:

        win.fill(('white'))
        player = pygame.draw.rect(win, 'blue', (x, y, 20, 20))

        display_score()
        highest = display_score()

        enemy1 = pygame.draw.rect(win, 'red', (en_x, en_y, 20, 20))
        enemy2 = pygame.draw.rect(win, 'red', (en2_x, en2_y, 20, 20))
        enemy3 = pygame.draw.rect(win, 'red', (en3_x, en3_y, 20, 20))
        enemy4 = pygame.draw.rect(win, 'red', (en4_x, en4_y, 20, 20))

        en_x += 1.3
        en2_y += 1.3
        en3_x -= 1.3
        en4_y -= 1.3

        if en_x >= 200:
            en_y = random.randint(0, 180)
            en_x = -20

        if en2_y >= 200:
            en2_x = random.randint(0, 180)
            en2_y = -20

        if en3_x <= -20:
            en3_y = random.randint(0, 180)
            en3_x = 200

        if en4_y <= -20:
            en4_y = 200
            en4_x = random.randint(0, 180)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if x > 180:
                x = 180
            elif x < 0:
                x = 0
            else:
                x += 2

        if keys[pygame.K_LEFT]:
            if x > 200:
                x = 200
            elif x < 0:
                x = 0
            else:
                x -= 2

        if keys[pygame.K_UP]:
            if y > 200:
                y = 200
            elif y < 0:
                y = 0
            else:
                y -= 2

        if keys[pygame.K_DOWN]:
            if y > 180:
                y = 180
            elif y < 0:
                y = 0
            else:
                y += 2

        if keys[pygame.K_r]:
            print('press')
            current_time+=20

        if player.colliderect(enemy1) or player.colliderect(enemy2) or player.colliderect(enemy3) or player.colliderect(
                enemy4):
            x = 90
            y = 90
            player = pygame.draw.rect(win, 'blue', (x, y, 20, 20))
            game_active = False

    else:
        player = pygame.draw.rect(win, 'blue', (x, y, 20, 20))
        win.fill(('pink'))

        win.blit(ld_surface, ld_rect)
        win.blit(ld2_surface, ld2_rect)
        win.blit(ld3_surface, ld3_rect)
        best = best_score(highest, best)
        best_score(highest, best)
    clock.tick(60)
    pygame.display.update()