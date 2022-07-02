import pygame

pygame.init

VolumeM_do_game = 0
pygame.mixer.init()
musica_de_fundo = pygame.mixer.music.load('sounds/musicadefundo.mp3')
pygame.mixer.music.set_volume(VolumeM_do_game)
pygame.mixer.music.play(-5)