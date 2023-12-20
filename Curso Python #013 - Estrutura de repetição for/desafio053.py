print("Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.")

usuarioFrase = input("Digite uma frase: ").replace(" ", "")  # Remova os espaços da frase
usuarioFraseContrario = ""

# Use um loop for para inverter a frase
for i in range(len(usuarioFrase) - 1, -1, -1):
    usuarioFraseContrario += usuarioFrase[i]

# Verifique se a frase original (sem espaços) é igual à frase ao contrário (sem espaços)
if usuarioFrase == usuarioFraseContrario:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
