def main():
    print("Crie um programa que leia a idade e o sexo de várias pessoas.")
    print("A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:")
    print("A) Quantas pessoas têm mais de 18 anos?")
    print("B) Quantos homens foram cadastrados?")
    print("C) Quantas mulheres têm menos de 20 anos?")
    print(50 * "*")

    maiorIdade = 0
    menorIdadeMulher = 0
    homensCadastrados = 0

    while True:
        print("Olá, preencha as informações abaixo:")
        idade = int(input("Qual é a idade da pessoa? "))
        sexo = input("Qual é o sexo da pessoa [M/F]? ").lower()

        if idade > 18:
            maiorIdade += 1
        if sexo == "m":
            homensCadastrados += 1
        if sexo == "f" and idade < 20:
            menorIdadeMulher += 1

        escolha = input("Você quer continuar? (sim/não) ").lower()

        if escolha != "sim":
            break

    print(f"Pessoas maior de idade: {maiorIdade}")
    print(50 * "*")
    print(f"Homens cadastrados: {homensCadastrados}")
    print(50 * "*")
    print(f"Mulheres com menos de 20 anos: {menorIdadeMulher}")
    print(50 * "*")

if __name__ == "__main__":
    main()
