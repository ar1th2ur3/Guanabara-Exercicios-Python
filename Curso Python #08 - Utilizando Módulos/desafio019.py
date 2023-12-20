import random

def sortearNome(nomes):
    nome_sorteado = random.choice(nomes)
    return nome_sorteado

def main():
    print("Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.")

    nomes = ["Arthur", "Lucas", "Rosangela", "Roberto"]
    nome_sorteado = sortearNome(nomes)

    print(f"O nome sorteado foi: {nome_sorteado}")

if __name__ == "__main__":
    main()
