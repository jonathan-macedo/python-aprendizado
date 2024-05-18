cond = 0
boll = True
nomes = ["Joao", "Maria", "Noé", "Paris", "Mariana", "Mario", "Mariano"]

# Com While
while cond <= 15 and boll == True:
    if cond == 13:
        print("Finalmente SAIU!!!")
        boll = False
    cond = cond + 1
    print("Ainda não saiu")

print("------------------------------------------------------------------------------------------------------------")
# Com For - Simples
for i in nomes:
    print(i)

# Com For - Enumerate
for i, elementos in enumerate(nomes):
    print(f"Indice: {i} ---- Elemento: {elementos}")

# Com For - Range
for i in range(5):
    print("Com a função range(): ", i)
