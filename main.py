
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

#Tela
altura = 600
largura = 600
tamanho = largura , altura
superficie= display.set_mode(size=(tamanho))
fundo=scale (load('img/back1.png'),tamanho)
display.set_caption('Cobra KKK')
relogio = pygame.time.Clock()

ganhou = ('Parabens !!!')
pontos = 0
x_jogador = randint (40, 300)
y_jogador = randint (80, 600)
x_maca = randint (40, 300)  
y_maca = randint (80, 600)
fonte = pygame.font.SysFont("font/ARCADE.TTF", 40, False, False )
lista_cobra = []
comprimento_inicial = 5
velocidade = 5
x_controle = 20
y_controle = 0
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(superficie,(0,255,0),(XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global pontos , comprimento_inicial , lista_cabeca , lista_cobra , morreu
    pontos = 0
    comprimento_inicial = 5
    lista_cobra = []
    lista_cabeca = []
    morreu = False

while True:
    relogio.tick(30)
    
    superficie.blit(fundo,(0,0))
    mensagemwin = f'Ganhou {ganhou}'
    mensagem = f'Pontos: {pontos}'
    texto_vitoria = fonte.render(mensagemwin,True,(255,255,255))
    texto_formatado = fonte.render(mensagem, True, (225,255,255))
    # Eventos 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    # Evento de controles teclado
        
        if event.type == KEYDOWN:
            
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade 
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = - velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    
    x_jogador = x_jogador + x_controle
    y_jogador = y_jogador + y_controle 
    
    ret_linha1= pygame.draw.line(superficie,(0,0,255),(0,altura),(0,0),5)
    ret_linha2 = pygame.draw.line(superficie,(0,0,255),(0,0),(largura,0),5)
    ret_linha3 = pygame.draw.line(superficie,(0,0,255),(altura,0),(altura,altura),5)
    ret_linha4 = pygame.draw.line(superficie,(0,0,255),(largura,largura),(0,largura),5)
    
    ret_circ = pygame.draw.circle(superficie,(0,255,0),(x_maca,y_maca),10)    
    jogador = pygame.draw.rect(superficie,(0,255,0),(x_jogador,y_jogador,20,20))    
    ret_maca = pygame.draw.circle(superficie,(0,255,100),(x_maca,x_maca),5)
    
    
    (superficie,(x_jogador,y_jogador,40,50))
    
    if jogador.colliderect(ret_maca):
        x_maca = randint(40, largura)
        y_maca = randint(80, altura)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 10
        colisao_wi.play()
        
    if jogador.colliderect(ret_circ):
        x_maca = randint(40, largura)
        y_maca = randint(40, altura)
        pontos = pontos - 1
        comprimento_inicial = comprimento_inicial - 10
        colisao_br.play() 

    if jogador.colliderect(ret_linha1 ):
        pontos = pontos - 1
        colisao_br.play()  

    if jogador.colliderect(ret_linha2):
        pontos = pontos - 1
        colisao_br.play()  

    if jogador.colliderect(ret_linha3):
        pontos = pontos - 1
        colisao_br.play()  

    if jogador.colliderect(ret_linha4):
        pontos = pontos - 1
        colisao_br.play()   

    if pontos >= 10:
        ganhou: superficie.blit(texto_vitoria,(200,0))
    
    

    lista_cabeca = []
    lista_cabeca.append (x_jogador)
    lista_cabeca.append (y_jogador)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca)> 1:
        fonte2 = pygame.font.SysFont('arial',20,True, True)
        mensagem = 'Game Over! Precisone a tecla R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem,True,(0,0,0))


        morreu = True
        while morreu:
            superficie.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                   if event.key == K_r: 
                    reiniciar_jogo()
        

            superficie.blit(texto_formatado,(40,200))
            pygame.display.update()
    if x_jogador > largura :
        x_jogador = 0
    if x_jogador < 0 :
        x_jogador = largura
    if y_jogador < 0 :
        y_jogador = altura
    if y_jogador > altura :
        y_jogador = 0
   
    aumenta_cobra(lista_cobra)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra [0]

   
    superficie.blit(texto_formatado,(0,0))

    display.update()
 
  

    

