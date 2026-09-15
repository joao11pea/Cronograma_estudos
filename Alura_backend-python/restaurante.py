class Restaurante:
    

    def __init__(self, nome="", categoria="", ativo = False):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f"{self.nome} | {self.categoria}"
        

restaurante1 = Restaurante("MC", "FastFood", )

print(restaurante1)