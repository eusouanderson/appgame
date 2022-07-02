import pygame
import random
from pygame.sprite import Group, GroupSingle ,Sprite

pygame.init()

x = 700
y = 600
tamanho_nave = 50 , 50

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('War Naves2')

bg = pygame.image.load('img/back2.png').convert_alpha()
bg = pygame.transform.scale(bg,(x,y))

alien = pygame.image.load('enemy/PNG_Parts&Spriter_Animation/Ship4/Ship4.png')
alien = pygame.transform.scale(alien,(100,100))

playerImg = pygame.image.load('navei/redfighter0001.png')
playerImg = pygame.transform.scale(playerImg,(100,100))
playerImg = pygame.transform.rotate(playerImg, -90)

missil = pygame.image.load('img/lith1.png')
missil = pygame.transform.scale(missil,(50,50))
missil = pygame.transform.rotate(missil, -45)

rodando = True
font = pygame.font.SysFont('font/ARCADE.TTF', 50)
vel_x_missil = 0
pos_x_missil = 250
pos_y_missil = 310

pos_allien_x = 700
pos_allien_y = 360

pos_player_x = 200
pos_player_y = 300

pontos = 10
triggered = False

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect() 
# Classes 

  
              
 


def respawn():
    x = 600
    y = random.randint(1,500)
    return [x,y]
def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_x_missil = 0
    return[respawn_missil_x,respawn_missil_y, triggered, vel_x_missil]
def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -=1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False

clock = pygame.time.Clock()
while rodando:
    clock= 150
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg,(0,0))
    rel_x = x % bg.get_rect().width
    screen.blit(bg,(rel_x -bg.get_rect().width,0))
    if rel_x < 750:
        screen.blit(bg,(rel_x,0))

    # posicao do Rect

    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_y_missil
    missil_rect.x = pos_x_missil

    alien_rect.y = pos_allien_y
    alien_rect.x = pos_allien_x



    # Movimento
    x -= 0.1
    pos_allien_x -= 0.5
    pos_x_missil += vel_x_missil

    userInput = pygame.key.get_pressed()
    
    if userInput[pygame.K_a] and pos_player_y : 
            pos_player_x = pos_player_x - 1
            pos_player_y = pos_player_y + 0
            if not triggered:
                pos_x_missil = pos_x_missil - 1
                pos_y_missil = pos_y_missil + 0
    if userInput[pygame.K_d] and pos_player_y :
            pos_player_x = pos_player_x + 1
            pos_player_y = pos_player_y - 0
            if not triggered:
                pos_x_missil = pos_x_missil + 1
                pos_y_missil = pos_y_missil - 0
    if userInput[pygame.K_w]and pos_player_x : 
            pos_player_x = pos_player_x + 0
            pos_player_y = pos_player_y - 1
            if not triggered:
                pos_x_missil = pos_x_missil + 0 
                pos_y_missil = pos_y_missil - 1
    if userInput[pygame.K_s] and pos_player_x : 
            pos_player_x = pos_player_x - 0
            pos_player_y = pos_player_y + 1
            if not triggered:
                pos_x_missil = pos_x_missil - 0
                pos_y_missil = pos_y_missil + 1
    if userInput[pygame.K_SPACE] and pos_player_x :
            triggered = True
            vel_x_missil = 1
    #Regras
    if pontos == -1:
        rodando = True


    # rerspawn
    if pos_allien_x == 50:
        pos_allien_x = respawn()[0]
        pos_allien_y = respawn()[1]
        
    if pos_x_missil == 600:
        pos_x_missil, pos_y_missil, triggered, vel_x_missil = respawn_missil()

        
    if pos_allien_x == 50 or colisions():
        pos_allien_x = respawn()[0]
        pos_allien_y = respawn()[1]

    # Grupos 

    group_nave = pygame.sprite.Group()
    #group_nave.add(Nave())
    group_nave.draw(screen)
    group_nave.update()

    pygame.draw.rect(screen,(255,255,255),player_rect,-1)
    pygame.draw.rect(screen,(255,0,0),missil_rect,-1)
    pygame.draw.rect(screen,(255,0,0),alien_rect,-1)

    score = font.render(f'Pontos: {int(pontos)} ',True,(0,0,0))
    screen.blit(score,(5,5))

    # Criar Imagem
    screen.blit(missil,(pos_x_missil,pos_y_missil))
    screen.blit(alien,(pos_allien_x,pos_allien_y))
    screen.blit(playerImg,(pos_player_x,pos_player_y))
    pygame.display.update()


    
   