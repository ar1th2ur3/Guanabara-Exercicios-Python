print("Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.")

n = soma = 0
while True:
    n = int(input("Digite um número: "))

    if n == 999:
        
        break
    soma += n

print(f"a soma entre eles foi:{soma}")