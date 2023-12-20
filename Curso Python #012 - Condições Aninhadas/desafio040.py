from random import randint

def calculoMedia(n1, n2):
    media = (n1 + n2) / 2
    if media < 5:
        return f"Você foi reprovado. Média: {media:.1f}"
    elif 5 <= media <= 7:
        return f"Você está de recuperação. Média: {media:.1f}"
    else:
        return f"Você foi aprovado. Média: {media:.1f}"

def main():
    print("Crie um programa que leia duas notas de um aluno e calcule sua média,")
    print("mostrando uma mensagem no final, de acordo com a média atingida:")
    print("Média abaixo de 5.0: REPROVADO.")
    print("Média entre 5.0 e 7.0: RECUPERAÇÃO.")
    print("Média 7.0 ou superior: APROVADO.")

    n1 = randint(1, 10)
    n2 = randint(1, 10)

    mensagem = calculoMedia(n1, n2)

    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(mensagem)

if __name__ == "__main__":
    main()
