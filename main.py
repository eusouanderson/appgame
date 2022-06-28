from turtle import update
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



pygame.init()

VolumeS_do_game = 10
VolumeM_do_game = 5
# Soms
musica_de_fundo = pygame.mixer.music.load('sounds/musicadefundo.mp3')
pygame.mixer.music.set_volume(VolumeM_do_game)
pygame.mixer.music.play(-1)
colisao_br = pygame.mixer.Sound('sounds/break_block.wav')
colisao_br.set_volume(VolumeS_do_game)
colisao_wi = pygame.mixer.Sound('sounds/coin.wav')
colisao_wi.set_volume(VolumeS_do_game)
# Tamanho de tela
altura = 600
largura = 600
tamanho = largura , altura
superficie= display.set_mode(size=(tamanho))
fundo=scale (load('img/back1.png'),tamanho)
display.set_caption('War Naves')
relogio = pygame.time.Clock()

class unicornio(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/sprite1.jpg')
        self.rect = self.image.get_rect()
        

class Nave1(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/nav1.jpg')
        self.rect = self.image.get_rect()
        
        
    
class Magia1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/mg1.jpg')
        self.rect = self.image.get_rect()  
    def update(self):
        ...
        
class Inimigo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/ini1.png')
        self.rect = self.image.get_rect()
    def update(self):
        ...

nave = Nave1()
inimigo1= Inimigo1() 
grupo_magias = Group()
grupo_inimigos = Group(inimigo1)
grupo_nave= GroupSingle(nave)


x = int(largura/2)
y = int(altura/2 )
pontos = 0
x_verde = randint (40, 300)
y_verde = randint (80, 600)
x_circ = randint (40, 300)  
y_circ = randint (80, 600)
fonte = pygame.font.SysFont("font/ARCADE.TTF", 40, True, True )

while True:
    relogio.tick(160)
    superficie.blit(fundo,
    (0,0))
    #Grupos
    #grupo_nave.draw(superficie)
    grupo_inimigos.draw(superficie)
    #grupo_magias.draw(superficie)
    #Letras na Tela
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (225,255,255))
    # Eventos 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    # Evento de controles teclado
        
        if event.type == KEYDOWN:
            

            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20 
            if event.key == K_s:
                y = y + 20
            if event.key == K_SPACE:
               ...


    if pygame.key.get_pressed()[K_a]:
        x = x - 8
    if pygame.key.get_pressed()[K_d]:
        x = x + 8
    if pygame.key.get_pressed()[K_w]:
        y = y - 8
    if pygame.key.get_pressed()[K_s]:
        y = y + 8

    
    ret_linha1= pygame.draw.line(superficie,(255,0,255),(0,altura),(0,0),5)
    ret_linha2 = pygame.draw.line(superficie,(255,0,255),(0,0),(largura,0),5)
    ret_linha3 = pygame.draw.line(superficie,(255,0,255),(altura,0),(altura,altura),5)
    ret_linha4 = pygame.draw.line(superficie,(255,0,255),(largura,largura),(0,largura),5)
    
    ret_circ = pygame.draw.circle(superficie,(0,255,100),(x_circ,y_circ),40)    
    jogador = pygame.draw.rect(superficie,(255,0,0),(x,y,40,50))    
    ret_verde = pygame.draw.rect(superficie,(0,255,100),(x_verde,x_verde,40,50))
    
    
    (superficie,(x,y,40,50))
    
            


    if jogador.colliderect(ret_verde):
        x_verde = randint(40, largura)
        y_verde = randint(80, altura)
        pontos = pontos + 1
        colisao_wi.play()
        

    if jogador.colliderect(ret_circ):
        x_circ = randint(40, largura)
        y_circ = randint(40, altura)
        pontos = pontos - 1
        colisao_br.play()   
   
   
    superficie.blit(texto_formatado,(0,0))

    display.update()
 
    

    

