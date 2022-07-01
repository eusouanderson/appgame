
from ast import While
from asyncore import loop
from cmath import rect
from timeit import repeat
from tracemalloc import start, stop
from turtle import end_fill
import pygame
from pygame.locals import * 
from pygame.locals import QUIT
from random import randint
from pygame.sprite import Group, GroupSingle ,Sprite
import random

pygame.init

VolumeM_do_game = 0
pygame.mixer.init()
musica_de_fundo = pygame.mixer.music.load('sounds/musicadefundo.mp3')
pygame.mixer.music.set_volume(VolumeM_do_game)
pygame.mixer.music.play(-5)


largura ,altura = 700 , 500 
final = True
objects =[]
final = True
tamanho = largura , altura

tamanho_nave = 100, 100

tela = pygame.display.set_mode((tamanho))
pygame.display.set_caption ('War Naves')

img= pygame.image.load('img/back2.png')

class Tela(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.sprites = []
        self.sprites.append(pygame.image.load('img/back1.png'))          
        self.sprites.append(pygame.image.load('img/back2.png'))          
        self.sprites.append(pygame.image.load('img/back3.png'))          
        self.sprites.append(pygame.image.load('img/back4.png'))   
        self.image = self.sprites[+3]
        self.rect = self.image.get_rect(center=(230,80))       
    def update(self):
        ...


class Inimigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.inimigo1 = []
        self.inimigo2 = []
        self.inimigo3 = []
        self.inimigo4 = []
        self.inimigo5 = []
        self.inimigo6 = []
        self.inimigo1.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship1/Ship1.png'))
        self.inimigo2.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship2/Ship2.png'))
        self.inimigo3.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship3/Ship3.png'))
        self.inimigo4.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship4/Ship4.png'))
        self.inimigo5.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship5/Ship5.png'))
        self.inimigo6.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship6/Ship6.png'))
        self.image = self.inimigo1[0] 
        self.image = self.inimigo2[0]
        self.image = self.inimigo3[0]
        self.image = self.inimigo4[0]
        self.image = self.inimigo5[0]
        self.image = self.inimigo6[0]
        self.list = list(group_inimigos)
        self.rect = self.image.get_rect(center=(230,80))
        self.rect = self.image.get_rect(center=(250,60))
        
    def update(self):
        self.list.index
        if  self.rect.x :
            self.rect.x -= +1 
        if  self.rect.x == -0 :
            self.rect.x += 500
            self.rect.x = 30
           
    

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 

        self.image = pygame.image.load('img/lith1.png')
        self.rect = self.image.get_rect(center=(x,y))
        
        
    def update(self): 
       group_laser.draw(tela)
       if tecla_f:
        
        self.rect.y -= 1

        if self.rect.y >= tamanho[0]:
            self.kill()
         
        #self.rect = self.image.get_rect(center = (x,y))

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []       
        self.sprites.append(pygame.image.load('navei/redfighter0001.png'))          #1
        self.sprites.append(pygame.image.load('navei/redfighter0002.png'))          #2
        self.sprites.append(pygame.image.load('navei/redfighter0003.png'))          #3
        self.sprites.append(pygame.image.load('navei/redfighter0004.png'))          #4
        self.sprites.append(pygame.image.load('navei/redfighter0005.png'))          #5
        self.sprites.append(pygame.image.load('navei/redfighter0006.png'))          #6
        self.sprites.append(pygame.image.load('navei/redfighter0007.png'))          #7
        self.sprites.append(pygame.image.load('navei/redfighter0008.png'))          #8
        self.sprites.append(pygame.image.load('navei/redfighter0009.png'))          #9
        self.sprites.append(pygame.image.load('navei/redfighter0008.png'))          #10
        self.sprites.append(pygame.image.load('navei/redfighter0007.png'))          #11
        self.sprites.append(pygame.image.load('navei/redfighter0006.png'))          #12
        self.sprites.append(pygame.image.load('navei/redfighter0005.png'))          #13
        self.sprites.append(pygame.image.load('navei/redfighter0004.png'))          #14
        self.sprites.append(pygame.image.load('navei/redfighter0003.png'))          #15
        self.sprites.append(pygame.image.load('navei/redfighter0002.png'))          #16
        self.sprites.append(pygame.image.load('navei/redfighter0001.png'))          #17
        self.sprites.append(pygame.image.load('navei/redfighternormal0001.png'))    #18    
        self.sprites.append(pygame.image.load('navei/redfighternormal0002.png'))    #19  
        self.sprites.append(pygame.image.load('navei/redfighternormal0003.png'))    #20
        self.sprites.append(pygame.image.load('navei/redfighternormal0004.png'))    #21
        self.sprites.append(pygame.image.load('navei/redfighternormal0005.png'))    #22
        self.sprites.append(pygame.image.load('navei/redfighternormal0006.png'))    #23
        self.sprites.append(pygame.image.load('navei/redfighternormal0007.png'))    #24
        self.sprites.append(pygame.image.load('navei/redfighternormal0008.png'))    #25
        self.sprites.append(pygame.image.load('navei/redfighternormal0009.png'))    #26
        self.sprites.append(pygame.image.load('navei/redfighternormal0008.png'))    #27  
        self.sprites.append(pygame.image.load('navei/redfighternormal0007.png'))    #28
        self.sprites.append(pygame.image.load('navei/redfighternormal0006.png'))    #29
        self.sprites.append(pygame.image.load('navei/redfighternormal0005.png'))    #30
        self.sprites.append(pygame.image.load('navei/redfighternormal0004.png'))    #31
        self.sprites.append(pygame.image.load('navei/redfighternormal0003.png'))    #32
        self.sprites.append(pygame.image.load('navei/redfighternormal0002.png'))    #33
        self.sprites.append(pygame.image.load('navei/redfighternormal0001.png'))    #34
        self.atual = True
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(400,300))
    
    def update(self):
            self.atual = self.atual + 0.35
            if self.atual >= len(self.sprites):        
                    self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(tamanho_nave)) 
            self.rect = self.image.get_rect( center =(x,y))
           
x = 30
y = 30
x = x+ 300
y = y+ 300
      
group_inimigos = pygame.sprite.Group()
group_nave = pygame.sprite.Group()
group_laser = pygame.sprite.Group()
group_nave.add(Nave())
group_laser.add(Laser())
group_inimigos.add(Inimigos())
group_tela = pygame.sprite.Group()
group_tela.add(Tela())
 

while final:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()

    userInput = pygame.key.get_pressed()
    joy = pygame.joystick.get_count
    tamanho_nave = 100, 100
    
    if userInput[pygame.K_a]: 
            x = x - 4
            y = y + 0
    if userInput[pygame.K_d]: 
            x = x + 4
            y = y - 0
    if userInput[pygame.K_w]: 
            x = x + 0
            y = y - 4
                
    if userInput[pygame.K_s]: 
            x = x - 0
            y = y + 4
    if  userInput[pygame.K_f]:
        ...
    
    if userInput[pygame.K_SPACE]:
        tamanho_nave = 200 , 200
    
        ...



    tecla_f = userInput[pygame.K_f]
 
     
    
    movetela= 30
     
    
    tela.blit(tela,(0,0))
    rel_y = y % img.get_rect().height
    tela.blit(img,(rel_y - img.get_rect().height,10 ))
    if rel_y < 500 :
        tela.blit(img,(rel_y, 1))
    y-=  1

    group_tela.draw(tela)
    group_inimigos.draw(tela)
    group_nave.draw(tela)
    
    group_laser.update()
    group_inimigos.update()
    group_nave.update()
    pygame.display.flip()

