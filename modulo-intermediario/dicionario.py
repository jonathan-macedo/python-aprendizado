livraria = {"id": 1, "book": "Santo Agostinho", "author": "Giovanni Papini"}

# Vai pegar um item do dicionario
print(livraria["book"])  # Santo Agostinho


# Algumas funções importantes
print(livraria.values())  # vai retornar os valores do dicionario
print(livraria.keys())  # vai retornar as chaves, ou seja, indicadores do dicionario
print(livraria.items())  # vai retornar os valores e as chaves

for key, value in livraria.items():
    print(f"A chave:{key} tem o valor {value}")
