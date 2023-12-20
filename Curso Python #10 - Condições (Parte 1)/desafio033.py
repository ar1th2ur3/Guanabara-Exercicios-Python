def VerificarNumero(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        mensagem = "O número n1 é o maior."
    elif n2 > n1 and n2 > n3:
        mensagem = "O número n2 é o maior."
    else:
        mensagem = "O número n3 é o maior."
    return mensagem

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    mensagem = VerificarNumero(n1, n2, n3)

    print(mensagem)

if __name__ == "__main__":
    main()
