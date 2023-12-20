def calculoViagem(vViagem):
    if vViagem <= 200:
        preco = vViagem * 0.50
    else:
        preco = vViagem * 0.45
    return preco

def main():
    print("Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.")
    print("Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.")

    vViagem = float(input("Qual a distância da viagem? "))
    preco = calculoViagem(vViagem)
    print(f"O preço da passagem é R${preco:.2f}")

if __name__ == "__main__":
    main()
