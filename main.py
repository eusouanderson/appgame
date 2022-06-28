from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 640
largura = 400
tamanho = 640, 400
tela= display.set_mode(size=(600,400), depth=0)
display.set_caption('War Naves')
fundo=scale ( load('img/cenario.jpg'), tamanho)
relogio = pygame.time.Clock()



class Nave1(Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = load('img/nav1.jpg')
        self.rect = self.image.get_rect()
    def update(self):
        ...
class Magia1(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('img/mg1.jpg')
        self.rect = self.image.get_rect()  
    def update(self):
        ...
class Inimigo1(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('img/ini1.png')
        self.rect = self.image.get_rect()
    def update(self):
        ...


inimigo1= Inimigo1() 
magia= Magia1()
nave= Nave1()
x = largura/2
y = altura/2 
pontos = 0
x_verde = randint (40, 600)
y_verde = randint (50, 430)
x_circ = randint (40,600)
y_circ = randint (50,430)
fonte = pygame.font.SysFont("Arial", 40, True, True )

while True:
    relogio.tick(160)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (225,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20 
            if event.key == K_s:
                y = y + 20
    if pygame.key.get_pressed()[K_a]:
        x = x - 8
    if pygame.key.get_pressed()[K_d]:
        x = x + 8
    if pygame.key.get_pressed()[K_w]:
        y = y - 8
    if pygame.key.get_pressed()[K_s]:
        y = y + 8

    ret_linha1= pygame.draw.line(tela,(255,0,255),(0,600),(0,0),5)
    ret_linha2 = pygame.draw.line(tela,(255,0,255),(0,0),(600,0),5)
    ret_linha3 = pygame.draw.line(tela,(255,0,255),(600,0),(600,600),5)
    ret_circ = pygame.draw.circle(tela,(0,255,100),(x_circ,y_circ),40)
    ret_vermelho = pygame.draw.rect(tela,(255,0,0),(x,y,40,50))
    ret_verde = pygame.draw.rect(tela,(0,255,0),(x_verde,y_verde,40,50))

    if ret_vermelho.colliderect(ret_verde):
        x_verde = randint(40, 600)
        y_verde = randint(50, 430)
        pontos = pontos + 1
    if ret_vermelho.colliderect(ret_circ):
        x_circ = randint(40, 600)
        y_circ = randint(50, 430)
        pontos = pontos - 1
   
   
    tela.blit(texto_formatado,(410,10))


    display.update()
 
    

    

