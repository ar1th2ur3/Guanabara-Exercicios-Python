def conversãoInteiro(n, v):
    def binario(n):
        return bin(n)[2:]

    def octal(n):
        return oct(n)[2:]

    def hexadecimal(n):
        return hex(n)[2:]

    conversores = {1: binario, 2: octal, 3: hexadecimal}
    
    if v in conversores:
        return conversores[v](n)
    else:
        return "Nenhuma das opções escolhidas"

def main():
    print("Este programa converte um número inteiro para diferentes bases numéricas.")
    print("1 para binário")
    print("2 para octal")
    print("3 para hexadecimal")

    n = int(input("Digite um número inteiro: "))
    v = int(input("Escolha a base de conversão (1/2/3): "))

    opçãoEscolhida = conversãoInteiro(n, v)
    
    if opçãoEscolhida != "Nenhuma das opções escolhidas":
        print(f"O valor {n} na base {v} é: {opçãoEscolhida}")
    else:
        print("Opção inválida. Escolha 1 para binário, 2 para octal ou 3 para hexadecimal.")

if __name__ == "__main__":
    main()
