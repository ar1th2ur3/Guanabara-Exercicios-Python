from time import sleep

def calcularIMC(peso, altura):
    if altura == 0:
        raise ValueError("A altura não pode ser zero.")
    imc = peso / (altura ** 2)
    return imc

def classificarIMC(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso saudável"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

def obterInformacoesIMC(imc):
    if imc < 18.5:
        return "Você está abaixo do peso. Recomenda-se ganhar peso de forma saudável."
    elif 18.5 <= imc < 24.9:
        return "Você tem um peso saudável. Continue com hábitos saudáveis."
    elif 25 <= imc < 29.9:
        return "Você está sobrepeso. Considere fazer ajustes na sua dieta e praticar exercícios."
    elif 30 <= imc < 34.9:
        return "Você tem Obesidade Grau 1. Consulte um profissional de saúde para orientação."
    elif 35 <= imc < 39.9:
        return "Você tem Obesidade Grau 2. Procure ajuda médica para um plano de gerenciamento."
    else:
        return "Você tem Obesidade Grau 3. É crucial buscar ajuda médica imediatamente."

def main():
    print("Desenvolva um programa que leia o peso e a altura de uma pessoa e forneça informações sobre o IMC.")
    sleep(2)
    
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura = float(input("Digite a sua altura (em metros): "))
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos válidos.")
        return

    try:
        imc = calcularIMC(peso, altura)
    except ValueError as e:
        print(str(e))
        return

    classificacao = classificarIMC(imc)
    informacoes = obterInformacoesIMC(imc)

    print(f"Seu IMC é {imc:.2f}, o que indica: {classificacao}")
    print(informacoes)

if __name__ == "__main__":
    main()
