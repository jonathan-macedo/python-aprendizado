def buscar_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = buscar_menor(arr)
        novo_arr.append(arr.pop(menor))
    return novo_arr


print(ordenacao_selecao([5, 3, 6, 2, 10]))
