#mao na massa Alura

#por conveção o nome da classe começa com letra Maiuscula 
class Musica:
    nome = ""
    artista = ""
    duracao = ""

musica1 = Musica()
musica1.nome = "Atlas"
musica1.artista = "Caio Ocean"
musica1.duracao = 102

print(vars(musica1))

#forma com metodos
class Carros:
    def __init__(self, marca="", nome="", cor=""): #self aponta para a instancia 
        self.marca = marca
        self.nome = nome
        self.cor = cor

    def __str__(self):
        return f"{self.marca} | {self.nome}  |  {self.cor} "


carro = Carros("Fiat", "Uno", "branco")
print(carro)