def calcular_alistamento(idade, gênero):
    if idade < 18:
        falta = 18 - idade
        ano_alistamento = 2023 + falta
        return f"Faltam {falta} anos para o alistamento. Você deverá se alistar em {ano_alistamento}."

    elif idade == 18:
        return "Você precisa se alistar imediatamente."

    else:
        atraso = idade - 18
        ano_alistamento = 2023 - atraso

        if gênero == "masculino":
            mensagem = f"Você já passou do prazo de alistamento. Você está atrasado {atraso} anos."
            mensagem += f"Você deveria ter se alistado em {ano_alistamento}."
        elif gênero == "feminino":
            mensagem = f"O alistamento militar não é obrigatório para mulheres, mas é voluntário."
        else:
            mensagem = "Gênero não reconhecido. O alistamento pode variar."

        return mensagem

def main():
    try:
        idade = int(input("Digite a sua idade: "))
        gênero = input("Digite o seu gênero (masculino/feminino): ").lower()

        mensagem = calcular_alistamento(idade, gênero)
        print(mensagem)
    except ValueError:
        print("Erro: Insira uma idade válida.")

if __name__ == "__main__":
    main()
