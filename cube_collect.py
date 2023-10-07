import pygame, random,time,threading
pygame.init()
win_x=500
win_y=500
win = pygame.display.set_mode((win_x, win_y))
clock = pygame.time.Clock()
x=250
y=250
highscore=0
spot_x=random.randint(0,480)
spot_y=random.randint(35,480)

font = pygame.font.Font('text.txt', 15)
font2 = pygame.font.Font('text.txt', 20)
score_surface = font.render('SCORE:0', False, (64, 64, 64))
score_rect = score_surface.get_rect(topleft=(10, 10))

highscore_surface = font2.render(f'HIGH SCORE:{highscore}', False, (64, 64, 64))
highscore_rect = highscore_surface.get_rect(center=(250,250))
points=0
time_left=15
start_time=int(pygame.time.get_ticks()/1000)
current_time=0
game=True

def countdown():
    global game,time_left
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    timer_surface = font.render(f'TIME:{time_left-current_time}', False, (64, 64, 64))
    timer_rect = score_surface.get_rect(topleft=(400, 10))
    win.blit(timer_surface, timer_rect)

    if time_left-current_time<1:
        print('yh')
        game=False




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    win.fill('white')
    if game==True:


        win.fill(('#AEBCFF'))

        win.blit(score_surface, score_rect)

        countdown()

        spot = pygame.draw.rect(win, 'red', (spot_x, spot_y, 20, 20))
        player = pygame.draw.rect(win, 'black', (x, y, 30, 30))

        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if x > (win_x-30):
                x = (win_x-30)
            elif x < 0:
                x = 0
            else:
                x += 7

        if keys[pygame.K_LEFT]:
            if x > win_x:
                x = win_x
            elif x < 0:
                x = 0
            else:
                x -= 7

        if keys[pygame.K_UP]:
            if y > win_x:
                y = win_x
            elif y < 35:
                y = 35
            else:
                y -= 7

        if keys[pygame.K_DOWN]:
            if y > win_x-30:
                y = win_x-30
            elif y < 0:
                y = 0
            else:
                y += 7

        if player.colliderect(spot):
            spot_x = random.randint(0, win_x-20)
            spot_y = random.randint(35, win_y-20)
            points+=1
            spot = pygame.draw.rect(win, 'red', (spot_x, spot_y, 20, 20))
            score_surface = font.render(f'SCORE:{points}', False, (64, 64, 64))


    if game==False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            x = 250
            y = 250
            points=0
            score_surface = font.render(f'SCORE:{points}', False, (64, 64, 64))
            start_time = int(pygame.time.get_ticks() / 1000)
            time_left=15
            game=True


        if points>highscore:
            highscore=points
        win.fill(('#AEBCFF'))
        title_surface = font2.render(f'CUBE COLLECTOR', False, (64, 64, 64))
        title_rect = title_surface.get_rect(center=(250, 140))
        des_surface = font.render(f'USE ARROWS TO COLLECT CUBES', False, (64, 64, 64))
        des_rect = des_surface.get_rect(center=(250, 155))


        pscore_surface = font2.render(f'YOUR SCORE:{points}', False, (64, 64, 64))
        pscore_rect = pscore_surface.get_rect(center=(250, 220))

        highscore_surface = font2.render(f'HIGH SCORE:{highscore}', False, (64, 64, 64))
        msg_surface = font.render(f'---press SPACE to start---', False, (64, 64, 64))
        msg_rect=msg_surface.get_rect(center=(250,275))
        win.blit(highscore_surface,highscore_rect)
        win.blit(msg_surface, msg_rect)
        win.blit(pscore_surface, pscore_rect)
        win.blit(title_surface, title_rect)
        win.blit(des_surface, des_rect)

    clock.tick(60)
    pygame.display.update()




