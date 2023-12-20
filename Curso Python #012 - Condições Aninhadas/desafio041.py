def categoriaAtleta(atletaIdade):
    if atletaIdade <= 9:
        print("Para a sua idade, você é mirim.")
    elif atletaIdade <= 14:
        print("Para a sua idade, você é: INFANTIL")
    elif atletaIdade <=19:
        print("Para a sua idade, você é: JUNIOR.")
    elif atletaIdade <=20:
        print("Para a sua idade, você é: SENIOR.")
    else:
        print("Para a sua idade, você é: MASTER.")
    

def main():
    print("A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a icade:")
    print("Até 9 anos: MIRIM.")
    print("Até 14 anos: INFANTIL.")
    print("Até 19 anos: JUNIOR.")
    print("Até 20 anos: SENIOR.")
    print("Acima: MASTER.")

    atletaIdade = int(input("Digite a idade do atleta: "))

    message = categoriaAtleta(atletaIdade)

    print(message)

if __name__ == "__main__":
    main()