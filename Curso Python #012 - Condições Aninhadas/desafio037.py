def conversãoInteiro(n, v):
    if v == 1:
        binario = bin(n)
        return str(binario)
    elif v == 2:
        octal = oct(n)
        return str(octal)
    elif v == 3:
        hexadecimal = hex(n)
        return str(hexadecimal)
    else:
        return "Nenhuma das opções escolhidas"

def main():
    print("Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.")
    print("1 para binário")
    print("2 para octal")
    print("3 para hexadecimal")

    n = int(input("Digite um número qualquer: "))
    v = int(input("Digite uma opção: "))

    opçãoEscolhida = conversãoInteiro(n, v)
    
    print(opçãoEscolhida)

if __name__ == "__main__":
    main()
