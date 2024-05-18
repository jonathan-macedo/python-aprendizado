notas01 = int(input("Digite nota 1: "))

# Simples
if notas01 == 10:
    print("Conseguiu seu DEZ!!!")

print("-----------------------------------")

# Com else
if notas01 <= 2:
    print("Repetiu de ano")
else:
    print("Passou de ano!!!")

print("----------------------------------")

# Composto
if notas01 == 0:
    print("Ficou devendo MUITO")
elif notas01 >= 7:
    print("UFA")
else:
    print("CHEGA NÉ")
