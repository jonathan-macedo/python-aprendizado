try:
    # Nesse bloco vai acontecer a operação
    numero01 = int(input("Numerador: "))
    numero02 = int(input("Denominador: "))
    resposta = numero01 / numero02
except:
    # Nesse bloco será responsável pelo erro na operação, caso tenha
    print("Algo deu errado em sua conta")
else:
    # OPCIONAL
    # Nesse bloco vai exibir a resposta da operação
    print(resposta)
finally:
    # OPCIONAL
    # Bloco que será sempre executado, mesmo com erro ou acerto
    print("volte sempre cidadão")
