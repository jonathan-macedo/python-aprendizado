# from uteis import calculo
from uteis.calculo.fatorial import fatorial

numero01 = int(input("Digite um valor: "))
fat = fatorial(numero01)
# fat = calculo.fatorial(numero01)
print(f"O fatorial de {numero01} é {fat}")
