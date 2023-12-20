def main():
    print("Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas, Quantas letras ao todo (sem considerar espaços), Quantas letras tem o primeiro nome, e o último nome separado.")

    nome = input("Digite o seu nome, por gentileza: ")

    nome = nome.strip()

    if nome.isalpha():  # Verifica se o nome contém apenas letras
        print(f"O seu nome, em letras maiúsculas, é: {nome.upper()}")
        print(f"O seu nome: {nome} tem {len(nome)} letras.")

        nome_parts = nome.split()
        if len(nome_parts) >= 2:  # Verifica se o nome é composto por pelo menos dois nomes
            primeiro_nome = nome_parts[0]
            ultimo_nome = nome_parts[-1]
            print(f"O primeiro nome é: {primeiro_nome}")
            print(f"O último nome é: {ultimo_nome}")
        else:
            print("Não foi possível separar o primeiro e o último nome, pois o nome não é composto por pelo menos dois nomes.")
    else:
        print("Nome inválido. Certifique-se de que contém apenas letras.")

if __name__ == "__main__":
    main()
