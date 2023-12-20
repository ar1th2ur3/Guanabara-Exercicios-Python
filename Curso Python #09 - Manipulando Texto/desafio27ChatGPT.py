def achar_primeiro_nome(nome_completo):
    """Retorna o primeiro nome a partir de um nome completo."""
    nome_split = nome_completo.split()
    if nome_split:
        return nome_split[0]
    else:
        return "Nome não encontrado"

def achar_ultimo_nome(nome_completo):
    """Retorna o último nome a partir de um nome completo."""
    nome_split = nome_completo.split()
    if nome_split:
        return nome_split[-1]
    else:
        return "Nome não encontrado"

def main():
    print("Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.")
    print("Exemplo: Ana Maria de Souza.")
    print("Primeiro nome = Ana")
    print("Último nome = Souza")

    nome_completo = input("Digite o seu nome completo: ")

    primeiro_nome = achar_primeiro_nome(nome_completo)
    ultimo_nome = achar_ultimo_nome(nome_completo)

    print(f"O seu primeiro nome é: {primeiro_nome}")
    print(f"O seu último nome é: {ultimo_nome}")

if __name__ == "__main__":
    main()
