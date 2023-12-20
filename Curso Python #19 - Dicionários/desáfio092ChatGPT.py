import datetime

def cadastrar_pessoa():
    pessoa = {}
    pessoa['nome'] = input("Por favor, digite o nome da pessoa: ")
    pessoa['anoNascimento'] = int(input("Por favor, digite o ano de nascimento: "))
    pessoa['carteiraDeTrabalho'] = input("A pessoa tem carteira de trabalho? (0 não tem): ")
    return pessoa

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def cadastrar_trabalhador():
    pessoa = cadastrar_pessoa()

    if pessoa['carteiraDeTrabalho'] == "0":
        exibir_dados_pessoa(pessoa)
    else:
        pessoa['AnoContratacao'] = int(input("Qual foi o ano de contratação? "))
        pessoa['Salario'] = float(input("Qual o salário? "))
        exibir_dados_pessoa(pessoa, True)

def exibir_dados_pessoa(pessoa, trabalhador=False):
    print(50 * "-=")
    print(f"O nome da pessoa é: {pessoa['nome']}")
    print(50 * "-=")
    print(f"O ano de nascimento é: {pessoa['anoNascimento']}")
    print(50 * "-=")
    print(f"A pessoa tem: {calcular_idade(pessoa['anoNascimento'])} anos")
    print(50 * "-=")

    if not trabalhador:
        print("Não tem carteira de trabalho.")
        print(50 * "-=")
    else:
        print(f"Ano de contratação: {pessoa['AnoContratacao']}")
        print(50 * "-=")
        print(f"Salário: {pessoa['Salario']}")
        print(50 * "-=")

    if trabalhador:
        print(f"{pessoa['nome']} irá se aposentar com {calcular_idade(pessoa['anoNascimento']) + 35}")

if __name__ == "__main__":
    print("Desafio 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.")
    print("Se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.")
    print("Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.")
    
    cadastrar_trabalhador()
