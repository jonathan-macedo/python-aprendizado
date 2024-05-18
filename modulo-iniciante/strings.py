print("Ola")
print("ola")
print(
    """
    Olá
      Mundo
      Novo
"""
)
print("-----------------------------------------------------------------------------")
# Tamanho da string e pegar uma parte dela
NOME = "Jonathan"
print(len(NOME))
print(NOME[3])
print(NOME[2:-1])

print("-----------------------------------------------------------------------------")
# OPERAÇÕES

print("Operação in")
print(NOME in "Jonathan")  # True
print(NOME in "Jo")  # False

print("Operação not in")
print(NOME not in "Jonathan")  # False
print(NOME not in "Jo")  # True

print("Operação concatenação")
print(NOME + " " + "ão")

print("Operação de repição")
print(NOME * 3)

print("----------------------------------------------------------------------------")

# MÉTODOS
print(NOME.capitalize())
print(NOME.count("a"))
print(NOME.startswith("n"))
print(NOME.endswith("J"))
print("Jonathan está em casa dormindo".split(" "))
print(" ".join(["Jonathan", "em casa"]))
print(NOME.replace("Jonathan", "João"))
