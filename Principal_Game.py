
import pygame
from pygame.locals import * 
from pygame.locals import QUIT
from random import randint

import random

pygame.init()

VolumeM_do_game = 1
pygame.mixer.init()
pygame.mixer.music.load('sounds/Flies By The Fire.wav')
missil_sound = pygame.mixer.Sound('sounds/laserfire02.ogg')
missil_sound.set_volume(VolumeM_do_game)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

#Configuracoes 
# Tela
largura ,altura = 600 , 600 
x = largura
y = altura

rodando = True
objects =[]
tamanho = largura , altura
font = pygame.font.SysFont('font/ARCADE.TTF', 50)

# Nave 
veL_nave = 5
velocidade_do_missil = 10
vel_y_missil = 0
pos_x_missil = largura/2
pos_y_missil = altura/2 

pos_allien_x = 700
pos_allien_y = 360

pos_player_x = largura/2
pos_player_y = altura/2

pontos = 10
# Sound





# Config Nave
triggered = False

tamanho_nave = 100, 100

screen = pygame.display.set_mode((tamanho))
pygame.display.set_caption ('War Naves')

img= pygame.image.load('img/back2.png')

missil = pygame.image.load('img/lith1.png')
missil = pygame.transform.scale(missil,(50,50))
missil = pygame.transform.rotate(missil, -45)

missil_rect = missil.get_rect() 

missil1 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion3/Explosion3_4.png')
missil1 = pygame.transform.scale(missil,(500,550))
missil1 = pygame.transform.rotate(missil, -45)

missil1_rect = missil1.get_rect() 

alien = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship4/Ship4.png')
alien = pygame.transform.scale(alien,(100,100))

pos_allien_x = 300
pos_allien_y = 300
alien_rect = alien.get_rect()


class Inimigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.inimigo = []
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship1/Ship1.png'))
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship2/Ship2.png'))
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship3/Ship3.png'))
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship4/Ship4.png'))
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship5/Ship5.png'))
        self.inimigo.append(pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship6/Ship6.png'))
        self.atual = 0
        self.image = self.inimigo[1]
        self.rect = self.image.get_rect(center=(230,80))
        self.rect = self.rect
        
    def update(self):
        
        
        self.atual = self.atual + 0.1
        if self.atual >= len(self.inimigo):        
            self.rect
        if  self.rect.x :
                self.rect.x -= 1 
        if  self.rect.x == -0 :
                self.rect.x += 500 
           
aumentando_magia = 50,50           
   


      
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
        self.atual = 0
        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=(400,300))
    
    def update(self):
            self.atual = self.atual + 0.35
            if self.atual >= len(self.sprites):        
                    self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(tamanho_nave)) 
            self.rect = self.image.get_rect( center =(pos_player_x,pos_player_y))
            

         # Funcoes 

def respawn():
    y = random.randint(1,500)
    x = 600
    return [x,y]
def respawn_missil():
    triggered = False
    missil_sound.play()
    respawn_missil_x = pos_player_x 
    respawn_missil_y = pos_player_y 
    vel_y_missil = 0
    return[respawn_missil_x,respawn_missil_y, triggered, vel_y_missil]
def colisions():
    global pontos
    if missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False


group_inimigos = pygame.sprite.Group()
group_nave = pygame.sprite.Group()
group_nave.add(Nave())
group_inimigos.add(Inimigos())





clock = pygame.time.Clock()

while rodando:
    clock = 100


    #posicao do Rect
    missil1_rect.x = pos_x_missil
    missil1_rect.y = pos_y_missil
    missil_rect.y = pos_y_missil
    missil_rect.x = pos_x_missil
    alien_rect.y = pos_allien_y
    alien_rect.x = pos_allien_x

    # Movimento
    x -= 0.1
    pos_allien_x -= 0.5
    
    pos_y_missil -= vel_y_missil

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()

    userInput = pygame.key.get_pressed()
    
    if userInput[pygame.K_a] and pos_player_x > 44 : 
            pos_player_x = pos_player_x - veL_nave
            pos_player_y = pos_player_y + 0
            if not triggered:
                pos_x_missil = pos_x_missil - veL_nave
                pos_y_missil = pos_y_missil + 0
    if userInput[pygame.K_d] and pos_player_x < largura - 45 :
            pos_player_x = pos_player_x + veL_nave
            pos_player_y = pos_player_y - 0
            if not triggered:
                pos_x_missil = pos_x_missil + veL_nave
                pos_y_missil = pos_y_missil - 0
    if userInput[pygame.K_w]and pos_player_y > 44: 
            pos_player_x = pos_player_x + 0
            pos_player_y = pos_player_y - veL_nave
            if not triggered:
                pos_x_missil = pos_x_missil + 0 
                pos_y_missil = pos_y_missil - veL_nave
    if userInput[pygame.K_s] and pos_player_y < altura - 45: 
            pos_player_x = pos_player_x - 0
            pos_player_y = pos_player_y + veL_nave
            if not triggered:
                pos_x_missil = pos_x_missil - 0
                pos_y_missil = pos_y_missil + veL_nave
    if userInput[pygame.K_SPACE]  :
            triggered = True
            vel_y_missil = velocidade_do_missil
            
            # Respawn

    if pos_allien_y == 50:
        pos_allien_x = respawn()[0]
        pos_allien_y = respawn()[1]

    if pos_y_missil < 0:
        pos_x_missil, pos_y_missil, triggered, vel_y_missil = respawn_missil()

    if pos_allien_y == 50 or colisions():
        pos_allien_x = respawn()[0]
        pos_allien_y = respawn()[1]
   
    print(pontos)
   
    screen.blit(img,(0, 0))

   
    #group_tela.draw(tela)
    group_inimigos.draw(screen)
    
    pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
    screen.blit(missil1,(pos_x_missil-65 ,pos_y_missil-10))

    pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
    screen.blit(missil1,(pos_x_missil-55 ,pos_y_missil-10))

    pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
    screen.blit(missil1,(pos_x_missil-45 ,pos_y_missil-10))

    pygame.draw.rect(screen,(255,0,0),missil_rect,-1)
    screen.blit(missil1,(pos_x_missil-30 ,pos_y_missil-10))

    pygame.draw.rect(screen,(255,0,0),alien_rect,-1)
    screen.blit(alien,(pos_allien_x,pos_allien_y))

    score = font.render(f'Pontos: {int(pontos)} ',True,(0,0,0))
    screen.blit(score,(5,5))

    group_nave.update()
    group_nave.draw(screen)
    #group_tela.update()
    #group_laser.update()
    group_inimigos.update()
   
    pygame.display.flip()

