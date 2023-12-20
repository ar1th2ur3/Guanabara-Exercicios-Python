import datetime

print("Desáfio 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.")
print("Se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.")
print("Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.")

ano_atual = datetime.datetime.now().year
pessoa = {}
idadePessoa = 0

pessoa['nome'] = str(input("Por favor, digite o nome da pessoa: "))
pessoa['anoNascimento'] = int(input("Por favor, digite o ano de nascimento: "))
pessoa['carteiraDeTrabalho'] = str(input("A pessoa tem carteira de trabalho ?(0 não tem) "))
idadePessoa = ano_atual - pessoa['anoNascimento']

if pessoa['carteiraDeTrabalho'] is "0":
    print(50 * "-=")
    print(f"O nome da pessoa é: {pessoa['nome']}")
    print(50 * "-=")
    print("O ano de nascimento é:", pessoa["anoNascimento"])
    print(50 * "-=")
    print(f"A pessoa tem: {idadePessoa} anos")
    print(50 * "-=")
    print("Não tem carteira de trabalho.")
    print(50 * "-=")
else:
    pessoa['AnoContratacao'] = int(input("Qual foi o ano de contratação? "))
    print(50 * "-=")
    pessoa['Salario'] = float(input("Qual o salário? "))
    print(50 * "-=")
print(f"O(a) irá {pessoa['nome']} irá se aposentar com {idadePessoa + 35}")
    
