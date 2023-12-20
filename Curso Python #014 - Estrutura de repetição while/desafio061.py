print("Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.")

a1 = float(input("Primeiro termo: "))
r = float(input("Razão: "))

n = 1  # Inicializa o contador n com 1

while n <= 10:  # Enquanto n for menor ou igual a 10
    an = a1 + (n - 1) * r
    print(f'O {n}º termo da PA é {an}')
    n += 1  # Incrementa o contador para passar para o próximo termo
