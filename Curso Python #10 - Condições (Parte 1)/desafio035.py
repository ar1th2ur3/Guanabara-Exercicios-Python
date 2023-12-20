from time import sleep

def calculoTriangulo(v1, v2, v3):
    if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
        return "É possível formar um triângulo."
    else:
        return "Não é possível formar um triângulo."

def main():
    print("Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.")
    sleep(2)
    v1 = float(input("Digite o valor do primeiro comprimento: "))
    v2 = float(input("Digite o valor do segundo comprimento: "))
    v3 = float(input("Digite o valor do terceiro comprimento: "))

    mensagem = calculoTriangulo(v1, v2, v3)

    print(mensagem)

if __name__ == "__main__":
    main()
