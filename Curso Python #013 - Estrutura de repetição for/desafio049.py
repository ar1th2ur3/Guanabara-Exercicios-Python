def main():
    print("Refaça o desafio 009, mostrando a tabuada de um número que o usuário ecolher, só que agora, utilizando um laço for.")

    n = int(input("Digite o número da tabuada que você deseja: "))

    for c in range (1 , 10+1):
        x = n * c
        print(f" {n} * {c} = {x}")

if __name__ == "__main__":
    main()