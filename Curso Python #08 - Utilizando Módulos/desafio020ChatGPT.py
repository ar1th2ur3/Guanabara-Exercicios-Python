import random

def sortear_ordem_apresentacao(nomes):
    ordem_apresentacao = nomes[:]
    random.shuffle(ordem_apresentacao)
    return ordem_apresentacao

def main():
    print("Desafio - Sorteio de Ordem de Apresentação")

    num_alunos = int(input("Quantos alunos estão apresentando? "))
    
    if num_alunos < 1:
        print("Número de alunos deve ser pelo menos 1.")
        return

    nomes = []
    for i in range(num_alunos):
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nomes.append(nome)

    ordem_apresentacao = sortear_ordem_apresentacao(nomes)

    print("Ordem de Apresentação Sorteada:")
    for i, aluno in enumerate(ordem_apresentacao, 1):
        print(f"{i}. {aluno}")

if __name__ == "__main__":
    main()
