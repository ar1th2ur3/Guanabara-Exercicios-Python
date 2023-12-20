print("Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.")

t = 1
while True:

    n = int(input("Digite o número desejado para a tabuada aparecer: "))

    if n < 0:
        break

    while t <= 9:

        t += 1

        print(f"{n} x {t} = {n*t}")

print("PAROU")