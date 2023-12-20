from random import randint

idade = randint(15,50)

if idade == 18:
    print("Você precisa se alistar.")
elif idade > 18:
    print(f"Você já passou do tempo de alistamento, você está atrasado {idade-18} anos")
else:
    idadeFalta = 18 - idade
    print(f"Faltam {idadeFalta} anos para você se alistar")