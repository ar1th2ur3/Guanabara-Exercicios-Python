def main():
    print("Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados")

    numero = str(input("Digite um número: "))
    
    numeroSeparado = list(numero)

    print(numeroSeparado)

if __name__ == "__main__":
    main()
