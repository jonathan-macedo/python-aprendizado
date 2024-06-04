# EXERCÍCIO DE FIXAÇÃO
# def soma(lista):
#     if lista == []:
#         return 0
#     return lista[0] + soma(lista[1:])


# print(soma([1, 3, 5]))


# def num_items(lista):
#     return len(lista)


# print("A maneira básica: ", num_items([1, 3, 5, 4, 9, 10]))


# def count_items(lista):
#     if lista == []:
#         return 0
#     return 1 + count_items(lista[1:])


# print("A maneira recursiva: ", count_items([1, 3, 5, 4, 9, 10]))


# def maximo(lista):
#     if len(lista) == 2:
#         return lista[0] if lista[0] > lista[1] else lista[1]
#     sub_max = maximo(lista[1:])
#     return lista[0] if lista[0] > sub_max else sub_max


# print(maximo([10, 325, 51, 44, 98, 101]))


# def pesquisa_binaria_recursiva(lista, item, baixo, alto):
#     if alto >= baixo:
#         meio = (baixo + alto) // 2
#         chute = lista[meio]

#         if chute == item:
#             return meio
#         elif chute > item:
#             return pesquisa_binaria_recursiva(lista, item, baixo, meio - 1)
#         else:
#             return pesquisa_binaria_recursiva(lista, item, baixo, meio + 1)
#     else:
#         return None


# minha_lista = [1, 3, 5, 7, 9]

# resposta1 = pesquisa_binaria_recursiva(minha_lista, 3, 1, 9)


# EXEMPLO REAL DE QUICKSORT
def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([10, 58, 366, 102, 3644, 1, 2, 8]))
