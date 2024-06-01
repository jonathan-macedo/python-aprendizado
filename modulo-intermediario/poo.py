from random import randint


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


# Classe com métodos estáticos
class Cliente:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand


print(Cliente.gera_id())


# Gatters e Setters
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor


p1 = Produto("Camiseta", 50)
p1.desconto(10)
print(p1.preco)
p2 = Produto("Calça", "R$12")
p1.desconto(20)
print(p2.preco)
