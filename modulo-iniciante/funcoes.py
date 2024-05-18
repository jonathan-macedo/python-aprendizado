# Funções padrões da linguagem
def calcular_pagamento(qtd_horas, valor_hora):
    """
    Essa função irá calcular o pagamento do funcionário

    Args:
        qtd_horas (string): quantidade de horas
        valor_hora (string): valor da hora

    Returns:
        float: o valor do salário do funcionário
    """
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))

    return salario


str_horas = input("Digite as horas: ")
str_taxa = input("Digite a taxa: ")
total_salario = calcular_pagamento(str_horas, str_taxa)
print("O valor de seus rendimentos é R$", total_salario)

print("------------------------------------------------------------------------------------------------")

# Função lambda

quadrado = lambda x: x**2

resultado = quadrado(4)
print("Quadrado de 4:", resultado)
