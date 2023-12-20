
def space():
    print("*"*50)
def main():

    print("Crie um programa que lea o nome de uma cidade e diga se ela começa ou não com o nome Santo")
    space()
    
    nome = str(input("Digite o nome de uma Cidade: "))
    space()

    print("Iremos verificar se sua Cidade digitada possui Santo no nome")
    space()

    print('Santo' in nome)
    space()

if __name__ == "__main__":
    main()