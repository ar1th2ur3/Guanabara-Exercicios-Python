print("Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.")
print(100 * "=")
print("Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.")
print(100 * "=")

numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    n = int(input("Digite um número de 0 até 20: "))

    if n > 20:
        print(f"Você digitou {n}, que não está entre 0 - 20.")
        print("Digite um número entre 0 a 20.")
        continue
    else:
        print(f"Você digitou o número: {numeros_por_extenso[n]}")
        break
