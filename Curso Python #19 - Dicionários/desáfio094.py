print("Desáfio 094: Crie um programa que leia *nome*, *sexo*, e *idade* de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.")
print("No final, mostre:")
print("A) Quantas pessoas foram cadastradas.")
print("B) A *média* de idade do grupo.")
print("C) Uma lista com todas as mulheres.")
print("D) Uma lista com todas as pessoas com idade acima da média.")

dadosPessoasLista = list()
totalPessoas = 0
somaIdade = 0 

while True:
    dadosPessoas = {}
    print(50 * "-=")
    dadosPessoas['Nome'] = str(input("Digite o nome da pessoa, por gentileza: "))
    print(50 * "-=")
    dadosPessoas['Sexo'] = str(input("Digite o sexo da pessoa, por gentileza [M/F]: ")).upper()[0]
    while True:
        if dadosPessoas['Sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F!")
        dadosPessoas['Sexo'] = str(input("Digite o sexo da pessoa, por gentileza [M/F]: ")).upper()[0]
    print(50 * "-=")
    dadosPessoas['Idade'] = int(input("Digite a idade da pessoa, por gentileza: "))
    print(50 * "-=")

    escolha = str(input("Você deseja continuar [S/N]? ")).upper()[0]
    while True:
        if escolha in "SN":
            break
        print("ERRO! Digite apenas S ou N!")
        escolha = str(input("Você deseja continuar [S/N]? ")).upper()[0]
    dadosPessoasLista.append(dadosPessoas.copy())

    if escolha != "S":
        break

print(f"A) *{len(dadosPessoasLista)}* pessoas foram cadastradas")
print(50 * "-=")

#Média Idade Grupo.
for pessoas in dadosPessoasLista:
    somaIdade += pessoas["Idade"]

media = somaIdade/len(dadosPessoasLista)
print("A média de idade do grupo é:", media)

for pessoas in dadosPessoasLista:
    if pessoas["Idade"] > media:
        print("Pessoas com a idade acima da média:", pessoas["Nome"])

for mulheres in dadosPessoasLista:
    if mulheres["Sexo"] == "F".lower():
        print("Mulheres na lista:", mulheres["Nome"])