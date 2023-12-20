from time import sleep

def calculoIMC(peso, altura):
    imc = peso / altura ** 2
    return imc

def statusIMC(imc):
    if imc < 18.5:
        return "Abaixo do peso."
    elif 18.5 <= imc < 25:
        return "Peso ideal."
    elif 25 <= imc < 30:
        return "Sobrepeso."
    elif 30 <= imc < 40:
        return "Obesidade."
    else:
        return "Obesidade mórbida."

def main():
    print("Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:")
    print("Abaixo de 18.5: Abaixo do peso.")
    print("Entre 18.5 e 25: Peso ideal.")
    print("25 até 30: Sobrepeso.")
    print("30 até 40: Obesidade.")
    print("Acima de 40: Obesidade mórbida.")
    
    sleep(2)
    
    peso = float(input("Digite o seu peso (em kg): "))
    altura = float(input("Digite a sua altura (em metros): "))
    
    imc = calculoIMC(peso, altura)
    status = statusIMC(imc)

    print(f"Seu IMC é {imc:.2f}, o que indica: {status}")

if __name__ == "__main__":
    main()
