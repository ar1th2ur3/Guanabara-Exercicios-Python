from random import randint

def verificaçãoMaior(números):
    if not números:
        return "A lista está vazia."

    maior = max(números)
    menor = min(números)
    média = sum(números) / len(números)

    mensagem = f"O maior número na lista é: {maior}\n"
    mensagem += f"O menor número na lista é: {menor}\n"
    mensagem += f"A média dos números na lista é: {média:.2f}\n"
    mensagem += "Lista de números:"
    
    for num in números:
        mensagem += f" {num}"

    return mensagem

def main():
    try:
        n = int(input("Quantos números você deseja comparar? "))
        números = [randint(1, 100) for _ in range(n)]
    except ValueError:
        print("Erro: Insira um número válido para a quantidade de números.")
        return

    message = verificaçãoMaior(números)
    print(message)

if __name__ == "__main__":
    main()
