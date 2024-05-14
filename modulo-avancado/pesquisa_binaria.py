def pesquisa_binaria(lista: list, item: int):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) / 2
        chute = lista[meio]
        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
        return None

minha_lista = [1, 3, 5, 7, 9]

resposta1 = pesquisa_binaria(minha_lista, 3)
resposta2 = pesquisa_binaria(minha_lista, -1)
print(resposta1)
print(resposta2)