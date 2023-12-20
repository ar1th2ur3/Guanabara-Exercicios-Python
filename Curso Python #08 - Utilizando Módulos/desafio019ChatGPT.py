import random

def sortear_nome(nomes):
    nome_sorteado = random.choice(nomes)
    return nome_sorteado

def main():
    print("Desafio - Sorteio de Aluno")

    num_alunos = int(input("Quantos alunos estão presentes? "))
    
    nomes = []
    for i in range(num_alunos):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nomes.append(nome)

    nome_sorteado = sortear_nome(nomes)

    print(f"O nome sorteado foi: {nome_sorteado}")

if __name__ == "__main__":
    main()
