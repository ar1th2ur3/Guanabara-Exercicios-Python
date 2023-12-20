def main():
    try:
        idade = int(input("Digite a sua idade: "))

        if idade == 18:
            print("Você precisa se alistar imediatamente.")
        elif idade > 18:
            atraso = idade - 18
            print(f"Você já passou do prazo de alistamento. Você está atrasado {atraso} anos.")

            # Calcule o ano em que deveria ter se alistado
            ano_alistamento = 2023 - atraso
            print(f"Você deveria ter se alistado em {ano_alistamento}.")
        else:
            falta = 18 - idade
            print(f"Faltam {falta} anos para você se alistar.")

            # Calcule o ano em que deverá se alistar
            ano_alistamento = 2023 + falta
            print(f"Você deverá se alistar em {ano_alistamento}.")
    except ValueError:
        print("Erro: Insira uma idade válida.")

if __name__ == "__main__":
    main()
