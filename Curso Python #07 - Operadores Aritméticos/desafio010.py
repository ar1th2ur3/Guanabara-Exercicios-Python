def calcular_dólares(v, taxaDolar = 3.27):
    dolar = v / taxaDolar
    return dolar

v = float(input("Digite o total de dinheiro que você possui:"))

quantidadeDolar = calcular_dólares(v)
print(f"Você pode comprar {quantidadeDolar:.2f} dólares")
