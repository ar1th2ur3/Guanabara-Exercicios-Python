print("Desáfio 102: Crie um programa que tenha uma função fatorial() que receba dos parâmetros: o número a calcula e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.")

def fatorial(num, show=False):
    """Calcula o fatorial de um número.
    
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor fatorial de um número n."""
    
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f"{c} ", end="")
            else:
                print(f"{c} x ", end="")

    if show:
        print(f"= {f}")
    else:
        print(f"{f}")

    return f

n = int(input("Digite um número para calcular o fatorial: "))
fatorial(n, True)
