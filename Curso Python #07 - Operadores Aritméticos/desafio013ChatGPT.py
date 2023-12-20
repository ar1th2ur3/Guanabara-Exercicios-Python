
def calcular_salario_com_acrescimo(salario, acrescimo_percentual):
    valor_acrescimo = salario * (acrescimo_percentual / 100)
    salario_final = salario + valor_acrescimo
    return salario_final

def main():
    print("Calculadora de acréscimo salarial")

    salario = float(input("Digite o salário do funcionário: "))
    acrescimo_percentual = 13  # 13% de acréscimo

    salario_final = calcular_salario_com_acrescimo(salario, acrescimo_percentual)

    print(f"O salário com {acrescimo_percentual}% de acréscimo é: R${salario_final:.2f}")

if __name__ == "__main__":
    main()
