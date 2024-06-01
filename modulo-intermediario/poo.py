# Classe simples e execução simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, nome_amigo):
        print(f"{self.nome} está falando com {nome_amigo}")


p1 = Pessoa("João", 21)
p1.falar("Maria")


# Classe com métodos de classe
class Carro:
    ano_lancamento = 2018

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor

    def carro_velho(self):
        if self.valor <= 10.000:
            print("Carro antigo com o valor abaixo de 10.000")
            return
        print(f"O carro da marca {self.marca} é novo")

    @classmethod
    def novo_carro(cls, marca):
        return cls(marca, 25.520)


c1 = Carro.novo_carro("Ford")
print(c1.valor)
