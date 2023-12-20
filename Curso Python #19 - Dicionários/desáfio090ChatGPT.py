def main():
    print("Desafio 090: Desenvolva um programa que leia o nome e a média de um aluno, armazenando essas informações em um dicionário.")
    print("Ao final, exiba o conteúdo da estrutura na tela.\n")

    aluno = {}

    aluno['nome'] = str(input("Informe o nome do aluno: "))

    try:
        aluno['media'] = float(input(f"Informe a média do(a) {aluno['nome']}: "))
    except ValueError:
        print("Erro: Certifique-se de inserir um valor numérico para a média.")
        return

    aluno['situacao'] = 'Aprovado' if aluno['media'] >= 5 else 'Reprovado'

    print(f"\nDados do(a) {aluno['nome']}:\n")
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {aluno['media']}")
    print(f"Situação: {aluno['situacao']}")

if __name__ == "__main__":
    main()
