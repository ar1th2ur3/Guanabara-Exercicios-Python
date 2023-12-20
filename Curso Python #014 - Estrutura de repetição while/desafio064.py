print("Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.")
print("No final, mostre quantos números foram digitados e qual foi a soma entre eles.")

soma = 0
cont = 0

while True:
    n = int(input("Digite um número: "))
    
    if n == 999:
        print("Você digitou 999. Encerrando o programa.")
        break
    
    cont += 1
    soma += n

print(f"Foram digitados {cont} números e a soma entre eles é {soma}.")
