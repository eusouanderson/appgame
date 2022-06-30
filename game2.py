
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
final = True
objects =[]
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.power = []
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
        self.animar = False
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect(center=(400,300))
    def poder(self):
        self.sprites.append(pygame.image.load('navei/redfighternormal0001.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0002.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0003.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0004.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0005.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0006.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0007.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0008.png'))    
        self.sprites.append(pygame.image.load('navei/redfighternormal0009.png'))  
        self.image = self.power[self.animar]
        self.rect = self.image.get_rect(center=(400,300))  
    def update(self):
        
        self.animar = self.animar + 0.15
        self.animar = True
        if self.animar >= len(self.power):
            self.animar = 0
        self.image = self.sprites[int(self.animar)]
        
        self.atual = self.atual + 0.15
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(tamanho_nave)) 
        self.rect = self.image.get_rect( center =(x,y))
x = 30
y = 30
x = x+ 300
y = y+ 300
  
        
   

       
group_nave = pygame.sprite.Group()
group_nave.add(Nave())


while final:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()

    userInput = pygame.key.get_pressed()
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
    if  userInput[pygame.K_SPACE]:
            tamanho_nave = 500,500
    if  userInput[pygame.K_c]:
            tamanho_nave = 100, 100
                 
   
    movetela= 30
     
    
    tela.blit(img,(0,0))
    rel_y = movetela % img.get_rect().height
    tela.blit(img,(rel_y - img.get_rect().height,1 ))
    if rel_y < 500 :
        tela.blit(img,(rel_y, 1))
    movetela -=  1
    
    group_nave.draw(tela)
    
    
  

    group_nave.update()
    pygame.display.flip()

