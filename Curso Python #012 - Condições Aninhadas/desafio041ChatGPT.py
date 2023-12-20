def categoriaAtleta(atletaIdade):
    if atletaIdade <= 9:
        return "MIRIM"
    elif atletaIdade <= 14:
        return "INFANTIL"
    elif atletaIdade <= 19:
        return "JUNIOR"
    elif atletaIdade <= 20:
        return "SENIOR"
    else:
        return "MASTER"

def main():
    print("A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:")
    print("Até 9 anos: MIRIM.")
    print("Até 14 anos: INFANTIL.")
    print("Até 19 anos: JUNIOR.")
    print("Até 20 anos: SENIOR.")
    print("Acima: MASTER")

    atletaIdade = int(input("Digite a idade do atleta: "))
    
    categoria = categoriaAtleta(atletaIdade)
    print(f"Para a sua idade, você é: {categoria}")

if __name__ == "__main__":
    main()
