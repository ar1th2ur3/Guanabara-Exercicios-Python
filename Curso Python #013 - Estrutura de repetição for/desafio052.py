def main():
    print("Este programa verifica se um número inteiro é primo ou não.")

    nUsuario = int(input("Digite um número: "))
    is_primo = True

    if nUsuario <= 1:
        is_primo = False
    else:
        for count in range(2, int(nUsuario**0.5) + 1):
            if nUsuario % count == 0:
                is_primo = False
                break

    if is_primo:
        print(f"O número {nUsuario} é primo.")
    else:
        print(f"O número {nUsuario} não é primo.")

if __name__ == "__main__":
    main()
