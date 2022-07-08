import pygame
from pygame.locals import * 
from pygame.locals import QUIT
from random import randint

import random

pygame.init()
pygame.font.init()
# Sound
VolumeM_do_game = 1
pygame.mixer.init()
pygame.mixer.music.load('sounds/Flies By The Fire.wav')
missil_sound = pygame.mixer.Sound('sounds/laserfire02.ogg')
missil_sound.set_volume(VolumeM_do_game)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

pontos1= 10000
pontos2= 20000
pontos3= 30000
pontos4= 40000


#Configuracoes 
# Tela
largura ,altura = 700 , 600 
x = largura
y = altura

rodando = True
objects =[]
tamanho = largura , altura
font = pygame.font.Font('font/ARCADE_N.TTF', 20)

# Nave 
veL_nave = 3
velocidade_do_missil = 10
vel_y_missil = 0
pos_x_missil = largura/2
pos_y_missil = altura/2 

pos_allien_x = 700
pos_allien_y = 360

pos_player_x = largura/2
pos_player_y = altura/2

pontos = 0
level = 0

#TELA INICIAL 

tela_inicial2= pygame.image.load('img/inicial (2).png')
tela_inicial2= pygame.transform.scale(tela_inicial2,(largura,altura))
tela_inicial= pygame.image.load('img/inicial.png')
tela_inicial= pygame.transform.scale(tela_inicial,(largura,altura))

# Tamanho da Nave
triggered = False

tamanho_nave = 100, 100
tamanho_do_missil = 100, 100

# Config IMAGENS E TELA

screen = pygame.display.set_mode((tamanho))
pygame.display.set_caption ('Infinite War Naves')


img= pygame.image.load('img/space3.jpg')
#img= pygame.transform.scale(img,(largura,altura))

img2= pygame.image.load('img/space3.jpg')
#img2= pygame.transform.scale(img2,(largura,altura))

img3= pygame.image.load('img/space3.jpg')
#img3= pygame.transform.scale(img3,(largura,altura))

img4= pygame.image.load('img/space3.jpg')
#img4= pygame.transform.scale(img4,(largura,altura))

img5= pygame.image.load('img/space3.jpg')
#img5= pygame.transform.scale(img5,(largura,altura))

missil = pygame.image.load('img/lith1.png')
missil = pygame.transform.scale(missil,(tamanho_do_missil))
missil = pygame.transform.rotate(missil,random.randint(1,100))


missil1 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion1/Explosion1_2.png')
missil1 = pygame.transform.scale(missil,(tamanho_do_missil))
missil1 = pygame.transform.rotate(missil,random.randint(1,100))



missil2 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion1/Explosion1_3.png')
missil2 = pygame.transform.scale(missil2,(tamanho_do_missil))
missil2 = pygame.transform.rotate(missil2,random.randint(1,100))



missil3 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion1/Explosion1_4.png')
missil3 = pygame.transform.scale(missil3,(tamanho_do_missil))
missil3 = pygame.transform.rotate(missil3,random.randint(1,100))



missil4 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion1/Explosion1_5.png')
missil4 = pygame.transform.scale(missil4,(tamanho_do_missil))
missil4 = pygame.transform.rotate(missil4,random.randint(1,100))


missilalien = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Explosions/Explosion1/Explosion1_5.png')
missilalien = pygame.transform.scale(missil4,(tamanho_do_missil))
#missilalien = pygame.transform.rotate(missil4,random.randint(1,100))



# ALLIENS 

tamanho_alien = 200,200
alien = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship1/Ship1.png')
alien = pygame.transform.scale(alien,(tamanho_alien))
alien = pygame.transform.rotate(alien, 0)

alien1 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship2/Ship2.png')
alien1 = pygame.transform.scale(alien1,(tamanho_alien))
alien1 = pygame.transform.rotate(alien1, 0)

alien2 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship3/Ship3.png')
alien2 = pygame.transform.scale(alien2,(tamanho_alien))
alien2 = pygame.transform.rotate(alien2, 0)

alien3 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship4/Ship4.png')
alien3 = pygame.transform.scale(alien3,(tamanho_alien))
alien3 = pygame.transform.rotate(alien3, 0)

alien4 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship5/Ship5.png')
alien4 = pygame.transform.scale(alien4,(tamanho_alien))
alien4 = pygame.transform.rotate(alien4, 0)

alien5 = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship6/Ship6.png')
alien5 = pygame.transform.scale(alien5,(tamanho_alien))
alien5 = pygame.transform.rotate(alien5, 0)

pos_allien_y = 300
pos_allien_x = 300


# RECTs
alien_rect = alien.get_rect()
alien1_rect =alien1.get_rect()
alien2_rect =alien2.get_rect()
alien3_rect =alien3.get_rect()
alien4_rect = alien4.get_rect()
missilalien_rect = missilalien.get_rect()

missil_rect = missil.get_rect()
missil1_rect = missil1.get_rect()
missil2_rect = missil2.get_rect()
missil3_rect = missil3.get_rect()
missil4_rect = missil4.get_rect()



img_rect = img.get_rect()
img2_rect = img2.get_rect()
img3_rect = img3.get_rect()
img4_rect = img4.get_rect()
img5_rect = img5.get_rect()

screen_rect = screen.get_rect()


tela_inicial_rect = tela_inicial.get_rect()


aumentando_magia = 50,50          
   
              

      
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []       
        self.sprites.append(pygame.image.load('navei/redfighter0001.png'))          #1 esq
        self.sprites.append(pygame.image.load('navei/redfighter0002.png'))          #2 esq
        self.sprites.append(pygame.image.load('navei/redfighter0003.png'))          #3 esq
        self.sprites.append(pygame.image.load('navei/redfighter0004.png'))          #4 esq
        self.sprites.append(pygame.image.load('navei/redfighter0005.png'))          #5 meio
        self.sprites.append(pygame.image.load('navei/redfighter0006.png'))          #6 dir
        self.sprites.append(pygame.image.load('navei/redfighter0007.png'))          #7 dir
        self.sprites.append(pygame.image.load('navei/redfighter0008.png'))          #8 dir
        self.sprites.append(pygame.image.load('navei/redfighter0009.png'))          #9 dir
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
        self.image = pygame.transform.scale(self.image,(100,100)) 
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect( center =(pos_player_x,pos_player_y))
            
# Funcoes 


def respawn():
    y = random.randint(0 ,altura)
    x = largura
    return [x,y]
def respawn_missil():
    triggered = False
    missilalien_rect.x = pos_allien_x
    missilalien_rect.y = pos_allien_y
    missil_sound.play()
    respawn_missil_x = pos_player_x 
    respawn_missil_y = pos_player_y 
    vel_y_missil = 0
    return[respawn_missil_x,respawn_missil_y, triggered, vel_y_missil]
def colisions():
    global pontos , level
   
    if missil_rect.colliderect(alien_rect):
        pontos += 100
        
        
        return True
    else:
        return False
        
def reiniciar_jogo():
    global pontos , level ,morreu
    pontos = 0    
    level = 0
    morreu = False



group_nave = pygame.sprite.Group()
group_nave.add(Nave())


time =pygame.time.Clock()
pause_time = pygame.time.delay(1)




while rodando:
    fps = time.tick(100)
    print(time)    
    

#posicao do Rect
    missil1_rect.x =  missil1_rect.x + 1
    missil1_rect.y = missil1_rect.y +1 
    missil_rect.y = pos_y_missil
    missil_rect.x = pos_x_missil
    alien_rect.y = pos_allien_y
    alien_rect.x = pos_allien_x
    missilalien_rect.x = missil1_rect.x 

# Movimento
    x -= 0.1
    pos_allien_x -= 1 
    
    
    pos_x_missil += vel_y_missil
    missilalien_rect.x += velocidade_do_missil

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()

    userInput = pygame.key.get_pressed()
    
    if userInput[pygame.K_a] and pos_player_x > 44 : 
            pos_player_x = pos_player_x - veL_nave
            pos_player_y = pos_player_y - 0
            if not triggered:
                pos_x_missil = pos_x_missil - veL_nave
                pos_y_missil = pos_y_missil + 0
    if userInput[pygame.K_d] and pos_player_x < largura - 45 :
            pos_player_x = pos_player_x + veL_nave
            pos_player_y = pos_player_y - 0
            if not triggered:
                pos_x_missil = pos_x_missil + veL_nave
                pos_y_missil = pos_y_missil - 0
    if userInput[pygame.K_w]and pos_player_y > 44 : 
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
            
    if userInput[pygame.K_f]  :
            
            tamanho_nave= 500 , 500        

# Respawn

    if pos_y_missil <=largura-largura :
       missilalien_rect.x, pos_x_missil, pos_y_missil, triggered, vel_y_missil = respawn_missil()
    if pos_x_missil >= largura :
        pos_x_missil, pos_y_missil, triggered, vel_y_missil = respawn_missil()

    if pos_allien_x == largura-largura or colisions():
        pontos -= 30
        
        pos_allien_x = respawn()[0]
        pos_allien_y = respawn()[1]
      

#  Niveis de tela 
            
    if pontos > 0 : 
            

            pygame.draw.rect(img,(255,0,0),alien_rect,-1)
            screen.blit(img,(0,img_rect.y))

            if pontos >= pontos1 :
                img = img2
                level = +1
                alien= alien2
            if  pontos > pontos2 :
                level = +2
                img2 = img3
            if pontos >  pontos3 :
                level = +3
                img3 = img4
            if pontos >  pontos4 :
                level = +4
                img4 = img5
            if pontos < -0 :
                pause_time(100000)
  
            rel_x = x % img.get_rect().width
            screen.blit(img,(rel_x - img.get_rect().width,0))
            if rel_x < altura:
                screen.blit(img,(rel_x,0))
            x-= 10 
            pygame.draw.rect(screen,(255,0,0),alien_rect,-1)
            screen.blit(alien,(pos_allien_x,pos_allien_y))
            
            if pontos >= pontos1 :
                alien= alien2
            if  pontos > pontos2 :
                alien2=alien3
            if pontos >  pontos3 :
                alien3=alien4
            if pontos >  pontos4 :
                alien4=alien5

            
            pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
            screen.blit(missil,(pos_x_missil-100 ,pos_y_missil-50))            
            
            if pontos >= pontos1 :
                missil=missil1
            if  pontos > pontos2 :
                missil1=missil2
            if pontos >  pontos3 :
                missil2=missil3
            if pontos >  pontos4 :
                missil3=missil4
# Tela inicial
#Poderes

    pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
    screen.blit(missil1,(pos_x_missil-100 ,pos_y_missil -50))


    pygame.draw.rect(screen,(255,0,0),missil1_rect,-1)
    screen.blit(missilalien,(pos_allien_x ,pos_allien_y))

    pygame.draw.rect(screen,(255,0,0),missil_rect,-1)
    screen.blit(missil1,(pos_x_missil-100 ,pos_y_missil -50 ))
    #Aliens
    score = font.render(f'Pontos: {int(pontos)} ',True,(255,80,0))
    screen.blit(score,(5,5))
    score = font.render(f'Level: {int(level)} ',True,(255,80,0))
    screen.blit(score,(400,5))
  
    group_nave.draw(screen)
    group_nave.update()
   
    pygame.display.flip()

