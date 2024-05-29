# Lista dinâmica - Pode ter valores diversos
livraria = []

# Lista (Array) - Não pode ter outros tipos de dados, depois de definidos
nomes = ["jonathan", "jonas", "joana", "jailson", "joão", "jones"]

print(nomes)

print("=-=" * 25)

# Método para adicionar novo item
nomes.append("Maria")
print(nomes)
print("=-=" * 25)

# Método para remover do final da lista
nomes.pop()  # remove a Maria
print(nomes)
print("=-=" * 25)

# Vai limpar todos os itens da Lista
nomes.clear()
print(nomes)
print("=-=" * 25)

# Vai ordenar todos os nomes da lista (Array)
nomes.sort()
print(nomes)
print("=-=" * 25)

# Vai ordenar os itens de maneira reversa
nomes.reverse()
print(nomes)
print("=-=" * 25)
