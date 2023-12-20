v = float(input("Digite o valor do produto:"))
desconto = v * 0.05  # 5% de desconto
valor_com_desconto = v - desconto
print(f"O produto custa R${v:.2f}, e o valor dele com 5% de desconto é: R${valor_com_desconto:.2f}")
