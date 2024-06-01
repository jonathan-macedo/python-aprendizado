# Classe simples e execução simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, nome_amigo):
        print(f"{self.nome} está falando com {nome_amigo}")


p1 = Pessoa("João", 21)
p1.falar("Maria")
