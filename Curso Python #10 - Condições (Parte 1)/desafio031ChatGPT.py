def calculoViagem(distancia, idade_passageiro):
    preco_base = 0.50  # Preço base por quilômetro
    if distancia <= 200:
        preco = distancia * preco_base
    else:
        preco = distancia * (preco_base - 0.05)  # Desconto de 5% para viagens mais longas

    if idade_passageiro < 12:
        preco *= 0.7  # Desconto de 30% para passageiros com menos de 12 anos
    elif idade_passageiro >= 65:
        preco *= 0.8  # Desconto de 20% para passageiros com 65 anos ou mais

    return preco

def main():
    print("Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km e a idade do passageiro.")
    print("Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.")
    print("Ofereça descontos de 30% para passageiros com menos de 12 anos e de 20% para passageiros com 65 anos ou mais.")

    distancia = float(input("Qual a distância da viagem em Km? "))
    idade_passageiro = int(input("Qual a idade do passageiro? "))

    preco = calculoViagem(distancia, idade_passageiro)
    print(f"O preço da passagem é R$ {preco:.2f}")

if __name__ == "__main__":
    main()
