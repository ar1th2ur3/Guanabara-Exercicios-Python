def space():
    print("*" * 50)

def check_city_name(nome):
    if 'Santo' in nome:
        return True
    return False

def main():
    print("Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo")
    space()

    while True:
        nome = input("Digite o nome de uma cidade (ou digite 'q' para sair): ")
        if nome.lower() == 'q':
            break

        result = check_city_name(nome)
        if result:
            print(f"A cidade {nome} possui 'Santo' no nome.")
        else:
            print(f"A cidade {nome} não possui 'Santo' no nome.")
        space()

if __name__ == "__main__":
    main()
