





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
