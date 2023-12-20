
def main():
    print("Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiusculas, Qunatas letras ao todo(sem considerar espaços), Quantas letras tem o primeiro nome")

    nome = input("Digite o seu nome, por gentileza: ")

    nome = nome.strip()

    print(f"O seu nome, em letras maiúsculas, é: {nome.upper()}")

    print(f"O seu nome: {nome} tem {len(nome)} letras")  

    nome = nome.split()

    print(f"O primeiro nome de {nome} é {nome[0]}")


if __name__ == "__main__":
    main()