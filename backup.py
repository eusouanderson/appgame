
class Unicornio(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_unicornio= []
        for i in range(3):
            img= sprite_sheet.subsurface((i*32,0),(32,32))
            self.imagens_unicornio.append(img)

        self.index_lista = 0
        self.image = self.imagens_unicornio[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        if self.index_lista > 2:
            self.index_lista =0
        self.index_lista += 0.25
        self.image = self.imagens_unicornio[int(self.index_lista)]
        

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




class Inimigo2(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('img/ini2.png')
        self.rect = self.image.get_rect()      
inimigo2 = Inimigo2()

class Inimigo3(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('img/ini3.png')
        self.rect = self.image.get_rect()
    def update(self):
        ...
inimigo3 = Inimigo3()

class Inimigo4(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('img/ini4.png')
        self.rect = self.image.get_rect()
    def update(self):
        ...
inimigo4= Inimigo4()

grupo_nave = GroupSingle(nave)


grupo_inimigos = Group()
grupo_inimigos.add(inimigo1)
grupo_inimigos.add(inimigo2)
grupo_inimigos.add(inimigo3)
grupo_inimigos.add(inimigo4)

grupo_nave = GroupSingle()
grupo_nave.add(nave)

grupo_magia = GroupSingle(magia1)



   '''
    if pygame.key.get_pressed()[K_a]:
        x_jogador = x_jogador - 8
    if pygame.key.get_pressed()[K_d]:
        x_jogador = x_jogador + 8
    if pygame.key.get_pressed()[K_w]:
        y_jogador = y_jogador - 8
    if pygame.key.get_pressed()[K_s]:
        y_jogador = y_jogador + 8 '''