def calcularSalarioFuncionario(salario, acrescimoPorcentagem):
    valorAcrecimo = salario * (acrescimoPorcentagem / 100)
    salarioFinal = salario + valorAcrecimo
    return salarioFinal

def main():
    salario = float(input("Digite o seu salário: "))
    acrescimoPorcentagem = 15  # 15% de acréscimo

    salarioFinal = calcularSalarioFuncionario(salario, acrescimoPorcentagem)

    print(f"O salário com {acrescimoPorcentagem}% de acréscimo é: R${salarioFinal:.2f}")

if __name__ == "__main__":
    main()
