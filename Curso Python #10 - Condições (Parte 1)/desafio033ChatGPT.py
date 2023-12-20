def VerificarNumeros(n1, n2, n3):
    numeros = [n1, n2, n3]
    
    # Ordena os números em ordem crescente
    numeros_crescente = sorted(numeros)
    
    # Ordena os números em ordem decrescente
    numeros_decrescente = sorted(numeros, reverse=True)
    
    maior_numero = numeros_decrescente[0]
    
    mensagem = f"Números em ordem crescente: {numeros_crescente}\n" \
               f"Números em ordem decrescente: {numeros_decrescente}\n" \
               f"O maior número é {maior_numero}."
    
    return mensagem

def main():
    print("Desafio 033: Desenvolva um programa que compare três números e determine qual deles é o maior.")
    
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    mensagem = VerificarNumeros(n1, n2, n3)

    print(mensagem)

if __name__ == "__main__":
    main()
