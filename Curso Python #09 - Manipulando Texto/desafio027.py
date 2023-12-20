def acharPrimeiroNome(nomeCompleto):
    return nomeCompleto.split()[0]

def acharUltimoNome(nomeCompleto):
    return nomeCompleto.split()[-1]

def main():
    print("Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente")
    print("Ex: Ana Maria de Souza.")
    print("primeiro = Ana")
    print("último = Souza")

    nomeCompleto = str(input("Digite o seu nome completo: "))
    
    primeiroNome = acharPrimeiroNome(nomeCompleto)

    print(f"O seu primeiro nome é: {primeiroNome}")

    ultimoNome = acharUltimoNome(nomeCompleto)

    print(f"O seu último nome é: {ultimoNome}")


if __name__ == "__main__":
    main()