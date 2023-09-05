import pygame
from sys import exit
from pygame import mixer
from random import randint


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = pygame.font.Font('Pixeltype.ttf', 50)
    score = current_time // 100
    score_surf = score_surf.render(f"{score}", False, "white")
    score_rect = score_surf.get_rect(topleft=(65, 20))
    screen.blit(score_surf, score_rect)
    return score


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 10

            if obstacle_rect.bottom == 350:
                screen.blit(enemy_ice_surface, obstacle_rect)
            elif obstacle_rect.bottom == 335:
                screen.blit(enemy_ork_surface, obstacle_rect)
            else:
                screen.blit(enemy_oko_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect): return False
    return True

game_is_on = False
pygame.init()
# Rozmiar ekranu
screen = pygame.display.set_mode((800, 400))
# Tło
bg = pygame.image.load('background.png').convert()
score_icon = pygame.image.load('score_icon.png').convert()
life_icon = pygame.image.load('life_icon.jpg').convert()
# Podłoga
ground_surface = pygame.image.load('floor.png').convert()
ground_rect = ground_surface.get_rect(topleft=(0, 375))
# Czcionka
# score_display = pygame.font.Font('Pixeltype.ttf', 50)
# score_display = score_display.render('Score:', False, 'White')
# score_rect = score_display.get_rect(topleft=(65, 20))

life_display = pygame.font.Font('Pixeltype.ttf', 50)
life_display = life_display.render(" Life: 1 ", False, 'black')
life_rect = life_display.get_rect(topleft=(620, 20))
# Nazwa
pygame.display.set_caption('Matin2')
# Ikonka
programIcon = pygame.image.load('matinzdj.png').convert()
pygame.display.set_icon(programIcon)
# Zegar
clock = pygame.time.Clock()
# Muzyka
mixer.init()
mixer.music.load('bg_music.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()
# Wrogowie
# 49x88
enemy_ice_surface = pygame.image.load("Podziemny_Kawał_Lodu.png").convert_alpha()
enemy_ork_surface = pygame.image.load("monster.png").convert_alpha()
enemy_oko_surface = pygame.image.load("Pustynne_Lataj._Oko.png").convert_alpha()
# obstacles
obstacle_rect_list = []
# Gracz 177x160
player_surface = pygame.image.load('woj.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 375))
player_gravity = 0

# intro screen
player_stand = pygame.image.load("player_stand.jpg").convert()
player_stand = pygame.transform.rotozoom(player_stand, 0, 0.7)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = pygame.font.Font('Pixeltype.ttf', 70)
game_name = game_name.render("Matin2", False, "white")
game_name_rect = game_name.get_rect(center=(400, 35))

game_mess = pygame.font.Font('Pixeltype.ttf', 50)
game_mess = game_mess.render("Press 'space' to run!", False, 'white')
game_mess_rect = game_mess.get_rect(center=(400, 370))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1100)

pkt = 0
# Wszystkie klawisze
keys = pygame.key.get_pressed()

start_time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_is_on:
            # skok
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and player_rect.bottom == 375:
                    player_gravity = -20
            # w prawo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_rect.right += 20
            # w lewo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_rect.left -= 20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_is_on = True
                player_rect.left = 0
                mixer.music.play()
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_is_on:
            random_number = randint(0, 3)
            if random_number == 0:
                obstacle_rect_list.append(enemy_ice_surface.get_rect(bottomright=(randint(900, 1100), 350)))
            elif random_number == 1:
                obstacle_rect_list.append(enemy_oko_surface.get_rect(bottomright=(randint(900, 1100), 340)))
            else:
                obstacle_rect_list.append(enemy_ork_surface.get_rect(bottomright=(randint(900, 1100), 335)))

    if game_is_on:
        # ziemia i tło
        screen.blit(bg, (0, 0))
        screen.blit(ground_surface, ground_rect)
        # wyświetlanie interfejsu
        pygame.draw.rect(screen, 'white', life_rect)
        screen.blit(life_display, life_rect)
        screen.blit(life_icon, (750, 10))
        # pygame.draw.rect(screen, 'black', score_rect)
        # screen.blit(score_display, score_rect)
        screen.blit(score_icon, (10, 0))
        pkt = display_score()

        # gracz - przechodzenie między stronami ekranu
        if player_rect.right <= 0:
            player_rect.left = 800
        elif player_rect.left >= 800:
            player_rect.right = 0

        # gracz - mechanizm spadania za pomocą grawitacji
        player_rect.y += player_gravity
        player_gravity += 1
        if player_rect.bottom >= 375:
            player_rect.bottom = 375

        # gracz - wyświetlanie
        screen.blit(player_surface, player_rect)
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_is_on = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill("orange")
        screen.blit(player_stand, player_stand_rect)
        score_message = pygame.font.Font('Pixeltype.ttf', 50)
        score_message = score_message.render(f"Your score: {pkt}", False, 'white')
        score_message_rect = score_message.get_rect(center=(400, 370))
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list = []

        player_gravity = 0

        if pkt == 0:
            screen.blit(game_mess, game_mess_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
