import pygame
from pygame import mixer


def make_screen():
        screen = pygame.display.set_mode((800, 400))
        # Tło
        bg = pygame.image.load('background.png').convert()
        score_icon = pygame.image.load('score_icon.png').convert()
        life_icon = pygame.image.load('life_icon.jpg').convert()
        # Podłoga
        ground_surface = pygame.image.load('floor.png').convert()
        # Czcionka
        score_display = pygame.font.Font('Pixeltype.ttf', 50)
        score_display = score_display.render('Score:', False, 'White')
        score_rect = score_display.get_rect(topleft=(65, 20))

        life_display = pygame.font.Font('Pixeltype.ttf', 50)
        life_display = life_display.render(" Life: ", False, 'black')
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