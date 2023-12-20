def main():
    print("Programa que lê um número de 0 a 9999 e realiza várias operações com os dígitos.")

    numero = input("Digite um número: ")
    
    if not numero.isnumeric() or not 0 <= int(numero) <= 9999:
        print("Número inválido. Digite um número entre 0 e 9999.")
        return

    numeroSeparado = list(numero)

    print(f"Número digitado: {numero}")

    # Calcula a soma dos dígitos
    soma = sum(int(digito) for digito in numeroSeparado)
    print(f"Soma dos dígitos: {soma}")

    # Calcula o produto dos dígitos
    produto = 1
    for digito in numeroSeparado:
        produto *= int(digito)
    print(f"Produto dos dígitos: {produto}")

    # Verifica se o número é um palíndromo
    if numero == numero[::-1]:
        print("O número é um palíndromo.")
    else:
        print("O número não é um palíndromo.")

if __name__ == "__main":
    main()
