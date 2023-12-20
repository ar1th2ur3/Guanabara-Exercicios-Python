import math

print("Programa para calcular o fatorial de um número inteiro positivo.")

try:
    n = int(input("Digite um número para calcular o fatorial: "))
    
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
    
    # Verificar se o número é maior que 170, pois fatoriais de números maiores que 170 não cabem em um float.
    if n > 170:
        raise ValueError("O número é muito grande para calcular o fatorial com precisão usando um float.")
    
    fatorial = math.factorial(n)  # Usando a função math.factorial para calcular o fatorial
    
    print(f"O fatorial de {n} é: {fatorial}")
    
except ValueError as e:
    print(f"Erro: {e}")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
