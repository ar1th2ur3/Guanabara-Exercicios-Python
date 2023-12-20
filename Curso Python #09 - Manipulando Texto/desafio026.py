def main():
    print("Faça um programa que leia uma frase pelo teclado e mostre: 1- Quantas vezes aparece a letra A, Em que posição ela aparece a primeira vez, 3- Em que posição ela aparece a última vez.")

    frase = str(input("Digite uma frase: "))

    #Quantas vezes a letra A aparece
    print("Na sua frase a letra A aparece:",frase.count("a"),"vezes")

    #Em que posição ela irá aparecer pela primeira vez
    print("A primeira vez que a letra aparece é no indice:",frase.find("a"))

    #Em que posição irá aparecer pela última vez.
    print("A última vez que a letra A aparece é no indice:",frase.rfind("a"))

if __name__ == "__main__":
    main()