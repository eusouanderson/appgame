class Cachorros :
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au ')
    def correr(self):
        print(f'{self.nome} esta correndo')
cachorro1 = Cachorros('Toby', 'Marrom', 5 , 'Grande')

print(cachorro1.nome)

cachorro1.idade = 10
print(cachorro1.tamanho)
print(cachorro1.idade)

cachorro1.latir()
cachorro1.correr()

cachorro2 = Cachorros('Max', 'preto' , 3 , 'pequeno')

print(cachorro2.nome)
cachorro2.correr()




