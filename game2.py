from email.mime import image
from re import X
from tkinter import CENTER
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite
from pygame.rect import Rect
import pygame
from pygame.locals import * 
from pygame.locals import QUIT
from sys import exit
from random import randint
from pygame.sprite import Group, GroupSingle
import random 



pygame.init

largura ,altura = 700 , 500 
tamanho_nave = 100, 100

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption ('War Naves')

img= pygame.image.load('img/back2.png')
x = 300
y = 300
final = True
toplef = x , y
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('navei/redfighter0001.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0002.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0003.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0004.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0005.png'))#center
        self.sprites.append(pygame.image.load('navei/redfighter0006.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0007.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0008.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0009.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0008.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0007.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0006.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0005.png'))#esq
        self.sprites.append(pygame.image.load('navei/redfighter0004.png'))#center
        self.sprites.append(pygame.image.load('navei/redfighter0003.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0002.png'))#dir
        self.sprites.append(pygame.image.load('navei/redfighter0001.png'))#dir
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y 
        #self.image = pygame.transform.scale(self.image,(128,128))
        

    def update(self):
        self.atual = self.atual + 0.15
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(tamanho_nave))
        

 


group_nave = pygame.sprite.Group()
group_nave.add(Nave())


while final:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()
           
        if event.type == KEYDOWN:
            
            if event.key == K_a:
                 x =+ 20
                 y = 0
                   
            if event.key == K_d:
                 x = -20
                 y = 0
            if event.key == K_w:
                 x = 0
                 y = 20
                  
            if event.key == K_s:
                 x = 0
                 y = -20
    
    
    tela.blit(img,(0,0))
    group_nave.draw(tela)

    group_nave.update()
    pygame.display.flip()

