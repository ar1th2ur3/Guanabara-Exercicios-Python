vogais = "aeiou"
words = ("gato", "cachorro", "mouse", "teclado", "livro", "janela", "carro", "mesa", "cadeira", "sol", "lua", "arvore", "futebol", "bicicleta", "telefone", "computador", "porta", "chave", "amigo", "rio")


for word in words:
    vowels = ""
    for letter in word:
        if letter in vogais:
            vowels += letter
    print(f"A palavra {word} contém as vogais: {vowels}")
