from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        print("Erro: O passo não pode ser zero.")
        return

    # Ajuste na lógica para incluir o fim mesmo quando o passo não o atinge exatamente
    if inicio <= fim:
        for i in range(inicio, fim + 1, passo):
            print(f"{i}", end=' ')
            sleep(0.5)
        
    else:
        for i in range(inicio, fim - 1 if passo > 0 else fim, -passo):
            print(f"{i}", end=' ')
            sleep(0.5)
        
# Exemplos de uso:
print("A) De 1 até 10, de 1 em 1.")
contador(1, 10, 1)
print(50 * "-=")
print("B) De 10 até 0, de 2 em 2.")
contador(10, 0, 2)
print(50 * "-=")
print("C) Uma contagem personalizada.")
print("Agora é a sua vez de escolher!")

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
