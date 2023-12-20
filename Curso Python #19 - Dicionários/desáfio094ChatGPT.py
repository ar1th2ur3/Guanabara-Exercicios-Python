class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

def display_menu():
    print("\nMenu:")
    print("1. Add a new person")
    print("2. Display statistics")
    print("3. Exit")

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

# Your existing code here...

dadosPessoasLista = list()

while True:
    display_menu()
    choice = get_valid_input("Enter your choice: ", input_type=str)

    if choice == "1":
        dadosPessoas = {}
        print(50 * "-=")
        dadosPessoas['Nome'] = get_valid_input("Digite o nome da pessoa, por gentileza: ")
        print(50 * "-=")
        dadosPessoas['Sexo'] = get_valid_input("Digite o sexo da pessoa, por gentileza [M/F]: ", input_type=str.upper)
        while dadosPessoas['Sexo'] not in ['M', 'F']:
            print("Invalid input. Please enter 'M' or 'F'.")
            dadosPessoas['Sexo'] = get_valid_input("Digite o sexo da pessoa, por gentileza [M/F]: ", input_type=str.upper)
        print(50 * "-=")
        dadosPessoas['Idade'] = get_valid_input("Digite a idade da pessoa, por gentileza: ", input_type=int)
        print(50 * "-=")

        dadosPessoasLista.append(dadosPessoas.copy())

    elif choice == "2":
        if not dadosPessoasLista:
            print("Nenhuma pessoa cadastrada ainda.")
        else:
            totalPessoas = len(dadosPessoasLista)
            somaIdade = sum(pessoa["Idade"] for pessoa in dadosPessoasLista)
            media = somaIdade / totalPessoas

            print(f"A) {totalPessoas} pessoas foram cadastradas")
            print("B) A média de idade do grupo é:", round(media, 2))

            print("C) Mulheres na lista:")
            for mulher in dadosPessoasLista:
                if mulher["Sexo"] == "F":
                    print("   ", mulher["Nome"])

            print("D) Pessoas com a idade acima da média:")
            for pessoa in dadosPessoasLista:
                if pessoa["Idade"] > media:
                    print("   ", pessoa["Nome"])


    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
