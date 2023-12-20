def escolhaGenero(genero):
    while genero != "m" and genero != "f":
        print("Escolha o gênero correto.")
        genero = input("Digite o gênero desejado (M/F): ").lower()
    if genero == "m":
        print(f"Obrigado por escolher o gênero: Masculino")
    else:
        print(f"Obrigado por escolher o gênero: Feminino")

def main():

    print("Faça um programa que leia o *sexo* de uma pessoa, mas só aceite os valores *M* ou *F*.")
    print("Caso esteja errado, peça a digitação novamente até ter um valor correto.")

    genero = input("Digite o gênero desejado (M/F): ").lower()

    escolhaGenero(genero)

print("Fim")

if __name__ == "__main__":
    main()